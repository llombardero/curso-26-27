#!/usr/bin/env python3
"""Auditoría reproducible de la simplificación global de MiniJarvis."""
from __future__ import annotations
import hashlib, json, re, subprocess
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote
from zipfile import ZipFile

ROOT=Path(__file__).resolve().parent

def files(base): return [p for p in base.rglob('*') if p.is_file()]
def hashes(base):
    out=defaultdict(list)
    for p in files(base): out[hashlib.sha256(p.read_bytes()).hexdigest()].append(str(p.relative_to(base)))
    return [v for v in out.values() if len(v)>1]

def broken_links():
    broken=[]
    pat=re.compile(r'(?<!!)\[[^]]*\]\(([^)]+)\)')
    for p in ROOT.rglob('*.md'):
        if any(x in p.parts for x in {'.git','.obsidian','99-ARCHIVO-NO-DISTRIBUIDO'}): continue
        for raw in pat.findall(p.read_text(encoding='utf-8',errors='replace')):
            raw=raw.strip().split()[0].strip('<>')
            if not raw or raw.startswith(('#','http://','https://','mailto:')): continue
            target=(p.parent/unquote(raw.split('#',1)[0])).resolve()
            if not target.exists(): broken.append(f'{p.relative_to(ROOT)} -> {raw}')
    return broken

def curricular_tokens_current():
    text='\n'.join(p.read_text(encoding='utf-8',errors='ignore') for p in ROOT.rglob('*.md') if '.git' not in p.parts)
    return sorted(set(re.findall(r'\b(?:RA\d+|CE\d+(?:\.[a-z])?)\b',text,re.I)))
def curricular_tokens_head():
    paths=subprocess.check_output(['git','ls-tree','-r','--name-only','HEAD'],cwd=ROOT,text=True).splitlines()
    chunks=[]
    for path in paths:
        if path.endswith('.md'):
            chunks.append(subprocess.check_output(['git','show',f'HEAD:{path}'],cwd=ROOT,text=True,errors='ignore'))
    return sorted(set(re.findall(r'\b(?:RA\d+|CE\d+(?:\.[a-z])?)\b','\n'.join(chunks),re.I)))

def secrets():
    pat=re.compile(r'(?i)(?:ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)')
    hits=[]
    for p in ROOT.rglob('*'):
        if not p.is_file() or any(x in p.parts for x in {'.git','.obsidian','__pycache__'}): continue
        if p.suffix.lower() not in {'.md','.py','.txt','.html','.json','.yml','.yaml','.env'}: continue
        text=p.read_text(encoding='utf-8',errors='ignore')
        if pat.search(text): hits.append(str(p.relative_to(ROOT)))
    return hits

def zip_errors():
    errors=[]
    for p in ROOT.glob('Minijarvis-*.zip'):
        with ZipFile(p) as z:
            bad=z.testzip()
            if bad: errors.append(f'{p.name}: {bad}')
    return errors

def main():
    current=curricular_tokens_current(); baseline=curricular_tokens_head()
    report={
      'counts': {name:len(files(ROOT/name)) for name in ['01-ALUMNADO','01-ALUMNADO-HTML','02-PROFESORADO','04-DRIVE-5-EQUIPOS','05-PAQUETE-MOODLE']},
      'hito_template_dirs': len(list((ROOT/'01-ALUMNADO/02-HITOS').glob('*/plantillas'))),
      'session_admin_blocks': sum('## Registro breve' in p.read_text(encoding='utf-8') or '## Evidencia mínima antes de salir' in p.read_text(encoding='utf-8') for p in (ROOT/'01-ALUMNADO/03-SESIONES').rglob('*.md')),
      'drive_duplicate_groups': hashes(ROOT/'04-DRIVE-5-EQUIPOS'),
      'moodle_duplicate_groups': hashes(ROOT/'05-PAQUETE-MOODLE'),
      'broken_markdown_links': broken_links(),
      'curricular_tokens_baseline': baseline,
      'curricular_tokens_current': current,
      'curricular_tokens_preserved': baseline==current,
      'secret_hits': secrets(),
      'zip_errors': zip_errors(),
      'zip_count': len(list(ROOT.glob('Minijarvis-*.zip'))),
      'private_example_files_in_moodle': [str(p.relative_to(ROOT)) for p in (ROOT/'05-PAQUETE-MOODLE').rglob('*') if p.is_file() and 'laura' in p.name.lower()],
    }
    print(json.dumps(report,ensure_ascii=False,indent=2))
    failed=[]
    if report['hito_template_dirs']: failed.append('persisten plantillas por hito')
    if report['session_admin_blocks']: failed.append('persisten bloques administrativos de sesión')
    if report['broken_markdown_links']: failed.append('hay enlaces Markdown rotos')
    if not report['curricular_tokens_preserved']: failed.append('no se preservó el conjunto RA/CE')
    if report['secret_hits']: failed.append('posibles secretos')
    if report['zip_errors'] or report['zip_count']!=7: failed.append('ZIP inválidos o incompletos')
    if report['private_example_files_in_moodle']: failed.append('ejemplos privados en Moodle')
    raise SystemExit('; '.join(failed) if failed else 0)
if __name__=='__main__': main()

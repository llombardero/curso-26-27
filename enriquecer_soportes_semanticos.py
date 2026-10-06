"""Extractive supports after composition; no source/planner changes or clock allocation.

Integration: frames = enrich(renderer_module, session, frames); then
renderer_module.SEMANTIC_LAYOUTS.update(layouts(renderer_module)).
All mergers stay inside one SlideSpec; origins refer to actual raw expansion.
"""
from dataclasses import replace
import re
import componer_presentaciones_semanticas as composition


def _paragraphs(unit):
    return list(dict.fromkeys(unit.visible_content + unit.presenter_content))


def _archive(frame):
    notes = list(frame.notes)
    for unit in frame.units:
        for original in _paragraphs(unit):
            note = ('visible_detail', unit.source_refs[0].heading, original)
            if note not in notes:
                notes.append(note)
    return replace(frame, notes=notes)


def _criterion_height(r, atoms):
    return sum(max(r.rendered_height(a.alternative, 5.75, 24) + .08 +
                       r.rendered_height(a.text, 5.75, 24) for a in atoms[i:i + 2]) + .12
               for i in range(0, len(atoms), 2))


def normalize_presentation_atom(atom, java_literals):
    """Keep conceptual notation out of Java boxes and reconcile literal evidence."""
    changes = {}
    if atom.language != 'java' and '->' in atom.text:
        corrected = atom.text.replace('->', '→')
        changes[atom.text] = corrected
        if atom.kind == 'code' and atom.language == 'text':
            return replace(atom, text=corrected, kind='prose', language=''), changes
        return replace(atom, text=corrected), changes

    lines = atom.text.splitlines()
    assignments = bool(lines) and all(re.fullmatch(r'[A-Za-z_$][\w$]*\s*=\s*-?\d+[.;]?', line) for line in lines)
    if atom.kind == 'cards' and assignments:
        corrected_lines = [line[:-1] + ';' if line.endswith('.') else line if line.endswith(';') else line + ';'
                           for line in lines]
        for original, corrected in zip(lines, corrected_lines):
            if original != corrected:
                changes[original] = corrected
        return replace(atom, text='\n'.join(corrected_lines), kind='code'), changes

    corrected_lines = []
    for line in lines:
        corrected = line
        output = re.fullmatch(r'(Salida (?:esperada|obtenida):\s*)(.+?)(\.)?', line)
        if output and output[2] in java_literals and output[3]:
            corrected = output[1] + output[2]
        if corrected.lstrip().startswith('¿'):
            corrected = corrected.rstrip(';')
            corrected = corrected.replace(
                '¿qué comportamiento visible aporta cada línea?',
                '¿qué prepara cada línea, qué efecto tiene y cuál produce salida?',
            )
        if corrected != line:
            changes[line] = corrected
        corrected_lines.append(corrected)
    return replace(atom, text='\n'.join(corrected_lines)), changes


def enrich(r, session, frames):
    """Derive legible, source-anchored views; retain full originals in notes."""
    if frames and all(frame.relations.get('source_supports_enriched') for frame in frames):
        return frames
    result = list(frames)
    # Sibling criteria must carry the same explicit README parent, not merely
    # coincidentally share titles or a session number.
    index = 0
    while index < len(result):
        first = result[index]
        if first.kind in {'title', 'readme_support'} or not first.units:
            index += 1
            continue
        end = index + 1
        while end < len(result) and result[end].plan_index == first.plan_index:
            end += 1
        group = result[index:end]
        wanted = ('Qué hace', 'Qué límites tiene', 'Cómo se ejecuta', 'Qué pruebas demuestran que funciona')
        criteria = []
        parents = set()
        for heading in wanted:
            candidates = [(f, u) for f in group for u in f.units
                          if u.source_refs[0].heading == heading
                          and any('README' in ref.heading for ref in u.source_refs[1:])]
            if len(candidates) != 1:
                break
            frame, unit = candidates[0]
            parents.update(ref.heading for ref in unit.source_refs[1:] if 'README' in ref.heading)
            paragraphs = [r.prose_text(p) for p in _paragraphs(unit)
                          if not r.fenced_body(p) and not p.startswith('>')]
            if not paragraphs:
                break
            sentences = re.split(r'(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚ])', paragraphs[0])
            extract = sentences[-1] if heading in wanted[2:] else sentences[0]
            indices = tuple(dict.fromkeys(i for a in frame.atoms for i in a.source_indices))
            criteria.append(r.RenderAtom(extract, indices, 'support_criterion', alternative=heading))
        if len(criteria) == 4 and len(parents) == 1 and _criterion_height(r, criteria) <= 5.29:
            parent = next(iter(parents))
            parts = [f for f in group if any(u.source_refs[0].heading in (*wanted, parent) for u in f.units)]
            # Never move unrelated units to notes as a side effect.
            if all(all(u.source_refs[0].heading in (*wanted, parent) or not u.visible_content for u in f.units) for f in parts):
                merged = composition.combine([_archive(f) for f in parts], title=parent,
                                             kind='readme_support', atoms=criteria)
                positions = [result.index(f) for f in parts]
                for pos in reversed(positions):
                    del result[pos]
                result.insert(positions[0], merged)
                end = index + 1
        index = end
    enriched = []
    for frame in result:
        if frame.kind in {'title', 'classification', 'parallel', 'readme_support', 'source_support'}:
            enriched.append(frame)
            continue
        atoms = list(frame.atoms)
        columns = None
        for unit in frame.units:
            raw = _paragraphs(unit)
            # Restore the external user's source introduction, including the
            # sentence lost by project_item's trailing-colon filter.
            introduction = next((r.prose_text(p) for p in raw
                                 if 'sin explicación oral previa' in p), None)
            if introduction and any(a.kind == 'cards' for a in atoms):
                questions = [a for f in result if f.plan_index == frame.plan_index
                             and unit in f.units for a in f.atoms if 'otra persona' in a.text and '¿' in a.text]
                context = [r.RenderAtom(introduction, ())] + questions
                context += [a for a in atoms if a.kind != 'cards']
                steps = [a for a in atoms if a.kind == 'cards']
                columns = (list(range(1, len(context))), list(range(len(context), len(context) + len(steps))))
                atoms = context + steps
            # Source-ordered list markers, not a solved classification. Only
            # the immediately preceding explicit marker labels a list.
            if any('fuera del alcance' in p.lower() for p in raw):
                for n, original in enumerate(raw):
                    if n == 0 or not re.match(r'\s*(?:[-*]|\d+\.)\s', original):
                        continue
                    marker = r.prose_text(raw[n - 1])
                    if not marker.endswith(':'):
                        continue
                    lines = r.prose_text(original).splitlines()
                    matching = [a for a in atoms if a.kind == 'cards'
                                and all(line in lines for line in a.text.splitlines())]
                    if matching:
                        if not any(a.kind == 'boundary' for a in atoms):
                            atoms.insert(atoms.index(matching[0]), r.RenderAtom(marker, (), 'boundary'))
                        if 'fuera del alcance' in marker.lower():
                            # Keep the explicit future-vs-current distinction,
                            # not a colour code that learners must infer.
                            for p in raw[n + 1:]:
                                if 'contenidos posteriores' in p:
                                    full = r.prose_text(p)
                                    atoms = [replace(a, text=full) if a.text in full and a.kind == 'prose' else a for a in atoms]
                                    break
            if 'reproducible_test' in unit.relations and any('Entrada usada:' in a.text and 'Salida obtenida:' in a.text for a in atoms):
                chain = next((a for f in result if f.plan_index == frame.plan_index and unit in f.units
                              for a in f.atoms if 'entrada → resultado esperado → resultado obtenido → qué demuestra' in a.text), None)
                if chain and not any(chain.text == a.text for a in atoms):
                    atoms.insert(0, replace(chain, reference=True))
        # Promote, verbatim, the source's prepare/official-delivery distinction.
        for atom in list(atoms):
            if atom.kind != 'cards':
                continue
            for line in atom.text.splitlines():
                public_or_internal = r'(?:S\d+|H(?:[0-7]|F)\.\d+)'
                if (re.search(rf'\b{public_or_internal} prepara\b', line)
                        and re.search(rf'\b{public_or_internal} realiza la entrega oficial\b', line)):
                    atoms.remove(atom)
                    remainder = [t for t in atom.text.splitlines() if t != line]
                    atoms.insert(0, r.RenderAtom(line, atom.source_indices, 'boundary'))
                    if remainder:
                        atoms.append(replace(atom, text='\n'.join(remainder)))
        if atoms != frame.atoms:
            frame = _archive(replace(frame, atoms=atoms, kind='source_support',
                                     relations={**frame.relations, **({'support_columns': columns} if columns else {})}))
        if frame.kind == 'source_support' and not columns:
            # Adding a mandatory source label may consume the space formerly
            # used by a secondary paragraph. Give that paragraph its own view,
            # never silently demote an instruction to presenter notes.
            height = sum((r.cards_geometry(a.text.splitlines(), rendered=True)[1]
                          if a.kind == 'cards' else r.rendered_height(a.text, size=22 if a.kind == 'code' else 24)) + .1
                         for a in frame.atoms)
            if height > 5.29 and any(a.kind == 'cards' for a in frame.atoms):
                core = [a for a in frame.atoms if a.kind in {'cards', 'boundary'}]
                secondary = [a for a in frame.atoms if a not in core]
                enriched.append(replace(frame, atoms=core))
                if secondary:
                    enriched.append(replace(frame, atoms=secondary))
                continue
        enriched.append(frame)
    java_literals = {
        literal for frame in enriched for atom in frame.atoms
        if atom.kind == 'code' and atom.language == 'java'
        for literal in re.findall(r'"([^"\\]*(?:\\.[^"\\]*)*)"', atom.text)
    }
    normalized = []
    for frame in enriched:
        atoms = []
        changes = {}
        for atom in frame.atoms:
            corrected, atom_changes = normalize_presentation_atom(atom, java_literals)
            atoms.append(corrected)
            changes.update(atom_changes)
        readme_tests = next((atom for atom in atoms if atom.language == 'markdown'
                             and atom.text.startswith('## Pruebas')
                             and 'Entrada usada:' not in atom.text), None)
        if readme_tests and not any(atom.text.startswith('ESTRUCTURA INICIAL') for atom in atoms):
            label = r.RenderAtom(
                'ESTRUCTURA INICIAL · completa después cada prueba: entrada → esperado → obtenido → significado.',
                readme_tests.source_indices, 'boundary',
            )
            atoms.insert(atoms.index(readme_tests), label)
        relations = dict(frame.relations)
        if changes:
            relations['presentation_normalizations'] = {
                **relations.get('presentation_normalizations', {}), **changes,
            }
        normalized.append(replace(frame, atoms=atoms, relations=relations))
    fitted = []
    for frame in normalized:
        start = r.composition.frame_start(r, frame)
        height = sum(r.composition.physical_height(r, atom, frame.recognition) + .1
                     for atom in frame.atoms)
        splittable = {
            'concept', 'focus', 'code', 'prediction', 'linked_prediction', 'contrast',
            'activity', 'check', 'closure', 'recognition', 'source_support', 'readme_support',
        }
        if frame.kind in splittable and start + height > 6.84:
            fitted.extend(r.composition.conservative_partition(r, [frame]))
        else:
            fitted.append(frame)
    return [replace(frame, relations={**frame.relations, 'source_supports_enriched': True})
            for frame in fitted]


def render_readme_support(r, prs, session, frame):
    slide = r.semantic_base(prs, session, frame)
    y = r.frame_content_top(frame, 1.55)
    for start in range(0, len(frame.atoms), 2):
        bottom = y
        for column, atom in enumerate(frame.atoms[start:start + 2]):
            x = .7 + column * 6.15
            label_height = r.rendered_height(atom.alternative, 5.75, 24)
            height = r.rendered_height(atom.text, 5.75, 24)
            if y + label_height + .08 + height > 6.84:
                raise r.RepresentationError('Criterios README no caben sin reducir tipografía')
            r.text_box(slide, 'Soporte identidad', atom.alternative, x, y, 5.75, label_height,
                       size=24, bold=True, color=r.ACCENT)
            box = r.text_box(slide, 'Soporte criterio fuente', atom.text, x, y + label_height + .08,
                             5.75, height, size=24)
            box.fill.solid()
            box.fill.fore_color.rgb = r.WHITE
            bottom = max(bottom, y + label_height + .08 + height)
        y = bottom + .12
    return slide


def render_source_support(r, prs, session, frame):
    slide = r.semantic_base(prs, session, frame)
    columns = frame.relations.get('support_columns')
    lanes = [(frame.atoms, .7, 11.9)] if not columns else [
        ([frame.atoms[i] for i in indices], .7 + n * 6.15, 5.75)
        for n, indices in enumerate(columns)]
    top = r.frame_content_top(frame, 1.55)
    if columns:
        header = frame.atoms[0]
        height = r.rendered_height(header.text, 11.9, 24)
        r.text_box(slide, 'Soporte condición fuente', header.text, .7, top, 11.9, height,
                   size=24, bold=True)
        top += height + .10
    for atoms, x, width in lanes:
        y = top
        for atom in atoms:
            if atom.kind == 'cards' and not columns:
                y += r.render_atom(slide, atom, y, frame.recognition) + .10
                continue
            size = 22 if atom.kind == 'code' else 24
            height = r.rendered_height(atom.text, width, size)
            if y + height > 6.84:
                raise r.RepresentationError('Referente e instrucciones fuente no caben sin reducir tipografía')
            r.text_box(slide, 'Soporte fuente', atom.text, x, y, width, height, size=size,
                       bold=atom.kind == 'boundary', code=atom.kind == 'code',
                       color=r.ACCENT if atom.kind == 'boundary' else r.INK)
            y += height + .10
    return slide


def layouts(r):
    """Explicit registration: no import-time mutation of the renderer."""
    return {
        'readme_support': lambda prs, session, frame: render_readme_support(r, prs, session, frame),
        'source_support': lambda prs, session, frame: render_source_support(r, prs, session, frame),
    }

#!/usr/bin/env python3
"""Regenera los ejemplos privados de Laura con la arquitectura mínima del curso.

Los ejemplos son material docente privado y se publican de forma diferida. Hay un
único diario individual y un único Scrum de equipo, ambos evolutivos; Moodle
recibe una entrega mínima por hito; los Sites solo aparecen en C1, C2 y HF.
"""
from __future__ import annotations

import base64
import shutil
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXAMPLES = ROOT / "03-EJEMPLOS-LAURA-PRIVADOS"

HITOS = {
    "h0-torre-papel": ("H0", "Torre de papel y Scrum", "Organizar un sprint y comprobar una torre estable.", "La base inicial era estrecha; el equipo decidió ensancharla antes de ganar altura.", "Torre estable durante 10 segundos, backlog y retrospectiva actualizados.", "No aplica"),
    "h1-primer-asistente": ("H1", "Primer asistente por consola", "Crear y ejecutar la primera versión básica de MiniJarvis.", "Se mantuvo el alcance sin menú ni bucles para poder explicar cada línea.", "El programa saluda, solicita el nombre y termina sin errores.", "h1-entrega"),
    "h2-decisiones-depuracion": ("H2", "Decisiones y depuración", "Añadir menú, repetición, decisiones y salida controlada.", "Se corrigió la comparación de textos y se documentó una depuración con breakpoint.", "El menú responde a casos previstos y termina de forma controlada.", "h2-entrega"),
    "h3-memoria-colecciones": ("H3", "Memoria y colecciones", "Guardar y consultar recuerdos durante una ejecución.", "Se eligió una lista y se añadió tratamiento explícito de memoria vacía.", "Los recuerdos permanecen disponibles hasta cerrar el programa.", "h3-entrega"),
    "h4-agente-orientado-objetos": ("H4", "Agente orientado a objetos", "Separar responsabilidades mediante objetos.", "Main inicia, Agent coordina y Memory conserva recuerdos.", "El comportamiento anterior se conserva con un diseño más claro.", "h4-entrega"),
    "h5-extensible-clean-code-patrones": ("H5", "Extensibilidad, código limpio y patrones", "Añadir herramientas con bajo impacto y refactorizar sin romper.", "Se aplicó un Command simplificado mediante Tool sin introducir sobreingeniería.", "Las herramientas comparten contrato y las pruebas de regresión pasan.", "h5-entrega"),
    "h6-persistente-trazable": ("H6", "Persistencia y trazabilidad", "Conservar memoria e historial entre ejecuciones.", "Se usaron rutas relativas, errores controlados y datos ficticios.", "La memoria persiste y los errores de fichero dejan un estado seguro.", "h6-entrega"),
    "h7-integracion-ia-responsable": ("H7", "Integración responsable de IA", "Incorporar una ayuda simulada con límites y validación humana.", "Toda respuesta se presenta como propuesta y requiere validación humana.", "La simulación rechaza datos sensibles y registra la validación.", "h7-entrega"),
    "hf-presentacion-final-recuperacion-mejora": ("HF", "Presentación final, recuperación y mejora", "Demostrar la evolución de MiniJarvis y defender decisiones.", "Cada afirmación se enlaza con una versión estable y una prueba observable.", "La demostración es reproducible y Laura explica su aportación.", "hf-final"),
}


def clean_legacy() -> None:
    """Elimina únicamente la documentación antigua generada, no el código."""
    for folder in HITOS:
        hito = EXAMPLES / folder
        if not hito.is_dir():
            raise RuntimeError(f"No existe el hito {hito}")
        for name in ("docs", "evidencias-digitales"):
            shutil.rmtree(hito / name, ignore_errors=True)
        for path in hito.glob("*.md"):
            path.unlink()
    for name in ("FUENTES-CURSO", "ENTREGAS-MOODLE", "PORTFOLIOS-PERIODICOS"):
        shutil.rmtree(EXAMPLES / name, ignore_errors=True)


# Los libros canónicos se conservan como OOXML comprimido: reserializarlos con
# openpyxl cambia el paquete ZIP aunque las celdas coincidan y rompe el contrato
# de reproducibilidad byte a byte exigido para los ejemplos privados.
DIARY_XLSX = (
    b"c-"
    b"oCv1zZ$+*Iv2>$t5I~R$M|Pr8}ghmR?{NY1pMh>Fy5c?iLW~k}g3>5u`;z5D@&(d*7e0eD{98Z~Dyq&oeV;PRx1Kl+e&g0RR9tz{^0!@Q@Dm;nua(gaQB%Uh"
    b"my(I9=_Xtj+B0t-)@#HVqRJD&1T}7~^HSb*w5hB$LH<f%@d{>NRk&xCZlUs60XQfi!gLYT>#yru^sORYhV$Uv1=0f<%E%xV20eL6rrgFZ2AIclQ-_tCF0*s$"
    b"3l_BFyUU7#3S%NJVJ&y2G*Rg_wAA()Z@#n}mV_zQ+a+=6&vZ2HYEvNh4o)`f;UhKQ3seH>0uG1R}=wm3EG~Oc;Zb%Q#g<B7Tc!?C`bjfDA(ccm=Zh1C;Zc|G"
    b"r&`2n2BuzUnwV5rgNSipq60ud#n?Y-Gq%bKg}pn2yPjnM|WlG8q+lL4V|VK*;0+30r<qeGX9j!z$d~25?nW06-"
    b"WI03i6wD$WRZ8w=;3Hd)smic04qy(AmD2zn;W8x=$u83RI2jSS~PSb=`#)aDuNTeCV8!_eGw*-"
    b"TrB+oK{G&UB&yk3>)PV_mIUTevAB`5}t=f)8bEOCyX7&Mf4zvS=^7H!2lhzbHWD&%Qxih~~jI-"
    b"g}cGi|VFx=Xoo5+q5m94GxQiHBY7+w8L`I(zMlU7Yk#_8*;LB`TCG+(*_YkaGu~G^Y+13HOfe+A_zN!YDRZ;RAVSYMS`)OW`8KKG`f*?bprIjFxvVy<jw<+F"
    b"a2^s#t5_~?WdJdkux)joegB83f8w8G<vF*D=UVJts*kWE=ODy63J!-"
    b"+`qw$W{X>ZJEez6*x+oiJ?B<_(`wc6rP=23+??e5=GhdmMAe6Vpe0+P2gbec9QHtOg<%=G`U@j-"
    b"gc6Rjlm1)9vvs!h_K0okLH1rnk+X6SW3W{h>H#Pw09|^%bSJ#@Uf%j-bqeZQGTC1GE>;i!OtQ0mSz{2N{U^SDoNt18Vk-ygbVJ6fR;2y}blMH<=A7YPx8}BA"
    b")^@+8^TBOe*=GMn9l|9ifQ=flCXFkZ!bmZACU)H1eNJPV|K1RL!F2deA5Aj~7o7?dEM`z}qm#j5R5uOeKX#-"
    b"hA;>e&8>p&AUPA6BuQG6+YA9jrN3~lSOvJjt4dg+eo*p0?H$>qQfUG#u*5kyHxD6yReD-"
    b"(p6YNZpV1ce+<m<0tp<xKhiB}`X53HzYjd5WPVtU_hn@1ecV>?vS_Yo1%dXh@x`o$5&)NDQWJdzD`-"
    b"LEyc!W6qi`P1_<+r8lOXaK<Bbug0r<#`CWg{{S3Tkc=}r!%kek&Ecs|Mp`%t?uFH=FEsz>xY8&>e2;5Df&Zgq=uHOR`Z+Vi0vj7=dn^8$A(kG_Z&H^2-"
    b"(rbq~+5b(JP!uP`ms&@*l~5QILT-yLlr+lkYOHqtFzgcN(ipqoLA<F=O9i|L7EYTRGuPau9=mK)&t^nBa%t1esL%nz)VBkVv%^k#)y6`18Cl*)aCthNFj!>>"
    b"m`#@lZ(SO*)EeKIA?59?v-mLwy7dT6uBEH7^$9@Au5K#EXT9_bV3a$L-"
    b"1DiWDktJ4(Cb4Y;meKy)J?=|N><J>Tcm)kf2C?82aquO53<6@7WKEA;fQaEl0B_?@kvc-"
    b"rPDI&LoVi%jiN)&n!1cbYZmyN6dkmrcwS=1NI_aN75o3a-WO(M_Yx|5|M4=kX{eW_oz<@E#>xtBcK-rXzfm?|vz_dY{j$u&ne#!Kzb9v<Lda6^M?Rxz|buS;"
    b"{s%m5Ah;T$<wK3~2#+?DLd~%<Pq@zR<}>ZVF$hpNYRf2a1d)9P*<HNO=3z7g_@&T(}WdlM`>G6KX0vOxIMl=gj-"
    b"yFLNTSWT<B{2S~C)8I7@kc;y!KJYUmG&C^#h=;2mjy4tUyIETt0c$fOdxnzz(qP3AX-bz8wHjF%JM`gpK_>R^6B-^`14%~^O&EGgOpMY2o^_H-"
    b"+T+_zjGYRUq92^%R4_a|GF;ilzi+$EV%w=-!Cn!6}mul-"
    b"(ZI}saTI*ySZF%8s)Ol%o%&;K(vD>QPNrE;>+>bINTpw1;Ied6Wo8f}EV2|7t8=_Gyk&44Bv8z#5d~o?hgw35KXRo<m(s$D(RsQ2}#eP2b`8un*H0s0J$>JH"
    b";ckv*z^Z?IlsOl<hFgCgHn*jQJ4F)(J*>e+h&I%-<Ric4!inanYiS=cRcvzj*hVE*E0ai|fwpXA07rNozvn~T6&ja7Ff-)WU-PMuyN4;fEuRVt!Y83>RAod^"
    b"?$anWese6U7WRcle0ge3LCTqIP+28z4#AQ0t_~)fuR8cX~<l-d1l+)y7&y^I^OO2P3E46gZp1#IOljZGMKFf%E+?zhJT=tDRfUe4o8Hu~}PPJ-"
    b"!9!NW9Hc6MYslRhsC|YT7iScLP5zsboT3k!c*DLAYDIad?WMQs}aI&(4{mT3po$9#V^!R}BGWjdmf@ojN`xi3r>v37g;|ZeMPm^q&oW-"
    b"d0TbbO>0a51ra*6jkXGi<78j-2$GYe}hR4_j?7dh!gJV)(i`?$fqUH`h0{g0AuSnE=Fv5wt3*!F7%7&Mi>e?C^p^J?WREC3*k5dZ-"
    b"GuFuYJ3k!rZ=dazbq%e}EU{Bpo{OpI~^P*FLh^8>Jpi{P5ZMk?9!F;DMX76XvJ15oImo35Mm-bG>omf&$250?#Pr<o3o@+Ta46NV>4b`pf?}NlHy$s!evC{n"
    b"?UN(G%*I|(2Lntu&EAD>%;W~bPHmEu)x39O<$Dr=F(-"
    b"rK7@Lr%Q)S_*epTIBa_!gpsI~%xPN1C$Am?R;bBnhw6{V+eDo_?{1Y6vgs`o1^ib)@v1R(8AgM|+)>+kz1Md4Z_5Xxr-P*Z@J$*2{*5S-"
    b"(a_suRZ(+(6ALh}sI$$6M^lbw)+i?Ct4Q{`j_HSIg3qrOx}_RI`#LjHRwF=G{_@lBFw4U2Dv{#n(!f_AGU-"
    b"*03XR>SgM%51Mdhs`3Un^<*!1!&bOA;9TOHNXSyc%=UbI1$hrgQWOO2MzM*E^IEhx^YV!@3k`~b6sR##s_zVH@<?e3vqPplXEr7GIjy(7KM_k&p94!|JzXE~"
    b"aeC+^EQCBqiFAxlSA(u09y4+l<kEHl1I*S*^eefY8Vh6VRwjt(#|QLq`(|wWrXEISBuI9)5W2~XV=DE@7(ReYjUBayA&PRTwW1_JY}{`zCyyRxeiPx*^$RBf"
    b"c4N2IrSRXnB6;^f8mpk1LFvb3+@6c*k&>LR=hmiu6>@WivL!e77=Mg!hX`KYu5H*<(?Y@1u_Br+PDY=!D(S}!1S@_px*}(&!A9u~5K)cZhR+#A`!l-"
    b"L*`V4m7Z+JrlYj_HO$6=42}dAf{=>?|QOv1pve<Bqz$I_-p_<X=y1voNtL?*R9az=!tCnwj-"
    b"&c><qU(&uUbMgRQpZw<QWxQw0KbqIFuv@`5bMN%(Rk2H7}8CA{0baEYb!G-"
    b">0c7qVc{2NFyoRUjm|Ek_)2t(D;sdGh4c3Qs5`XZ_oJZJa?kWAv8M1T>}gq4N#D8k46<l@Re54lAz4aUL+}irG+Hg}9wOaoy#S&=*&4=@Rl750=+K@UVSwI^"
    b"!p0<#Ud7a+f)B-"
    b"xZ^t7Zo#)kOww?(U6o45unbPahCyWxKgFPg<f*A1n2p;k|F@+uv4=dX|Q<Ig=;g1(<E8$gs8urD=ko~U6QxD1`Rq0fWY1%qg{BJU>W7?VJDDWpITcx`?oo<i"
    b"SOyp-m7-}rC0b>(^1R-E?3Dd(<%$K6*SZ#0I!lIGZpN8&~njIz!_!Hqgie%+Kzi_L;N;1=Xd==&)Se3!V-+Z=OC1U*bn=?q(SjN;9Cvfp1ui7wJ5_;LN-"
    b"4Z#IsVtg<<XNW3iHjSOvw~{hbI8Vqh6q~kq_LV_7e)O{z7r@;@^08$LuRb9nb^*O+lo1{;h{6B(i$&gk_BBwmp9+O`;2Cu(#N+g&cm^anI`fbck}3F!f8-"
    b"PZ3!-"
    b"}l~X*_ub?(<xn!c8HNalUg<*yzb&)Q^{3L1MeXE$BFw*?tTjR3IdEG_#Kr_cQf631b=mE+yW`f|mY>ON%AkFo*Qj4edhJ|23upU?e7vG%i8S+iaj(ZqaPYMx"
    b"!Xf~WBjkQAm#R=`RqPG1(k~8+lExSuwoTJAkQGW5%@_smYwt>LSmgD$nSx-GBHMP!FB3U>K-HuX2A8q^O0AJC2H&WPyr5&dVttyndPkP)H#rtYW*{+-"
    b"#F3EAk(r@2o?~BuZdGWCc5^Vgp)!JAh6T>oI9E6AzoegOO_>~Xs*4!fA_Kcgl^km|RoaG2V%IE8?8CIld6JrHe9F&Lip7p3HUqzguJKT4@AnaJYa{Z`M)~=U"
    b"ckHU(Ei-TXMJF)_Gt2BwU*D=3c@|1G^M`vnjU4Y`oRq^gj&ZMqyMT;G5k;<XCQ;beK<3wEKm6?M~D9h}Uq_;P#J5^5aD+l$s>BA{KVJlMuq<mSHbaVEEKn2)"
    b"6;t0EV=RPk{T7wI)hA-"
    b";{k`|CVda7)s>j85*^aE31VB$@X6}WoC#t&^xJiB*~Fa;~ZY%Max*IvZnq2WfYRpP%r>qOk)m_R!Cww&y2KK(o5KXX(M<_6FMpE5GKKP8PDohc;CZq#q!y;H"
    b"6_)#XvrO<2Lww<3rdTCEII_l5;A>F*hsjw%X$t`l+vYPmAy`(v4Gt$5aI$&lWnPYfbwh!!f1pblTx<xObrtSyezUZ&iO+#gWJ5=+VKW_G!?Kc-"
    b"R?mH8`9smofig9^+mKGvJ{J6fnijS4b-RMdSAYaE1>F26T-Rp0$2Rb5qsa3f4A1S>yYf4+~Ekr^w`phA6jBpEHa2tk{iS%$Io1w~xwyB&R-"
    b"X&DBD14)xA=c303XD!ie)o^oB(D`V%E?@jXG?VTM(ppk6vd&taekylhbti0uV0wFpZ`M^2W5;nc4?$IvHOirFxgnIhr&-"
    b"OUbkwa+l<rw8otr865E;mulspwDm!%o`f%u*`*tw#BM6w*<tmMKUGSa5+--"
    b"G1)aF5O9A;@f5fg2JoFWzZwo_3O=6fN>8`k?P@XDb!!^E%IZ6l=)Fh~ZV^_qRr8$x@+c9#K3F41PsELUy*I+x6mwzDk4pB*|xsMtB|>#1u!WQj$u!SuXnHFq"
    b"Lq^srDxvSK3Ewbbl80TU<Q`j@RwwdyIcA>O4P-dZyNp1~oU)_eA#0J5|O+Z>kGvG_(W)6a|Ab`rjYuOHXpdy>$^dVEBOMv=Z|svg}6yr-FjdO761+=Q!E2&o"
    b"4eNX2wqiPH-"
    b"`9kj)#^r{700XQp_Q)Lh)XwiqjLCxheM*=6}MfvuwpzH<?7pe$8<uJ>s@0sovu$DBe|b&eAM^<d?&*E)7M`U9bzdi~&32@4q}<)V$PLkcYDF{1B0{caa8g&Z"
    b"nwnn^`>$VQfY;#5rd$@6C%AZF`!qt4>F27rHf{iqK5o)k*$$@7u4n#%w~Qz2_*SojvwsK;E@uVg(M$VDEtv9ekqP2JSp2*@&Fpm_7tV$0fLt6A||g5k0b8#_"
    b"fJqpF>(8CR|bbQ(wD{!(NvWQp*{pm2G89NWxcw0Ee860J));(9qD6Lw{?uGMJUGMCwz4XEp6?k4r^khTg4yW@6PV_1#5d)OHR<r?xV!<Ui}=M&%<=QouuIP7"
    b"F_dy8Ky3*j1<JbR`F>39=+f11EZ9j)4oLYtd6o4zDY8m%v_%6b(u#(CG|j3~iQd@p{wm*~~qiZr%Ri4h<$w=--"
    b"Z45!i>RVvDk$<LfxQ+%U@l3>gz@?|TDqwD@@^Y_R=r*z=bo8}9S4Rq$>`*!1;%)u>du*STRiZ*C9{#t=1^jIw?{O#ic_H3nv+E34Zgk(37NZ2o9kB)2Yng%("
    b"!k6l%udt7K3f7bPUb-9(e=*1A-"
    b"<l1pC%rotCh6fJ17W&o3$tocVFN`lbYhm$uU2&p$_Y%KmTM;`=Jbg{Eq74P_q3Kw;(whu3RKL^G?D8`xZ$V`lHieYS&bTNOUZMWSO##2$^yzoMST+;@;OB~W"
    b"ea_g)!p4~s{ByhC+WtuF+C%AGES#LJ?CnHA++Z#cy@egr-u(J+Sp<YcSl$-^iHSbau&^;jT#s;uTRAw>U#r+Ti-"
    b"6z=go6+#r!(}rsWo*5+dEj;U0<=Zcd|7_T#HUHP6tz{wJFSklZT6okJIVDF+hJ}(rdXpSp0tw?JX^>pcc~hP^7Je9pWE=Z;SxZYneL1ED$0f&Ksl{h+e^51f"
    b"(G#@PLckRKVQa6w1qME+7b^=M;U!`N#W;{u%cN==ng#Yh%V<H~3V4#r<D4{crSN_8o~=`pLTmRhhY~(y&%q=M^qin?gKL`cofiiGk(=k8L;vh;_u(0*HJ39v"
    b"9eI9z-"
    b"ASq^qW#&NhwM)nbZBh4{OY73xLZ7T8PgM3RXXoT#iUy3}FiO|BU326N{QQc>JnDB@irAx08v_YOy|uvqKUl`C=|<uK+=%FUp#A7;dJ?RN~RAOxbnWXUc!`Uh"
    b"cEsgfI<=cV)@_=vcLipM2Nxl)H+lODe{IiAyUGnO26n!wggBq&Sm2r(dF`)Xo3ctmE%lBsSbp_4Juf>~o(TT-P!=1G?Au4wA8Xb(A>!H-"
    b"tLF{o|GuD7fOSB9Rhc5|NqtU^ynd}#qOpH7O2neRiuscRAJK4@;e3$#%89BCBAD!t~GImYn*_dYimyBy&$73yo#E};Fzn?R)O?GV>r(fFr(I2-"
    b"=rGUI=7nKD(x?%`%lhV%h(E+{rAIA9aO_?}Xc#z*mSFCsDIR&k5Lr2qz*C-af82R{2hdc9uzYL!j2nxTc-bm$MSE0aEB;U#a?$6rX|H)|+2YPwwvY?CUL8Kb"
    b"dJ1WozRGD)G+v{_3XrYQtXmlTiayJnNuy=&k>p^Q;l;_j(!3Dzcz3J;D&IekANtiG^!>Qbt|3Cw($W-H#%`6)Ud-`1Ldw-cW>hPfBLC5QG|TfDns)qNw2>hs"
    b"yujtR%feQloSL&DSZ@>so7m>RVNq+>z{c_(Uk4~1l2A;k}e2_7I6M?~D_+K=MV%!ke28L`5R1oU=Cm(Ex{?+!rZcfQAJ(H5Qlxbvw)jBj9dRYL3a%sPdd5(+"
    b"9Q+P|~H|C#ci1O7Khd{g-"
    b"*dHP$K9OVX;dQ<f#`}JEj2JIiYu$urkyZGM#I9UJO)89n6*>L|x$j18j_WLHv%?ke;1xfht_5L@?KPTYdC^W=>q~n{nznN%$E83F$Uuowi&dsR$jWa;{k1?j"
    b"Egn{{U0M7NSaQ*(I<UghV0e8UaO8"
)

SCRUM_XLSX = (
    b"c-oD61y~$Q*Cy^H5ZooWySoP0;Lacu9EK1a0t|r=+y)7*!JPoXT?g0Tt^q<|2xQ5<-"
    b"){cPes`apneLkI>UyiI&Z+m*sXCe}h)DQwaBygFekSs!L^%4Jui)X}@Q~o(o<7`t<H+gd;_hJO;^M&Z#>ug5N=qYz3kUVAQU-"
    b"QnQQ#;A#<c!GLkg)Hy_OU4@swNSz)y;C$pEWm`9WM#TDH!IP48>HImr&OjdUCca=r~n6Ba997>O(H)#K?)q?wPy&P*FQMa#|0%mju){X?%zz0jPNbbVt-qAu"
    b"ZeImvR22Ss=%k87QtuyZ+I!DTu+9tq(Y*BIrD`}bFnu&8jO<K{k12PGwG*km}`e;L65Q1mm$Ob{D78C;-k!+*QR$K0{xW>|B-"
    b"{P616+ew*e0yfX@EYhClrG%ujGe!`9f3AU=z*<5#ci)ti#D&P6Zz3zUc5Gr*XhaAD(>Br6JwMKR4OP<e<<nNCa{X9{ycW8__f4sy6Rod~)LB=*ab2OWclH8>"
    b"R|+q`jmV&2;+3T#!82sxbG!ZOtQo7dl27pb{9*jXS1E+m?_NR39r?5p%|E>-"
    b"Z>=(2;<v6_c_%^CmN=qB2$WSFG|M(b)C)!Ui$y`^fpD7t5DT}ziM<8_9Goa7931xFV(|cZJKA{s7Rt8XaCABs{vE;aEjUP&FB(kpA(qy2YIG#mn34D`fDDkq"
    b"yg#Q;G-"
    b"90#Q^<6Z#vK#S@Su_i6_fa36z2tO`OHo7LC{z^UzlIssWi&W<i<uZD~s~hf44&U%f|vx{@f7gRwB=CchMi;v#54DcZsi@uT9U!y54oAu=?e6y<TK4Vw#>-"
    b"%}QY$VSP@vfk2<<*0f2~usu&W7|=f0qDk_>TA3CtgLKAVV@!KEN?rPS9r@{SSZPcH<pz|N*EGff*O-FW=d525Yz{(f)O%GC{b6QCxwD>NOv&L%y>?IKYDM`-"
    b"F)%8F;BM4QDT!cC$otyPY_9k-@nPw?r`_OOxC`fge&a^v<(<{u<@~(NV)I-"
    b"ohjiuoDX}e6k`FTLPc|1~f29$5s=8Y<07wO0)!k@T`DUAGyFKc_VUW33S^TEV$D9M$h476wHWW#2sr2xDDQn*LWK}A{Rtmv!`Vnf6;7p2#%clmgfXj|RKl-"
    b"(Bp5)p$EvjL24Iq99HkDpIGl28G-"
    b";?=+rkd_qssN0}wFBmBvUgmHLTCt4TXGmOsn3Z9ZzM09yJ6&(`HQA#%a$V)edNvXTvY0GcCmxPyPY(yV+LuoA>$XC(!xATd|?`zge8P;UZ@YiAg0nzZ%L0T!"
    b"f_avxrup@rl$vRCQRYEgpAkRDC^MU@!kw1)0~93zZLFGm1eMBL(VtaLPbOtR+OspocIPLr8LK|bCoo_#sx%OP@}n4QTO5CQ2OG_VZ4pUiLKsO^Sw|A^E$0Dx"
    b"kr(_ga4=IWw!g-"
    b"zd(e8JAYsUyuURMWN+hS^Y@wiFa6VBQs3mldC<SpSYIG3R&LIWM3qql?Qw0oPy|tbgrn^6YUM_LbNn;sN#!NfRJZXF$opeA&dR6Eh~siE(%g{BJ@62^LfG=f"
    b"6wZ|7?L6N2dq$+N&@jW37a?_;Ysn!ZP)5?DJz?H-"
    b"kHA$;97+MxgoNfBe6$l@4^Nbbyr_=fg}nQqxhB5tHiWgrXQvR!9A1CH|D1VUnGh2mZ^@#gxOzSB<<A7pNjn5FYw+5~bFL-"
    b"H*pRnDmL+}+IDFqx5jGDdi_23<xt&RzFL&(?3`1iY1n|FAG}H;4Y-"
    b"}`GPM{TnJHGoISC;qXDXdXbw_+4wzZUdxc<JkuqwKb~A}Bs}Oj1Xj5!`82Z{+>HB3L0QSClI?o%cuI38}p<vrjj<p5PbB!{7hMP*Bp}_l_Ks*z0yN1(J8X9}"
    b"{3N<<{y8XpPKDFBGo)A%n<kBw7yYn3?~g@-"
    b"0i%k*5NbQk_d)oRT3YM2!YZg=S{2MfXKaioH=fBMXxHh(s(tmUu3RC?xIwwyw~DIO;Vw2sjBHl1r>E_p#hkKbQyf**E1x0p-"
    b"bNG6(RoBA%P05@VLxQ1g6GF9oEpWl-A#BMtPvSfih-"
    b"(%N@v?ZRYoOp+YT{4v)GdJgOelMmH*eTpf7?8#0nMXuaQW6jrWnJ;M>&ket#WqGBI+s`CwJ#lqgG3IT-"
    b"&_PL!t11rIUZ2n8JWW(}eNn1sSh;H@tmB}cak1}*xm)X}<1@nm>PKs<v`-dxOy(BLjPl~IQgmHkpv-s;x@G=wBsom3Q6d|US>jx+s?2-"
    b"$Qk=;fFXy<qUnX$xHRQ$SNcm|#H*A|xOAdj*X0mw3YaxNwDm~P<%35QCG8~OibSRWMUz^6BiXhlRi?iJGDKN<-FjY^<I+?NQvs7fQ?ykW`y$Nbgy`Ep+i!-"
    b"W`-kUBH5#Mit;{~7enU6L`+r@f6xqtB;;nyt)F997JmwPU-OOW-"
    b"7qAGZ1qlPvJ`de%n&}UzVSV+ltqzNv`zSclMPE(ARIV&U2$(}DMsFR&2B~<y`HTUBSdYS@X&+1J^yjpKMboJ9UStwQI8+uQSuL~NL(@VsZ^H!5oS$jr@cZCu"
    b"aCU?mH9C+B2&3iTvR~`=s{(mUn-qPI$paXITI@|rl{K%bJ7~RxZa1)<i+}kZn^u;cIlwYjFU?5Duj%ojq?BwntNov$W_XY+R4LDUyV(pw8>ql+yglNqyZ!wV"
    b"Cy|sF+D7S*?rnl-"
    b"6KX`l;Qd@GmDbt3!EsGiF)~%1`vSoryUJ>}u*OFIz`hw)a647A5!4dzNAb8l@*nm7Z|4RNMh2G@O=qWB7u({2as9Jh{m2P^4atj)r)Tb3hJ3$BoVKk$I#-"
    b"i&M<V~nQH-2Lsff2Iy^vNJ)|F2(+7lx6QE@|4`q~$t*XWXP%$k|HFIt&_eqo4HkH*9@YR0RO-"
    b"%?NQh%=K;w47kW1{OAZNga*oj*%)d%2Lub+HDs})i28<!kd!15wD9gZY33x{@*H#jQ^8e31Lbg!N%NO|^0XC5fTsBR9p6PisU)I|cTfYV2^O76XF-"
    b"{g#YRHSp}v^(@=hlF*xBfkW#Q;2i{%W<z%I%(`=W@eG_Lz}hOfX4O5x2+Tfd1`e?2_%wDqOtShl6ENfgJH!KH?&g%?2=JnEr5MkIa~hgqzZKTH@a;+Yw8YxX"
    b"88v{YTF9A0XX^+;5#EEk@9Sk1Km3FX?+Bkg-~aTBrgV~>SLog+yPG9p!IqOyWpC&X=^JZoQDaliZ#hTg;TQbQ73mvC;V+K+?otSlxrTyda#%A%Vs!L-"
    b"A7DImW7*gYfs*YMmk6^2irwF%pFY#p}q!wL%fNe4T<&gk;PuI5DsaHg;Dmnsk^M1M$c*UNOHg;~KEkD$0$dt&pxOA>bz^B~I@j<@1IG)GY6s(!`!%?pcDr`x"
    b"dNPn;Lmw9}hJxs+Kk4+dM~OT2JEvVeYHa32AqmC&2#9nLN)0b{y13kDtWsU<&637B~6oCwejaKC+-"
    b"|H^XJ*tXC4Pjx~9DL6bwfrC?I_*Zq}`D@~tHtM`2gwt<slkGtk7>KME>9~<^*tA4@Y!%aMkT$Q%tWBY<zTCKvc$715Tp3V}%*^N(@|FWxlu@N&SJFC7ay0z%"
    b";JYb@rL<$Ho}$uWHUzFj*G^_MI)2iuot&XE#(ah1>#KXm9XY}i_mYwI6)m2|1|dg2Rgog{(O`}jE8FKr9?`Sp_8<9GJ3}FY!!~&<j#p&D7)e6XzfPKeo%@2B"
    b"NkwMPsp1xHw0Kmh^BmX;+9n%aUX1KqF#*3nvlklHRjCaKGifTu8~8TX{#6g5{51j)ST;5nS+2M=RM^%4RGbIR3S^?CpDY&MT1=fd*6x=(`QQe?9MbReM)f2^"
    b">PM-"
    b"&#$BCw{p$9eYe~wT6k;6C9MbzXvkn{kNsK^@WiG)hDXnFqVnBL}R*1NAXuJ#*b@<+6{rFBooDaDWl!&hiej`2jZ5!fY)yDcme)pU7WlUPGOXv*z!c<xfRUA6"
    b"vXFGmR4MPK~9Gd4<J<Xb_VH;F)mlq$yY~w5mCnPFM{N)QLhSqeorS5VIVe|86@vS8-cZn~;z$hk|1hMU9WR3Bu&xqj-"
    b">>JQ96Vn2>i`R1&Ek3n%>WPvD?F`$pBI#lG;%GwMPv3x*{p7*g!OR9sm?|$k&8j}ayl~5G8K|vS3PsS|h>q_!3;6)_c{NDo48&<kEK@tks@!*M-"
    b"?5TA0EX#rwOI+#QWu{UTt`9#a<coN(wQ&FK7Y<o#EfoF%$;zJ4+C&+G$IsSP``&p?k0{wn}(@YG|dKLVK#NJRs94F{mrLTl^nl5H;IYf@ZEd-yt><3anYJz$"
    b"gaX`(=2DlpVh?DG8lx^Pi$Q4vRXIe|HLzTmSYizXZ_N);$BB{A|+mL6?%v4680>RmQ$|2jYz}N_rQiN$3onC1Q#O?mnl;NVu9{4YHuc0IwON)j1Zr#C+Ti=h"
    b"ma~JAN>pTU9GTS+Tullj54;$fC^9YO8=g<V&8PQ$c)i57NqC+77EXj<X@|^F~<QB!vrKUdG26DQKBsjwY5|{qN0qowfa1w<4U$(AtTP0GWCtIhO*ppwsp&c2"
    b"coubX&CEa>lVxd7*9Je2bc&dMClM!xR~U3aI})^d$2+xctoPB%VglLzMCop#pb#ta<hk4FCtfS7_A6=TiI~|^PZfL_M8Mr9i5Q(oR~=;Nie=^!^ZK2V$LieS"
    b"UpJZ9n_tO-W~iB<z-"
    b"<a#~fDyeYFbzkEFa|ZICQ*9~YaJn4(iI9XkfuEjm(LI~F}WKUJBBOVJuv+e+az@Jix2>bJvV()O<bXNSk+?O)Bl9f~ss++qKOJyfvr*8HJ@0H{0Fz{`Lq&EM"
    b"ZhH-S>(f-`v57pA7jYSzt;*cML>V5L*vkD94%_=U_XijidRwWV6myvGQtAY65@3L0~N-dJS-"
    b"#a2bT!wKwmy`tUY1m?S4@hf8)TcC+dj#JkK(~BQpb{YF%Hp?SLOAOxrr*qcE2b4IXRHL~<Zqt_MS9#=fan)m(8`M$IPSpu9>>mEmWZjqcxliSDS(R1N^lrm|"
    b"eRU_!Pzx^R7}OR9_bMt{R8dCvDt%hiaiuNSkO9j}neUA_zl8#*TizGhZTiSH$A*KpQvq)s{OpCH;6$0S<{T*sdem!)PSnb<bP|%o9Z_vEYFk13Z{=Apc6&}Z"
    b"`mkYjdpn;X=?5c2>?CeY4)@^Ob(bcOd$8}e%XP-j4+7U@@|@Ean1K(C`6)kaTB_@jW6FK-"
    b"S==NUk}kbdknVmx&7}Wprwdjx(xqWj8ob>)q7~N9^U$OdQ+<y4<A_Q$lF!~zG&ZFb6WhCxGY{Q}bZKNu@?+9IXn+OzF?k=<%#vK3F{*rLr|rh}QajV7vpO2^"
    b"uK!IN?@;~H;(as<dtDirQ*yN{sKD1XOjn_mTM)a8m};;`P2!V9Db9eJBgU*DL<GkY9gmG9_ymJl8%d|)6xAi1TO!SguaEVfGMfK&j{xN+eO{2G{O}xg&9^Nm"
    b"1i|i-(3>F<UTN-uIVrK8tsOvE0v$cqV|>t6>+40@CDZY2drry{I_hVy*7JSzcGn?Qo4+3UEjLXFDiCBixD@(-H7vaUF)Z#&0yshDHsN-"
    b"2HTU#_?tMwe^N^;|`IF03LwHtnJRA#n&E#7F@vB(b{zjAURuob-<+dhF7HU~^k;^X97*s@XH#^5XDOJ?gVS0IG&4ID-"
    b"%!SRGwOV?g_n(Fw9YfQ%*UJU6jxz>2c~XWbITRO`n>VVURgUVyi~gpuMmz4MYSCjS4!jQYT{!1B$-@eVYuR%HTE!!X-"
    b"IaFhYcVJc_Q0}jm$xl9Ok{u#U}OPEA9j_|<9MQASeq{0t;oZEyo2YyZk#C{J$&Zfg2HD^QZ*@(>GE#0Xx>xR0dGqA9ni&U5uH0zO?8*Ku#L5_C1PKquTG@J$"
    b"|pVbtIo&!iqw0C!mNpgP6pdpS8Q;4>UzZmQ0%Tb$2TKew%ziQoj6dl16J8Tisgvrk*CVUjBhH6cl92J3bvoa9t&k+#WLi<9Eu)$HwxW#qe+*XW%S>=*NyY#$"
    b"cVP+C#V+8eP^k`Vx=*_^BjXg?+43U$?|uS$<a|VjD+?%@U)z<@|@#_GjePh2=)W@c<&7&y$Ezn;@InIgyQgXvh?$_jKalckKUJB(8u8#JeZbE973jgZw{^Jd"
    b"-XPk4#PEi^zCausS6Ew_#(*|H`U*vx8xmW(dkH9Fj-M2S|HHJN>d+3wNpzXC}ppzXxXpzAQ64?rMA(k7AB1d8j3?!=aLOW(fmBQ7N9yh`zwBOLdIar-ddZXs"
    b"EO8$$Fc*hrnWeWpu!nw_2c*gu#p-iO=)dL#~auNJKI0FgzX$`?0OL~_GhWDW|;;2JR9}`&V8M%Fx6_YRc!&-;|n^^<*uZ?5^U{-"
    b"@=He#C1GOks!<~s$Qby)d`rW%@82SqbJc-?EL<`(Cyt||iNHXg0Qk{?IatSBXSjkm#e(JOKdNc-1vZQZ_U+IMRMu0*_UZtcWp{cSLhRYmXN-"
    b"D!8&M>tbk&n{+&=kAsXt4S#XEtgzmP!fgy@agqmwonpm9XC^W!UwW9{r|xCSd^n`UMB3tTKTLOAb^WwoSo0L7^;k?j^<n)WANY?#c%q!t6XTL<rRcgGJ*Z+k"
    b"}_=PYb*`A3f&Aqyq;wyd_czdPFN6*n)$=UB9b+iK^1W>4U!UUYKy%m!D~<RAyVo%~i|Ggo!_8&|q13<mI-M^2bKG;O}5o#FMtr-"
    b")1<!AhMF@60*A$`%{5#$4~?RPVtFCg<hy-d4Z?Km1_5*H;GSvhI4jCKy@w+7t;W6;oS1e4`516?ze(Gr&BjaE*>=>>m*$-"
    b"SYi*wtT$t<o!d^*?8grn_W6D*M~N$k2L=7`jeRrW1g9((t;OX#DzY_xp&kFm@rkY6c7!?uq8>7cjB-Px;o`Ke?Rd0q@QKnM)Z(`7`M%VKDBS_wdWeIq#FPAU"
    b"X{J&zuybitWs>lHR~N68A9Mq)2qw1Me4rMH6FC4;6P&gwrjk4)_>+8f+oi{9|>ZLTyEYDx`X8(wl{(9NFS0yPzd`z3PHhPZ@vmx!EIBTeUe_M5?%Sd0xMSmr"
    b"nqs%?KNdA_hPKSLBAAbp)2{Ft}{z2p6XGtV+f3%Y?^Ult@k0JURdL&Cv#R3C}T2|WH9_KiKh;6Y!IKkW-"
    b"6@3Tsld~S|rOXcgqsFTlvn>3Q?~6b$F8V7&oNVvZ#^apO$Xt?IvWir;Ak*b70Ps#VV9JaOJ+yg~ct&wY2=wm{mi8PF|~<$Z3n8N`Lg-qM&-%pdf-Fg7&jtXI"
    b"<r4Y+@1=XJ6ImI!&*ex#-"
    b"n!F6l<r7~*p$3mVy0K3|frR+@_V7I_ievn?{4iPXLI{@`LJ&+Mv@Vs9&B7|Z9GcVy9?6>Qj^hyO*?G}L7Ui(yeXQ_^u1U6`bOX3V0r-"
    b"gnuc{r3DidIl=_PdXo12-"
    b"B#1pmQ<Wf2DK2zv+C*c~juG+nIgH7fq2BUs3ylVpsFc67@oE%6o492FSKFJ#+uq(j{(W+tO02fwWONv2+I;GLwF?<LED)4L|bu^Y9o4W()Z~_i_b8-(S>-"
    b"+N!%I><WhaJMCDtF^p8R{XZ7{>Q!h_9heiv&0=Z_JbK+e*(}7<{l(@g+;a-KwYQ6GMh#q{-e?KAGr~f9jdbow-koR1-"
    b"c8qw9a!ui>aWvxorQ<MBwKv_+D&Bsfl7YWpuDn`;q2|_5W)r+(xCq*-q@xmSwD<}Uo#@=85P+S%m+lT^nprK)n!I32|TXxr-"
    b"1DQQ{`5l(Iwhg3R7^VDy?AX+#xKsXXLzothNTdSgYqiaWCDy176UcM${M7O-"
    b"_uO`?I>tU~Eh0L^t}TTw}YgQ?Z`#4ABN;9#Wey8Wmglg+bwJdLJsH<)8ImFO_~YrhQIX-"
    b"hX%0RCttR1*T&zl74lFwZolKo5nF$m~VJgqWTJBHI_Z>y&$ahwT8BY>=i$)zm^UxnNwMP2$w67m(t<RM(usXvw=PSb-"
    b"foqGRsbn0RBaKU%I!Y*|rnp^V~N9&Et#2Z!@wx-Xb}!B}26P&RYwS4a0e*V^dK4PaB?gOy=q~H~6l3DD5FTcEs{7684ar(@=ZRW84QdH{5b7#FO#Q4iQO2c0"
    b"x<uhXsBFDc0arU$*T{+l5GeP~(<}$G-"
    b"mz3225a2YhLUZEhSKT@G*k7%V#6&yoxqT7SY4&aVaR*Hj|>F!Z6(z2TWrrU@CxAe@o2>6^YVfsVQwqtJEl@6SS05b)r`pqL@ga@K@{C*5t)1gfS{jz1C^yYW"
    b"N^Ar<$Z#z%cc1iwu}$k8R{K)SiE48tCX_k+R@!z0UnU*ilWz;N;lAW2K0=@mL@pZz>IJbTRWbNKzZd2`Y(7GjO&ge1NAebEm;vs(A}=P353Xk$MIE3^45)De"
    b"<o1B;^Z$LqhVwH>uC_Pp0m+w*<$fr`!EcP=UjSmNa@$kbr|vQ^A)JoNO0&act7%gYKqi;XmijBz*<cQXJYEkWVIq8t(>8K6^r5bMZ;ORXdxfGXQC!NMqIVP7"
    b"BCH4$lC)YkI+c{7GT)hsJbcNAf&bsYyNy%=)^d??en|9Qe+L)Aw#_41XKJ8?IiAs>sNdh)HDHd%BPd?7M7;kyX#_#>_vLagfeC@L*Xo@WHy+OZzvSXt;bRdR"
    b"=lW;}gQv&ZY1h7>E&C48_ipblv<UwzM^tLu5@2{F!5F#u@svXJ2k2$!-"
    b"=;0q?#Tu`>1*A@sr9*`b!#v3L>7CtEoJUhhdu7^Kl#9e9*lRUd9&M=nDT2OCDmCDP@xJ+NmU*%%FD-_;uXJibaP)Fex-tQIqOQs3i3=WDz=Ojd8{eDm9Hybl"
    b"J`Or8pD=ZO_MK1K5lwN1%h81v<!jsm))AB`6zm5(YGse8U;BMC;u)PEmg3GcnWr7J`CT2?G9bu8$+D-"
    b"6@hWr57HFb|wF^Jv~iw@>$HM`X;*9X#U%pC^=H^JMT!L!C%)zRIm;sW?rSXopw!W*Re>}7+ah3!;$NZmhoYdZe?s$bC^Fh}NTJCDTL4K^eZ7#%tjHxyp9+%9"
    b"Hd4IyUz4{DNoU2*dHOzDzyqb+)cx^)wsvD)2L5?gNqiSY)aOmx6Y7uos?6{7azmNm;pmF(4xjT-^lp&>22GIIWrA+4!0@-"
    b"{}+<B*lcx2XI;;TULq1?db~(V^+>^X*ddj~-!GoNWD=Fli_X-"
    b"3k!T_k&lmv)K1r(<S{FW3uxlxG<>qpqNlqFmp0Wpkw!2cKB|DJ*PL5#uvPo(@Mc~ev{bRH$X<wX}IF=8x+35n6OaW&Lm`M55b`)SEwYZ$5hN+)l>392R2+&W"
    b"5AnDN2Sz+Z+77%BlWK}7?)CD8i7c{H&p*5d1k_rYzQJ8oGAIfl05%kBo7&NUlbt*yKIvkKW)DcR#jr`54N3xWW0vfS4m2V*KECbJE3w=Go`ZDC&J@=wzb6+C"
    b"we}V483iormT}X{Ys_s1XVXpshWDT^Br8I38AVZ5x_+taCG4I(5wHGV#)oCs2pN{Jf^>=No*$f%#3UC1x2#%Q$W~;!TASWdVU}3nb*avVRgmU^i=8!c>n`#h"
    b"Ih!b8v5V2e32bWxf6b3vW_@Q+ah5sPlyX<ZEaH29FMUL2r+Qg4Vt*GnB)MiO!1iZtG`Hmgx^FD_N)BBMz(PsFK)-"
    b"6X1fsw5rFK|C$uI<q^W`iRn3Qc)EK@1Cg*sR5|qSzCK(dUcrJ)|yN7e<%$L~tr=KMHA=xm_82I|~GGrg78sabr;ax8j!#wqN9Re#r@*XC!$~g+2QtoYCeu_>"
    b"pB}+#p#;~5dmghgBN%lKzDXM=RX{<`?jHydnj%o_AIRDDe?Wxq(+V0>K-EcY2$PB<3C>S6hom;FF(eslrRm#~<%L}<**N6&6kX{c4-"
    b"Wr;*kj%z6m}J(OWP%P`$(rT9gGJmRf+uFjZfczs5x(m#ZBRkf!V&})tXFH=-"
    b"D$(&;>yS8Q!U%c6b7C6#HF#HCs<uB&n?GU&;`R(emwm;KknFK$Ar~&64;Rb%U;L{D0E!BK3|X{I2|!OCbSatWKQKt;;!x%8iB;ow@X=>uu?#ub3`*6EB%~qr"
    b"(lP5uc0~tb-40ic`ki9qbr}gg~OBaUO%(ffwm+@6$|?<L5SPhIbdZLCRep~<!imCnp<UMg2?L9>nKV7GUkqk5-x-"
    b"JRVva1_}a4S_0!3^nSmOM@l8ozaw9+9jDESG4dBOqzFUVXoR^%Tr6|nEA>5XuZbBHg^gPe(YJh2(k|Yeubs*i{RA9NR)m@?@>r#xD(!0(V<qPF{Qe;W4(A|W"
    b"JosbMxQpA3q0{*JW$f42&Oufvte5T$_7X?;&N?OQ{Jrzyb$ASGDI2k;}bu8b_mjMP6V^2}?Wz_R!cusS<0r#*yH);%pu<hFHg)ocO*`mO;54nwe8D7&|o`2_"
    b"h3t{g*<UTE07mEU4Q1X$-"
    b"EC%|=h(tEIN9<{Mp7R8LU3z(G=j9G<fAC*nwJ9z&(5&0n6yf91HY}feV|1M$6CG~WgaE!5=*1VpM*c2<m#e)<vy;Sz_ms!6gvCep$`;QHyh$_0gFlYJR|Y<E"
    b"!65^MM5YLEaA(N>I-CW559dtXC1*TtoV%pBtZwJ{Ld}8|-GU$~gwRFQkBnajE8fp-!fGO5f_{iu6I7p$@`1(5axg%Q_-"
    b"@oV^v&3qekS;1hQ1>UHwzeH;6+6ekOjAUV>Ci2E3>>%<#oHC3cke*aI@%>avjY)(9mZ=JN%1<itWrka?6tt&UyZV#^|cCD)p4j^)si193EQSohc3BoA3}}pU"
    b";3hotd2So`|3{LSoORjcq$^H8K`%5kgIde890FD~P4dNGkkOE5{ttW&|9G|C)2RkWW_y_a?S&Yp-e_r`1r=+nYfuE(;8D&d!2-"
    b")$|6U=kOBUGW3bip$Sjd8#5cfE9V1t<<d~kt-<efw))fds-7|x$?iH(_S0Mab2Ec-I%Usa{jEJ_w%DTDeGk8I!j`BX?P{YzJaW?qPgW%49emnpPV82ne@BC-"
    b"Scju~?a`}=7yH!U0`67(5F-U*s>7ELJ&3N;tVV_WLRZNEO>qR-ORRX$Xx_mT%(GJNS2=WrwK`nT7f8cT09!%KgE~8$Ypk|#!92mF;Zi7kGQ)ysjd4;n9$W0`"
    b"q^K4`rizHsq}w6ZnuQE1g?a!40wvF18tpN!e@ci<pT;QU(PgoxIh@}vOQilxqa?7551*K#V54n5ddUL87FI*KPIP!loj_4wHUr4-"
    b"+GzK2uG#F|I*Um#f*Wf0waCIt&`*wCHY5T@OOcjsiVSrWjr&yQk*Q-R@X~pIb&$Ss{Al2~NA_8P<Y^jV&a>`~Ot?nM0B@@Kot5e!;qZ<X>*;5+TiPHxi%#-"
    b"}PM;vB@E=G2M<wC@Qpuf&pWRIGaB#m5%!hmC?lz7doE*Q;r!DPbk`LNQ{o2Oe1L)!`PRq@~MN4htZ0!O7I@^iUdV*}(g=i%u#I$W3EkO@Yc-RA7J*XdwID3f"
    b"G+Jiu@BAlEa*7i0|mL41~t~SmOIkqnDPL`mDOLsd?S4(RLOFJ7*9xg5cPWS(bLHkckYF%$voBtm~7h7APwT+yMwWpJfGw8nnKYD_eTG!Iu&ITk-%lRm-hn89"
    b"iAWo~zCB)AMu;k;j6y)ON<Kh;erRJ0n<NQZ^CH^_ak)LQ>Sv+(mHVPaZ>EC1g?>_yX=zsO^=rp(UHZ=~)+9!icZwq2F@?ND{wM9n`uBRwVJ`L4a3qp2Fw2DI"
    b"ndV>{utxWQ1jLkXMaRL4#FIw*c+M1UNtFPr9$h($n&Z!NgYq6bETav};18wG4jz<wcq=LEn0}QOH)i%kEXN&4gJSd$s@cLv8?7tR5!#%t3pIRPYzr6~jaATG"
    b"moofxr^dgMm#Pl!Xej{lB!#$dk^MK{1_FwX71A3oVP!uG8bNZP=(EtSWwmB?>pcu2znHs9V(HVAfq9}{2flhAT-G8(xM6iw~WtB006<f?%5-"
    b"DD>6;SAz+A=;hRLNs@oOq^4qa=cj{Z8flW4BMFxRyxKUCb(#RO0zQzosy|xZY%n)X;Gd<HfefDSDmEI=m{qSBDNsWlh24>^o&;#I-"
    b"bvGwRJ8MPtDap<bDlGf&>U?0cR!5|__d%1%7reR&YYI7mgnU(u-"
    b"$q;uW5X_o~%el(Q|bXE0bevk_s%HLrd#<DKXpa&H&|E*gdroW{!n%Jp~$o<<@9(<Vw`a~G#?5kPHvWFRZbmVN$gAM_%NTj1u4eG}hYRiRc8(DHfhPQrw`Nfl"
    b"UN>wX=YFZ7J6R@CH7A8c_Mz8N}c*g3iAZW#%)#gmA3H1%vjffWh$|7HgSg8a?oA;dy-QrKcDtW1uUf?XP*0)*015XmG*gA@Hu^`Upv)%M&kHj_nxDBs&#o6V"
    b"3X=pUmFmC}x*P$#>S|JBm7A%sQgbGmN4z4Icv^WKPoOF0kBy4ausJgZ%wCBYN>DZ<?aLgCq0Ae#QkVe{NUTgUlhaP0oeifqj-T@0=;-"
    b"rb5RrwAlAiIxr)?}({w!7BMe{8!LKa!<&p<%yJ)b>uaOJ3NeV&x%;9N5;Bs{qrwi{r=bx4$p;8{ak8RDnmpNBs8~x&Qsi4~F}{Bjz3#ejLg5r*I1VqqwfeMI"
    b"VRa{3(iy^j`yW9s@iMDfj~riTd9I3?3sq-u?fBK!f)0u>g-"
    b"z9&h^oL2<?S_buSZD34e8|DX)w{QG+UW0c1WOMg&O3IBbW=`qS<&*cw_Kl#7=F^^FmPniCos8av?^yv@Ef46aeP*!RGVeuYU|Cr1F6y&1&e=+-"
    b"GoX6br2WNo(zcP`g3Np&?2e2Q$mJhv1%lP~1e*vH*cVP"
)

H1_README = """# H1 — Primer asistente por consola

> Ejemplo privado de Laura. Mostrar solo después del intento propio del alumnado.

## Objetivo

Construir y comprobar una primera versión pequeña de MiniJarvis utilizando únicamente los contenidos trabajados en H1.

Esta versión permite observar:

- la estructura básica de un programa Java;
- la clase `Main` y el método `main`;
- salida por consola;
- variables y constantes;
- tipos `String`, `int` y `boolean`;
- entrada mediante `Scanner`;
- conversión de texto a número;
- un cálculo sencillo;
- una comparación que produce un valor booleano.

No utiliza todavía menús, bucles, `switch`, colecciones, varias clases propias, ficheros, persistencia ni IA real.

---

## Arquitectura de evidencias

Versión estable:

```text
h1-entrega
```

El repositorio y este README son la evidencia técnica canónica.

- Diario individual evolutivo: `../FUENTES-CURSO/01-Diario-individual-MiniJarvis.xlsx`.
- Scrum de equipo evolutivo: `../FUENTES-CURSO/02-Scrum-equipo-MiniJarvis.xlsx`.
- Entrega Moodle mínima: `../ENTREGAS-MOODLE/H1-entrega.md`.

No se crean informes paralelos de ejecución, pruebas, defensa o uso de IA.

---

## Estructura

```text
h1-primer-asistente/
├── README.md
└── src/
    └── Main.java
```

---

## Compilación y ejecución

Desde la carpeta `h1-primer-asistente`:

```bash
javac -d out src/Main.java
java -cp out Main
```

---

## Ejecución comprobable [EQUIPO]

Ejemplo con datos ficticios:

```text
Hola, soy MiniJarvis.
¿Cómo te llamas? Laura
¿Cuántas horas has practicado Programación? 4
Hola, Laura.
Si la próxima semana practicas una hora más, serán 5 horas.
¿Has practicado al menos 3 horas? true
```

La salida puede cambiar según los datos introducidos.

Si en la entrada numérica se escribe un texto no convertible, `Integer.parseInt` produce un error de ejecución. En H1 se observa y se explica ese comportamiento; todavía no se incorpora tratamiento de excepciones.

---

## Qué ocurre en el programa

### Entrada de texto

```java
String userName = scanner.nextLine();
```

`nextLine()` devuelve texto y ese valor se guarda en una variable `String`.

### Entrada numérica

La entrada de consola sigue llegando inicialmente como texto:

```java
String hoursText = scanner.nextLine();
```

Después se convierte:

```java
int studyHours = Integer.parseInt(hoursText);
```

### Cálculo

```java
int nextWeekHours = studyHours + EXTRA_HOURS_NEXT_WEEK;
```

El programa suma una hora al valor introducido.

### Comparación

```java
boolean enoughPractice = studyHours >= REFERENCE_HOURS;
```

La comparación produce `true` o `false`.

No se utiliza todavía ese booleano para ejecutar caminos diferentes del programa.

---

## Decisiones del ejemplo

- Se mantiene todo el código propio dentro de `Main`.
- Se usa `Scanner` para leer por consola.
- La entrada numérica se recibe primero como `String`.
- La conversión se realiza mediante `Integer.parseInt`.
- El cálculo utiliza una constante con nombre.
- La comparación se guarda en una variable `boolean`.
- No se introducen contenidos de hitos posteriores.

---

## Comprobaciones realizadas

Caso utilizado en el ejemplo:

```text
Nombre: Laura
Horas: 4
```

Resultado esperado:

```text
Horas calculadas para la semana siguiente: 5
Comparación con 3 horas: true
```

También puede probarse, por ejemplo:

```text
Nombre: Laura
Horas: 2
```

En ese caso:

```text
Horas calculadas para la semana siguiente: 3
Comparación con 3 horas: false
```

---

## Defensa de Laura [INDIVIDUAL]

Laura debe poder localizar y explicar en el código:

- dónde comienza la ejecución;
- una variable;
- una constante;
- un literal;
- el objeto `Scanner`;
- qué devuelve `nextLine`;
- por qué es necesaria la conversión numérica;
- qué operación realiza el cálculo;
- por qué la comparación produce un `boolean`;
- cómo compilar y ejecutar el programa.

También debe poder modificar un dato sencillo, volver a ejecutar y explicar el cambio.

La defensa se realiza sobre el producto real. No necesita una plantilla escrita independiente.

---

## Idea clave

```text
No es un MiniJarvis avanzado.

Es una primera versión Java pequeña
que Laura puede ejecutar, comprobar,
modificar y explicar por completo.
```
"""


def canonical_xlsx(payload: bytes) -> bytes:
    """Recupera el XLSX canónico conservando su serialización byte a byte."""
    return zlib.decompress(base64.b85decode(payload))


def create_course_workbooks() -> None:
    target = EXAMPLES / "FUENTES-CURSO"
    target.mkdir()
    (target / "01-Diario-individual-MiniJarvis.xlsx").write_bytes(canonical_xlsx(DIARY_XLSX))
    (target / "02-Scrum-equipo-MiniJarvis.xlsx").write_bytes(canonical_xlsx(SCRUM_XLSX))


def technical_sections(code: str) -> str:
    sections = {
        "H0": """## Proceso de equipo [EQUIPO]\n\n- Backlog: diseñar base, construir, medir estabilidad, revisar y mejorar.\n- Definición de terminado: torre autoportante y prueba registrada.\n- Retrospectiva: ensanchar la base antes de aumentar altura.\n\n## Aportación de Laura [INDIVIDUAL]\n\nLaura documentó la prueba y puede explicar el cambio de diseño. H0 no usa GitHub, tags ni Sites; la fotografía no-code se conserva en Drive solo si aporta evidencia.""",
        "H1": """## Ejecución comprobable [EQUIPO]\n\n```text\nMiniJarvis: ¿Cómo te llamas?\nLaura\nHola, Laura. Soy MiniJarvis.\n```\n\nEl README contiene requisitos, compilación, ejecución y ejemplo. La versión evaluada es `h1-entrega`.""",
        "H2": """## Pruebas y depuración [EQUIPO]\n\nCasos: ayuda, saludo, estado, comando desconocido y salir. Un breakpoint después de leer el comando permitió observar `command`, `running` y `userName`; se corrigió la comparación con `equalsIgnoreCase`.""",
        "H3": """## Decisión sobre la colección [EQUIPO]\n\nSe usa `ArrayList<String>` porque conserva un número variable de recuerdos durante la ejecución. Se prueban memoria vacía, un recuerdo, varios y repetidos.""",
        "H4": """## Diseño de clases [EQUIPO]\n\n```mermaid\nclassDiagram\n  Main --> Agent\n  Agent --> Memory\n```\n\nEl diagrama de clases forma parte del README. El diagrama de comportamiento es práctica coordinada opcional de Entornos, no entrega obligatoria de Programación.""",
        "H5": """## Refactorización y patrón [EQUIPO]\n\n`Tool` define el contrato de las acciones. La semejanza con Command es encapsular cada acción ejecutable; no se añaden invocadores o fábricas sin necesidad. La revisión se acredita con historial y PR/revisión de código.""",
        "H6": """## Persistencia, errores y seguridad [EQUIPO]\n\nLas rutas son relativas, los fallos se controlan sin ocultarlos y los logs usan datos ficticios. La prueba guarda un recuerdo, reinicia el programa y verifica su recuperación.""",
        "H7": """## IA responsable [EQUIPO]\n\nLa integración es simulada o autorizada, rechaza datos sensibles y presenta las respuestas como propuestas. El registro relevante se mantiene en diario o Scrum, no en un archivo paralelo.""",
        "HF": """## Demostración final [EQUIPO → COMPROBACIÓN INDIVIDUAL]\n\nLa demo parte de un entorno limpio, usa `hf-final` y recorre una prueba representativa. Laura defiende una decisión propia, localiza el artefacto, muestra la prueba y explica una mejora. La recuperación se limita a evidencias concretas no superadas.""",
    }
    return sections[code]


def create_readmes() -> None:
    for folder, data in HITOS.items():
        code, title, objective, decision, result, version = data
        if code == "H1":
            (EXAMPLES / folder / "README.md").write_text(H1_README, encoding="utf-8")
            continue
        github = "H0 no exige GitHub, tag ni Sites." if code == "H0" else f"Versión estable: `{version}`. El repositorio y su README son la evidencia técnica canónica."
        (EXAMPLES / folder / "README.md").write_text(
            f"""# {code} — {title}\n\n> Ejemplo privado de Laura. Mostrar solo después del intento propio del alumnado.\n\n## Objetivo\n\n{objective}\n\n## Arquitectura de evidencias\n\n{github}\n\n- Diario individual evolutivo: `../FUENTES-CURSO/01-Diario-individual-MiniJarvis.xlsx`.\n- Scrum de equipo evolutivo: `../FUENTES-CURSO/02-Scrum-equipo-MiniJarvis.xlsx`.\n- Entrega Moodle mínima: `../ENTREGAS-MOODLE/{code}-entrega.md`.\n\n{technical_sections(code)}\n\n## Decisión y resultado\n\n- Decisión: {decision}\n- Resultado probado: {result}\n\n## Defensa de Laura [INDIVIDUAL]\n\nLaura localiza su aportación, reproduce una prueba y explica una decisión sin apoyarse en una plantilla de defensa separada.\n""",
            encoding="utf-8",
        )


def create_moodle_deliveries() -> None:
    target = EXAMPLES / "ENTREGAS-MOODLE"
    target.mkdir()
    for _, data in HITOS.items():
        code, title, objective, decision, result, version = data
        if code == "H0":
            items = "1. Ticket o texto breve del equipo.\n2. Confirmación de Scrum actualizado.\n3. Enlace opcional a una fotografía no-code en Drive.\n\nNo se entrega GitHub, tag ni Site."
        elif code == "H1":
            items = "1. Tag `h1-entrega` o commit estable.\n2. Confirmación de diario y Scrum actualizados.\n3. Evidencia no-code excepcional, solo si existe."
        elif code == "HF":
            items = "1. Release o tag `hf-final`.\n2. Site personal final.\n3. Site de equipo final.\n4. Defensa individual.\n5. Recuperación concreta solo si procede."
        else:
            items = f"1. Tag `{version}` o commit estable.\n2. Confirmación de diario y Scrum actualizados.\n3. Evidencia no-code excepcional, solo si existe."
        links = "" if code == "H1" else "- Enlaces: `URL_RESTRINGIDA_EJEMPLO`.\n\n"
        note = (
            "No volver a copiar URLs estables. "
            if code == "H1" else ""
        ) + "No se adjuntan README, capturas, registros IA ni PDF/XLSX rutinarios."
        (target / f"{code}-entrega.md").write_text(
            f"# Entrega Moodle de ejemplo — {code}\n\n- Equipo: Equipo Ada.\n- Alumna: Laura.\n{links}{items}\n\n{note}\n",
            encoding="utf-8",
        )


def create_sites() -> None:
    target = EXAMPLES / "PORTFOLIOS-PERIODICOS"
    target.mkdir()
    for checkpoint, scope in (("C1", "H1–H3"), ("C2", "H4–H5"), ("HF", "H1–H7")):
        (target / f"{checkpoint}-site-personal.md").write_text(
            f"# Site personal de Laura — {checkpoint}\n\nSíntesis de {scope}: aportación individual, aprendizaje, evidencia profunda y decisión que puede defender. No replica el diario ni el README.\n",
            encoding="utf-8",
        )
        (target / f"{checkpoint}-site-equipo.md").write_text(
            f"# Site del Equipo Ada — {checkpoint}\n\nSíntesis de {scope}: incremento, prueba principal, decisión de equipo y enlace al repositorio. No replica Scrum ni Moodle.\n",
            encoding="utf-8",
        )


def create_publication_readme() -> None:
    (EXAMPLES / "README-PUBLICACION.md").write_text(
        """# Ejemplos de Laura — publicación diferida\n\nMaterial docente privado. Cada ejemplo se muestra solo después del intento propio del alumnado o cuando existe una primera versión defendible.\n\n## Modelo canónico\n\n- `FUENTES-CURSO/`: un diario individual y un Scrum de equipo, evolutivos durante todo el curso.\n- cada hito: código y un README técnico integrado; no hay `docs/` paralelos.\n- `ENTREGAS-MOODLE/`: una entrega mínima por hito, alineada con las tareas reales.\n- `PORTFOLIOS-PERIODICOS/`: Sites únicamente en C1, C2 y HF.\n- las marcas `[INDIVIDUAL]`, `[EQUIPO]` y `[EQUIPO → COMPROBACIÓN INDIVIDUAL]` distinguen autoría y producto compartido.\n\nLos ejemplos ayudan a interpretar criterios y preparar la defensa; no son plantillas para copiar ni se incluyen en el paquete Moodle del alumnado.\n""",
        encoding="utf-8",
    )


def main() -> None:
    clean_legacy()
    create_course_workbooks()
    create_readmes()
    create_moodle_deliveries()
    create_sites()
    create_publication_readme()
    print("Ejemplos de Laura regenerados con arquitectura mínima")


if __name__ == "__main__":
    main()

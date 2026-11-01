#!/usr/bin/env python3
"""Gera a composicao (index.html) de um episodio a partir de roteiro.json.

Problema que resolve: escrever o index.html a mao custa ~40 min por episodio e
erra em tres pontos que so aparecem no render — tempo de cena, fonte que estoura
os 840 px e cena que nao fecha no fim do video. O roteiro ja tem tudo; o HTML e
mecanico.

Entrada (na pasta do episodio):

    roteiro.json        cenas, textos, fonte por cena, falas
    tempos_cenas.json   opcional, saida de scripts/remapear.py (tempo real)

Sem `tempos_cenas.json` o script distribui o tempo por numero de caracteres da
fala e avisa que o tempo e **provisorio**: nesse estado serve para conferir
texto e composicao, nao para render final.

Saida:

    index.html          composicao completa, 1080x1920, 30 fps, GSAP
    narracao.txt        uma fala por paragrafo (so com --narracao)

O que o script garante (contrato de docs/ARQUITETURA.md §2 e §3):

- 1080x1920, fps 30, `data-start="0"` na stage, ids unicos, classe `clip`;
- cenas em sequencia, sem sobreposicao, cobrindo o video ate o fim;
- `font-size` explicito por cena (sem isso o contrato reprova);
- timeline do GSAP com o inicio real de cada cena;
- `window.__timelines.<id>` e o seek `?t=` para QA por frame.

O que ele **nao** garante: que a linha caiba em 840 px. Fonte e tinta nao sao a
mesma coisa — medir com scripts/medir-texto.ps1 no frame renderizado.

Layouts (v2, docs/LAYOUTS.md §10): a cena pode trazer `"tipo": "<layout>"`.
O registro em templates/layouts/registro.json e a fonte da verdade; o CSS e o
JS da biblioteca sao **inlinados** no index.html (o render nao depende de copia
por episodio). Sem `tipo`, a saida e identica ao v1 — o que sustenta 001-007.

Uso:

    .venv\\Scripts\\python.exe scripts\\gerar-episodio.py episodios\\005-voo-19
    .venv\\Scripts\\python.exe scripts\\gerar-episodio.py episodios\\006-passo-dyatlov --narracao
    .venv\\Scripts\\python.exe scripts\\gerar-episodio.py episodios\\005-voo-19 --check
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

LARGURA_UTIL = 840          # px uteis da coluna de texto (template v1)
FONTE_MIN, FONTE_MAX = 72, 190
AVANCO_CAPITULAR = 0.59     # avanco medio de uma capitular Georgia, em em
DURACAO_MIN_CENA = 2.2      # s; abaixo disso a cena nao da tempo de ler
ALERTA_CENA_LONGA = 6.0     # s; acima disso a retention do 004 caiu

RAIZ = Path(__file__).resolve().parent.parent
DIR_LAYOUTS = RAIZ / "templates" / "layouts"


def carregar_registro() -> dict:
    """Le templates/layouts/registro.json: id -> metadados do layout."""
    caminho = DIR_LAYOUTS / "registro.json"
    if not caminho.exists():
        raise SystemExit(f"registro de layouts ausente: {caminho}")
    dados = json.loads(caminho.read_text(encoding="utf-8-sig"))
    return {lay["id"]: lay for lay in dados["layouts"]}


REGISTRO = carregar_registro()
LAYOUTS = tuple(REGISTRO)

# campos que o layout nao vive sem (os demais de `campos` sao opcionais)
OBRIGATORIOS = {
    "checklist": ["itens"],
    "chart-grow": ["valores"],
}

BASE_CSS = """  * { box-sizing: border-box; }
  html, body { margin: 0; padding: 0; background: #0A0A0B; }
  #stage {
    position: relative;
    width: 1080px;
    height: 1920px;
    overflow: hidden;
    background: #0A0A0B;
    font-family: Georgia, "Times New Roman", serif;
    color: #E8E6E1;
  }
  .bg {
    position: absolute;
    inset: -90px;
    background:
      radial-gradient(900px 700px at 28% 18%, rgba(178,58,46,0.13), transparent 62%),
      radial-gradient(1200px 900px at 72% 82%, rgba(60,70,90,0.18), transparent 66%),
      linear-gradient(160deg, #101014 0%, #0A0A0B 55%, #07070A 100%);
    transform: scale(1.06);
  }
  .vignette {
    position: absolute;
    inset: 0;
    box-shadow: inset 0 0 430px 130px rgba(0,0,0,0.88);
  }
  .frame {
    position: absolute;
    inset: 64px;
    border: 1px solid rgba(232,230,225,0.10);
  }
  .mark {
    position: absolute;
    top: 112px;
    left: 120px;
    font-family: Inter, Arial, sans-serif;
    font-size: 21px;
    letter-spacing: 8px;
    color: #6B6B70;
    z-index: 5;
  }
  .dossier {
    position: absolute;
    top: 112px;
    right: 120px;
    font-family: Inter, Arial, sans-serif;
    font-size: 21px;
    letter-spacing: 6px;
    color: #4A4A50;
    z-index: 5;
  }
  .foot {
    position: absolute;
    bottom: 190px;
    left: 120px;
    right: 120px;
    font-family: Inter, Arial, sans-serif;
    font-size: 19px;
    letter-spacing: 4px;
    color: #45454C;
    z-index: 5;
  }
  .scene {
    position: absolute;
    inset: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 0 120px;
    z-index: 2;
  }
  .scene h1 {
    margin: 0;
    font-weight: 400;
    line-height: 0.99;
    letter-spacing: -2px;
    text-wrap: balance;
  }
  .kicker {
    font-family: Inter, Arial, sans-serif;
    font-size: 24px;
    letter-spacing: 7px;
    color: #B23A2E;
    margin-bottom: 30px;
  }
  .small {
    display: block;
    margin-top: 34px;
    font-family: Inter, Arial, sans-serif;
    font-size: 28px;
    line-height: 1.45;
    letter-spacing: 4px;
    color: #6B6B70;
  }
  .accent {
    width: 280px;
    height: 2px;
    margin-top: 40px;
    background: #B23A2E;
    transform-origin: left center;
  }
  #fade {
    position: absolute;
    inset: 0;
    background: #000;
    opacity: 0;
    z-index: 20;
    pointer-events: none;
  }
"""


def carregar(caminho: Path) -> dict:
    if not caminho.exists():
        raise SystemExit(f"roteiro nao encontrado: {caminho}")
    dados = json.loads(caminho.read_text(encoding="utf-8"))
    if not dados.get("cenas"):
        raise SystemExit(f"{caminho}: nenhuma cena")
    return dados


def estimar_fonte(titulo: list[str], letter_spacing: float = -2) -> int:
    """Primeira estimativa da fonte: a linha mais longa tem de caber em 840 px.

    E chute, nao medida: `AVANCO_CAPITULAR` sai do 005 (16 caracteres a 82 px
    deram 772 px de tinta). Serve para o render nao nascer grotesco; o valor
    final vem de scripts/medir-texto.ps1.
    """
    maior = max(len(linha) for linha in titulo)
    px = LARGURA_UTIL / (AVANCO_CAPITULAR * maior)
    px = px - letter_spacing * 0.5
    return int(max(FONTE_MIN, min(FONTE_MAX, math.floor(px / 2) * 2)))


def tempos_provisorios(cenas: list[dict], duracao: float) -> list[dict]:
    """Distribui o tempo por caracteres de fala, com piso por cena."""
    pesos = []
    for c in cenas:
        fala = (c.get("fala") or "").strip()
        pesos.append(max(1, len(fala)))
    total = sum(pesos)
    brutos = [duracao * p / total for p in pesos]
    # piso: cena que nao da tempo de ler puxa tempo das vizinhas
    sobra = sum(max(0.0, DURACAO_MIN_CENA - b) for b in brutos)
    folga = [b - DURACAO_MIN_CENA for b in brutos if b > DURACAO_MIN_CENA]
    escala = 1.0 if not folga or sobra <= 0 else 1 - sobra / sum(folga)
    ajustados = [b if b <= DURACAO_MIN_CENA else DURACAO_MIN_CENA + (b - DURACAO_MIN_CENA) * escala
                 for b in brutos]
    fator = duracao / sum(ajustados)
    ajustados = [a * fator for a in ajustados]

    saida, inicio = [], 0.0
    for i, dur in enumerate(ajustados):
        dur = round(dur, 3)
        saida.append({"cena": i + 1, "inicio": round(inicio, 3), "start": round(inicio, 3),
                      "duration": dur, "fim": round(inicio + dur, 3)})
        inicio += dur
    saida[-1]["fim"] = round(saida[-1]["start"] + saida[-1]["duration"], 3)
    return saida


def carregar_tempos(caminho: Path, cenas: list[dict], duracao: float) -> tuple[list[dict], bool]:
    if not caminho.exists():
        return tempos_provisorios(cenas, duracao), False
    dados = json.loads(caminho.read_text(encoding="utf-8"))
    if len(dados) != len(cenas):
        raise SystemExit(
            f"{caminho.name}: {len(dados)} tempos para {len(cenas)} cenas — "
            f"remapear de novo depois de mexer no roteiro")
    return dados, True


def validar(roteiro: dict, tempos: list[dict]) -> list[str]:
    avisos: list[str] = []
    cenas = roteiro["cenas"]
    ids = [c["id"] for c in cenas]
    if len(set(ids)) != len(ids):
        raise SystemExit(f"ids repetidos: {ids}")
    for i, c in enumerate(cenas):
        if not c.get("titulo"):
            raise SystemExit(f"{c['id']}: sem titulo")
        linhas = len(c["titulo"]) + len(c.get("pequeno") or [])
        if linhas > 5:
            avisos.append(f"{c['id']}: {linhas} linhas de texto (o template pede 4)")
        tipo = c.get("tipo")
        if tipo is not None:
            if tipo not in REGISTRO:
                raise SystemExit(f"{c['id']}: tipo desconhecido '{tipo}' — "
                                 f"validos: {', '.join(LAYOUTS)}")
            for campo in OBRIGATORIOS.get(tipo, []):
                if not c.get(campo):
                    raise SystemExit(f"{c['id']}: layout '{tipo}' exige o campo '{campo}'")
            if tipo == "chart-grow":
                vals = c.get("valores") or []
                if not all(isinstance(v, (int, float)) for v in vals) or not 2 <= len(vals) <= 5:
                    raise SystemExit(f"{c['id']}: chart-grow pede 2 a 5 valores numericos")
            if tipo == "checklist" and not 2 <= len(c.get("itens") or []) <= 5:
                raise SystemExit(f"{c['id']}: checklist pede 2 a 5 itens")
            if c.get("asset") and not (c.get("credito") and c.get("licenca")):
                raise SystemExit(f"{c['id']}: asset exige 'credito' e 'licenca' "
                                 f"(docs/LAYOUTS.md §4)")
            if tipo in ("zoom-through",) and i == len(cenas) - 1:
                avisos.append(f"{c['id']}: zoom-through na ultima cena (o corte nao existe)")
    for i, t in enumerate(tempos):
        if t["duration"] > ALERTA_CENA_LONGA:
            avisos.append(f"cena {i + 1} ({cenas[i]['id']}): {t['duration']:.2f} s "
                          f"(acima de {ALERTA_CENA_LONGA:g} s)")
        if t["duration"] < DURACAO_MIN_CENA * 0.7:
            avisos.append(f"cena {i + 1} ({cenas[i]['id']}): {t['duration']:.2f} s "
                          f"(curta demais para ler)")
    fim = tempos[-1]["start"] + tempos[-1]["duration"]
    if abs(fim - roteiro["duracao"]) > 0.3:
        avisos.append(f"ultima cena termina em {fim:.2f} s de {roteiro['duracao']:g} s")
    return avisos


def css_cenas(cenas: list[dict]) -> str:
    regras = []
    for c in cenas:
        px = c.get("fonte_px") or estimar_fonte(c["titulo"], c.get("letter_spacing", -2))
        c["fonte_px"] = px
        ls = c.get("letter_spacing")
        extra = f" letter-spacing: {ls}px;" if ls is not None else ""
        regras.append(f"  .{c['id']} h1 {{ font-size: {px}px;{extra} }}")
        tipo = c.get("tipo")
        if tipo:
            escala = REGISTRO[tipo].get("escala_fonte", 1.0)
            if abs(escala - 1.0) > 0.001:
                regras.append(f"  .{c['id']}.layout-{tipo} h1 "
                              f"{{ font-size: {int(round(px * escala))}px;{extra} }}")
    return "\n".join(regras) + "\n"


def _core(c: dict) -> str:
    """Miolo de texto comum a todos os layouts: identico ao v1."""
    partes = []
    if c.get("kicker"):
        partes.append(f'    <div class="kicker">{c["kicker"]}</div>')
    partes.append(f'    <h1>{"<br>".join(c["titulo"])}</h1>')
    if c.get("pequeno"):
        partes.append(f'    <span class="small">{"<br>".join(c["pequeno"])}</span>')
    if c.get("acento"):
        partes.append('    <div class="accent"></div>')
    return "\n".join(partes)


def _moldura(c: dict, core: str) -> str:
    """Estrutura visual do layout em volta do texto (templates/layouts/layouts.css)."""
    tipo = c["tipo"]
    asset = c.get("asset")
    img = f' style="background-image: url(\'{asset}\')"' if asset else ""

    if tipo == "orbit":
        spokes = "\n".join(f'      <i style="transform: rotate({a}deg)"></i>'
                           for a in (0, 90, 180, 270))
        orbs = "\n".join(f'      <span class="orb{" hot" if i == 0 else ""}" '
                         f'style="transform: rotate({a}deg) translateY(-410px)"></span>'
                         for i, a in enumerate((0, 90, 180, 270)))
        return (f'    <div class="ly-decor">\n      <div class="ring">\n{spokes}\n{orbs}\n'
                f'      </div>\n    </div>\n    <div class="core">\n{core}\n    </div>')

    if tipo == "couch-wall":
        celulas = []
        for i in range(12):
            estilo = f' style="background-image: url(\'{asset}\')"' if asset and i < 3 else ""
            celulas.append(f'      <span{estilo}></span>')
        return (f'    <div class="wall">\n' + "\n".join(celulas) + '\n    </div>\n'
                f'    <div class="scrim"></div>\n    <div class="core">\n{core}\n    </div>')

    if tipo == "ui-world":
        url = c.get("janela", "")
        return (f'    <div class="win">\n'
                f'      <div class="bar"><b></b><b></b><b></b><div class="url">{url}</div></div>\n'
                f'      <div class="body">\n        <div class="core">\n{core}\n        </div>\n'
                f'      </div>\n    </div>')

    if tipo == "frame-break":
        return (f'    <div class="fb-frame"></div>\n    <div class="fb-mask"></div>\n'
                f'    <div class="core">\n{core}\n    </div>')

    if tipo == "phone-mockup":
        return (f'    <div class="phone">\n      <div class="notch"></div>\n'
                f'      <div class="screen">\n        <div class="core">\n{core}\n        </div>\n'
                f'      </div>\n      <div class="home"></div>\n    </div>')

    if tipo == "checklist":
        lis = "\n".join(
            f'      <li class="item"><span class="box"><svg viewBox="0 0 24 24">'
            f'<path d="M4 12.5 L9.5 18 L20 6"/></svg></span>'
            f'<span class="txt">{item}</span></li>' for item in c.get("itens") or [])
        return (f'    <div class="core">\n{core}\n    </div>\n'
                f'    <ul class="list">\n{lis}\n    </ul>')

    if tipo == "headline-wall":
        man = c.get("manchetes") or (c["titulo"] * 3)[:6]
        rows = "\n".join(f'      <span>{m}</span>' for m in man)
        return (f'    <div class="wall">\n{rows}\n    </div>\n'
                f'    <div class="scrim"></div>\n    <div class="core">\n{core}\n    </div>')

    if tipo == "chart-grow":
        valores = c.get("valores") or []
        rotulos = c.get("rotulos") or [str(v) for v in valores]
        maior = max(valores) if valores else 1
        barras = "\n".join(
            f'      <div class="bar{" hot" if v == maior else ""}">'
            f'<u data-valor="{v}">0</u><b style="height: {round(100 * v / maior)}%"></b>'
            f'<i>{rot}</i></div>'
            for v, rot in zip(valores, rotulos))
        return (f'    <div class="core">\n{core}\n    </div>\n'
                f'    <div class="chart">\n{barras}\n    </div>')

    if tipo == "green-screen":
        classe = "key asset" if asset else "key"
        return (f'    <div class="{classe}"{img}></div>\n    <div class="keyline"></div>\n'
                f'    <div class="core">\n{core}\n    </div>')

    if tipo == "paper-cut":
        return (f'    <div class="layer l1"></div>\n    <div class="layer l2"></div>\n'
                f'    <div class="layer l3"></div>\n'
                f'    <div class="core">\n{core}\n    </div>')

    if tipo == "doodle-boil":
        trilhas = [
            "M 70 152 C 150 46, 430 26, 700 66 C 846 88, 862 196, 640 240 "
            "C 424 284, 118 268, 74 196 C 58 168, 58 160, 70 152",
            "M 74 148 C 158 52, 420 30, 704 62 C 840 80, 856 200, 636 236 "
            "C 420 278, 122 274, 70 192 C 56 166, 60 156, 74 148",
            "M 66 156 C 146 42, 436 22, 696 70 C 852 94, 866 190, 646 244 "
            "C 428 290, 114 262, 78 200 C 60 172, 54 162, 66 156",
        ]
        svgs = "\n".join(f'      <svg viewBox="0 0 888 300" preserveAspectRatio="none">'
                         f'<path d="{d}"/></svg>' for d in trilhas)
        return (f'    <div class="boil">\n{svgs}\n    </div>\n'
                f'    <div class="core">\n{core}\n    </div>')

    if tipo == "vertigo":
        return f'    <div class="ly-decor"></div>\n    <div class="core">\n{core}\n    </div>'

    if tipo == "cover-story":
        masthead = c.get("masthead", "ARQUIVO")
        edicao = c.get("edicao", "N\u00ba 45 \u00b7 ARQUIVO")
        chamada = c.get("manchete", "")
        return (f'    <div class="cover">\n      <div class="masthead">{masthead}</div>\n'
                f'      <div class="rule"></div>\n      <div class="issue">{edicao}</div>\n'
                f'      <div class="core">\n{core}\n      </div>\n'
                f'      <div class="call">{chamada}</div>\n      <div class="barcode"></div>\n'
                f'    </div>')

    if tipo == "glass-type":
        return f'    <div class="pane"></div>\n    <div class="core">\n{core}\n    </div>'

    # digital-zoom, zoom-through, pull-back: o texto e a propria moldura
    return f'    <div class="core">\n{core}\n    </div>'


def secao(c: dict, i: int, t: dict) -> str:
    tipo = c.get("tipo")
    classe = f'scene {c["id"]} clip'
    atributos = ""
    if tipo:
        classe += f" layout layout-{tipo}"
        atributos = f' data-layout="{tipo}"'
        if c.get("asset"):
            atributos += f' data-asset="{c["asset"]}"'
            atributos += f' data-credito="{c.get("credito", "")}"'
            atributos += f' data-licenca="{c.get("licenca", "")}"'
    partes = [
        f'  <section class="{classe}" id="{c["id"]}" '
        f'data-start="{t["start"]:.3f}" data-duration="{t["duration"]:.3f}" '
        f'data-track-index="1" data-cena="{i + 1}"{atributos}>'
    ]
    partes.append(_moldura(c, _core(c)) if tipo else _core(c))
    partes.append("  </section>")
    return "\n".join(partes)


def html(roteiro: dict, tempos: list[dict]) -> str:
    cenas = roteiro["cenas"]
    dur = roteiro["duracao"]
    audio = roteiro.get("audio") or {}
    vol_voz = audio.get("voz", 1.0)
    vol_drone = audio.get("drone", 0.16)
    comp = roteiro["composition_id"]
    marca = roteiro.get("marca", "DOSSIÊ 45")
    dossie = roteiro.get("dossie", "")
    rodape = roteiro.get("rodape", "")
    offset = roteiro.get("entrada_offset", 0.05)
    zoom = roteiro.get("zoom_fim", 1.14)

    # entrada do texto: 0,05 s depois da troca de cena (a cena ja esta no ar)
    entradas = []
    for i, t in enumerate(tempos):
        entradas.append((cenas[i]["id"], t["start"] if i == 0 else round(t["start"] + offset, 2)))

    linhas_entrada = "\n".join(
        f'      ["{cid}", {t:.2f}],' for cid, t in entradas).rstrip(",")

    corpo = "\n\n".join(secao(c, i, t) for i, (c, t) in enumerate(zip(cenas, tempos)))

    # v2: so entra a biblioteca se alguma cena declarar `tipo`. Sem `tipo` a
    # saida continua byte a byte igual ao v1 (001-007 dependem disso).
    usar_layouts = any(c.get("tipo") for c in cenas)
    css_total = BASE_CSS + css_cenas(cenas)
    bloco_layouts = ""
    if usar_layouts:
        css_total += ("\n  /* ---------- templates/layouts/layouts.css ---------- */\n"
                      + (DIR_LAYOUTS / "layouts.css").read_text(encoding="utf-8"))
        js_lay = (DIR_LAYOUTS / "layouts.js").read_text(encoding="utf-8")
        bloco_layouts = f'  <script>\n{js_lay}  </script>\n'

    if usar_layouts:
        animacao = """      const lay = root.dataset.layout || "texto";
      const fn = (window.__layouts && window.__layouts[lay]) || window.__layouts.texto;
      fn(root, tl, t, dur, start);"""
    else:
        animacao = """      tl.from(root.querySelector("h1"), { opacity: 0, y: 36, duration: 0.55, ease: "power2.out" }, t);
      const accent = root.querySelector(".accent");
      if (accent) tl.from(accent, { scaleX: 0, duration: 0.5, ease: "power2.out" }, t + 0.10);
      const small = root.querySelector(".small");
      if (small) tl.from(small, { opacity: 0, y: 14, duration: 0.45, ease: "power2.out" }, t + 0.18);
      const kicker = root.querySelector(".kicker");
      if (kicker) tl.from(kicker, { opacity: 0, duration: 0.4, ease: "power1.out" }, t + 0.05);"""

    return f"""<!doctype html>
<!-- {roteiro['slug']} | template misterio-45 {'+ layouts v2' if usar_layouts else '(v1 congelado)'} | {len(cenas)} cenas | gerado por scripts/gerar-episodio.py -->
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>{roteiro.get('titulo_pagina', roteiro['slug'])}</title>
<style>
{css_total}</style>
</head>
<body>
<div id="stage" data-composition-id="{comp}" data-start="0" data-width="1080" data-height="1920" data-fps="30">
  <div class="bg"></div>
  <div class="vignette"></div>
  <div class="frame"></div>
  <div class="mark">{marca}</div>
  <div class="dossier">{dossie}</div>

{corpo}

  <div class="foot">{rodape}</div>
  <div id="fade"></div>

  <!-- Áudio: voz.wav e drone.wav ({dur:g} s) nesta pasta. Não remova os ids. -->
  <audio id="voz" data-start="0" data-duration="{dur:g}" data-track-index="0" data-volume="{vol_voz}" src="voz.wav"></audio>
  <audio id="drone" data-start="0" data-duration="{dur:g}" data-track-index="2" data-volume="{vol_drone}" src="drone.wav"></audio>

  <script src="gsap.min.js"></script>
{bloco_layouts}  <script>
    const DUR = {dur:g};
    const tl = gsap.timeline({{ paused: true }});
    tl.to({{}}, {{ duration: DUR }}, 0);
    tl.fromTo(".bg", {{ scale: 1.06 }}, {{ scale: {zoom:.2f}, duration: DUR, ease: "none" }}, 0);

    const scenes = [
{linhas_entrada}
    ];

    scenes.forEach(([id, t]) => {{
      const root = document.getElementById(id);
      const start = parseFloat(root.dataset.start || "0");
      const dur = parseFloat(root.dataset.duration || String(DUR));
      tl.set(root, {{ autoAlpha: 0 }}, 0);
      tl.set(root, {{ autoAlpha: 1 }}, start);
      tl.set(root, {{ autoAlpha: 0 }}, start + dur);
{animacao}
    }});

    tl.to("#fade", {{ opacity: 1, duration: 0.7, ease: "power1.in" }}, {dur - 0.7:.2f});
    window.__timelines = window.__timelines || {{}};
    window.__timelines.{comp} = tl;

    // QA: congelar um frame via ?t=12.5 (não afeta o render)
    const seek = new URLSearchParams(location.search).get("t");
    if (seek !== null) {{
      const t = Math.max(0, Math.min(DUR, parseFloat(seek) || 0));
      tl.time(t, false);
      document.querySelectorAll(".clip").forEach((el) => {{
        const start = parseFloat(el.dataset.start || "0");
        const dur = parseFloat(el.dataset.duration || "0");
        el.style.visibility = (t >= start && t < start + dur) ? "visible" : "hidden";
      }});
    }}
  </script>
</div>
</body>
</html>
"""


def narracao(roteiro: dict) -> str:
    falas = [(c.get("fala") or "").strip() for c in roteiro["cenas"]]
    if not all(falas):
        faltando = [c["id"] for c, f in zip(roteiro["cenas"], falas) if not f]
        raise SystemExit(f"cenas sem fala: {', '.join(faltando)}")
    return "\n\n".join(falas) + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Gera o index.html a partir de roteiro.json")
    ap.add_argument("episodio", help="diretorio do episodio")
    ap.add_argument("--roteiro", default="roteiro.json")
    ap.add_argument("--tempos", default="tempos_cenas.json")
    ap.add_argument("--saida", default="index.html")
    ap.add_argument("--narracao", action="store_true",
                    help="tambem (re)escreve narracao.txt a partir das falas")
    ap.add_argument("--check", action="store_true",
                    help="so valida e mede o tempo; nao escreve nada")
    args = ap.parse_args(argv)

    ep = Path(args.episodio)
    roteiro = carregar(ep / args.roteiro)
    tempos, reais = carregar_tempos(ep / args.tempos, roteiro["cenas"], roteiro["duracao"])
    avisos = validar(roteiro, tempos)

    print(f"{roteiro['slug']}: {len(roteiro['cenas'])} cenas | "
          f"{'tempos reais' if reais else 'TEMPOS PROVISORIOS'}")
    print("| # | inicio | duracao | fonte | linhas |")
    print("|---:|---:|---:|---:|---:|")
    for i, (c, t) in enumerate(zip(roteiro["cenas"], tempos)):
        px = c.get("fonte_px") or estimar_fonte(c["titulo"], c.get("letter_spacing", -2))
        linhas = len(c["titulo"]) + len(c.get("pequeno") or [])
        print(f"| {i + 1} | {t['start']:.2f} | {t['duration']:.2f} | {px} | {linhas} |")

    usados = [c.get("tipo") for c in roteiro["cenas"] if c.get("tipo")]
    if usados:
        print(f"  layouts: {len(usados)} de {len(roteiro['cenas'])} cenas "
              f"({', '.join(sorted(set(usados)))})")

    for a in avisos:
        print(f"  aviso: {a}")
    if not reais:
        print("  aviso: sem tempos_cenas.json — rode a voz e remapear.py antes do render")

    if args.check:
        print("\n--check: nada foi escrito")
        return 0

    if reais:
        (ep / args.saida).write_text(html(roteiro, tempos), encoding="utf-8")
        print(f"\n{args.saida}: escrito")
    else:
        print("\nnada escrito: o index.html precisa dos tempos reais")

    if args.narracao:
        (ep / "narracao.txt").write_text(narracao(roteiro), encoding="utf-8")
        print("narracao.txt: escrito")

    print("proximo: .\\scripts\\medir-texto.ps1 " + str(ep))
    return 0


if __name__ == "__main__":
    sys.exit(main())

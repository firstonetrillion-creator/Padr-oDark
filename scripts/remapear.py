#!/usr/bin/env python3
"""Remapeia as cenas de um episodio a partir da transcricao real da voz.

Problema que resolve: o `transcricao.json` do faster-whisper agrupa frases por
VAD (5 blocos para 12 cenas), entao `segments` nao serve. As palavras servem.

E o texto da tela nao e igual ao texto que o ASR ouve: a narracao escreve os
numeros de um jeito ("18h20", "10 galoes", "30 metros") e o ASR devolve outro
("18 e 20", "dez galoes", "50 metros" — erra mesmo). Comparar token a token
quebra. Solucao: normalizar todo numero para "#" e alinhar as **sequencias
inteiras** com difflib. O alinhamento global e mais robusto que casar frase por
frase, porque aproveita o contexto do video todo.

Saida (por padrao `<episodio>/tempos_cenas.json`):

    [{"cena": 1, "inicio": 0.0, "start": 0.0, "duration": 3.95}, ...]

`start`/`duration` ja seguem o contrato de `docs/ARQUITETURA.md` §3:
    start    = inicio da fala - 0,05
    duration = inicio da proxima - start - 0,05
e a ultima cena fecha na duracao do video.

Uso:
    .venv\\Scripts\\python.exe scripts\\remapear.py episodios\\005-voo-19
    .venv\\Scripts\\python.exe scripts\\remapear.py episodios\\005-voo-19 --duracao 45 --aplicar
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path

FOLGA = 0.05  # respiro entre cenas (contrato §3)


def tokens(texto: str) -> list[str]:
    """Minusculo, sem pontuacao, numero vira '#'. '18h20' -> '18','20'."""
    t = texto.lower()
    t = re.sub(r"(?<=\d)h(?=\d)", " ", t)          # 18h20 -> 18 20
    t = re.sub(r"[^0-9a-zà-ÿ#]+", " ", t)
    saida = []
    for tok in t.split():
        saida.append("#" if tok.isdigit() else tok)
    return saida


def alinhar(roteiro: list[str], asr: list[str]) -> dict[int, int]:
    """Mapa indice_no_roteiro -> indice_no_asr, so para tokens iguais."""
    sm = SequenceMatcher(None, roteiro, asr, autojunk=False)
    mapa: dict[int, int] = {}
    for bloco in sm.get_matching_blocks():
        for k in range(bloco.size):
            mapa[bloco.a + k] = bloco.b + k
    return mapa


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Remapeia cenas pela transcricao real")
    ap.add_argument("episodio", help="diretorio do episodio")
    ap.add_argument("--narracao", default="narracao.txt")
    ap.add_argument("--transcricao", default="transcricao.json")
    ap.add_argument("--saida", default="tempos_cenas.json")
    ap.add_argument("--duracao", type=float, default=45.0)
    ap.add_argument("--aplicar", action="store_true",
                    help="grava data-start/data-duration no index.html")
    args = ap.parse_args(argv)

    ep = Path(args.episodio)
    falas = [p.strip() for p in
             (ep / args.narracao).read_text(encoding="utf-8").split("\n\n") if p.strip()]
    dados = json.loads((ep / args.transcricao).read_text(encoding="utf-8"))

    palavras: list[dict] = []
    for seg in dados.get("segments", []):
        palavras.extend(seg.get("words") or [])
    if not palavras:
        raise SystemExit("transcricao sem words[]: rode transcribe.py de novo")

    asr = [tokens(w.get("word", "")) for w in palavras]
    asr_flat = [t for grupo in asr for t in grupo]
    # indice de cada token achatado -> palavra de origem
    dono: list[int] = [i for i, grupo in enumerate(asr) for _ in grupo]

    roteiro: list[str] = []
    inicio_frase: list[int] = []
    for fala in falas:
        inicio_frase.append(len(roteiro))
        roteiro.extend(tokens(fala))

    mapa = alinhar(roteiro, asr_flat)
    cobertos = len(mapa)
    if cobertos < 0.6 * len(roteiro):
        raise SystemExit(
            f"alinhamento fraco: {cobertos}/{len(roteiro)} tokens casados "
            f"({cobertos / len(roteiro):.0%}) — conferir a narracao")

    # inicio de cada cena = primeiro token alinhado a partir da fronteira
    inicios: list[float] = []
    for idx in inicio_frase:
        achou = None
        for k in range(idx, len(roteiro)):
            if k in mapa:
                achou = k
                break
        if achou is None:
            raise SystemExit(f"nao alinhei a cena que comeca no token {idx}")
        inicios.append(round(float(palavras[dono[mapa[achou]]]["start"]), 3))

    if inicios[0] > 1.0:
        raise SystemExit(f"primeira cena comeca em {inicios[0]} s: a voz tem "
                         f"silencio no inicio e a cena 1 fica muda")
    inicios[0] = 0.0

    cenas = []
    for i, ini in enumerate(inicios):
        start = round(ini - FOLGA, 3) if i else 0.0
        start = max(0.0, start)
        fim = inicios[i + 1] if i + 1 < len(inicios) else args.duracao
        dur = round(fim - start - FOLGA, 3)
        cenas.append({"cena": i + 1, "inicio": ini, "start": start,
                      "duration": dur, "fim": round(start + dur, 3)})

    (ep / args.saida).write_text(json.dumps(cenas, ensure_ascii=False, indent=2),
                                 encoding="utf-8")

    print(f"{ep.name}: {len(cenas)} cenas | alinhamento {cobertos}/{len(roteiro)} "
          f"({cobertos / len(roteiro):.0%})")
    print("| # | início | duração | texto |")
    print("|---:|---:|---:|---|")
    for c, fala in zip(cenas, falas):
        marca = " ⚠" if c["duration"] > 6.0 else ""
        print(f"| {c['cena']} | {c['start']:.2f} | {c['duration']:.2f}{marca} "
              f"| {fala[:58]} |")
    print(f"\nfim da ultima cena: {cenas[-1]['fim']:.2f} s de {args.duracao:g}")

    if args.aplicar:
        html = (ep / "index.html").read_text(encoding="utf-8")
        trocas = 0
        for c in cenas:
            padrao = re.compile(
                r'(data-start=")[\d.]+(")(\s+data-duration=")[\d.]+(")([^>]*?'
                r'data-cena="' + str(c["cena"]) + r'")')
            novo, n = padrao.subn(
                lambda m: f'{m.group(1)}{c["start"]:.3f}{m.group(2)}{m.group(3)}'
                          f'{c["duration"]:.3f}{m.group(4)}{m.group(5)}', html)
            if n:
                html, trocas = novo, trocas + n
        if trocas == len(cenas):
            (ep / "index.html").write_text(html, encoding="utf-8")
            print(f"index.html: {trocas} cenas atualizadas")
        else:
            print(f"index.html: {trocas}/{len(cenas)} cenas casaram — "
                  f"aplicar a mao (precisa de data-cena=\"N\" em cada section)")

    return 0


if __name__ == "__main__":
    sys.exit(main())

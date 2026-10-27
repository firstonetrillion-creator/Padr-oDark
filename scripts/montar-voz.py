#!/usr/bin/env python
"""Monta a voz de um episodio cena por cena e escreve os tempos exatos.

Problema que resolve: o fluxo de um take unico depende de ASR para descobrir
onde cada cena comeca (`transcricao.json` -> `remapear.py`). Quando o Piper
sai com prosodia incomum, o faster-whisper erra palavras ("cortam um degrau"
virou "Cota o mundo legal" no 006) e o alinhamento derrapa mais de um segundo
numa cena so. O texto aparece fora de sincronia e nao ha como saber olhando a
tabela.

Aqui cada paragrafo de `narracao_tts.txt` e sintetizado separado e concatenado
com um silencio calculado. O tempo deixa de ser estimado: e a soma dos blocos.

Trade-off: a prosodia e por cena (cada bloco comeca do zero). Para frases
curtas de 2-5 s isso e o mesmo que um respiro entre cartoes; para paragrafos
longos e continuacao de raciocinio, prefira o take unico + `remapear.py`.

Saida:

    voz_raw.wav         com `--inicio` de respiro na frente
    tempos_cenas.json   contrato de docs/ARQUITETURA.md §3:
                          start    = fala - 0,05 (a cena ja esta no ar)
                          duration = proxima fala - start - 0,05
                        primeira cena em 0, ultima fechando a duracao

Uso:

    .venv\\Scripts\\python.exe scripts\\montar-voz.py episodios\\006-passo-dyatlov
    .venv\\Scripts\\python.exe scripts\\montar-voz.py episodios\\006-passo-dyatlov --length-scale 1.06
    .venv\\Scripts\\python.exe scripts\\montar-voz.py laboratorio\\001-60s-fawcett --duracao 60 --fim 1.5
"""

from __future__ import annotations

import argparse
import json
import wave
from array import array
from pathlib import Path

from piper import PiperVoice, SynthesisConfig

DEFAULT_DATA_DIR = Path(r"C:\Users\valentim\Tools\piper-data\espeak-ng-data")
DEFAULT_MODEL = r"models\vozes\pt_BR-faber-medium.onnx"


def cortar_silencio(pcm: array, limiar: int = 220) -> array:
    """Remove silencio nas pontas: o respiro entre cenas e decidido aqui."""
    ini, fim = 0, len(pcm)
    while ini < fim and abs(pcm[ini]) < limiar:
        ini += 1
    while fim > ini and abs(pcm[fim - 1]) < limiar:
        fim -= 1
    return pcm[ini:fim]


def silencio(segundos: float, taxa: int) -> array:
    return array("h", bytes(2 * max(0, int(segundos * taxa))))


def main() -> None:
    ap = argparse.ArgumentParser(description="Voz cena por cena + tempos exatos")
    ap.add_argument("episodio", help="diretorio do episodio")
    ap.add_argument("--texto", default="narracao_tts.txt")
    ap.add_argument("--saida", default="voz_raw.wav")
    ap.add_argument("--tempos", default="tempos_cenas.json")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--duracao", type=float, default=45.0)
    ap.add_argument("--inicio", type=float, default=0.6, help="respiro antes da primeira fala")
    ap.add_argument("--fim", type=float, default=0.9, help="silencio depois da ultima fala")
    ap.add_argument("--length-scale", type=float, default=1.0)
    ap.add_argument("--noise-scale", type=float, default=0.667)
    ap.add_argument("--noise-w", type=float, default=0.80)
    ap.add_argument("--pesos", default="",
                    help="silencio relativo de cada fronteira, separado por virgula "
                         "(1,0 = media; >1 = respiro maior)")
    args = ap.parse_args()

    ep = Path(args.episodio)
    texto_path = ep / args.texto
    paragrafos = [p.strip() for p in texto_path.read_text(encoding="utf-8").split("\n\n") if p.strip()]
    if not paragrafos:
        raise SystemExit(f"sem texto em {texto_path}")

    rot = ep / "roteiro.json"
    if rot.exists():
        cenas = json.loads(rot.read_text(encoding="utf-8"))["cenas"]
        if len(cenas) != len(paragrafos):
            raise SystemExit(
                f"{len(paragrafos)} paragrafos para {len(cenas)} cenas — "
                f"ajuste {args.texto} ou o roteiro.json")

    pesos = [1.0] * len(paragrafos)
    if args.pesos:
        pesos = [float(p) for p in args.pesos.split(",")]
        if len(pesos) != len(paragrafos):
            raise SystemExit(f"--pesos: {len(pesos)} valores para {len(paragrafos)} cenas")

    voice = PiperVoice.load(args.model, espeak_data_dir=str(DEFAULT_DATA_DIR))
    taxa = voice.config.sample_rate
    cfg = SynthesisConfig(
        length_scale=args.length_scale,
        noise_scale=args.noise_scale,
        noise_w_scale=args.noise_w,
        volume=1.0,
    )

    blocos: list[array] = []
    print(f"{ep.name}: {len(paragrafos)} cenas")
    for i, texto in enumerate(paragrafos, 1):
        pcm = array("h")
        for chunk in voice.synthesize(texto, syn_config=cfg):
            pcm.frombytes(chunk.audio_int16_bytes)
        pcm = cortar_silencio(pcm)
        blocos.append(pcm)
        print(f"  {i:02d}: {len(pcm) / taxa:6.3f} s  {len(texto.split()):3d} pal.  {texto[:52]}")

    fala = sum(len(b) for b in blocos) / taxa
    disponivel = args.duracao - args.inicio - args.fim
    if fala > disponivel:
        alvo = args.length_scale * disponivel / fala
        raise SystemExit(
            f"fala {fala:.2f} s nao cabe em {disponivel:.2f} s "
            f"(duracao {args.duracao:g} - inicio {args.inicio:g} - fim {args.fim:g}); "
            f"use --length-scale {alvo:.2f}")

    # o silencio que sobra e dividido entre as fronteiras, proporcional aos pesos
    sobra = disponivel - fala
    unidade = sobra / sum(pesos)
    silencios = [p * unidade for p in pesos]

    saida = array("h")
    saida.extend(silencio(args.inicio, taxa))
    cursor = args.inicio
    falas = []
    for bloco, sil in zip(blocos, silencios):
        falas.append(cursor)
        saida.extend(bloco)
        cursor += len(bloco) / taxa
        saida.extend(silencio(sil, taxa))
        cursor += sil
    saida.extend(silencio(args.fim, taxa))

    with wave.open(str(ep / args.saida), "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(taxa)
        wav.writeframes(saida.tobytes())

    # contrato §3: a cena entra 0,05 s antes da fala e sai 0,05 s antes da proxima
    tempos = []
    for i, ini in enumerate(falas):
        start = 0.0 if i == 0 else round(ini - 0.05, 3)
        if i + 1 < len(falas):
            dur = round(falas[i + 1] - 0.05 - start, 3)
        else:
            dur = round(args.duracao - start, 3)
        tempos.append({"cena": i + 1, "inicio": round(ini, 3), "start": start, "duration": dur})
    (ep / args.tempos).write_text(json.dumps(tempos, ensure_ascii=False, indent=2), encoding="utf-8")

    total = len(saida) / taxa
    print(f"\nfala: {fala:.3f} s | silencio: {sobra + args.inicio + args.fim:.3f} s "
          f"({(sobra + args.inicio + args.fim) / total * 100:.1f}% do video)")
    print(f"total: {total:.3f} s de {args.duracao:g} | {taxa} Hz mono -> {ep / args.saida}")
    print(f"tempos: {ep / args.tempos}")
    if abs(total - args.duracao) > 0.01:
        print(f"  atencao: total {total:.3f} s != {args.duracao:g} s "
              f"(o arredondamento de 16 bits deixa menos de 1 ms por bloco)")


if __name__ == "__main__":
    main()

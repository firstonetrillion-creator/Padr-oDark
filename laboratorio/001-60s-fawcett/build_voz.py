#!/usr/bin/env python
"""Monta a voz do laboratorio 001 (60 s) cena por cena.

Diferente do fluxo dos episodios (um take continuo esticado para 45 s), aqui a
voz e sintetizada **por cena** e o silencio entre as cenas e distribuido para
fechar 60,000 s. Motivo: o estilo "Trilho" usa o silencio como pontuacao, e um
take unico com 8 s de sobra no fim nao da respiro no meio.

Saida:
  voz_raw.wav          60,000 s, 16-bit mono na taxa do modelo
  tempos_cenas.json    inicio/fim de cada uma das 16 cenas

Uso:
  .venv\\Scripts\\python.exe laboratorio\\001-60s-fawcett\\build_voz.py
"""

from __future__ import annotations

import argparse
import json
import wave
from array import array
from pathlib import Path

from piper import PiperVoice, SynthesisConfig

DEFAULT_DATA_DIR = Path(r"C:\Users\valentim\Tools\piper-data\espeak-ng-data")

# Peso do silencio em cada fronteira. 1.0 = media. >1 = respiro maior.
# A ultima posicao e o respiro final, antes do fade.
PESOS = [1.2, 0.8, 0.9, 1.1, 0.9, 1.0, 1.4, 0.8, 1.1, 0.8, 1.3, 0.8, 0.9, 0.9, 1.2, 1.6]


def cortar_silencio(pcm: array, limiar: int = 220) -> array:
    """Remove silencio nas pontas para o respiro ser controlado por nos."""
    ini, fim = 0, len(pcm)
    while ini < fim and abs(pcm[ini]) < limiar:
        ini += 1
    while fim > ini and abs(pcm[fim - 1]) < limiar:
        fim -= 1
    return pcm[ini:fim]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--texto", default=str(Path(__file__).with_name("narracao_tts.txt")))
    ap.add_argument("--model", default=r"models\vozes\pt_BR-faber-medium.onnx")
    ap.add_argument("--saida", default=str(Path(__file__).with_name("voz_raw.wav")))
    ap.add_argument("--tempos", default=str(Path(__file__).with_name("tempos_cenas.json")))
    ap.add_argument("--duracao", type=float, default=60.0)
    ap.add_argument("--length-scale", type=float, default=1.0)
    ap.add_argument("--noise-scale", type=float, default=0.65)
    ap.add_argument("--noise-w", type=float, default=0.80)
    args = ap.parse_args()

    paragrafos = [p.strip() for p in Path(args.texto).read_text(encoding="utf-8").split("\n\n") if p.strip()]
    if len(paragrafos) != len(PESOS):
        raise SystemExit(f"esperava {len(PESOS)} cenas no texto, achei {len(paragrafos)}")

    voice = PiperVoice.load(args.model, espeak_data_dir=str(DEFAULT_DATA_DIR))
    taxa = voice.config.sample_rate
    cfg = SynthesisConfig(
        length_scale=args.length_scale,
        noise_scale=args.noise_scale,
        noise_w_scale=args.noise_w,
        volume=1.0,
    )

    blocos: list[array] = []
    for i, texto in enumerate(paragrafos, 1):
        pcm = array("h")
        for chunk in voice.synthesize(texto, syn_config=cfg):
            pcm.frombytes(chunk.audio_int16_bytes)
        pcm = cortar_silencio(pcm)
        blocos.append(pcm)
        print(f"  cena {i:02d}: {len(pcm) / taxa:6.3f} s  {len(texto.split())} pal.")

    # sobra de tempo dividida entre as fronteiras, proporcional aos pesos
    fala = sum(len(b) for b in blocos) / taxa
    sobra = args.duracao - fala
    if sobra <= 0:
        raise SystemExit(f"fala ({fala:.2f} s) ja passa de {args.duracao} s: reduza --length-scale")
    unidade = sobra / sum(PESOS)
    silencios = [p * unidade for p in PESOS]

    saida = array("h")
    tempos = []
    cursor = 0.0
    for i, bloco in enumerate(blocos):
        ini = cursor
        saida.extend(bloco)
        cursor += len(bloco) / taxa
        tempos.append({"cena": i + 1, "inicio": round(ini, 3), "fim": round(cursor, 3), "silencio_depois": round(silencios[i], 3)})
        silencio = array("h", bytes(2 * int(silencios[i] * taxa)))
        saida.extend(silencio)
        cursor += silencios[i]

    with wave.open(args.saida, "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(taxa)
        wav.writeframes(saida.tobytes())

    Path(args.tempos).write_text(json.dumps(tempos, ensure_ascii=False, indent=2), encoding="utf-8")
    dur = len(saida) / taxa
    print(f"\nfala: {fala:.3f} s | silencio: {sobra:.3f} s ({sobra / dur * 100:.1f}% do video)")
    print(f"total: {dur:.3f} s | {taxa} Hz mono -> {args.saida}")


if __name__ == "__main__":
    main()

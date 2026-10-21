#!/usr/bin/env python
"""Wrapper do Piper TTS para caminhos com acento no Windows.

O espeak-ng abre os arquivos de dados com fopen ANSI e falha quando o caminho
contem caracteres nao-ASCII (ex.: "Padrao" com til). Por isso os dados sao
copiados para C:\\Users\\valentim\\Tools\\piper-data e passados explicitamente.

Uso:
  .venv\\Scripts\\python.exe scripts\\tts.py ^
    --model models\\vozes\\pt_BR-faber-medium.onnx ^
    --input episodios\\001-faroleiros\\narracao.txt ^
    --output episodios\\001-faroleiros\\voz_raw.wav ^
    --length-scale 1.06
"""

from __future__ import annotations

import argparse
import wave
from pathlib import Path

from piper import PiperVoice, SynthesisConfig

DEFAULT_DATA_DIR = Path(r"C:\Users\valentim\Tools\piper-data\espeak-ng-data")


def main() -> None:
    parser = argparse.ArgumentParser(description="Piper TTS (wrapper ASCII)")
    parser.add_argument("--model", required=True, help="caminho do .onnx")
    parser.add_argument("--input", required=True, help="arquivo de texto UTF-8")
    parser.add_argument("--output", required=True, help="arquivo .wav de saida")
    parser.add_argument("--data-dir", default=str(DEFAULT_DATA_DIR))
    parser.add_argument("--length-scale", type=float, default=1.0)
    parser.add_argument("--noise-scale", type=float, default=0.667)
    parser.add_argument("--noise-w", type=float, default=0.8)
    parser.add_argument("--volume", type=float, default=1.0)
    args = parser.parse_args()

    text = Path(args.input).read_text(encoding="utf-8").strip()
    if not text:
        raise SystemExit("texto vazio")

    data_dir = Path(args.data_dir)
    if not data_dir.is_dir():
        raise SystemExit(f"espeak-ng-data nao encontrado em {data_dir}")

    voice = PiperVoice.load(args.model, espeak_data_dir=data_dir)
    config = SynthesisConfig(
        length_scale=args.length_scale,
        noise_scale=args.noise_scale,
        noise_w_scale=args.noise_w,
        volume=args.volume,
    )

    with wave.open(args.output, "wb") as wav_file:
        voice.synthesize_wav(text, wav_file, syn_config=config)

    print(f"ok: {args.output}")


if __name__ == "__main__":
    main()

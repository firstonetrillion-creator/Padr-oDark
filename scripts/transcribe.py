#!/usr/bin/env python
"""Transcreve um WAV com faster-whisper e imprime JSON com tempos por palavra.

Uso:
  .venv\\Scripts\\python.exe scripts\\transcribe.py episodios\\001-faroleiros\\voz.wav --model small
"""

from __future__ import annotations

import argparse
import json
import sys

from faster_whisper import WhisperModel


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("audio")
    parser.add_argument("--model", default="small")
    parser.add_argument("--language", default="pt")
    parser.add_argument("--output", default="")
    args = parser.parse_args()

    model = WhisperModel(args.model, device="cpu", compute_type="int8")
    segments, info = model.transcribe(
        args.audio,
        language=args.language,
        word_timestamps=True,
        vad_filter=True,
        beam_size=5,
    )

    data = {
        "language": info.language,
        "duration": info.duration,
        "segments": [],
    }
    for seg in segments:
        data["segments"].append(
            {
                "start": round(seg.start, 3),
                "end": round(seg.end, 3),
                "text": seg.text.strip(),
                "words": [
                    {
                        "start": round(w.start, 3),
                        "end": round(w.end, 3),
                        "word": w.word.strip(),
                    }
                    for w in (seg.words or [])
                ],
            }
        )

    text = json.dumps(data, ensure_ascii=False, indent=2)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as fh:
            fh.write(text)
        print(f"ok: {args.output}", file=sys.stderr)
    else:
        print(text)


if __name__ == "__main__":
    main()

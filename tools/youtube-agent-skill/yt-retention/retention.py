#!/usr/bin/env python3
"""retention.py - leitura de retenção do YouTube Studio para Shorts de 45 s.

Adaptado de Jakeschincariol/youtube-agent-skill (MIT), commit a2feb21.
Mudanças em relação ao original:
  - janela de gancho padrão 3 s e 10 s (Shorts); 30 s fica como legado;
  - detecção de eixo segundos/percentual robusta para vídeos com menos de 100 s;
  - interpolação do valor retido no instante exato;
  - leitura de transcrição SRT/VTT/JSON sem depender de yt-edit;
  - relatório em PT-BR.

Uso:
    python retention.py retencao.csv --duration 45
    python retention.py retencao.csv --duration 45 --transcript transcricao.json
    python retention.py retencao.csv --duration 45 --json

O CSV é o export do Studio:
    Analytics -> Engajamento -> gráfico de retenção -> baixar -> "Retenção da audiência"

O arquivo tem duas colunas: posição (segundos ou percentual) e porcentagem
ainda assistindo. A posição pode vir como número, "0:03" ou "3,5".

Leitura correta:
  - 3 s é a janela em que o Short decide se continua ou é ignorado;
  - 10 s mostra se o contexto segurou depois do gancho;
  - 30 s só interessa em long-form. Não usar como gate de Short.
"""

from __future__ import annotations

import argparse
import bisect
import csv
import json
import os
import re
import sys
from itertools import chain
from typing import Iterable, Optional


DEFAULT_MIN_3S = 70.0
DEFAULT_MIN_10S = 45.0
DEFAULT_MIN_CLIFF_DROP = 1.0
DEFAULT_MIN_CLIFF_RATE = 1.5


def _parse_number(cell: str) -> Optional[float]:
    """Converte '99,5%', '1.234,5' ou '99.5' em float."""
    c = cell.strip().replace("\u00a0", " ").replace(" ", "").replace("%", "")
    if not c:
        return None
    if "," in c and "." in c:
        if c.rfind(",") > c.rfind("."):
            c = c.replace(".", "").replace(",", ".")
        else:
            c = c.replace(",", "")
    elif "," in c:
        c = c.replace(",", ".")
    try:
        return float(c)
    except ValueError:
        return None


def _parse_clock(cell: str) -> Optional[float]:
    """Converte '0:03', '1:02:03' ou '03,5' em segundos."""
    c = cell.strip().replace(",", ".")
    if ":" not in c:
        return None
    parts = c.split(":")
    if len(parts) not in (2, 3):
        return None
    try:
        nums = [float(p) for p in parts]
    except ValueError:
        return None
    if len(nums) == 2:
        return nums[0] * 60 + nums[1]
    return nums[0] * 3600 + nums[1] * 60 + nums[2]


def _parse_cell(cell: str) -> Optional[tuple[float, str]]:
    """Retorna (valor, 'clock'|'number') ou None."""
    clock = _parse_clock(cell)
    if clock is not None:
        return clock, "clock"
    number = _parse_number(cell)
    if number is not None:
        return number, "number"
    return None


def _header_hint(header: str) -> Optional[str]:
    h = header.casefold()
    if "second" in h or "segundo" in h or "segundos" in h:
        return "seconds"
    if "%" in h or "percent" in h or "porcent" in h:
        return "percent"
    return None


def load_csv(path: str) -> tuple[list[tuple[float, float]], Optional[str]]:
    """Lê o CSV e devolve [(posição, retenção)] + dica de eixo."""
    with open(path, newline="", encoding="utf-8-sig", errors="replace") as fh:
        sample = fh.read(8192)
        fh.seek(0)
        try:
            dialect = csv.Sniffer().sniff(sample, delimiters=",;\t")
        except csv.Error:
            dialect = csv.excel

        reader = csv.reader(fh, dialect)
        first = next(reader, None)
        if first is None:
            return [], None

        hint = None
        first_parsed = [_parse_cell(c) for c in first]
        parsed_count = sum(p is not None for p in first_parsed)
        rows: list[tuple[float, float]] = []

        if parsed_count >= 2:
            # O arquivo não tem cabeçalho; a primeira linha já é dado.
            source: Iterable[list[str]] = chain([first], reader)
        else:
            hint = _header_hint(" ".join(first))
            source = reader

        for row in source:
            values = [_parse_cell(c) for c in row]
            values = [v for v in values if v is not None]
            if len(values) < 2:
                continue
            x, x_kind = values[0]
            y, _ = values[1]
            if x_kind == "clock":
                hint = "seconds"
            if x < 0 or not (0.0 <= y <= 100.5):
                continue
            rows.append((x, y))

    # Deduplica posições e ordena. Em empate, fica o último valor lido.
    by_x: dict[float, float] = {}
    for x, y in rows:
        by_x[round(float(x), 6)] = float(y)
    return sorted(by_x.items()), hint


def detect_axis(
    rows: list[tuple[float, float]], hint: Optional[str], duration: Optional[float]
) -> str:
    if hint in ("seconds", "percent"):
        return hint
    if not rows:
        return "percent"
    max_x = max(x for x, _ in rows)
    if max_x > 100.5:
        return "seconds"
    # Um vídeo de 45 s com eixo em segundos termina em ~45, não em 100.
    # O original tratava max <= 100.5 como percentual e quebrava justamente
    # no formato Shorts. Aqui a duração desempata.
    if duration and duration > 0 and max_x <= duration * 1.05 and max_x < 99.5:
        return "seconds"
    return "percent"


def to_seconds(
    rows: list[tuple[float, float]], axis: str, duration: Optional[float]
) -> list[tuple[float, float]]:
    if axis == "percent":
        if not duration or duration <= 0:
            raise ValueError(
                "eixo percentual exige --duration (ex.: --duration 45); "
                "sem isso não dá para converter 3 s e 10 s."
            )
        return [(x / 100.0 * duration, y) for x, y in rows]
    return rows


def interp_at(rows: list[tuple[float, float]], t: float) -> float:
    """Valor retido em t, interpolando entre amostras."""
    if not rows:
        return 0.0
    xs = [x for x, _ in rows]
    if t <= xs[0]:
        return rows[0][1]
    if t >= xs[-1]:
        return rows[-1][1]
    i = bisect.bisect_left(xs, t)
    if i == 0:
        return rows[0][1]
    x0, y0 = rows[i - 1]
    x1, y1 = rows[i]
    if x1 == x0:
        return y1
    return y0 + (y1 - y0) * ((t - x0) / (x1 - x0))


def _status(value: float, threshold: float) -> str:
    return "OK" if value >= threshold else "ABAIXO"


def build_hooks(
    rows: list[tuple[float, float]],
    duration: Optional[float],
    min_3s: float,
    min_10s: float,
) -> list[dict]:
    start = rows[0][1]
    windows = [(3.0, "3 s", min_3s), (10.0, "10 s", min_10s)]
    # 30 s é útil para long-form; em Shorts é só referência histórica.
    if duration is None or duration >= 30.0:
        windows.append((30.0, "30 s", None))

    hooks = []
    for seconds, label, threshold in windows:
        if duration is not None and seconds > duration + 0.5:
            continue
        retained = interp_at(rows, seconds)
        hooks.append(
            {
                "seconds": seconds,
                "label": label,
                "retained": round(retained, 2),
                "leak": round(start - retained, 2),
                "status": _status(retained, threshold) if threshold else "legado",
                "threshold": threshold,
            }
        )
    return hooks


def build_cliffs(
    rows: list[tuple[float, float]],
    min_drop: float,
    min_rate: float,
    top: int,
) -> list[dict]:
    cliffs = []
    for i in range(1, len(rows)):
        x0, y0 = rows[i - 1]
        x1, y1 = rows[i]
        dt = x1 - x0
        if dt <= 0:
            continue
        drop = y0 - y1
        if drop <= 0:
            continue
        rate = drop / dt
        if drop >= min_drop and rate >= min_rate:
            cliffs.append(
                {
                    "from_seconds": round(x0, 2),
                    "to_seconds": round(x1, 2),
                    "lost": round(drop, 2),
                    "per_second": round(rate, 2),
                }
            )
    cliffs.sort(key=lambda c: (-c["per_second"], -c["lost"]))
    return cliffs[:top]


def build_slide(rows: list[tuple[float, float]]) -> dict:
    end_t = rows[-1][0]
    start_t = min(10.0, end_t)
    y0 = interp_at(rows, start_t)
    y1 = interp_at(rows, end_t)
    span = end_t - start_t
    loss = y0 - y1
    return {
        "from_seconds": round(start_t, 2),
        "to_seconds": round(end_t, 2),
        "loss": round(loss, 2),
        "per_second": round(loss / span, 3) if span > 0 else 0.0,
    }


def _parse_timestamp(value: str) -> Optional[float]:
    value = value.strip().replace(",", ".")
    parts = value.split(":")
    if len(parts) not in (2, 3):
        return None
    try:
        nums = [float(p) for p in parts]
    except ValueError:
        return None
    if len(nums) == 2:
        return nums[0] * 60 + nums[1]
    return nums[0] * 3600 + nums[1] * 60 + nums[2]


def load_transcript(path: str) -> list[tuple[float, float, str]]:
    """Lê SRT, VTT ou JSON do faster-whisper e devolve (início, fim, texto)."""
    if not os.path.exists(path):
        return []
    if path.lower().endswith(".json"):
        with open(path, encoding="utf-8-sig", errors="replace") as fh:
            data = json.load(fh)
        segments = data.get("segments", []) if isinstance(data, dict) else data
        cues = []
        for seg in segments:
            try:
                start = float(seg["start"])
                end = float(seg["end"])
            except (KeyError, TypeError, ValueError):
                continue
            text = str(seg.get("text", "")).strip()
            if text:
                cues.append((start, end, text))
        return cues

    raw = open(path, encoding="utf-8-sig", errors="replace").read()
    raw = raw.replace("\r\n", "\n").replace("\r", "\n")
    cues = []
    for block in re.split(r"\n\s*\n", raw):
        lines = [line for line in block.split("\n") if line.strip()]
        if not lines:
            continue
        if lines[0].strip().upper().startswith("WEBVTT"):
            lines = lines[1:]
        timing_index = next((i for i, line in enumerate(lines) if "-->" in line), None)
        if timing_index is None:
            continue
        left, right = lines[timing_index].split("-->", 1)
        start = _parse_timestamp(left)
        end = _parse_timestamp(right.split()[0] if right.split() else "")
        if start is None or end is None:
            continue
        text = re.sub(r"<[^>]+>", "", " ".join(lines[timing_index + 1 :])).strip()
        if text:
            cues.append((start, end, text))
    return cues


def said_at(
    cues: list[tuple[float, float, str]], t: float, window: float = 2.0
) -> str:
    near = [text for start, end, text in cues if start <= t + window and end >= t - window]
    return " ".join(near)[:180]


def _fmt_pct(value: float) -> str:
    return f"{value:.1f}%"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Lê o CSV de retenção do YouTube Studio e reporta 3 s, 10 s, quedas e slide.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("csv", help="export de retenção do YouTube Studio")
    parser.add_argument("--duration", type=float, help="duração do vídeo em segundos")
    parser.add_argument("--transcript", help="SRT, VTT ou JSON do faster-whisper")
    parser.add_argument(
        "--axis",
        choices=("auto", "seconds", "percent"),
        default="auto",
        help="eixo da primeira coluna (padrão: auto)",
    )
    parser.add_argument("--min-3s", type=float, default=DEFAULT_MIN_3S)
    parser.add_argument("--min-10s", type=float, default=DEFAULT_MIN_10S)
    parser.add_argument("--min-cliff-drop", type=float, default=DEFAULT_MIN_CLIFF_DROP)
    parser.add_argument("--min-cliff-rate", type=float, default=DEFAULT_MIN_CLIFF_RATE)
    parser.add_argument("--top-cliffs", type=int, default=5)
    parser.add_argument("--transcript-window", type=float, default=2.0)
    parser.add_argument("--json", action="store_true", help="saída JSON")
    args = parser.parse_args()

    if not os.path.exists(args.csv):
        parser.error(f"arquivo não encontrado: {args.csv}")

    rows, hint = load_csv(args.csv)
    if len(rows) < 2:
        print("não consegui ler pelo menos 2 pontos do CSV", file=sys.stderr)
        raise SystemExit(1)

    axis = args.axis if args.axis != "auto" else detect_axis(rows, hint, args.duration)
    try:
        rows = to_seconds(rows, axis, args.duration)
    except ValueError as exc:
        parser.error(str(exc))

    rows = [(max(0.0, x), y) for x, y in rows]
    rows.sort(key=lambda p: p[0])
    if args.duration is not None:
        rows = [(min(x, args.duration), y) for x, y in rows]

    hooks = build_hooks(rows, args.duration, args.min_3s, args.min_10s)
    cliffs = build_cliffs(
        rows, args.min_cliff_drop, args.min_cliff_rate, args.top_cliffs
    )
    slide = build_slide(rows)

    cues = load_transcript(args.transcript) if args.transcript else []
    said = {
        str(c["from_seconds"]): said_at(cues, c["from_seconds"], args.transcript_window)
        for c in cliffs
        if cues
    }

    payload = {
        "file": os.path.basename(args.csv),
        "points": len(rows),
        "axis": axis,
        "duration": args.duration,
        "start": round(rows[0][1], 2),
        "end": round(rows[-1][1], 2),
        "hooks": hooks,
        "cliffs": cliffs,
        "slide": slide,
        "said": said,
        "thresholds": {"min_3s": args.min_3s, "min_10s": args.min_10s},
    }

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return

    print(
        f"\n  {payload['file']}   {payload['points']} pontos   "
        f"{_fmt_pct(payload['start'])} -> {_fmt_pct(payload['end'])}"
    )
    print(
        f"  eixo: {axis}"
        + (f"   duração: {args.duration:.1f} s" if args.duration else "")
    )
    print("\n  RETENÇÃO NO GANCHO")
    for hook in hooks:
        line = (
            f"    {hook['label']:<5} {_fmt_pct(hook['retained']):>6}   "
            f"perda {hook['leak']:5.1f}"
        )
        if hook["status"] == "legado":
            line += "   [legado long-form]"
        else:
            line += f"   [{hook['status']}]"
        print(line)
    print("    3 s e 10 s são as janelas de Shorts; 30 s não é gate de Short.")

    print("\n  QUEDAS")
    if not cliffs:
        print("    nenhuma queda acima do limiar — a perda é slide, não momento")
    for cliff in cliffs:
        where = (
            f"{cliff['from_seconds']:.1f}s -> {cliff['to_seconds']:.1f}s"
        )
        line = (
            f"    -{cliff['lost']:.1f} p.p.  em {where:<20} "
            f"({cliff['per_second']:.1f} p.p./s)"
        )
        key = str(cliff["from_seconds"])
        if said.get(key):
            line += f'   "{said[key]}"'
        print(line)

    slide = payload["slide"]
    print("\n  SLIDE")
    print(
        f"    -{slide['loss']:.1f} p.p. de {slide['from_seconds']:.1f}s "
        f"a {slide['to_seconds']:.1f}s ({slide['per_second']:.2f} p.p./s)"
    )
    print("    queda é um momento; slide é ritmo. O fix é diferente.")
    print(
        f"\n  Metas provisórias: 3 s >= {args.min_3s:.0f}% ; "
        f"10 s >= {args.min_10s:.0f}% . Calibrar depois de 6 vídeos.\n"
    )


if __name__ == "__main__":
    main()

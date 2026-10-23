#!/usr/bin/env python3
r"""Testes dos helpers vendorizados de youtube-agent-skill.

Rodar da raiz:
    .\.venv\Scripts\python.exe scripts\test_youtube_agent.py
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RETENTION = ROOT / "tools" / "youtube-agent-skill" / "yt-retention" / "retention.py"
TITLE = ROOT / "tools" / "youtube-agent-skill" / "yt-package" / "title.py"
HOOKS = ROOT / "tools" / "youtube-agent-skill" / "yt-script" / "hooks.json"


def run_json(script: Path, args: list[str]) -> object:
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    result = subprocess.run(
        [sys.executable, "-X", "utf8", str(script), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=env,
        check=False,
    )
    if result.returncode != 0:
        raise AssertionError(
            f"{script.name} falhou ({result.returncode})\n"
            f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}"
        )
    return json.loads(result.stdout)


def write_csv(path: Path, header: str | None, rows: list[tuple[float, float]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        if header:
            fh.write(header + "\n")
        for x, y in rows:
            fh.write(f"{x},{y}\n")


class RetentionTests(unittest.TestCase):
    def test_seconds_axis_with_header(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            csv_path = Path(tmp) / "retencao.csv"
            write_csv(
                csv_path,
                "Elapsed (seconds),Audience retention (%)",
                [(0, 100), (3, 90), (10, 70), (30, 60), (45, 50)],
            )
            data = run_json(
                RETENTION, [str(csv_path), "--duration", "45", "--json"]
            )
            self.assertEqual(data["axis"], "seconds")
            hooks = {h["seconds"]: h for h in data["hooks"]}
            self.assertAlmostEqual(hooks[3.0]["retained"], 90.0, places=1)
            self.assertAlmostEqual(hooks[10.0]["retained"], 70.0, places=1)
            self.assertAlmostEqual(data["end"], 50.0, places=1)

    def test_seconds_axis_without_header_for_45s_short(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            csv_path = Path(tmp) / "retencao.csv"
            write_csv(
                csv_path,
                None,
                [(0, 100), (3, 90), (10, 70), (30, 60), (45, 50)],
            )
            data = run_json(
                RETENTION, [str(csv_path), "--duration", "45", "--json"]
            )
            # Regressão do bug do original: max 45 <= 100.5 era lido como %.
            self.assertEqual(data["axis"], "seconds")
            hooks = {h["seconds"]: h for h in data["hooks"]}
            self.assertAlmostEqual(hooks[3.0]["retained"], 90.0, places=1)

    def test_percent_axis_with_duration(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            csv_path = Path(tmp) / "retencao.csv"
            write_csv(
                csv_path,
                "Elapsed (%),Audience retention (%)",
                [
                    (0, 100),
                    (6.6667, 90),
                    (22.2222, 70),
                    (66.6667, 60),
                    (100, 50),
                ],
            )
            data = run_json(
                RETENTION, [str(csv_path), "--duration", "45", "--json"]
            )
            self.assertEqual(data["axis"], "percent")
            hooks = {h["seconds"]: h for h in data["hooks"]}
            self.assertAlmostEqual(hooks[3.0]["retained"], 90.0, places=1)
            self.assertAlmostEqual(hooks[10.0]["retained"], 70.0, places=1)

    def test_absolute_percent_axis_is_normalized(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            csv_path = Path(tmp) / "retencao.csv"
            write_csv(
                csv_path,
                "Posição no vídeo (%),Retenção absoluta de público (%)",
                [
                    (0, 162.11),
                    (6.6667, 150.0),
                    (22.2222, 100.0),
                    (66.6667, 75.0),
                    (100, 68.0),
                ],
            )
            data = run_json(
                RETENTION, [str(csv_path), "--duration", "45", "--json"]
            )
            self.assertEqual(data["axis"], "percent")
            self.assertAlmostEqual(data["start"], 100.0, places=1)
            hooks = {h["seconds"]: h for h in data["hooks"]}
            self.assertAlmostEqual(hooks[3.0]["retained"], 92.5, places=1)
            self.assertAlmostEqual(hooks[10.0]["retained"], 61.7, places=1)
            self.assertAlmostEqual(data["end"], 42.0, places=1)

    def test_transcript_names_the_cliff(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            csv_path = Path(tmp) / "retencao.csv"
            srt_path = Path(tmp) / "transcricao.srt"
            write_csv(
                csv_path,
                "Elapsed (seconds),Audience retention (%)",
                [(0, 100), (3, 90), (10, 70), (11, 55), (45, 50)],
            )
            srt_path.write_text(
                "1\n00:00:09,000 --> 00:00:11,000\nO navio estava vazio.\n",
                encoding="utf-8",
            )
            data = run_json(
                RETENTION,
                [
                    str(csv_path),
                    "--duration",
                    "45",
                    "--transcript",
                    str(srt_path),
                    "--json",
                ],
            )
            self.assertTrue(data["cliffs"], "a queda de 15 p.p. deveria ser detectada")
            self.assertIn("navio", data["said"].get("10.0", "").lower())


class TitleTests(unittest.TestCase):
    def test_ptbr_flags_caps_vague_and_missing_specificity(self) -> None:
        data = run_json(
            TITLE,
            ["--title", "O mistério INCRÍVEL do NAVIO SEM tripulação", "--json"],
        )
        result = data[0]
        keys = {key for key, _ in result["issues"]}
        self.assertIn("shouting", keys)
        self.assertIn("vague", keys)
        self.assertIn("no-number", keys)

    def test_proper_name_counts_as_specificity(self) -> None:
        data = run_json(
            TITLE,
            ["--title", "Mary Celeste: o navio encontrado vazio em 1872", "--json"],
        )
        result = data[0]
        keys = {key for key, _ in result["issues"]}
        self.assertNotIn("no-number", keys)
        self.assertLessEqual(result["chars"], 60)

    def test_thumbnail_duplicate_is_flagged(self) -> None:
        data = run_json(
            TITLE,
            [
                "--title",
                "Mary Celeste: o navio encontrado vazio em 1872",
                "--thumb",
                "NAVIO VAZIO",
                "--json",
            ],
        )
        keys = {key for key, _ in data[0]["issues"]}
        self.assertIn("duplicate", keys)


class HookSourceTests(unittest.TestCase):
    def test_hooks_json_has_21_formulas(self) -> None:
        data = json.loads(HOOKS.read_text(encoding="utf-8"))
        self.assertEqual(len(data["hooks"]), 21)
        for hook in data["hooks"]:
            self.assertIn("id", hook)
            self.assertIn("shape", hook)
            self.assertTrue(hook["match"])

    def test_ptbr_checklist_has_21_rows(self) -> None:
        text = (ROOT / "docs" / "GANCHOS-21.md").read_text(encoding="utf-8")
        rows = [line for line in text.splitlines() if line.startswith("| ") and "|" in line]
        numbered = [
            line
            for line in rows
            if line.split("|")[1].strip().isdigit()
        ]
        self.assertEqual(len(numbered), 21)


if __name__ == "__main__":
    unittest.main(verbosity=2)

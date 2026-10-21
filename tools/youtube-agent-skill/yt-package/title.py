#!/usr/bin/env python3
"""title.py - lint de título + thumbnail para YouTube, em PT-BR.

Adaptado de Jakeschincariol/youtube-agent-skill (MIT), commit a2feb21.
Mudanças:
  - stopwords, termos vagos e mensagens em português;
  - normalização Unicode para comparar palavras com/sem acento;
  - nome próprio conta como especificidade, além de número/data;
  - o score é heurístico: use os problemas listados, não o número isolado.

Uso:
    python title.py --title "Mary Celeste: o navio encontrado vazio em 1872"
    python title.py --title "..." --thumb "NAVIO VAZIO"
    python title.py titles.txt
    python title.py --title "..." --json

O título e a thumbnail são uma unidade. Se os dois dizem a mesma coisa, metade
da superfície de clique foi desperdiçada.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata


DESKTOP, MOBILE, HARD = 60, 40, 100

VAGUE = {
    "incrivel",
    "inacreditavel",
    "insano",
    "louco",
    "enorme",
    "gigante",
    "melhor",
    "pior",
    "segredo",
    "revolucionario",
    "épico",
    "epico",
    "perfeito",
    "completo",
    "tudo",
    "chocante",
    "surreal",
    "bizarro",
    "assustador",
    "perturbador",
    "arrepiante",
    "sinistro",
    "definitivo",
    "ultimo",
    "ultima",
}

STOP = {
    "o",
    "a",
    "os",
    "as",
    "de",
    "do",
    "da",
    "dos",
    "das",
    "em",
    "no",
    "na",
    "nos",
    "nas",
    "um",
    "uma",
    "uns",
    "umas",
    "para",
    "por",
    "com",
    "sem",
    "e",
    "ou",
    "é",
    "e",
    "sao",
    "que",
    "se",
    "ao",
    "aos",
    "à",
    "às",
    "as",
    "como",
    "quando",
    "onde",
    "porque",
    "sobre",
    "entre",
    "depois",
    "antes",
    "ate",
    "até",
    "mas",
    "ja",
    "já",
    "nao",
    "não",
    "sim",
    "ele",
    "ela",
    "eles",
    "elas",
    "isso",
    "isto",
    "aquilo",
    "esse",
    "essa",
    "este",
    "esta",
    "aquele",
    "aquela",
    "eu",
    "voce",
    "você",
    "voces",
    "vocês",
    "nos",
    "nós",
    "me",
    "te",
    "lhe",
    "meu",
    "minha",
    "seu",
    "sua",
    "nosso",
    "nossa",
}


def fold(text: str) -> str:
    """Minúsculas sem acento, para comparar palavras."""
    normalized = unicodedata.normalize("NFKD", text)
    return "".join(c for c in normalized if not unicodedata.combining(c)).lower()


def words(text: str) -> list[str]:
    return re.findall(r"[a-z0-9']+", fold(text))


def proper_names(text: str) -> list[str]:
    """Nomes com duas palavras capitalizadas ou siglas; evita 'O Farol'."""
    names = re.findall(
        r"\b[A-ZÀ-ÖØ-Þ][a-zà-öø-ÿ'’-]{2,}\s+[A-ZÀ-ÖØ-Þ][a-zà-öø-ÿ'’-]{2,}\b",
        text,
    )
    # Siglas curtas (USS, DNA). Evita contar palavras em caixa alta como "NAVIO".
    acronyms = [
        token
        for token in re.findall(r"\b[A-ZÀ-ÖØ-Þ]{2,4}\b", text)
        if fold(token) not in STOP and fold(token) not in VAGUE
    ]
    return list(dict.fromkeys(names + acronyms))


def check(title: str, thumb: str | None = None) -> dict:
    t = title.strip()
    n = len(t)
    issues: list[tuple[str, str]] = []
    good: list[str] = []

    if n > HARD:
        issues.append(("length", f"{n} caracteres — o limite duro do YouTube é {HARD}"))
    elif n > DESKTOP:
        issues.append(
            ("length", f"{n} caracteres — a busca no desktop corta perto de {DESKTOP}")
        )
    else:
        good.append(f"{n} caracteres, dentro do corte de {DESKTOP} do desktop")

    if n > MOBILE:
        head = t[:MOBILE].rsplit(" ", 1)[0]
        issues.append(
            (
                "mobile",
                f'o feed mobile mostra cerca de "{head}..." — '
                "confira se o sujeito sobrevive",
            )
        )

    caps = [w for w in t.split() if len(w) > 2 and w.isupper()]
    if len(caps) > 2:
        issues.append(
            (
                "shouting",
                f"{len(caps)} palavras em caixa alta — duas é o teto antes de parecer spam",
            )
        )
    elif caps:
        good.append(f"{len(caps)} palavra em caixa alta para ênfase")

    vague = [w for w in words(t) if w in VAGUE]
    if vague:
        issues.append(
            (
                "vague",
                f"{', '.join(sorted(set(vague)))} — troque por número, nome ou data",
            )
        )

    nums = re.findall(r"\d[\d.,]*%?", t)
    names = proper_names(t)
    if nums:
        good.append(f"traz um dado concreto ({', '.join(nums[:3])})")
    elif names:
        good.append(f"traz nome próprio ({', '.join(names[:2])})")
    else:
        issues.append(
            (
                "no-number",
                "sem número, data ou nome próprio — o ajuste mais confiável",
            )
        )

    if t.endswith("?"):
        good.append("pergunta aberta no título")

    front = [w for w in words(t)[:3] if w not in STOP]
    if not front:
        issues.append(
            ("front-load", "as três primeiras palavras são só filler — traga o sujeito")
        )

    if thumb:
        title_words = set(words(t)) - STOP
        thumb_words = set(words(thumb)) - STOP
        shared = title_words & thumb_words
        if shared:
            issues.append(
                (
                    "duplicate",
                    f"a thumbnail repete o título em {', '.join(sorted(shared))} — "
                    "ela deve dizer o que o título não diz",
                )
            )
        else:
            good.append("thumbnail e título carregam palavras diferentes")
        if len(words(thumb)) > 4:
            issues.append(
                (
                    "thumb-length",
                    f"{len(words(thumb))} palavras na thumbnail — "
                    "três é o teto no tamanho do feed",
                )
            )

    score = max(0, min(100, 100 - 14 * len(issues) + 4 * len(good)))
    return {"title": t, "chars": n, "score": score, "issues": issues, "good": good}


def show(result: dict) -> None:
    print(f'\n  "{result["title"]}"')
    print(f"  {result['chars']} caracteres   score {result['score']}/100")
    for key, message in result["issues"]:
        print(f"    x  {key:<12} {message}")
    for message in result["good"]:
        print(f"    ok              {message}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Lint de título e thumbnail para YouTube em PT-BR."
    )
    parser.add_argument("file", nargs="?", help="arquivo com um título por linha")
    parser.add_argument("--title", help="título único")
    parser.add_argument("--thumb", help="texto da thumbnail, se houver")
    parser.add_argument("--json", action="store_true", help="saída JSON")
    args = parser.parse_args()

    if args.title:
        rows = [check(args.title, args.thumb)]
    elif args.file:
        with open(args.file, encoding="utf-8-sig") as fh:
            lines = [line.strip() for line in fh if line.strip()]
        rows = [check(line, args.thumb) for line in lines]
    else:
        parser.print_help()
        raise SystemExit(1)

    rows.sort(key=lambda row: -row["score"])
    if args.json:
        print(json.dumps(rows, ensure_ascii=False, indent=2))
        return

    for row in rows:
        show(row)
    print()


if __name__ == "__main__":
    main()

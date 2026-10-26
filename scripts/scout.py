#!/usr/bin/env python3
"""Scout de canais: mede quais canais de Shorts estao **acelerando agora**.

NAO descobre canais sozinho. Isso e decisao de desenho, nao preguica: o yt-dlp
nao respeita os filtros de busca do YouTube (testado em 26/10/2026: `sp` de
Shorts e de ordenar por data sao ignorados, e `ytsearchdate` nao existe nesta
versao). Descoberta automatica por hashtag tambem e ruido: a pagina
`/hashtag/truecrime` devolve 135 canais majoritariamente em ingles.

O que funciona, e e o que este script faz:

- A lista `/shorts` de um canal vem **ordenada do mais novo para o mais antigo**.
  Logo a posicao na lista e a recencia — nao precisa de data de upload.
- `yt-dlp -J --flat-playlist` nessa lista devolve titulo, id, duracao, views
  (arredondadas) e o total de inscritos do canal.

Entao: **voce traz os canais, o script mede.** Fonte natural de descoberta e o
seu proprio feed de Shorts — o algoritmo ja esta te mostrando os concorrentes do
nicho. Coloque os canais em `biblioteca/canais-semente.txt` (um por linha,
URL ou ID).

Metricas (todas relativas, para sobreviver ao arredondamento das views):

- `aceleracao` = mediana das 5 mais recentes / mediana das mais antigas.
  > 1,5 = o canal esta subindo agora. < 0,7 = ja passou o pico.
- `breakout` = maior short / mediana da janela. Mede se um video furou.
- `views_por_inscrito` = mediana / inscritos. Proxy externo de retencao: o
  YouTube so continua empurrando para publico frio quando a retencao segura.
- `n_lidos` = quantos shorts a janela alcancou. Poucos shorts + mediana alta =
  canal novo com tracao — o alvo mais barato de modelar.

A medida honesta de velocidade so aparece no **segundo** snapshot: `--diff`
compara os mesmos shorts entre datas e devolve views/dia.

Uso:
    .venv\\Scripts\\python.exe scripts\\scout.py
    .venv\\Scripts\\python.exe scripts\\scout.py --janela 40
    .venv\\Scripts\\python.exe scripts\\scout.py --diff

Saidas:
    logs/scout-YYYY-MM-DD.json   snapshot completo
    stdout                       tabela ranqueada
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
YTDLP = ROOT / ".venv" / "Scripts" / "yt-dlp.exe"
LOGS = ROOT / "logs"
SEEDS = ROOT / "biblioteca" / "canais-semente.txt"

DUR_MIN, DUR_MAX = 15, 180


def eprint(*a: object) -> None:
    print(*a, file=sys.stderr, flush=True)


def ler_sementes(caminho: Path) -> list[str]:
    if not caminho.exists():
        return []
    alvos = []
    for linha in caminho.read_text(encoding="utf-8").splitlines():
        linha = linha.split("#", 1)[0].strip()
        if not linha:
            continue
        m = re.search(r"(UC[\w-]{22})", linha)
        alvos.append(m.group(1) if m else linha)
    return alvos


def ytdlp_json(url: str, extra: list[str], timeout: int = 180) -> dict[str, Any] | None:
    cmd = [str(YTDLP), "-J", "--flat-playlist", "--no-warnings",
           "--ignore-errors", *extra, url]
    try:
        out = subprocess.run(cmd, capture_output=True, timeout=timeout,
                             check=False, encoding="utf-8", errors="replace")
    except subprocess.TimeoutExpired:
        eprint("  timeout")
        return None
    if not out.stdout:
        return None
    try:
        return json.loads(out.stdout)
    except json.JSONDecodeError:
        return None


def med(vals: list[float]) -> float:
    vals = [float(v) for v in vals if v is not None]
    return statistics.median(vals) if vals else 0.0


def perfil(alvo: str, janela: int) -> dict[str, Any] | None:
    if alvo.startswith("UC") and len(alvo) == 24:
        url = f"https://www.youtube.com/channel/{alvo}/shorts"
    elif alvo.startswith("@"):
        url = f"https://www.youtube.com/{alvo}/shorts"
    else:
        url = alvo.rstrip("/") + "/shorts"

    data = ytdlp_json(url, [f"--playlist-end={janela}"])
    if not data:
        return None
    # Na aba /shorts o yt-dlp nao entrega `duration` (vem None). A aba ja e de
    # Shorts por definicao, entao so filtra quando a duracao existe.
    ents = []
    for e in data.get("entries") or []:
        if not e.get("id"):
            continue
        dur = e.get("duration")
        if dur is not None and not (DUR_MIN <= dur <= DUR_MAX):
            continue
        ents.append(e)
    if not ents:
        return None

    views = [float(e.get("view_count") or 0) for e in ents]
    m_geral = med(views)
    m_novo = med(views[:5])
    m_antigo = med(views[10:janela] or views[5:])
    inscritos = data.get("channel_follower_count")

    return {
        "canal_id": data.get("channel_id") or alvo,
        "canal": data.get("channel") or data.get("uploader") or alvo,
        "url": data.get("channel_url") or url,
        "inscritos": inscritos,
        "n_lidos": len(ents),
        "janela": janela,
        "mediana": m_geral,
        "med_novo": m_novo,
        "med_antigo": m_antigo,
        "aceleracao": round(m_novo / m_antigo, 2) if m_antigo else None,
        "breakout": round(max(views) / m_geral, 2) if m_geral else None,
        "views_por_inscrito": round(m_geral / inscritos, 3) if inscritos else None,
        "top_shorts": [
            {"id": e.get("id"), "views": e.get("view_count"),
             "dur": e.get("duration"),
             "titulo": (e.get("title") or "")[:80]}
            for e in ents[:12]
        ],
    }


def score(c: dict[str, Any]) -> float:
    """Ranqueia candidato a ser modelado.

    Premia aceleracao e breakout (o canal esta sendo empurrado agora), views por
    inscrito (proxy de retencao) e canal pequeno (mais barato de copiar).

    A escala entra como log10 para nao deixar canal de 40 views liderar so por
    ter razao alta: em volume baixo, `aceleracao` e ruido puro (40 → 280 views
    da 7x sem significar nada).
    """
    import math
    s = 0.0
    s += min(c.get("aceleracao") or 0, 5) * 2.0
    s += min(c.get("breakout") or 0, 10) * 0.8
    s += min(c.get("views_por_inscrito") or 0, 20) * 0.6
    escala = math.log10(max(c.get("med_novo") or 1, 1))
    s += min(escala, 5.5) * 2.2                     # 100 views ≈ 4,4 · 10k ≈ 8,8
    n = c.get("n_lidos") or 0
    if 0 < n < 40:
        s += 3.0
    if 0 < n < 20:
        s += 1.5
    if (c.get("med_novo") or 0) < 500:
        s -= 4.0                                     # ruido estatistico
    return round(s, 1)


def num(v: Any) -> str:
    if v is None:
        return "–"
    if abs(v) >= 1000:
        return f"{v/1000:.0f}k"
    return f"{v:g}"


def tabela(canais: list[dict[str, Any]]) -> str:
    linhas = [
        "| # | Canal | Score | Acel. | Breakout | Views/inscr. | Shorts lidos | Mediana | 5 novos | Inscr. |",
        "|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for i, c in enumerate(canais, 1):
        ace = "–" if c.get("aceleracao") is None else f"{c['aceleracao']:g}x"
        brk = "–" if c.get("breakout") is None else f"{c['breakout']:g}x"
        vpi = "–" if c.get("views_por_inscrito") is None else f"{c['views_por_inscrito']:g}"
        linhas.append(
            f"| {i} | {c['canal'][:26]} | **{c['score']}** | {ace} | {brk} | {vpi} "
            f"| {c['n_lidos']} | {num(c['mediana'])} | {num(c['med_novo'])} "
            f"| {num(c['inscritos'])} |"
        )
    return "\n".join(linhas)


def comparar(velho: dict[str, Any], novo: dict[str, Any]) -> str:
    """Diffta os mesmos shorts entre snapshots -> views/dia real.

    Unica medida honesta de "crescendo rapido": o mesmo video acumulando views
    entre duas datas. Views vem arredondadas no modo flat, entao diferencas
    pequenas nao contam.
    """
    try:
        dias = (date.fromisoformat(novo["data"]) - date.fromisoformat(velho["data"])).days
    except Exception:
        dias = 0
    if dias <= 0:
        return "(snapshots do mesmo dia — espere 48-72 h)"

    antes: dict[str, float] = {}
    for c in velho["canais"]:
        for s in c.get("top_shorts") or []:
            if s.get("id") and s.get("views") is not None:
                antes[s["id"]] = float(s["views"])

    linhas = []
    for c in novo["canais"]:
        ganho, n = 0.0, 0
        for s in c.get("top_shorts") or []:
            if s.get("id") in antes and s.get("views") is not None:
                ganho += float(s["views"]) - antes[s["id"]]
                n += 1
        if n:
            linhas.append((ganho / dias, c["canal"], n, ganho / n / dias))
    linhas.sort(reverse=True)

    out = ["| Views/dia | Canal | Shorts comparados | Views/dia por short |",
           "|---:|---|---:|---:|"]
    for g, nome, n, por in linhas[:20]:
        out.append(f"| **{g:,.0f}** | {nome[:30]} | {n} | {por:,.0f} |".replace(",", "."))
    out.append(f"\n_{dias} dia(s) entre snapshots. Só entra short presente nas duas leituras._")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Mede canais de Shorts que estao acelerando")
    ap.add_argument("--sementes", default=str(SEEDS), help="arquivo com um canal por linha")
    ap.add_argument("--canais", nargs="*", default=None, help="canais avulsos (URL ou UC...)")
    ap.add_argument("--janela", type=int, default=30, help="shorts lidos por canal")
    ap.add_argument("--diff", action="store_true", help="compara com o snapshot anterior")
    args = ap.parse_args(argv)

    alvos = (args.canais or []) + ler_sementes(Path(args.sementes))
    if not alvos:
        eprint(f"nenhum canal: preencha {args.sementes} ou use --canais")
        return 2

    LOGS.mkdir(exist_ok=True)
    canais: list[dict[str, Any]] = []
    for i, alvo in enumerate(alvos, 1):
        eprint(f"  {i}/{len(alvos)}: {alvo[:55]}")
        p = perfil(alvo, args.janela)
        if p:
            p["score"] = score(p)
            canais.append(p)
        else:
            eprint("      sem dados")

    if not canais:
        eprint("nenhum canal respondeu")
        return 1

    canais.sort(key=lambda c: -c["score"])
    hoje = date.today().isoformat()
    snap = LOGS / f"scout-{hoje}.json"
    snap.write_text(json.dumps({"data": hoje, "janela": args.janela, "canais": canais},
                               ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\n## Scout {hoje} — {len(canais)} canais\n")
    print(tabela(canais))
    print(f"\nsnapshot: `logs/scout-{hoje}.json`")

    if args.diff:
        anteriores = [p for p in sorted(LOGS.glob("scout-*.json")) if p.name != snap.name]
        if not anteriores:
            print("\n(sem snapshot anterior — rode de novo em 48-72 h para ter velocidade)")
        else:
            print(f"\n## Velocidade real vs `{anteriores[-1].name}`\n")
            print(comparar(json.loads(anteriores[-1].read_text(encoding="utf-8")), {"data": hoje, "canais": canais}))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

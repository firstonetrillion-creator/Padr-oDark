#!/usr/bin/env python3
"""Coleta metadados de Shorts para comparar nichos.

Nao baixa video: usa yt-dlp apenas para listar canais/Shorts e ler metadados.
A metrica principal e views por inscrito; retencao real nao existe em metadados.

Uso tipico:
    .\\.venv\\Scripts\\python.exe scripts\\nicho.py
    .\\.venv\\Scripts\\python.exe scripts\\nicho.py --limit 3 --refresh

Saidas:
    logs/nicho-YYYY-MM-DD.json   (dados completos)
    docs/NICHO.md                (secao de dados, preservando o resto do arquivo)
"""

from __future__ import annotations

import argparse
import json
import shutil
import statistics
import subprocess
import sys
import time
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_YTDLP = ROOT / ".venv" / "Scripts" / "yt-dlp.exe"
OWN_CHANNEL_ID = "UCwgP68Uen2KoIh2R-j231Yw"
OWN_CHANNEL_NAME = "cod mind million"

MISTERIO_QUERIES = [
    "mistério arquivo",
    "mistérios reais",
    "casos sem solução",
    "arquivo oculto",
    "mistério história real",
    "farol mistério",
]

PSICOLOGIA_QUERIES = [
    "psicologia sombria",
    "manipulação psicológica",
    "sinais de manipulação",
    "sabotagem psicológica",
    "comportamento humano sombrio",
    "autoengano",
]

NICHE_LABELS = {
    "misterio": "Mistério / Arquivo",
    "psicologia": "Psicologia sombria",
}


def eprint(*args: object) -> None:
    print(*args, file=sys.stderr, flush=True)


def fmt_int(value: Any) -> str:
    if value is None:
        return "—"
    try:
        return f"{int(value):,}".replace(",", ".")
    except (TypeError, ValueError):
        return "—"


def fmt_float(value: Any, digits: int = 1, suffix: str = "") -> str:
    if value is None:
        return "—"
    try:
        return f"{float(value):.{digits}f}{suffix}"
    except (TypeError, ValueError):
        return "—"


def fmt_duration(value: Any) -> str:
    if value is None:
        return "—"
    try:
        seconds = int(round(float(value)))
    except (TypeError, ValueError):
        return "—"
    return f"{seconds}s"


def fmt_date(value: Any) -> str:
    if not value:
        return "—"
    text = str(value)
    if len(text) == 8 and text.isdigit():
        return f"{text[:4]}-{text[4:6]}-{text[6:8]}"
    return text


def md_escape(value: Any, limit: int | None = None) -> str:
    text = "" if value is None else str(value)
    text = text.replace("\r", " ").replace("\n", " ").replace("|", "\\|").strip()
    if limit and len(text) > limit:
        text = text[: limit - 1].rstrip() + "…"
    return text


def parse_upload_date(value: Any) -> date | None:
    if not value:
        return None
    text = str(value)
    if len(text) != 8 or not text.isdigit():
        return None
    try:
        return date(int(text[:4]), int(text[4:6]), int(text[6:8]))
    except ValueError:
        return None


class YtDlp:
    def __init__(self, executable: Path, timeout: int = 90, sleep: float = 0.5) -> None:
        self.executable = executable
        self.timeout = timeout
        self.sleep = sleep
        self.calls = 0

    def _run(self, args: list[str]) -> dict[str, Any]:
        cmd = [
            str(self.executable),
            "--no-warnings",
            "--ignore-errors",
            "--socket-timeout",
            "30",
            *args,
        ]
        self.calls += 1
        try:
            proc = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=self.timeout,
            )
        except subprocess.TimeoutExpired as exc:
            raise RuntimeError(f"timeout após {self.timeout}s") from exc

        if proc.returncode != 0:
            detail = (proc.stderr or proc.stdout or "").strip().splitlines()
            raise RuntimeError(detail[-1] if detail else f"yt-dlp saiu com {proc.returncode}")

        output = (proc.stdout or "").strip()
        if not output:
            raise RuntimeError("yt-dlp não devolveu JSON")

        try:
            data = json.loads(output)
        except json.JSONDecodeError as exc:
            snippet = output[:300].replace("\n", " ")
            raise RuntimeError(f"JSON inválido: {snippet}") from exc

        if not isinstance(data, dict):
            raise RuntimeError("JSON inesperado (não é objeto)")
        return data

    def search(self, query: str, limit: int) -> list[dict[str, Any]]:
        data = self._run(
            [
                "--flat-playlist",
                "--dump-single-json",
                "--playlist-end",
                str(limit),
                f"ytsearch{limit}:{query}",
            ]
        )
        entries = data.get("entries") or []
        return [entry for entry in entries if isinstance(entry, dict)]

    def channel_shorts(self, channel_id: str, channel_url: str | None, limit: int) -> dict[str, Any]:
        base = (channel_url or "").rstrip("/")
        if not base:
            if channel_id.startswith("UC"):
                base = f"https://www.youtube.com/channel/{channel_id}"
            elif channel_id.startswith("@"):
                base = f"https://www.youtube.com/{channel_id}"
            else:
                base = f"https://www.youtube.com/@{channel_id}"
        url = base + "/shorts"
        return self._run(
            [
                "--flat-playlist",
                "--dump-single-json",
                "--playlist-end",
                str(limit),
                url,
            ]
        )

    def video(self, video_id: str) -> dict[str, Any]:
        last_error: Exception | None = None
        for client in ("android", "web"):
            try:
                return self._run(
                    [
                        "--skip-download",
                        "--dump-single-json",
                        "--extractor-args",
                        f"youtube:player_client={client}",
                        f"https://www.youtube.com/watch?v={video_id}",
                    ]
                )
            except Exception as exc:  # tenta o próximo cliente
                last_error = exc
        raise RuntimeError(str(last_error) if last_error else "falha ao ler vídeo")

    def wait(self) -> None:
        if self.sleep > 0:
            time.sleep(self.sleep)


def load_cache(cache_dir: Path, video_id: str) -> dict[str, Any] | None:
    path = cache_dir / f"{video_id}.json"
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def save_cache(cache_dir: Path, video_id: str, data: dict[str, Any]) -> None:
    cache_dir.mkdir(parents=True, exist_ok=True)
    path = cache_dir / f"{video_id}.json"
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def channel_key(entry: dict[str, Any]) -> str | None:
    value = entry.get("channel_id") or entry.get("uploader_id")
    return str(value) if value else None


def channel_name(entry: dict[str, Any]) -> str:
    return str(entry.get("channel") or entry.get("uploader") or "")


def is_own_channel(channel_id: str | None, name: str) -> bool:
    if channel_id and channel_id == OWN_CHANNEL_ID:
        return True
    return name.strip().lower() == OWN_CHANNEL_NAME


def discover_channels(
    yt: YtDlp,
    queries: list[str],
    search_limit: int,
    max_channels: int,
    own_channel_id: str,
) -> tuple[list[dict[str, Any]], list[str]]:
    found: dict[str, dict[str, Any]] = {}
    errors: list[str] = []

    for query in queries:
        try:
            entries = yt.search(query, search_limit)
        except Exception as exc:
            errors.append(f"busca '{query}': {exc}")
            eprint(f"  ! busca falhou: {query}: {exc}")
            yt.wait()
            continue

        added = 0
        for entry in entries:
            cid = channel_key(entry)
            name = channel_name(entry)
            if not cid or is_own_channel(cid, name) or cid.startswith(OWN_CHANNEL_ID):
                continue
            if cid not in found:
                found[cid] = {
                    "channel_id": cid,
                    "channel": name,
                    "channel_url": entry.get("channel_url") or entry.get("uploader_url"),
                    "query": query,
                }
                added += 1
        eprint(f"  busca '{query}': {len(entries)} resultados, {added} canais novos")
        yt.wait()

    channels = list(found.values())[:max_channels]
    return channels, errors


def collect_niche(
    yt: YtDlp,
    niche: str,
    queries: list[str],
    args: argparse.Namespace,
    cache_dir: Path,
) -> dict[str, Any]:
    label = NICHE_LABELS.get(niche, niche)
    eprint(f"\n[{label}] descobrindo canais…")
    channels, errors = discover_channels(
        yt,
        queries,
        args.search_results,
        args.max_channels,
        args.own_channel_id,
    )
    eprint(f"[{label}] {len(channels)} canais para visitar")

    found: dict[str, dict[str, Any]] = {}
    for index, channel in enumerate(channels, start=1):
        cid = channel["channel_id"]
        name = channel.get("channel") or cid
        try:
            data = yt.channel_shorts(cid, channel.get("channel_url"), args.max_per_channel)
        except Exception as exc:
            errors.append(f"canal {name}: {exc}")
            eprint(f"  ! canal {name}: {exc}")
            yt.wait()
            continue

        subs = data.get("channel_follower_count")
        if subs is not None and (subs < args.min_subs or subs > args.max_subs):
            eprint(
                f"  [{index}/{len(channels)}] {name}: {fmt_int(subs)} inscritos "
                f"fora da faixa {fmt_int(args.min_subs)}–{fmt_int(args.max_subs)}; ignorado"
            )
            yt.wait()
            continue

        entries = data.get("entries") or []
        added = 0
        for entry in entries:
            if not isinstance(entry, dict):
                continue
            vid = entry.get("id")
            if not vid or vid in found:
                continue
            found[vid] = {
                "id": str(vid),
                "title": entry.get("title"),
                "views": entry.get("view_count"),
                "duration": entry.get("duration"),
                "channel": data.get("channel") or name,
                "channel_id": cid,
                "subs": subs,
                "query": channel.get("query"),
            }
            added += 1
            if len(found) >= args.per_niche * 2:
                break

        eprint(
            f"  [{index}/{len(channels)}] {name}: "
            f"{fmt_int(subs)} inscritos, {len(entries)} shorts, {added} novos, total {len(found)}"
        )
        yt.wait()
        if len(found) >= args.per_niche * 2:
            break

    candidates = list(found.values())
    if args.limit:
        candidates = candidates[: args.limit]

    eprint(f"[{label}] lendo metadados de {len(candidates)} shorts…")
    items: list[dict[str, Any]] = []
    for index, flat in enumerate(candidates, start=1):
        vid = flat["id"]
        meta = None if args.refresh else load_cache(cache_dir, vid)
        if meta is None:
            try:
                meta = yt.video(vid)
                save_cache(cache_dir, vid, meta)
            except Exception as exc:
                errors.append(f"vídeo {vid}: {exc}")
                eprint(f"  ! vídeo {vid}: {exc}")
                meta = None
            yt.wait()

        item = normalize_item(flat, meta)
        if item["duration"] is not None:
            if item["duration"] < args.min_duration or item["duration"] > args.max_duration:
                eprint(
                    f"  - ignorado {vid}: duração {item['duration']}s "
                    f"fora de {args.min_duration}–{args.max_duration}s"
                )
                continue
        items.append(item)
        if len(items) >= args.per_niche:
            break
        if index % 10 == 0:
            eprint(f"  … {index}/{len(candidates)} lidos, {len(items)} válidos")

    items.sort(key=lambda row: (row["views_per_sub"] is None, -(row["views_per_sub"] or 0)))
    return {
        "label": label,
        "queries": queries,
        "channels_found": len(channels),
        "items": items,
        "summary": summarize(items, args.min_subs_ranking),
        "errors": errors,
        "coverage": {
            "requested": args.per_niche,
            "collected": len(items),
        },
    }


def normalize_item(flat: dict[str, Any], meta: dict[str, Any] | None) -> dict[str, Any]:
    meta = meta or {}
    views = meta.get("view_count")
    if views is None:
        views = flat.get("views")
    subs = meta.get("channel_follower_count")
    if subs is None:
        subs = flat.get("subs")
    likes = meta.get("like_count")
    comments = meta.get("comment_count")
    duration = meta.get("duration")
    if duration is None:
        duration = flat.get("duration")

    try:
        views = int(views) if views is not None else None
    except (TypeError, ValueError):
        views = None
    try:
        subs = int(subs) if subs is not None else None
    except (TypeError, ValueError):
        subs = None
    try:
        likes = int(likes) if likes is not None else None
    except (TypeError, ValueError):
        likes = None
    try:
        comments = int(comments) if comments is not None else None
    except (TypeError, ValueError):
        comments = None
    try:
        duration = float(duration) if duration is not None else None
    except (TypeError, ValueError):
        duration = None

    upload_date = parse_upload_date(meta.get("upload_date"))
    age_days = (date.today() - upload_date).days if upload_date else None
    views_per_sub = None
    if views is not None and subs is not None:
        views_per_sub = round(views / subs, 2) if subs > 0 else None
    like_rate = None
    if likes is not None and views:
        like_rate = round(100 * likes / views, 2)
    comment_rate = None
    if comments is not None and views:
        comment_rate = round(100 * comments / views, 2)

    video_id = str(flat.get("id") or meta.get("id") or "")
    return {
        "id": video_id,
        "title": meta.get("title") or flat.get("title") or "",
        "channel": meta.get("channel") or flat.get("channel") or "",
        "channel_id": meta.get("channel_id") or flat.get("channel_id") or "",
        "url": f"https://www.youtube.com/shorts/{video_id}",
        "views": views,
        "subs": subs,
        "likes": likes,
        "comments": comments,
        "views_per_sub": views_per_sub,
        "like_rate": like_rate,
        "comment_rate": comment_rate,
        "duration": duration,
        "upload_date": upload_date.isoformat() if upload_date else None,
        "age_days": age_days,
        "query": flat.get("query"),
        "metadata_ok": bool(meta),
    }


def median(values: list[float | int | None]) -> float | None:
    clean = [float(value) for value in values if value is not None]
    if not clean:
        return None
    return round(statistics.median(clean), 2)


def summarize(items: list[dict[str, Any]], min_subs_ranking: int) -> dict[str, Any]:
    rankable = [
        item
        for item in items
        if item["views_per_sub"] is not None and (item["subs"] or 0) >= min_subs_ranking
    ]
    top_videos = sorted(rankable, key=lambda row: -(row["views_per_sub"] or 0))[:15]
    top_views = sorted(
        [item for item in items if item["views"] is not None],
        key=lambda row: -(row["views"] or 0),
    )[:10]

    by_channel: dict[str, list[dict[str, Any]]] = {}
    for item in items:
        cid = item.get("channel_id") or item.get("channel") or "?"
        by_channel.setdefault(str(cid), []).append(item)

    channels_detail: list[dict[str, Any]] = []
    for cid, rows in by_channel.items():
        subs = median([row.get("subs") for row in rows])
        channel_views_per_sub = median([row.get("views_per_sub") for row in rows])
        if channel_views_per_sub is None or (subs or 0) < min_subs_ranking:
            continue
        channels_detail.append(
            {
                "channel": rows[0].get("channel") or "",
                "channel_id": cid,
                "subs": subs,
                "n": len(rows),
                "median_views": median([row.get("views") for row in rows]),
                "views_per_sub": channel_views_per_sub,
                "median_like_rate": median([row.get("like_rate") for row in rows]),
            }
        )
    channels_detail.sort(key=lambda row: -(row["views_per_sub"] or 0))

    return {
        "n": len(items),
        "channels": len(by_channel),
        "channels_ranked": len(channels_detail),
        "median_views": median([item["views"] for item in items]),
        "median_views_channel": median([row["median_views"] for row in channels_detail]),
        "median_views_per_sub": median([item["views_per_sub"] for item in items]),
        "median_views_per_sub_channel": median([row["views_per_sub"] for row in channels_detail]),
        "median_like_rate": median([item["like_rate"] for item in items]),
        "median_like_rate_channel": median([row["median_like_rate"] for row in channels_detail]),
        "median_comment_rate": median([item["comment_rate"] for item in items]),
        "median_duration": median([item["duration"] for item in items]),
        "channels_detail": channels_detail,
        "top_channels": channels_detail[:15],
        "top_views_per_sub": top_videos,
        "top_views": top_views,
        "min_subs_ranking": min_subs_ranking,
    }


def render_table(items: list[dict[str, Any]], limit: int = 15) -> list[str]:
    lines = [
        "| # | Canal | Short | Views | Inscritos | Views/inscrito | Like | Coment. | Duração | Data |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for index, item in enumerate(items[:limit], start=1):
        channel = item.get("channel") or "—"
        channel_url = f"https://www.youtube.com/channel/{item['channel_id']}" if item.get("channel_id") else ""
        channel_md = f"[{md_escape(channel, 28)}]({channel_url})" if channel_url else md_escape(channel, 28)
        title = md_escape(item.get("title"), 62)
        video_md = f"[{title}]({item.get('url')})" if item.get("url") else title
        lines.append(
            "| {idx} | {channel} | {title} | {views} | {subs} | {vps} | {like} | {comment} | {duration} | {date} |".format(
                idx=index,
                channel=channel_md,
                title=video_md,
                views=fmt_int(item.get("views")),
                subs=fmt_int(item.get("subs")),
                vps=fmt_float(item.get("views_per_sub"), digits=2),
                like=fmt_float(item.get("like_rate"), suffix="%"),
                comment=fmt_float(item.get("comment_rate"), suffix="%"),
                duration=fmt_duration(item.get("duration")),
                date=fmt_date(item.get("upload_date")),
            )
        )
    return lines


def render_channel_table(channels: list[dict[str, Any]], limit: int = 15) -> list[str]:
    lines = [
        "| # | Canal | Shorts | Inscritos | Mediana views | Mediana views/inscrito | Mediana like |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for index, row in enumerate(channels[:limit], start=1):
        channel = row.get("channel") or "—"
        channel_url = f"https://www.youtube.com/channel/{row['channel_id']}" if row.get("channel_id") else ""
        channel_md = f"[{md_escape(channel, 34)}]({channel_url})" if channel_url else md_escape(channel, 34)
        lines.append(
            "| {idx} | {channel} | {n} | {subs} | {views} | {vps} | {like} |".format(
                idx=index,
                channel=channel_md,
                n=row.get("n", 0),
                subs=fmt_int(row.get("subs")),
                views=fmt_int(row.get("median_views")),
                vps=fmt_float(row.get("views_per_sub"), digits=2),
                like=fmt_float(row.get("median_like_rate"), suffix="%"),
            )
        )
    return lines


def render_report(data: dict[str, Any]) -> str:
    generated = data.get("generated_at", "")
    lines = [
        "<!-- nicho-dados:start -->",
        f"## Dados coletados em {generated[:10]}",
        "",
        "> Coleta automática via `yt-dlp`, **somente metadados**. Retenção real não está disponível; views/inscrito e engajamento são proxies.",
        "",
        "### Resumo",
        "",
        "| Nicho | Shorts | Canais | Mediana views (canal) | Mediana views/inscrito (canal) | Mediana like (canal) | Mediana duração |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for niche, block in data.get("niches", {}).items():
        summary = block.get("summary", {})
        lines.append(
            "| {label} | {n} | {channels} | {views} | {vps} | {like} | {duration} |".format(
                label=block.get("label", niche),
                n=summary.get("n", 0),
                channels=summary.get("channels", 0),
                views=fmt_int(summary.get("median_views_channel")),
                vps=fmt_float(summary.get("median_views_per_sub_channel"), digits=2),
                like=fmt_float(summary.get("median_like_rate_channel"), suffix="%"),
                duration=fmt_duration(summary.get("median_duration")),
            )
        )

    lines.extend(
        [
            "",
            "**Como ler:** a amostra usa canais de "
            f"{fmt_int(data.get('config', {}).get('min_subs', 100))} a "
            f"{fmt_int(data.get('config', {}).get('max_subs', 500000))} inscritos; "
            "views por inscrito favorece canais pequenos com demanda real. Canais fora da faixa "
            "ficam de fora para evitar ruído. O script não decide o nicho: ele mede demanda; "
            "custo, risco e fit continuam na análise manual.",
            "",
        ]
    )

    for niche, block in data.get("niches", {}).items():
        summary = block.get("summary", {})
        lines.append(f"### {block.get('label', niche)}")
        lines.append("")
        coverage = block.get("coverage", {})
        lines.append(
            f"Cobertura: **{coverage.get('collected', len(block.get('items', [])))}/{coverage.get('requested', '—')}** shorts; "
            f"{block.get('channels_found', 0)} canais visitados; {summary.get('channels_ranked', 0)} canais no ranking; "
            f"{len(block.get('errors', []))} erro(s)."
        )
        lines.append("")
        lines.append("**Top 15 canais por mediana de views/inscrito**")
        lines.append("")
        lines.extend(render_channel_table(summary.get("top_channels", []), 15))
        lines.append("")
        lines.append("**Top 15 shorts por views/inscrito**")
        lines.append("")
        lines.extend(render_table(summary.get("top_views_per_sub", []), 15))
        lines.append("")
        lines.append("**Top 10 shorts por views absolutas**")
        lines.append("")
        lines.extend(render_table(summary.get("top_views", []), 10))
        lines.append("")

        errors = block.get("errors") or []
        if errors:
            lines.append("<details><summary>Erros da coleta</summary>")
            lines.append("")
            for error in errors[:40]:
                lines.append(f"- {md_escape(error)}")
            if len(errors) > 40:
                lines.append(f"- … e mais {len(errors) - 40}.")
            lines.append("")
            lines.append("</details>")
            lines.append("")

    lines.append("<!-- nicho-dados:end -->")
    return "\n".join(lines).rstrip() + "\n"


def write_markdown(path: Path, report: str) -> None:
    marker_start = "<!-- nicho-dados:start -->"
    marker_end = "<!-- nicho-dados:end -->"
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        current = path.read_text(encoding="utf-8")
    else:
        current = "# Validação de nicho\n\n"

    if marker_start in current and marker_end in current:
        before = current.split(marker_start, 1)[0].rstrip()
        after = current.split(marker_end, 1)[1].lstrip()
        new = before + "\n\n" + report + ("\n" + after if after else "")
    else:
        new = current.rstrip() + "\n\n" + report

    path.write_text(new, encoding="utf-8")


def resolve_path(value: str | None, default: Path) -> Path:
    if not value:
        return default
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Coleta metadados de Shorts por nicho (yt-dlp).")
    parser.add_argument("--per-niche", type=int, default=50, help="Shorts válidos por nicho (padrão: 50).")
    parser.add_argument("--search-results", type=int, default=50, help="Resultados de busca por query (padrão: 50).")
    parser.add_argument("--max-channels", type=int, default=60, help="Canais visitados por nicho (padrão: 60).")
    parser.add_argument("--max-per-channel", type=int, default=5, help="Shorts lidos por canal (padrão: 5).")
    parser.add_argument("--min-duration", type=float, default=10, help="Duração mínima em segundos (padrão: 10).")
    parser.add_argument("--max-duration", type=float, default=90, help="Duração máxima em segundos (padrão: 90).")
    parser.add_argument("--min-subs", type=int, default=100, help="Inscritos mínimos do canal (padrão: 100).")
    parser.add_argument("--max-subs", type=int, default=500000, help="Inscritos máximos do canal (padrão: 500.000).")
    parser.add_argument("--min-subs-ranking", type=int, default=100, help="Inscritos mínimos para o ranking (padrão: 100).")
    parser.add_argument("--limit", type=int, default=0, help="Limita vídeos por nicho; útil para teste.")
    parser.add_argument("--sleep", type=float, default=0.5, help="Pausa entre chamadas ao yt-dlp (padrão: 0.5s).")
    parser.add_argument("--timeout", type=int, default=90, help="Timeout por chamada em segundos (padrão: 90).")
    parser.add_argument("--refresh", action="store_true", help="Ignora o cache de metadados.")
    parser.add_argument("--yt-dlp", default=None, help="Caminho do yt-dlp (padrão: .venv/Scripts/yt-dlp.exe).")
    parser.add_argument("--cache-dir", default="logs/nicho-cache", help="Diretório de cache.")
    parser.add_argument("--out", default=None, help="JSON de saída (padrão: logs/nicho-YYYY-MM-DD.json).")
    parser.add_argument("--md", default="docs/NICHO.md", help="Markdown de saída (padrão: docs/NICHO.md).")
    parser.add_argument("--queries-misterio", nargs="+", default=MISTERIO_QUERIES)
    parser.add_argument("--queries-psicologia", nargs="+", default=PSICOLOGIA_QUERIES)
    parser.add_argument("--own-channel-id", default=OWN_CHANNEL_ID)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    today = date.today().isoformat()

    yt_path = Path(args.yt_dlp) if args.yt_dlp else DEFAULT_YTDLP
    if not yt_path.exists():
        found = shutil.which("yt-dlp")
        if not found:
            eprint(f"yt-dlp não encontrado em {yt_path} nem no PATH.")
            return 2
        yt_path = Path(found)

    out_path = resolve_path(args.out, ROOT / "logs" / f"nicho-{today}.json")
    md_path = resolve_path(args.md, ROOT / "docs" / "NICHO.md")
    cache_dir = resolve_path(args.cache_dir, ROOT / "logs" / "nicho-cache")

    yt = YtDlp(yt_path, timeout=args.timeout, sleep=args.sleep)
    eprint(f"yt-dlp: {yt_path}")
    eprint(f"Saída: {out_path}")
    eprint(f"Markdown: {md_path}")

    niches = {
        "misterio": args.queries_misterio,
        "psicologia": args.queries_psicologia,
    }
    data: dict[str, Any] = {
        "generated_at": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        "method": "yt-dlp metadata only; channel /shorts crawl; no video download",
        "config": {
            "per_niche": args.per_niche,
            "search_results": args.search_results,
            "max_channels": args.max_channels,
            "max_per_channel": args.max_per_channel,
            "min_duration": args.min_duration,
            "max_duration": args.max_duration,
            "min_subs": args.min_subs,
            "max_subs": args.max_subs,
            "min_subs_ranking": args.min_subs_ranking,
            "queries": niches,
        },
        "own_channel_id": args.own_channel_id,
        "niches": {},
    }

    for niche, queries in niches.items():
        data["niches"][niche] = collect_niche(yt, niche, queries, args, cache_dir)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    eprint(f"\nJSON salvo: {out_path}")

    report = render_report(data)
    if args.md:
        write_markdown(md_path, report)
        eprint(f"Markdown atualizado: {md_path}")

    for niche, block in data["niches"].items():
        summary = block["summary"]
        eprint(
            f"[{block['label']}] {summary['n']} shorts, "
            f"mediana views/inscrito={summary['median_views_per_sub']}, "
            f"mediana views={summary['median_views']}"
        )

    eprint(f"Chamadas ao yt-dlp: {yt.calls}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

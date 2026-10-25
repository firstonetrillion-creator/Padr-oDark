# Status — 005

> Criado por `scripts/novo-episodio.ps1` em 2026-10-25 20:02 a partir de `templates/misterio-45`
> (sha256 `0e0a2281`, commit `c0516b8`). Atualizar a cada etapa concluida.

| Etapa | Estado | Artefato |
|---|---|---|
| Briefing | **pronto** | `briefing.md` (Board of Investigation 1945, achados 1–56; NHHC; NASFL; USNI) |
| Gancho | **pronto — aguardando aprovação** | `gancho.md` (“Cinco aviões pediram socorro. Nenhum voltou. Nem o resgate.”) |
| Roteiro | pendente | `roteiro.md` |
| Narracao | pendente | `narracao.txt`, `voz_raw.wav`, `voz.wav` (45,00 s) |
| Transcricao | pendente | `transcricao.json` |
| Assets | nao usado | v1 tipografica (sem imagens) |
| Composicao | pendente | `index.html` (13 cenas) |
| QA visual | pendente | `qa-frames/` |
| Render | pendente | `final.mp4` |
| QA | pendente | `qa.md` |
| Publicacao | pendente | YouTube Shorts |

## Medicoes

- Voz crua: —
- Voz final: —
- Contrato (`check-contrato.ps1`): —
- Render (standard): —
- Loudness: — LUFS cru -> — LUFS final

## Proximos passos

1. `briefing.md` (skill briefing) e `gancho.md` (skill gancho).
2. `roteiro.md` com 110–125 palavras.
3. TTS + processamento para 45,00 s.
4. Transcrever e remapear `data-start`/`data-duration`.
5. `.\scripts\check-contrato.ps1 episodios\005-voo-19\index.html` -> contrato OK.
6. QA visual por `?t=` e render (um por vez).
# Status — 003

> Criado por `scripts/novo-episodio.ps1` em 2026-10-21 22:33 a partir de `templates/misterio-45`
> (sha256 `0e0a2281`, commit `ac25c1e`). Atualizar a cada etapa concluida.

| Etapa | Estado | Artefato |
|---|---|---|
| Briefing | pronto | `briefing.md` (fontes NPS + Quinn) |
| Gancho | pronto | `gancho.md` (fórmula 1 — O Dado) |
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

1. **Briefing e gancho concluídos.** Revisar o gancho depois do gate de retenção de 23/10.
2. `roteiro.md` com 110–125 palavras, mantendo o fato central e a correção da lenda.
3. TTS + processamento para 45,00 s.
4. Transcrever e remapear `data-start`/`data-duration`.
5. `.\scripts\check-contrato.ps1 episodios\003-roanoke\index.html` -> contrato OK.
6. QA visual por `?t=` e render (um por vez).
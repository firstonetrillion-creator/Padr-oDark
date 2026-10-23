# Status — 003

> Criado por `scripts/novo-episodio.ps1` em 2026-10-21 22:33 a partir de `templates/misterio-45`
> (sha256 `0e0a2281`, commit `ac25c1e`). Atualizado em 23/10/2026: gancho revisado e roteiro v1.

| Etapa | Estado | Artefato |
|---|---|---|
| Briefing | pronto | `briefing.md` (fontes NPS + Quinn) |
| Gancho | pronto | `gancho.md` (fórmula 1 — O Dado; revisão de 23/10) |
| Roteiro | pronto | `roteiro.md` (113 palavras, 13 cenas) |
| Narracao | texto pronto; áudio pendente | `narracao.txt`; faltam `voz_raw.wav`, `voz.wav` (45,00 s) |
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

1. **Gancho, roteiro e texto de narração concluídos.** O gancho revisado foi aprovado em 23/10/2026.
2. Revisar o roteiro e o `narracao.txt`; se aprovado, gerar TTS com `length_scale` a calibrar para 45,00 s.
3. Processar `voz_raw.wav` em `voz.wav` e transcrever para `transcricao.json`.
4. Remapear `data-start`/`data-duration` no `index.html` (ainda contém o texto-exemplo do 001).
5. `.\scripts\check-contrato.ps1 episodios\003-roanoke\index.html` -> contrato OK.
6. QA visual por `?t=` e render (um por vez).
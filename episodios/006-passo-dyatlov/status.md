# Status - 006

> Criado por `scripts/novo-episodio.ps1` em 2026-10-26 22:03 a partir de `templates/misterio-45`
> (sha256 `0e0a2281`, commit `ae1040f`). Atualizar a cada etapa concluida.

| Etapa | Estado | Artefato |
|---|---|---|
| Briefing | **concluido** | `briefing.md` (Gaume & Puzrin 2021; processo 2-236; ICRF; PGR 2020) |
| Gancho | **concluido** | `gancho.md` — "Eles cortaram a encosta para dormir. A neve esperou nove horas." |
| Roteiro | **concluido** | `roteiro.md` + `roteiro.json` (114 palavras, 14 cenas, max 4,17 s) |
| Narracao | **concluida** | `narracao.txt`, `narracao_tts.txt`, `voz_raw.wav` 45,000 s, `voz.wav` 45,000 s |
| Transcricao | **nao usada** | voz sintetizada cena por cena: `tempos_cenas.json` vem do `montar-voz.py` |
| Assets | nao usado | v1 tipografica (sem imagens) |
| Composicao | **concluida** | `index.html` gerado do `roteiro.json`; 14 cenas; contrato **OK, 1 aviso** |
| QA visual | **concluido** | 14 frames; pior tinta **806 px** de 840; 6 cenas com fonte corrigida antes do render |
| Render | **concluido** | `final_raw.mp4` 45,000 s, 1350 frames, 5 segmentos, 0 retries, 3m09,9s |
| QA | **QA PASS** | `qa.md` escrito |
| Publicacao | **pronta, aguardando aprovacao** | `publicacao.md` (titulo 48 chars, lint 98/100), `capa.png` em 32,6 s, `006-passo-dyatlov_shorts_v1.mp4` |

## Medicoes

- Voz crua: **45,000 s** (40,814 s de fala + 4,186 s de silencio, 9,3%)
- Voz final: **−22,15 LUFS**, TP **−8,12**, LRA 2,70
- Contrato (`check-contrato.ps1`): **OK, 1 aviso** (14 cenas em vez de 13)
- Tinta: pior linha **806 px** (s4); s1 medida no mp4 (680 px)
- Render (standard): 1350 frames, 5 segmentos, 0 retries, **3m09,9s**
- Loudness: −22,17 LUFS cru -> **−15,19 LUFS** final (ganho **+7,0 dB**), TP −1,30
- Arquivo: **45,013 s · 3.859.117 bytes** · SHA-256 `B2AA85F3A308E155FAA953BF395BF1CC2E03A3FB66F3DC64CD1D9119F10033A6`

## Proximos passos

1. **Aprovacao humana** do video (gate da Fase 1) + escuta de "Dyatlov", "Kholat Saykhl", "Thibeaux-Brignolles".
2. Upload no YouTube Shorts pelo usuario; marcar **AI use = Yes**.
3. Conferir a vitrine publica sem cookies (`yt-dlp`: `public`, `age_limit=0`, `duration=45`).
4. Registrar em `biblioteca/publicados.csv` e medir a retencao de 48 h.

# Status — 007

> Criado por `scripts/novo-episodio.ps1` em 2026-10-29 17:45 a partir de `templates/misterio-45`
> (sha256 `0e0a2281`, commit `4104419`). Atualizar a cada etapa concluida.

| Etapa | Estado | Artefato |
|---|---|---|
| Briefing | **concluido** | `briefing.md` (Homem de Somerton 1948; fontes Wikipédia PT, Guardian 27/07/2022 e 31/07/2022, ABC 01/12/2018) |
| Gancho | **concluido** | `gancho.md` — "Um homem morto na praia. Um código costurado na roupa." |
| Roteiro | **concluido** | `roteiro.json` (108 palavras, 12 cenas, max 5,029 s — cena 3, 29 ms acima do teto) |
| Narracao | **concluida** | `narracao.txt`, `narracao_tts.txt`, `voz_raw.wav` 35,768 s de fala + 9,232 s de silêncio, `voz.wav` 45,000 s (+5 dB, limiter 0,85, pré-render) |
| Transcricao | nao usado | tempo exato por construção (`montar-voz.py`), sem ASR |
| Assets | nao usado | v1 tipografica (sem imagens) |
| Composicao | **concluida** | `index.html` gerado do `roteiro.json` + `tempos_cenas.json`; 12 cenas; contrato **OK, 1 aviso** (re-rodado em 31/10) |
| QA visual | **concluido** | 7 frames re-extraidos do `final.mp4` (`qa-final/qa-frame-01..07.png`); sem overflow; pior tinta 800 px (s9) |
| Render | **concluido** | `final_raw.mp4` 45,000 s (29/10 17:58); `final.mp4` reprocessado em 31/10 |
| QA | **QA PASS** | `qa.md` — 45,013 s, −15,0 LUFS, TP −5,9, LRA 3,2 |
| Capa | **pronta** | `capa.png` em 17,7 s ("O PAPEL DIZIA: ACABADO. / PERSIA, TAMÁM SHUD.") |
| Publicacao | **pronta, aguardando aprovacao** | `publicacao.md`; titulo "Somerton: o homem sem nome por 74 anos" (38 chars, lint 100/100) |
| Aprovacao humana | **pendente** | "conclua" nao autoriza publicar |
| Retencao 48 h | pendente | D+2 da data de publicacao |

## Medicoes

- Voz crua: `voz_raw.wav` 45,000 s (cena por cena)
- Voz final: `voz.wav` 45,000 s, +5 dB, limiter 0,85
- Contrato (`check-contrato.ps1`): **OK, 1 aviso** (31/10)
- Render (standard): `final_raw.mp4` 45,000 s, **−10,6 LUFS** (voz pré-normalizada)
- Loudness: −10,6 LUFS cru → **−15,0 LUFS** final (`volume=-4.4dB` + limitador 0,85)
- SHA-256 (`final.mp4`): `DE13EECD7C89DB3B2F5BB233CBA6F16C6F916E4B123AD4FE7DE2A4F01F462B6B`

## Proximos passos

1. **Escuta humana** dos nomes (Somerton, Adelaide, Tamám Shud, Omar Caiame,
   Glenelg) — transliterações no `briefing.md`.
2. **Aprovação humana explícita** para publicar (31/10 é sábado; próxima janela
   da cadência seg–sex: segunda 02/11 às 19h).
3. Publicar no YouTube Shorts (conta Dossiê 45), marcar **AI use = Yes**,
   conferir `duration=45`/`age_limit=0` por `yt-dlp`.
4. Registrar em `biblioteca/publicados.csv`; retenção 48 h em D+2.

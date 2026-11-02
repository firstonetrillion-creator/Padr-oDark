# Status — 008

> Criado por `scripts/novo-episodio.ps1` em 2026-11-01 22:22 a partir de `templates/misterio-45`
> (sha256 `0e0a2281`, commit `c471653`). Atualizar a cada etapa concluida.

| Etapa | Estado | Artefato |
|---|---|---|
| Briefing | **concluido** | `briefing.md` (3 fontes numeradas) |
| Gancho | **concluido** | `gancho.md` (formula 17) |
| Roteiro | **concluido** | `roteiro.json` (12 cenas, 106 palavras) |
| Narracao | **concluido** | `narracao.txt`, `narracao_tts.txt`, `voz_raw.wav`, `voz.wav` (45,000 s) |
| Transcricao | **nao usada** | tempos exatos de `montar-voz.py` (`tempos_cenas.json`) |
| Assets | nao usado | v1 tipografica + 2 layouts (`digital-zoom`, `orbit`) |
| Composicao | **concluido** | `index.html` (12 cenas) |
| QA visual | **concluido** | `qa-medida/` (12 snapshots), `qa-frames/` (12 frames + cena 1) |
| Render | **concluido** | `final_raw.mp4` -> `final.mp4` (1350 frames, 5 segmentos) |
| QA | **QA PASS** | `qa.md`, `capa.png`, `publicacao.md` |
| Publicacao | **aguardando aprovacao humana** | YouTube Shorts |

## Medicoes

- Voz crua: **−15,7 LUFS**, TP **+0,1** (Piper saiu quente)
- Voz final: **−22,0 LUFS**, TP −6,2 (`volume=-6.3dB,alimiter=limit=0.85`)
- Contrato (`check-contrato.ps1`): **OK, 1 aviso** (12 cenas, padrao 13)
- Render (standard): 3m30,0s, 1350 frames, 5 segmentos, 0 retries
- Loudness: **−19,1** LUFS cru -> **−15,0** LUFS final (ganho +4,1 dB)
- Pico final: true peak **−2,1 dBFS** · LRA 2,4 LU
- SHA-256 `final.mp4`: `70CB5963590E04DD133FD4FAB59212592311074893E7FBC3DB69CA0162F704A7`

## Proximos passos

1. **Escuta humana** dos nomes (Maks Redrum, Chicago, dabliu-ge-ene,
   dabliu-te-te-dabliu, Doktor U, efe-ce-ce, efe-be-i).
2. **Aprovacao humana explicita** do video.
3. Publicar em conta do Dossie 45 (selo **AI**), respeitando 1/dia, 19h.
4. Medir retencao em 48 h e registrar em `biblioteca/publicados.csv`.

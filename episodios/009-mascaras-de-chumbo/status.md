# Status — 009

> Criado por `scripts/novo-episodio.ps1` em 2026-11-02 a partir de `templates/misterio-45`
> (sha256 `0e0a2281`, commit `e50d7e6`). Atualizar a cada etapa concluida.

| Etapa | Estado | Artefato |
|---|---|---|
| Briefing | **concluido** | `briefing.md` (9 fontes numeradas) |
| Gancho | **concluido** | `gancho.md` (formula 17 + 14) |
| Roteiro | **concluido** | `roteiro.json` (12 cenas, 109 palavras) |
| Narracao | **concluido** | `narracao.txt`, `narracao_tts.txt`, `voz_raw.wav`, `voz.wav` (45,000 s) |
| Transcricao | **nao usada** | tempos exatos de `montar-voz.py` (`tempos_cenas.json`) |
| Assets | nao usado | v1 tipografica + 2 layouts (`digital-zoom`, `checklist`) |
| Composicao | **concluido** | `index.html` (12 cenas) |
| QA visual | **concluido** | `qa-medida/` (11 snapshots), `qa-frames/` (12 frames) |
| Render | **concluido** | `final_raw.mp4` -> `final.mp4` (1350 frames, 5 segmentos) |
| QA | **QA PASS** | `qa.md`, `capa.png`, `publicacao.md` |
| Publicacao | **aguardando aprovacao humana** | YouTube Shorts |

## Medicoes

- Voz crua: **−16,1 LUFS**, TP **+0,1** (Piper quente, como no 008)
- Voz final: **−22,0 LUFS**, TP −5,8 (`volume=-5.9dB,alimiter=limit=0.85`)
- Fala: **34,958 s** + silencio **10,042 s** (22,3%)
- Cena mais longa: **4,64 s** (s2); mais curta: **3,05 s** (s8)
- Contrato (`check-contrato.ps1`): **OK, 1 aviso** (12 cenas, padrao 13)
- Medida de tinta: pior **800 px** (s6 e s8); s1 so no frame do mp4 (ESTOURA de camera)
- Render (standard): **3m32,0s**, 1350 frames, 5 segmentos, 0 retries
- Loudness: **−19,1** LUFS cru -> **−14,9** LUFS final (ganho +4,1 dB)
- Pico final: true peak **−1,7 dBFS** · LRA 3,9 LU
- Duracao: **45,013 s** · **3.834.702 bytes**
- SHA-256 `final.mp4`: `3E0A2ACEEEEE0A09E51049F00B634B059607CB9341A462FA79C4B04E1BD173AC`

## Proximos passos

1. **Escuta humana** dos nomes (Cãpos dos Goitacazes, Niterói, Vintém, Manoel
   Pereira da Cruz, Miguel José Viana, Idovan Ferreira, Élcio Correia Gomes,
   Gracinda Barbosa Coutinho de Souza).
2. **Aprovacao humana explicita** do video.
3. Publicar depois do 007 (02/11) e do 008 (03/11), 1/dia, 19h.
4. Medir retencao em 48 h e registrar em `biblioteca/publicados.csv`.

# Status — 002

> Criado por `scripts/novo-episodio.ps1` em 2026-10-21 16:48 a partir de `templates/misterio-45`
> (sha256 `0e0a2281`, commit `ad2747d`). Atualizado ao fim da produção.

| Etapa | Estado | Artefato |
|---|---|---|
| Briefing | pronto | `briefing.md` |
| Gancho | pronto | `gancho.md` (fórmula 17 — A Alegação Impossível) |
| Roteiro | pronto | `roteiro.md` (110 palavras de tela / 121 faladas) |
| Shotlist | pronto | `shotlist.md` (13 cenas) |
| Narração | pronto | `narracao.txt`, `voz_raw.wav` (43,04 s), `voz.wav` (45,00 s) |
| Transcrição | pronto | `transcricao.json` (timestamps por palavra) |
| Assets | não usado | v1 tipográfica (sem imagens) |
| Composição | pronto | `index.html` (13 cenas sincronizadas) |
| QA visual | pronto | `qa-frames/` (frame 1, 13 cenas, fade e bordas) |
| Render | pronto | `final.mp4`, `final_raw.mp4`, `002-mary-celeste_shorts_v1.mp4` |
| QA | **PASS** | `qa.md` (técnico + aprovação humana em 21/10/2026) |
| Publicação | **publicado** | YouTube Shorts, 21/10/2026 — https://youtube.com/shorts/n6dtveQguf4 |

## Medições

- Voz crua (`length_scale` 1,12): **43,04 s**
- Voz final: **45,00 s** (0,6 s de respiro + pad)
- Contrato (`check-contrato.ps1`): **OK, 0 avisos** (29 invariantes)
- Render (standard): **3m00,9s**, 5 segmentos, 0 retries, 4 reciclagens de browser
- `final_raw.mp4`: 45,0 s, 3,4 MB
- Loudness: **−21,5 LUFS** cru → **−15,4 LUFS** final (+6,2 dB, limitador 0,85)
- Pico final: **−1,5 dBFS**
- `final.mp4`: **45,013 s**, **3,6 MB**, 1080×1920, H.264, 30 fps, AAC 48 kHz estéreo
- Título: 52 caracteres; lint **98/100**

## Publicação

- **YouTube Shorts:** https://youtube.com/shorts/n6dtveQguf4
- **Data:** 21/10/2026
- **Visibilidade:** Público
- **Aviso de conteúdo sintético:** marcado no Studio; selo **AI** visível na página
- **Métricas:** medir em **23/10/2026** (48 h)

## Próximos passos

1. Em 23/10/2026, baixar o CSV de retenção do 002 no Studio e rodar `retention.py --duration 45`.
2. Coletar views, retenção em 3 s/10 s, retenção média, conclusão, salvos e compartilhados.
3. Preencher `biblioteca/publicados.csv` e criar `retencao.md` do 002.
4. Comparar com o 001 e decidir manter, ajustar ou matar o formato.

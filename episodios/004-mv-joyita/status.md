# Status — 004

> Criado por `scripts/novo-episodio.ps1` em 2026-10-23 16:01 a partir de `templates/misterio-45`
> (sha256 `0e0a2281`, commit `a11581f`). Atualizar a cada etapa concluida.

| Etapa | Estado | Artefato |
|---|---|---|
| Briefing | **pronto** | `briefing.md` (Comissão NZ 1956, Apia; Wright) |
| Gancho | **pronto** | `gancho.md` (“O barco foi achado vazio. E ainda flutuava.”) |
| Roteiro | **pronto** | `roteiro.md` (131 palavras, 13 cenas, tempos reais) |
| Narracao | **pronto** | `narracao.txt`, `voz_raw.wav` (44,117 s), `voz.wav` (45,000 s) |
| Transcricao | **pronto** | `transcricao.json` (timestamps por palavra) |
| Assets | nao usado | v1 tipografica (sem imagens) |
| Composicao | **pronta** | `index.html` (13 cenas; cena 6 com 4 linhas explicitas) |
| QA visual | **concluido** | `qa-frames/` (14 frames) + `qa-final/` (14 frames do render) |
| Render | **concluido** | `final_raw.mp4` 45,000 s, −21,64 LUFS |
| QA | **PASS** | `qa.md` (`final.mp4` 45,013 s, −15,16 LUFS, TP −1,42) |
| Publicacao | **publicado** em 24/10/2026 | https://youtube.com/shorts/rlSArCY3bH0 |

## Medicoes

- Voz crua: **44,117914 s** (`length_scale` 0,90; `noise_scale` 0,65; `noise_w` 0,80)
- Voz final: **45,000 s**, **−21,63 LUFS**, TP **−7,37 dBFS**
- Contrato (`check-contrato.ps1`): **OK, 0 avisos**
- Render (standard): **45,000 s**, 3.654.546 bytes, 5 segmentos, 0 retries, 3m16s
- Loudness: −21,64 LUFS cru -> **−15,16 LUFS** final (ganho +6,5 dB; TP −1,42 dBFS)
- `final.mp4`: **45,013 s**, 3.652.954 bytes, SHA-256 `406906CE…`

## Publicado

- URL: https://youtube.com/shorts/rlSArCY3bH0
- Público, **AI use = Yes**, não é para crianças, sem promoção paga.
- Cópia de upload `004-mv-joyita_shorts_v1.mp4` (SHA-256 `406906CE…`).
- Retenção de 48 h: medir em **26/10/2026**.

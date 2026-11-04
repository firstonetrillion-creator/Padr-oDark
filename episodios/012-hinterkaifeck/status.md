# Status — 012-hinterkaifeck

> Criado por `scripts/novo-episodio.ps1` em 2026-11-04 12:40 a partir de
> `templates/misterio-45` (sha256 `0e0a2281`, commit `85fea05`).
> **Produzido em 04/11/2026.**

| Etapa | Estado | Artefato |
|---|---|---|
| Briefing | **pronto** — 10 fontes numeradas | `briefing.md` |
| Gancho | **pronto** — aprovado no lote | `gancho.md` |
| Roteiro | **pronto** — 108 palavras, 12 cenas | `roteiro.json` |
| Narração | **pronta** — 35,958 s de fala + 9,042 s de silêncio | `narracao_tts.txt`, `voz_raw.wav`, `voz.wav` |
| Transcrição | **não usada** — tempos exatos por construção | `tempos_cenas.json` |
| Assets | **não usado** — v1 tipográfica (sem imagens) | — |
| Composição | **pronta** — 12 cenas, 2 layouts | `index.html` |
| QA visual | **concluído** — 11 snapshots + 12 frames do mp4 + 2 do gancho | `qa-frames/`, `contact-1.png`, `contact-2.png` |
| Render | **concluído** — 3m11,8s, 5 segmentos, 0 retries | `final_raw.mp4`, `final.mp4` |
| QA | **QA PASS** | `qa.md` |
| Publicação | **pronta, aguardando aprovação** | `publicacao.md`, `capa.png` |

## Medições

- Voz crua: **−16,4 LUFS**, TP **+0,1**
- Voz normalizada: **−22,0 LUFS**, TP −5,5 (`volume=-5.6dB` + limitador 0,85)
- Contrato (`check-contrato.ps1`): **OK, 1 aviso** (12 cenas)
- Render (standard): **3m11,8s**, 1350 frames, 5 segmentos, 0 retries
- Loudness: **−19,1 LUFS** cru → **−15,0 LUFS** final (+4,1 dB), TP −1,4, LRA 4,0
- Tinta: pior linha **810 px** de 840 (s5); nenhuma quebra de título
- SHA-256: `6B3E3F5458D3DAC1D1AA4F6CCB8ECDB1599A9C5BB6F656053AB55AA3E16F28C6`

## Decisões

- 2 layouts: `digital-zoom` no gancho (igual ao 008 ao 011, variável controlada) e
  `checklist` na cena 4 — o cartão lista as quatro coisas que Andreas viu antes da
  noite.
- Capa na cena 3 (`PEGADAS NA NEVE. / NENHUMA DE VOLTA.`) para não repetir o
  gancho nem o ano do título.
- **Sem idades no vídeo** — as fontes divergem (Andreas 63/64, Maria 44/45).
- **Sem graphicidade:** o detalhe da autópsia da menina ficou só no `briefing.md`.
- **Falas enxugadas** antes do render: o primeiro take deu 40,0 s de fala
  (silêncio de 11,1%) e a cena 11 em 6,278 s, por causa dos dois anos soletrados.
- **Item do `checklist` trocado**: "pegadas só de ida" repetia a cena 3; entrou
  "A VACA SOLTA NO ESTÁBULO".

## Próximos passos

1. Escuta humana dos nomes e **aprovação explícita**.
2. Publicação manual (cadência de 3–4/dia) e registro em
   `biblioteca/publicados.csv`.
3. Retenção de 48 h — **D+2 da data de publicação**.

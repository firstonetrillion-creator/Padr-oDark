# Status — 011-ss-baychimo

> Criado por `scripts/novo-episodio.ps1` em 2026-11-02 18:00 a partir de
> `templates/misterio-45` (sha256 `0e0a2281`, commit `b302b00`).
> **Produzido em 03/11/2026.**

| Etapa | Estado | Artefato |
|---|---|---|
| Briefing | **pronto** — 9 fontes numeradas | `briefing.md` |
| Gancho | **pronto** — aprovado no lote | `gancho.md` |
| Roteiro | **pronto** — 113 palavras, 12 cenas | `roteiro.json` |
| Narração | **pronta** — 36,049 s de fala + 8,951 s de silêncio | `narracao.txt`, `narracao_tts.txt`, `voz_raw.wav`, `voz.wav` |
| Transcrição | **não usada** — tempos exatos por construção | `tempos_cenas.json` |
| Assets | **não usado** — v1 tipográfica (sem imagens) | — |
| Composição | **pronta** — 12 cenas, 2 layouts | `index.html` |
| QA visual | **concluído** — 11 snapshots + 12 frames do mp4 + 3 do gancho | `qa-frames/`, `contact-1.png`, `contact-2.png` |
| Render | **concluído** — 3m15,9s, 5 segmentos, 0 retries | `final_raw.mp4`, `final.mp4` |
| QA | **QA PASS** | `qa.md` |
| Publicação | **pronta, aguardando aprovação** | `publicacao.md`, `capa.png` |

## Medições

- Voz crua: **−15,1 LUFS**, TP **+0,1**
- Voz normalizada: **−22,0 LUFS**, TP −6,8 (`volume=-6.9dB` + limitador 0,85)
- Contrato (`check-contrato.ps1`): **OK, 1 aviso** (12 cenas)
- Render (standard): **3m15,9s**, 1350 frames, 5 segmentos, 0 retries
- Loudness: **−19,1 LUFS** cru → **−15,0 LUFS** final (+4,1 dB), TP −2,7, LRA 3,8
- Tinta: pior linha **807 px** de 840 (s3); nenhuma quebra de título
- SHA-256: `4C71CB5817C14CAABE2EED269471ECD4DC20BF1AEAB0196A68862D81A7B70869`

## Decisões

- 2 layouts: `digital-zoom` no gancho (igual ao 008, 009 e 010, variável
  controlada) e `orbit` na cena 10 (o intervalo de 1931 a 1969).
- **`orbitas` não existe no gerador** — a chave foi removida do `roteiro.json`; o
  layout desenha o anel com quatro pontos, sem rótulo de data.
- Capa na cena 7 (`ESTRANHOS A BORDO. / O PORÃO AINDA TINHA PELES.`) para não
  repetir o gancho nem o número do título.
- **Falas enxugadas** antes do render: o primeiro take deu 42,4 s de fala e a
  cena 10 em 5,748 s. As datas que já estavam nos kickers saíram da fala.
- **Rodapé corrigido**: saiu o NPS (fonte do 010) e entrou
  `FONTE · WIKIPÉDIA · DALTON & DELGADO, 2006`.

## Próximos passos

1. Escuta humana dos nomes e **aprovação explícita**.
2. Publicação manual (cadência de 3–4/dia) e registro em
   `biblioteca/publicados.csv`.
3. Retenção de 48 h — **D+2 da data de publicação**.

# Status — 010-carroll-a-deering

> Criado por `scripts/novo-episodio.ps1` em 2026-11-02 17:50 a partir de
> `templates/misterio-45` (sha256 `0e0a2281`, commit `b302b00`).
> **Produzido em 03/11/2026.**

| Etapa | Estado | Artefato |
|---|---|---|
| Briefing | **pronto** — 12 fontes numeradas | `briefing.md` |
| Gancho | **pronto** — aprovado no lote | `gancho.md` |
| Roteiro | **pronto** — 113 palavras, 12 cenas | `roteiro.json` |
| Narração | **pronta** — 36,188 s de fala + 8,812 s de silêncio | `narracao.txt`, `narracao_tts.txt`, `voz_raw.wav`, `voz.wav` |
| Transcrição | **não usada** — tempos exatos por construção | `tempos_cenas.json` |
| Assets | **não usado** — v1 tipográfica (sem imagens) | — |
| Composição | **pronta** — 12 cenas, 2 layouts | `index.html` |
| QA visual | **concluído** — 11 snapshots + 12 frames do mp4 + 3 do gancho | `qa-frames/`, `contact-1.png`, `contact-2.png` |
| Render | **concluído** — 3m56,5s, 5 segmentos, 0 retries | `final_raw.mp4`, `final.mp4` |
| QA | **QA PASS** | `qa.md` |
| Publicação | **pronta, aguardando aprovação** | `publicacao.md`, `capa.png` |

## Medições

- Voz crua: **−16,3 LUFS**, TP **+0,2**
- Voz normalizada: **−22,0 LUFS**, TP −5,5 (`volume=-5.7dB` + limitador 0,85)
- Contrato (`check-contrato.ps1`): **OK, 1 aviso** (12 cenas)
- Render (standard): **3m56,5s**, 1350 frames, 5 segmentos, 0 retries
- Loudness: **−19,1 LUFS** cru → **−15,0 LUFS** final (+4,1 dB), TP −1,4, LRA 3,6
- Tinta: pior linha **805 px** de 840 (s3); nenhuma quebra de título
- SHA-256: `33FC547F185995B414EA804D78D265EE54E509F4EBD5CF00205B67FC360A225D`

## Decisões

- 2 layouts: `digital-zoom` no gancho (igual ao 008 e ao 009, variável
  controlada) e `checklist` na cena 4 (o que faltava a bordo).
- O **Triângulo das Bermudas não entra em cartão**: a ligação é posterior
  (1931–1974) e o naufrágio foi em Cape Hatteras. Fica marcado no `briefing.md` e
  na descrição.
- Capa na cena 3 (`ONZE HOMENS. NENHUM CORPO.`) para não repetir o gancho nem o
  título.

## Próximos passos

1. Escuta humana dos nomes e **aprovação explícita**.
2. Publicação manual (cadência de 3–4/dia) e registro em
   `biblioteca/publicados.csv`.
3. Retenção de 48 h — **D+2 da data de publicação**.

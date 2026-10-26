# QA — 005-voo-19

**Data:** 2026-10-26
**Arquivo:** `final.mp4`
**Render:** standard, 1080×1920, 30 fps, segmentado 5×300 frames, 1 worker,
low-memory; 1350/1350 frames, 0 retries, 4 reciclagens de browser (3m11s)
**Duração:** 45,013 s · **Tamanho:** 3.344.787 bytes (3,34 MB)
**Voz:** Piper `pt_BR-faber-medium`, `length_scale` 1,15; cru 43,839 s → 45,000 s
(−16,17 LUFS na voz isolada, TP −3,18)
**SHA-256 (`final.mp4`):** `69696A09F4A9A41DF0C0D19103ABE4B3602EC1DB18A9F3753535F1F8F7C4DBBF`

## Técnico

| Item | Medição | Status |
|---|---|---|
| Codec de vídeo | H.264, 1080×1920 | OK |
| FPS | 30/1 constante | OK |
| Áudio | AAC 48 kHz, estéreo | OK |
| Loudness | −15,16 LUFS (cru: −16,19; ganho **+1,05 dB**) | OK |
| Pico | true peak −2,18 dBFS; limitador em 0,85 não chegou a atuar | OK |
| LRA | 2,20 LU | OK |
| Preto inesperado | nenhum; fade final em 44,3–45,0 s | OK |
| Texto cortado | 12 cenas conferidas em frame; nenhuma acima de 4 linhas | OK |
| Linha mais larga | **772 px de 840** (cena 1, "PEDIRAM SOCORRO.") | OK |
| Sincronia | 12 cenas de `tempos_cenas.json` (remapear.py, 107/113 tokens) | OK |
| Fantasma de cena | `autoAlpha` por cena; 14 frames conferidos | OK |
| Contrato | `check-contrato.ps1` — **OK, 1 aviso** (12 cenas, padrão é 13) | OK |
| QA automático | `qa.ps1` | **PASS** |
| Marca | `DOSSIÊ 45` / dossiê `005` | OK |

## Editorial

- [x] Gancho visual em 0,0 s; texto do gancho no frame 1; voz entra em 0,0 s
- [x] Uma ideia por vídeo: cinco aviões que pediram socorro e o resgate que sumiu
- [x] Fatos com fonte: Board of Investigation (NAS Jacksonville, 7/12/1945,
  achados 1–56); NHHC; NASFL Museum; USNI *Naval History* (out/2021)
- [x] **27 mortos** = 14 do Voo 19 + 13 do PBM; o vídeo não afirma o que houve
  com eles — nenhum corpo e nenhum destroço foram encontrados
- [x] "Está nas Bahamas" é reconstrução do inquérito, não testemunho
- [x] "10 galões" é paráfrase da última transmissão registrada
- [x] Nenhuma menção ao Triângulo das Bermudas como causa
- [x] Sem graphicidade gratuita; sem CTA comercial
- [x] ASR ouviu "50 metros" e "petoleiro"; **escuta humana pendente** para
  "Avengers", "Keys", "Bahamas" e "amarar"

## Identidade

- [x] Paleta, tipografia, moldura, marca `DOSSIÊ 45` e dossiê `005`
- [x] Voz impessoal, sem "eu" ou "nós"
- [x] Drone a 0,16 (mesmo arquivo do 004, −51,34 LUFS — inaudível, igual a 001–004)
- [x] Capa `capa.png` — frame em 38,6 s, 1080×1920, "27 HOMENS / NENHUM CORPO."

## Ritmo (o que mudou em relação ao 004)

| Medida | 004 | 005 |
|---|---:|---:|
| Palavras faladas | 131 | **111** |
| Palavras por segundo | 2,9 | **2,5** |
| Cenas | 13 | 12 |
| Cena mais longa | **6,57 s** | **5,00 s** |
| Cena 2 | cartão de contexto estático | sobe a aposta (o rádio funcionava) |

Nenhuma cena passa de 5,0 s e a cena 2 deixou de ser cartão de contexto — as duas
correções que a retenção do 004 pedia. O miolo continua com movimento apenas de
entrada de texto (mesmo v1 congelado de 001–004); animação contínua é variável
do A/B do 007.

## Armadilha registrada

`hyperframes snapshot` **sai vazio na cena 1** (testado em 0,6 s, 2,0 s e 3,9 s;
acontece igual no 004). O gancho só se confere em frame do `final_raw.mp4`. Em
compensação, o `snapshot` serve para as cenas 2–12 e poupa um render inteiro.

# QA — 006-passo-dyatlov

**Data:** 2026-10-26
**Arquivo:** `final.mp4`
**Render:** standard, 1080×1920, 30 fps, segmentado 5×300 frames, 1 worker,
low-memory; 1350/1350 frames, 0 retries, 4 reciclagens de browser (3m09,9s)
**Duração:** 45,013 s · **Tamanho:** 3.859.117 bytes (3,86 MB)
**Voz:** Piper `pt_BR-faber-medium`, `length_scale` 1,10, sintetizada **cena por
cena** (`montar-voz.py`): 40,814 s de fala + 4,186 s de silêncio (9,3%) já
totalizando 45,000 s; `voz.wav` −22,15 LUFS, TP −8,12, LRA 2,70
**SHA-256 (`final.mp4`):** `B2AA85F3A308E155FAA953BF395BF1CC2E03A3FB66F3DC64CD1D9119F10033A6`

## Técnico

| Item | Medição | Status |
|---|---|---|
| Codec de vídeo | H.264, 1080×1920 | OK |
| FPS | 30/1 constante | OK |
| Áudio | AAC 48 kHz, estéreo | OK |
| Loudness | −15,19 LUFS (cru: −22,17; ganho **+7,0 dB**) | OK |
| Pico | true peak −1,30 dBFS; limitador em 0,85 atuou ~0,2 dB | OK |
| LRA | 2,80 LU | OK |
| Preto inesperado | nenhum; fade final em 44,3–45,0 s | OK |
| Texto cortado | 14 cenas conferidas em frame; nenhuma acima de 5 linhas | OK |
| Linha mais larga | **806 px de 840** (cena 4, "UM DEGRAU") | OK |
| Sincronia | 14 cenas de `tempos_cenas.json` — **exatos por construção**, sem ASR | OK |
| Fantasma de cena | `autoAlpha` por cena; 14 frames conferidos | OK |
| Contrato | `check-contrato.ps1` — **OK, 1 aviso** (14 cenas, padrão é 13) | OK |
| QA automático | `qa.ps1` | **PASS** |
| Marca | `DOSSIÊ 45` / dossiê `006` | OK |

## Editorial

- [x] Gancho visual em 0,0 s; texto do gancho no frame 1; voz entra em 0,6 s
- [x] Uma ideia por vídeo: **a avalanche chegou horas depois do grupo dormir**
- [x] Fatos com fonte: Gaume & Puzrin, *Comm. Earth & Environment* 2:10 (2021),
  DOI `10.1038/s43247-020-00081-8`; processo criminal nº 2-236 (1959); ICRF
  2015–2019; Procuradoria-Geral do Distrito Federal dos Urais (11/07/2020)
- [x] "Nove horas" no gancho = a perícia indica **9,5 a 13,5 h** e o modelo acha
  **7,2 a 13,5 h**; a faixa exata aparece na cena 12 — o número redondo não
  contradiz a fonte
- [x] "A saída soterrada" é reconstrução do ICRF; o laudo de 1959 registra só que
  a barraca foi **cortada por dentro**
- [x] "Três tentam voltar" é inferência de posição (300/480/630 m do cedro); o
  laudo não registra intenção — a tela não afirma o motivo
- [x] "Dois tórax, um crânio" = Dubinina, Zolotaryov, Thibeaux-Brignolles;
  **Kolevatov** morreu de hipotermia, por isso a tela não diz "quatro"
- [x] Lesões: o modelo de 2021 as chama de **graves e não letais**; o laudo de
  1959 as tratou como causa de morte. O vídeo mostra as duas leituras e afirma
  só o **atraso**, que ambos aceitam
- [x] "2020: a Rússia diz avalanche" = anúncio da Procuradoria-Geral, não
  sentença judicial
- [x] **Nada** de yeti, OVNI, esferas laranja, testes militares ou "língua
  arrancada" — a lista de lendas está em `briefing.md` e ficou fora do vídeo
- [x] Sem graphicidade gratuita; sem CTA comercial
- [ ] **Escuta humana pendente** de "Dyatlov", "Kholat Saykhl",
  "Thibeaux-Brignolles" (o ASR não serve de conferência: erra os três)

## Identidade

- [x] Paleta, tipografia, moldura, marca `DOSSIÊ 45` e dossiê `006`
- [x] Voz impessoal, sem "eu" ou "nós"
- [x] Drone a 0,16 (mesmo arquivo do 004/005, −51,34 LUFS — inaudível, igual a
  001–005; som audível é variável do A/B do 007)
- [x] Capa `capa.png` — frame em 32,6 s, 1080×1920: `DOIS TÓRAX AFUNDADOS. / UM
  CRÂNIO RACHADO. / SEM FERIDA NA PELE.`

## Ritmo (o que mudou em relação ao 005)

| Medida | 005 | 006 |
|---|---:|---:|
| Palavras escritas | 111 | **114** |
| Palavras por segundo | 2,5 | **2,5** |
| Cenas | 12 | **14** |
| Cena mais longa | 5,00 s | **4,17 s** |
| Cena 2 | sobe a aposta (o rádio funcionava) | sobe a aposta (barraca cortada por dentro) |
| Tempo das cenas | derivado do ASR | **soma dos blocos** (sem ASR) |

O miolo continua com movimento apenas de entrada de texto (mesmo v1 congelado de
001–004); animação contínua e som audível são variáveis do A/B do 007.

## Método: por que 14 cenas e voz por cena

**14 cenas.** No take único a última cena ficava **6,44 s** no ar — a voz só
termina aos ~44 s e o remap fecha a última cena no fim do vídeo. O veredito virou
dois cartões (1959 · força natural / 2020 · avalanche) e cada um cabe em ~3 s.

**Voz por cena.** O ASR do faster-whisper errou **28% dos tokens** neste áudio
("cortam um degrau" → "Cota o mundo legal"; "cedro" → "cedo"; "Dyatlov" →
"Diato") e o `remapear.py` pôs a cena 4 **1,4 s** fora. Testado também com
`medium`: o erro se repete. A solução foi sintetizar cada parágrafo separado e
concatenar com silêncio calculado (`scripts/montar-voz.py`): o tempo passou a ser
exato por construção. Efeito colateral aceito: a prosódia reinicia a cada cartão,
o que neste formato soa como respiro.

## Armadilha registrada

`hyperframes snapshot` **sai vazio na cena 1** também no 006 (bug conhecido desde
o 004). A cena 1 foi medida no `final.mp4` e sai marcada `(mp4)`; a tabela
reporta `5/4` linhas porque o kicker conta como bloco de texto — conferido no
frame, o título tem as 4 linhas previstas e 680 px de tinta.

O `medir-texto.ps1` também pegou o que a estimativa não pegaria: com `fonte_px`
152 a cena 4 **quebrava "UM DEGRAU" em duas linhas** no frame (a caixa cabia,
a tinta não). Corrigida para 136; seis cenas ao todo desceram de fonte antes do
render.

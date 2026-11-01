# QA — LAB 003 (17 estilos, 45 s)

**Data:** 2026-10-31
**Arquivo:** `final.mp4`
**Render:** standard, 1080×1920, 30 fps, segmentado 5×300 frames, 1 worker,
low-memory; 1352/1352 frames, 0 retries, 3m06,1s
**Duração:** 45,077 s · **Tamanho:** 7.181.696 bytes (7,18 MB)
**Voz:** Piper, 17 blocos — 34,004 s de fala + 10,996 s de silêncio (24,4%);
`voz.wav` 45,000 s, −16,3 LUFS
**SHA-256 (`final.mp4`):** `59D282C210FAA4AD8DECC7BCB416342DC43CE5C1FCFB1A318B6AA67AAA5E9AF7`

## Técnico

| Item | Medição | Status |
|---|---|---|
| Codec de vídeo | H.264, 1080×1920 | OK |
| FPS | 30/1 constante | OK |
| Áudio | AAC 48 kHz, estéreo | OK |
| Loudness | −15,0 LUFS (cru: −14,1; ganho **−0,9 dB**) | OK |
| Pico | true peak −2,5 dBFS | OK |
| LRA | 3,6 LU | OK |
| Preto inesperado | nenhum; fade final no fim | OK |
| Contrato | `check-contrato.ps1 -Duracao 45` — **OK, 2 avisos** (`lab003` fora do padrão `epNNN`; 17 cenas) | OK |
| QA automático | `qa.ps1 -Duracao 45` | **PASS** |
| Layouts declarados | 17 de 17 (`layout-<tipo>` em todas as cenas) | OK |
| Biblioteca inlinada | `window.__layouts` presente no `index.html` | OK |

## Custo

| Medida | Valor |
|---|---|
| Render (segundo) | 3m06,1s — **menor** que o 006 (3m09,9s) e o 005 (3m11s) |
| Render (primeiro, com a órbita fraca) | 4m53,4s — a diferença é a máquina, não o layout |
| Frames | 1352, nenhum perdido |
| Segmentos | 5, 0 retries |

17 cenas animadas custam o mesmo que 12–14 cenas do formato: o que pesa é a
duração (1352 frames), não o número de cenas.

## Tinta no frame (não na caixa)

Medido no PNG extraído do `final.mp4` em 62% de cada cena
(`ffmpeg → gray → bbox por linha`, limiar 120). Frames em `qa-frames/`,
script `frames.py`.

| # | Layout | Largura | x0 | x1 | Linhas | Flag |
|---:|---|---:|---:|---:|---:|---|
| 1 | orbit | 718 | 120 | 838 | 2 + decoro | ok |
| 2 | couch-wall | 776 | 124 | 900 | 2 | ok |
| 3 | ui-world | 656 | 202 | 858 | 3 | ok |
| 4 | frame-break | 772 | **112** | 884 | 2 | ESTOURA (moldura) |
| 5 | digital-zoom | 668 | **86** | 754 | 2 | ESTOURA (câmera) |
| 6 | phone-mockup | 364 | 358 | 722 | 2 | ok |
| 7 | checklist | 734 | 126 | 860 | 2 + 3 itens | ok |
| 8 | headline-wall | 822 | 122 | 944 | 2 + parede | apertado (parede) |
| 9 | zoom-through | 700 | 120 | 820 | 2 | ok |
| 10 | chart-grow | 838 | 120 | **958** | 2 + barras | apertado (barras) |
| 11 | pull-back | 690 | 126 | 816 | 2 | ok |
| 12 | green-screen | 786 | 120 | 906 | 2 | ok |
| 13 | paper-cut | 708 | 124 | 832 | 2 | ok |
| 14 | doodle-boil | 666 | 120 | 786 | 2 + traço | ok |
| 15 | vertigo | 754 | **72** | 826 | 2 | ESTOURA (raios) |
| 16 | cover-story | 780 | 150 | 930 | 2 | ok (capa) |
| 17 | glass-type | 532 | 122 | 654 | 2 | ok |

**Os três `ESTOURA` são decoro, não texto:**

- **4 frame-break:** x0=112 é a moldura (o gesto é o texto atravessá-la). O
  título começa em x=120 e termina em 884.
- **5 digital-zoom:** no pico do zoom o texto sai da coluna de propósito —
  `escala_fonte` 0,86. Termina em x=86 e 754, **sem corte** nas bordas.
- **15 vertigo:** x0=72 são os raios do fundo. O texto está em 120–826.

**Nenhum título quebrou em 3 linhas.** Nove títulos foram reduzidos antes do
render para caber em 2 (o `phone-mockup` a 55% e o `glass-type` a 68% são
reduções de desenho, não correções).

## Cinco correções aplicadas antes do render final

| Cena | Problema no frame | Correção |
|---|---|---|
| 10 chart-grow | barras com **0 px** de altura | `.bar { height: 100% }` (a barra `<b>` estava sem altura de referência) |
| 14 doodle-boil | traço por cima do texto, 900 px de largura | traço atrás (`z-index: 1`), 780 px |
| 12 green-screen / 15 vertigo | silhueta e raios fortes demais | opacidades reduzidas |
| 13 paper-cut | `.edge` criava uma faixa clara sobre o rodapé | `.edge` removido |
| 1 orbit | **decoro quase invisível no mp4** | anel `::before` + orbes mais claros + 2 px de raio |

## As duas armadilhas do laboratório

**1. `hyperframes snapshot` não mostra a cena 1.** A órbita parecia pronta no
snapshot e saiu invisível no primeiro `final.mp4` — só o frame do mp4 mostrou.
Regra que já estava no `ESTADO.md` e que este LAB confirmou: **cena 1 só se
confere em frame do mp4**.

**2. `alimiter=limit=0.85` não garante true peak.** O `voz.wav` tem pico de
amostra −1,41 dBFS (0,85 exato) mas **true peak +0,2 dBFS** — o limitador corta
a amostra, não o inter-sample. No mix o limitador do renderer resolveu (final
TP −2,5). Para o formato: medir **true peak**, não pico de amostra.

## Limitação conhecida

No `headline-wall` a parede de manchetes passa **atrás do kicker** — em
20,26 s o "HEADLINE WALL" fica sobre a palavra "CÓDIGO". É legível (vermelho
claro sobre vermelho escuro) e é consequência do desenho (parede centralizada,
kicker fixo). Se incomodar no episódio, a correção é uma placa escura atrás do
kicker, não mexer na parede.

## Editorial

- [x] Uma cena por estilo, na ordem pedida pelo usuário
- [x] `kicker` = nome do estilo em inglês; narração nomeia o estilo em cada cena
- [x] Nada de imagem de terceiros: todos os decoros são CSS/SVG
- [x] Nenhum fato histórico no laboratório — é prova de motor, não episódio
- [ ] **Aprovação humana dos 17 estilos** — pendente (é o objetivo do LAB)

## O que este arquivo prova

1. O **motor** aceita 17 layouts no mesmo `gerar-episodio.py`, com o contrato
   antigo intacto: sem `tipo`, a saída continua byte-idêntica ao v1 (007
   conferido por SHA-256).
2. O **custo** não muda: 3m06s de render para 45 s, igual a um episódio normal.
3. O **frame** aguenta: nenhum título em 3 linhas, nenhum texto cortado, e os
   três `ESTOURA` são decoro de câmera por desenho.

Nada entra em episódio antes da aprovação. `sombra-direta` e o Dossiê 45
seguem com o v1.

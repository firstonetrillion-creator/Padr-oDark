# QA — 011-ss-baychimo

**Data:** 2026-11-03
**Arquivo:** `final.mp4`
**Render:** standard, 1080×1920, 30 fps, captura segmentada — **1350/1350
frames**, 5 segmentos, 0 retries, **3m15,9s**
**Duração:** 45,013 s · **Tamanho:** 4.008.609 bytes (3,82 MB)
**Voz:** Piper `pt_BR-faber-medium`, **cena por cena** (`montar-voz.py`) —
36,049 s de fala + 8,951 s de silêncio (19,9%) = 45,000 s
**SHA-256 (`final.mp4`):**
`4C71CB5817C14CAABE2EED269471ECD4DC20BF1AEAB0196A68862D81A7B70869`

## Técnico

| Item | Medição | Status |
|---|---|---|
| Codec de vídeo | H.264, 1080×1920 | OK |
| FPS | 30/1 constante | OK |
| Áudio | AAC 48 kHz, estéreo | OK |
| Loudness | **−15,0 LUFS** (cru: −19,1; pós-render **+4,1 dB** + limitador 0,85) | OK |
| Pico | true peak **−2,7 dBFS** | OK |
| LRA | 3,8 LU | OK |
| Preto inesperado | nenhum; fade final em ~44,3–45,0 s | OK |
| Texto cortado | 12 frames do `final.mp4`; nenhuma cena acima de 3 linhas | OK |
| Linha mais larga | **807 px de 840** (s3) na medida; 808 px no frame do mp4 | OK |
| Sincronia | 12 cenas de `tempos_cenas.json` — **exatas por construção**, sem ASR | OK |
| Contrato | `check-contrato.ps1` — **OK, 1 aviso** (12 cenas, padrão é 13) | OK |
| QA automático | `qa.ps1 -Duracao 45` | **PASS** |
| Marca | `DOSSIÊ 45` / dossiê `011` | OK |

## Layouts (2 por episódio, como aprovado em 01/11)

| Cena | Layout | Por quê |
|---|---|---|
| s1 (0,00–5,23) | `digital-zoom` | mesmo tratamento do gancho do 008, 009 e 010 (variável controlada do lote) |
| s10 (32,99–37,29) | `orbit` | o anel de pontos marca o intervalo — 1931 a 1969 — em volta de "38 ANOS DEPOIS" |

As outras 10 cenas são o cartão do v1, sem `tipo`. Contrato §2b passou:
`data-layout`, `window.__layouts` inlinado e `layout-<tipo>` em todas.

**Achado do `orbit`:** o gerador **não consome `orbitas`** — a chave existia no
`roteiro.json` e não virava nada no HTML. O layout desenha o anel com quatro
pontos em 0/90/180/270°, sem rótulo de data. A chave foi removida do roteiro para
não deixar dado morto. As datas continuam nos kickers das cenas 7, 9 e 10.

**Achado do `orbit` (2):** o anel passa **atrás** do texto (`.ring` z-index 1,
`.core` z-index 3) e gira de −26° a 62° durante a cena, então um dos pontos
atravessa a linha do kicker por uma fração de segundo. No frame de 35,71 s o
ponto cai no espaço entre "A" e "ÚLTIMA". **Não cobre letra** — é decoro do
layout aprovado no LAB 003, não fantasma de texto.

**Gancho conferido em frame do mp4:** a cena 1 fica **legível em 0,10 s**
(kicker e título no ar, ainda em fade) e **completa em 0,60 s** — kicker, título,
duas linhas pequenas e a régua. É o quarto episódio seguido em que o
`digital-zoom` entrega o primeiro segundo.

**Armadilha confirmada:** o `frames.py` marca a cena 1 como `ESTOURA`
(x0 = 70, x1 = 960) porque o zoom (`scale: 1.12`) cresce e o texto passa da
margem de 116 px. É **câmera**, não estouro de cartão. Regra do LAB 003 vale:
`ESTOURA` em `digital-zoom`/`orbit`/`vertigo`/`pull-back` não reprova. O x1 de
960 no pico do zoom foi **provocado de propósito**: com a fonte original (128) a
palavra "ABANDONARAM" ia a **1040 px**, a 40 px da borda; com 118 fecha em 960.

## Editorial

- [x] **Gancho aprovado no lote:** "Abandonaram o navio no gelo. Ele navegou 38
      anos sozinho." — ação/consequência, sem contexto; o frame 1 já conta o
      abandono e a volta.
- [x] **Cena 2 não é cartão de contexto** (regra pós-004): entrega a **virada** —
      "TEMPORAL / LEVOU ELE." + "E ELE / VOLTOU."
- [x] Uma ideia por vídeo: **um navio abandonado no gelo que continuou
      aparecendo por 38 anos, sem ninguém a bordo**
- [x] Fatos com fonte: Wikipédia (EN), Kenn Harper (*Nunatsiaq News*, 2006),
      Dalton & Delgado (2006), Hutchison (1934), Manitoba Museum (2020) —
      rodapé no vídeo
- [x] "Um temporal levou ele. E ele voltou." = 24/11/1931, temporal de três dias,
      temperatura de −60 °C a zero, navio achado intacto a 45 milhas
- [x] "Um cargueiro da Hudson's Bay, carregado de peles." = comprado pela HBC em
      1921, nove viagens ao Ártico, preso no gelo com a carga de peles no porão
- [x] "O gelo fechou. Vinte e dois saíram de avião. Quinze ficaram." = 15/10/1931,
      retirada aérea de 22 tripulantes; 15 ficaram e construíram abrigo na praia
- [x] "Voltaram ao navio. Tiraram as peles. E deixaram ele." = as duas viagens de
      trenó para tirar mantimentos; abandono definitivo em março de 1932, com
      peles ainda no porão
- [x] "45 milhas ao sul. Depois, trezentas a leste." = os dois primeiros
      avistamentos depois do abandono
- [x] "Estranhos subiram a bordo. O porão ainda tinha peles." = 11/08/1933, a
      12 milhas de Wainwright, abordagem pelos moradores e pela tripulação do
      *M.S. Trader*
- [x] "Uma botânica escreveu: parecia uma torre acima do gelo." = Isobel Wylie
      Hutchison, *North to the Rime-Ringed Sun* (1934): o casco "se erguia como
      uma torre acima do pequeno Trader"
- [x] "Tentaram rebocar. O gelo não deixou." = novembro de 1939, capitão Hugh
      Polson; o gelo se moveu e ele desistiu
- [x] "Em 1969, foi visto pela última vez." = último avistamento registrado, Mar
      de Beaufort, entre Point Barrow e Icy Cape
- [x] "O Alasca procurou o navio. Não achou nada." = projeto do governo do Alasca
      em 2006; não localizado
- [x] **A compressão do gancho é corrigida no corpo:** o vídeo **nunca** repete
      "navegou" — depois da cena 1 o navio "apareceu", "voltou" e "ficou no
      gelo". O `briefing.md` registra que o Baychimo **derivava**, sem leme e sem
      máquina
- [x] **Não afirma que afundou:** a cena 12 pergunta ("SE AFUNDOU, OU SE AINDA
      ESTÁ LÁ"), não conclui — a hipótese do naufrágio é presunção, não registro
- [x] **Ninguém morreu:** o vídeo não sugere tripulação perdida; os 22 saíram de
      avião em outubro e os 15 em março
- [x] **Carga:** "o porão ainda tinha peles" — os quinze tiraram as mais valiosas,
      não todas
- [x] Sem graphicidade gratuita; sem CTA comercial
- [ ] **Escuta humana pendente** de "Baychimo", "Hudson's Bay", "Wainwright",
      "Point Barrow", "Beaufort", "Polson", "Hutchison" (transliterações no
      `briefing.md` e no `narracao_tts.txt`)

## Cadeia de áudio (medida antes, não depois)

| Etapa | LUFS | TP |
|---|---:|---:|
| `voz_raw.wav` (Piper, volume 1.0) | −15,1 | **+0,1** |
| `voz.wav` (`volume=-6.9dB,alimiter=limit=0.85`) | −22,0 | −6,8 |
| `final_raw.mp4` (mix com drone a 0,16) | −19,1 | −6,8 |
| `final.mp4` (`volume=4.1dB,alimiter=limit=0.85`) | **−15,0** | −2,7 |

O Piper saiu **quente** de novo (−15,1 LUFS, TP +0,1), como no 008 (−15,7), 009
(−16,1) e 010 (−16,3). O sinal do pós foi escolhido **depois** de medir o cru:
**+4,1 dB**, e não +7 dB. O `final_raw` caiu em **−19,1 LUFS**, o mesmo valor do
008, do 009 e do 010.

## Identidade

- [x] Paleta, tipografia, moldura, marca `DOSSIÊ 45` e dossiê `011`
- [x] Voz impessoal, sem "eu" ou "nós"
- [x] Drone a 0,16 — **mesmo arquivo dos anteriores** (inaudível por projeto)
- [x] Rodapé corrigido antes do render: saiu o **NPS** (fonte do 010, não deste
      caso) e ficou `FONTE · WIKIPÉDIA · DALTON & DELGADO, 2006`
- [x] Capa `capa.png` — frame em **25,52 s**, 1080×1920: `ESTRANHOS / A BORDO.` +
      `O PORÃO AINDA / TINHA PELES.` (s7, 23,35–26,77 s)

## Ritmo (variável do lote 007–011: o gancho)

| Medida | 007 | 008 | 009 | 010 | **011** |
|---|---:|---:|---:|---:|---:|
| Palavras escritas | 108 | 106 | 109 | 113 | **113** |
| Cenas | 12 | 12 | 12 | 12 | **12** |
| Cena mais longa | 5,029 s | 4,70 s | 4,64 s | 4,57 s | **5,23 s** (s1) |
| Silêncio | 20,5% | 17,9% | 22,3% | 19,6% | **19,9%** |
| Gancho | "Um homem morto na praia" | "Dois canais de TV foram invadidos ao vivo" | "Dois homens mortos no morro" | "O navio apareceu vazio" | **"Abandonaram o navio no gelo"** |
| 1º segundo | moldura só | texto legível em 0,10 s | texto legível no 1º frame | legível em 0,10 s | **legível em 0,10 s; completo em 0,60 s** |

**A cena 1 tem 5,23 s — 233 ms acima do teto de 5 s.** É o gancho aprovado do
lote em uma frase só (4,06 s de fala + 0,6 s de entrada + cauda), e encurtar
significaria mudar o texto aprovado. Registrado aqui como o 007 fez com a sua
cena de 5,029 s. As outras 11 cenas ficam entre 2,58 s e 4,84 s.

## Correções antes do render

- **Falas enxugadas** depois da primeira síntese: o take inicial deu **42,4 s de
  fala** (silêncio de 5,8%) e a cena 10 em **5,748 s**. Saíram as datas faladas
  que já estavam nos kickers: s5 11→9 palavras, s7 16→9, s9 13→6, s10 17→12.
  Resultado: **36,0 s de fala e 19,9% de silêncio**, na média do lote.
- **Títulos reescritos** porque quebravam em 3 linhas: `O TEMPORAL` → `TEMPORAL`
  (s2) e `UM CARGUEIRO` → `CARGUEIRO` (s3).
- **Fonte reduzida em 5 cenas:** s7 150→138, s8 150→124, s9 150→146, s11 150→140,
  s12 140→110. A s12 ("ENCONTRADO.") é a mais estreita do lote: 11 caracteres a
  140 px iam a 955 px.
- **Fonte da s1 128→118** e re-render: no pico do zoom a palavra "ABANDONARAM"
  ia a **1040 px** (40 px da borda); agora fecha em 960.
- **Rodapé corrigido** e re-render: o NPS vinha do 010 e não é fonte deste caso.

## Pendências

- Escuta humana dos nomes e aprovação explícita — **não publica sem isso**.
- O `qa.ps1` mediu **−15,0 LUFS** e o `ebur128` **−15,0**: as duas concordaram
  neste episódio (no 010 divergiram em 0,1 por arredondamento).

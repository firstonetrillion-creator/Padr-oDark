# QA — 010-carroll-a-deering

**Data:** 2026-11-03
**Arquivo:** `final.mp4`
**Render:** standard, 1080×1920, 30 fps, captura segmentada — **1350/1350
frames**, 5 segmentos, 0 retries, **3m56,5s**
**Duração:** 45,013 s · **Tamanho:** 4.088.419 bytes (3,90 MB)
**Voz:** Piper `pt_BR-faber-medium`, **cena por cena** (`montar-voz.py`) —
36,188 s de fala + 8,812 s de silêncio (19,6%) = 45,000 s
**SHA-256 (`final.mp4`):**
`33FC547F185995B414EA804D78D265EE54E509F4EBD5CF00205B67FC360A225D`

## Técnico

| Item | Medição | Status |
|---|---|---|
| Codec de vídeo | H.264, 1080×1920 | OK |
| FPS | 30/1 constante | OK |
| Áudio | AAC 48 kHz, estéreo | OK |
| Loudness | **−14,9 LUFS** (cru: −19,1; pós-render **+4,1 dB** + limitador 0,85) | OK |
| Pico | true peak **−1,4 dBFS** | OK |
| LRA | 3,6 LU | OK |
| Preto inesperado | nenhum; fade final em ~44,3–45,0 s | OK |
| Texto cortado | 12 frames do `final.mp4`; nenhuma cena acima de 5 linhas | OK |
| Linha mais larga | **805 px de 840** (s3); nos frames do mp4, 800 px | OK |
| Sincronia | 12 cenas de `tempos_cenas.json` — **exatas por construção**, sem ASR | OK |
| Contrato | `check-contrato.ps1` — **OK, 1 aviso** (12 cenas, padrão é 13) | OK |
| QA automático | `qa.ps1 -Duracao 45` | **PASS** |
| Marca | `DOSSIÊ 45` / dossiê `010` | OK |

## Layouts (2 por episódio, como aprovado em 01/11)

| Cena | Layout | Por quê |
|---|---|---|
| s1 (0,00–4,49) | `digital-zoom` | o gesto do caso é aproximar de um navio sem ninguém dentro; mesmo tratamento do gancho do 008 e do 009 (variável controlada) |
| s4 (10,77–14,69) | `checklist` | o que faltava a bordo é uma lista de evidências: botes, diário, instrumentos, pertences, âncoras |

As outras 10 cenas são o cartão do v1, sem `tipo`. Contrato §2b passou:
`data-layout`, `window.__layouts` inlinado e `layout-<tipo>` em todas.

**Achado:** a cena 1 fica **legível em 0,10 s** (frame extraído do mp4: título no
ar, ainda em fade) e **completa em 0,60 s** — kicker, título, linha pequena e
régua. É a variável do lote (o primeiro segundo) e o terceiro episódio seguido em
que o `digital-zoom` ajuda nela.

**Armadilha confirmada:** o `frames.py` marca a cena 1 como `ESTOURA`
(x0 = 70 px, x1 = 720) porque o zoom cresce e o texto passa da margem de 116 px.
É **câmera**, não estouro de cartão. Regra do LAB 003 vale: `ESTOURA` em
`digital-zoom`/`orbit`/`vertigo`/`pull-back` não reprova.

## Editorial

- [x] **Gancho aprovado no lote:** "O navio apareceu vazio. E a comida ainda
      estava na mesa." — 4 palavras na primeira frase, ação/consequência, sem
      contexto. Frame 1 já conta o achado.
- [x] **Cena 2 não é cartão de contexto** (regra pós-004): entrega a **cena do
      abordar** — "A BORDO, NINGUÉM. / AS VELAS ESTAVAM POSTAS."
- [x] Uma ideia por vídeo: **um navio achado vazio, com sinais de vida
      interrompida, e onze homens que nunca apareceram**
- [x] Fatos com fonte: NPS (Cape Hatteras), Wikipédia (EN e DE), Bland Simpson
      (2005), McAllister (2009), Grenon (2010), NYT e Washington Post (1921),
      New York Herald (26/08/1921) — rodapé no vídeo
- [x] "O guarda costeiro subiu a bordo. Não havia ninguém." = abordagem em
      04/02/1921 pelo *Manning* e pelo *Rescue*, com o capitão James Carlson
- [x] "Onze homens. Nenhum corpo. Nenhum bote." = tripulação de 11; nenhum corpo
      encontrado; os dois botes sumiram
- [x] "Faltavam os botes, o diário, os instrumentos e as âncoras." = lista da
      Guarda Costeira: dois botes, diário de bordo, cronômetro, sextante, os
      pertences e as duas âncoras
- [x] "O leme estava quebrado. O navio não governava." = timão em pedaços, caixa
      da agulha arrebentada, leme solto do eixo; dois faróis vermelhos no mastro
- [x] "No farol de Cape Lookout, um homem gritou pelo megafone." = 29/01/1921,
      farol flutuante nº 80, comandante Thomas Jacobson
- [x] "Perdemos as âncoras. E não era o capitão quem falava." = Jacobson
      registrou que não era o capitão nem um oficial; o homem era ruivo e tinha
      sotaque estrangeiro
- [x] "Em Barbados, o imediato disse: pego o capitão antes de Norfolk." =
      McLellan, bêbado, no Continental Café, ouvido por três capitães
- [x] "Em abril, uma garrafa apareceu na praia. Dizia que eram piratas." =
      11/04/1921, Buxton, pescador Christopher Columbus Gray
- [x] "O pescador que a achou tinha escrito ela. E confessou." = perícia em
      caligrafia e confissão a agentes federais; ele queria um emprego na estação
      de farol
- [x] "Cinco repartições investigaram. O caso fechou sem resposta." = Comércio,
      Tesouro, Justiça, Marinha e Estado; encerrado no fim de 1922
- [x] "O casco foi dinamitado. Nenhum dos onze foi encontrado." = dinamitado em
      março de 1921 por ser perigo à navegação; nenhum corpo jamais achado
- [x] **Lenda fora do vídeo, e registrada:** o Triângulo das Bermudas **não entra
      em cartão** (ligação posterior: Fort 1931, Gaddis 1965, Berlitz 1974; o
      naufrágio foi em Cape Hatteras). Marcado no `briefing.md` e na descrição
- [x] "A comida ainda estava na mesa" = **comida posta, não tocada**. O vídeo não
      diz "quente" nem "fresca" — o navio passou quatro dias encalhado
- [x] Não diz que houve motim: o inquérito **adotou** a hipótese e **nunca a
      provou**
- [x] Não afirma piratas, bolcheviques, contrabandistas nem furacão como causa
- [x] Sem graphicidade gratuita; sem CTA comercial
- [ ] **Escuta humana pendente** de "Carroll A. Deering", "Cape Hatteras",
      "Diamond Shoals", "Cape Lookout", "Barbados", "Norfolk", "Wormell",
      "McLellan" (transliterações no `briefing.md` e no `narracao_tts.txt`)

## Cadeia de áudio (medida antes, não depois)

| Etapa | LUFS | TP |
|---|---:|---:|
| `voz_raw.wav` (Piper, volume 1.0) | −16,3 | **+0,2** |
| `voz.wav` (`volume=-5.7dB,alimiter=limit=0.85`) | −22,0 | −5,5 |
| `final_raw.mp4` (mix com drone a 0,16) | −19,1 | −5,5 |
| `final.mp4` (`volume=4.1dB,alimiter=limit=0.85`) | **−15,0** | −1,4 |

O Piper saiu **quente** de novo (−16,3 LUFS, TP +0,2), como no 008 (−15,7) e no
009 (−16,1). O sinal do pós foi escolhido **depois** de medir o cru; por isso o
ganho foi **+4,1 dB**, e não +7 dB. O `final_raw` caiu em **−19,1 LUFS**, igual
ao 008 e ao 009.

## Identidade

- [x] Paleta, tipografia, moldura, marca `DOSSIÊ 45` e dossiê `010`
- [x] Voz impessoal, sem "eu" ou "nós"
- [x] Drone a 0,16 — **mesmo arquivo dos anteriores** (inaudível por projeto)
- [x] Capa `capa.png` — frame em **9,6 s**, 1080×1920: `ONZE HOMENS. / NENHUM
      CORPO. / NENHUM BOTE.` (s3, 7,81–10,76 s)

## Ritmo (variável do lote 007–011: o gancho)

| Medida | 007 | 008 | 009 | **010** |
|---|---:|---:|---:|---:|
| Palavras escritas | 108 | 106 | 109 | **113** |
| Cenas | 12 | 12 | 12 | **12** |
| Cena mais longa | 5,029 s | 4,70 s | 4,64 s | **4,57 s** (s12) |
| Silêncio | 20,5% | 17,9% | 22,3% | **19,6%** |
| Gancho | "Um homem morto na praia" | "Dois canais de TV foram invadidos ao vivo" | "Dois homens mortos no morro" | **"O navio apareceu vazio. E a comida ainda estava na mesa."** |
| 1º segundo | moldura só | texto legível em 0,10 s | texto legível no 1º frame | **legível em 0,10 s; completo em 0,60 s** |

Nenhuma cena passou de 5 s. O 010 tem **113 palavras** — o maior do lote — mas a
cena mais longa (4,57 s) ficou **abaixo** das do 007, 008 e 009: as falas são
mais curtas e o silêncio entre elas é menor (19,6%).

## Correções antes do render

- Fonte reduzida em 8 cenas: s2 168→162, s3 186→184, s4 138→134, s5 150→142,
  s7 138→122, s10 140→132, s11 128→122, s12 124→122.
- s5 estourava (842 px, x1 = 967); as demais ficaram "apertadas" (829–837).
- **s9 e s12 trocaram de título** porque a linha quebrava em duas: `UMA GARRAFA`
  (11 caracteres a 124 px) virava três linhas, e `FOI DINAMITADO.` (14) também.
  Ficaram `A GARRAFA / NA PRAIA.` e `O CASCO FOI / DINAMITADO.`
- **s7 ganhou kicker** (`O HOMEM DO MEGAFONE`): sem kicker o bloco subia e
  desalinhava do resto da sequência.

## Pendências

- Escuta humana dos nomes e aprovação explícita — **não publica sem isso**.
- O `qa.ps1` mediu **−14,9 LUFS** e o `ebur128` **−15,0**: diferença de
  arredondamento entre as duas ferramentas, registrada para não parecer
  divergência.

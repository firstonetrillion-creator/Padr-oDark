# QA — 008-max-headroom

**Data:** 2026-11-01
**Arquivo:** `final.mp4`
**Render:** standard, 1080×1920, 30 fps, captura segmentada — **1350/1350
frames** no container, 5 segmentos, 0 retries, 3m30,0s
**Duração:** 45,013 s · **Tamanho:** 3.914.187 bytes (3,91 MB)
**Voz:** Piper `pt_BR-faber-medium`, **cena por cena** (`montar-voz.py`) —
36,927 s de fala + 8,073 s de silêncio (17,9%) = 45,000 s
**SHA-256 (`final.mp4`):**
`70CB5963590E04DD133FD4FAB59212592311074893E7FBC3DB69CA0162F704A7`

## Técnico

| Item | Medição | Status |
|---|---|---|
| Codec de vídeo | H.264, 1080×1920 | OK |
| FPS | 30/1 constante | OK |
| Áudio | AAC 48 kHz, estéreo | OK |
| Loudness | **−15,0 LUFS** (cru: −19,1; pós-render **+4,1 dB** + limitador 0,85) | OK |
| Pico | true peak **−2,1 dBFS** | OK |
| LRA | 2,4 LU | OK |
| Preto inesperado | nenhum; fade final em ~44,3–45,0 s | OK |
| Texto cortado | 12 frames do `final.mp4` + 3 extras da cena 1; nenhuma cena acima de 5 linhas | OK |
| Linha mais larga | **802 px de 840** (s4, s6 e s12) | OK |
| Sincronia | 12 cenas de `tempos_cenas.json` — **exatas por construção**, sem ASR | OK |
| Contrato | `check-contrato.ps1` — **OK, 1 aviso** (12 cenas, padrão é 13) | OK |
| QA automático | `qa.ps1 -Duracao 45` | **PASS** |
| Marca | `DOSSIÊ 45` / dossiê `008` | OK |

## Layouts (1ª vez em episódio)

Dois estilos, como aprovado em 01/11 (**1–2 por episódio**):

| Cena | Layout | Por quê |
|---|---|---|
| s1 (0,00–4,40) | `digital-zoom` | zoom em degraus imita o gesto do caso: uma imagem analógica invadindo outra |
| s11 (36,29–40,99) | `orbit` | um dado isolado no centro — **NÃO PODEM SER PRESOS.** |

As outras 10 cenas são o cartão do v1, sem `tipo`. Contrato §2b passou:
`data-layout`, `window.__layouts` inlinado e `layout-<tipo>` em todas.

**Achado do `digital-zoom`:** a cena 1 fica **legível em 0,10 s** (o zoom parte
da escala cheia e o texto já está no ar), ao contrário do v1, em que o primeiro
frame é só a moldura e o texto entra por volta de 0,6 s. É a variável do lote
(o primeiro segundo) e a primeira evidência de que o layout ajuda nela.

**Armadilha confirmada:** `medir-texto.ps1` marca a cena 1 como `ESTOURA`
(x0 = 70–89 px) porque o zoom cresce e o texto passa da margem de 116 px. É
**câmera**, não estouro de cartão — nada é cortado (x1 máx. 820). Regra do
LAB 003 vale: `ESTOURA` em `digital-zoom`/`orbit`/`vertigo`/`pull-back` não
reprova.

## Editorial

- [x] **Gancho aprovado no lote:** "Dois canais de TV foram invadidos ao vivo.
      Ninguém foi preso." — 8 palavras na primeira frase, ação/consequência,
      sem contexto. Frame 1 já conta o ato.
- [x] **Cena 2 não é cartão de contexto** (regra pós-004): entrega o
      **mecanismo** — "CHICAGO, 1987. / O SINAL VINHA POR MICRO-ONDAS."
- [x] Uma ideia por vídeo: **duas emissoras invadidas ao vivo, uma máscara, e
      um crime que prescreveu sem que ninguém fosse identificado**
- [x] Fatos com fonte: Wikipédia (EN) "Max Headroom signal hijackings";
      WTTW News 21/11/2017 (a emissora invadida); VICE/Motherboard 25/11/2013 —
      rodapé no vídeo
- [x] "Nove e catorze" / "21H14" = WGN-TV, 22/11/1987, no bloco de esportes
- [x] "A torre estava vazia. Ninguém podia cortar." = WTTW sem engenheiro de
      plantão na Sears Tower (porta-voz Anders Yocom, WTTW 2017)
- [x] "A FCC investigou. O FBI examinou a fita." = investigação aberta no dia
      seguinte; o FBI fez ampliações fotográficas da fita
- [x] "Prescreveu em noventa e dois" = prazo federal de cinco anos, vencido em
      1992 (VICE, com base no manual do Departamento de Justiça)
- [x] **"EU TAMBÉM NÃO SEI O QUE HOUVE."** é **tradução** da fala de Dan Roan
      ("if you're wondering what's happened, so am I"), não citação literal —
      o cartão atribui ("DAN ROAN, AO VIVO.") e não finge transcrição
- [x] **Nenhuma lenda no vídeo:** os irmãos "J e K", Eric Fournier e o
      "funcionário demitido da WGN" estão fora, como lista em `briefing.md`
- [x] Não diz que houve "hacker invadindo computador": foi **sinal de
      micro-ondas sobreposto** ao enlace estúdio–torre
- [x] Não diz que a segunda invasão durou "90 segundos exatos": a fita mede 82 s
      e a emissora relata ~90 s; o vídeo não cita duração
- [x] Sem graphicidade gratuita; sem CTA comercial
- [ ] **Escuta humana pendente** de "Máks Rédrum", "Chicágo", "dábliu gê êne",
      "dábliu tê tê dábliu", "Dóktor U", "éfe cê cê", "éfe bê i"
      (transliterações no `briefing.md` e no `narracao_tts.txt`)

## Correção feita antes do render final

O fecho dizia **"TRINTA E OITO ANOS SEM NOME"**. Em 22/11/2026 o caso completa
**39 anos**, então o número apodreceria em três semanas — e o vídeo fica no ar.
Trocado pelo fato permanente: **"NINGUÉM SABE QUEM USAVA A MÁSCARA."**
Re-sintetizada a voz (só a cena 12), regerado o HTML, medido de novo e
**re-renderizado**. O primeiro `final.mp4` (SHA-256 `EEFC47C2…6749C0`) foi
substituído; o `final_raw.mp4` atual é o do segundo render.

## Cadeia de áudio (medida antes, não depois)

| Etapa | LUFS | TP |
|---|---:|---:|
| `voz_raw.wav` (Piper, volume 1.0) | −15,7 | **+0,1** |
| `voz.wav` (`volume=-6.3dB,alimiter=limit=0.85`) | −22,0 | −6,2 |
| `final_raw.mp4` (mix com drone a 0,16) | −19,1 | −6,2 |
| `final.mp4` (`volume=4.1dB,alimiter=limit=0.85`) | **−15,0** | −2,1 |

O Piper saiu **quente** (−15,7 LUFS, TP +0,1) — o oposto do 006 (−22,17). O
sinal do pós foi escolhido **depois** de medir o cru, como manda a correção do
007; por isso o ganho foi **+4,1 dB**, e não +7 dB.

## Identidade

- [x] Paleta, tipografia, moldura, marca `DOSSIÊ 45` e dossiê `008`
- [x] Voz impessoal, sem "eu" ou "nós"
- [x] Drone a 0,16 — **mesmo arquivo dos anteriores** (SHA-256 igual ao 003–007;
      inaudível por projeto, som audível é variável de canal novo)
- [x] Capa `capa.png` — frame em **31,1 s**, 1080×1920: `A TORRE ESTAVA VAZIA. /
      NINGUÉM PODIA CORTAR.` (s9, 29,66–32,60 s)

## Ritmo (variável do lote 007–011: o gancho)

| Medida | 005 | 006 | 007 | **008** |
|---|---:|---:|---:|---:|
| Palavras escritas | 111 | 114 | 108 | **106** |
| Cenas | 12 | 14 | 12 | **12** |
| Cena mais longa | 5,00 s | 4,17 s | 5,029 s | **4,70 s** (s11) |
| Silêncio | — | 9,3% | 20,5% | **17,9%** |
| Gancho | "Cinco aviões pediram socorro" | "Eles cortaram a encosta" | "Um homem morto na praia" | **"Dois canais de TV foram invadidos ao vivo. Ninguém foi preso."** |
| 1º segundo | moldura só | moldura só | moldura só | **texto legível em 0,10 s** (`digital-zoom`) |

Nenhuma cena passou de 5 s — o problema do 007 (5,029 s) não se repetiu: a cena
11 pedia 5,508 s com o ano por extenso e foi encurtada para "prescreveu em
noventa e dois" (o kicker já mostra **1992**).

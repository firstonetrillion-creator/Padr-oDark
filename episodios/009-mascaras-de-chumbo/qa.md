# QA — 009-mascaras-de-chumbo

**Data:** 2026-11-02
**Arquivo:** `final.mp4`
**Render:** standard, 1080×1920, 30 fps, captura segmentada — **1350/1350
frames**, 5 segmentos, 0 retries, **3m32,0s**
**Duração:** 45,013 s · **Tamanho:** 3.834.702 bytes (3,83 MB)
**Voz:** Piper `pt_BR-faber-medium`, **cena por cena** (`montar-voz.py`) —
34,958 s de fala + 10,042 s de silêncio (22,3%) = 45,000 s
**SHA-256 (`final.mp4`):**
`3E0A2ACEEEEE0A09E51049F00B634B059607CB9341A462FA79C4B04E1BD173AC`

## Técnico

| Item | Medição | Status |
|---|---|---|
| Codec de vídeo | H.264, 1080×1920 | OK |
| FPS | 30/1 constante | OK |
| Áudio | AAC 48 kHz, estéreo | OK |
| Loudness | **−14,9 LUFS** (cru: −19,1; pós-render **+4,1 dB** + limitador 0,85) | OK |
| Pico | true peak **−1,7 dBFS** | OK |
| LRA | 3,9 LU | OK |
| Preto inesperado | nenhum; fade final em ~44,3–45,0 s | OK |
| Texto cortado | 12 frames do `final.mp4`; nenhuma cena acima de 5 linhas | OK |
| Linha mais larga | **800 px de 840** (s6 e s8) | OK |
| Sincronia | 12 cenas de `tempos_cenas.json` — **exatas por construção**, sem ASR | OK |
| Contrato | `check-contrato.ps1` — **OK, 1 aviso** (12 cenas, padrão é 13) | OK |
| QA automático | `qa.ps1 -Duracao 45` | **PASS** |
| Marca | `DOSSIÊ 45` / dossiê `009` | OK |

## Layouts (2 por episódio, como aprovado em 01/11)

| Cena | Layout | Por quê |
|---|---|---|
| s1 (0,00–4,34) | `digital-zoom` | o gesto do caso é olhar de perto uma foto que não revela nada; mesmo tratamento do gancho do 008 (variável controlada) |
| s4 (12,69–16,69) | `checklist` | o bilhete é o documento do caso: quatro comandos, marcados um a um |

As outras 10 cenas são o cartão do v1, sem `tipo`. Contrato §2b passou:
`data-layout`, `window.__layouts` inlinado e `layout-<tipo>` em todas.

**Achado:** a cena 1 fica legível no **primeiro frame** — o `digital-zoom` parte
da escala cheia e o texto já está no ar, como no 008. É a variável do lote (o
primeiro segundo) e o segundo episódio seguido em que o layout ajuda nela.

**Armadilha confirmada:** o `frames.py` marca a cena 1 como `ESTOURA`
(x0 = 72 px) porque o zoom cresce e o texto passa da margem de 116 px. É
**câmera**, não estouro de cartão — x1 máx. 842 e nada é cortado. Regra do
LAB 003 vale: `ESTOURA` em `digital-zoom`/`orbit`/`vertigo`/`pull-back` não
reprova.

## Editorial

- [x] **Gancho aprovado no lote:** "Dois homens mortos no morro. Máscaras de
      chumbo. Nenhuma marca." — 5 palavras na primeira frase, ação/consequência,
      sem contexto. Frame 1 já conta o resultado.
- [x] **Cena 2 não é cartão de contexto** (regra pós-004): entrega a
      **contradição** — "ELES IAM A SÃO PAULO. / O ÔNIBUS FOI PARA NITERÓI."
- [x] Uma ideia por vídeo: **dois técnicos cumprem um bilhete escrito à mão e
      morrem sem que o laudo diga de quê**
- [x] Fatos com fonte: Wikipédia (PT) "Mistério das máscaras de chumbo";
      *O Globo* 22/08/1966 e 14/09/1966; *O Cruzeiro* 12/09/1966;
      *Correio da Manhã* 27/10/1966 — rodapé no vídeo
- [x] "Saíram de Campos. Iam a São Paulo. Foram para Niterói." = saída de Campos
      dos Goytacazes em 17/08/1966, destino declarado e chegada a Niterói
- [x] "Compraram capa e água. Ele parecia ter hora marcada." = capa impermeável
      e garrafa d'água compradas em Niterói; funcionária da loja disse que Miguel
      parecia nervoso, "como se tivesse hora marcada" — o cartão atribui a
      impressão à atendente
- [x] "Um bilhete no bolso. Dezesseis e trinta: local determinado." / "Dezoito e
      trinta: ingerir cápsula após o efeito." = bilhete na caligrafia de Miguel,
      transcrito em *O Globo* 22/08/1966 e *O Cruzeiro*
- [x] "Quatro dias depois, um menino achou os corpos." = 20/08/1966, Jorge da
      Costa Alves, 18 anos, empinando pipa no Morro do Vintém
- [x] "Terno, capa e máscara de chumbo em forma de óculos. Nenhum ferimento." =
      descrição dos corpos; IML não encontrou sinal de violência
- [x] "No bolso, códigos de válvulas eletrônicas." = bloco com símbolos e números,
      códigos de referência para válvulas
- [x] "Dois meses depois, o laudo: causa indeterminada." = laudo do IML
- [x] "O delegado falou em experiência parapsicológica." = delegado Idovan
      Ferreira, *O Globo* 14/09/1966 — o cartão diz "PARAPSICOLOGIA, DISSE ELE."
- [x] **Lenda marcada como lenda:** o disco voador entra na s11 com kicker
      **A LENDA** e a linha **NUNCA PROVADO.**; o vídeo não afirma que houve
      disco nem que a morte teve causa extraterrestre
- [x] "Nenhuma marca" = **nenhum sinal de violência** (laudo). O vídeo não diz
      "sem um arranhão" nem "intactos" — os corpos estavam em decomposição
- [x] Não diz que o laudo "não achou veneno": ele **não pôde fazer** o exame
      toxicológico (decomposição)
- [x] Não afirma autoria, assassinato, suicídio ritual nem causa extraterrestre
- [x] Sem graphicidade gratuita; sem CTA comercial
- [ ] **Escuta humana pendente** de "Cãpos dos Goitacazes", "Niterói", "Vintém",
      "Manoel Pereira da Cruz", "Miguel José Viana", "Idovan Ferreira",
      "Élcio Correia Gomes", "Gracinda Barbosa Coutinho de Souza"
      (transliterações no `briefing.md` e no `narracao_tts.txt`)

## Cadeia de áudio (medida antes, não depois)

| Etapa | LUFS | TP |
|---|---:|---:|
| `voz_raw.wav` (Piper, volume 1.0) | −16,1 | **+0,1** |
| `voz.wav` (`volume=-5.9dB,alimiter=limit=0.85`) | −22,0 | −5,8 |
| `final_raw.mp4` (mix com drone a 0,16) | −19,1 | −5,9 |
| `final.mp4` (`volume=4.1dB,alimiter=limit=0.85`) | **−14,9** | −1,7 |

O Piper saiu **quente** de novo (−16,1 LUFS, TP +0,1), como no 008 (−15,7) e ao
contrário do 006 (−22,17). O sinal do pós foi escolhido **depois** de medir o
cru; por isso o ganho foi **+4,1 dB**, e não +7 dB.

## Identidade

- [x] Paleta, tipografia, moldura, marca `DOSSIÊ 45` e dossiê `009`
- [x] Voz impessoal, sem "eu" ou "nós"
- [x] Drone a 0,16 — **mesmo arquivo dos anteriores** (inaudível por projeto)
- [x] Capa `capa.png` — frame em **32,68 s**, 1080×1920: `CAUSA /
      INDETERMINADA.` (s9, 30,53–33,92 s)

## Ritmo (variável do lote 007–011: o gancho)

| Medida | 006 | 007 | 008 | **009** |
|---|---:|---:|---:|---:|
| Palavras escritas | 114 | 108 | 106 | **109** |
| Cenas | 14 | 12 | 12 | **12** |
| Cena mais longa | 4,17 s | 5,029 s | 4,70 s | **4,64 s** (s2) |
| Silêncio | 9,3% | 20,5% | 17,9% | **22,3%** |
| Gancho | "Eles cortaram a encosta" | "Um homem morto na praia" | "Dois canais de TV foram invadidos ao vivo" | **"Dois homens mortos no morro. Máscaras de chumbo. Nenhuma marca."** |
| 1º segundo | moldura só | moldura só | texto legível em 0,10 s | **texto legível no 1º frame** (`digital-zoom`) |

Nenhuma cena passou de 5 s. A cena mais longa é a 2 (4,64 s) — a contradição
São Paulo/Niterói, que precisa dos dois destinos no ar.

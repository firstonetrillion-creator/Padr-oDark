# ESTADO — retomada por etapa

> **Arquivo de instrução do OpenCode** (`opencode.jsonc`). Atualizar a **cada passo**, não a cada etapa.
> Depois de uma compactação, a versão atual deste arquivo é relida do disco e vira a baseline da sessão.
> Memória longa continua em `MEMORIA.md`; aqui só o suficiente para retomar sem reler nada.

**Atualizado:** 2026-11-04 · **Gate 2 PASSA (3 de 6)** · **007–012: QA PASS, aguardando aprovação humana** · 17 layouts: APROVADOS em 01/11 — 1º uso no 008 · canal único · `sombra-direta` pausado

## Onde estamos

**Gate 2 fechado em 29/10/2026 — PASSA.** Com 005 em **54,3%** e 006 em **50,0%**
(no limite), o canal fecha **3 de 6** acima de 50% de `% média assistida`
(002 87,0%; 003 87,0%; 005 54,3%), e o critério era ≥3. Os 6 vídeos da Fase 2
estão no ar e medidos.

**O que o gate libera:** decidir o modelo do canal 2 e o A/B de v2 — cada um
como **uma variável em canal separado**. **O que ele não faz:** autorizar mudar
duas coisas no Dossiê 45, que segue com o v1 e com a regra “sem cartão parado
depois do gancho”.

**Achado que sobrevive ao gate:** o 005 (12 cenas) **dobrou** a duração média do
004 (0:25 contra 0:21) com **menos views** (224 contra 1.200); o 006 (14 cenas)
ficou no limite e **caiu no gancho** (ficaram 38,2% contra 46,5%). O miolo foi
resolvido — o próximo ajuste é o **primeiro segundo**.

**Fora da fila, aprovada em 01/11:** a **biblioteca de 17 estilos de cena**
(`templates/layouts/`) passou o LAB 003 com QA PASS em 31/10 e foi **aprovada
pelo usuário em 01/11**. É aditiva: sem `tipo` no roteiro, o HTML sai idêntico
ao v1 (007 conferido por SHA-256). Uso: **1–2 estilos por episódio**.

## Biblioteca de layouts — 17 estilos (**aprovada** em 01/11)

| Etapa | Estado |
|---|---|
| Biblioteca | **pronta** — `templates/layouts/{registro.json,layouts.css,layouts.js,README.md}`; 4 famílias sobre o cartão do v1 |
| Gerador | **pronto** — `"tipo"` por cena, inlining no `index.html`, validação (tipo, `itens`/`valores`, asset sem crédito, `zoom-through` no fim) |
| Contrato | **pronto** — `check-contrato.ps1` §2b (data-layout, `window.__layouts`, `layout-<tipo>`, arquivo de asset) |
| Retrocompatível | **provado** — 007 regerado sem `tipo`: `index.html` com o **mesmo SHA-256** |
| LAB 003 | **QA PASS** — `laboratorio/003-layouts-17/`: 17 cenas, 45,077 s, 3m06s de render, −15,0 LUFS, TP −2,5, 1352 frames; SHA-256 `59D282C2…5E9AF7` |
| Frames | **conferidos** — 17 frames do `final.mp4` + `contact-1.png`/`contact-2.png`; nenhum título em 3 linhas |
| Aprovação | **APROVADA em 01/11** — os 17 entram, 1–2 por episódio |
| 1º uso em episódio | **008** — `digital-zoom` na cena 1 e `orbit` na cena 11; as outras 10 cenas seguem o cartão do v1 |

**Os 17:** orbit · couch-wall · ui-world · frame-break · digital-zoom ·
phone-mockup · checklist · headline-wall · zoom-through · chart-grow ·
pull-back · green-screen · paper-cut · doodle-boil · vertigo · cover-story ·
glass-type.

**Armadilhas novas:** (1) `snapshot` não mostra a cena 1 — a órbita saiu
invisível no 1º render, só o frame do mp4 pegou; (2) `alimiter=limit=0.85`
limita **amostra**, não inter-sample (`voz.wav`: pico −1,41, TP **+0,2**);
(3) `ESTOURA` em câmera (`digital-zoom`, `vertigo`, `pull-back`,
`zoom-through`) e em decoro (moldura, barras, parede) **não reprova**.

## Fila imediata — lote 007–011 (temas **aprovados** em 29/10)

Plano completo em `docs/PLANO.md` §“Fase 3 — lote 007–011”. **007 a 012
concluídos** (todos com QA PASS, publicação pronta, aguardando aprovação). Canal
único: Dossiê 45 (`sombra-direta` e `mente-obscura` pausados).

**A variável do lote é o gancho:** o primeiro segundo abre com ação/consequência,
nunca com contexto. Tudo o mais fica igual ao 005 (45 s, **12 cartões**, ≤5 s,
v1, Piper, 1080×1920/30 fps). **Hipótese:** mediana de “ficaram” ≥ 46,5% e de
`% média` > 54,3%. **Cadência (decidida pelo usuário em 02/11): 3–4 vídeos por
dia**, publicados manualmente. A cadência anterior (1/dia, 19h, seg–sex) valia
até 01/11. Com 3–4/dia os vídeos competem pela mesma audiência no feed: a
retenção de 48 h vale por vídeo, mas a comparação entre vídeos do mesmo dia fica
confundida — ler a mediana do lote como **sinal**, não como teste controlado.

| # | Slug | Tema | Gancho | Estado |
|---|---|---|---|---|
| 007 | `007-homem-de-somerton` | Homem de Somerton (1948) | “Um homem morto na praia. Um código costurado na roupa.” | **QA PASS 31/10 — publicação pronta, aguardando aprovação** |
| 008 | `008-max-headroom` | Invasão Max Headroom (1987) | “Dois canais de TV foram invadidos ao vivo. Ninguém foi preso.” | **QA PASS 01/11 — publicação pronta, aguardando aprovação** |
| 009 | `009-mascaras-de-chumbo` | Máscaras de chumbo (1966) | “Dois homens mortos no morro. Máscaras de chumbo. Nenhuma marca.” | **QA PASS 02/11 — publicação pronta, aguardando aprovação** |
| 010 | `010-carroll-a-deering` | Carroll A. Deering (1921) | “O navio apareceu vazio. E a comida ainda estava na mesa.” | **QA PASS 03/11 — publicação pronta, aguardando aprovação** |
| 011 | `011-ss-baychimo` | SS Baychimo (1931–1969) | “Abandonaram o navio no gelo. Ele navegou 38 anos sozinho.” | **QA PASS 03/11 — publicação pronta, aguardando aprovação** |
| 012 | `012-hinterkaifeck` | Hinterkaifeck (1922) | “Seis pessoas mortas na fazenda. Alguém ainda ordenhou as vacas.” | **QA PASS 04/11 — publicação pronta, aguardando aprovação** |

**Próximo comando:** o lote está produzido — **seis vídeos prontos e sem
aprovação** (007 a 012). Falta escuta humana dos nomes e **aprovação explícita**
(“publique” conta; “conclua” não). **Cadência nova (02/11): 3–4 por dia**, na
ordem que o usuário definir — com seis prontos, o estoque cobre **de um a dois
dias**.


## Episódio 012 — Hinterkaifeck

| Etapa | Estado |
|---|---|
| Briefing | **pronto** — 10 fontes numeradas: Wikipédia DE e EN, *Salzburger Wacht* 06/04/1922, *Salzburger Volksblatt* 22/04/1922 e 01/02/1935, Donaukurier 2012, Augsburger Allgemeine 2012, Leuschner 1997, Bill James 2017, Hinterkaifeck-Wiki |
| Gancho | **aprovado no lote** — “Seis pessoas mortas na fazenda. Alguém ainda ordenhou as vacas.” |
| Roteiro | **pronto** — `roteiro.json`, 108 palavras, **12 cenas**, máx **4,63 s** (s12) |
| Voz | **pronta** — cena por cena (`montar-voz.py`): 35,958 s de fala + 9,042 s de silêncio (20,1%) → `voz_raw.wav` 45,000 s |
| Áudio pré-render | **cru −16,4 LUFS / TP +0,1** → `voz.wav` `volume=-5.6dB` + limitador 0,85 → **−22,0 LUFS**, TP −5,5 |
| Composição | **pronta** — 12 cenas; **2 layouts**: `digital-zoom` (s1) e `checklist` (s4); contrato **OK, 1 aviso** |
| QA visual | **concluído** — 11 cenas no snapshot + 12 frames do mp4 + gancho em 0,10 s e 0,60 s; pior tinta **810 px** (s5); s1 só no frame do mp4 |
| Render | **concluído** — `final_raw.mp4` 45,000 s, 1.350 frames, 5 segmentos, 0 retries, **3m11,8s** (4m16,9s no 1º, antes do ajuste do checklist) |
| Áudio final | **+4,1 dB** + limitador 0,85 (cru −19,1) → **−15,0 LUFS**, TP −1,4, LRA 4,0 |
| QA | **QA PASS** — `qa.ps1 -Duracao 45`; `qa.md` escrito em 04/11 |
| Capa | **pronta** — `capa.png` em 10,20 s (“PEGADAS NA NEVE. / NENHUMA DE VOLTA.”) |
| publicacao.md | **pronto** — título `Hinterkaifeck: 1922 sem um acusado` (34 chars, lint **98/100**); SHA-256 `6B3E3F54…E16F28C6` |
| Aprovação humana | **pendente** |
| Publicação | **pendente** — cadência de 3–4/dia |

**Correções antes do render:** o primeiro take deu **40,0 s de fala** (silêncio de
11,1%) e a **s11 em 6,278 s**, porque os dois anos soletrados (“mil novecentos e
cinquenta e cinco”) estouravam a cena. A s11 virou “Os autos fecharam. Décadas
depois, ainda ouviam testemunhas.” e os anos ficaram no kicker `1955 · 1986`. O
fecho também encurtou: a s12 fechava em **5,745 s** (a última cena absorve a cauda
do vídeo) e virou “Ninguém foi acusado. Hoje, ali é só lavoura.”, com o ano no
cartão pequeno.

**Achado do `text-wrap: balance`:** `FOI ACUSADO.` a 130 px (12 caracteres ≈
940 px) quebrava em duas e fazia o título sair em **3 linhas**. Voltou para
`NINGUÉM FOI / ACUSADO.` com fonte **116** (751 px). O gerador não avisa — só o
`medir-texto.ps1` pega, e só depois de o HTML novo ser gerado (snapshot antigo não
serve).

**Achado do `checklist`:** os `itens` são texto pequeno e **não** entram na conta
de linhas do `medir-texto.ps1` (que mede o `h1`); a conferência é visual.

**Armadilha nova:** `Set-Content -Encoding UTF8` no PowerShell 5.1 grava **BOM** e
o `gerar-episodio.py` morre com `Unexpected UTF-8 BOM`. Editar `roteiro.json` com
o `edit` tool ou com `[IO.File]::WriteAllText` + `UTF8Encoding($false)`.

**Decisões do episódio:** **sem idades** (as fontes divergem: Andreas 63/64,
Maria 44/45) e **sem graphicidade** — o detalhe da autópsia da menina ficou só no
`briefing.md`; o vídeo diz o que aconteceu, não como o corpo ficou. O item 1 do
`checklist` era “pegadas só de ida”, que a s3 acabava de dizer; entrou **“A VACA
SOLTA NO ESTÁBULO”**, um fato do briefing que só o cartão entrega. Nenhuma cena
passa de 5 s — primeiro episódio do lote sem exceção no teto.

## Episódio 011 — SS Baychimo

| Etapa | Estado |
|---|---|
| Briefing | **pronto** — 9 fontes numeradas: Wikipédia EN, Kenn Harper (*Nunatsiaq News* 24/11/2006), Dalton & Delgado 2006, Hutchison 1934, Manitoba Museum 2020, *Time* 29/02/1932, Gillingham 1955, *UNESCO Courier* 1991, projeto do Alasca 2006 |
| Gancho | **aprovado no lote** — “Abandonaram o navio no gelo. Ele navegou 38 anos sozinho.” (fórmula 17) |
| Roteiro | **pronto** — `roteiro.json`, 113 palavras, **12 cenas**, máx **5,23 s** (s1, 233 ms acima do teto — registrado) |
| Voz | **pronta** — cena por cena (`montar-voz.py`): 36,049 s de fala + 8,951 s de silêncio (19,9%) → `voz_raw.wav` 45,000 s |
| Áudio pré-render | **cru −15,1 LUFS / TP +0,1** → `voz.wav` `volume=-6.9dB` + limitador 0,85 → **−22,0 LUFS**, TP −6,8 |
| Composição | **pronta** — 12 cenas; **2 layouts**: `digital-zoom` (s1) e `orbit` (s10); contrato **OK, 1 aviso** |
| QA visual | **concluído** — 11 cenas no snapshot; pior tinta **807 px** (s3); s1 só no frame do mp4, legível em 0,10 s |
| Render | **concluído** — `final_raw.mp4` 45,000 s, 1.350 frames, 5 segmentos, 0 retries, **3m15,9s** |
| Áudio final | **+4,1 dB** + limitador 0,85 (cru −19,1) → **−15,0 LUFS**, TP −2,7, LRA 3,8 |
| QA | **QA PASS** — `qa.ps1 -Duracao 45`; `qa.md` escrito em 03/11 |
| Capa | **pronta** — `capa.png` em 25,52 s (“ESTRANHOS A BORDO. / O PORÃO AINDA TINHA PELES.”) |
| publicacao.md | **pronto** — título `SS Baychimo: 38 anos à deriva no gelo` (37 chars, lint **100/100**); SHA-256 `4C71CB58…B70869` |
| Aprovação humana | **pendente** |
| Publicação | **pendente** — cadência de 3–4/dia |

**Correções antes do render:** o primeiro take deu **42,4 s de fala** (silêncio
de 5,8%) e a cena 10 em **5,748 s**; saíram as datas faladas que já estavam nos
kickers (s5 11→9 palavras, s7 16→9, s9 13→6, s10 17→12) e o silêncio voltou a
19,9%. `O TEMPORAL` → `TEMPORAL` (s2) e `UM CARGUEIRO` → `CARGUEIRO` (s3)
quebravam em 3 linhas. Fonte reduzida em 5 cenas (s7 138, s8 124, s9 146, s11
140, s12 110) e a **s1 de 128 para 118**: no pico do zoom “ABANDONARAM” ia a
**1040 px**, a 40 px da borda; agora fecha em 960.

**Dois achados:** (1) o **`orbit` não consome `orbitas`** — a chave não vira
rótulo nenhum no HTML (o layout desenha só o anel com quatro pontos), e foi
removida do `roteiro.json`; (2) o anel passa **atrás** do texto e gira de −26° a
62°, então um ponto atravessa a linha do kicker por uma fração de segundo — não
cobre letra, é decoro aprovado no LAB 003.

**Armadilha nova:** o rodapé do 011 nasceu com **`NPS`** copiado do 010 — fonte
do caso anterior, não deste. Corrigido para `FONTE · WIKIPÉDIA · DALTON &
DELGADO, 2006` **antes** do render final; o rodapé aparece nas 12 cenas, então
conferir fonte no rodapé é etapa, não detalhe.

**Decisão do episódio:** o gancho diz “navegou”, mas o **corpo nunca repete a
palavra** — o navio “apareceu”, “voltou”, “ficou no gelo”. O `briefing.md`
registra que o Baychimo **derivava** com o gelo, sem leme e sem máquina, e que
“afundou em 1969” é **presunção**, não registro (a cena 12 pergunta, não
conclui). Ninguém morreu: os 22 saíram de avião em outubro e os 15 em março.

## Episódio 010 — Carroll A. Deering

| Etapa | Estado |
|---|---|
| Briefing | **pronto** — 12 fontes numeradas: Wikipédia EN e DE, NPS Cape Hatteras (“The Ghost Ship of the Outer Banks”), Simpson 2002/2005, McAllister 2009, Grenon 2010, NYT e Washington Post (jun/1921), New York Herald 26/08/1921, Boston Globe 05/04/1919, AP/St. Louis Post-Dispatch 21/06/1921, News & Observer 23/09/1955 |
| Gancho | **aprovado no lote** — “O navio apareceu vazio. E a comida ainda estava na mesa.” (fórmula 17) |
| Roteiro | **pronto** — `roteiro.json`, 113 palavras, **12 cenas**, máx **4,57 s** (s12) |
| Voz | **pronta** — cena por cena (`montar-voz.py`): 36,188 s de fala + 8,812 s de silêncio (19,6%) → `voz_raw.wav` 45,000 s |
| Áudio pré-render | **cru −16,3 LUFS / TP +0,2** → `voz.wav` `volume=-5.7dB` + limitador 0,85 → **−22,0 LUFS**, TP −5,5 |
| Composição | **pronta** — 12 cenas; **2 layouts**: `digital-zoom` (s1) e `checklist` (s4, o que faltava a bordo); contrato **OK, 1 aviso** |
| QA visual | **concluído** — 11 cenas no snapshot; pior tinta **805 px** (s3); s1 só no frame do mp4 |
| Render | **concluído** — `final_raw.mp4` 45,000 s, 1.350 frames, 5 segmentos, 0 retries, **3m56,5s** |
| Áudio final | **+4,1 dB** + limitador 0,85 (cru −19,1) → **−15,0 LUFS**, TP −1,4, LRA 3,6 |
| QA | **QA PASS** — `qa.ps1 -Duracao 45`; `qa.md` escrito em 03/11 |
| Capa | **pronta** — `capa.png` em 9,6 s ("ONZE HOMENS. / NENHUM CORPO. / NENHUM BOTE.") |
| publicacao.md | **pronto** — título `Carroll A. Deering: 1921, o navio vazio` (39 chars, lint **100/100**); SHA-256 `33FC547F…360A225D` |
| Aprovação humana | **pendente** |
| Publicação | **pendente** — cadência de 3–4/dia |

**Correções antes do render:** s2 168→162, s3 186→184, s4 138→134, s5 150→142,
s7 138→122, s10 140→132, s11 128→122, s12 124→122; s12 e s9 trocaram de título
(“O CASCO FOI / DINAMITADO.” e “A GARRAFA / NA PRAIA.”) porque a linha a 14 e a 11
caracteres quebrava em duas. A s7 ganhou kicker **O HOMEM DO MEGAFONE** — sem ele
o bloco subia e desalinhava do resto.

**Decisão do episódio:** **o Triângulo das Bermudas não entra em cartão**. A
ligação é posterior (Fort 1931, Gaddis 1965, Berlitz 1974) e o naufrágio foi em
Cape Hatteras; fica marcada como lenda no `briefing.md` e numa linha da descrição
em `publicacao.md`. O 009 usou cartão de lenda porque o disco voador estava no
material de 1966; aqui não há documento de época que sustente a lenda.

## Episódio 009 — Máscaras de chumbo

| Etapa | Estado |
|---|---|
| Briefing | **pronto** — 9 fontes numeradas: Wikipédia PT (base), Wikipédia EN, O Globo 22/08 e 14/09/1966, O Cruzeiro 12/09/1966, Correio da Manhã 27/10/1966, Aventuras na História 2019, Linha Direta, Skeptoid |
| Gancho | **aprovado no lote** — “Dois homens mortos no morro. Máscaras de chumbo. Nenhuma marca.” (fórmula 17 + 14) |
| Roteiro | **pronto** — `roteiro.json`, 109 palavras, **12 cenas**, máx **4,64 s** (s2) |
| Voz | **pronta** — cena por cena (`montar-voz.py`): 34,958 s de fala + 10,042 s de silêncio (22,3%) → `voz_raw.wav` 45,000 s |
| Áudio pré-render | **cru −16,1 LUFS / TP +0,1** → `voz.wav` `volume=-5.9dB` + limitador 0,85 → **−22,0 LUFS**, TP −5,8 |
| Composição | **pronta** — 12 cenas; **2 layouts**: `digital-zoom` (s1) e `checklist` (s4, o bilhete); contrato **OK, 1 aviso** |
| QA visual | **concluído** — 11 cenas no snapshot; pior tinta **800 px** (s6 e s8); s1 só no frame do mp4, legível no 1º frame |
| Render | **concluído** — `final_raw.mp4` 45,000 s, 1.350 frames, 5 segmentos, 0 retries, **3m32,0s** |
| Áudio final | **+4,1 dB** + limitador 0,85 (cru −19,1) → **−14,9 LUFS**, TP −1,7, LRA 3,9 |
| QA | **QA PASS** — `qa.ps1 -Duracao 45`; `qa.md` escrito em 02/11 |
| Capa | **pronta** — `capa.png` em 32,68 s (“CAUSA / INDETERMINADA.”) |
| publicacao.md | **pronto** — título `Máscaras de chumbo: dois mortos em 1966` (39 chars, lint **100/100**); SHA-256 `3E0A2ACE…D173AC` |
| Aprovação humana | **pendente** — escuta dos nomes + aprovação explícita |
| Publicação | **pendente** — cadência de **3–4/dia**; ordem definida pelo usuário |

**Números finais:** `final.mp4` **45,013 s · 3.834.702 bytes · −14,9 LUFS ·
TP −1,7 · LRA 3,9** (ganho **+4,1 dB** sobre −19,1). SHA-256
`3E0A2ACEEEEE0A09E51049F00B634B059607CB9341A462FA79C4B04E1BD173AC`.

**Decisões do episódio:** o bilhete entra em `checklist` com os quatro comandos
separados (16h30 · local; 18h30 · cápsula; proteger metais; aguardar sinal) —
o layout existe para enumerar evidência, e o bilhete é o documento do caso. O
disco voador entra **marcado como lenda** (s11: “A LENDA / NUNCA PROVADO”), como
o 008 fez com a autoria nunca provada.

**Achados de medida:** a s3 a 170 px quebrou “UMA CAPA” em duas linhas (3 linhas
em vez de 2) e a s7 a 170 px estourou para x1 = 969. Corrigidas para 150 e 160.
A lista do bilhete, com o item único “PROTEGER METAIS · AGUARDAR SINAL”, ia a
930 px; dividida em dois itens, caiu para 838.

## Episódio 008 — Max Headroom

| Etapa | Estado |
|---|---|
| Briefing | **pronto** — Wikipédia (EN) “Max Headroom signal hijackings”; WTTW News 21/11/2017; VICE/Motherboard 25/11/2013 |
| Gancho | **aprovado no lote** — “Dois canais de TV foram invadidos ao vivo. Ninguém foi preso.” (fórmula 17) |
| Roteiro | **pronto** — `roteiro.json`, 106 palavras, **12 cenas**, máx **4,70 s** (s11) |
| Voz | **pronta** — cena por cena (`montar-voz.py`): 36,927 s de fala + 8,073 s de silêncio (17,9%) → `voz_raw.wav` 45,000 s |
| Áudio pré-render | **cru −15,7 LUFS / TP +0,1** (Piper quente) → `voz.wav` `volume=-6.3dB` + limitador 0,85 → **−22,0 LUFS**, TP −6,2 |
| Composição | **pronta** — 12 cenas; **1º episódio com layouts**: `digital-zoom` (s1) e `orbit` (s11); contrato **OK, 1 aviso** |
| QA visual | **concluído** — 12 snapshots + 12 frames do `final.mp4` + 3 extras da cena 1; pior tinta **802 px** de 840 |
| Render | **concluído** — `final_raw.mp4` 45,000 s, 1.350 frames, 5 segmentos, 0 retries, **3m30,0s** |
| Áudio final | **+4,1 dB** + limitador 0,85 (cru −19,1) → **−15,0 LUFS**, TP −2,1, LRA 2,4 |
| QA | **QA PASS** — `qa.ps1 -Duracao 45`; `qa.md` escrito em 01/11 |
| Capa | **pronta** — `capa.png` em 31,1 s (“A TORRE ESTAVA VAZIA. / NINGUÉM PODIA CORTAR.”) |
| publicacao.md | **pronto** — título `Max Headroom: a TV invadida que ninguém explicou` (48 chars, lint **98/100**); SHA-256 `70CB5963…F704A7` |
| Aprovação humana | **pendente** — escuta dos nomes + aprovação explícita |
| Publicação | **pendente** — 1/dia, 19h: 007 em 02/11, 008 em 03/11 |

**Dois achados novos:** (1) **o `digital-zoom` resolve o primeiro segundo** — a
cena 1 fica legível em **0,10 s**, contra ~0,6 s do v1 (medido em frame do mp4);
(2) **o Piper saiu quente** (−15,7 LUFS, TP +0,1, o oposto do 006 em −22,17) e
por isso o pós foi **+4,1 dB**, não +7. Medir o cru antes de escolher o sinal
continua sendo a regra.

**Correção antes do render final:** o fecho dizia “TRINTA E OITO ANOS SEM NOME”
— em 22/11/2026 o caso completa 39 anos, e o número apodreceria em três
semanas. Trocado pelo fato permanente “NINGUÉM SABE QUEM USAVA A MÁSCARA.”,
com voz e render refeitos.

## Episódio 007 — Homem de Somerton

| Etapa | Estado |
|---|---|
| Briefing | **pronto** — Wikipédia PT “Caso Taman Shud”; Guardian 27/07/2022 e 31/07/2022; ABC 01/12/2018 |
| Gancho | **aprovado no lote** — “Um homem morto na praia. Um código costurado na roupa.” (fórmula 10 + dado da 1) |
| Roteiro | **pronto** — `roteiro.json`, 108 palavras, **12 cenas**, máx **5,029 s** (cena 3, 29 ms acima do teto — registrado) |
| Voz | **pronta** — cena por cena (`montar-voz.py`): 35,768 s de fala + 9,232 s de silêncio (20,5%) → `voz_raw.wav` 45,000 s; `voz.wav` +5 dB, limitador 0,85 **antes** do render |
| Composição | **pronta** — 12 cenas geradas do `roteiro.json`; contrato **OK, 1 aviso** (re-rodado em 31/10) |
| QA visual | **concluído** — 7 frames do `final.mp4`; sem overflow; pior tinta **800 px** de 840 (s9) |
| Render | **concluído** — `final_raw.mp4` 45,000 s, **1.350 frames**, 29/10 17:58 |
| Áudio final | **reprocessado em 31/10** — cru −10,6 LUFS (voz pré-normalizada) → `volume=-4.4dB` + limitador 0,85 → **−15,0 LUFS**, TP −5,9, LRA 3,2 |
| QA | **QA PASS** — `qa.md` assinado em 31/10 |
| Capa | **pronta** — `capa.png` em 17,7 s (“O PAPEL DIZIA: ACABADO. / PERSIA, TAMÁM SHUD.”) |
| publicacao.md | **pronto** — título `Somerton: o homem sem nome por 74 anos` (38 chars, lint **100/100**); SHA-256 `DE13EECD…462B6B` |
| Aprovação humana | **pendente** — escuta dos nomes + aprovação explícita |
| Publicação | **pendente** — 31/10 é sábado; próxima janela da cadência: **segunda 02/11 às 19h** (publicar no sábado é decisão explícita do usuário) |

**Correção feita em 31/10:** `frame_s1.png` e `frame_fecho.png` eram o **mesmo
arquivo** (SHA-256 idêntico — a extração de 29/10 falhou). Re-extraídos do
`final.mp4` como `qa-final/qa-frame-01..07.png`; antigos preservados em
`qa-final/antigos-extracao-falhou/`.

**Armadilha nova:** o `final_raw.mp4` saiu em **−10,6 LUFS** porque a voz foi
pré-normalizada com +5 dB **antes** do render (em 004–006 o ganho era no pós).
O passo de normalização de 29/10 reduziu o volume sem registrar o filtro. Regra:
medir o cru **antes** de escolher o sinal do pós, e registrar o comando.

## Episódio 006 — Passo Dyatlov

| Etapa | Estado |
|---|---|
| Briefing | **pronto** — Gaume & Puzrin 2021; processo 2-236 (1959); ICRF 2015–2019; PGR 2020 |
| Gancho | **pronto** — “Eles cortaram a encosta para dormir. A neve esperou nove horas.” |
| Roteiro | **pronto** — `114` palavras, **14 cenas**, máx **4,17 s**, 2,5 pal./s |
| Voz | **pronta** — **cena por cena** (`montar-voz.py`), ls 1.10: 40,814 s de fala + 4,186 s de silêncio → `voz_raw.wav` **45,000 s**; `voz.wav` −22,15 LUFS, TP −8,12 |
| Tempos | **exatos por construção** (`tempos_cenas.json` do `montar-voz.py`), sem ASR |
| Composição | **pronta** — 14 cenas geradas do `roteiro.json`; contrato **OK, 1 aviso** (14 em vez de 13) |
| QA visual | **concluído** — 14 frames do render; pior tinta **806 px** de 840; 6 cenas com fonte corrigida antes do render |
| Render | **concluído** — `final_raw.mp4` 45,000 s, 1.350 frames, **5 segmentos**, 0 retries, 3m09,9s |
| QA | **QA PASS** — `qa.md` escrito |
| Publicação | **PUBLICADO em 27/10** — https://youtube.com/shorts/K_sgJjNHg84 (`K_sgJjNHg84`); `duration=45` e `age_limit=0` conferidos |

**Números finais:** `final.mp4` **45,013 s · 3.859.117 bytes · −15,19 LUFS ·
TP −1,30 dBFS** (ganho **+7,0 dB** sobre −22,17). SHA-256
`B2AA85F3A308E155FAA953BF395BF1CC2E03A3FB66F3DC64CD1D9119F10033A6`.
Capa em 32,6 s (“DOIS TÓRAX AFUNDADOS. / UM CRÂNIO RACHADO. / SEM FERIDA NA
PELE.”). Título: `Passo Dyatlov: a avalanche chegou 9 horas depois`.

**Números novos:** o `final_raw.mp4` já saiu em **−22,17 LUFS**, quase igual ao
`voz.wav` (−22,15) — o drone a 0,16 é inaudível como projetado. O ganho foi
**+7,0 dB**, o maior até agora (004 +6,5; 005 +1,05).

**Achado do QA:** o `medir-texto.ps1` pegou uma quebra **invisível na
estimativa** — com `fonte_px` 152 a cena 4 partia “UM DEGRAU” em duas linhas no
frame. Seis cenas desceram de fonte antes do render (s4 152→136, s7 138→132,
s8 124→118, s9 124→122, s11 138→130, s13 98→96).

**Falso alarme registrado:** o frame de 5,9 s **parece** ter texto duplicado
quando visto em escala reduzida. A medição por banda de tinta dá exatamente 3
linhas + a linha pequena, 834 px de largura total (incluindo rodapé). Não há
fantasma.

**Por que 14 cenas:** no take único a última cena ficava **6,44 s** no ar
(a voz só termina às 44 s e o remap fecha a cena no fim do vídeo). O veredito
virou dois cartões — **1959 · FORÇA NATURAL** e **2020 · AVALANCHE** — e cada um
cabe em ~3 s.

**O que mudou no método:** o ASR do faster-whisper errou 28% dos tokens
(“cortam um degrau” virou “Cota o mundo legal”) e o `remapear.py` derrapou
**1,4 s** na cena 4. A voz passou a ser sintetizada por cena e concatenada com
silêncio calculado — o tempo é a soma dos blocos. Novo script:
`scripts/montar-voz.py` (documentado em `scripts/README.md` e
`docs/ARQUITETURA.md` §3.2 e §6).

**Próximo comando:** ~~em 29/10, ler a retenção de 48 h de 005 e 006~~ **feito
em 29/10**: 005 **54,3%**, 006 **50,0%**. Registros preenchidos
(`biblioteca/publicados.csv`, `canais/dossie45/metricas.csv`) e **Gate 2 fechado
com 3 de 6**. Ver `episodios/006-passo-dyatlov/retencao.md`.

## Episódio 005 — Voo 19

| Etapa | Estado |
|---|---|
| Briefing | **pronto** — fontes primárias validadas (Board of Investigation 1945, 56 achados) |
| Gancho | **aprovado** em 25/10/2026 |
| Roteiro | **pronto** — `111` palavras, **12 cenas** (2,5 palavras/s) |
| Voz | **pronta** — `voz_raw.wav` 43,839 s (ls 1.15) → `voz.wav` 45,000 s, −16,17 LUFS, TP −3,18 |
| Remap | **pronto** — `transcricao.json` + `tempos_cenas.json` (12 cenas, máx 5,00 s) |
| Composição | **pronta** — 12 cenas, contrato **OK, 1 aviso** (12 em vez de 13) |
| QA visual | **concluído** — 12 frames do render + gancho medido (máx 772 px de 840) |
| Render | **concluído** — `final_raw.mp4` 45,000 s, 5 segmentos, 0 retries, 3m11s |
| QA / publicação | **QA PASS** · **aprovado** em 26/10 · **PUBLICADO em 27/10** |

**No ar:** https://youtube.com/shorts/wlPEoYErlZQ · `wlPEoYErlZQ` ·
216 views e 5 likes no snapshot de 27/10 · `duration=45`, `age_limit=0` conferidos
por `yt-dlp` sem cookies · **retenção de 48 h vence em 29/10**. Selo **AI** na
página pública: a conferir.

**Pacote de publicação:** `publicacao.md` (título 46 chars, lint **98/100**;
descrição com fontes; hashtags; capa em 38,6 s) e cópia
`005-voo-19_shorts_v1.mp4` (SHA-256 igual ao `final.mp4`).

**Números finais:** `final.mp4` **45,013 s · 3.344.787 bytes · −15,16 LUFS ·
TP −2,18 dBFS** (ganho +1,05 dB — o `voz.wav` já estava em −16,17, ao contrário
dos +6,5 dB do 004). SHA-256 `69696A09F4A9A41DF0C0D19103ABE4B3602EC1DB18A9F3753535F1F8F7C4DBBF`.
Capa `capa.png` em 38,6 s ("27 HOMENS / NENHUM CORPO.").

**Gancho:** “Cinco aviões pediram socorro. Nenhum voltou. Nem o resgate.”
Capa: `27 HOMENS / NENHUM CORPO` (~39 s, cena 11).
Cena 2 **não** é cartão de contexto (regra pós-004): “O rádio funcionava. Eles
falavam com a base. Não sabiam onde estavam.”

**Próximo comando:** nada a produzir até decidir. O 006 está pronto e **sem
aprovação**; a retenção do 005 vence em **29/10**.

## Gerador (novo em 26/10)

`scripts/gerar-episodio.py` escreve o `index.html` a partir de `roteiro.json`
(+ `tempos_cenas.json` do `remapear.py`). O 005 é o teste de aceitação: gerado do
JSON, o HTML sai idêntico ao escrito à mão.

`scripts/medir-texto.ps1` mede a **tinta** no frame (snapshot → PNG → bbox por
linha) e corrige `fonte_px` com `-Aplicar`. Ciclo padrão antes de cada render:

```
gerar-episodio.py  →  medir-texto.ps1  →  (-Aplicar)  →  gerar-episodio.py  →  render
```

**Regra nova:** o `index.html` gerado não se edita à mão — a próxima geração
apaga. Mudou texto, fonte ou tempo? Muda o `roteiro.json` e gera de novo.

**Armadilha nova:** `hyperframes snapshot` **não mostra a cena 1** — sai vazia em
0,6 s, 2,0 s e 3,9 s (o mesmo acontece com o 004, cujo vídeo publicado tem o
gancho normal). O `snapshot` serve para as cenas 2–12; a cena 1 só se confere em
frame do mp4.

**Armadilha 2:** frame de vídeo visto em escala reduzida **inventa fantasma** —
texto serifado fino parece duplicado/espaçado. Medir com perfil de pixels
(ffmpeg → gray → contagem por linha) antes de “corrigir” o que não está errado.

## Episódio 004 — MV Joyita

| Etapa | Estado |
|---|---|
| Briefing / gancho / roteiro | prontos (`131` palavras, 13 cenas) |
| Voz | `voz_raw.wav` 44,117 s (ls 0.90) → `voz.wav` 45,000 s, **−21,63 LUFS**, TP −7,37 |
| Transcrição + remap | prontos (`transcricao.json`, 13 cenas) |
| Contrato | **OK, 0 avisos** |
| QA visual | **concluído** — frames 1–14 + `contact.png`; cena 6 em 4 linhas; frame 13 (fecho) em 2 linhas, sem overflow. frame 14 é só o fade e tem artefato de escala da captura. |
| Render | **concluído** — `final_raw.mp4` 45,000 s, −21,64 LUFS; 5 segmentos, 0 retries |
| QA / publicação | **publicado** em 24/10/2026 | https://youtube.com/shorts/rlSArCY3bH0 |

**Números finais:** `final.mp4` **45,013 s · 3.652.954 bytes · −15,16 LUFS · TP −1,42 dBFS**
(ganho +6,5 dB + limitador 0,85). SHA-256 `406906CE2F8AC652CCF33A828EF6E1E120CBD1A8EA9645ACAC5E8968BEA6EED7`.
Capa `capa.png` em 4,0 s (“25 PESSOAS / NENHUM SINAL”). Título com lint **100/100** (35 chars).

**Estado: publicado e verificado.** Aprovação humana em 24/10/2026; vídeo no ar
como Shorts público. Conferido: `availability=public`, `age_limit=0`,
`duration=45` (yt-dlp sem cookies) e selo **IA** visível na página pública.
Métricas iniciais: 276 views na primeira hora.

## Painel do Studio (relido em 26/10, com login)

| Métrica | 002 Mary Celeste | 003 Roanoke | 004 MV Joyita |
|---|---:|---:|---:|
| Views (48 h) | 234 | 370 | **1.200** |
| Ficaram para assistir | 48,6% | **53,0%** | **54,0%** |
| Duração média | 0:35 | **0:39** | **0:21** de 0:46 |
| % média assistida | 76,1% | **84,8%** | **45,7%** |
| Shorts feed | n/d | 92,2% | 98,9% |
| Espectadores únicos | n/d | n/d | **296** |

**Leitura:** o 004 não perdeu mais gente no gancho — “ficaram para assistir” é
até **um pouco maior** que no 003. Perdeu **no meio**: metade da duração média.
Isso reforça o slide e enfraquece a ideia de que o gancho piorou.

**Duas correções que a releitura trouxe:**

1. **A duração média escorrega com o tempo.** O 002 estava em 0:40 (87,0%) em
   25/10 e está em **0:35 (76,1%)** em 26/10; o 003 foi de 0:40 para 0:39. Cada
   view nova vem de feed mais frio. **O Gate 2 tem de usar janela fixa de 48 h.**
2. **O público real não é o imaginado.** 82,1% tem **55+** (zero abaixo de 45),
   78,2% masculino, 94,7% celular, e o **Brasil é só 49,2%** das views. Detalhe
   em `biblioteca/publico.md`.

## Scout de canais (novo em 26/10)

`scripts/scout.py` + `biblioteca/canais-semente.txt` — mede canais de Shorts que
estão **acelerando agora**. Fluxo invertido de propósito: **yt-dlp não descobre
canal** (não respeita filtro de busca), então o humano traz os canais e o script
mede. Segunda rodada com `--diff` dá views/dia real.

**Achado da 1ª rodada (12 canais do nicho):** só **1** tem volume (≥5k de
mediana) *e* aceleração (≥1,5×) — Wakinho, que é curiosidades, não arquivo.
Os que aceleram forte (Arquivo Sem Rastros 7×, De Olho 4×, Cofre dos Mistérios
2,5×) têm mediana de **44 a 297 views**: razão sem significância. Os que têm
volume estão parados ou caindo (Penumbroo **0,09×**, colapsando; Ossos Perdidos
1,0×). Só 3 passam de 0,5 views/inscrito.

**Leitura:** neste nicho, na amostra atual, **não há máquina de breakout para
copiar**. Ou o nicho é raso, ou os vencedores estão num nicho adjacente
(true crime / documentário), ou as sementes estão erradas.

Levantamento completo, com o raciocínio e os limites: **`docs/ESCALA.md`**.
Decisão registrada em `docs/DECISOES.md` e `docs/PLANO.md`. Ordem acordada em
26/10: **documentar → 005 → LAB 001 → gerador → A/B**. Nada de escalar o formato
antes do Gate 2.

## Laboratório (fora da fila, não publica)

`laboratorio/001-60s-fawcett/` — ensaio do **007**, com material barato.

| Item | Estado |
|---|---|
| Conceito | **pronto** — 4 variáveis, regra do trilho, critério de sucesso |
| Roteiro | **pronto** — `131` palavras, **16 cenas**, **60 s** (2,18 pal./s) |
| Narração | `narracao.txt` + `narracao_tts.txt` (148 tokens: números por extenso) |
| Voz | **pronta** — `voz_raw.wav` 59,999 s; `voz.wav` 60,000 s, −16,04 LUFS, TP −3,21 |
| Drone | **pronto** — gerado por lavfi (110/165 Hz + ruído), 60,000 s, −19,74 LUFS |
| Composição | **pronta** — 18 cenas (s8 e s10 divididas), contrato **OK, 1 aviso** |
| QA visual | **concluído** — 18 frames do render; **3 cenas corrigidas** (s5 96→90, s8a 104→98, s1 90→88); pior linha **826 px** |
| Render | **concluído** — 1.800 frames, 6 segmentos, 0 retries, 4m03s |
| QA | **QA PASS** (`qa.ps1 -Duracao 60`) · `qa.md` escrito · capa em 2,0 s |

**Números finais:** `final.mp4` **60,010 s · 4.652.077 bytes · −15,16 LUFS ·
TP −1,93 · LRA 3,70** (ganho +0,9 dB). SHA-256
`71A48162BDF327DB68EC4E2C10B50DFFA69DC64256C1B5BDE1BA2147606F6739`.
Marcador do trilho conferido no render: x=122 / 110 / 330 / 540 / 124 / 958
em 3 / 12 / 24 / 36 / 48 / 57 s.

**Voz gerada por cena** (`build_voz.py`): 16 blocos sintetizados separados e
concatenados com silêncio ponderado → **46,76 s de fala + 13,24 s de silêncio
(22,1%)**. Um take único não daria respiro no meio.

**Descoberta:** o `drone.wav` do 004 está em **−51,3 LUFS** (a 0,16 vira −67 no
mix, inaudível). O bed do laboratório foi feito em −19,7 para ficar ~20 dB sob a
voz — ou seja, o 001–004 são praticamente voz seca.

**Armadilha nova:** `tremolo` exige `f ≥ 0.1`. E `-Duracao` foi adicionado a
`check-contrato.ps1` **e a `qa.ps1`** (padrão 45, nada muda para 001–006; o
laboratório usa `-Duracao 60`).

**Armadilha 3 (26/10):** três cenas do laboratório **estouravam os 840 px** no
frame real (s5 882 px até x=1004, s8a 878 até 999, s1 840) — as métricas antigas
de texto não tinham pego porque mediam a caixa, não a tinta. Medir sempre
`ffmpeg → gray → bbox por linha` no PNG do frame, não `getBoundingClientRect`.

**Armadilha 4 (26/10):** `fromTo` com `yoyo: true` **termina no valor de partida**.
O “pisca” do marcador do trilho foi escrito assim e deixou o marcador a **15% de
opacidade** no vídeo todo — o 1º render do LAB 001 mediu (33,10,9) onde devia
estar (178,58,46). Corrigido para `to(...)`; agora o marcador anda visível
(x=285 em 20 s, x=550 em 40 s). Detalhe em `docs/ARQUITETURA.md` §9.

**Hipótese:** o que derruba o miolo não é a quantidade de texto, é o **estado
parado**. Por isso a contagem de palavras do teste é **idêntica à do 004 (131)** —
a diferença é tempo (60 s contra 45) e movimento (trilho de datas que anda).

**Tema:** Percy Fawcett, Mato Grosso, 1925 — também testa **assunto nacional**.

**Atenção:** 60 s = 1.800 frames, acima do limite de ~1.350 do Chrome; captura
segmentada obrigatória. Este teste **não** altera o v1 congelado do 003–006.

## Expansão — canais de teste (novo em 27/10)

Método criado para abrir **outros canais no YouTube testando outros modelos**.
Está em `canais/README.md`; o estado de cada canal fica em `canais/<slug>/`.

**As três regras:** um canal = **um modelo** (nicho + formato + voz + cadência +
visual); ao abrir o canal 2 muda **uma** dimensão e as outras quatro ficam iguais
ao Dossiê 45; **hipótese e critério de morte escritos na `ficha.md` antes do
vídeo 1**.

| Item | Onde |
|---|---|
| Método, protocolo de medição, critério de decisão | `canais/README.md` |
| Registro (uma linha por canal) | `canais/registro.csv` |
| Exemplo preenchido — o único canal com histórico | `canais/dossie45/{ficha.md,metricas.csv,decisoes.md}` |
| Canal novo | copiar `canais/_template/` para `canais/<slug>/` |
| Episódios de canal novo | `canais/<slug>/episodios/` (scripts são path-based; `novo-episodio.ps1` só grava em `episodios/`) |

**Decisão:** **N = 8** vídeos antes de decidir **escalar** (mediana de `% média`
≥ 50% **e** 10 s ≥ 50%) / **ajustar** (uma das duas) / **matar** (mediana < 40%
e views < 30% da referência). Custo ~16 h por canal; máx. **2 canais ativos**
nesta máquina. O teste de v2 (imagem de arquivo, som audível, 60 s) vira **canal
novo**, não um sétimo vídeo do Dossiê 45.

**Candidatos, não escolhidos:** A = mesmo formato + nicho adjacente (true crime
PT-BR); B = mesmo nicho + 60 s; C = mesmo nicho + som audível. **Decisão adiada
pelo usuário em 27/10 para depois do Gate 2** — o resultado de 005/006 muda qual
variável vale testar.

## Novo canal — `sombra-direta` (ativo, episódio 001 pronto)

Criado em 27/10/2026 como canal de teste fora da fila do Dossiê 45. Episódio 001
produzido e com QA PASS, aguardando aprovação humana para publicação.

| Item | Valor |
|---|---|
| Nome | Sombra Direta |
| Slug | `sombra-direta` |
| Nicho | psicologia sombria / manipulação mental / estoicismo vs Maquiavel |
| Template | `templates/sombra-cinema/` (CSS+GSAP, sem WebGL) |
| Episódio 001 | `canais/sombra-direta/episodios/001-mente-em-jogo/` |
| Estado | `ativo` |
| Vídeos produzidos | 1 |
| Bloqueio | **3 variáveis mudam vs Dossiê 45** (nicho, visual, áudio) — método permite 1; teste livre sem leitura comparativa controlada |

### Episódio 001 — Mente em Jogo (concluído)

**Gancho:** "Você é manipulado agora. E não sente nada." (fórmula 4 — Consequência)  
**Tema:** estoicismo vs Maquiavel / manipulação mental  
**Tom:** sombrio, seco, sem adjetivos vazios  
**Duração:** 45,01 s, 11 cenas, ~101 palavras  
**Visual:** CSS + GSAP apenas (sem WebGL/Three.js), fundo animado, texto fade+scale, glitch por CSS no twist  
**Áudio:** voz em 1,0 + bed sonoro audível + 3 pulsos de impacto  

| Etapa | Estado |
|---|---|
| Briefing / gancho / roteiro | prontos |
| narracao_tts.txt | pronto (11 parágrafos, 1 por cena) |
| Voz | pronta (Piper, ls 1.20, cena por cena, 45.000 s) |
| Bed + impacto | prontos (FFmpeg lavfi) |
| index.html | pronto (template sombra-cinema) |
| Contrato | OK (3 avisos aceitáveis) |
| Render | concluído — final_raw.mp4 45,0 s, 1350 frames, 5 segmentos, 0 retries |
| Áudio normalizado | concluído — +7,0 dB, limiter 0,85 |
| QA | **QA PASS** — −14,6 LUFS, 1080×1920, 30 fps, AAC 48 kHz |
| Capa | pronta — `capa.png` em 2,5 s |
| Cópia de publicação | pronta — `001-mente-em-jogo_shorts_v1.mp4` |
| publicacao.md | pronto |
| qa.md | assinado |
| SHA-256 | `F1466221164822E5696D0FE5B8B2112AC3E6055F61B7CD0E25B1D3D7B43ABB5E` |
| Aprovação humana | **pendente** |
| Publicação | **pendente** (conta Google separada do Dossiê 45) |
| Retenção 48 h | **pendente** — registrar em `canais/sombra-direta/metricas.csv` |

**Atenção:** nada disso entra no Dossiê 45. v1 do 45 fica congelado até o Gate 2
(29/10). Publicação de `sombra-direta` só em conta Google separada e com
aprovação humana explícita.

## Aceleração (novo em 27/10)

O render é **~3% do custo** (45 s = 3m10s; vídeo completo = ~2 h). 16 vídeos, que
são 2 canais × 8, dão **~1 h de render contra ~32 h de trabalho**. O gargalo é
pesquisa, decisão e espera de aprovação — não a máquina.

| Item | Estado |
|---|---|
| `scripts/tempo.ps1` | **pronto** — abre/fecha por etapa, grava `logs/tempo.csv`, `-Relatorio` agrega por etapa e por episódio. Sem base retroativa: começa no 007 |
| `docs/LAYOUTS.md` | **especificação pronta** — 8 tipos de cena, contrato retrocompatível (`sem tipo = texto`), manifesto de assets, política de imagem, plano LAB 002 |
| IA (`build.nvidia.com`) | **fora de produção** — tier é *trial* e FLUX.1-dev é *non-commercial*; 40 RPM não é o limite, a licença é. Serve para teste de estilo |
| Decisões abertas | imagem de arquivo × IA × só CSS/SVG; som junto ou separado; regra 7 para footage |

**Nada implementado no visual:** os layouts entram no template **depois** do
Gate 2, via LAB 002 (20–30 s, 3 layouts), nunca direto num episódio.

## Esperando (nada a fazer até as datas)

- **007 e 008** — escutar os nomes (007: Somerton, Adelaide, Tamám Shud, Omar
  Caiame, Glenelg; 008: Máks Rédrum, Chicágo, dábliu gê êne, dábliu tê tê
  dábliu, Dóktor U, éfe cê cê, éfe bê i), obter **aprovação explícita** e
  publicar **um por dia, 19h, seg–sex**: 007 em **02/11**, 008 em **03/11**.
  Retenção 48 h de cada um: **D+2 da data de publicação**.
- ~~**2026-10-29** — retenção de 48 h de **005** e **006**~~ **feito** (29/10):
  **005 54,3%** (224 views, ficaram 46,5%, 0:25 de 0:46) e **006 50,0%**
  (79 views, ficaram 38,2%, 0:23 de 0:46 — no limite do arredondamento).
  **Gate 2 PASSA com 3 de 6.** Evidência em `episodios/005-voo-19/retencao.md`
  e `episodios/006-passo-dyatlov/retencao.md`.
  - **005** era o teste da regra “sem cartão parado depois do gancho”: **passou**,
    e dobrou a duração média do 004 com menos views.
  - **006** testava se 14 cenas resolviam o miolo: ficou no limite e **perdeu no
    gancho** (38,2%). O miolo não é mais o problema; o primeiro segundo é.
- ~~**2026-10-26** — retenção de 48 h do **004**~~ **feito**: painel relido com
  login em 26/10. Falta só o `Todos.csv` de curva (aba Content do Studio não
  carrega). Ver `episodios/004-mv-joyita/retencao.md`.
- Leitura do 003: gancho melhorou (3 s e 10 s acima do 002), **mas o fim caiu**
  (36,1% vs 42,2%): slide de −32,4 p.p. entre 10 s e 44,5 s. Hipótese: a
  explicação do CROATOAN entregue cedo demais.

**Próximo comando (o que decidir agora):** produção do lote em dia (007 e 008
prontos), então a fila é **decisão**, não produção. Em ordem:
1. **Aprovar e publicar o 007** (janela 02/11, 19h) e o **008** (03/11, 19h) —
   falta só escuta humana dos nomes e “publique”.
2. **Usar a biblioteca no 009** — já provada no 008 (1–2 estilos por episódio:
   o gancho em `digital-zoom` e um dado isolado em `orbit`). No 009, manter a
   mesma disciplina: no máximo o gancho + um cartão de dado.
3. **Aprovar ou não** o `sombra-direta` 001 (`QA PASS`, cópia pronta) — precisa de
   conta Google separada, que ainda não existe.
4. **Escolher o modelo do canal 2** (A/B/C, adiado de propósito para depois do
   gate). Com 005 acima de 50% e 006 no limite por gancho, a leitura favorece
   testar **gancho/visual** antes de nicho.
5. Só depois: o A/B de v2.

## Bloqueios e regras vivas

- **Aprovação é explícita por vídeo.** “publique” conta; “conclua” ou “vamos aguardar” não.
- Um render por vez; 1080×1920, 30 fps, H.264 + AAC.
- **v1 não está mais congelado pelo Gate 2** (fechado em 29/10), mas continua
  sendo a referência: mudança de fonte/efeito/imagem entra como **uma variável**
  em **canal separado**, nunca direto no Dossiê 45.
- **Os 17 layouts estão aprovados (01/11)** e entram no Dossiê 45 como **1–2
  cartões por episódio**, nunca como troca do v1 — o lote 007–011 testa o
  gancho, e visual junto seria uma segunda variável.
- **Layout no gancho não quebra a variável do lote:** o 008 pôs `digital-zoom` na
  cena 1 e `orbit` na cena 11. O texto do primeiro segundo continua igual ao do
  gancho aprovado; o layout só muda *como* o cartão entra (e o zoom deixa o
  texto legível em 0,10 s, contra ~0,6 s do v1).
- **Áudio: medir o cru antes de escolher o sinal.** O Piper não tem volume
  previsível: 006 saiu em −22,17 LUFS, 007 em −15,2 (por isso o pós foi −4,4 dB)
  e 008 em −15,7 (pós +4,1 dB). Medir `voz_raw.wav` e `final_raw.mp4` com
  `ebur128` e ler o **true peak**, nunca o pico de amostra.
- Alerta em `qa.md`: cena 2 é cartão estático de 6,57 s. Só dividir se a retenção do 003 pedir.
- `docs/PLANO.md` (correção da fonte 004 → Comissão NZ, Apia) commitado junto com o 004.
- **Gate 2 usa janela fixa de 48 h** para “% média assistida”. A duração média
  cai com o tempo (002: 87,0% → 76,1% em um dia), então medir em datas
  diferentes compara públicos diferentes.
- **Público medido (26/10):** 82,1% com 55+, 0% abaixo de 45, 78,2% masculino,
  94,7% celular, Brasil só **49,2%**. Ver `biblioteca/publico.md`. Registrar a
  mesma leitura no 005: se repetir em dois vídeos, é o canal; se não, é o vídeo.
- **Studio Análises:** abre em branco / “Oops” na primeira carga. Funciona assim: abrir
  `.../video/<id>/analytics/tab-overview/period-default?hl=en&cb=<timestamp>`, esperar e
  **recarregar até o card “Audience retention” aparecer** (1–3 tentativas). O que o card
  entrega: “Stayed to watch”, “Average view duration” e views. **% média assistida =
  duração média ÷ 46 s** (validado pelo 002: 0:40 → 87,0%).
  **A aba Content (tabela por vídeo) e a lista de vídeos nunca carregam** — puxar
  vídeo a vídeo. **Reach/Audience** só abrem clicando no `TP-YT-PAPER-TAB`, não por URL.

## Compactação

- Compactar **entre etapas**, não no meio: `opencode api post /api/session/<id>/compact --data '{}'`.
- Antes de compactar: atualizar este arquivo e commitar o que for durável.
- Saídas grandes (frames, logs, HTML) vão para arquivo; no chat, só o resumo.

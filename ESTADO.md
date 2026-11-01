# ESTADO — retomada por etapa

> **Arquivo de instrução do OpenCode** (`opencode.jsonc`). Atualizar a **cada passo**, não a cada etapa.
> Depois de uma compactação, a versão atual deste arquivo é relida do disco e vira a baseline da sessão.
> Memória longa continua em `MEMORIA.md`; aqui só o suficiente para retomar sem reler nada.

**Atualizado:** 2026-10-31 · **Gate 2 PASSA (3 de 6)** · **007 Somerton: QA PASS, aguardando aprovação humana** · **17 layouts: LAB 003 QA PASS, aguardando aprovação** · canal único · `sombra-direta` pausado

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

**Fora da fila, pronto e parado:** a **biblioteca de 17 estilos de cena**
(`templates/layouts/`) passou o LAB 003 com QA PASS em 31/10. É aditiva: sem
`tipo` no roteiro, o HTML sai idêntico ao v1 (007 conferido por SHA-256). Não
entra em episódio antes da aprovação.

## Biblioteca de layouts — 17 estilos (31/10, aguardando aprovação)

| Etapa | Estado |
|---|---|
| Biblioteca | **pronta** — `templates/layouts/{registro.json,layouts.css,layouts.js,README.md}`; 4 famílias sobre o cartão do v1 |
| Gerador | **pronto** — `"tipo"` por cena, inlining no `index.html`, validação (tipo, `itens`/`valores`, asset sem crédito, `zoom-through` no fim) |
| Contrato | **pronto** — `check-contrato.ps1` §2b (data-layout, `window.__layouts`, `layout-<tipo>`, arquivo de asset) |
| Retrocompatível | **provado** — 007 regerado sem `tipo`: `index.html` com o **mesmo SHA-256** |
| LAB 003 | **QA PASS** — `laboratorio/003-layouts-17/`: 17 cenas, 45,077 s, 3m06s de render, −15,0 LUFS, TP −2,5, 1352 frames; SHA-256 `59D282C2…5E9AF7` |
| Frames | **conferidos** — 17 frames do `final.mp4` + `contact-1.png`/`contact-2.png`; nenhum título em 3 linhas |
| Aprovação | **pendente** — nada entra em episódio antes |

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

Plano completo em `docs/PLANO.md` §“Fase 3 — lote 007–011”. **007 concluído em
31/10 (QA PASS, publicação pronta, aguardando aprovação); 008–011 nada
produzido.** Canal único: Dossiê 45 (`sombra-direta` e `mente-obscura` pausados).

**A variável do lote é o gancho:** o primeiro segundo abre com ação/consequência,
nunca com contexto. Tudo o mais fica igual ao 005 (45 s, **12 cartões**, ≤5 s,
v1, Piper, 1080×1920/30 fps). **Hipótese:** mediana de “ficaram” ≥ 46,5% e de
`% média` > 54,3%. **Cadência fixa:** 1/dia, 19h de Brasília, seg–sex.

| # | Slug | Tema | Gancho | Estado |
|---|---|---|---|---|
| 007 | `007-homem-de-somerton` | Homem de Somerton (1948) | “Um homem morto na praia. Um código costurado na roupa.” | **QA PASS 31/10 — publicação pronta, aguardando aprovação** |
| 008 | `008-max-headroom` | Invasão Max Headroom (1987) | “Dois canais de TV foram invadidos ao vivo. Ninguém foi preso.” | nada produzido |
| 009 | `009-mascaras-de-chumbo` | Máscaras de chumbo (1966) | “Dois homens mortos no morro. Máscaras de chumbo. Nenhuma marca.” | nada produzido |
| 010 | `010-carroll-a-deering` | Carroll A. Deering (1921) | “O navio apareceu vazio. E a comida ainda estava na mesa.” | nada produzido |
| 011 | `011-ss-baychimo` | SS Baychimo (1931–1969) | “Abandonaram o navio no gelo. Ele navegou 38 anos sozinho.” | nada produzido |

**Próximo comando:** o **007 está pronto para publicar** — falta escuta humana
dos nomes e **aprovação explícita** (“publique” conta; “conclua” não). Publicado
o 007, começar o **008** com `briefing.md` (fontes numeradas), gancho e
`roteiro.json`. Cadência: 1/dia, 19h, seg–sex.

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

- **007** — escutar os nomes (Somerton, Adelaide, Tamám Shud, Omar Caiame,
  Glenelg), obter **aprovação explícita** e publicar. 31/10 é sábado; próxima
  janela da cadência (seg–sex): **segunda 02/11 às 19h**. Retenção 48 h: **D+2
  da data de publicação**.
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

**Próximo comando (o que decidir agora):** o gate está fechado, então a fila é
**decisão**, não produção. Em ordem:
1. **Aprovar o LAB 003** — quais dos 17 estilos entram (ou cortar). Aprovado,
   o uso é 1–2 por episódio (gancho + cartão de dado), nunca trocar o v1
   inteiro no meio do lote 007–011, que testa o **gancho**.
2. **Aprovar ou não** o `sombra-direta` 001 (`QA PASS`, cópia pronta) — precisa de
   conta Google separada, que ainda não existe.
3. **Escolher o modelo do canal 2** (A/B/C, adiado de propósito para depois do
   gate). Com 005 acima de 50% e 006 no limite por gancho, a leitura favorece
   testar **gancho/visual** antes de nicho.
4. Só depois: LAB 002 (layouts) e o A/B de v2.

## Bloqueios e regras vivas

- **Aprovação é explícita por vídeo.** “publique” conta; “conclua” ou “vamos aguardar” não.
- Um render por vez; 1080×1920, 30 fps, H.264 + AAC.
- **v1 não está mais congelado pelo Gate 2** (fechado em 29/10), mas continua
  sendo a referência: mudança de fonte/efeito/imagem entra como **uma variável**
  em **canal separado**, nunca direto no Dossiê 45.
- **Os 17 layouts não entram no Dossiê 45** antes da aprovação do LAB 003; e,
  aprovados, entram como **1–2 cartões por episódio**, não como troca do v1 —
  o lote 007–011 testa o gancho.
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

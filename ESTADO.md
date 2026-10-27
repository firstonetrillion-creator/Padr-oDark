# ESTADO — retomada por etapa

> **Arquivo de instrução do OpenCode** (`opencode.jsonc`). Atualizar a **cada passo**, não a cada etapa.
> Depois de uma compactação, a versão atual deste arquivo é relida do disco e vira a baseline da sessão.
> Memória longa continua em `MEMORIA.md`; aqui só o suficiente para retomar sem reler nada.

**Atualizado:** 2026-10-27 · **Sessão anterior:** 006 publicado; **6 de 6 no ar** · método de canais criado

## Onde estamos

Fase 2 **concluída: 6/6 publicados** (001–006). Os dois últimos subiram no mesmo
dia (005 e 006, 27/10), então as duas janelas de 48 h fecham juntas em **29/10** —
é quando o **Gate 2** fica decidível. Nada novo em produção até lá.

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

**Próximo comando:** em **29/10**, ler a retenção de 48 h de **005 e 006** no
Studio (vídeo a vídeo, `.../analytics/tab-overview/period-default?hl=en&cb=<ts>`,
recarregando até o card aparecer), preencher `biblioteca/publicados.csv` **e**
`canais/dossie45/metricas.csv` e fechar o **Gate 2** — basta **um** dos dois
passar de 50% de % média assistida. Antes disso **não se abre canal novo**: a
escolha do modelo (A/B/C) é do usuário, não do agente.

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
PT-BR); B = mesmo nicho + 60 s; C = mesmo nicho + som audível. Escolher um é
decisão do usuário e vai para `docs/DECISOES.md`.

## Esperando (nada a fazer até as datas)

- **2026-10-29** — retenção de 48 h de **005** (`wlPEoYErlZQ`) e **006**
  (`K_sgJjNHg84`), as duas no mesmo dia. Uma delas fechando
  acima de 50% de % média assistida fecha o **Gate 2**.
  - **005** é o primeiro vídeo inteiramente gerado por JSON, 12 cenas, nenhuma
    acima de 5 s: testa a regra “sem cartão parado depois do gancho”.
  - **006** tem 14 cenas, voz por cena e o mesmo v1 visual: testa se o problema
    do miolo era só o cartão estático ou algo mais.
- ~~**2026-10-26** — retenção de 48 h do **004**~~ **feito**: painel relido com
  login em 26/10. Falta só o `Todos.csv` de curva (aba Content do Studio não
  carrega). Ver `episodios/004-mv-joyita/retencao.md`.
- Leitura do 003: gancho melhorou (3 s e 10 s acima do 002), **mas o fim caiu**
  (36,1% vs 42,2%): slide de −32,4 p.p. entre 10 s e 44,5 s. Hipótese: a
  explicação do CROATOAN entregue cedo demais.

## Bloqueios e regras vivas

- **Aprovação é explícita por vídeo.** “publique” conta; “conclua” ou “vamos aguardar” não.
- Um render por vez; 1080×1920, 30 fps, H.264 + AAC.
- v1 congelado até o Gate 2: sem fonte/efeito novo.
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

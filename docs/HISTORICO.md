# HISTORICO — Padrao-Dark

> Linha do tempo do que foi **entregue**, com data, evidência e decisão.
> Não é um diário: é o registro de marcos para uma sessão nova saber o que já existe.
> Mais recente no topo. Última atualização: **2026-10-24**.

## 2026-10-25 — 004 MV Joyita: retenção de 24 h

**Entregue**
- Export de 24 h em `episodios/004-mv-joyita/retencao-24h.csv`;
  `retention.py` rodado e `retencao.md` criado.
- **1.066 views** e 21 likes em 24 h (~3× o total do 003 em 48 h).
- **3 s = 90,9%** (PASS), **10 s = 43,4%** (**abaixo** da meta de 45%),
  fim **17,3%**.
- Painel do Studio: ficaram **53,4%**, duração média **0:21**,
  **porcentagem visualizada média 45,7%**, Shorts feed 98,9%.
- **Contraste com o 003:** “ficaram para assistir” é maior (53,4% vs 52,6%),
  mas a duração média caiu pela metade (0:40 → 0:21). O problema é o **miolo**,
  não o gancho.
- Quedas concentradas em **4,0–8,6 s**, dentro da cena 2 — o cartão estático de
  6,57 s com data/origem/destino/número, que estava marcado como alerta no
  `qa.md`.

**Decisão**
- O gancho de clique é forte (views altas, 3 s alto); a **entrega após o gancho**
  é o gargalo.
- Regra nova para 005/006: **nunca um cartão parado de contexto depois do
  gancho**; contexto em ≤2 s ou colado a uma consequência; um dado por cartão;
  fecho com consequência, não resumo.
- 48 h do 004 serão medidas em 26/10; a linha em `publicados.csv` fica `n/d`
  até lá (a coluna é de 48 h).

**Evidência**
- `retencao-24h.csv`, `retencao.md`, `qa.md` (alerta da cena 2),
  `biblioteca/publicados.csv`.

## 2026-10-25 — 003 Roanoke: retenção de 48 h

**Entregue**
- Export “Todos” do Studio (retenção absoluta) salvo em
  `episodios/003-roanoke/retencao.csv`; `retention.py --duration 45` rodado.
- **370 views**, **+1 inscrito**, 1,96 h de watch time; 41 impressões de
  miniatura com CTR 0% (o feed de Shorts não conta como impressão).
- **3 s = 92,7%** (meta ≥70) e **10 s = 68,5%** (meta ≥45): **PASS** nas duas.
  Fim da curva: **36,1%**.
- Painel do Studio (mesmo dia, com retry): ficaram **52,6%**, duração média
  **0:40**, **porcentagem visualizada média 87,0%**, Shorts feed 92,2%.
- `retencao.md` criado; linha do 003 em `publicados.csv` com views, 3 s e 10 s.
- Diagnóstico: **slide** de −32,4 p.p. entre 10 s e 44,5 s, não uma queda única.
  As maiores perdas (4,5–8,1 s) estão no trecho que entrega CROATOAN e o explica
  na mesma cena.

**Decisão**
- O ajuste de gancho do Gate 1 **funcionou**: 003 supera o 002 em 3 s e em 10 s.
- A perda está no miolo/fim: reter a explicação para depois de uma consequência
  e não gastar o fecho resumindo o que o vídeo já disse. Aplicar no 005.

**Evidência**
- `episodios/003-roanoke/retencao.csv`, `retencao.md`, `analytics/`
  (views por dia e resumo de conteúdo), `biblioteca/publicados.csv`.

## 2026-10-24 — 004 MV Joyita: publicado

**Entregue**
- Publicado no YouTube Shorts: https://youtube.com/shorts/rlSArCY3bH0
- Cópia de upload `004-mv-joyita_shorts_v1.mp4` conferida por SHA-256
  (`406906CE…`, idêntico ao `final.mp4`).
- Título `MV Joyita: o barco que não afundava` (35 caracteres); descrição com
  fontes; 5 hashtags; capa `capa.png`.
- Studio: **Público**, **não é para crianças**, **AI use = Yes**, sem
  promoção paga. Copyright: nenhum problema.
- Vitrine conferida: `yt-dlp` sem cookies (`availability=public`,
  `age_limit=0`, `duration=45`) e página pública com o selo **IA** visível
  ao lado do título.
- `publicados.csv` atualizado; tag `ep-004-publicado`.

**Decisão**
- Aprovação humana registrada em 24/10/2026 (“aprovado”).

**Evidência**
- URL acima, `publicacao.md`, `qa.md` (QA PASS), `004-mv-joyita_shorts_v1.mp4`.

## 2026-10-23 — 004 MV Joyita: render e QA técnico

**Entregue**
- Cena 6 corrigida: o h1 quebrava em “CARGUEIRO O / ACHOU.”; agora tem
  **4 linhas explícitas** (`CINCO SEMANAS / DEPOIS, UM / CARGUEIRO / O ACHOU.`).
  `qa-frames/frame-06.png` e `contact.png` regerados.
- Render segmentado **5×300 frames**, 1 worker, low-memory: **1350/1350 frames,
  0 retries, 4 reciclagens de browser**, 3m16s; `final_raw.mp4` **45,000 s**,
  **−21,64 LUFS**, TP **−7,39 dBFS**.
- Normalização **+6,5 dB** + `alimiter=limit=0.85:level=disabled`: `final.mp4`
  **45,013 s**, **3.652.954 bytes**, **−15,16 LUFS**, TP **−1,42 dBFS**.
  `qa.ps1`: **QA PASS**.
- QA visual do render em `qa-final/` (14 frames + contact): cena 6 em 4 linhas,
  fecho em 2 linhas, sem overflow nem fantasma.
- Capa `capa.png` extraída em **4,0 s** (“25 PESSOAS / NENHUM SINAL”).
- `qa.md` escrito; SHA-256 do `final.mp4` `406906CE…`.
- `hyperframes` (shim `.ps1`) é bloqueado pela execution policy; comandos
  canônicos passaram a usar **`hyperframes.cmd`** em `AGENTS.md` e `MEMORIA.md`.

**Decisão**
- O 004 fica **pronto para aprovação humana**; não publica sem escuta de
  “Joyita”, “Tokelau”, “Apia” e sem “Aprovado — publicar”.
- Alerta registrado em `qa.md`: a cena 2 é um cartão estático de 6,57 s
  (3,03–9,60 s). Só dividir se a retenção do 003 pedir.

**Evidência**
- `episodios/004-mv-joyita/final.mp4`, `final_raw.mp4`, `qa.md`, `status.md`,
  `qa-final/`, `capa.png`, `render.log`.

## 2026-10-23 — Memória de sessão: `ESTADO.md` como instrução

**Entregue**
- Diagnóstico: a compactação do OpenCode mantém ~15k tokens recentes + resumo;
  o que existia só no chat se perde. O checkpoint anterior perdeu o meio da etapa
  do 004 (estado da cena 6 e do render).
- `opencode.jsonc` na **raiz do workspace** (config não é descoberta em subpasta):
  `instructions: ["Padrao-Dark/ESTADO.md", "Padrao-Dark/AGENTS.md"]`,
  `compaction.keep.tokens: 30000`, `compaction.buffer: 24000`.
- `Padrao-Dark/ESTADO.md`: uma tela, atualizada **a cada passo**. Depois de cada
  compactação a versão em disco é relida e vira baseline da sessão.
- `AGENTS.md`: nova camada “Passo” na tabela de memória + regra de compactar
  **entre etapas**, nunca no meio de um render.

**Decisão**
- Memória operacional passa a ser por passo (arquivo), não por conversa.
- `MEMORIA.md` continua sendo a memória longa; `ESTADO.md` é o ponteiro curto.

**Evidência**
- `opencode.jsonc`, `Padrao-Dark/ESTADO.md`, `Padrao-Dark/AGENTS.md`, `MEMORIA.md` §5.

## 2026-10-23 — 003 Roanoke publicado no YouTube Shorts

**Entregue**
- Aprovação humana explícita do `final.mp4` em 23/10/2026.
- Cópia de publicação `003-roanoke_shorts_v1.mp4`, idêntica ao `final.mp4`
  (SHA-256 `D7C9B676…`); capa `capa.png` extraída em **4,0 s**, 1080×1920.
- Título `Roanoke: a colônia que sumiu e deixou uma palavra` (49 caracteres;
  lint **80/100**); descrição com fontes (NPS e Quinn), ressalva 117–118 e
  hashtags `#misterio #roanoke #croatoan #coloniaperdida #dossie45`.
- **Publicado como Público:** https://youtube.com/shorts/8ptxqKGe4Bk.
- **AI use = Yes** no Studio; selo **AI** visível na página pública.
- Metadados públicos conferidos via `yt-dlp` sem cookies:
  `availability=public`, `age_limit=0`, `duration=45`.
- Linha adicionada em `biblioteca/publicados.csv`; retenção de 48 h agendada
  para **25/10/2026**.

**Decisão**
- Fase 2 com **3/6 publicados** (001, 002 e 003).
- Manter o v1 e iniciar o **004 MV Joyita**; 005 Voo 19 e 006 Passo Dyatlov na
  sequência.

**Evidência**
- https://youtube.com/shorts/8ptxqKGe4Bk
- `episodios/003-roanoke/publicacao.md`, `qa.md`, `status.md`;
  `biblioteca/publicados.csv`.

## 2026-10-23 — 003 Roanoke: render, QA e correção de marca

**Entregue**
- Render segmentado **5×300 frames**, 1 worker, low-memory; `final_raw.mp4`
  **45,000 s**, **−21,9 LUFS**, true peak **−7,2 dBFS**.
- Normalização **+6,5 dB** + `alimiter=limit=0.85:level=disabled`;
  `final.mp4` **45,013 s**, **3.557.345 bytes**, **−15,4 LUFS**, true peak
  **−1,4 dBFS**. O `qa.ps1` lê **−15,5 LUFS** por arredondamento.
- `qa.ps1`: **QA PASS** (duração, resolução, fps, áudio, loudness, sem preto
  inesperado).
- 14 frames em `qa-final/` (`frame-01.png` … `frame-14.png`); frame 1,
  CROATOAN, twist, fecho e fade conferidos sem overflow, ghosting ou marca
  errada.
- `qa.md` criado; `status.md`, `MEMORIA.md` e `docs/PLANO.md` atualizados.

**Correção**
- O primeiro render ainda exibia a marca antiga `ARQUIVO NOTURNO`. O
  `index.html` foi corrigido para `DOSSIÊ 45` e o vídeo foi renderizado de
  novo.
- Os artefatos do render antigo ficaram preservados como
  `final_raw_brand-antigo.mp4`, `final_brand-antigo.mp4`,
  `qa-frames-brand-antigo/`, `qa-final-brand-antigo/`,
  `renders-brand-antigo/` e `.hyperframes-brand-antigo/`.

**Decisão**
- Manter o visual v1; nenhuma fonte ou efeito novo antes do Gate 2.
- **Não publicar** sem aprovação humana explícita do `final.mp4`.
- Próxima etapa: aprovação; depois cópia `003-roanoke_shorts_v1.mp4`,
  `capa.png`, `publicacao.md`, publicação e retenção em 48 h.

**Evidência**
- `episodios/003-roanoke/final.mp4`; `final_raw.mp4`; `qa.md`;
  `qa-final/`; `status.md`; `index.html`; `scripts/qa.ps1`.

## 2026-10-23 — 003 Roanoke: voz, transcrição e composição v1

**Entregue**
- `narracao_tts.txt` com **`Croatoun`** nas duas ocorrências; a tela usa
  **`CROATOAN`** e `narracao.txt` usa **`Croatoan`**.
- Take selecionado: `voz_raw.wav` **44,69 s** (`length_scale` 1,00;
  `noise_scale` 0,65; `noise_w` 0,80) → `voz.wav` **45,00 s**, 48 kHz
  estéreo, **−21,99 LUFS**, pico **−7,22 dB**.
- Cadeia de voz: highpass 75 Hz, de-esser 0,25, EQ 250 Hz −1,5 dB /
  3,5 kHz +3 dB / 8 kHz +1 dB, compressor −18 dB 3:1, limitador 0,95,
  `adelay=260`, `apad`, `-t 45`.
- `drone.wav` de 45 s a partir do bed do 002, com fade-in de 1 s e
  fade-out de 42–45 s.
- `transcricao.json` com timestamps por palavra.
- `index.html` remapeado para 13 cenas: 0–3,75; 3,75–6,50; 6,50–8,60;
  8,60–14,20; 14,20–18,20; 18,20–21,20; 21,20–24,80; 24,80–29,00;
  29,00–31,40; 31,40–34,40; 34,40–37,40; 37,40–40,60; 40,60–45,00 s.
- `check-contrato.ps1`: **OK, 0 avisos**. QA visual em `qa-frames/`
  (frame 1, 13 cenas, fade), sem overflow; CROATOAN visível em 3,75 s.
- `status.md` e `roteiro.md` atualizados com tempos reais e nota de
  pronúncia. O ASR transcreveu “Croaton” nas duas ocorrências; os nomes
  não são usados como texto final.

**Decisão**
- Usar `Croatoun` apenas no TTS; não alterar a tela nem o texto canônico.
- Manter o visual v1; nenhuma fonte ou efeito novo antes do Gate 2.
- Próxima etapa: render segmentado, normalizar `final_raw.mp4` para
  ~−15,3 LUFS (~+6,5 dB), QA técnico, aprovação humana e publicação.

**Evidência**
- `episodios/003-roanoke/status.md`; `voz_raw.wav`; `voz.wav`;
  `transcricao.json`; `index.html`; `qa-frames/`; `check-contrato.ps1`.

## 2026-10-23 — 003 Roanoke: roteiro v1 e narração escritos

**Entregue**
- Gancho revisado e aprovado: **“117 pessoas sumiram. Nenhum corpo. Uma
  palavra.”** A versão anterior repetia o título.
- `episodios/003-roanoke/roteiro.md`: **113 palavras faladas**, 13 cenas,
  estrutura gancho → CROATOAN → correção → contexto → evidência → twist →
  fecho.
- `episodios/003-roanoke/narracao.txt` criado com o texto exato para TTS.
- `status.md` e `gancho.md` atualizados; `index.html` ainda está no
  texto-exemplo do 001 e será remapeado depois da voz.

**Decisão**
- CROATOAN entra na **cena 2**, antes de geografia/contexto, para pagar o
  gancho imediatamente.
- O número **117** é usado com a variação **117–118** documentada; “nenhum
  corpo” significa ausência no sítio, não prova de morte de todos.
- Próxima etapa: TTS + processamento para 45,00 s; depois transcrição e
  remapeamento do `index.html`.

**Evidência**
- `episodios/003-roanoke/roteiro.md`; `narracao.txt`; `gancho.md`;
  `status.md`; `briefing.md`.

## 2026-10-23 — Gate 1 verificado: 002 passa, 001 fica sem curva

**Entregue**
- CSV de retenção do 002 exportado e salvo em
  `episodios/002-mary-celeste/retencao.csv`; `retencao.md` criado.
- `episodios/001-faroleiros/retencao.csv` salvo (vazio) e `retencao.md`
  criado com a leitura possível.
- `biblioteca/publicados.csv` atualizado com views, 3 s e retenção média.
- `retention.py` corrigido para normalizar retenção absoluta (>100%) do
  export avançado do Studio.

**Números**
- **002:** 234 views; 103 engaged; 1,2 h; 0:40; 48,3% ficaram; 87,0% de
  retenção média; **3 s = 91,6%**, **10 s = 61,8%**.
- **001:** 31 views; 9 engaged; 0,0 h; 0:15; 24,3% ficaram; 33,3% de
  retenção média; sem curva de 3 s/10 s.

**Decisão**
- Manter o formato v1, sem antecipar o visual v2.
- **003 autorizado**: revisar o gancho para acrescentar informação nova
  (“Nenhum corpo”) e entregar CROATOAN na cena 2.

**Evidência**
- `episodios/002-mary-celeste/retencao.md`;
  `episodios/001-faroleiros/retencao.md`;
  `biblioteca/publicados.csv`; `tools/youtube-agent-skill/yt-retention/retention.py`.

## 2026-10-22 — Backlog visual v2 registrado

**Entregue**
- `docs/PLANO.md` ganhou a seção **Melhorias visuais — backlog
  pós-validação**.
- Direção registrada: layouts múltiplos, tipografia como imagem, textura,
  provas visuais, movimento intencional, sound design e key art.
- `MEMORIA.md` §3.6 aponta para o backlog e para a regra de não iniciar.

**Decisão**
- Primeiro fechar os 6 vídeos e o Gate 2; depois testar o v2 em **1 vídeo
  A/B**, comparando retenção — não por gosto.
- **003–006 ficam no formato v1** para não contaminar a comparação.
- ReelMimic, WebGL/Three.js, OpenMontage e automação de publicação ficam
  fora do MVP até o gate 3.

**Evidência**
- `docs/PLANO.md` §Melhorias visuais; `MEMORIA.md` §3.6.

## 2026-10-21 — 003 Roanoke: briefing e gancho prontos

**Entregue**
- `episodios/003-roanoke/` criado a partir de `templates/misterio-45`
  (commit `ac25c1e`), com `index.html` e `status.md`.
- `briefing.md` com o fato central, a correção da lenda e fontes oficiais:
  NPS Fort Raleigh (1587, 1590 e teorias) e David Beers Quinn,
  *The Roanoke Voyages, 1584–1590* (Hakluyt Society, 1955).
- `gancho.md` com 10 opções; escolhido **“117 pessoas sumiram. Deixaram
  uma palavra.”** (fórmula 1 — O Dado).
- `status.md` marca briefing e gancho como prontos; roteiro pendente.

**Decisão**
- A produção final do 003 continua travada até o gate de retenção de
  001/002 em **23/10**; o roteiro pode ser adiantado.
- O número de colonos varia entre 117 e 118 nas páginas do NPS; o
  briefing registra a variação e usa 117 no gancho.

**Evidência**
- `episodios/003-roanoke/briefing.md`, `gancho.md` e `status.md`;
  `docs/PLANO.md` §Execução imediata.

## 2026-10-21 — Plano de execução 003–006 definido

**Entregue**
- `docs/PLANO.md` ganhou a seção **Execução imediata**, com o gate de
  retenção de 001/002 em **23/10/2026**.
- Fila provisória para os 4 vídeos restantes, com janela-alvo, fonte
  principal, ângulo e status de validação: Roanoke, MV Joyita, Voo 19 e
  Passo Dyatlov.
- Gate 2 definido para depois do 006: medir 48 h dos 6 e comparar com a
  meta de retenção média > 40% em 3 vídeos.
- `MEMORIA.md` agora aponta para o checklist e a fila em `docs/PLANO.md`.

**Decisão**
- A fila 003–006 só trava depois do gate de 23/10; a retenção pode exigir
  ajuste de gancho/ritmo antes de produzir os 4.
- Temas entram como **candidatos** até validação das fontes.

**Evidência**
- `docs/PLANO.md` §Execução imediata; `MEMORIA.md` §3.1.

## 2026-10-21 — 002 Mary Celeste publicado no YouTube Shorts

**Entregue**
- `002-mary-celeste` publicado no **YouTube Shorts** em 21/10/2026:
  https://youtube.com/shorts/n6dtveQguf4
- Título público: **Mary Celeste: o navio encontrado sem ninguém em 1872**
  (52 caracteres; lint 98/100).
- Descrição com contexto, fontes e 5 hashtags; capa `capa.png`; visibilidade
  **Público**.
- Aviso de conteúdo sintético marcado no Studio; selo **AI** visível na página.
- `biblioteca/publicados.csv` recebeu a linha do 002.
- `publicacao.md`, `status.md`, `qa.md` e `MEMORIA.md` atualizados para o
  estado publicado.
- Medição de 48 h agendada para **23/10/2026**, junto com o 001.

**Decisão**
- O 002 entra na validação de nicho como **2/6**; restam 4 vídeos de mistério.
- Manter o formato tipográfico v1 e o gate de aprovação humana para os
  próximos episódios.

**Evidência**
- URL pública acima; `episodios/002-mary-celeste/`; `biblioteca/publicados.csv`.

## 2026-10-21 — 002 Mary Celeste: produção fechada, QA PASS, aguardando aprovação

**Entregue**
- `episodios/002-mary-celeste/` criado a partir de `templates/misterio-45`
  (sha256 `0e0a2281`, commit `ad2747d`).
- `briefing.md`, `gancho.md` (fórmula 17 — A Alegação Impossível),
  `roteiro.md` (110 palavras de tela / 121 faladas), `shotlist.md`,
  `narracao.txt`, `voz_raw.wav` 43,04 s, `voz.wav` 45,00 s,
  `transcricao.json`, `index.html` com 13 cenas sincronizadas.
- `voz_raw.wav` com Piper `pt_BR-faber-medium`, `length_scale` 1,12;
  `voz.wav` com 0,6 s de respiro e pad para 45,00 s.
- `check-contrato.ps1`: **OK, 0 avisos** (29 invariantes).
- `final_raw.mp4` 45,0 s / 3,4 MB; `final.mp4` **45,013 s / 3,6 MB**,
  1080×1920, H.264, 30 fps, AAC 48 kHz estéreo.
- Loudness: −21,5 LUFS cru → **−15,4 LUFS** (+6,2 dB, limitador 0,85);
  pico **−1,5 dBFS**.
- Render segmentado: **3m00,9s**, 5 segmentos, 0 retries.
- `qa.ps1`: **QA PASS**. `qa.md` assinado; 15 frames em `qa-frames/`.
- Cópia de publicação: `002-mary-celeste_shorts_v1.mp4`; capa `capa.png`
  (frame em 1,5 s).
- `publicacao.md` com título de 52 chars, descrição, 5 hashtags, fontes
  e aviso de conteúdo sintético; lint de título **98/100**.

**Decisão**
- O gancho usa a lenda (“O navio foi encontrado sem ninguém. E com o
  jantar servido.”), marcada no frame 1 como **A LENDA**, e a cena 2
  corrige a invenção antes de qualquer afirmação factual.
- A data narrada é **5 de dezembro** (horário de bordo); o briefing
  registra a diferença em relação a 4 de dezembro (horário terrestre).
- “Nove chegaram vazios” descreve a carga em Gênova, não o estado no
  momento do achado.
- O 002 continua tipográfico v1; sem footage ou imagem de terceiros.

**Pendente na época** (resolvido na entrada acima)
- Aprovação humana do vídeo.
- Colar `identidade/descricao-canal.txt` no Studio e conferir a vitrine
  pública.
- Publicar, registrar em `biblioteca/publicados.csv` e medir retenção
  em 48 h.

**Evidência**
- `episodios/002-mary-celeste/` (textos, áudio, composição, `final.mp4`,
  `qa.md`, `qa-frames/`, `publicacao.md`).

## 2026-10-21 — Rebranding fechado: Dossiê 45, 9 shorts privados, descrição criada

**Entregue**
- Nome público **Dossiê 45** confirmado em `youtube.com/@Dossie45`.
- Os 9 shorts de psicologia foram privados; a aba Shorts mostra **1** vídeo
  público, o piloto `001-faroleiros`.
- Descrição do canal criada em `identidade/descricao-canal.txt` — 520
  caracteres, impessoal, com proposta, método, frequência e hashtags.
- `docs/REBRANDING.md`, `docs/IDENTIDADE.md`, `MEMORIA.md` e `docs/PLANO.md`
  atualizados com o estado real do canal.

**Pendente**
- Colar a descrição no Studio e salvar palavras-chave/país.
- Conferir em janela anônima: nome novo, bio nova e 1 Short de mistério.

**Decisão**
- Só publicar o 002 depois de colar a descrição e conferir a vitrine pública.

## 2026-10-21 — youtube-agent-skill adotado seletivamente; auditoria do rebranding

**Entregue**
- Vendor MIT de `Jakeschincariol/youtube-agent-skill` no commit `a2feb21` em
  `tools/youtube-agent-skill/`, com `LICENSE` e `ORIGEM.md`.
- `retention.py` patchado para Shorts: 3 s e 10 s, 30 s como legado, correção
  do eixo de 45 s, interpolação e transcrição SRT/VTT/JSON.
- `hooks.json` mantido intacto; checklist PT-BR em `docs/GANCHOS-21.md`.
- `title.py` adaptado para PT-BR: stopwords, termos vagos, nome próprio e
  normalização Unicode.
- `scripts/test_youtube_agent.py`: **9 testes PASS** (retenção em segundos,
  percentual, CSV de 45 s sem cabeçalho, transcrição, lint PT-BR e hooks).
- Skills atualizadas: `gancho` aponta para as 21 fórmulas; `publicacao` roda o
  lint de título; nova skill `retencao` para as 48 h.

**Auditoria do rebranding (verificação pública em 21/10/2026 — estado na época; resolvido na entrada acima)**
- Avatar e banner **estão no ar**: avatar 900×900 e banner recortado em
  2048×339; o texto principal e o subtítulo cabem na área segura.
- Naquele momento, a página pública ainda mostrava o nome **`Dossie45`** (sem
  acento/espaço), descrição vazia e **10 shorts** na aba Shorts. O nome foi
  corrigido e os 9 shorts antigos foram privados na sequência.
- Antes do 002: colar a descrição e conferir a vitrine pública.

**Decisão**
- Adotar `yt-retention`, `hooks.json` e `yt-title` agora.
- Adiar `yt-viral` e `yt-audit` para depois dos 6 vídeos; documentado em
  `docs/PLANO.md` e `docs/DECISOES.md`.
- Não usar `hookscore.py` em PT-BR: heurística em inglês, sem calibração local.

**Evidência**
- `tools/youtube-agent-skill/`; `docs/GANCHOS-21.md`; `scripts/test_youtube_agent.py`;
  `docs/PLANO.md`; `docs/DECISOES.md`.

## 2026-10-21 — Handle @Dossie45 no ar; identidade visual gerada

**Entregue**
- Canal agora responde em `youtube.com/@Dossie45` — mesmo channel ID do piloto (`UCwgP68Uen2KoIh2R-j231Yw`), verificado em 21/10.
- `identidade/banner.png` (2048×1152, texto dentro da área segura 1235×338) e `identidade/avatar.png` (800×800), gerados por Chrome headless a partir de HTML editável, na paleta e na Georgia do template.
- `docs/REBRANDING.md` com estado real do canal, textos prontos e ordem de execução.

**Pendente na época** (estado atual na entrada acima)
- Nome de exibição estava `Dossie45`; trocar para **Dossiê 45**.
- Descrição, palavras-chave, país e links ainda vazios.
- Avatar/banner já no ar; faltava deslistar os 9 shorts de psicologia.

**Decisão**
- Marca de tela passa a ser **DOSSIÊ 45** a partir do 002; o 001 não é re-renderizado.

## 2026-10-21 — Baseline versionado e contrato testável

**Entregue**
- Repositório git iniciado em `Padrao-Dark` (`main`, commit `782df62`, 59 arquivos de texto/código, tag `ep-001-publicado`).
- `.gitignore` deixa fora `.venv/` (415 MB), mídia (123 MB) e `qa-frames/`; **nada foi apagado do disco**. `core.autocrlf false`.
- `scripts/check-contrato.ps1`: 29 invariantes antes do render (stage, cenas, tempos, CSS por cena, áudio com duração real via `ffprobe`, `autoAlpha`, `window.__timelines`). Validado no `001`: 29 PASS, 0 avisos.
- `scripts/novo-episodio.ps1`: cria episódio do template, troca `data-composition-id`, chave da timeline, dossiê e título, grava `.template-version` (sha256 + commit) e `status.md`. Testado com slug descartável; pasta de teste removida.
- Documentação: `docs/ARQUITETURA.md` §6/§7, `scripts/README.md`, `docs/DECISOES.md` (graphify, claude-mem, git).

**Decisão**
- Git entrou por **rollback e drift de template**, não por causa do graphify (que só usa git no hook opcional).
- graphify segue adiado para o corpus de docs/episódios; claude-mem não será instalado agora (detalhes em `docs/DECISOES.md`).
- Próximo passo segue sendo o rebranding e o vídeo 002 — ferramenta não é o gargalo.

## 2026-10-21 — Validação de nicho concluída; Mistério/Arquivo é a âncora

**Entregue**
- Coleta completa: **48 shorts/14 canais** de Mistério/Arquivo e **50/17** de Psicologia sombria, canais de 100–500 mil inscritos.
- Mistério: mediana de views/inscrito por canal **0,10**; 3 canais ≥1,0 (Pequeno Contexto 1,50; Penumbroo 1,04; Crimes que Marcaram 1,02); mediana de views 2.075.
- Psicologia: **0,06**; nenhum canal ≥0,5; mediana de views 1.428; like rate 6,95% vs 3,37% do mistério.
- Dados completos e tabelas em `logs/nicho-2026-10-21.json` e `docs/NICHO.md`.
- Auditoria do canal: Cod Mind Million tem 6 inscritos, 10 shorts, histórico de psicologia; o piloto de mistério tem 6 views.

**Decisão**
- **Mistério/Arquivo é o nicho âncora da Fase 2.**
- **Rebrandar o Cod Mind Million** para marca de arquivo/mistério — nome de trabalho **“Dossiê 45”** (handle `@Dossie45`, disponível na checagem). Arquivar/unlistar os 9 shorts de psicologia; manter o piloto.
- Validação com **6 vídeos de mistério** (piloto + 5), não 3+3, para não misturar nichos no mesmo canal. Psicologia fica como fallback em canal novo.
- Handle a confirmar no YouTube Studio; `@Dossie45` e `@ArquivoNoturno45` retornaram 404 (disponíveis na checagem), enquanto `@ArquivoNoturno`, `@SalaEscura`, `@Dossie404`, `@Canal3AM` e `@ORelatorio` estão ocupados.

**Evidência**
- `logs/nicho-2026-10-21.json`; `docs/NICHO.md`; `docs/DECISOES.md`; `docs/PLANO.md`.

## 2026-10-21 — Script de nicho implementado

**Entregue**
- `scripts/nicho.py`: coleta metadados de Shorts via `yt-dlp`, sem baixar vídeo.
- Descoberta por buscas PT-BR + aba `/shorts` dos canais; faixa de 100 a 500 mil inscritos para medir canais pequenos.
- Métricas: views, inscritos, views/inscrito, like, comentário, duração e data; mediana por canal e por short.
- Saídas: `logs/nicho-<data>.json` + seção em `docs/NICHO.md`; cache em `logs/nicho-cache/`.
- `scripts/README.md` documenta uso, limites e flags.
- Teste curto em `logs/nicho-test3.json` (6 shorts por nicho) validou a coleta e o relatório.

**Decisão**
- Usar `--extractor-args "youtube:player_client=android"` para evitar o bloqueio de bot em metadados de vídeo; sem cookies.
- Retenção real não entra: metadados só permitem proxies. A retenção real será lida no YouTube Studio.

**Concluído**
- Coleta completa: 48/50 shorts de Mistério e 50/50 de Psicologia; 243 chamadas ao `yt-dlp`; dados em `logs/nicho-2026-10-21.json` e `docs/NICHO.md`.
- Auditoria do canal Cod Mind Million registrada em `docs/NICHO.md` (6 inscritos, conteúdo de psicologia); decisão de marca tomada na entrada acima.

**Evidência**
- `scripts/nicho.py`; `scripts/README.md`; `logs/nicho-test3.json`.

## 2026-10-21 — Piloto 001 publicado

**Entregue**
- `001-faroleiros` publicado no **YouTube Shorts** em 21/10/2026: https://youtube.com/shorts/WKuNVjl3d5M
- Título confirmado via oEmbed: “Os três faroleiros que sumiram de um farol trancado”.
- Linha registrada em `biblioteca/publicados.csv` (métricas em branco até 48 h).
- `publicacao.md` e `status.md` atualizados com URL e data.

**Decisão**
- **Fase 2 iniciada.** Próximo: validação de nicho e produção dos 5 vídeos restantes.
- Medir métricas em **23/10/2026** (48 h).

**Evidência**
- URL pública acima; `episodios/001-faroleiros/publicacao.md`; `biblioteca/publicados.csv`.

## 2026-10-21 — Memória em duas camadas

**Entregue**
- `MEMORIA.md` — memória geral de retomada (estado, pendências, comandos, armadilhas).
- `docs/ARQUITETURA.md` — memória de código (contratos de cena, áudio, tempo, render, QA).
- `docs/HISTORICO.md` — este arquivo.
- `scripts/README.md` — o que cada script entrega e como usar.
- Cabeçalho de memória em `episodios/001-faroleiros/index.html`.
- `AGENTS.md` atualizado para ler `MEMORIA.md` primeiro e atualizar a memória ao fim de cada etapa.

**Decisão**
- Duas camadas explícitas: geral (`MEMORIA.md`) e código (`docs/ARQUITETURA.md` + `HISTORICO.md` + comentários).
- `codebase-memory-mcp` continua adiado até o primeiro vídeo publicado (RAM de 8 GB).

**Evidência**
- Arquivos acima no repositório.

## 2026-10-21 — Piloto 001 aprovado

**Entregue**
- `episodios/001-faroleiros/final.mp4`: **45,01 s, 3,3 MB, 1080×1920, 30 fps, H.264 + AAC 48 kHz estéreo, −15,6 LUFS**.
- `001-faroleiros_shorts_v1.mp4` (cópia de publicação) e `capa.png`.
- `qa.md`: QA técnico **PASS**; aprovação humana registrada (“ficou perfeito”).
- `publicacao.md`: título, descrição, hashtags, aviso de IA.
- `status.md`: todas as etapas do episódio fechadas.
- Render final em **3m18s** (standard, segmentado 5×300 frames, 0 retries).

**Correções que entraram no piloto**
- Ghosting: cada cena agora tem `autoAlpha` de entrada/saída na timeline; antes o texto da cena antiga ficava a ~3% de opacidade.
- Cena `s5b` (“A PORTA ESTAVA FECHADA.”) criada para a fala que estava sem imagem.
- `s8` corrigido para “O MAR DESTRUIU / PARTE DO / ANCORADOURO.” (fato mais preciso).
- Gancho `s1` reequebrado em 4 linhas (evitou “UM” sozinho).
- `s4` e `s11` com fontes 96 px e 80 px para quebra estável no render.
- `s1` começa em 0,0 s (sem flash preto no início).
- Áudio cru em −21,8 LUFS normalizado para −15,6 LUFS com ganho estático de +6,2 dB e limitador em −1,5 dBFS.

**Evidência**
- `episodios/001-faroleiros/qa.md`
- `episodios/001-faroleiros/qa-frames/` (frames por cena e frames do MP4 final)
- `logs/bench.json` (G0)

## 2026-10-21 — Template `misterio-45`

**Entregue**
- `templates/misterio-45/index.html` — composição validada, 13 cenas, áudio `voz`/`drone`, QA por `?t=`.
- `templates/misterio-45/gsap.min.js` — dependência local.
- `templates/misterio-45/README.md` — passo a passo: cópia, voz, transcrição, remapeamento de cenas, QA visual, render segmentado, normalização e publicação.
- `templates/misterio-45/beat-sheet.md` — 13 beats, tempos de referência, orçamento de 110–125 palavras e limites de linha.

**Decisão**
- O template parte da composição real do piloto (não de um esqueleto não testado). O texto de exemplo deve ser substituído; o README avisa.
- Áudio não vai no template: cada episódio gera `voz.wav` e `drone.wav`.

**Evidência**
- `templates/misterio-45/` (lint sem erros; apenas avisos de track densa e estrutura aninhada).

## 2026-10-20/21 — Piloto: voz, transcrição e composição

**Entregue**
- `narracao.txt` com 118 palavras.
- `voz_raw.wav` (41,45 s, Piper `pt_BR-faber-medium`, `length_scale` 1.28).
- `voz.wav` com 45,00 s (respiro + cauda).
- `drone.wav` de 45 s.
- `transcricao.json` com timestamps por palavra (faster-whisper `small`, PT).
- `index.html` com 13 cenas sincronizadas, tipografia Georgia, moldura, vinheta e rodapé de fonte.
- `shotlist.md` reescrito para o formato tipográfico real (o plano original previa fotos de stock, que não foram usadas).

**Decisão**
- Formato **type-only** no piloto: mais rápido, mais barato e adequado à máquina. Fotos/parallax ficam para a v2.
- Margem lateral de 120 px; rodapé a 190 px da base.
- Uma cena por frase ou par de frases curtas; 13 cenas em 45 s.

**Evidência**
- `episodios/001-faroleiros/` (todos os artefatos)
- `episodios/001-faroleiros/transcricao.json`

## 2026-10-20 — Render: falha e correção

**Problema**
- Primeiro render do piloto caiu em **1333/1350 frames** com `Protocol error (Page.captureScreenshot): Target closed` (memória acumulada do Chrome headless).

**Correção entregue**
- Captura segmentada: `HF_SEGMENTED_CAPTURE=true`, `HF_SEGMENT_FRAMES=300`, `HF_SEGMENT_BROWSER_RECYCLE=1`, `--workers 1 --low-memory-mode --protocol-timeout 600000 --resume`.
- Resultado: 5 segmentos, 0 retries, sem crash.
- Documentado na skill `render` e no template.

**Evidência**
- `episodios/001-faroleiros/status.md` (medições)
- `.opencode/skills/render/SKILL.md`

## 2026-10-20 — Gate G0

**Entregue**
- Benchmark de 45 s em 1080×1920 renderizado em **2m32,8s** (158,8 s incluindo doctor/probe).
- Gate **PASS** (meta: < 12 min).
- `logs/bench.json` com o resultado.

**Decisão**
- A máquina aguenta o formato; o gargalo é conteúdo, não render.

**Evidência**
- `logs/bench.json`
- `bench/bench-45.mp4`

## 2026-10-20 — Cérebro instalado

**Entregue**
- Node v22.23.3, npm 10.9.9, Git 2.56.0, FFmpeg/ffprobe 8.1.3.
- uv 0.13.4, Python 3.12.15 em `.venv`.
- Piper 1.8.0 + voz `pt_BR-faber-medium`.
- faster-whisper 1.2.1, yt-dlp 2026.8.19.
- HyperFrames 0.8.181 + Chrome Headless Shell 152.
- Instalação em espaço de usuário (`C:\Users\valentim\Tools`), sem admin.

**Correções de ambiente**
- DLLs do VC++ copiadas para `onnxruntime`/`.venv` (Piper/faster-whisper).
- `espeak-ng-data` copiado para caminho ASCII (`C:\Users\valentim\Tools\piper-data`), porque o Piper falha com “Padrão” acentuado.
- Patch no `faster_whisper/audio.py` (`av.open(..., mode="r")`) por incompatibilidade com PyAV 19.

**Decisão**
- Stack: HyperFrames (Apache 2.0) + Piper + faster-whisper + yt-dlp + FFmpeg.
- Sem WebGL/Three.js, Docker, WSL, Remotion ou Hermes3D nesta máquina.
- `codebase-memory-mcp` e OpenMontage adiados até depois do primeiro vídeo publicado.

**Evidência**
- `docs/STACK.md`
- `scripts/verify.ps1` (versões)
- `scripts/install-brain.ps1`

---

## Próximos marcos (ainda sem data)

- [x] Publicar `001-faroleiros` e registrar em `biblioteca/publicados.csv`.
- [x] Publicar `002-mary-celeste` (2/6) e registrar em `biblioteca/publicados.csv`.
- [ ] Escrever o script de validação de nicho (`yt-dlp`, 50 shorts/nicho, views por inscrito).
- [ ] Produzir e publicar os 4 vídeos restantes de validação.
- [ ] Medir retenção em 48 h e escolher o nicho âncora.
- [ ] Instalar `codebase-memory-mcp` após o primeiro vídeo publicado.

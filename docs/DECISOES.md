# Decisões de stack (ADR)

Data: 2026-10-21
Status: aceito para o MVP

Critérios de corte, nesta ordem:

1. Produz o vídeo?
2. Roda em 8 GB / 2 núcleos / sem GPU?
3. Licença permite uso comercial e venda de serviço?
4. Integra com OpenCode?
5. Está no caminho crítico dos 10 primeiros vídeos?

## Decisão

| Repositório | Veredito | Papel | Licença |
|---|---|---|---|
| heygen-com/hyperframes | **Adotado** | Render 9:16 e 16:9 | Apache 2.0 |
| DeusData/codebase-memory-mcp | **Adotado (fase 2)** | Memória do código do estúdio | MIT |
| yihui-dev/awesome-opus5-5-videos | **Adotado** | Biblioteca de ganchos e referências | MIT |
| lemomo-ai/lemo-opuscar | **Adotado só como documentação** | Direção de arte (`STYLE.md`, `DIRECTOR.md`) | MIT / CC BY 4.0 |
| calesthio/OpenMontage | **Adiado (fase 2)** | Pesquisa, roteiro, QA, Backlot | AGPLv3 |
| remotion-dev/remotion | **Descartado no MVP** | — | Licença própria |
| iamlukethedev/Hermes3D | **Descartado** | — | MIT |
| ruvnet/ruflo | **Descartado no MVP** | — | MIT |

## Justificativas

### HyperFrames — adotado
Render HTML/CSS/GSAP determinístico via Chrome headless + FFmpeg. Sem taxa por render, sem React, skill oficial para OpenCode. É o único motor que cabe no hardware e no orçamento.

### codebase-memory-mcp — adotado na fase 2
Binário nativo de 46 MB, MIT, sem runtime. Ajuda a navegar OpenMontage/HyperFrames sem queimar contexto. Não entra no caminho crítico do primeiro vídeo.

### awesome-opus5-5-videos — adotado
703 prompts em Canvas/SVG/GSAP/Three.js. Usar apenas o subconjunto **Canvas/SVG/GSAP**; ignorar Three.js/WebGL/GLSL (inviável na HD 620).

### lemo-opuscar — adotado como documentação
51 estilos com `STYLE.md`, mais `DIRECTOR.md` e `TECHNIQUE.md`. Não rodar a pipeline completa (1080p frame-a-frame levaria horas). Serve como biblioteca de direção.

### OpenMontage — adiado
O core Python é leve (sem torch), mas o `make setup` instala o `remotion-composer`. Para os 10 primeiros vídeos o gargalo é roteiro e render, não pesquisa. Licença AGPL: produzir vídeos é livre; **vender o sistema** exige abrir o código — o Kit deve conter nossos templates, não uma cópia do OpenMontage.

### Remotion — descartado
Licença gratuita só até 3 funcionários; peso de 500 MB–1 GB; redundante com HyperFrames. Revisitar apenas para cenas data-driven complexas ou render em Lambda.

### Hermes3D — descartado
Não produz vídeo. É um escritório 3D para agentes, com Next.js + Three.js + Phaser + backend (1,5–2,5 GB) e WebGL em iGPU. Zero impacto em retenção ou receita. Revisitar só como fachada comercial.

### ruflo — descartado
Orquestração de swarms para código; nosso pipeline é linear. Centenas de MCP tools, daemon e hooks competindo por RAM. Revisitar ao operar 3+ canais simultâneos.

## Lacunas preenchidas

| Necessidade | Ferramenta | Licença |
|---|---|---|
| Voz offline PT-BR | rhasspy/piper | MIT |
| Legendas com timestamp | SYSTRAN/faster-whisper | MIT |
| Pesquisa de nicho | yt-dlp/yt-dlp | Unlicense |
| Montagem/QA | FFmpeg | LGPL/GPL |

## Regras

- `yt-dlp` só para análise de metadados. Nunca reupload.
- Não instalar Docker, WSL, Hermes3D, ruflo full ou Lens 3D nesta máquina.
- Nenhum render em paralelo: um Chrome headless por vez.

## Memória do projeto — adotada em 2026-10-21

Duas camadas explícitas, para uma sessão nova retomar sem depender do histórico do chat:

| Camada | Arquivo | Papel |
|---|---|---|
| Geral | `MEMORIA.md` | estado, pendências, comandos, armadilhas, decisões travadas |
| Código | `docs/ARQUITETURA.md` | contratos de cena, áudio, tempo, render e QA |
| Entrega | `docs/HISTORICO.md` | linha do tempo com data, evidência e decisão |
| Scripts | `scripts/README.md` | o que cada script entrega e como usar |

`codebase-memory-mcp` continua **fase 2**: só depois do primeiro vídeo publicado, para não competir por RAM com o render. A documentação acima é a memória operacional até lá.

## Decisões do piloto 001

- **Formato type-only** na v1: sem fotos de stock, sem parallax, sem WebGL. O texto é a imagem. Reduz tempo, custo e risco na máquina.
- **Captura segmentada** como padrão nesta máquina: `HF_SEGMENT_FRAMES=300` + reciclagem do Chrome + `--resume`. O render único caía em ~1333/1350 frames por memória.
- **Ganho estático + limitador** no pós, em vez de `loudnorm` dinâmico: preserva a narração contínua sem bombeamento.
- **13 cenas** (não 12): a fala “a porta estava fechada” ganhou cena própria.
- **Margem de 120 px** e rodapé a 190 px da base para área segura de Shorts/TikTok/Reels.

## PI-Desktop — avaliado em 2026-10-21

Repositório: [`vastsa/PI-Desktop`](https://github.com/vastsa/PI-Desktop). Desktop workspace para agentes de código: Electron + host core em Rust + pi Agent Harness + plugins. LGPL-3.0, early preview 0.21.x, ~7,1 mil stars, 222 issues abertas; release 0.20.1 (13/10/2026) com portable Windows.

**Veredito: não adotar agora.** Reavaliar depois do primeiro vídeo publicado.

| Critério | Leitura |
|---|---|
| Produz vídeo? | Não. Não substitui HyperFrames, FFmpeg, Piper nem yt-dlp. |
| Resolve memória? | Já resolvemos com `MEMORIA.md` + `docs/ARQUITETURA.md` + `docs/HISTORICO.md`, sem custo de RAM. |
| Cabe em 8 GB? | Risco. Electron + runtime de agente + Chrome de render competem com o HyperFrames, que já estourou memória uma vez. Não medido. |
| Maturidade | Early preview, 222 issues abertas, histórico recente de perda de mensagens em sessão (corrigido). Não é base para produção contínua. |
| Migração | Alto custo: nosso fluxo é OpenCode (AGENTS.md, `.opencode/skills`, comandos). O PI-Desktop usa o runtime `pi`; importar sessões do OpenCode não migra skills nem automações. |
| Licença | LGPL-3.0 permite uso interno e venda de vídeos. Se um dia distribuirmos o app modificado num kit, revisar obrigações de código aberto. |
| Ganho único | Sessões persistentes, importação de sessões do OpenCode, MCP, subagentes e orquestração de workers. Útil em outro estágio, não no gargalo atual. |

**Quando reavaliar:** após o primeiro vídeo publicado e a validação de nicho. Teste seguro: baixar o **portable** do Windows, abrir uma **cópia** do projeto, medir RAM em repouso e durante um render curto; não migrar no meio de uma fase. Usos plausíveis no futuro: continuidade de sessões, hospedagem de MCP e painel de múltiplos workers na Fase 4.

## Hypit — avaliado em 2026-10-21

Repositório: [`hypit-ai/hypit`](https://github.com/hypit-ai/hypit). Framework TypeScript para agentes criarem vídeo a partir de uma linguagem declarativa (SVML), com compiler/runtime, captura HTML headless, FFmpeg, WhisperX, yt-dlp e componentes. v0.3.1, criado em 29/07/2026, ~24,5 mil stars, 2,7 mil forks, 53 issues abertas. Licença própria baseada em Apache 2.0, com condições.

**Veredito: usar como referência conceitual; não adotar como dependência do MVP.** Reavaliar depois dos 6 vídeos de validação, se precisarmos de motion graphics/B-roll, variantes em escala ou timeline editável.

| Critério | Leitura |
|---|---|
| Produz vídeo? | Sim, inclusive sem modelos generativos: `examples/semantic-composition` renderiza HTML/CSS/SVG + FFmpeg localmente. Mas é outro pipeline, concorrente do HyperFrames. |
| Encaixe no formato | Fraco para o “Mistério 45” type-only: o valor do Hypit está em clonagem de virais, UGC, talking heads, B-roll e legendas; nada disso é o gargalo atual. |
| Cabe em 8 GB? | Risco. Os exemplos usam 64 processos Chromium concorrentes; a Runtime tem configuração de capacidade, mas precisaria ser limitada a 1–2. Não medido. |
| Migração | Alta. Seria preciso reescrever o template em SVML/componentes e trocar um fluxo já validado, sem ganho comprovado para 45 s tipográficos. |
| Maturidade | Muito jovem (~3 meses), v0.3.1, 53 issues, mudanças rápidas. Não é base estável para produção contínua. |
| Licença | Uso interno e trabalho para clientes permitido; os outputs são nossos. **Não** podemos oferecer como SaaS multi-tenant nem vender/empacotar Hypit ou derivado sem licença comercial. |
| Ganho aproveitável | Tempo ancorado em palavras/eventos; separação Autor/Run/Build; reuso explícito de outputs; estrutura de memória do projeto (Brief, Treatment, Analysis, Timeline, Progress). |
| Risco de marca | O pitch “clone any viral video” conflita com a regra de não reupload. Só usar para analisar estrutura e criar original, nunca para reaproveitar footage de terceiros. |

**O que aproveitar sem instalar**
- Ler `examples/semantic-composition` e os docs de timing/component design para inspirar a próxima versão do template (ênfase por palavra, ciclo de vida de cena).
- Adotar a ideia de “tratamento” e “análise” por episódio, se isso reduzir retrabalho nos 5 vídeos restantes.
- Manter reuso explícito de assets aprovados quando formos para 30 shorts.

**O que não fazer**
- Instalar o skill globalmente ou trocar o HyperFrames agora.
- Usar o `yt-dlp` do Hypit para baixar/recortar vídeos de terceiros.
- Empacotar Hypit no kit comercial sem licença.

## Canal — decisão em 2026-10-21

- **Um canal = um nicho.** Não misturar Mistério/Arquivo com Psicologia sombria; a audiência e o algoritmo ficam ambíguos.
- O canal atual, **Cod Mind Million**, tem 6 inscritos, 10 shorts e histórico de psicologia/desenvolvimento pessoal. O vídeo de mistério do piloto tem 6 views.
- Com 6 inscritos, o custo de rebranding é baixo; a continuidade vale pouco.

**Dados de nicho (metadados, canais de 100–500 mil inscritos):**

| Nicho | Shorts | Canais | Mediana views/inscrito (canal) | Canais ≥1,0 | Like rate (canal) |
|---|---:|---:|---:|---:|---:|
| Mistério / Arquivo | 48 | 14 | **0,10** | **3** | 3,37% |
| Psicologia sombria | 50 | 17 | 0,06 | 0 | 6,95% |

A psicologia engaja mais por like, mas tem demanda relativa menor; nenhum canal de psicologia chegou a 0,5 views/inscrito, enquanto três de mistério passaram de 1,0. O like não compensa a diferença de demanda.

**Decisão:**
- **Mistério/Arquivo é o nicho âncora da Fase 2.**
- **Rebrandar o Cod Mind Million** para uma marca de arquivo/mistério — nome **“Dossiê 45”** (handle `@Dossie45`, confirmado em 21/10). Arquivar/unlistar os 9 shorts antigos de psicologia e manter o piloto.
- **Validar com 6 vídeos de mistério** (piloto + 5), não 3+3, para não misturar nichos no mesmo canal. Se a retenção falhar, testar Psicologia sombria em um canal novo; não no mesmo canal.
- **Handle:** `@Dossie45` confirmado e no ar em 21/10/2026. Na checagem inicial, `@ArquivoNoturno`, `@SalaEscura`, `@Dossie404`, `@Canal3AM`, `@ORelatorio`, `@ArquivoDaMeiaNoite`, `@Arquivo3AM`, `@DossieNoturno` e `@RelatorioNoturno` estavam ocupados; `@Dossie45`, `@ArquivoNoturno45` e `@Arquivo307` retornaram 404. Alternativas: **Dossiê 45** (adotado), **Arquivo 3:07** (`@Arquivo307`), **Arquivo Noturno 45**.
- **Por que rebrandar e não criar canal novo:** 6 inscritos não são continuidade relevante; o piloto já está no canal; uma marca é mais simples de operar. Criar canal novo só se o handle/nome escolhido estiver indisponível ou se quisermos preservar o canal antigo.

**Execução em 21/10/2026:** handle `@Dossie45` e avatar/banner no ar; nome público **Dossiê 45** confirmado; os 9 shorts de psicologia foram privados e a aba Shorts mostra só o piloto. Falta colar a descrição de `identidade/descricao-canal.txt` no Studio. Ver `docs/REBRANDING.md`.

## youtube-agent-skill — adoção seletiva em 2026-10-21

Repositório: [`Jakeschincariol/youtube-agent-skill`](https://github.com/Jakeschincariol/youtube-agent-skill).
Commit vendorizado: `a2feb2104981a375ffd4f87ee04f4f5344ac43c6`. Licença MIT.

**Veredito: adotar como camada de análise e escrita, não como pipeline.** O pack
não renderiza, não narra, não publica e não substitui HyperFrames/Piper/FFmpeg.
O vendor fica em `tools/youtube-agent-skill/`; nenhuma skill global do Claude
Code foi instalada.

| Peça | Decisão | Motivo |
|---|---|---|
| `yt-retention/retention.py` | **adotar com patch** | É a leitura que falta para as 48 h do piloto. O original usa janela de 30 s e confunde eixo de segundos com percentual em vídeos < 100 s. |
| `yt-script/hooks.json` | **adotar como checklist** | 21 fórmulas úteis para revisar o gancho. A versão PT-BR de trabalho é `docs/GANCHOS-21.md`. |
| `yt-package/title.py` | **adotar com patch** | Lint de título + thumbnail. Precisa de stopwords, termos vagos e nomes próprios em PT-BR. |
| `yt-viral/swipe.py` | **adiar** | Rankeia por múltiplo sobre a mediana do canal, mas exige 4+ vídeos por canal; nossa amostra tem muitos canais com 1–5. O `nicho.py` já cobre a comparação por canal. Reavaliar após os 6 vídeos. |
| `yt-audit` | **adiar** | Auditoria de canal com uma correção; faz mais sentido com 6+ vídeos e o canal limpo. |
| `yt-edit`, `yt-shorts`, `yt-chapters`, `yt-comment`, `yt-plan`, `yt-seo` | **não adotar agora** | Sem dead air (TTS), sem long-form, sem comentários e sem necessidade de plano/SEO paralelo. |

**Não usar `hookscore.py` em PT-BR.** A heurística é calibrada em inglês; o
score não é válido para nossos ganchos. As 21 fórmulas continuam úteis como
checklist editorial.

**Licença:** MIT permite uso comercial e inclusão no kit pago, desde que o
aviso de copyright e a licença sejam preservados. Não há restrição de SaaS
multi-tenant como em outras ferramentas avaliadas.

**Patches:** detalhes em `tools/youtube-agent-skill/ORIGEM.md`; testes em
`scripts/test_youtube_agent.py` (9 casos, incluindo o eixo de 45 s e o lint
PT-BR). O `hooks.json` fica intacto; a adaptação de trabalho fica em
`docs/GANCHOS-21.md`.

## Ferramentas de contexto — avaliadas em 2026-10-21

### Graphify-Labs/graphify — útil no corpus de docs, não no código

Medido no projeto real, não no README:

| Corpus | Antes | Com grafo | Ganho | Leitura |
|---|---:|---:|---:|---|
| Código do projeto | 4.466 tokens | 4.030 | **1,1×** | não compensa: 67 nós, 33 deles em `scripts/nicho.py` |
| `docs/` + `MEMORIA.md` + `AGENTS.md` | 5.066 | 2.423 | **2,1×** | 76 nós, 101 arestas, 9 comunidades, 0 dangling, 65% EXTRACTED |

- A consulta “narração → áudio → vídeo” no grafo de código começou em `.video()` e devolveu 4.611 tokens — pior que ler os arquivos.
- O próprio relatório avisa: “corpus de ~9.833 palavras cabe numa janela de contexto; talvez você não precise de grafo”.
- **Veredito:** não usar como economizador de token no código. Usar em `docs/` + `episodios/` quando houver ~10 episódios (a razão cresce; hoje é 2×).
- **Não** adicionar a regra “consulte o grafo antes de grep” ao `AGENTS.md` enquanto o grafo de código for pior que a leitura direta.
- O grafo **não** depende do git; só o `graphify hook install` (rebuild por commit) depende.

### thedotmack/claude-mem — não instalar agora

Captura cada chamada de ferramenta via hooks, grava em SQLite+FTS5, comprime com IA e reinjeta contexto. Roda worker Express persistente (Node 20+/Bun) e MCP de busca.

- **Compatível** com OpenCode: contrato V1/V2 corrigido no PR #4577, validado no OpenCode 2.0.22.
- **Não adotado** porque: (1) worker + compressão por observação competem com Chrome headless + FFmpeg numa máquina de 8 GB com a regra “um render por vez”; (2) captura *tool calls*, e o valor do projeto está em decisões e medições (−15,6 LUFS, 2m32,8s), que não aparecem em tool call; (3) cria segunda fonte de verdade contra `MEMORIA.md` curado e pode mascarar memória desatualizada; (4) custo de compressão recorrente para um corpus de ~10 mil palavras.
- **O que aproveitar:** automatizar a *escrita* da memória (uma skill de fechamento de etapa), não a captura.
- **Reavaliar se:** multi-projeto/multi-agente, 16 GB+ de RAM, ou se o `MEMORIA.md` deixar de ser mantido à mão.

### Git — adotado em 2026-10-21

- Git 2.56.0 já estava instalado em `C:\Users\valentim\Tools`; faltava o repositório.
- `git init -b main`, commit baseline `782df62` (59 arquivos de texto/código), tag `ep-001-publicado`.
- `.gitignore` exclui `.venv/`, mídia (`*.mp4`, `*.wav`, `*.onnx`) e `qa-frames/`; **nada foi apagado do disco**.
- Motivo: rollback de experimento de fonte/template, diff de contrato entre episódios e baseline antes do rebranding. Não é pré-requisito do graphify.






### Modelagem de canais e escala - decidido em 2026-10-26

- Levantamento em `docs/ESCALA.md`; ferramenta em `scripts/scout.py`.
- **Modelar copia o pacote visível, não a retenção.** Duração, frame 0, texto por cartão, tema e série são copiáveis; curva de retenção, ritmo de revelação e desenho sonoro não são. A coluna invisível é onde o canal perde.
- **Views não são a régua.** O 004 teve 3x as views do 003 e metade da retenção. Proxy externo de retenção: views por inscrito, breakout e aceleração.
- **Descoberta de canal é humana, medição é da máquina.** yt-dlp não respeita filtro de busca, `ytsearchdate` não existe na versão instalada e hashtag é ruído global.
- **O gargalo é vazão, não ideia.** 2 dias por vídeo; 20-30 curvas exigiriam ~2 meses. A resposta é um gerador (`roteiro.json` -> `index.html`), não mais referência.
- **Nada de escalar o formato antes do Gate 2.**
- **Gate 2 passa a usar janela fixa de 48 h** para "% média assistida", porque a duração média escorrega com o tempo.

### Canais de teste - método decidido em 2026-10-27

- **Método completo em `canais/README.md`.** Registro em `canais/registro.csv`, um diretório por canal em `canais/<slug>/` gerado de `canais/_template/`. `canais/dossie45/` é o exemplo preenchido (o único canal com histórico).
- **Um canal = um modelo; um canal = uma variável.** Modelo é a combinação de cinco escolhas (nicho, formato, voz, cadência, visual). Ao abrir o canal 2, **uma** muda e as outras quatro ficam iguais ao Dossiê 45 — duas mudanças ao mesmo tempo não dão leitura.
- **Hipótese e critério de morte escritos na `ficha.md` antes do vídeo 1.** No dia da leitura não se decide com o número na mão; decide-se com a regra escrita antes.
- **N = 8 vídeos antes de decidir** (escalar / ajustar / matar), porque com 3 a mediana é o valor do meio e qualquer oscilação muda a conclusão. O Dossiê 45 é exceção: 6 é a amostra do Gate 2.
- **Custo de decisão por canal: ~16 h** (8 vídeos × ~2 h). Máximo **2 canais ativos** nesta máquina: 1 produzindo, 1 medindo. Um render por vez continua inviolável.
- **Canal novo não é campo de teste do Dossiê 45.** O v1 dos 6 episódios fica congelado até o Gate 2; o teste de v2 (imagem de arquivo, som audível, 60 s) vira canal novo, não um sétimo vídeo.
- **Episódios de canal novo ficam em `canais/<slug>/episodios/`.** Os scripts são path-based e funcionam sem alteração; `novo-episodio.ps1` grava sempre em `episodios/` (pendência: dar um `-Destino`).
- **Candidatos, ainda não escolhidos:** A = mesmo formato + nicho adjacente (true crime PT-BR); B = mesmo nicho + 60 s; C = mesmo nicho + desenho sonoro audível. **Escolha adiada em 27/10 para depois do Gate 2** (decisão do usuário): o número de 005/006 diz se o formato já está resolvido ou se o problema é o miolo, e isso muda qual variável vale testar.

### Gate 2 — fechado em 2026-10-29

- **Resultado: PASSA.** `% média assistida` em 48 h: 002 **87,0%**, 003 **87,0%**, 005 **54,3%** → **3 de 6** acima de 50%. O critério era ≥3 de 6. 004 45,7%, 006 **50,0%** (limite do arredondamento), 001 33,3% (fora da amostra).
- **O que fica decidido:** o formato de 45 s tipográfico **não está descartado** — mas também não está otimizado: 005 (12 cenas, gerado do JSON) fez **54,3%** com 224 views, e 006 (14 cenas) ficou em 50,0% com 79 views e **38,2%** de “ficaram para assistir”.
- **Regra que sobrevive:** o que derrubava o miolo era o **estado parado**, não a quantidade de texto — o 005 dobrou a duração média do 004 (0:25 contra 0:21) com menos views.
- **Próximo alvo declarado:** o **primeiro segundo**. O 006 abria com contexto (“Eles cortaram a encosta para dormir”) e perdeu no gancho; o 005 abria com ação (“Cinco aviões pediram socorro”).
- **O gate não autoriza** mudar duas variáveis no Dossiê 45: mudança de visual/fonte/imagem continua indo para **canal separado**, uma por vez.
- **Limite de medição registrado:** 3 s / 10 s da curva não são legíveis no painel controlado (hover sintético não funciona). Só views, “Stayed to watch” e duração média entram no registro; o resto fica vazio, nunca estimado.

### Canal único — decidido em 2026-10-29

- **O estúdio opera um canal só: o Dossiê 45.** `sombra-direta` (001 com QA PASS, nunca publicado) e `mente-obscura` (ficha + roteiro, sem render) ficam **pausados** — arquivo em disco, não apagados, sem linha removida do `registro.csv`.
- **Motivo:** a decisão de escala do usuário em 29/10 é **produzir conteúdo**, não abrir canal. Com um canal, o custo por vídeo cai (não há ficha, identidade e medição paralelas) e a leitura fica numa série só.
- **Consequência metodológica:** o teste de v2 (imagem, som, 60 s) **não** tem mais para onde ir. Ou entra como **uma variável na própria série** (com o risco de contaminar a comparação), ou espera um segundo canal. Enquanto isso, a série continua no v1.
- **O que isso não muda:** aprovação humana por vídeo, janela fixa de 48 h, um render por vez, `% média` como régua.

### Lote 007–011 — aprovado em 2026-10-29

- **A variável do lote é o gancho** (o primeiro segundo), porque o Gate 2 isolou exatamente isso: 005 abriu com ação e fez **46,5%** de “ficaram para assistir”; 006 abriu com contexto e fez **38,2%**, com o mesmo visual e a mesma voz.
- **Fixo:** 45 s, **12 cartões**, nenhum acima de 5 s, 1 ideia por cartão, sem cartão de contexto depois do gancho, v1 tipográfico, Piper `pt_BR-faber-medium`, 1080×1920/30 fps, ~−15 LUFS.
- **Hipótese:** mediana de “ficaram” **≥ 46,5%** e de `% média` **> 54,3%** nos 5 vídeos.
- **Critério:** as duas medianas passando → adotar a regra e escalar para os 30 shorts da Fase 3; só uma → a próxima variável é **ritmo/visual** (LAB 002); nenhuma → reavaliar o formato.
- **Cadência fixa:** 1/dia, 19h de Brasília, seg–sex. **Horário é constante, não variável** — com 5 vídeos não se isola horário de dia da semana e de gancho. Não há dado de horário no projeto; Shorts feed foi 92,2% (003) e 98,9% (004) das views.
- **Temas aprovados:** Somerton (1948), Max Headroom (1987), Máscaras de chumbo (1966), Carroll A. Deering (1921), SS Baychimo (1931–1969). Reservas: Hinterkaifeck, Mulher de Isdal, Yuba County Five, Voynich.
- **Aprovar o lote é aprovar os temas**, não a publicação: a aprovação continua **por vídeo**, explícita.
- **Custo:** ~10 h (≈6 h de briefing/fonte) + 5 renders de ~3 min, um por vez.

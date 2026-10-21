# HISTORICO — Padrao-Dark

> Linha do tempo do que foi **entregue**, com data, evidência e decisão.
> Não é um diário: é o registro de marcos para uma sessão nova saber o que já existe.
> Mais recente no topo. Última atualização: **2026-10-21**.

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
- [ ] Escrever o script de validação de nicho (`yt-dlp`, 50 shorts/nicho, views por inscrito).
- [ ] Produzir e publicar 6 vídeos de validação.
- [ ] Medir retenção em 48 h e escolher o nicho âncora.
- [ ] Instalar `codebase-memory-mcp` após o primeiro vídeo publicado.

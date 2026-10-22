# MEMORIA — Padrao-Dark

> **Leia este arquivo primeiro.** Ele é a memória de retomada do projeto.
> Depois: `AGENTS.md` (regras) → `docs/PLANO.md` (fases) → `docs/HISTORICO.md` (o que já foi entregue).
> Última atualização: **2026-10-21**. Se você é uma sessão nova, não refaça o que está marcado como entregue.

## 1. Onde estamos

**Fase 1 concluída e piloto publicado.** O cérebro está instalado, o gate G0 passou, o piloto `001-faroleiros` foi aprovado pelo usuário ("ficou perfeito") e publicado no YouTube Shorts em 21/10/2026. O template `misterio-45` foi extraído e o QA técnico está assinado. A validação de nicho por metadados foi concluída em 21/10/2026: **Mistério/Arquivo é a âncora**. Em 21/10/2026 também foi feita a **adoção seletiva do `youtube-agent-skill`** (retenção 3 s/10 s, 21 ganchos e lint de título). O **002-mary-celeste** foi produzido, passou no QA técnico e foi **publicado no YouTube Shorts em 21/10/2026**; a Fase 2 segue com os 4 vídeos restantes e a medição de retenção de 001 e 002.

| Frente | Estado | Evidência |
|---|---|---|
| Cérebro (Node, FFmpeg, Python, Piper, faster-whisper, yt-dlp, HyperFrames) | pronto | `docs/STACK.md` |
| Gate G0 (45 s em 1080×1920) | **PASS** | `logs/bench.json`, 2m32,8s |
| Piloto `001-faroleiros` | **aprovado** | `episodios/001-faroleiros/final.mp4`, `qa.md` |
| Template `misterio-45` | pronto | `templates/misterio-45/` |
| Documentação de retomada | pronta | este arquivo + `docs/ARQUITETURA.md` + `docs/HISTORICO.md` |
| Publicação | **publicado** (21/10/2026) | 001: [Shorts](https://youtube.com/shorts/WKuNVjl3d5M); 002: [Shorts](https://youtube.com/shorts/n6dtveQguf4) |
| Validação de nicho | **concluída (metadados)** | `logs/nicho-2026-10-21.json`, `docs/NICHO.md` |
| Versionamento | **git iniciado (21/10/2026)** | commit `782df62`, tag `ep-001-publicado` |
| 6 vídeos de validação | **2/6 publicados** | piloto + 002 + 4 restantes |
| Episódio 002 — Mary Celeste | **publicado** (21/10/2026) | `episodios/002-mary-celeste/`, [Shorts](https://youtube.com/shorts/n6dtveQguf4) |
| Canal | **Dossiê 45**: nome, avatar/banner, descrição no ar e 9 shorts antigos privados | [canal](https://youtube.com/@Dossie45), `docs/REBRANDING.md` |
| Ferramentas de análise | **adotadas seletivamente** | `tools/youtube-agent-skill/`, `docs/GANCHOS-21.md` |
| `codebase-memory-mcp` | **não instalado** (adiado) | decisão em `docs/DECISOES.md` |

## 2. O que já foi entregue

### Infraestrutura
- Node v22.23.3, npm 10.9.9, Git 2.56.0, FFmpeg/ffprobe 8.1.3, uv 0.13.4, Python 3.12.15.
- Piper 1.8.0 + voz `pt_BR-faber-medium`; faster-whisper 1.2.1; yt-dlp 2026.8.19.
- HyperFrames 0.8.181 + Chrome Headless Shell 152.
- Tudo em `C:\Users\valentim\Tools` e `.venv` (sem admin).
- Correções aplicadas: DLLs VC++ no onnxruntime/venv, `espeak-ng-data` em caminho ASCII, patch do `av` no faster-whisper. Detalhes em `docs/STACK.md`.

### Conteúdo e método
- 8 skills operacionais em `.opencode/skills/` (briefing, gancho, roteiro, voz, render, qa, publicacao, retencao).
- `docs/`: decisões, stack, nicho, plano, QA, identidade, `GANCHOS-21.md`.
- `biblioteca/`: ganchos, fontes, `publicados.csv`.
- `scripts/qa.ps1`: QA automático (duração, resolução, fps, áudio, loudness, preto inesperado).
- `scripts/check-contrato.ps1`: 29 invariantes da composição antes do render (resolução, cenas, áudio com duração real via ffprobe, `autoAlpha`, timeline montada).
- `scripts/novo-episodio.ps1`: cria episódio a partir do template e carimba `.template-version` (sha256 + commit).
- `scripts/nicho.py`: coleta metadados de Shorts por nicho (views/inscrito, engajamento); não baixa vídeo.
- `tools/youtube-agent-skill/`: vendor MIT com retenção 3 s/10 s, `hooks.json` e lint de título PT-BR; testes em `scripts/test_youtube_agent.py`.

### Piloto 001 — Eilean Mor
- `narracao.txt` (118 palavras) → `voz_raw.wav` 41,45 s → `voz.wav` 45,00 s.
- `transcricao.json` com timestamps por palavra; 13 cenas sincronizadas.
- `index.html` tipográfico, 1080×1920, 30 fps, 13 cenas, `autoAlpha` por cena.
- `final.mp4`: **45,01 s, 3,3 MB, −15,6 LUFS**, H.264 + AAC 48 kHz estéreo.
- `qa.md`: QA técnico **PASS**; aprovação humana registrada em 21/10/2026.
- Cópia de publicação: `001-faroleiros_shorts_v1.mp4`; capa: `capa.png`.
- **Publicado no YouTube Shorts em 21/10/2026:** https://youtube.com/shorts/WKuNVjl3d5M (canal Cod Mind Million).

### Episódio 002 — Mary Celeste (21/10/2026)
- Tema: abandono documentado × lenda do “jantar servido”.
- `briefing.md`, `gancho.md` (fórmula 17), `roteiro.md` (110 palavras de tela / 121 faladas), `shotlist.md`.
- `voz_raw.wav` 43,04 s (`length_scale` 1,12) → `voz.wav` 45,00 s; `transcricao.json` por palavra.
- `index.html` com 13 cenas sincronizadas; gancho visível no frame 1; `autoAlpha` por cena.
- `check-contrato.ps1`: **OK, 0 avisos** (29 invariantes).
- `final.mp4`: **45,013 s, 3,6 MB, −15,4 LUFS, pico −1,5 dBFS**, 1080×1920, H.264, 30 fps, AAC 48 kHz estéreo.
- `qa.md`: QA técnico **PASS**; aprovação humana em 21/10/2026.
- Cópia de publicação: `002-mary-celeste_shorts_v1.mp4`; capa: `capa.png`.
- Título: `Mary Celeste: o navio encontrado sem ninguém em 1872` (52 chars; lint 98/100).
- **Publicado no YouTube Shorts em 21/10/2026:** https://youtube.com/shorts/n6dtveQguf4. Aviso de conteúdo sintético marcado; selo **AI** visível.

### Template
- `templates/misterio-45/index.html` — composição validada, 13 cenas, áudio `voz`/`drone`, QA por `?t=`.
- `templates/misterio-45/beat-sheet.md` — 13 beats, tempos e orçamento de palavras.
- `templates/misterio-45/README.md` — passo a passo completo, incluindo armadilhas.

### Versionamento (21/10/2026)
- `git init -b main`; commit baseline `782df62` com **59 arquivos de texto/código**; tag anotada `ep-001-publicado`.
- `.gitignore` deixa fora `.venv/` (415 MB), mídia `*.mp4`/`*.wav`/`*.onnx` (123 MB) e `qa-frames/`. **Nada foi apagado do disco**: evidência continua na pasta.
- `core.autocrlf false` (local) para evitar churn de CRLF.
- Identidade provisória `valentim <valentim@localhost>`; sem remote e sem chave SSH, nada foi enviado.
- Fluxo: commit por etapa, tag por episódio publicado.

## 3. O que falta (em ordem)

### 3.1 Medir os publicados 001 e 002 (48 h)
> Checklist do gate e fila provisória 003–006: `docs/PLANO.md` §Execução imediata.

1. Publicados em 21/10/2026 no YouTube Shorts; TikTok/Reels ficam como reaproveitamento opcional.
2. Em **23/10/2026**, baixar o CSV de retenção do Studio para 001 e 002 e rodar `tools/youtube-agent-skill/yt-retention/retention.py --duration 45` em cada; coletar também views, retenção média, conclusão, salvos e compartilhados.
3. Preencher as colunas em aberto das linhas de `biblioteca/publicados.csv` e criar `episodios/001-faroleiros/retencao.md` e `episodios/002-mary-celeste/retencao.md`.
4. Decidir: manter gancho/formato, ajustar ou matar.

### 3.2 Validação de nicho — concluída (21/10/2026)
- Coleta completa: 48 shorts de Mistério/Arquivo (14 canais) e 50 de Psicologia sombria (17 canais), canais de 100–500 mil inscritos.
- **Mistério/Arquivo:** mediana de views/inscrito por canal **0,10**; 3 canais ≥1,0 (Pequeno Contexto 1,50; Penumbroo 1,04; Crimes que Marcaram 1,02); mediana de views por canal 2.075.
- **Psicologia sombria:** mediana de views/inscrito por canal **0,06**; nenhum canal ≥0,5; mediana de views por canal 1.428.
- **Engajamento:** psicologia tem like rate maior (6,95% vs 3,37%), mas demanda relativa menor. O like não compensa a diferença de views/inscrito.
- **Decisão:** Mistério/Arquivo é a âncora da Fase 2. Psicologia fica como fallback, não como teste paralelo.
- Dados completos em `logs/nicho-2026-10-21.json` e `docs/NICHO.md`.

### 3.3 Produzir 6 vídeos
- **6 vídeos de Mistério 45** (2/6 publicados; faltam 4), no canal rebrandado.
- **003-roanoke** em pré-produção: briefing e gancho prontos; roteiro pendente; produção final só depois do gate de 23/10.
- Manter o gate para os próximos: aprovação humana explícita e descrição do canal conferida antes de publicar.
- Usar `templates/misterio-45/` e o fluxo de `MEMORIA.md` §6.
- Meta: 5–7 shorts/semana; um render por vez.
- Se a retenção dos 6 ficar abaixo do gate (média <40% ou nenhum >40%), reavaliar: testar Psicologia sombria em canal novo antes de trocar de ferramenta.
- Diagnóstico por vídeo: 3 s ≥ 70% e 10 s ≥ 45% são metas provisórias; o gate de 40% de média continua valendo para a fase.

### 3.4 Ferramentas de análise — concluído (21/10/2026)
- Vendor seletivo de `Jakeschincariol/youtube-agent-skill` (MIT, commit `a2feb21`) em `tools/youtube-agent-skill/`.
- `retention.py` com patch para Shorts: 3 s/10 s, eixo de 45 s corrigido, transcrição SRT/VTT/JSON.
- `hooks.json` mantido intacto; checklist PT-BR em `docs/GANCHOS-21.md`.
- `title.py` adaptado para PT-BR (stopwords, termos vagos, nome próprio).
- `scripts/test_youtube_agent.py`: 9 testes passando.
- `yt-viral` e `yt-audit` adiados para depois dos 6 vídeos; decisão em `docs/PLANO.md` e `docs/DECISOES.md`.

### 3.5 Desbloqueado pelo primeiro vídeo (21/10/2026)
- `codebase-memory-mcp` pode ser instalado e o projeto indexado, **fora de uma janela de render** (RAM de 8 GB).
- OpenMontage continua fora até o gate 3 (ver `docs/PLANO.md`).

## 4. Ambiente e restrições

| Item | Valor |
|---|---|
| Máquina | Dell Inspiron 5468, i5-7200U 2C/4T, 8 GB RAM, Intel HD 620, Windows 10 22H2 |
| Disco | C: ~67 GB livres; D:/E: HDD USB |
| Binários | `C:\Users\valentim\Tools` (Node, FFmpeg, Git) |
| Python | `.venv` do projeto (Piper, faster-whisper, yt-dlp) |
| Render | HyperFrames + Chrome headless; **um por vez** |
| Regra | Sem WebGL/Three.js, sem Docker/WSL, sem Remotion/Hermes3D |

## 5. Mapa de arquivos

| Caminho | O que é |
|---|---|
| `MEMORIA.md` | este arquivo; estado e retomada |
| `AGENTS.md` | regras invioláveis e fluxo |
| `README.md` | visão do produto e stack |
| `docs/PLANO.md` | fases, gates, capacidade, métricas |
| `docs/HISTORICO.md` | linha do tempo do que foi entregue |
| `docs/ARQUITETURA.md` | contratos do código (cenas, áudio, render, QA) |
| `docs/STACK.md` | instalação, versões, correções de ambiente |
| `docs/DECISOES.md` | decisões e descartes |
| `docs/NICHO.md` | hipóteses de nicho e critérios |
| `docs/REBRANDING.md` | textos e ordem de execução do rebranding no YouTube Studio |
| `docs/GANCHOS-21.md` | checklist PT-BR das 21 fórmulas de gancho |
| `docs/QA.md` | checklist editorial e técnico |
| `.opencode/skills/` | instruções por etapa |
| `templates/misterio-45/` | template validado |
| `episodios/<slug>/` | um diretório por vídeo, com status e QA |
| `scripts/` | instalação, voz, transcrição, QA, benchmark, testes |
| `tools/youtube-agent-skill/` | vendor MIT: retenção, hooks e lint de título |
| `biblioteca/publicados.csv` | registro de publicação e métricas |

## 6. Comandos canônicos

```powershell
# ambiente novo
$env:Path = "C:\Users\valentim\Tools\node;C:\Users\valentim\Tools\ffmpeg\bin;" + $env:Path

# verificar instalação
.\scripts\verify.ps1

# criar episódio novo (carimba o template usado)
.\scripts\novo-episodio.ps1 002-slug "Título do episódio"

# contrato antes do QA visual e do render
.\scripts\check-contrato.ps1 episodios\<slug>\index.html

# voz (sempre pelo wrapper, nunca piper.exe)
.\.venv\Scripts\python.exe scripts\tts.py `
  --model models\vozes\pt_BR-faber-medium.onnx `
  --input episodios\<slug>\narracao.txt `
  --output episodios\<slug>\voz_raw.wav --length-scale 1.28

# transcrição com timestamps
.\.venv\Scripts\python.exe scripts\transcribe.py `
  episodios\<slug>\voz.wav --model small --language pt `
  --output episodios\<slug>\transcricao.json

# retenção do Studio (48 h)
.\.venv\Scripts\python.exe tools\youtube-agent-skill\yt-retention\retention.py `
  episodios\<slug>\retencao.csv --duration 45 `
  --transcript episodios\<slug>\transcricao.json

# lint de título + thumbnail
.\.venv\Scripts\python.exe tools\youtube-agent-skill\yt-package\title.py `
  --title "<título>" --thumb "<texto da capa>"

# testes das ferramentas de análise
.\.venv\Scripts\python.exe scripts\test_youtube_agent.py

# QA visual de uma cena, sem render
$chrome = (Get-ChildItem "$env:USERPROFILE\.cache\hyperframes\chrome\chrome-headless-shell" -Recurse -Filter chrome-headless-shell.exe | Select-Object -First 1).FullName
$uri = [System.Uri]::new((Resolve-Path index.html)).AbsoluteUri
& $chrome --disable-gpu --hide-scrollbars --window-size=1080,1920 `
  --virtual-time-budget=1500 --screenshot=qa-frames\t12.5.png "$uri`?t=12.5"

# render segmentado (evita Target closed)
$env:HF_SEGMENTED_CAPTURE = "true"
$env:HF_SEGMENT_FRAMES = "300"
$env:HF_SEGMENT_BROWSER_RECYCLE = "1"
hyperframes render --output final_raw.mp4 --quality standard --fps 30 `
  --workers 1 --low-memory-mode --protocol-timeout 600000 --resume

# normalizar áudio (medir antes; o piloto usou +6,2 dB)
ffmpeg -i final_raw.mp4 -c:v copy `
  -af "volume=6.2dB,alimiter=limit=0.85:level=disabled" `
  -c:a aac -b:a 192k -movflags +faststart final.mp4

# QA automático
.\scripts\qa.ps1 episodios\<slug>\final.mp4
```

## 7. Armadilhas conhecidas

| Sintoma | Causa | Solução |
|---|---|---|
| `piper.exe` falha com caminho acentuado | espeak-ng não lê `Padrão` | usar `scripts/tts.py` |
| Shims `.ps1` bloqueados | execution policy | chamar `.cmd` ou `-ExecutionPolicy Bypass` |
| Render mudo | `<audio>` sem `id` | manter `id="voz"` e `id="drone"` |
| Texto fantasma de outra cena | GSAP só anima entrada | `autoAlpha` por cena (já no template) |
| Chrome fecha em ~1300/1350 frames | memória acumulada | captura segmentada + 1 worker |
| Linha quebra diferente no render | fonte na fronteira dos ~840 px | reduzir 4–8 px ou quebrar antes |
| Áudio em −22 LUFS | TTS baixo + drone discreto | ganho estático + limitador no pós |
| `qa.ps1` “falha” no ffmpeg | stderr vira erro no PowerShell | o script já contorna; rodar com Bypass |
| faster-whisper quebra no `av` 19 | `metadata_errors` removido | patch em `faster_whisper/audio.py` |
| Retenção de 45 s lida como 100% no fim | eixo em segundos (máx. 45) confundido com percentual | usar o `retention.py` patchado; `--axis seconds` se preciso |
| Score de gancho estranho em PT-BR | `hookscore.py` é calibrado em inglês | não usar; consultar `docs/GANCHOS-21.md` |

## 8. Decisões que não se reabrem

- HyperFrames (Apache 2.0), Piper, faster-whisper, yt-dlp, FFmpeg.
- Vídeo **tipográfico** (texto é a imagem); sem WebGL, Three.js, shaders.
- PT-BR até o gate de expansão.
- Nada de reupload de terceiros; `yt-dlp` só metadados.
- Um render por vez; 1080×1920, 30 fps, H.264 + AAC.
- Fato precisa de fonte; lenda marcada como lenda.
- `codebase-memory-mcp` e OpenMontage só depois do primeiro vídeo publicado.
- PI-Desktop fica fora do MVP; reavaliar só depois do primeiro vídeo (ver `docs/DECISOES.md`).
- Hypit é referência conceitual, não dependência do MVP; não empacotar no kit sem licença comercial.
- Um canal = um nicho; não misturar Mistério/Arquivo com Psicologia sombria.
- Mistério/Arquivo é a âncora da Fase 2; o Cod Mind Million foi rebrandado para **Dossiê 45** (handle `@Dossie45`, avatar/banner no ar). Nome público, descrição de `identidade/descricao-canal.txt` e deslistagem dos 9 shorts antigos concluídos. Psicologia fica como fallback em canal novo, não no mesmo canal.
- `youtube-agent-skill` é adotado **seletivamente** (retenção, hooks como checklist, lint de título). `yt-viral` e `yt-audit` ficam para depois dos 6 vídeos; `hookscore.py` não é usado em PT-BR.

## 9. Protocolo de memória

Ao fim de **cada etapa**:

1. Atualizar a tabela da §1 e as listas das §2/§3 deste arquivo.
2. Acrescentar uma entrada datada em `docs/HISTORICO.md` (o que, evidência, decisão).
3. Atualizar `episodios/<slug>/status.md` e `qa.md` quando for um episódio.
4. Se mudar um contrato de código, atualizar `docs/ARQUITETURA.md`.
5. Nunca apagar evidência (áudio, frames de QA, `final_raw.mp4`).

> Regra de ouro: se uma sessão nova não conseguir retomar lendo `MEMORIA.md` + `AGENTS.md` + `docs/PLANO.md`, esta memória está incompleta.

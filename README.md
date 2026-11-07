# Padrao-Dark

Framework de produção de vídeo curto **faceless** ("dark") para YouTube Shorts, TikTok e Reels.

> Status: **Gate 2 fechado (3 de 6 acima de 50% de % média)** + **lote 007–011 publicado** +
> template `misterio-45` + **17 layouts de cena aprovados** + ferramentas de análise
> (retenção 3 s/10 s, 21 ganchos, lint de título, métricas de canal).
> Última atualização: 2026-11-06

## O que é

Um pipeline repetível que transforma uma ideia em vídeo publicado:

```
gancho -> pesquisa -> roteiro -> shotlist -> voz -> visual -> render -> QA -> publicação -> retenção (48 h)
```

Cada etapa tem um artefato e um gate. Sem template, não há escala.

## O que não é

- Não é SaaS
- Não é geração de vídeo por IA local (a máquina não tem GPU)
- Não é "fazemos qualquer vídeo" — são formatos fixos por canal

## Estrutura

```
Padrao-Dark/
├── .opencode/skills/  instruções por etapa (briefing, gancho, roteiro, voz, render, qa, publicação)
├── docs/              decisões, stack, nicho, plano, QA, identidade, arquitetura, histórico
├── templates/         composições HyperFrames (misterio-45 + 17 layouts aprovados)
├── identidade/        paleta, fontes, LUT, sound design
├── biblioteca/        ganchos, estruturas, fontes, métricas, publicados.csv
├── canais/            método de expansão: um canal por modelo (dossie45, sombra-direta, _template/)
├── episodios/         um diretório por vídeo (roteiro.json, briefing.md, publicacao.md, qa.md, etc.)
├── laboratorio/       ensaios fora da fila (001-60s-fawcett, 003-layouts-17, etc.)
├── models/vozes/      modelos Piper (binários .onnx não versionados)
├── bench/             composição de teste (gate G0)
├── scripts/           instalação, automação, voz, QA, benchmark, scout
├── tools/             vendor seletivo (yt-retention, hooks.json, lint de título)
├── logs/              instalação e execução
├── graphify-out/      grafo de conhecimento (opcional, não versionado por padrão)
├── maestri/           estado local do canvas Maestri (não versionado)
├── .venv/             ambiente Python (não versionado)
├── AGENTS.md          regras de operação do projeto
├── ESTADO.md          estado de retomada por passo (atualizado a cada passo)
├── MEMORIA.md         memória geral do projeto
├── README.md          este arquivo
└── LICENSE            MIT
```

## Stack

| Camada | Ferramenta |
|---|---|
| Orquestração | OpenCode |
| Render | HyperFrames (Apache 2.0) |
| Voz | Piper TTS (MIT) — wrapper `scripts/tts.py` |
| Legendas | faster-whisper (MIT) |
| Montagem/QA | FFmpeg |
| Pesquisa | yt-dlp (metadados apenas, sem reupload) |
| Memória de código | codebase-memory-mcp (MIT) |
| Pesquisa/roteiro/QA | OpenMontage (AGPL) |

Decisões e descartes: [docs/DECISOES.md](docs/DECISOES.md).

## Regras invioláveis

1. **Um render por vez.** Chrome headless + FFmpeg saturam a máquina.
2. **1080×1920, 30 fps, H.264 + AAC** para shorts.
3. **Sem WebGL, Three.js ou shaders.** A GPU é Intel HD 620.
4. **Sem Docker, WSL, Hermes3D, ruflo ou Remotion** nesta máquina.
5. **Fato precisa de fonte.** Lenda precisa ser marcada como lenda.
6. **Tudo em português (PT-BR)** até o gate de expansão.
7. **Nada de reupload** de conteúdo de terceiros. `yt-dlp` só para metadados.

## Instalação

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\install-brain.ps1
```

Sem admin: tudo em `C:\Users\valentim\Tools` e no perfil do usuário.

## Estado do projeto (06/11/2026)

- **Gate 2:** PASSA (3 de 6 vídeos acima de 50% de % média assistida, janela de 48 h)
- **Lote 007–011:** publicado (02–05/11) e medido — retenção falhou no miolo, passou no gancho
- **012 Hinterkaifeck:** QA PASS, aguardando aprovação humana para publicação
- **17 layouts:** aprovados em 01/11, entram 1–2 por episódio
- **Canal de teste `sombra-direta`:** episódio 001 pronto, aguardando conta Google separada

## Subindo ao GitHub

1. Crie um repositório vazio no GitHub (não inicialize com README, LICENSE ou .gitignore — o projeto já tem todos).
2. Adicione o remote:

```powershell
git remote add origin https://github.com/<seu-usuario>/<repositorio>.git
git branch -M main
git push -u origin main
```

3. Após o push, configure branch protection, CODEOWNERS e secrets se necessário.

## Antes de publicar qualquer vídeo

Seguir `docs/QA.md`. Sem `qa.ps1` com **QA PASS** e `qa.md` assinado, não publica. A aprovação humana do vídeo é obrigatória.

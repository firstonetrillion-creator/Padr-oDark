# Padrao-Dark

Framework de produção de vídeo curto **faceless** ("dark") para YouTube Shorts, TikTok e Reels.

> Status: **cérebro instalado** + **piloto 001 aprovado** (QA PASS, −15,6 LUFS) +
> template `misterio-45` + **Dossiê 45 em rebranding** + ferramentas de análise
> (retenção 3 s/10 s, 21 ganchos e lint de título).
> Última atualização: 2026-10-21

## O que é

Um pipeline repetível que transforma uma ideia em vídeo publicado:

```
gancho -> pesquisa -> roteiro -> shotlist -> voz -> visual -> render -> QA -> publicação
```

Cada etapa tem um artefato e um gate. Sem template, não há escala.

## O que não é

- Não é escritório 3D (Hermes3D está fora)
- Não é SaaS
- Não é geração de vídeo por IA local (a máquina não tem GPU)
- Não é "fazemos qualquer vídeo" — são 5 formatos fixos

## Estrutura

```
Padrao-Dark/
├── .opencode/skills/  instruções por etapa (briefing, gancho, roteiro, voz, render, qa, publicação)
├── docs/            decisões, stack, nicho, plano, QA, identidade
├── templates/       composições HyperFrames
├── identidade/      paleta, fontes, LUT, sound design
├── biblioteca/      ganchos, estruturas, fontes, trilhas
├── episodios/       um diretório por vídeo
├── models/vozes/    modelos Piper
├── bench/           composição de teste (gate G0)
├── scripts/         instalação e automação
├── tools/           vendor seletivo de ferramentas de análise
└── logs/            instalação e execução
```

## Stack

| Camada | Ferramenta |
|---|---|
| Orquestração | OpenCode |
| Render | HyperFrames (Apache 2.0) |
| Voz | Piper TTS (MIT) — wrapper `scripts/tts.py` |
| Legendas | faster-whisper (MIT) |
| Montagem/QA | FFmpeg |
| Pesquisa | yt-dlp (metadados) |
| Memória de código | codebase-memory-mcp (MIT) — fase 2 |
| Pesquisa/roteiro/QA | OpenMontage (AGPL) — fase 2 |

Decisões e descartes: [docs/DECISOES.md](docs/DECISOES.md).

## Instalação

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\install-brain.ps1
```

Sem admin: tudo em `C:\Users\valentim\Tools` e no perfil do usuário.

## Próximos passos

1. Colar a descrição de `identidade/descricao-canal.txt` no Studio e salvar
   palavras-chave/país. Nome, avatar/banner e deslistagem já estão prontos.
2. Publicar os 5 vídeos restantes de **Mistério 45** (o piloto é 1/6).
3. Em 23/10, medir o piloto com
   `tools/youtube-agent-skill/yt-retention/retention.py` e preencher
   `biblioteca/publicados.csv`.
4. Decidir manter/ajustar o formato com base na retenção de 3 s e 10 s.
5. Só depois dos 6 vídeos: reavaliar `yt-viral` e `yt-audit`.

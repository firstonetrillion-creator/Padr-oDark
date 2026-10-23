# AGENTS — Padrao-Dark

Framework de produção de vídeo curto faceless. **Leia `MEMORIA.md` primeiro**; depois `docs/ARQUITETURA.md`, `docs/PLANO.md` e `README.md`.

## Memória (não pule)

| Camada | Arquivo | Para quê |
|---|---|---|
| Passo | `ESTADO.md` | uma tela; atualizar **a cada passo**. É `instructions` (sobrevive à compactação) |
| Geral | `MEMORIA.md` | onde estamos, o que falta, comandos, armadilhas |
| Código | `docs/ARQUITETURA.md` | contratos de cena, áudio, tempo, render e QA |
| Entrega | `docs/HISTORICO.md` | o que já foi feito, com data e evidência |

Ao fim de **cada passo**, atualizar `ESTADO.md` (feito / pendente / bloqueio / próximo comando). Ao fim de **cada etapa**, atualizar `MEMORIA.md` (§1–§3) e acrescentar uma entrada em `docs/HISTORICO.md`. Se mudou um contrato de código, atualizar `docs/ARQUITETURA.md`. Nunca apagar evidência.

**Compactação é lossy:** o que só existe no chat desaparece. Compacte entre etapas (`opencode api post /api/session/<id>/compact --data '{}'`) e nunca no meio de um render.

## Regras invioláveis

1. **Um render por vez.** Chrome headless + FFmpeg saturam a máquina.
2. **1080×1920, 30 fps, H.264 + AAC** para shorts.
3. **Sem WebGL, Three.js ou shaders.** A GPU é Intel HD 620.
4. **Sem Docker, WSL, Hermes3D, ruflo ou Remotion** nesta máquina.
5. **Fato precisa de fonte.** Lenda precisa ser marcada como lenda.
6. **Tudo em português (PT-BR)** até o gate de expansão.
7. **Nada de reupload** de conteúdo de terceiros. `yt-dlp` só para metadados.

## Fluxo

```
briefing -> gancho -> roteiro -> shotlist -> voz -> render -> QA -> publicação -> retenção (48 h)
```

Cada etapa tem uma skill em `.opencode/skills/<id>/SKILL.md` e um artefato em `episodios/<slug>/`.

## Onde está o quê

| Caminho | Conteúdo |
|---|---|
| `MEMORIA.md` | estado de retomada (ler primeiro) |
| `docs/` | decisões, stack, nicho, plano, QA, identidade, arquitetura, histórico |
| `docs/ARQUITETURA.md` | contratos do código |
| `docs/HISTORICO.md` | linha do tempo do que foi entregue |
| `.opencode/skills/` | instruções operacionais (briefing, gancho, roteiro, voz, render, qa, publicacao, retencao) |
| `templates/misterio-45/` | composição validada + beat sheet + README |
| `biblioteca/` | ganchos, fontes, métricas |
| `episodios/` | um diretório por vídeo |
| `models/vozes/` | Piper |
| `scripts/` | instalação, verificação, voz, transcrição, QA, benchmark |
| `tools/youtube-agent-skill/` | vendor MIT: retenção, hooks.json, lint de título |
| `bench/` | composição de teste G0 |

## Ferramentas

```powershell
# versões
.\scripts\verify.ps1

# benchmark (45 s)
.\scripts\bench.ps1

# render de um episódio (segmentado; evita Target closed)
cd episodios\<slug>
$env:HF_SEGMENTED_CAPTURE = "true"
$env:HF_SEGMENT_FRAMES = "300"
$env:HF_SEGMENT_BROWSER_RECYCLE = "1"
hyperframes.cmd render --output final_raw.mp4 --quality standard --fps 30 `
  --workers 1 --low-memory-mode --protocol-timeout 600000 --resume

# normalizar loudness (medir antes; piloto usou +6,2 dB)
ffmpeg -i final_raw.mp4 -c:v copy `
  -af "volume=6.2dB,alimiter=limit=0.85:level=disabled" `
  -c:a aac -b:a 192k -movflags +faststart final.mp4

# QA técnico
.\scripts\qa.ps1 episodios\<slug>\final.mp4
```

Detalhes e armadilhas: `docs/ARQUITETURA.md` §4 e `templates/misterio-45/README.md`.

Binários em `C:\Users\valentim\Tools` (Node, Git, FFmpeg) e `.venv` (Piper, faster-whisper, yt-dlp).

## Antes de publicar

Seguir `docs/QA.md`. Sem `qa.ps1` com **QA PASS** e `qa.md` assinado, não publica. A aprovação humana do vídeo é obrigatória (gate da Fase 1).

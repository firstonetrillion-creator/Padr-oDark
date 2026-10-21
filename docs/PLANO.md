# Plano 30 / 60 / 90

## Fases e gates

| Fase | Prazo | Entrega | Gate |
|---|---|---|---|
| **0. Cérebro** | 2 dias | Node, FFmpeg, Python, Piper, HyperFrames instalados; benchmark medido | Short de 45 s renderiza em < 12 min |
| **1. Piloto** | 7 dias | Identidade + template Mistério 45 + 1 vídeo completo | Vídeo aprovado por você |
| **2. Validação** | 14 dias | 6 vídeos de Mistério 45 (piloto + 5) | Retenção média > 40% em 3 vídeos |
| **3. Repetição** | 30 dias | 30 shorts + 1 longo de 8 min | Retenção > 45% e tempo estável |
| **4. Serviço** | 60 dias | Kit + oferta mensal | 1 cliente pagante |

> **G0 medido em 20/10/2026:** 45 s em 1080×1920 renderizados em **2m32,8s** (158,8 s incluindo doctor e probe). Gate **PASS**. A máquina aguenta o formato; o gargalo agora é conteúdo, não render.

> **Fase 1 concluída e Fase 2 iniciada (21/10/2026):** piloto `001-faroleiros` — 13 cenas, 45,01 s, QA técnico **PASS** (−15,6 LUFS), template `misterio-45` extraído e **vídeo aprovado pelo usuário** (“ficou perfeito”). Piloto **publicado no YouTube Shorts**: https://youtube.com/shorts/WKuNVjl3d5M. Próximo: validação de nicho + 5 vídeos.

> **Nicho decidido em 21/10/2026:** Mistério/Arquivo é a âncora (0,10 views/inscrito por canal vs 0,06 da psicologia; 3 canais ≥1,0 vs 0). A validação passa a ser **6 vídeos de mistério** (piloto + 5), no canal **Dossiê 45** (`@Dossie45`). O rebranding visual está no ar; nome e deslistagem dos 9 shorts antigos concluídos. Falta colar a descrição de `identidade/descricao-canal.txt` antes do 002. Psicologia fica como fallback em canal novo se a retenção falhar. Dados em `docs/NICHO.md`; decisão em `docs/DECISOES.md`.

## Capacidade desta máquina

| Produção | Volume |
|---|---|
| Shorts 1080×1920, 45 s | 5–7/semana |
| Longo 8 min (a partir de shorts) | 1/semana (render noturno) |
| Render total | 2–4 h/semana |

## Rotina semanal

- Segunda: 10 ganchos + aprovação
- Terça/quarta: 3 roteiros + shotlists
- Quinta: vozes + assets
- Sexta: 3 renders + QA
- Sábado: publicação + planilha
- Domingo: análise e ajuste de gancho

## Métricas (planilha semanal)

Retenção 3 s · retenção média · conclusão · salvamentos · compartilhamentos · seguidores por vídeo.
Views e likes não decidem nada.

## Critérios de kill

- 10 vídeos sem nenhum > 40% de retenção → reescrever hooks
- 30 vídeos sem tração → trocar nicho
- > 90 min por vídeo → refazer template
- 60 dias sem cliente → reposicionar oferta

## O que NÃO entra antes do gate 3

- OpenMontage completo
- Hermes3D
- Remotion
- Automação de publicação
- Longos de 15+ min

> `codebase-memory-mcp` foi liberado após o primeiro vídeo publicado (21/10/2026); instalar fora de janela de render.

## Ferramentas de análise — youtube-agent-skill

Decisão de 21/10/2026: **adoção seletiva**, com vendor em
`tools/youtube-agent-skill/` e licença MIT preservada. O pack inteiro não foi
instalado e não substitui HyperFrames, Piper ou FFmpeg.

| Peça | Estado | Uso |
|---|---|---|
| `yt-retention/retention.py` | **adotado com patch** | CSV do Studio; 3 s e 10 s para Shorts, 30 s como legado; quedas + slide. |
| `yt-script/hooks.json` | **adotado como checklist** | Fonte das 21 fórmulas; adaptação PT-BR em `docs/GANCHOS-21.md`. |
| `yt-package/title.py` | **adotado com patch** | Lint de título + thumbnail em PT-BR. |

**Adiado para depois dos 6 vídeos:**
- `yt-viral/swipe.py` — rankeia por múltiplo sobre a mediana do canal, mas exige
  4+ vídeos por canal. Nossa amostra tem muitos canais com 1–5; o `nicho.py` já
  cobre a comparação por canal. Reavaliar quando houver mais dados.
- `yt-audit` — auditoria de canal que termina em uma correção. Faz mais sentido
  com 6+ vídeos publicados e o canal já limpo.

**Não adotado agora:** `yt-edit`, `yt-shorts`, `yt-chapters`, `yt-comment`,
`yt-plan`, `yt-seo`. Motivos em `tools/youtube-agent-skill/ORIGEM.md`.

**Não usar `hookscore.py` em PT-BR:** a heurística é em inglês e não foi
calibrada para o formato. As 21 fórmulas valem como checklist, não como score.

## Definição de pronto (por vídeo)

Ver [QA.md](QA.md).

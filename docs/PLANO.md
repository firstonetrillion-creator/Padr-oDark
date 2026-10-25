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

> **Fase 1 concluída e Fase 2 iniciada (21/10/2026):** piloto `001-faroleiros` — 13 cenas, 45,01 s, QA técnico **PASS** (−15,6 LUFS), template `misterio-45` extraído e **vídeo aprovado pelo usuário** (“ficou perfeito”). Piloto **publicado no YouTube Shorts**: https://youtube.com/shorts/WKuNVjl3d5M. **Estado em 23/10/2026:** 3/6 publicados; 003 publicado; faltam 004–006.

> **Nicho decidido em 21/10/2026:** Mistério/Arquivo é a âncora (0,10 views/inscrito por canal vs 0,06 da psicologia; 3 canais ≥1,0 vs 0). A validação passa a ser **6 vídeos de mistério** (piloto + 5), no canal **Dossiê 45** (`@Dossie45`). O rebranding visual está no ar; nome, descrição do canal e deslistagem dos 9 shorts antigos concluídos. O **002-mary-celeste** foi publicado em 21/10/2026. Psicologia fica como fallback em canal novo se a retenção falhar. Dados em `docs/NICHO.md`; decisão em `docs/DECISOES.md`.

## Execução imediata (a partir de 23/10/2026)

### Gate 1 — 23/10: retenção do 001 e do 002

- [x] Baixar o CSV de retenção do Studio para 001 e 002. O 002 veio com curva; o 001 veio vazio (sem dados).
- [x] Rodar `tools/youtube-agent-skill/yt-retention/retention.py --duration 45` nos dois arquivos. O parser foi ajustado para retenção absoluta (>100%).
- [x] Preencher `biblioteca/publicados.csv` com o que existe; salvos, compartilhados e conclusão ficam `n/d`.
- [x] Criar `episodios/001-faroleiros/retencao.md` e `episodios/002-mary-celeste/retencao.md`.
- [x] Decidir: **manter** o formato, com **ajuste de gancho** no 003. O 002 passou 3 s (91,6%) e 10 s (61,8%); o 001 ficou em 24,3% de retenção inicial e sem curva.

### 003 — publicado (23/10/2026)

- [x] Gancho aprovado, roteiro de 113 palavras e `narracao.txt`.
- [x] Voz, transcrição, composição v1, contrato e QA visual.
- [x] Render segmentado, normalização para ~−15,4 LUFS e QA técnico **PASS**.
- [x] Marca corrigida para `DOSSIÊ 45` e vídeo re-renderizado.
- [x] Aprovação humana do `final.mp4` (23/10/2026).
- [x] Publicação no YouTube Shorts — https://youtube.com/shorts/8ptxqKGe4Bk.
- [ ] Retenção em 48 h — **medida em 25/10/2026**: 3 s 92,7%, 10 s 68,5%, fim 36,1%; falta a porcentagem visualizada média do painel.

### Fila 003–006

A fila foi confirmada após o Gate 1 (23/10). Alvo: **1 vídeo a cada 2–3 dias**, concluir os 4 até **04/11/2026**, mantendo aprovação humana antes de publicar.

| Ordem | Janela-alvo | Tema | Fonte principal | Ângulo | Status |
|---|---|---|---|---|---|
| 003 | 24–26/10 | Colônia de Roanoke (1590) | *The Roanoke Voyages, 1584–1590* (David Beers Quinn, Hakluyt Society); registros do Fort Raleigh/NPS | Cerca de 117 colonos desapareceram; “CROATOAN” é a pista documentada. O que os registros permitem concluir — e o que é lenda. | **publicado** em 23/10/2026; retenção em 25/10 |
| 004 | 27-29/10 | MV Joyita (1955) | Comissão de Inquérito da Nova Zelândia em Apia (1956), relatório C. C. Marsack; Archives NZ IT1/23579122; David G. Wright, *Joyita: Solving the Mystery* | 25 pessoas desapareceram; o barco foi achado à deriva, meio submerso. O que o inquérito documenta e o que continua em aberto. | em produção; fontes validadas |
| 005 | 30/10–01/11 | Voo 19 (1945) | Relatório do Board of Inquiry da Marinha dos EUA (1945); Naval History and Heritage Command | Cinco aviões e 14 homens sem destroço. O que o relatório diz — e o que a lenda do Triângulo das Bermudas acrescentou. | candidato; validar fontes |
| 006 | 02–04/11 | Passo Dyatlov (1959) | Investigação soviética (1959); Gaume & Puzrin, *Communications Earth & Environment* (2021) | Nove caminhantes, uma barraca cortada por dentro e lesões graves. O que o inquérito registrou e o que a ciência propôs. | candidato; validar fontes |

### Gate 2 — após o 006

- [ ] Medir 48 h dos 6 vídeos e comparar com o gate da Fase 2: **retenção média > 40% em 3 vídeos**.
- [ ] Decidir a Fase 3 com dados, não por impressão.

## Melhorias visuais — backlog pós-validação

**Status: não iniciar agora.** A prioridade é validar os 6 vídeos e a retenção. O formato v1 (type-only) fica **congelado no 003–006** para não contaminar a comparação. O v2 entra depois do Gate 2, em um vídeo de teste (007) ou numa nova temporada.

### Diagnóstico
- O visual v1 é limpo, mas depende de um único gesto (texto entrando/sumindo); pode parecer “letras passando”.
- O ganho não está em trocar o HyperFrames; está em direção de arte, composição e evidência visual.

### Backlog v2 (avaliar após o Gate 2)
- 5–6 layouts: capa de dossiê, documento, mapa/rota, número, cronologia, prova e fecho.
- Tipografia como imagem: palavra gigante, corte pela borda, espaço negativo, camadas de texto.
- Textura: papel, grão, scanlines, vinheta, carimbo e faixas de redação.
- Provas visuais: mapas, recortes, documentos e fotos de domínio público, com fonte e licença registradas.
- Movimento intencional: zoom lento, parallax, máscara e carimbo; não apenas slide.
- Sound design: drone, impactos secos, papel, máquina de escrever e silêncio antes do twist.
- Capa/key art que funcione parada no feed.
- Um “frame de impacto” a cada 5–7 s.

### Critérios para adotar
- [ ] Ter fechado os 6 vídeos e o Gate 2.
- [ ] Testar em **1 vídeo A/B**, não reformar todos de uma vez.
- [ ] Comparar retenção 3 s/10 s e média com o v1; não decidir por gosto.
- [ ] Medir tempo de produção e RAM; se passar de 90 min/vídeo, recuar.

### Fora de escopo
- WebGL/Three.js, ReelMimic, OpenMontage e automação de publicação antes do gate 3.
- Trocar voz/TTS junto com o visual: uma variável por vez.

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

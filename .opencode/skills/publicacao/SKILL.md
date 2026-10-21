---
name: Publicacao
description: Use para publicar e registrar métricas de um vídeo.
---

# Publicação

## Objetivo
Publicar sem retrabalho e registrar dados para a próxima decisão.

## Checklist
- Título: curiosidade + palavra-chave, ≤ 60 caracteres.
- Descrição: 2 linhas de contexto + fonte.
- Hashtags: 3–5 específicas.
- Capa: frame mais forte, sem texto duplicado.
- Aviso de conteúdo sintético quando exigido.
- Formato: 9:16 para TikTok/Reels/Shorts.

## Lint de título + thumbnail

Antes de publicar, rodar o lint PT-BR:

```powershell
.\.venv\Scripts\python.exe tools\youtube-agent-skill\yt-package\title.py `
  --title "Mary Celeste: o navio encontrado vazio em 1872" `
  --thumb "NAVIO VAZIO"
```

- O par título+thumbnail é a unidade; se repetem a mesma palavra, um dos dois está desperdiçado.
- O score é heurístico. Corrigir os **issues** listados, não perseguir 100.
- Título e thumbnail não substituem a fonte na descrição.

## Ordem
1. YouTube Shorts (índice)
2. TikTok (alcance)
3. Reels (reaproveitamento)

## Registro
Adicionar linha em `biblioteca/publicados.csv`:

```csv
data,slug,nicho,plataforma,views_48h,retencao_3s,retencao_media,conclusao,salvos,compartilhados
```

## Pós
- 48 h: preencher métricas.
- Comentários: objeções viram gancho.
- Decisão: manter formato, ajustar gancho ou matar.

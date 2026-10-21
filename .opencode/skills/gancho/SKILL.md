---
name: Gancho
description: Use para gerar e escolher o gancho dos primeiros 2 segundos de um short.
---

# Gancho

## Objetivo
Garantir retenção nos primeiros 2 segundos.

## Regras
- Primeira frase ≤ 9 palavras.
- Nada de "hoje vamos falar sobre".
- Começar com tensão, número ou contradição.
- O visual do frame 1 já conta parte da história.
- O gancho promete algo que o vídeo entrega.

## Fórmulas
1. **Contradição:** "Este arquivo foi apagado. E ele ainda existe."
2. **Número:** "Três pessoas entraram. O registro só tem duas saídas."
3. **Ordem:** "Não leia a última página."
4. **Consequência:** "Quem ouviu a fita não dormiu mais."

## Checklist de 21 fórmulas
Consultar `docs/GANCHOS-21.md` (adaptação PT-BR de
`tools/youtube-agent-skill/yt-script/hooks.json`).
- Escolher **uma fórmula dominante**; híbridos podem, mas sem empilhar promessas.
- Aplicar o checklist de aprovação do documento.
- **Não** usar `hookscore.py`: a heurística é em inglês e não foi calibrada para PT-BR.
- Fórmulas de primeira pessoa (“Eu Testei”, “O Resultado de Outro”) têm baixo
  encaixe na voz impessoal do Dossiê 45.

## Processo
1. Gerar 10 ganchos.
2. Eliminar os que dependem de contexto.
3. Testar em voz alta: cabe em 2 s?
4. Escolher 1 e escrever a linha visual do frame 1.
5. Registrar a fórmula escolhida em `gancho.md`.

## Saída
`episodios/<slug>/gancho.md` com 10 opções e o escolhido.

## Banco
Consultar `biblioteca/ganchos.md`.

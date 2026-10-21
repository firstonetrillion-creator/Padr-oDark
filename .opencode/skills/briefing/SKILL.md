---
name: Briefing
description: Use ao iniciar um episódio para fechar promessa, fato central, twist e limite de escopo.
---

# Briefing

## Objetivo
Transformar um tema bruto em um briefing fechado, com ângulo, fato central e limite de escopo.

## Entrada
- Tema ou pergunta
- Nicho (mistério / psicologia)
- Duração alvo (45 s padrão)

## Passos
1. Escrever a promessa em uma frase: "Este vídeo mostra que ___".
2. Definir o fato central verificável (fonte primária).
3. Definir o twist (o que o espectador não espera).
4. Listar 3 pistas que sustentam a escalada.
5. Marcar o que é fato, lenda ou especulação.
6. Escrever o limite: o que o vídeo NÃO vai responder.

## Saída
`episodios/<slug>/briefing.md` com:

```md
# <título de trabalho>
- Promessa:
- Fato central:
- Fonte:
- Twist:
- Pistas: 1) 2) 3)
- Classificação: fato | lenda | ficção
- Limite:
```

## Critério de aprovação
- A promessa cabe em 12 palavras.
- O fato central tem fonte citável.
- O twist não depende de mentir.

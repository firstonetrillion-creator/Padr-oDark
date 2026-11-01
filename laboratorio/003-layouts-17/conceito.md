# LAB 003 — os 17 estilos, um por cena

**Data:** 31/10/2026 · **Duração:** 45,0 s · **Cenas:** 17 · **Voz:** Piper, 17 blocos

## O que este laboratório testa

O usuário pediu 17 estilos de vídeo. Antes de qualquer episódio usá-los, este LAB
responde três perguntas de uma vez:

1. **O motor se sustenta?** Uma cena por layout, 17 layouts, o mesmo
   `gerar-episodio.py`, o mesmo contrato (`data-start`, `autoClip`, `?t=`).
2. **Quanto custa na máquina?** 17 cenas animadas em 45 s no Chrome headless da
   Intel HD 620, medido em tempo de render e em frames perdidos.
3. **O que quebra no frame?** Tinta acima de 840 px, título quebrando em 3
   linhas, decoração por cima do texto.

**Não testa** retenção. Nada aqui vai para o YouTube: é um contact sheet falado,
com o nome de cada estilo na narração, para o usuário aprovar ou cortar estilos.

## Desenho

- Uma cena por estilo, na ordem do pedido do usuário.
- `kicker` = nome do estilo em inglês (é o que o usuário vai reconhecer).
- `titulo` = duas linhas curtas em PT-BR, para medir tinta.
- `pequeno` = uma linha explicando o gesto.
- Narração = uma frase por cena nomeando o estilo (~2 s de fala por cena).

Falas curtas de propósito: 45 s ÷ 17 = 2,6 s por cena. Frase longa comeria o
tempo e o LAB viraria um episódio.

## Critério de aprovação

- Contrato **OK** (`check-contrato.ps1`) e render sem frame perdido.
- Nenhum título com **3 linhas** onde o roteiro pediu 2.
- Texto legível em todos, inclusive `phone-mockup` (fonte a 55%) e `glass-type`.
- Custo de render dentro da faixa de um episódio normal (±20%).

`ESTOURA` nos layouts de câmera (`digital-zoom`, `vertigo`, `pull-back`,
`zoom-through`) **não reprova**: o zoom sai dos 840 px por desenho.

## O que fica depois

- `qa.md` com os números e os 7 frames de conferência.
- Correções aplicadas em `templates/layouts/` (não neste laboratório: a
  biblioteca é o produto, o LAB é a prova).

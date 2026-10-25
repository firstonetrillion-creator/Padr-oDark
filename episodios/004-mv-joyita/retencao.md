# Retenção — 004 MV Joyita

> **Janela medida: 24 h** (24/10 19:00 → 25/10). O export de 48 h entra em
> **26/10/2026** e substitui os números abaixo em `retencao.csv`.

## Janela medida (24 h)

- **CSV:** `retencao-24h.csv` (export “Todos”, retenção absoluta; normalizado
  pela primeira amostra, que vem acima de 100% por loops).
- **Views:** **1.066** (1.053 às 24 h); **21 likes**.
- **Curva:** 100% → **17,3%** no fim (44,5 s).

## 3 s / 10 s

| Janela | Retenção | Meta provisória | Status |
|---|---:|---:|---|
| 3 s | **90,9%** | ≥ 70% | **PASS** |
| 10 s | **43,4%** | ≥ 45% | **ABAIXO** |
| 30 s | 24,8% | legado long-form | — |
| fim (44,5 s) | **17,3%** | — | — |

## Comparação com o 003

| Métrica | 003 (48 h) | 004 (24 h) |
|---|---:|---:|
| Views | 370 | **1.066** |
| 3 s | 92,7% | 90,9% |
| 10 s | 68,5% | **43,4%** |
| fim | 36,1% | **17,3%** |

**O gancho de clique é forte; a entrega não sustenta.** O 004 teve ~3× as views
do 003 e quase o mesmo 3 s — mas perde **25 p.p.** a mais até os 10 s. Ou seja:
o paradoxo “vazio… e ainda flutuava” trouxe gente; o que veio depois espantou.

## Onde perde — e a hipótese que se confirmou

As quedas se concentram em **4,0–8,6 s**, dentro da **cena 2** — exatamente o
cartão estático de 6,57 s que ficou marcado como alerta no `qa.md`:

- 4,0 → 4,5 s: **−5,1 p.p.** (11,4 p.p./s)
- 5,0 → 5,4 s: −3,8 p.p.
- 5,4 → 5,8 s: −4,6 p.p. (10,2 p.p./s)
- 7,2 → 7,7 s: **−5,4 p.p.** (12,0 p.p./s)
- 8,1 → 8,6 s: −3,8 p.p.

O áudio nesse trecho é só contexto: “Em 3 de outubro de 1955, o Joyita saiu de
Apia rumo a Tokelau. Levava 25 pessoas.”

**Diagnóstico:** o público aceitou o mistério e recebeu, como recompensa, uma
ficha técnica de 6 segundos parada na tela. Não é a duração da cena em si — é a
**função** dela: quatro dados (data, origem, destino, número) sem consequência
nem imagem. Depois dos 10 s a curva desce em slide (−26,1 p.p. até 44,5 s,
0,76 p.p./s), mas o dano grande já foi feito ali.

## Ressalva honesta: quanto da queda é cena 2 e quanto é alcance

O 004 não é uma comparação limpa com o 003. Ele foi **empurrado para um público
3× maior** (1.066 views em 24 h contra 370 em 48 h), e audiência mais fria
sempre retém menos — a primeira amostra da curva diz isso: **123,3% no 004**
contra **162,0% no 003**, ou seja, o 003 foi reassistido muito mais (loops).

Então a queda de 10 s pode ter duas causas somadas:

1. **Composição** — o cartão estático de 6,57 s (3,03–9,60 s), que é onde as
   cinco maiores quedas acontecem. Esta parte é observável na curva: os
   **−22,7 p.p.** perdidos entre 4,0 e 8,6 s são **48%** de toda a perda até os
   10 s (47,5 p.p.), num trecho de 4,6 s — 10% da duração do vídeo.
2. **Alcance** — feed mais largo traz gente menos interessada, e isso derruba
   3 s, 10 s e média de uma vez, sem culpa de nenhuma cena.

O teste que separa as duas: **005 e 006 sem cartão de contexto**. Se o 10 s
voltar para ≥55% com alcance parecido, a causa era a composição. Se continuar
baixo mesmo com menos views, a causa é o formato/gancho e o problema é outro.

## Regra para 005 e 006

1. **Nunca um cartão parado de contexto depois do gancho.** Data/origem/número
   entram em ≤2 s, ou colados a uma consequência (“saiu de Apia com 25
   pessoas — e nunca chegou”).
2. **O beat seguinte ao gancho tem de subir a aposta**, não organizar o assunto.
3. **Um dado por cartão.** O 004 empilhou quatro na mesma cena.
4. **Fecho com consequência nova**, não com resumo (lição do 003).

## Pendente (26/10)

- Export de 48 h → `retencao.csv`; conferir se 10 s estabiliza acima ou abaixo
  de 45%.
- Números do painel: porcentagem visualizada média, duração média e “ficaram
  para assistir”.
- Só então preencher a linha do 004 em `biblioteca/publicados.csv` (hoje `n/d`,
  porque a coluna é de 48 h).

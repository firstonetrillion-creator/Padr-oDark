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

## Painel do Studio (25/10, ~26 h)

| Métrica | 003 Roanoke | 004 MV Joyita |
|---|---:|---:|
| Views | 370 (48 h) | **1.141** (48 h) / 1.066 em 24 h |
| Ficaram para assistir | 52,6% | **53,4%** |
| Duração média | 0:40 de 0:46 | **0:21 de 0:46** |
| **% média assistida** | 87,0% | **45,7%** |
| Shorts feed | 92,2% | **98,9%** |

**Isto muda a leitura do gancho.** “Ficaram para assistir” do 004 (**53,4%**) é
*maior* que a do 003 (52,6%) e bem maior que a do 002 (48,3%). Ou seja: **não
perdemos mais gente no início** — perdemos no **meio**. A duração média caiu de
0:40 para **0:21**, metade do vídeo.

Isso é coerente com a curva (slide até 17,3%) e aponta para o **miolo**, não
para o gancho: o público que ficou não foi embora no clique seguinte, foi
escorrendo enquanto o vídeo organizava o assunto.

## A descoberta que vale mais que o 004: a métrica escorrega

Em 26/10 o mesmo painel, com login, mostrou **duração média menor nos vídeos
antigos**:

| Vídeo | Duração média em 25/10 | Duração média em 26/10 | % média assistida |
|---|---:|---:|---:|
| 002 Mary Celeste | 0:40 | **0:35** | 87,0% → **76,1%** |
| 003 Roanoke | 0:40 | **0:39** | 87,0% → **84,8%** |
| 004 MV Joyita | 0:21 | 0:21 | 45,7% → 45,7% |

“Ficaram para assistir” quase não muda (002: 48,3% → 48,6%; 003: 52,6% →
53,0%). **O que escorrega é a duração média.** O motivo é aritmético: cada view
nova vem de um feed mais frio e assiste menos, então a média global cai com o
tempo, mesmo sem nada piorar no vídeo.

Consequência para o **Gate 2**, que lê “% média assistida > 50%”:

> A régua tem de ter **janela fixa (48 h)**. Comparar o 005 medido em 48 h com o
> 002 medido em 5 dias seria comparar públicos diferentes. E o 003 já está
> **84,8%**, não 87,0% — o número de 25/10 era um retrato do momento, não um
> atributo do vídeo.

Isso **não reabre** a conclusão: 84,8% e 76,1% continuam muito acima de 45,7%.

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

## Fechamento em 48 h (lido em 26/10, com login)

| Métrica | 004 MV Joyita |
|---|---:|
| Views | **1.200** |
| Espectadores únicos | **296** |
| Inscritos | **+1** |
| Ficaram para assistir | **54,0%** |
| Duração média | **0:21** de 0:46 |
| **% média assistida** | **45,7%** |
| Shorts feed | **98,9%** |

**A duração média não se mexeu** (0:21 em 24 h e em 48 h) e o “ficaram para
assistir” subiu de 53,4% para **54,0%**. Confirma a leitura: o problema não é o
gancho. O vídeo perde 45% da audiência que já ficou.

> O export `Todos.csv` de 48 h **não foi gerado** — a aba Content do Studio
> falhou em todas as tentativas (ver `MEMORIA.md` §7). Os valores de curva
> (3 s, 10 s, fim) continuam os de 24 h, e são os que valem para o Gate 2.

### Para onde foi o tráfego

| Origem | Views |
|---|---:|
| Shorts feed | **98,9%** |
| Outros recursos do YouTube | 0,5% |
| Busca no YouTube | 0,4% |
| Direto ou desconhecido | 0,1% |
| Páginas de canal | 0,1% |

Os 0,4% de busca são ruído puro: **“budismo ensinamentos” (20%)** e
**“virgínia fonseca” (20%)** dos termos. Ninguém procurou o Joyita. O vídeo não
tem demanda de busca — vive e morre no feed.

### Quem assistiu

Detalhe em `biblioteca/publico.md`. O essencial, que muda a estratégia:

- **82,1% tem 55 anos ou mais** (65+ 39,2% · 55–64 42,9% · 45–54 17,9%) e
  **0% abaixo de 45**. Masculino 78,2%.
- **Celular 94,7%** do tempo de exibição.
- **Brasil é só 49,2%** das views: metade da audiência é estrangeira, num vídeo
  em português.
- **296 pessoas** para 1.200 views — ~4 views por espectador.

Não é o público que o formato imaginava. É o público que o formato **encontrou**.

## Pendente

- [ ] Export `Todos.csv` de 48 h, quando a aba Content voltar — só para os
      valores de curva (10 s e fim), que são o que o Gate 2 lê.
- [x] Linha do 004 em `biblioteca/publicados.csv` — preenchida em 26/10.

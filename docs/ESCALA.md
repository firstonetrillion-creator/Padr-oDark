# ESCALA — modelar o que funciona, e o que isso não resolve

> Escrito em **26/10/2026**, depois de medir o canal com login e construir o
> `scripts/scout.py`. Este documento existe para não perder o raciocínio: a
> pergunta "por que não copiar um canal grande e acelerar?" volta toda semana, e
> a resposta tem número.

## A pergunta

Com 4 vídeos publicados e ~2 dias de trabalho por vídeo, dá para acelerar
modelando canais que já crescem rápido? A intuição: se o conteúdo é o gargalo,
copiar o que funciona é mais rápido que descobrir.

**A intuição está meio certa — e o gargalo é outro.**

## O que modelar copia, e o que não copia

| Copiável (visível de fora) | Invisível |
|---|---|
| Duração e cadência de publicação | **Curva de retenção** |
| O que está na tela no frame 0 | Onde exatamente ele perde gente |
| Texto por cartão, número de cartões | Ritmo das revelações |
| Seleção de tema (o que repete) | Peso do desenho sonoro |
| Nome de série, padrão de título e capa | Por que o miolo segura |

A coluna da direita é **exatamente** onde o Dossiê 45 está perdendo. O 004 fez
**0:21 de 0:46**. O YouTube não publica retenção de terceiros.

**Portanto:** modelar importa o *pacote visível* e deixa o *mecanismo* para trás.
Não é inútil — é metade.

## O erro que views cometem

O 004 teve **3× as views** do 003 e **metade** da retenção.

| Vídeo | Views | % média assistida |
|---|---:|---:|
| 003 Roanoke | 370 | 84,8% |
| 004 MV Joyita | **1.200** | **45,7%** |

Se a régua fosse views, a conclusão seria "o 004 é o melhor vídeo do canal" — e
estaria errado. **Views não são o modelo; são o sintoma.** Um canal com milhões
de views pode ser um desastre de retenção.

## O único proxy externo de retenção

**O algoritmo insistindo.** Quando o YouTube continua empurrando um short para
público frio, é porque os primeiros segundos seguram — senão ele corta a
distribuição em horas. Isso aparece em metadados como:

- **views por inscrito** alto (o vídeo passa muito além da base);
- **breakouts repetidos** (vários shorts muito acima da mediana do canal);
- **aceleração** (as 5 publicações mais recentes acima das anteriores).

Nenhum é retenção. Todos são o *efeito* de retenção. É o que existe.

## `scripts/scout.py` — o que ele mede

Descobre-se que **yt-dlp não serve para descobrir canal**. Testado em 26/10 com
2026.08.19:

- os filtros de busca do YouTube (`sp` de Shorts, `sp` de ordenar por data) são
  **ignorados** pelo extrator;
- `ytsearchdate` **não existe** nesta versão;
- `/hashtag/truecrime` devolve 135 canais quase todos em inglês;
- busca por relevância devolve **3 Shorts em 40 resultados**.

Então o fluxo é invertido de propósito: **humano descobre, máquina mede**.

O que funciona: `yt-dlp -J --flat-playlist` na aba `/shorts` de um canal. Ela vem
ordenada do mais novo para o mais antigo — **posição = recência**, sem precisar
de data. Views vêm arredondadas, o que basta para razões.

| Métrica | Fórmula | Lê |
|---|---|---|
| Aceleração | mediana das 5 mais recentes ÷ mediana das antigas | >1,5× = subindo agora · <0,7× = passou o pico |
| Breakout | maior short ÷ mediana | o vídeo que furou a bolha |
| Views/inscrito | mediana ÷ inscritos | proxy de retenção |
| Shorts lidos | quantos a janela alcançou | poucos + mediana alta = canal novo com tração |

`--diff` compara dois snapshots e devolve **views/dia dos mesmos shorts** — a
única medida honesta de "crescendo rápido". Um rank de leitura única não decide
nada; velocidade exige duas datas.

### 1ª rodada — 26/10, 12 canais do nicho arquivo/mistério

| Canal | Score | Aceleração | Views/inscr. | Mediana | 5 novos | Inscr. |
|---|---:|---:|---:|---:|---:|---:|
| Wakinho | 25,5 | 1,82× | 0,04 | 14k | 18k | 351k |
| Crimes que Marcaram | 23,6 | 1,35× | 0,99 | 21k | 21k | 21k |
| Arquivo Sem Rastros | 22,3 | **7×** | 0,10 | **44** | 273 | 442 |
| TechTerror | 21,7 | 1,48× | 0,06 | 3k | 3k | 58k |
| De Olho — Caminhos do Medo | 20,6 | **4,01×** | 0,23 | **170** | 297 | 740 |
| Pequeno Contexto | 20,2 | 0,87× | 1,75 | 4k | 4k | 3k |
| Cafezinho Investigativo | 17,2 | 0,61× | 0,04 | 22k | 19k | 567k |
| Ossos Perdidos | 17,1 | 1,00× | 0,01 | 17k | 18k | 1,53M |
| Cofre dos Mistérios | 17,0 | 2,55× | 0,17 | **111** | 154 | 664 |
| Mistérios Resolvidos | 16,3 | 0,58× | 0,02 | 4k | 4k | 191k |
| Penumbroo | 14,7 | **0,09×** | 4,57 | 877 | **201** | 192 |
| Dr. Misterio | 13,8 | 0,60× | 0,003 | 939 | 599 | 311k |

**Leitura:**

1. **Nenhum canal combina volume e aceleração.** Só o Wakinho passa de 5k de
   mediana *e* 1,5× de aceleração — e ele é curiosidades, não arquivo.
2. **Quem acelera forte é minúsculo.** Arquivo Sem Rastros (7×) tem mediana de
   **44 views**; Cofre dos Mistérios (2,55×), 111. Razão em volume baixo é
   ruído: 44 → 273 dá "7×" e não significa nada.
3. **Quem tem volume está parado ou caindo.** Penumbroo em **0,09×** é colapso
   (877 → 201). Ossos Perdidos, 1,0× com 1,53M de inscritos.
4. **Só 3 canais passam de 0,5 views/inscrito** — e um deles está morrendo.

**Conclusão honesta:** neste nicho, nesta amostra, **não há máquina de breakout
para copiar.** Três explicações possíveis, e a diferença importa:

- o nicho é raso (arquivo/mistério em PT-BR não tem vencedor consistente);
- os vencedores estão num nicho adjacente (true crime, documentário);
- as sementes estão erradas — 12 canais montados em 10 minutos é amostra pequena.

Não decidir entre as três antes da 2ª rodada é o erro a evitar.

## O gargalo real: vazão, não ideia

| Fato | Número |
|---|---|
| Vídeos publicados | 4 em 6 dias |
| Cadência | ~2 dias por vídeo |
| Curvas necessárias para sinal | 20–30 |
| Tempo até ter sinal, nesta cadência | **~2 meses** |

Em dois meses sem mudar nada, o aprendizado é o mesmo de hoje. **Esse** é o
problema de escala.

E o motivo de 2 dias por vídeo é técnico: cada episódio é um `index.html`
escrito à mão, voz calibrada por episódio, remapeamento manual de tempos.
`check-contrato.ps1` já automatiza a *verificação*; falta a *geração*.

### O que multiplica por 10

Episódio vira **dado** (`roteiro.json`) → um gerador emite `index.html` e os
tempos → voz em lote. Um vídeo passa a ser ~2 horas em vez de 2 dias.

Efeito colateral que é o ponto: o A/B do Gate 2 deixa de ser **1 teste caro** e
vira **5 variantes na mesma semana**.

## Plano adotado (26/10/2026)

1. **Humano alimenta o scout** — 5 min rolando Shorts do nicho na própria conta,
   colando canais em `biblioteca/canais-semente.txt`. Alvo: faceless,
   tipográfico, 40–60 s, arquivo/mistério. 20 canais bastam.
2. **2ª rodada do scout em 48–72 h** com `--diff` → velocidade real.
3. **Assistir 10 shorts com cronômetro**, marcando a entrada de cada cartão.
   Isso nenhum scraper entrega e provavelmente rende mais que todo o resto.
4. **Construir o gerador** (`scripts/gerar-episodio.py`): `roteiro.json` →
   `index.html` com cenas e tempos. Aplicar em 005, 006 e no A/B.
5. **Não escalar o formato antes do Gate 2.** Escalar agora produz 20 vídeos a
   45% de retenção.

### Ordem de execução acordada

```
documentar  ->  005 (voz, remap, render, QA)  ->  LAB 001  ->  gerador  ->  A/B
```

## O que este documento NÃO afirma

- Não afirma que modelar é inútil. Afirma que modelar entrega **tema e
  empacotamento**, não retenção.
- Não afirma que o nicho morreu. Afirma que 12 canais não bastam para decidir.
- Não afirma que views não importam. Afirma que views **sozinhas** já enganaram
  uma vez (004), e vão enganar de novo.

## Evidência

- `logs/scout-2026-10-26.json` — snapshot completo dos 12 canais.
- `biblioteca/publico.md` — perfil do público medido (82,1% com 55+, Brasil 49,2%).
- `episodios/004-mv-joyita/retencao.md` — a queda do miolo e a métrica que escorrega.
- `scripts/scout.py`, `biblioteca/canais-semente.txt`.

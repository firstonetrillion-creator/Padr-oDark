# Retenção — 007 Somerton

> Curva exportada do Studio em **06/11/2026**, janela **02–06/11** (4 dias).
> Arquivo: `retencao.csv` (export "Todos"). Cálculo em `retention.py`
> (`--duration 45`) + integral da curva.
> **Atenção:** a janela é de 4 dias, não de 48 h — os números são um piso.

## Números

| Métrica | Valor |
|---|---|
| Views (acumuladas) | 1.265 |
| 3 s | **94,0%** |
| 8 s (proxy de "ficaram") | 51,6% |
| 10 s | **41,0%** |
| Fim (44,5 s) | **8,5%** |
| **% média assistida** | **34,9%** |
| Slide de 10 s a 44,5 s | −32,5 p.p. (0,94 p.p./s) |

## Onde perde

Maior queda: **−8,5 p.p. entre 5,0 s e 5,4 s** (18,9 p.p./s), com mais duas
quedas grandes em 4,5–5,0 s (−7,3) e 5,8–6,3 s (−5,9). Somando, o vídeo perde
**~27 p.p. entre o 4º e o 6º segundo**.

O que está na tela: a **cena 1** (`UM HOMEM MORTO / NA PRAIA. / UM CÓDIGO /
NA ROUPA.`) vai de 0 a 4,04 s; a **cena 2** (`O CORPO / NÃO TINHA / ETIQUETA.`)
entra em 4,04 s e sai em 7,66 s. A queda inteira acontece **na virada para a
cena 2 e no primeiro segundo dela**.

## Diagnóstico

**Gancho: o melhor do canal.** 94,0% em 3 s, acima do 004 (90,9) e do 006.
**Miolo: o pior do lote.** Slide de −32,5 p.p. e fim em 8,5% — o vídeo não
perde num ponto, sangra até o fim. O `% média` de 34,9% é o menor de todos os
vídeos medidos.

**Uma correção:** a cena 2 é a primeira e única chance depois do gancho, e ela
gasta 3,6 s num fato negativo e estático ("não tinha etiqueta"). Trocar por
consequência em movimento — o que o corpo *tinha* — é a mudança de uma variável.

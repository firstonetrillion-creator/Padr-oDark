# Retenção — 010 Carroll A. Deering

> Curva exportada do Studio em **06/11/2026**, janela **04–06/11** (~48 h).
> Arquivo: `retencao.csv` (export "Todos"). Cálculo em `retention.py`
> (`--duration 45`) + integral da curva. **Esta é a janela do gate.**

## Números

| Métrica | Valor |
|---|---|
| Views (acumuladas, ~48 h) | 522 |
| 3 s | **90,1%** |
| 8 s (proxy de "ficaram") | **37,8%** |
| 10 s | **31,7%** |
| Fim (44,5 s) | 14,8% |
| **% média assistida** | **40,7%** |
| Slide de 10 s a 44,5 s | **−16,8 p.p.** (0,49 p.p./s) |

## Onde perde

Maior queda: **−9,9 p.p. entre 5,8 s e 6,3 s** (22,0 p.p./s), seguida de −8,9
em 5,0–5,4 s e −6,9 em 4,5–5,0 s e 5,4–5,8 s. Entre o 4º e o 8º segundo perde
**~45 p.p.** — a maior perda de gancho do lote.

O que está na tela: **cena 1** (`O NAVIO / VEIO VAZIO.`, `digital-zoom`) até
4,49 s; **cena 2** (`A BORDO, / NINGUÉM.`) de 4,49 a 7,81 s; **cena 3**
(`ONZE / HOMENS.`) entra em 7,81 s.

## Diagnóstico

**O oposto do 007: gancho fraco, miolo forte.** É o pior começo do lote (10 s em
31,7%) e o **melhor corpo** (slide de −16,8 p.p., metade do 007). Depois dos 15 s
o vídeo praticamente não perde ninguém: 15 s = 28,7% e 20 s = 28,7%.

**Uma correção:** o gancho de duas batidas ("vazio" / "ninguém") não sustenta o
mesmo peso do de três batidas do 009. Testar a terceira batida emprestada do
fato mais forte do caso (onze homens, nenhum corpo, nenhum bote) na cena 1.

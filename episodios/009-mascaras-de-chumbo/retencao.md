# Retenção — 009 Máscaras de chumbo

> Curva exportada do Studio em **06/11/2026**, janela **04–06/11** (~48 h).
> Arquivo: `retencao.csv` (export "Todos"). Cálculo em `retention.py`
> (`--duration 45`) + integral da curva. **Esta é a janela do gate.**

## Números

| Métrica | Valor |
|---|---|
| Views (acumuladas, ~48 h) | 1.657 |
| 3 s | **93,7%** |
| 8 s (proxy de "ficaram") | 48,5% |
| 10 s | **42,7%** |
| Fim (44,5 s) | **15,2%** |
| **% média assistida** | **42,8%** |
| Slide de 10 s a 44,5 s | −27,5 p.p. (0,80 p.p./s) |

## Onde perde

Maior queda: **−10,1 p.p. entre 4,0 s e 4,5 s** (22,4 p.p./s), seguida de
−6,4 em 5,0–5,4 s e −5,4 em 4,5–5,0 s.

O que está na tela: a **cena 1** (`DOIS MORTOS / NO MORRO.`, em `digital-zoom`)
termina em **4,34 s**; a **cena 2** (`ELES IAM / A SÃO PAULO.`) entra em 4,34 s.
A maior queda do vídeo é **exatamente a virada da cena 1 para a cena 2** — o
corte, não o texto.

## Diagnóstico

**O melhor vídeo do lote em distribuição** (1.657 views) e o melhor `% média`
entre os quatro (42,8%). O gancho segura (93,7% em 3 s), mas o **corte do
primeiro cartão custa 10 p.p. em meio segundo** — e o mesmo padrão aparece nos
outros três.

**Uma correção:** encurtar a cena 1 para ~3,5 s ou entrar na cena 2 com
continuidade visual (mesmo enquadramento/elemento) em vez de corte seco. O
conteúdo da cena 2 está certo; a transição é que cobra o preço.

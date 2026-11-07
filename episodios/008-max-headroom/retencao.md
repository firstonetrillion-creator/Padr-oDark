# Retenção — 008 Max Headroom

> Curva exportada do Studio em **06/11/2026**, janela **02–06/11** (4 dias).
> Arquivo: `retencao.csv` (export "Todos"). Cálculo em `retention.py`
> (`--duration 45`) + integral da curva.
> **Atenção:** a janela é de 4 dias, não de 48 h — os números são um piso.

## Números

| Métrica | Valor |
|---|---|
| Views (acumuladas) | 1.222 |
| 3 s | **94,1%** |
| 8 s (proxy de "ficaram") | 51,5% |
| 10 s | **44,4%** |
| Fim (44,5 s) | **15,1%** |
| **% média assistida** | **42,5%** |
| Slide de 10 s a 44,5 s | −29,3 p.p. (0,85 p.p./s) |

## Onde perde

Maior queda: **−9,3 p.p. entre 5,4 s e 5,8 s** (20,6 p.p./s), seguida de
−6,7 em 5,8–6,3 s e −6,1 em 5,0–5,4 s. Entre o 4º e o 7º segundo o vídeo perde
**~36 p.p.** — a maior sangria concentrada do lote.

O que está na tela: a **cena 1** (`DOIS CANAIS / INVADIDOS / AO VIVO.`, em
`digital-zoom`) vai de 0 a 4,40 s; a **cena 2** é **`CHICAGO, / 1987.`**, de
4,40 a 9,05 s. A queda acontece inteira dentro dessa cena.

## Diagnóstico

**O 008 viola a regra do próprio lote.** A variável do lote era "sem cartão de
contexto depois do gancho" — e a cena 2 é exatamente um cartão de contexto
(lugar + data), com 4,65 s de duração. É o pior trecho do vídeo.

**Uma correção:** trocar `CHICAGO, 1987.` por uma consequência do que acabou de
acontecer (o que saiu do ar, o que o público viu). O gancho não precisa da
localização; o rodapé e a descrição já a entregam.

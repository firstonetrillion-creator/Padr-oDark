# Retenção — 003 Roanoke

## Janela medida

- **YouTube Studio:** 23/10/2026–25/10/2026 (48 h).
- **CSV:** `retencao.csv` (export avançado “Todos”, retenção absoluta;
  normalizado pela primeira amostra, que vem acima de 100% por causa de loops).
- **Views:** **370** no painel (368 no `yt-dlp` no mesmo dia); +**1 inscrito**;
  **1,96 h** de watch time; 41 impressões de miniatura, CTR 0% (Shorts não
  conta o feed como impressão).
- **Curva:** 100% → **36,1%** no fim (44,5 s).

## 3 s / 10 s

| Janela | Retenção | Meta provisória | Status |
|---|---:|---:|---|
| 3 s | **92,7%** | ≥ 70% | **PASS** |
| 10 s | **68,5%** | ≥ 45% | **PASS** |
| 30 s | 40,8% | legado long-form | — |
| fim (44,5 s) | **36,1%** | — | — |

## Comparação com o 002

| Métrica | 002 Mary Celeste | 003 Roanoke |
|---|---:|---:|
| 3 s | 91,6% | **92,7%** |
| 10 s | 61,8% | **68,5%** |
| fim | 42,2% | 36,1% |

**O ajuste de gancho do Gate 1 funcionou:** o 003 ganha nas duas janelas que
importam para Shorts. Mas **perde no fim**: a curva do 003 cai 32,4 p.p. entre
10 s e 44,5 s (0,94 p.p./s), contra uma queda menor no 002.

## Onde perde

Quedas concentradas entre **4,5 s e 8,1 s**, no trecho em que a palavra
CROATOAN é entregue **e imediatamente explicada**:

- 4,5 → 5,0 s: **−3,2 p.p.** (7,2 p.p./s)
- 5,4 → 5,8 s: −2,5 p.p.
- 6,3 → 6,8 s: −2,5 p.p.
- 7,7 → 8,1 s: −2,5 p.p.
- 43,6 → 44,1 s: −2,5 p.p. (fecho)

**Diagnóstico:** não é uma queda única — é **slide**. O público entra (3 s em
92,7%) e vai saindo em ritmo constante. A causa provável é a escolha de beat:
o 003 paga a promessa do gancho em 3,75 s e passa os 6 s seguintes explicando
que “não era um código, era o nome de um lugar”. Curiosidade resolvida cedo =
saída constante.

## Correção para o 004/005

- **Reter a explicação.** Entregar a pista sem traduzi-la na mesma cena; a
  explicação vem depois de uma consequência, não imediatamente.
- **Uma ideia por cartão**, sem emenda de duas frases na mesma cena (o trecho
  4,5–8,1 s tem duas ideias no mesmo beat).
- **Fecho não é resumo.** O 003 gasta os últimos 3,5 s repetindo o que o vídeo
  já disse; foi a última queda relevante (−2,5 p.p. em 43,6 s).
- O 004 já nasceu com o gancho em paradoxo (“vazio… e ainda flutuava”) e sem
  entregar a explicação na cena 2 — a hipótese a testar em 26/10 é se isso
  sustenta a curva depois dos 10 s.

## Pendente

- **Porcentagem visualizada média** do painel (o 002 registrou 87,0%): não é
  derivável do CSV; precisa do número do cartão de retenção no Studio.
- **Duração média** e **“ficaram para assistir”** do mesmo cartão.

## Linha em `biblioteca/publicados.csv`

`2026-10-23,003-roanoke,misterio,YouTube Shorts,370,92.7,n/d,n/d,n/d,n/d`

> `conclusao` fica `n/d` para manter a mesma definição do 001 e do 002. O fim
> da curva (**36,1%**) está na tabela acima.

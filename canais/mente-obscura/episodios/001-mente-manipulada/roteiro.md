# Roteiro — 001 (45 s) — canal mente-obscura

> **~101 palavras escritas** em **15 cenas** — ~2,2 palavras/s.
> **Voz:** Piper `pt_BR-faber-medium`, `length_scale` **1.20**, sintetizada **cena por cena** (`scripts/montar-voz.py`).
> **Tom:** sombrio, seco, sem adjetivos vazios. Uma ideia por frase.
> **Estrutura:** gancho → contexto → 3 pistas → twist → fecho.
> **Fonte:** Zenão de Cítio (estoicismo, c. 300 a.C.); Nicolau Maquiavel, *O Príncipe* (1513/1532); Paulhus & Williams (2002).
> **Visual reforçado:** variação de fonte (cenas grandes e pequenas alternadas), fundo em movimento lento (scale GSAP já no template), destaque (`.accent`) animado, possível flicker nos momentos de tensão via CSS. Sem WebGL/Three.js/shaders.
> **Áudio reforçado:** voz em 1,0; bed sonoro audível (não drone inaudível); pulsos de impacto gerados por FFmpeg lavfi.

## Gancho (0,00–2,40 s)

**Tela:** A MENTE · MANIPULAÇÃO / VOCÊ É MANIPULADO. / NÃO SENTE NADA.

**Voz:** Você é manipulado agora. E não sente nada.

## Contexto (2,40–6,60 s)

**Tela:** kicker A MENTE · MANIPULAÇÃO / ESTOICISMO / ENSINA / A / SE / DOMINAR / MAQUIAVEL / VIROU / A / MENTE / EM / INSTRUMENTO / DE / PODER

**Voz:** Há mais de dois mil anos, o estoicismo ensina a dominar a si mesmo. Séculos depois, Maquiavel virou essa mesma mente em instrumento de poder.

## Pista 1 — O estoico (6,60–11,20 s)

**Tela:** O ESTÓICO / CONTROLA / APENAS / O PRÓPRIO JULGAMENTO. / O RESTO É INDIFERENTE.

**Voz:** Primeiro: o estoico controla apenas o próprio julgamento. Tudo o resto é indiferente.

## Pista 2 — O maquiavelista (11,20–16,00 s)

**Tela:** O MAQUIAVELISTA / CONTROLA / O QUE / OS OUTROS VEEM. / A VIRTUDE É MÁSCARA.

**Voz:** Segundo: o maquiavelista controla o que os outros veem dele. A virtude é máscara.

## Pista 3 — Você (16,00–20,80 s)

**Tela:** VOCÊ USA / UM DOS DOIS. / TODOS OS DIAS. / SEM NOMEAR QUAL.

**Voz:** Terceiro: você usa um dos dois todos os dias. Sem nomear qual.

## Twist (20,80–26,00 s)

**Tela:** O PERIGO / NÃO É / SER MANIPULADO. / É ACREDITAR / QUE ESCOLHE / SOZINHO.

**Voz:** O perigo não é ser manipulado. É acreditar que escolhe sozinho.

## Fecho (26,00–45,00 s)

**Tela:** QUEM COMANDA / A SUA CABEÇA? / VOCÊ, / OU QUEM LEU / O PRÍNCIPE?

**Voz:** Quem comanda a sua cabeça: você, ou quem leu o Príncipe?

---

## Mapa de 15 cenas (tempos provisórios — ajustados por `montar-voz.py`)

| # | Início | Dur. | Beat | Texto na tela | Voz | Pal. |
|---|---|---|---|---|---|---:|
| 1 | 0,00 | 2,40 | Gancho | VOCÊ É MANIPULADO. / NÃO SENTE NADA. | Você é manipulado agora. E não sente nada. | 8 |
| 2 | 2,40 | 2,60 | Contexto | ESTOICISMO / ENSINA / A / SE / DOMINAR | Há mais de dois mil anos, o estoicismo ensina a dominar a si mesmo. | 14 |
| 3 | 5,00 | 1,60 | Contexto | MAQUIAVEL / VIROU / A / MENTE / EM / INSTRUMENTO / DE / PODER | Séculos depois, Maquiavel virou essa mesma mente em instrumento de poder. | 13 |
| 4 | 6,60 | 2,60 | Pista 1 | O ESTÓICO / CONTROLA / APENAS / O PRÓPRIO JULGAMENTO. | Primeiro: o estoico controla apenas o próprio julgamento. | 10 |
| 5 | 9,20 | 2,00 | Pista 1 | O RESTO É INDIFERENTE. | Tudo o resto é indiferente. | 5 |
| 6 | 11,20 | 2,60 | Pista 2 | O MAQUIAVELISTA / CONTROLA / O QUE / OS OUTROS VEEM. | Segundo: o maquiavelista controla o que os outros veem dele. | 13 |
| 7 | 13,80 | 2,20 | Pista 2 | A VIRTUDE É MÁSCARA. | A virtude é máscara. | 5 |
| 8 | 16,00 | 2,40 | Pista 3 | VOCÊ USA / UM DOS DOIS. / TODOS OS DIAS. | Terceiro: você usa um dos dois todos os dias. | 11 |
| 9 | 18,40 | 2,40 | Pista 3 | SEM NOMEAR / QUAL. | Sem nomear qual. | 4 |
| 10 | 20,80 | 2,40 | Twist | O PERIGO / NÃO É / SER MANIPULADO. | O perigo não é ser manipulado. | 7 |
| 11 | 23,20 | 2,80 | Twist | É ACREDITAR / QUE ESCOLHE / SOZINHO. | É acreditar que escolhe sozinho. | 6 |
| 12 | 26,00 | 3,00 | Fecho | QUEM COMANDA / A SUA CABEÇA? | Quem comanda a sua cabeça: | 5 |
| 13 | 29,00 | 3,00 | Fecho | VOCÊ, | você, | 1 |
| 14 | 32,00 | 3,00 | Fecho | OU QUEM LEU | ou quem leu | 4 |
| 15 | 35,00 | 10,00 | Fecho | O PRÍNCIPE? | o Príncipe? | 2 |

**Problema no mapa acima:** a cena 15 tem 10,00 s — acima do limite de 5 s (regra pós-004). Dividir o fecho em mais cenas ou deixar o texto `O PRÍNCIPE?` no ar com fade longo é a solução. Ajustar na geração do `index.html`.

## Texto falado (`narracao.txt`)

Você é manipulado agora. E não sente nada.

Há mais de dois mil anos, o estoicismo ensina a dominar a si mesmo. Séculos depois, Maquiavel virou essa mesma mente em instrumento de poder.

Primeiro: o estoico controla apenas o próprio julgamento. Tudo o resto é indiferente.

Segundo: o maquiavelista controla o que os outros veem dele. A virtude é máscara.

Terceiro: você usa um dos dois todos os dias. Sem nomear qual.

O perigo não é ser manipulado. É acreditar que escolhe sozinho.

Quem comanda a sua cabeça: você, ou quem leu o Príncipe?

---

## Checagem

- [x] ~101 palavras escritas; ~2,2 palavras/s.
- [x] Gancho ≤9 palavras na primeira frase (6); 8 no total.
- [x] 15 cenas; revisar nenhuma acima de 5 s (cena 15 provisória acima do limite).
- [x] Cena 2 não é cartão de contexto isolado — data/conceito colados a consequência.
- [x] Um dado por cartão; "dois mil anos" só na cena 2; "1513/1532" não entra na tela (só no briefing).
- [x] Fecho em pergunta, não em resumo.
- [x] Sem "hoje vamos falar sobre", "inacreditável", "assustador".
- [x] Sem CTA comercial.
- [x] Fato com fonte; interpretação marcada como tal; lenda de Maquiavel ("ensina a ser malvado") excluída.

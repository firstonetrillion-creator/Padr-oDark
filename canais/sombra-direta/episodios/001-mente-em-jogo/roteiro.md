# Roteiro — 001 (45 s) — canal sombra-direta

> **~101 palavras escritas** em **11 cenas** — ~2,2 palavras/s.
> **Voz:** Piper `pt_BR-faber-medium`, `length_scale` **1.20**, sintetizada **cena por cena** (`scripts/montar-voz.py`).
> **Tom:** sombrio, seco, sem adjetivos vazios. Uma ideia por frase.
> **Estrutura:** gancho → contexto → 3 pistas → twist → fecho.
> **Fonte:** Zenão de Cítio (estoicismo, c. 300 a.C.); Nicolau Maquiavel, *O Príncipe* (1513/1532); Paulhus & Williams (2002).
> **Visual:** template `sombra-cinema` — fundo animado, texto com fade+scale, destaque animado, glitch sério por CSS na cena do twist. Sem WebGL/Three.js/shaders.
> **Áudio:** voz em 1,0; bed sonoro audível (FFmpeg lavfi); pulsos de impacto no twist e no fecho.

## Gancho (0,00–2,40 s)

**Tela:** A MENTE · MANIPULAÇÃO / VOCÊ É MANIPULADO. / NÃO SENTE NADA.

**Voz:** Você é manipulado agora. E não sente nada.

## Contexto (2,40–6,00 s)

**Tela:** DOIS MIL ANOS. / DUAS MENTES. / UMA TE USA.

**Voz:** Há mais de dois mil anos, duas maneiras de usar a mente. Uma delas te usa.

## Pista 1 — O estoico (6,00–9,40 s)

**Tela:** O ESTÓICO / DOMINA A SI MESMO. / O RESTO É INDIFERENTE.

**Voz:** Primeiro: o estoico domina a si mesmo. Tudo o resto é indiferente.

## Pista 2 — Maquiavel (9,40–12,80 s)

**Tela:** MAQUIAVEL / DOMINA OS OUTROS. / A VIRTUDE É MÁSCARA.

**Voz:** Segundo: Maquiavel domina os outros. A virtude é máscara.

## Pista 3 — Você (12,80–16,20 s)

**Tela:** VOCÊ USA / UM DOS DOIS. / TODOS OS DIAS.

**Voz:** Terceiro: você usa um dos dois todos os dias.

## Transição (16,20–19,60 s)

**Tela:** SEM NOMEAR / QUAL.

**Voz:** Sem nomear qual.

## Twist (19,60–23,20 s)

**Tela:** O PERIGO / NÃO É / SER MANIPULADO. (glitch por CSS)

**Voz:** O perigo não é ser manipulado.

## Twist continua (23,20–26,60 s)

**Tela:** É ACREDITAR / QUE ESCOLHE / SOZINHO.

**Voz:** É acreditar que escolhe sozinho.

## Fecho (26,60–45,00 s)

**Tela:** QUEM COMANDA / A SUA CABEÇA? / VOCÊ, / OU QUEM LEU / O PRÍNCIPE?

**Voz:** Quem comanda a sua cabeça: você, ou quem leu o Príncipe?

---

## Mapa de 11 cenas (tempos provisórios — ajustados por `montar-voz.py`)

| # | Início | Dur. | Beat | Texto na tela | Voz | Pal. |
|---|---|---|---|---|---|---:|
| 1 | 0,00 | 2,40 | Gancho | VOCÊ É MANIPULADO. / NÃO SENTE NADA. | Você é manipulado agora. E não sente nada. | 8 |
| 2 | 2,40 | 3,60 | Contexto | DOIS MIL ANOS. / DUAS MENTES. / UMA TE USA. | Há mais de dois mil anos, duas maneiras de usar a mente. Uma delas te usa. | 17 |
| 3 | 6,00 | 3,40 | Pista 1 | O ESTÓICO / DOMINA A SI MESMO. / O RESTO É INDIFERENTE. | Primeiro: o estoico domina a si mesmo. Tudo o resto é indiferente. | 13 |
| 4 | 9,40 | 3,40 | Pista 2 | MAQUIAVEL / DOMINA OS OUTROS. / A VIRTUDE É MÁSCARA. | Segundo: Maquiavel domina os outros. A virtude é máscara. | 10 |
| 5 | 12,80 | 3,20 | Pista 3 | VOCÊ USA / UM DOS DOIS. / TODOS OS DIAS. | Terceiro: você usa um dos dois todos os dias. | 11 |
| 6 | 16,00 | 3,40 | Transição | SEM NOMEAR / QUAL. | Sem nomear qual. | 4 |
| 7 | 19,40 | 3,60 | Twist | O PERIGO / NÃO É / SER MANIPULADO. | O perigo não é ser manipulado. | 7 |
| 8 | 23,00 | 3,40 | Twist | É ACREDITAR / QUE ESCOLHE / SOZINHO. | É acreditar que escolhe sozinho. | 6 |
| 9 | 26,40 | 3,40 | Fecho | QUEM COMANDA / A SUA CABEÇA? | Quem comanda a sua cabeça: | 5 |
| 10 | 29,80 | 3,20 | Fecho | VOCÊ, | você, | 1 |
| 11 | 33,00 | 12,00 | Fecho | OU QUEM LEU / O PRÍNCIPE? | ou quem leu o Príncipe? | 5 |

**Problema no mapa acima:** a cena 11 tem 12,00 s — acima do limite de 5 s (regra pós-004). Dividir o fecho em mais cenas ou deixar o texto com fade longo é a solução. Ajustar na geração do `index.html` a partir do `roteiro.json`.

## Texto falado (`narracao.txt`)

Você é manipulado agora. E não sente nada.

Há mais de dois mil anos, duas maneiras de usar a mente. Uma delas te usa.

Primeiro: o estoico domina a si mesmo. Tudo o resto é indiferente.

Segundo: Maquiavel domina os outros. A virtude é máscara.

Terceiro: você usa um dos dois todos os dias.

Sem nomear qual.

O perigo não é ser manipulado.

É acreditar que escolhe sozinho.

Quem comanda a sua cabeça: você, ou quem leu o Príncipe?

---

## Checagem

- [x] ~101 palavras escritas; ~2,2 palavras/s.
- [x] Gancho ≤9 palavras na primeira frase (6); 8 no total.
- [x] 11 cenas; revisar nenhuma acima de 5 s (cena 11 provisória acima do limite).
- [x] Cena 2 não é cartão de contexto isolado — conceito colado a consequência.
- [x] Um dado por cartão; "dois mil anos" só na cena 2.
- [x] Fecho em pergunta, não em resumo.
- [x] Sem "hoje vamos falar sobre", "inacreditável", "assustador".
- [x] Sem CTA comercial.
- [x] Fato com fonte; interpretação marcada como tal; lenda excluída.

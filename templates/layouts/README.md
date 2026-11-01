# templates/layouts — biblioteca de layouts do v2

17 estilos + o cartão de texto do v1, como **dado** no `roteiro.json`.
Spec: `docs/LAYOUTS.md` §10 · contrato: `docs/ARQUITETURA.md` §2.2.1.

**Status: aprovado em 01/11/2026** (LAB 003, `QA PASS`). Regra de uso: **1–2
estilos por episódio** — gancho e/ou um cartão de dado. Trocar o visual inteiro
de um episódio é uma variável nova, não decoração.

## Arquivos

| Arquivo | Papel |
|---|---|
| `registro.json` | fonte da verdade: `id`, `familia`, `papel`, `campos`, `asset`, `custo`, `escala_fonte`, `nota` |
| `layouts.css` | estrutura de cada moldura |
| `layouts.js` | `window.__layouts[<id>](root, tl, t, dur, start)` |

O `gerar-episodio.py` **inlina** CSS e JS no `index.html` quando alguma cena tem
`tipo`. O render continua sem dependência de arquivo extra — só `gsap.min.js`,
`voz.wav` e `drone.wav` na pasta do episódio.

## Usar num episódio

```json
{
  "id": "s7",
  "tipo": "checklist",
  "kicker": "O QUE FALTAVA",
  "titulo": ["SEM", "ETIQUETA"],
  "itens": ["SEM DOCUMENTO", "SEM NOME"],
  "fala": "O corpo não tinha etiqueta."
}
```

Regras:

1. **Sem `tipo` = `texto`** (v1). Não declare `"tipo": "texto"` à toa: a saída
   muda de forma (ganha `.core` e a biblioteca inlinada). Funciona, mas o v1 puro
   é mais leve.
2. `itens` (checklist) e `valores` (chart-grow) são **obrigatórios**; faltando,
   a geração falha com o nome do campo.
3. `asset` é opcional em quase todos e **exige** `credito` e `licenca`
   (`autoral`, `dominio-publico`, `cc-by-4.0`, `licenciado`, `ia`). O
   `check-contrato.ps1` confere arquivo, crédito e licença.
4. `zoom-through` não pode ser a última cena.

## Adicionar um layout novo

1. Entrada em `registro.json` (`escala_fonte` se a moldura encolher o texto).
2. CSS em `layouts.css` com o prefixo `.layout-<id>`; animar só `transform` e
   `opacity`.
3. Função em `layouts.js`: `L["<id>"] = function (root, tl, t, dur, start) {...}`.
   Chame `base(root, tl, t)` se a entrada do texto for a do v1.
4. Moldura no `_moldura()` do `scripts/gerar-episodio.py` (o HTML que a função
   JS espera). Layout sem moldura própria cai no `<div class="core">` padrão.
5. Testar num LAB, nunca direto num episódio: 2 a 3 s por cena bastam para ver.

## O que quebra na Intel HD 620

- `backdrop-filter` animado, `blur`/`drop-shadow` grande em área cheia e
  `feTurbulence` (SVG) — derrubam a captura.
- `clip-path` animado — use estático e anime o `x`.
- Mais de ~30 nós animados por cena em área cheia.

## Armadilhas registradas

- `.bar` sem altura definida não resolve `height: %` do filho (barras do
  `chart-grow` nasceram com 0 px).
- Traço decorativo por cima do texto parece artefato de render: mantenha
  decoração em `z-index` menor que o `.core`.
- `medir-texto.ps1` marca `ESTOURA` nos layouts de câmera porque o zoom sai dos
  840 px de propósito. Não "corrija" isso reduzindo a fonte até o texto ficar
  pequeno: o pico é o efeito.
- PowerShell 5.1 grava `registro.json` com BOM; o gerador lê com `utf-8-sig`.

# LAYOUTS — a biblioteca visual do v2

> **Status: implementado em 2026-10-31** (§10). O v1 continua sendo o padrão:
> sem `tipo` no `roteiro.json`, a cena é `texto` e a saída é byte a byte a do v1.
> Os 17 estilos existem como módulo do gerador (`templates/layouts/`), validados
> por `check-contrato.ps1` e ensaiados em `laboratorio/003-layouts-17/`.
> §3–§9 são a especificação de 27/10 e continuam valendo como plano (assets,
> política de imagem, os oito tipos originais).
> Última atualização: **2026-10-31**.

## 1. O problema que resolve

Hoje o visual é um único gesto: texto entra, texto sai. Um canal novo com visual
diferente exigiria reescrever CSS, GSAP, `gerar-episodio.py` e `check-contrato.ps1`
— ou seja, ~1 semana por canal. Com layout como **dado**, o canal novo escolhe
quais layouts usa e em que proporção; o motor é o mesmo.

Regra de ouro: **layout não é tema.** Tema é cor/fonte/grão (troca em 1 arquivo).
Layout é a *estrutura* da cena (o que está na tela além do texto).

## 2. Contrato novo do `roteiro.json`

Retrocompatível: **sem `tipo`, a cena é `texto`** e o comportamento é exatamente
o do v1. Os seis episódios existentes continuam válidos sem tocar em nada.

```json
{
  "cenas": [
    {
      "id": "s3",
      "tipo": "mapa",
      "kicker": "ROTA",
      "titulo": ["O ÚLTIMO PONTO", "CONHECIDO"],
      "legenda": "Fort Lauderdale → Triângulo",
      "asset": "assets/rota-voo19.svg",
      "credito": "desenho próprio sobre carta náutica de 1945",
      "licenca": "autoral",
      "fonte_px": 120,
      "fala": "O último ponto conhecido ficava a duzentos quilômetros da costa."
    }
  ]
}
```

| Campo | Obrigatório em | Função |
|---|---|---|
| `tipo` | — (padrão `texto`) | escolhe o renderizador |
| `asset` | `documento`, `imagem`, `mapa` | caminho relativo ao episódio |
| `credito` | qualquer cena com `asset` | vai **renderizado na tela**, não só no JSON |
| `licenca` | qualquer cena com `asset` | `autoral`, `dominio-publico`, `cc-by-4.0`, `licenciado`, `ia` |
| `legenda` | opcional | linha curta de contexto |
| `fonte_px` | `texto`, `capa`, `numero`, `fecho` | medido por `medir-texto.ps1` |

## 3. Os oito layouts (um deles é o v1)

| Layout | Papel na narrativa | Técnica | Custo | Precisa de asset? |
|---|---|---|---|---|
| `texto` | cartão tipográfico (v1) | CSS + GSAP | 0 | não |
| `capa` | abrir o dossiê: número, etiqueta, carimbo | CSS (papel, sombra, carimbo) | baixo | não |
| `numero` | cravar uma cifra (“9 HORAS”, “27 HOMENS”) | contador + escala + vinheta | baixo | não |
| `cronologia` | mostrar o tempo passando | trilho + marcador que anda | baixo | não |
| `documento` | dar prova: telegrama, laudo, jornal | CSS (textura) ou foto de página | baixo/médio | às vezes |
| `mapa` | dar geografia: rota, ponto, área | SVG + `stroke-dashoffset` | baixo | não (autoral) |
| `prova` | isolar uma frase e sua fonte | recorte + destaque + filete | baixo | às vezes |
| `fecho` | veredito (já existe no v1) | cartão + acento | 0 | não |

**`mapa` é o de maior retorno e menor risco:** é desenho próprio, não tem
licença, não tem rosto, e resolve o que a tipografia não resolve — *onde*. O
Passo Dyatlov sem o corte da encosta, o Voo 19 sem a rota, o Joyita sem o atol:
todos perderam a informação que o espectador mais quer ver.

## 4. Manifesto de assets

Cada episódio que usa `asset` ganha `assets/manifest.json`. Sem manifesto
completo, o `check-contrato.ps1` **falha** (regra 5: fato precisa de fonte; a
mesma disciplina vale para imagem).

```json
{
  "arquivo": "assets/rota-voo19.svg",
  "tipo": "svg",
  "origem": "desenho próprio",
  "autor": "Padrao-Dark",
  "data": "2026-10-27",
  "licenca": "autoral",
  "sha256": "…",
  "uso": "cena s3"
}
```

## 5. O que muda em cada script

| Script | Mudança | Retrocompatível? |
|---|---|---|
| `gerar-episodio.py` | dispatcher por `tipo`; um template de HTML por layout | sim (sem `tipo` = `texto`) |
| `check-contrato.ps1` | valida `asset` existe, `sha256` bate, `credito`/`licenca` preenchidos | sim (só checa se houver `asset`) |
| `medir-texto.ps1` | passa a medir **só** cenas de texto; cenas de imagem são conferidas por presença/área | sim |
| `qa.ps1` | **nada** | sim |
| `montar-voz.py` / tempos | **nada** — o tempo continua nascendo da fala | sim |
| `novo-episodio.ps1` | copia `assets/` vazio + manifesto modelo | sim |

## 6. Politica de imagem (vinculante)

1. **Imagem gerada por IA é ilustração, não documento.** Nunca fotorrealista
   fingindo foto de arquivo, laudo ou jornal de época. Crédito na tela:
   “imagem ilustrativa gerada por IA”.
2. **Licença comercial é pré-requisito, não detalhe.** O tier grátis de
   `build.nvidia.com` é **trial**; FLUX.1-dev está marcado como *non-commercial*.
   Para produção, usar modelo de licença comercial (FLUX.1-schnell é Apache-2.0)
   ou provedor pago, e registrar a licença no manifesto.
3. **Footage de terceiros segue proibido** (regra 7). Arquivo fílmico só entra se
   a regra for mudada explicitamente e a licença for registrada.
4. **Texto permanece obrigatório** na cena 1 e no fecho: é a identidade do canal e
   é o que segura a retenção nos dois pontos medidos.

## 7. Custo e limite de máquina

- Layout de CSS/SVG: +0 a +5 s no render de 45 s (hoje ~3m10s).
- **Proibido** filtro caro em área cheia (`blur`, `drop-shadow` grande) animado:
  na Intel HD 620 isso derruba o frame rate da captura.
- `<img>` com `transform`/`opacity` é composição barata — Ken Burns é seguro.
- Um episódio = um render. A fila de canais é **serial**, nunca paralela.

## 8. Plano de adoção (não começar antes do Gate 2)

1. **LAB 002** em `laboratorio/` — 20 a 30 s, três layouts (`capa`, `mapa`,
   `numero`), sem voz nova (reusar um trecho do LAB 001). Objetivo: medir tempo
   de produção e conferir que o contrato se sustenta.
2. Se o LAB passar: `gerar-episodio.py` ganha os renderizadores e o
   `check-contrato.ps1` ganha as validações — no template, não no episódio.
3. Só então o **canal 2** nasce com `visual` definido na `ficha.md` (é a variável
   que muda; nicho, voz, cadência e formato ficam iguais ao Dossiê 45).
4. N = 8 vídeos antes de decidir escalar/ajustar/matar, como manda `canais/README.md`.

## 9. Decisões abertas (do usuário, não do agente)

- [ ] Imagem de arquivo (domínio público) **ou** IA ilustrativa **ou** só CSS/SVG?
- [ ] Som audível entra junto com o visual, ou em A/B separado? (Uma variável por vez.)
- [ ] A regra 7 (nada de footage de terceiros) continua valendo para arquivo fílmico em domínio público?

---

# 10. Os 17 estilos (implementado em 31/10/2026)

O usuário pediu 17 estilos de vídeo. Eles **não são 17 layouts paralelos**: são
quatro famílias que se combinam com o cartão de texto que já existe. O que muda
é a moldura e o movimento, não o contrato.

## 10.1 Onde está cada coisa

| Peça | Caminho | Papel |
|---|---|---|
| Registro | `templates/layouts/registro.json` | fonte da verdade: id, família, papel, campos, custo, `escala_fonte` |
| CSS | `templates/layouts/layouts.css` | estrutura de cada moldura (só `transform`/`opacity` animados) |
| JS | `templates/layouts/layouts.js` | `window.__layouts[<id>](root, tl, t, dur, start)` |
| Gerador | `scripts/gerar-episodio.py` | `_moldura()` + `_core()`; inlina CSS/JS quando há `tipo` |
| Contrato | `scripts/check-contrato.ps1` §2b | valida `data-layout`, biblioteca inlinada, `asset` com crédito e licença |
| Ensaio | `laboratorio/003-layouts-17/` | 17 cenas, 45 s, uma por estilo |

## 10.2 Uso

```json
{ "id": "s7", "tipo": "checklist", "kicker": "O QUE FALTAVA",
  "titulo": ["SEM", "ETIQUETA"], "itens": ["SEM DOCUMENTO", "SEM NOME"],
  "fala": "..." }
```

```
gerar-episodio.py <ep>  ->  medir-texto.ps1 <ep>  ->  (-Aplicar)  ->  gerar-episodio.py  ->  render
```

Sem `tipo` nada muda. Tipo desconhecido ou campo obrigatório ausente **falha na
geração**, não no render.

## 10.3 As quatro famílias

**Câmera** — movimento, não conteúdo. Vale em cima de qualquer moldura.
`orbit`, `digital-zoom`, `zoom-through`, `pull-back`, `vertigo`.

**Moldura** — uma casca em volta do texto: `ui-world`, `phone-mockup`,
`cover-story`, `couch-wall`, `green-screen`, `frame-break`.

**Widget** — conteúdo estruturado: `checklist` (`itens`), `chart-grow`
(`valores`, `rotulos`).

**Tipografia** — tratamento de tipo: `headline-wall`, `glass-type`,
`paper-cut`, `doodle-boil`.

## 10.4 Os 17, um por um

| # | `tipo` | Nome | Família | Papel narrativo | Campos extras | Asset | Custo |
|---:|---|---|---|---|---|---|---|
| 1 | `orbit` | Órbita | câmera | dar centro/escala a um dado isolado | — | opcional | 1 |
| 2 | `couch-wall` | Parede de sofá | moldura | acervo: muitas imagens, uma importa | — | opcional | 2 |
| 3 | `ui-world` | Mundo de interface | moldura | contexto de tela (arquivo, sistema) | `janela` | opcional | 1 |
| 4 | `frame-break` | Quebra de moldura | moldura | tensão: o texto não cabe | — | não | 1 |
| 5 | `digital-zoom` | Zoom digital | câmera | aproximar em degraus (VHS) | — | não | 0 |
| 6 | `phone-mockup` | Mockup de celular | moldura | trazer a informação para a tela | — | opcional | 1 |
| 7 | `checklist` | Lista de verificação | widget | enumerar evidências | `itens` (2–5) | não | 1 |
| 8 | `headline-wall` | Parede de manchetes | tipografia | ruído da imprensa | `manchetes` | não | 1 |
| 9 | `zoom-through` | Corte por zoom | câmera | emendar duas cenas atravessando a palavra | — | não | 0 |
| 10 | `chart-grow` | Gráfico que cresce | widget | comparar grandezas | `valores` (2–5), `rotulos` | não | 1 |
| 11 | `pull-back` | Recuo revelador | câmera | do detalhe ao contexto | — | não | 0 |
| 12 | `green-screen` | Fundo verde | moldura | pôr alguém/algo na frente | — | opcional | 1 |
| 13 | `paper-cut` | Recorte de papel | tipografia | profundidade física (camadas) | — | não | 1 |
| 14 | `doodle-boil` | Traço fervendo | tipografia | marcar a frase à mão, instável | — | não | 2 |
| 15 | `vertigo` | Vertigo | câmera | desconforto: quadro empurra, fundo recua | — | não | 0 |
| 16 | `cover-story` | Capa de revista | moldura | estatuto de matéria publicada | `masthead`, `edicao`, `manchete` | opcional | 1 |
| 17 | `glass-type` | Tipografia de vidro | tipografia | isolar a frase num painel frio | — | não | 2 |

**Mapa para os oito tipos de §3:** `numero` ≈ `chart-grow` de uma barra;
`cronologia` ≈ `orbit`/`headline-wall` com datas; `prova` ≈ `frame-break` +
`credito`; `fecho` continua sendo o cartão final do v1; `capa`, `documento` e
`mapa` seguem **não implementados** — precisam de asset de verdade (documento,
carta) ou de SVG autoral (mapa), e a política de imagem de §6 continua aberta.

## 10.5 Regras de máquina (medidas, não estimadas)

- **Só `transform` e `opacity`.** `backdrop-filter` animado, `blur` em área cheia
  e `feTurbulence` derrubam a captura na Intel HD 620. O vidro do `glass-type` é
  gradiente estático; o "ferver" do `doodle-boil` são **três traços alternando a
  10 fps**, não um filtro.
- **`clip-path` só estático.** `paper-cut` anima apenas `x` das camadas.
- **Câmera estoura os 840 px de propósito.** `digital-zoom`, `vertigo`,
  `pull-back` e `zoom-through` movem o texto para fora da coluna segura durante o
  movimento; o `medir-texto.ps1` marca `ESTOURA` e **isso é esperado**. Para o
  pico caber nos 1080 px, o registro já reduz a fonte (`escala_fonte` 0,86 em
  `digital-zoom` e `vertigo`; 0,55 no `phone-mockup`, 0,76 no `ui-world`, 0,80
  no `cover-story`).
- **`doodle-boil` assume até 2 linhas de título** — o traço é dimensionado para o
  bloco de duas linhas.
- **`zoom-through` não pode ser a última cena** (não há corte depois) — o gerador
  avisa.

## 10.6 O que o LAB 003 mediu

`laboratorio/003-layouts-17/` — 17 cenas, 45,0 s, voz de 34,0 s (17 blocos), um
render. Ver `qa.md` para os números e os frames. Achados que viraram correção:

1. `chart-grow` nasceu com barras de 0 px: `.bar` sem altura definida não resolve
   `height: %` do filho.
2. `doodle-boil` com o traço por cima do texto parecia artefato; foi para trás do
   texto (z-index) e o círculo foi estreitado para 780 px.
3. `green-screen` e `vertigo` estavam fortes demais (silhueta virou borrão verde,
   raios dominavam o quadro) — alpha reduzido.
4. `paper-cut` tinha um filete que cortava o texto: removido.
5. Nove títulos quebravam em 3 linhas no frame: fonte reduzida cena a cena.


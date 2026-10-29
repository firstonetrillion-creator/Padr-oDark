# LAYOUTS — a biblioteca visual do v2

> **Status: especificação. Nada implementado.** O v1 (só tipografia) continua
> congelado no 001–006 até o Gate 2.
> Este documento existe para que **abrir um canal novo deixe de ser um rebuild
> visual** e passe a ser configuração + roteiros.
> Última atualização: **2026-10-27**.

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

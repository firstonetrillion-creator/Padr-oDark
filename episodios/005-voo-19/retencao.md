# Retenção 48 h — 005 Voo 19

> Lido em **29/10/2026** no YouTube Studio, com login, vídeo a vídeo
> (`.../video/wlPEoYErlZQ/analytics/tab-overview/period-default?hl=en`), depois de
> **1 recarregamento**. Período do painel: **“Oct 26, 2026 — Now · Since published”**.
> Evidência: `retencao-48h.png` (captura do card de retenção).

## Números do painel

| Métrica | Valor |
|---|---|
| Views | **224** desde a publicação |
| Inscritos | **+2** |
| Ficaram para assistir (“Stayed to watch”) | **46,5%** |
| Duração média assistida | **0:25** de 0:46 |
| **% média assistida** | **54,3%** (25 ÷ 46) |
| Retenção em 3 s / 10 s / fim | **não lidas** — ver ressalva |

## Leitura

**Passa o Gate 2.** 54,3% é o terceiro vídeo acima de 50% (002 87,0%; 003 87,0%;
005 54,3%), e o critério pede ≥3 de 6.

É o primeiro vídeo **inteiramente gerado** (`roteiro.json` → `gerar-episodio.py`)
e o primeiro com **12 cenas, nenhuma acima de 5 s**, sem cartão parado depois do
gancho. O resultado sustenta a regra derivada do 004: o que derrubava o miolo era
o **estado parado**, não a quantidade de texto.

O 005 também **dobra a duração média do 004** (0:25 contra 0:21) com **menos
views** (224 contra 1.200) — ou seja, a melhora não vem de público mais quente.

## Ressalva de medição

O card do Studio **não entrega 3 s / 10 s / fim** nesta versão do painel: os
pontos da curva só aparecem em *hover* real do mouse, e o navegador controlado
não dispara o *hover* interno do componente (testado com `MouseEvent` e
`PointerEvent` sintéticos — o `yta-audience-retention-highlight-hovercard`
continua `display:none`). O “See more” da curva abre o relatório expandido, mas
não expõe os pontos em texto.

Por isso `retencao_3s` e `retencao_10s` ficam **vazios** no registro — nunca
estimados. O número que decide o gate (`% média`) foi lido direto do painel.

## Origem do tráfego

Shorts feed **71,4%**; YouTube search **28,6%**; direto/desconhecido 0%.

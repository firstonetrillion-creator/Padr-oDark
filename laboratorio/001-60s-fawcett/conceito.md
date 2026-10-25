# Laboratório 001 — 60 s, estilo “Trilho”

> **Não é episódio do canal.** Não entra em `biblioteca/publicados.csv`, não passa
> pelo gate de publicação, não muda o v1 congelado do 003–006.
> É o **ensaio do vídeo 007** (o A/B do Gate 2), feito antes com material barato
> para descobrir o que quebra antes de valer uma vaga na fila.

## O que este teste prova

O 004 perdeu metade da audiência **no miolo** (duração média 0:21 de 0:46, fim de
curva em 17,3%). O suspeito é a cena 2: um cartão parado de 6,57 s com data,
origem e número.

**Hipótese:** o que derruba não é a *quantidade* de texto — é o **estado parado**.
Um cartão onde nada muda de valor, nada avança, nada conta, é um convite a sair.

**Teste:** um elemento que muda de valor em **toda** cena (o trilho de datas) e a
regra de que nenhum cartão pode existir sem uma mudança de estado visível.

## As 4 variáveis (e por que juntas)

| # | Variável | v1 (001–004) | Laboratório | Isolável depois |
|---|---|---|---|---|
| 1 | Duração | 45 s | **60 s** | sim |
| 2 | Palavras | **131** (004) | **131** — mantido de propósito | não é variável: é o **controle** |
| 3 | Ritmo | 2,9 pal./s | **2,18 pal./s** | sim |
| 4 | Elemento que muda | kicker estático | **trilho de datas que anda** | sim |

A contagem de palavras ficou **idêntica à do 004** por decisão, não por acaso:
assim a diferença entre os dois vídeos é **tempo e movimento**, não quantidade de
texto. Se o teste falhar, o texto está descartado como culpado.

Juntar as quatro num teste só é deliberado: o laboratório é para achar **o que
quebra**, não para medir efeito. Se algo der errado, a etapa seguinte isola.

Variável secundária embutida no conteúdo: **cenário brasileiro** (Mato Grosso)
em vez de estrangeiro. O canal nunca testou assunto nacional; se a retenção do
007 for parecida, o nicho pode abrir.

## A regra do trilho

Cinco marcas fixas no rodapé, sempre visíveis:

```
1925 · · · · 1927 · · · · 1951 · · · · 2005 · · · · hoje
```

Um marcador vermelho percorre a linha conforme a narração avança de época. Ele
**nunca** fica parado mais de 1,5 s. Quando a narração volta no tempo (a carta
de 1925 aparece depois de 2005), o marcador **volta** — e isso é informação, não
enfeite.

É a diferença central em relação ao v1: no 004 a cena 2 era um bloco de texto
parado. Aqui, toda cena tem um número que se move.

## O que muda na composição

1. **Trilho de datas** no rodapé, com marcador animado (GSAP, `x` absoluto).
2. **Teto de 4 palavras por linha** — o v1 permite 5.
3. **Sem música.** Só drone + vento + um impacto por virada de ano. O silêncio
   entre falas passa a ser usado como pontuação.
4. **A citação tem voz diferente:** a carta de Fawcett entra com filtro de sala
   (passa-alta + leve saturação), para separar “o que ele escreveu” de “o que o
   narrador conta”. No v1 não existe essa distinção.
5. **Grão de filme** em camada CSS/SVG (sem WebGL, respeitando o limite da
   Intel HD 620).

## Critério de sucesso — sem publicação

Vídeo não publicado **não gera curva**. Não há como medir retenção aqui. Então o
sucesso é medido em produção, não em audiência:

- [ ] **Legibilidade:** ler todos os 16 cartões a 320 px de largura e a 0,25×.
- [ ] **Nunca parado:** nenhum intervalo >1,5 s em que só exista um elemento e
      ele não se mova. Verificar frame a frame no `qa-frames/`.
- [ ] **Custo:** horas de trabalho e tempo de render comparados ao 005 (45 s).
- [ ] **Voz:** 60 s sem cansar — teste de escuta contínua, sem corte.
- [ ] **Contrato:** `check-contrato.ps1` passa com 16 cenas.

Se os cinco passarem, o estilo vira candidato ao **007** — e aí sim se mede
retenção, com o vídeo publicado de verdade.

## Se quiser sinal antes do 007

Duas saídas honestas:

1. **Publicar o laboratório no próprio canal** e assumir que suja a amostra do
   Gate 2 (60 s num feed de 45 s). Não recomendo.
2. **Publicar num canal descartável** só para ler a curva. Custa uma conta e
   não contamina o Dossiê 45. É a única forma de ter número antes do 007.

## Custo esperado

- 60 s = **1.800 frames** em 1080×1920 → acima do limite de ~1.350 do Chrome.
  Captura segmentada **obrigatória** (`HF_SEGMENTED_CAPTURE=true`, 300 frames).
- Render ~33% mais longo que o 005. É o preço do formato.

## Riscos

| Risco | Mitigação |
|---|---|
| Trilho polui a leitura | teto de 4 palavras; trilho em 60% de opacidade |
| 60 s fica lento | 16 cenas, 3,75 s médias — mesmo ritmo de corte do v1 |
| Tema brasileiro muda o público | registrar separado; não misturar com a série |
| Sensibilidade (povos indígenas) | só o que está documentado; a versão Kalapalo é **relato**, não fato provado |

## Onde estão as fontes

`roteiro.md`, seção “Limites de fato”. Fatos ancorados em:
Royal Geographical Society (declaração de desaparecimento, jan. 1927),
*Exploration Fawcett* (1953), David Grann, *The New Yorker* (2005) e
*The Lost City of Z* (2009), Michael Heckenberger (arqueologia do Alto Xingu).

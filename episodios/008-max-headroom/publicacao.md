# Publicação — 008-max-headroom

> Status: **PRONTO — aguardando aprovação humana explícita** (01/11/2026).
> Cadência do lote: 1/dia, 19h de Brasília, seg–sex. O **007 está na frente**
> na fila (janela de segunda 02/11). Se o 007 sair em 02/11, o 008 entra em
> **03/11 às 19h**; se o usuário decidir publicar os dois, manter um por dia.

## Título

**Max Headroom: a TV invadida que ninguém explicou** — 48 caracteres.

Lint PT-BR: **98/100** (`title.py --title … --thumb "A TORRE ESTAVA VAZIA"`).
Traz nome próprio (Max Headroom, TV) e o corte de 60 caracteres do desktop; o
único aviso é o de sempre — no feed mobile o título aparece truncado em
"Max Headroom: a TV invadida que ninguém…", e o sujeito (**Max Headroom**)
sobrevive ao corte.

### Alternativas

- `Em 1987, invadiram a TV de Chicago ao vivo` (42) — 98/100
- `A TV de Chicago foi invadida ao vivo em 1987` (44) — 98/100
- `Max Headroom: o sinal da TV foi roubado duas vezes` (50) — 98/100

Todas empatam no lint; a escolhida é a única que nomeia o caso pelo apelido
pelo qual ele é procurado.

## Descrição

Na noite de 22 de novembro de 1987, dois canais de Chicago tiveram o sinal
invadido por uma transmissão pirata. Nas duas vezes, quem apareceu na tela
usava uma máscara do personagem Max Headroom, diante de um painel de metal
ondulado.

Às 21h14, a WGN-TV (canal 9) perdeu o sinal durante o bloco de esportes. A tela
ficou preta por cerca de 15 segundos; depois entrou a figura, balançando, com
chiado no áudio e nenhuma voz. Durou cerca de 30 segundos: um engenheiro trocou
a frequência do enlace estúdio–transmissor e retomou o sinal. De volta ao ar, o
âncora Dan Roan disse que também não sabia o que havia acontecido.

Duas horas depois, por volta das 23h20, a WTTW (canal 11, PBS) exibia *Doctor
Who*. Dessa vez havia voz — distorcida, quase ininteligível: piadas sobre
"nerds", uma referência ao bordão "Catch the wave" e uma brincadeira com as
iniciais da WGN. Não havia engenheiro de plantão na torre, e a emissora não
tinha como cortar antes do fim.

O método era analógico: o sinal saía do estúdio por micro-ondas até a antena no
alto de um arranha-céu. A hipótese aceita é que o invasor apontou um
transmissor mais forte para o receptor da torre, em linha de visão, sobrepondo
o sinal legítimo.

A FCC abriu investigação no dia seguinte, com apoio do FBI, que ampliou
fotografias da fita. Ninguém foi identificado, ninguém foi preso e ninguém
assumiu a autoria. O prazo de prescrição federal de cinco anos venceu em 1992:
mesmo que os responsáveis apareçam, não podem mais ser processados.

Fontes: Wikipédia (EN), "Max Headroom signal hijackings"; WTTW News, 21/11/2017
("30 Years Later, Notorious 'Max Headroom Incident' Remains a Mystery"); VICE /
Motherboard, 25/11/2013 ("The Mystery of the Creepiest Television Hack"). O
vídeo não afirma quem foi: as teorias mais difundidas — os irmãos "J e K", Eric
Fournier, um funcionário demitido da WGN — nunca foram comprovadas e ficaram
fora.

Narração sintética (Piper TTS); composição tipográfica original. Nenhuma
imagem, áudio ou vídeo de terceiros foi reutilizado.

## Hashtags

`#maxheadroom #chicago #anos80 #mistério #dossie45`

## Capa

`capa.png` — frame em **31,1 s**, 1080×1920: `A TORRE ESTAVA VAZIA. / NINGUÉM
PODIA CORTAR.` (cena 9, 29,66–32,60 s).

Escolhida porque nenhuma das três peças repete a outra: o **título** entrega o
caso e o apelido; o **gancho** entrega o ato (duas invasões, ninguém preso); a
**capa** entrega **a razão** — não havia ninguém na torre para cortar o sinal.
As candidatas óbvias foram descartadas pelo lint e pela repetição: a cena 4
(`UMA MÁSCARA DE MAX HEADROOM`) repete o título, e o fecho (`NINGUÉM SABE QUEM
USAVA A MÁSCARA`) repete a ideia do gancho. Não sobrepor texto: o frame já
contém a chamada.

## Aviso de conteúdo sintético

- Voz gerada por TTS local (Piper).
- Composição e textos originais; sem reupload de terceiros.
- No Studio: **AI use = Yes**. Conferir o selo **AI** na página pública.
- O vídeo não simula pessoas reais nem atribui falas a elas: a única fala em
  primeira pessoa ("eu também não sei o que houve") é **tradução** do que Dan
  Roan disse no ar, e o cartão atribui a ele.

## Checklist de publicação

- [x] Título ≤ 60 caracteres e lint executado (**98/100**, 48 chars)
- [x] Descrição com contexto e fontes
- [x] 5 hashtags específicas
- [x] Capa extraída do vídeo (`capa.png`, 31,1 s)
- [x] `qa.ps1 -Duracao 45` com **QA PASS** (−15,0 LUFS, TP −2,1)
- [x] `qa.md` escrito (01/11/2026)
- [ ] **Escuta humana** de "Máks Rédrum", "Chicágo", "dábliu gê êne",
      "dábliu tê tê dábliu", "Dóktor U", "éfe cê cê", "éfe bê i"
- [ ] **Aprovação humana explícita do vídeo**
- [x] Arquivo `008-max-headroom_shorts_v1.mp4` (SHA-256 `70CB5963…F704A7`,
      idêntico ao `final.mp4`)
- [ ] Publicar no YouTube Shorts (conta do Dossiê 45)
- [ ] Aviso de conteúdo sintético marcado (selo **AI**)
- [ ] Vitrine pública conferida (`yt-dlp` sem cookies: `duration=45`,
      `age_limit=0`, canal `Dossiê 45`)
- [ ] Registrar em `biblioteca/publicados.csv`
- [ ] Medir retenção em 48 h — **D+2 da data de publicação**

## Registro pós-publicação

| Campo | Valor |
|---|---|
| data | — |
| slug | `008-max-headroom` |
| nicho | `misterio` |
| plataforma | `YouTube Shorts` |
| url | — |
| visibilidade | — |
| selo_ai | — |
| thumbnail | `capa.png` (frame em 31,1 s) |
| views_48h | — |
| retencao_3s | — |
| retencao_media | — |
| ficaram_assistir | — |
| duracao_media | — |

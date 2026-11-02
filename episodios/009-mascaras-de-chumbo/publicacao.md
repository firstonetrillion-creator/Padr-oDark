# Publicação — 009-mascaras-de-chumbo

> Status: **PRONTO — aguardando aprovação humana explícita** (02/11/2026).
> Cadência do lote: 1/dia, 19h de Brasília, seg–sex. O **007** está na frente
> (janela de segunda 02/11) e o **008** em 03/11; o 009 entra depois dos dois,
> mantendo um por dia.

## Título

**Máscaras de chumbo: dois mortos em 1966** — 39 caracteres.

Lint PT-BR: **100/100** (`title.py`). Passa o corte de 60 do desktop, o corte do
feed mobile (o sujeito **Máscaras de chumbo** sobrevive) e traz um dado concreto
(1966). A versão do plano, `Máscaras de chumbo: dois mortos sem uma marca`
(45 chars), ficou em **76/100** — truncava no mobile em "…dois mortos sem uma…"
e não tinha número nem nome próprio. O "sem uma marca" continua no gancho e na
capa do vídeo.

### Alternativas

- `Máscaras de chumbo: Niterói, 1966` (33) — 100/100; mais seca, mas esconde o
  resultado (dois mortos)
- `Máscaras de chumbo: o caso sem causa de 1966` (44) — 94/100; trunca no mobile

## Descrição

Em 17 de agosto de 1966, dois técnicos em eletrônica saíram de Campos dos
Goytacazes dizendo às mulheres que iam a São Paulo comprar material de trabalho.
Foram para Niterói. Compraram uma capa impermeável e uma garrafa d'água; segundo
uma funcionária da loja, um deles parecia nervoso, "como se tivesse hora
marcada".

Três dias depois, um rapaz de 18 anos que empinava pipa no Morro do Vintém
encontrou os dois corpos, já em decomposição. Estavam de terno, capa
impermeável e máscaras de chumbo em formato de óculos. Não havia sinal de
violência nos corpos nem no local.

No bolso de um deles, um bilhete na caligrafia de Miguel José Viana:

"16:30 Hs. está local determinado. / 18:30 Hs. ingerir cápsula após efeito, /
proteger metais aguardar sinal máscara."

Havia também um bloco com símbolos e números — códigos de referência para
válvulas eletrônicas, coerentes com a profissão dos dois — e passagens de ônibus
datadas do dia 15.

Dois meses depois, o laudo do Instituto Médico Legal apontou causa
indeterminada. O estado avançado de decomposição impediu o exame toxicológico:
nunca se soube se eles haviam ingerido alguma substância. Em setembro, o
delegado Idovan Ferreira concluiu que os dois morreram em uma "experiência
parapsicológica mal-sucedida". Depois de três anos sem solução, o caso foi
arquivado.

A imprensa de 1966 publicou o relato de uma vizinha que dizia ter visto um
"disco voador" sobre o morro na tarde do dia 17. É relato de testemunha, nunca
verificado — e o vídeo o marca como lenda. O que está documentado é o bilhete, o
laudo e o arquivamento.

Fontes: Wikipédia (PT), "Mistério das máscaras de chumbo"; *O Globo*,
22/08/1966 ("Encontrados no Meio da Mata Dois Cadáveres Com Máscara de Chumbo")
e 14/09/1966 ("Delegado Encerra o Caso das Máscaras de Chumbo"); *O Cruzeiro*,
12/09/1966; *Correio da Manhã*, 27/10/1966.

Narração sintética (Piper TTS); composição tipográfica original. Nenhuma imagem,
áudio ou vídeo de terceiros foi reutilizado.

## Hashtags

`#mascarasdechumbo #niteroi #1966 #mistério #dossie45`

## Capa

`capa.png` — frame em **32,68 s**, 1080×1920: `CAUSA / INDETERMINADA.` (cena 9,
30,53–33,92 s).

Escolhida porque nenhuma das três peças repete a outra: o **título** entrega o
objeto e a data; o **gancho** entrega o resultado (dois mortos, nenhuma marca); a
**capa** entrega **a resposta oficial** — o laudo que não soube dizer a causa. As
candidatas óbvias foram descartadas pela repetição: a cena 1 (`DOIS MORTOS NO
MORRO`) repete o gancho, e o fecho (`O CASO FOI ARQUIVADO`) repete a ideia do
título. Não sobrepor texto: o frame já contém a chamada.

## Aviso de conteúdo sintético

- Voz gerada por TTS local (Piper).
- Composição e textos originais; sem reupload de terceiros.
- No Studio: **AI use = Yes**. Conferir o selo **AI** na página pública.
- O vídeo não simula pessoas reais nem atribui falas a elas: o bilhete é citado
  como documento (transcrição de imprensa), e a frase do delegado é atribuída a
  ele no cartão ("PARAPSICOLOGIA, DISSE ELE").

## Checklist de publicação

- [x] Título ≤ 60 caracteres e lint executado (**100/100**, 39 chars)
- [x] Descrição com contexto e fontes
- [x] 5 hashtags específicas
- [x] Capa extraída do vídeo (`capa.png`, 32,68 s)
- [x] `qa.ps1 -Duracao 45` com **QA PASS** (−14,9 LUFS, TP −1,7)
- [x] `qa.md` escrito (02/11/2026)
- [ ] **Escuta humana** de "Cãpos dos Goitacazes", "Niterói", "Vintém",
      "Manoel Pereira da Cruz", "Miguel José Viana", "Idovan Ferreira",
      "Élcio Correia Gomes", "Gracinda Barbosa Coutinho de Souza"
- [ ] **Aprovação humana explícita do vídeo**
- [x] Arquivo `009-mascaras-de-chumbo_shorts_v1.mp4` (SHA-256 `3E0A2ACE…D173AC`,
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
| slug | `009-mascaras-de-chumbo` |
| nicho | `misterio` |
| plataforma | `YouTube Shorts` |
| url | — |
| visibilidade | — |
| selo_ai | — |
| thumbnail | `capa.png` (frame em 32,68 s) |
| views_48h | — |
| retencao_3s | — |
| retencao_media | — |
| ficaram_assistir | — |
| duracao_media | — |

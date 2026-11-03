# Publicação — 011-ss-baychimo

> Status: **PRONTO — aguardando aprovação humana explícita** (03/11/2026).
> Cadência do lote: **3 a 4 vídeos por dia**, publicados manualmente pelo usuário
> (decisão de 02/11). O 007, o 008, o 009 e o 010 estão na frente, também sem
> aprovação.

## Título

**SS Baychimo: 38 anos à deriva no gelo** — 37 caracteres.

Lint PT-BR: **100/100** (`title.py`). Passa o corte de 60 do desktop, o corte do
feed mobile (o sujeito **SS Baychimo** sobrevive) e traz um dado concreto (38).
A versão do plano — `SS Baychimo: o navio que ninguém alcançou` (41 chars) — ficou
em **94/100** por truncar no mobile em "…o navio que ninguém…"; sem o "SS",
`Baychimo: o navio que ninguém alcançou` (38), cai para **90/100** por não ter
número, data nem nome próprio reconhecível.

O título usa **"à deriva"**, não "navegou": é o que o corpo do vídeo sustenta (o
navio ficou preso no gelo, sem leme e sem máquina) e a diferença está registrada
no `briefing.md` e no `qa.md`.

### Alternativas

- `SS Baychimo: abandonado em 1931, perdido em 1969` (48) — 94/100; trunca no
  mobile, mas entrega as duas datas
- `Baychimo: o navio que ninguém alcançou` (38) — 90/100; mais literária, sem
  dado concreto

## Descrição

Em outubro de 1931, o cargueiro SS Baychimo, da Hudson's Bay Company, ficou preso
no gelo compacto perto de Point Barrow, no Alasca, com um carregamento de peles no
porão. Vinte e dois tripulantes saíram de avião no dia 15. Quinze ficaram,
construíram um abrigo na praia e se prepararam para passar o inverno.

Em 24 de novembro, um temporal de três dias levantou a temperatura de −60 °C para
zero. Quando o vento parou, o navio não estava mais lá. O comandante Cornwell
concluiu que ele tinha se despedaçado. Dias depois, um caçador inuíte trouxe a
notícia: o Baychimo estava a 45 milhas dali, intacto, inclinado sobre o gelo. Os
quinze voltaram de trenó e retiraram mantimentos em duas viagens. Na terceira vez,
o navio tinha sumido de novo.

Ele continuou aparecendo por 38 anos. Foi abordado em 1933, 1934 e 1939; em
novembro de 1939 o capitão Hugh Polson tentou rebocá-lo e o gelo não deixou. Em
11 de agosto de 1933, a botânica Isobel Wylie Hutchison escreveu que o casco
"se erguia como uma torre acima do pequeno Trader". O último avistamento
registrado é de 1969, no Mar de Beaufort. Em 2006, o governo do Alasca começou um
projeto para localizá-lo, no fundo do mar ou ainda à tona. Não achou nada.

O navio não navegava: ele derivava com o gelo. Não há prova de que tenha
afundado — a hipótese é que o aço tenha cedido aos ciclos térmicos, mas isso é
presunção, não registro. Ninguém morreu no caso: toda a tripulação sobreviveu.

Fontes: Wikipédia (EN), "SS Baychimo"; Kenn Harper, "Taissumani: Nov. 24, 1931 —
Ghost Ship: The Disappearance of the Baychimo", *Nunatsiaq News*, 24/11/2006;
Anthony Dalton e James Delgado, *Baychimo: Arctic Ghost Ship* (Heritage House,
2006); Isobel Wylie Hutchison, *North to the Rime-Ringed Sun* (Blackie & Son,
1934); Manitoba Museum, "Baychimo: The Adventures of the Ghost Ship of the
Arctic" (2020); *Time*, 29/02/1932.

Narração sintética (Piper TTS); composição tipográfica original. Nenhuma imagem,
áudio ou vídeo de terceiros foi reutilizado.

## Hashtags

`#ssbaychimo #naviofantasma #artico #1931 #dossie45`

## Capa

`capa.png` — frame em **25,52 s**, 1080×1920: `ESTRANHOS / A BORDO.` +
`O PORÃO AINDA / TINHA PELES.` (cena 7, 23,35–26,77 s, com o kicker
`11 DE AGOSTO DE 1933`).

Escolhida porque nenhuma das três peças repete a outra: o **título** entrega o
nome e o intervalo (38 anos); o **gancho** entrega o abandono e a volta; a **capa**
entrega **o detalhe estranho** — alguém subiu a bordo e a carga ainda estava lá.
As candidatas óbvias foram descartadas pela repetição: a cena 1
(`ABANDONARAM NO GELO`) repete o gancho, e a cena 10 (`38 ANOS DEPOIS`) repete o
número do título e da primeira fala. Não sobrepor texto: o frame já contém a
chamada.

## Aviso de conteúdo sintético

- Voz gerada por TTS local (Piper).
- Composição e textos originais; sem reupload de terceiros.
- No Studio: **AI use = Yes**. Conferir o selo **AI** na página pública.
- O vídeo não simula pessoas reais: a única citação é de Isobel Wylie Hutchison,
  identificada no cartão como "uma botânica" e no rodapé como fonte.

## Checklist de publicação

- [x] Título ≤ 60 caracteres e lint executado (**100/100**, 37 chars)
- [x] Descrição com contexto e fontes
- [x] 5 hashtags específicas
- [x] Capa extraída do vídeo (`capa.png`, 25,52 s)
- [x] `qa.ps1 -Duracao 45` com **QA PASS** (−15,0 LUFS, TP −2,7)
- [x] `qa.md` escrito (03/11/2026)
- [ ] **Escuta humana** de "Baychimo", "Hudson's Bay", "Wainwright",
      "Point Barrow", "Beaufort", "Polson", "Hutchison"
- [ ] **Aprovação humana explícita do vídeo**
- [x] Arquivo `011-ss-baychimo_shorts_v1.mp4` (SHA-256
      `4C71CB58…B70869`, idêntico ao `final.mp4`)
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
| slug | `011-ss-baychimo` |
| nicho | `misterio` |
| plataforma | `YouTube Shorts` |
| url | — |
| visibilidade | — |
| selo_ai | — |
| thumbnail | `capa.png` (frame em 25,52 s) |
| views_48h | — |
| retencao_3s | — |
| retencao_media | — |
| ficaram_assistir | — |
| duracao_media | — |

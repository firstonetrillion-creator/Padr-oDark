# Publicação — 010-carroll-a-deering

> Status: **PRONTO — aguardando aprovação humana explícita** (03/11/2026).
> Cadência do lote: **3 a 4 vídeos por dia**, publicados manualmente pelo usuário
> (decisão de 02/11). O 007, o 008 e o 009 estão na frente, também sem aprovação.

## Título

**Carroll A. Deering: 1921, o navio vazio** — 39 caracteres.

Lint PT-BR: **100/100** (`title.py`). Passa o corte de 60 do desktop, o corte do
feed mobile (o sujeito **Carroll A. Deering** sobrevive) e traz um dado concreto
(1921). O título de trabalho — `Carroll A. Deering: o navio voltou vazio`
(40 chars) — ficou em **94/100**: sem número nem data. A versão com 41+ caracteres
(`o navio vazio de 1921`) cai para **94/100** por truncar no mobile.

### Alternativas

- `Deering: o navio de 1921 voltou vazio` (37) — 100/100; mais fluida, mas perde
  o nome completo do navio
- `Carroll A. Deering: 11 homens, nenhum corpo` (43) — 94/100; trunca no mobile

## Descrição

Em janeiro de 1921, um veleiro de cinco mastros apareceu encalhado nas Diamond
Shoals, na Carolina do Norte, com todas as velas postas, o leme quebrado e
ninguém a bordo. A mesa da cozinha estava posta. Faltavam os dois botes, o diário
de bordo, o cronômetro, o sextante, as âncoras e os pertences da tripulação.

Onze homens. Nenhum corpo. Nenhum bote.

O Carroll A. Deering tinha sido lançado em Bath, Maine, em abril de 1919, e
voltava do Rio de Janeiro. Em Barbados, em janeiro, o imediato Charles McLellan
tinha dito, bêbado, a três capitães: "Eu pego o capitão antes de chegarmos a
Norfolk". No dia 29 de janeiro, no farol flutuante de Cape Lookout, um homem
ruivo gritou pelo megafone que o navio perdera as âncoras — e não era o capitão
nem um oficial quem falava.

Em abril, um pescador de Buxton disse ter achado uma garrafa com uma carta
falando em piratas. A letra foi identificada como sendo do engenheiro do navio.
Depois, peritos concluíram que era falsa, e o pescador confessou: queria a
publicidade para conseguir emprego numa estação de farol.

Cinco repartições do governo americano investigaram — Comércio, Tesouro,
Justiça, Marinha e Estado. O inquérito foi encerrado no fim de 1922, sem
conclusão oficial. O casco foi dinamitado em março de 1921 por ser perigo para a
navegação.

O caso é às vezes listado como "Triângulo das Bermudas", mas isso é posterior: a
ligação vem de livros de 1931 a 1974, e o naufrágio foi em Cape Hatteras, fora do
triângulo clássico. O vídeo não usa essa versão.

Fontes: National Park Service (Cape Hatteras National Seashore), "The Ghost Ship
of the Outer Banks"; Wikipédia (EN e DE), "Carroll A. Deering"; Bland Simpson,
*Ghost Ship of Diamond Shoals* (UNC Press, 2002/2005); Ray McAllister, *Hatteras
Island* (2009); *New York Times*, 21 e 22/06/1921; *Washington Post*, 21/06/1921;
*New York Herald*, 26/08/1921.

Narração sintética (Piper TTS); composição tipográfica original. Nenhuma imagem,
áudio ou vídeo de terceiros foi reutilizado.

## Hashtags

`#carrolladeering #naviofantasma #1921 #mistério #dossie45`

## Capa

`capa.png` — frame em **9,6 s**, 1080×1920: `ONZE HOMENS. / NENHUM CORPO. /
NENHUM BOTE.` (cena 3, 7,81–10,76 s).

Escolhida porque nenhuma das três peças repete a outra: o **título** entrega o
nome e o ano; o **gancho** entrega a cena impossível (navio vazio, comida na
mesa); a **capa** entrega **o saldo** — onze homens, nenhum corpo. As candidatas
óbvias foram descartadas pela repetição: a cena 1 (`O NAVIO VEIO VAZIO`) repete o
gancho, e a cena 12 (`O CASCO FOI DINAMITADO`) é consequência, não promessa.
Não sobrepor texto: o frame já contém a chamada.

## Aviso de conteúdo sintético

- Voz gerada por TTS local (Piper).
- Composição e textos originais; sem reupload de terceiros.
- No Studio: **AI use = Yes**. Conferir o selo **AI** na página pública.
- O vídeo não simula pessoas reais: a fala do imediato é citada como registro de
  testemunhas (três capitães no Continental Café, Barbados) e o cartão a atribui
  a ele ("EU PEGO / O CAPITÃO.").

## Checklist de publicação

- [x] Título ≤ 60 caracteres e lint executado (**100/100**, 39 chars)
- [x] Descrição com contexto e fontes
- [x] 5 hashtags específicas
- [x] Capa extraída do vídeo (`capa.png`, 9,6 s)
- [x] `qa.ps1 -Duracao 45` com **QA PASS** (−14,9 LUFS, TP −1,4)
- [x] `qa.md` escrito (03/11/2026)
- [ ] **Escuta humana** de "Carroll A. Deering", "Cape Hatteras", "Diamond
      Shoals", "Cape Lookout", "Barbados", "Norfolk", "Wormell", "McLellan"
- [ ] **Aprovação humana explícita do vídeo**
- [x] Arquivo `010-carroll-a-deering_shorts_v1.mp4` (SHA-256
      `33FC547F…360A225D`, idêntico ao `final.mp4`)
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
| slug | `010-carroll-a-deering` |
| nicho | `misterio` |
| plataforma | `YouTube Shorts` |
| url | — |
| visibilidade | — |
| selo_ai | — |
| thumbnail | `capa.png` (frame em 9,6 s) |
| views_48h | — |
| retencao_3s | — |
| retencao_media | — |
| ficaram_assistir | — |
| duracao_media | — |

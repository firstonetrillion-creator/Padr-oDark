# QA — 012-hinterkaifeck

**Data:** 2026-11-04
**Arquivo:** `final.mp4`
**Render:** standard, 1080×1920, 30 fps, captura segmentada — **1350/1350
frames**, 5 segmentos, 0 retries, **3m11,8s**
**Duração:** 45,013 s · **Tamanho:** 3.783.232 bytes (3,61 MB)
**Voz:** Piper `pt_BR-faber-medium`, **cena por cena** (`montar-voz.py`) —
35,958 s de fala + 9,042 s de silêncio (20,1%) = 45,000 s
**SHA-256 (`final.mp4`):**
`6B3E3F5458D3DAC1D1AA4F6CCB8ECDB1599A9C5BB6F656053AB55AA3E16F28C6`

## Técnico

| Item | Medição | Status |
|---|---|---|
| Codec de vídeo | H.264, 1080×1920 | OK |
| FPS | 30/1 constante | OK |
| Áudio | AAC 48 kHz, estéreo | OK |
| Loudness | **−15,0 LUFS** (cru: −19,1; pós-render **+4,1 dB** + limitador 0,85) | OK |
| Pico | true peak **−1,4 dBFS** | OK |
| LRA | 4,0 LU | OK |
| Preto inesperado | nenhum; fade final em ~44,3–45,0 s | OK |
| Texto cortado | 12 frames do `final.mp4`; nenhuma cena acima de 3 linhas | OK |
| Linha mais larga | **810 px de 840** (s5) na medida; 812 px no frame do mp4 | OK |
| Sincronia | 12 cenas de `tempos_cenas.json` — **exatas por construção**, sem ASR | OK |
| Contrato | `check-contrato.ps1` — **OK, 1 aviso** (12 cenas, padrão é 13) | OK |
| QA automático | `qa.ps1 -Duracao 45` | **PASS** |
| Marca | `DOSSIÊ 45` / dossiê `012` | OK |

## Layouts (2 por episódio, como aprovado em 01/11)

| Cena | Layout | Por quê |
|---|---|---|
| s1 (0,00–4,63) | `digital-zoom` | mesmo tratamento do gancho do 008, 009, 010 e 011 (variável controlada do lote) |
| s4 (11,50–15,63) | `checklist` | o layout existe para enumerar evidência — e o cartão lista as quatro coisas que Andreas viu antes da noite |

As outras 10 cenas são o cartão do v1, sem `tipo`. Contrato §2b passou:
`data-layout`, `window.__layouts` inlinado e `layout-<tipo>` em todas.

**Achado do `checklist`:** os itens são texto pequeno e **não** entram na conta de
linhas do `medir-texto.ps1` (que mede o `h1`) — a s4 sai como "2/2". A conferência
dos quatro itens é visual, no frame.

**Gancho conferido em frame do mp4:** a cena 1 tem **kicker e título legíveis em
0,10 s** (título ainda em fade) e o cartão **completo em 0,60 s** — duas linhas de
título, duas de texto pequeno e a régua. É o quinto episódio seguido em que o
`digital-zoom` entrega o primeiro segundo.

**Armadilha confirmada:** o `frames.py` marca a cena 1 como `ESTOURA` (x0 = 72,
x1 = 766) porque o zoom (`scale: 1.12`) empurra o texto para fora da margem de
116 px. É **câmera**, não estouro de cartão — regra do LAB 003: `ESTOURA` em
`digital-zoom`/`orbit`/`vertigo`/`pull-back` não reprova.

## Editorial

- [x] **Gancho aprovado no lote:** "Seis pessoas mortas na fazenda. Alguém ainda
      ordenhou as vacas." — consequência, sem contexto; o frame 1 já entrega o
      fato e a contradição.
- [x] **Cena 2 não é cartão de contexto** (regra pós-004): entrega o **lugar** —
      "ISOLADA / NA MATA." + "70 KM AO NORTE / DE MUNIQUE." —, não uma ficha de
      data e país.
- [x] Uma ideia por vídeo: **seis pessoas mortas numa fazenda isolada e alguém
      que ficou na casa depois**
- [x] Fatos com fonte: Wikipédia (DE) e (EN), *Salzburger Wacht* (06/04/1922),
      *Salzburger Volksblatt* (22/04/1922 e 01/02/1935), Donaukurier (2012),
      Augsburger Allgemeine (2012), Leuschner (1997) — rodapé no vídeo
- [x] "Seis pessoas mortas na fazenda" = Andreas e Cäzilia Gruber, Viktoria
      Gabriel, Cäzilia (7), Josef (2) e a empregada Maria Baumgartner
- [x] "Alguém ainda ordenhou as vacas" = o gado foi **ordenhado e recebeu água**
      durante os quatro dias (EN) — o detalhe é do inquérito, não invenção
- [x] "Uma fazenda isolada na floresta, ao norte de Munique" = *Einödhof* a ~70 km
      de Munique, em Wangen (hoje Waidhofen), a 900 m de Gröbern
- [x] "Pegadas na neve. Só de ida." = Andreas contou aos vizinhos que achou
      pegadas da floresta até a porta da casa das máquinas, **sem volta**
- [x] "A chave sumiu. O cadeado foi arrombado. E passos no sótão." = a chave da
      porta da frente desapareceu antes do crime; o cadeado da casa das máquinas
      foi arrombado; a família ouvia passos no sótão à noite
- [x] "A VACA SOLTA NO ESTÁBULO" (cartão, não falado) = vaca desamarrada no
      estábulo, dias antes
- [x] "Naquela tarde chegou a nova empregada. Primeiro dia." = Maria Baumgartner
      começou em 31/03/1922; a irmã que a levou foi provavelmente a última pessoa
      a ver os moradores vivos
- [x] "Um por um, foram ao celeiro. A arma era do sítio." = as quatro primeiras
      vítimas foram atraídas ao celeiro, uma a uma; a arma era uma **Reuthaue**
      (enxada de roçar) do próprio sítio
- [x] "Depois, dentro da casa: a empregada e o menino." = Maria, na camarinha, e
      Josef, no berço
- [x] "Quatro dias depois, os vizinhos arrombaram o portão." = 04/04/1922, ~15h30,
      Lorenz Schlittenbauer com Michael Pöll e Jakob Sigl; o portão do celeiro foi
      arrombado porque todas as portas estavam trancadas
- [x] "O pão tinha acabado. E a carne, recém-cortada." = o pão da casa acabou e
      havia carne recém-cortada na despensa
- [x] "Cem mil marcos de recompensa. Cem suspeitos. Nenhuma acusação." =
      100.000 Mark oferecidos em **08/04/1922** pelo Ministério do Interior da
      Baviera; ~100 suspeitos no inquérito; **nenhuma acusação jamais**
- [x] "Os autos fecharam. Décadas depois, ainda ouviam testemunhas." = autos
      fechados em **1955**; últimas oitivas em **1986**
- [x] "Ninguém foi acusado. Hoje, ali é só lavoura." = a fazenda foi demolida em
      1923; o terreno é lavoura, com um pequeno monumento
- [x] **Nenhuma idade no vídeo** — as fontes divergem (Andreas 63/64, Maria
      44/45) e o número não paga o risco
- [x] **Sem graphicidade:** o vídeo não descreve ferimentos, cabeças, crânios nem
      o estado dos corpos; o detalhe da autópsia da menina ficou só no
      `briefing.md`
- [x] **As crianças não são o espetáculo:** "a empregada e o menino" aparece uma
      vez, na cena 7, e o vídeo segue
- [x] **Não diz que o assassino "morou" na casa** como fato consumado: o cartão
      diz "ALGUÉM AINDA / ORDENHOU AS VACAS" e o corpo mostra o que os autos
      provam (gado tratado, pão, carne)
- [x] **Nada de lenda:** sem casa assombrada, sem seita, sem ritual; a versão de
      que a empregada anterior saiu porque via fantasmas não tem depoimento na
      origem (registrado no `briefing.md`)
- [x] Sem CTA comercial
- [ ] **Escuta humana pendente** de "Hinterkaifeck", "Gröbern", "Waidhofen",
      "Cäzilia", "Schlittenbauer", "Reut­haue", "Baumgartner" (transliterações no
      `briefing.md` e no `narracao_tts.txt`)

## Cadeia de áudio (medida antes, não depois)

| Etapa | LUFS | TP |
|---|---:|---:|
| `voz_raw.wav` (Piper, volume 1.0) | −16,4 | **+0,1** |
| `voz.wav` (`volume=-5.6dB,alimiter=limit=0.85`) | −22,0 | −5,5 |
| `final_raw.mp4` (mix com drone a 0,16) | −19,1 | −5,5 |
| `final.mp4` (`volume=4.1dB,alimiter=limit=0.85`) | **−15,0** | −1,4 |

O Piper saiu **quente** (−16,4 LUFS, TP +0,1), como no 008 (−15,7), 009 (−16,1),
010 (−16,3) e 011 (−15,1). O sinal do pós foi escolhido **depois** de medir o cru:
**+4,1 dB**. O `final_raw` caiu em **−19,1 LUFS**, o mesmo valor do 008 ao 011.

## Identidade

- [x] Paleta, tipografia, moldura, marca `DOSSIÊ 45` e dossiê `012`
- [x] Voz impessoal, sem "eu" ou "nós"
- [x] Drone a 0,16 — **mesmo arquivo dos anteriores** (inaudível por projeto)
- [x] Rodapé conferido **antes** do render: `FONTE · WIKIPÉDIA · SALZBURGER
      WACHT, 1922` — fonte deste caso, e não a do episódio anterior (armadilha do
      011, que herdou o `NPS` do 010)
- [x] Capa `capa.png` — frame em **10,20 s**, 1080×1920: `PEGADAS / NA NEVE.` +
      `NENHUMA / DE VOLTA.` (s3, 7,93–11,50 s)

## Ritmo (variável do lote: o gancho)

| Medida | 007 | 008 | 009 | 010 | 011 | **012** |
|---|---:|---:|---:|---:|---:|---:|
| Palavras escritas | 108 | 106 | 109 | 113 | 113 | **108** |
| Cenas | 12 | 12 | 12 | 12 | 12 | **12** |
| Cena mais longa | 5,029 s | 4,70 s | 4,64 s | 4,57 s | 5,23 s | **4,63 s** |
| Silêncio | 20,5% | 17,9% | 22,3% | 19,6% | 19,9% | **20,1%** |
| Gancho | "Um homem morto na praia" | "Dois canais de TV foram invadidos" | "Dois homens mortos no morro" | "O navio apareceu vazio" | "Abandonaram o navio no gelo" | **"Seis pessoas mortas na fazenda"** |
| 1º segundo | moldura só | legível em 0,10 s | legível no 1º frame | legível em 0,10 s | legível em 0,10 s | **legível em 0,10 s; completo em 0,60 s** |

**Nenhuma cena passa de 5 s** — a mais longa é a s12 (4,63 s) e a menor é a s6
(3,10 s). É o primeiro episódio do lote sem nenhuma exceção registrada no teto.

## Correções antes do render

- **Falas enxugadas** depois da primeira síntese: o take inicial deu **40,0 s de
  fala** (silêncio de 11,1%) e a **s11 em 6,278 s** — os dois anos soletrados
  ("mil novecentos e cinquenta e cinco") estouravam a cena. A s11 virou "Os autos
  fecharam. Décadas depois, ainda ouviam testemunhas." e os anos ficaram no kicker
  `1955 · 1986`. Resultado: **35,96 s de fala e 20,1% de silêncio**.
- **Fecho encurtado:** a s12 vinha com 4,27 s de fala e fechava a cena em
  **5,745 s** (a última cena absorve a cauda do vídeo). Virou "Ninguém foi
  acusado. Hoje, ali é só lavoura." e o ano foi para o cartão pequeno
  ("CAIU EM 1923."). Agora 4,62 s.
- **Título da s12 em 3 linhas:** `text-wrap: balance` quebrava
  `FOI ACUSADO.` a 130 px (12 caracteres ≈ 940 px). Voltou para
  `NINGUÉM FOI / ACUSADO.` com fonte **116** (751 px).
- **Item do `checklist` trocado:** o primeiro item repetia "pegadas só de ida",
  que a s3 tinha acabado de dizer; entrou **"A VACA SOLTA NO ESTÁBULO"**, um fato
  do `briefing.md` que o cartão passa a entregar sozinho. Re-render feito por
  causa disso (**4m16,9s** no primeiro, **3m11,8s** no segundo).
- **Armadilha nova:** `Set-Content -Encoding UTF8` no PowerShell 5.1 grava
  **BOM** e o `gerar-episodio.py` morre com `Unexpected UTF-8 BOM`. Para editar
  `roteiro.json` fora do editor, usar `[IO.File]::WriteAllText` com
  `UTF8Encoding($false)` — ou o `edit` tool.

## Pendências

- Escuta humana dos nomes e aprovação explícita — **não publica sem isso**.
- O caso envolve crianças: a descrição pública repete o cuidado do vídeo (sem
  ferimentos, sem detalhe de autópsia).

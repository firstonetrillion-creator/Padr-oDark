# QA — 007-homem-de-somerton

**Data:** 2026-10-31 (render em 2026-10-29 17:58; QA técnico final em 31/10)
**Arquivo:** `final.mp4`
**Render:** standard, 1080×1920, 30 fps, captura segmentada; **1350/1350 frames**
confirmados no container (45,000 s de vídeo)
**Duração:** 45,013 s (container) · **Tamanho:** 3.377.639 bytes (3,38 MB)
**Voz:** Piper `pt_BR-faber-medium`, sintetizada **cena por cena** (`montar-voz.py`)
— 35,768 s de fala + 9,232 s de silêncio (20,5%) já totalizando 45,000 s;
`voz.wav` pré-normalizado +5 dB com limitador 0,85 **antes** do render
**SHA-256 (`final.mp4`):** `DE13EECD7C89DB3B2F5BB233CBA6F16C6F916E4B123AD4FE7DE2A4F01F462B6B`

## Técnico

| Item | Medição | Status |
|---|---|---|
| Codec de vídeo | H.264, 1080×1920 | OK |
| FPS | 30/1 constante | OK |
| Áudio | AAC 48 kHz, estéreo | OK |
| Loudness | −15,0 LUFS (cru: **−10,6**; pós-render −4,4 dB + limitador 0,85) | OK |
| Pico | true peak **−5,9 dBFS** (folga grande: a redução de −4,4 dB afastou o pico) | OK |
| LRA | 3,2 LU | OK |
| Preto inesperado | nenhum; fade final em ~44,3–45,0 s | OK |
| Texto cortado | 7 frames conferidos no `final.mp4` (s1, s2, s5, s9, s10, s12); nenhum acima de 5 linhas | OK |
| Linha mais larga | **800 px de 840** (cena 9, "IDENTIFICADO.") | OK |
| Sincronia | 12 cenas de `tempos_cenas.json` — **exatas por construção**, sem ASR | OK |
| Fantasma de cena | `autoAlpha` por cena; frames conferidos | OK |
| Contrato | `check-contrato.ps1` — **OK, 1 aviso** (12 cenas, padrão é 13) | OK |
| QA automático | `qa.ps1` | **PASS** |
| Marca | `DOSSIÊ 45` / dossiê `007` | OK |

## Editorial

- [x] Gancho: frame 0 é só a moldura (a cena 1 anima a partir de 0,6 s —
  comportamento do v1, igual a 004–006); em 1,5 s o gancho está completo
- [x] Uma ideia por vídeo: **o corpo apareceu sem nome, com uma palavra persa no
  bolso e um código num livro; 74 anos depois o DNA deu o nome, mas não a causa
  nem o código**
- [x] Fatos com fonte: Wikipédia PT "Caso Taman Shud"; The Guardian 27/07/2022 e
  31/07/2022; ABC News 01/12/2018 — rodapé no vídeo
- [x] **Gancho "código costurado na roupa"** — o papel "Taman Shud" foi achado num
  **compartimento secreto disfarçado no bolso da calça** (fonte: "disfarçado";
  o compartimento é costurado). As letras cifradas estão na contracapa do
  livro, e a cena 7 diz isso explicitamente. O briefing sanciona a imagem no
  gancho; o vídeo separa os dois achados
- [x] "2022: o DNA diz Carl Webb" = anúncio de Abbott & Fitzpatrick (26/07/2022);
  a polícia da Austrália do Sul **não** se pronunciou formalmente — o vídeo não
  afirma confirmação oficial
- [x] "Setenta e quatro anos" = 1948→2022, arredondamento correto
- [x] **Nada** de espião soviético, amante rejeitado (Jo Thomson/Alfred Boxall),
  Robin Thomson como filho ou "morte natural" — todos fora, como lista de lendas
- [x] O fecho **não** promete resposta: "Um nome. Sem respostas." — causa da
  morte e código seguem em aberto nas fontes
- [x] Sem graphicidade gratuita; sem CTA comercial
- [ ] **Escuta humana pendente** de "Somerton", "Adelaide", "Tamám Shud",
  "Omar Caiame", "Glenelg" (transliterações registradas no `briefing.md`)

## Identidade

- [x] Paleta, tipografia, moldura, marca `DOSSIÊ 45` e dossiê `007`
- [x] Voz impessoal, sem "eu" ou "nós"
- [x] Drone a 0,16 (mesmo arquivo dos anteriores — inaudível por projeto; som
  audível é variável de canal novo, não deste lote)
- [x] Capa `capa.png` — frame em 17,7 s, 1080×1920: `O PAPEL DIZIA: ACABADO. /
  PERSIA, TAMÁM SHUD.` (cena 5, 16,05–19,41 s)

## Ritmo (variável do lote 007–011: o gancho)

| Medida | 005 | 006 | **007** |
|---|---:|---:|---:|
| Palavras escritas | 111 | 114 | **108** |
| Cenas | 12 | 14 | **12** |
| Cena mais longa | 5,00 s | 4,17 s | **5,029 s** (cena 3) |
| Cena 2 | sobe a aposta | sobe a aposta | **sobe a aposta** (sem etiqueta, sem documento, sem nome) |
| Gancho | "Cinco aviões pediram socorro" | "Eles cortaram a encosta" | **"Um homem morto na praia. Um código costurado na roupa."** — ação/consequência, sem contexto |

A cena 3 ficou em **5,029 s** — 29 ms acima do teto de 5 s fixado no lote; foi
o **1 aviso** do contrato. Não justifica re-render: o corte é por bloco de fala
("Somerton Park, Adelaide. Primeiro de dezembro de 1948.") e re-sintetizar a
cena mudaria a duração total. Registrado para os próximos: **separar data de
lugar** quando a fala passar de 5 s.

## Achado novo — frames de QA duplicados

`frame_s1.png` e `frame_fecho.png` (extraídos em 29/10 17:59) tinham **o mesmo
SHA-256** (`5CEB3375…`): a extração falhou e gravou o mesmo PNG duas vezes. Os
frames foram **re-extraídos do `final.mp4`** (`qa-final/qa-frame-01..07.png`) e
conferidos. Os arquivos antigos foram preservados como evidência em
`qa-final/antigos-extracao-falhou/`.

## Correção de cadeia de áudio

O `final_raw.mp4` saiu em **−10,6 LUFS** porque a voz foi pré-normalizada com
**+5 dB** antes do render (diferente de 004–006, que subiam no pós). O passo de
normalização de 29/10 **reduziu** o volume sem registro do filtro. O áudio foi
**reprocessado em 31/10** com cadeia explícita:
`volume=-4.4dB,alimiter=limit=0.85:level=disabled` → **−15,0 LUFS**. O
`final_raw.mp4` (cru) está preservado.

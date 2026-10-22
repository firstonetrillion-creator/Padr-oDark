# QA — 002-mary-celeste

**Data:** 2026-10-21
**Arquivo:** `final.mp4` (cópia de publicação: `002-mary-celeste_shorts_v1.mp4`)
**Render:** standard, 1080×1920, 30 fps, segmentado 5×300 frames, **3m00,9s**
**Duração:** 45,01 s · **Tamanho:** 3,6 MB
**Voz:** Piper `pt_BR-faber-medium`, `length_scale` 1,12; cru 43,04 s → 45,00 s com 0,6 s de respiro

## Técnico

| Item | Medição | Status |
|---|---|---|
| Codec de vídeo | H.264, 1080×1920 | OK |
| FPS | 30/1 constante | OK |
| Áudio | AAC 48 kHz, estéreo | OK |
| Loudness | −15,4 LUFS (cru: −21,5; ganho +6,2 dB) | OK |
| Pico | limitador em 0,85 (−1,5 dBFS) | OK |
| Preto inesperado | nenhum (fade final intencional em 44,3 s) | OK |
| Margem lateral | 120 px | OK |
| Margem inferior | rodapé a 190 px | OK |
| Texto cortado | 13 cenas conferidas em frame; nenhuma acima de 4 linhas | OK |
| Sincronia | timestamps do faster-whisper; 13 cenas | OK |
| Fantasma de cena | `autoAlpha` por cena; bordas 4,1 s e 7,2 s conferidas | OK |
| Contrato | `check-contrato.ps1` — 29 invariantes | OK (0 avisos) |

## Editorial

- [x] Gancho visual em 0,0 s; texto do gancho visível em 0,02 s; voz em 0,24 s
- [x] Uma ideia por vídeo (o abandono do Mary Celeste e a lenda do jantar)
- [x] Fato verificável: Begg, Hicks, Fay e registros de Gibraltar
- [x] Lenda marcada como lenda no frame 1 (“A LENDA”) e corrigida na cena 2
- [x] Teoria apresentada como “mais conhecida”, não como conclusão provada
- [x] Twist antes do fecho: o jantar é invenção; o bote é o dado real
- [x] CTA natural, sem quebrar o tom (“O arquivo explica o abandono. Não explica o silêncio.”)
- [x] Sem afirmação difamatória sobre pessoa real
- [x] Sem graphicidade gratuita
- [x] “Nove chegaram vazios” não afirma que os barris estavam vazios no achado

## Identidade

- [x] Paleta, tipografia, moldura, marca “DOSSIÊ 45” e dossiê “002”
- [x] Voz impessoal, sem “eu” ou “nós”
- [x] Drone a 0,16, mesma família sonora do piloto
- [x] Capa `capa.png` extraída do frame em 1,5 s
- [x] Arquivo nomeado `002-mary-celeste_shorts_v1.mp4`

## Publicação

- [x] Título, descrição e hashtags em `publicacao.md`
- [x] Lint de título PT-BR: **98/100** (único aviso: truncamento no feed mobile)
- [x] Aviso de conteúdo sintético marcado na plataforma (selo **AI** visível)
- [x] Aprovação humana do vídeo — **aprovado em 21/10/2026**
- [x] Publicar no YouTube Shorts — https://youtube.com/shorts/n6dtveQguf4
- [x] Registrar em `biblioteca/publicados.csv`
- [ ] Medir retenção em 48 h — **agendado para 23/10/2026**

## Veredito

**QA técnico: PASS. Publicado no YouTube Shorts em 21/10/2026.**

Publicado após aprovação humana explícita e com a descrição do canal conferida
na vitrine pública.

# QA — 004-mv-joyita

**Data:** 2026-10-23
**Arquivo:** `final.mp4` (cópia de publicação: `004-mv-joyita_shorts_v1.mp4`)
**Render:** standard, 1080×1920, 30 fps, segmentado 5×300 frames, 1 worker,
low-memory; 1350/1350 frames, 0 retries, 4 reciclagens de browser
**Duração:** 45,013 s · **Tamanho:** 3.652.954 bytes (3,65 MB)
**Voz:** Piper `pt_BR-faber-medium`, `length_scale` 0,90; cru 44,117 s → 45,000 s
**SHA-256 (`final.mp4`):** `406906CE2F8AC652CCF33A828EF6E1E120CBD1A8EA9645ACAC5E8968BEA6EED7`

## Técnico

| Item | Medição | Status |
|---|---|---|
| Codec de vídeo | H.264, 1080×1920 | OK |
| FPS | 30/1 constante | OK |
| Áudio | AAC 48 kHz, estéreo | OK |
| Loudness | −15,16 LUFS (cru: −21,64; ganho +6,5 dB) | OK |
| Pico | true peak −1,42 dBFS; limitador em 0,85 (−1,41 dBFS) | OK |
| Preto inesperado | nenhum; fade final em 44,3–45,0 s é intencional | OK |
| Texto cortado | 13 cenas conferidas em frame; nenhuma acima de 4 linhas | OK |
| Cena 6 | quebra corrigida para 4 linhas explícitas (“CARGUEIRO” / “O ACHOU.”) | OK |
| Cena 13 | fecho em 2 linhas a 84 px, sem overflow | OK |
| Sincronia | timestamps do faster-whisper; 13 cenas | OK |
| Fantasma de cena | `autoAlpha` por cena; 14 frames do render conferidos | OK |
| Contrato | `check-contrato.ps1` — 29 invariantes | OK (0 avisos) |
| QA automático | `qa.ps1` | **PASS** |
| Marca | `DOSSIÊ 45` / dossiê `004` | OK |

## Editorial

- [x] Gancho visual em 0,0 s; texto do gancho no frame 1; voz entra em 0,0 s
- [x] Uma ideia por vídeo: o barco achado vazio que não afundaria
- [x] Fatos com fonte: relatório da Comissão de Inquérito (Apia, 1956) e
  David G. Wright, *Joyita: Solving the Mystery*
- [x] **25 pessoas** = 16 tripulantes + 9 passageiros (a divisão fica no
  `briefing.md`; o vídeo usa o total)
- [x] “Abandono inexplicável” é atribuído ao relatório, não ao canal
- [x] Nenhuma afirmação sobre o que aconteceu com as 25 pessoas
- [x] “Não afundaria” limitado ao casco de cortiça; não afirma navegabilidade
- [x] Bote e balsas lançados; sem destino nem ocupantes
- [x] Sem graphicidade gratuita; sem CTA comercial
- [x] ASR do modelo `small` ouviu “Rumatokelao” em vez de “rumo a Tokelau” e
  “estimou”; **escuta humana pendente** para “Joyita”, “Tokelau” e “Apia”

## Identidade

- [x] Paleta, tipografia, moldura, marca `DOSSIÊ 45` e dossiê `004`
- [x] Voz impessoal, sem “eu” ou “nós”
- [x] Drone a 0,16, mesma família sonora de 001–003
- [x] Capa `capa.png` — frame em 4,0 s, 1080×1920, “25 PESSOAS / NENHUM SINAL”

## Alerta de ritmo (não bloqueia)

A cena 2 ocupa **3,03–9,60 s** (6,57 s) com um único cartão estático
(“25 PESSOAS / NENHUM SINAL”). É a maior permanência do vídeo e cai bem em
cima da janela de decisão dos 10 s. Se a retenção do 003 mostrar queda nesse
ponto, dividir o cartão em dois beats dentro da mesma cena (sem mudar o
número de cenas) e re-renderizar — o render leva ~3 min.

## Publicação

- [ ] Aprovação humana do `final.mp4` — **pendente**
- [ ] Título, descrição e hashtags em `publicacao.md`
- [ ] Publicar no YouTube Shorts
- [ ] Registrar em `biblioteca/publicados.csv`
- [ ] Medir retenção em 48 h

## Veredito

**QA técnico e visual: PASS.** Pronto para aprovação humana; **não publicar**
sem “Aprovado — publicar”.

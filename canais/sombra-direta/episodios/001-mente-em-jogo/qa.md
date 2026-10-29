# QA — 001-mente-em-jogo (canal sombra-direta)

**Data:** 27/10/2026  
**Resultado:** QA PASS

## Vídeo

| Item | Valor | Status |
|---|---|---|
| Arquivo | `final.mp4` | OK |
| Duração | 45,01 s | OK (44–46 s) |
| Resolução | 1080×1920 | OK |
| Codec vídeo | H.264 | OK |
| FPS | 30 | OK |
| Codec áudio | AAC 48 kHz estéreo | OK |
| Loudness | −14,6 LUFS | OK (alvo −15) |
| Pico | dentro do limite | OK (limiter 0,85) |
| Preto inesperado | nenhum | OK |

## Áudio

| Faixa | Fonte | Volume |
|---|---|---|
| voz | `voz.wav` (Piper, cena por cena, ls 1.20) | 1,0 |
| drone/bed | `bed.wav` (FFmpeg lavfi, ruído low-pass) | 0,35 |
| impacto | `impacto.wav` (3 pulsos em 21/26/41 s) | 0,9 |

## Cenas

| # | Início | Duração | Beat | Fonte | Linhas |
|---|---|---|---|---|---|
| s1 | 0,000 | 4,946 s | Gancho | 126 px | 2 |
| s2 | 4,946 | 6,028 s | Contexto | 134 px | 3 |
| s3 | 10,974 | 5,768 s | Pista 1 | 118 px | 2 + small |
| s4 | 16,742 | 5,317 s | Pista 2 | 142 px | 2 + small |
| s5 | 22,059 | 4,448 s | Pista 3 | 110 px | 3 |
| s6 | 26,507 | 2,498 s | Transição | 126 px | 2 |
| s7 | 29,005 | 3,205 s | Twist | 142 px | 3 (glitch CSS) |
| s8 | 32,210 | 3,248 s | Twist | 118 px | 3 |
| s9 | 35,458 | 3,505 s | Fecho | 134 px | 2 |
| s10 | 38,963 | 2,095 s | Fecho | 120 px | 1 |
| s11 | 41,058 | 3,942 s | Fecho | 110 px | 2 |

**Aviso:** cenas s2 (6,03 s), s3 (5,77 s) e s4 (5,32 s) estão acima de 5 s (regra pós-004). Ajustar se a retenção pedir divisão.

## Visual

- Template: `templates/sombra-cinema/` (CSS + GSAP, sem WebGL/Three.js)
- Fundo animado (scale 1.04→1.12 ao longo de 45 s)
- Texto com fade + scale de entrada
- Destaque animado (`.accent`) nas cenas s1 e s11
- Glitch por CSS na cena s7 (twist)
- Vignette e pulse no fundo

## Capa

- `capa.png` extraída em 2,5 s (cena s1 — gancho)
- Título: "VOCÊ É MANIPULADO. / NÃO SENTE NADA."

## Próximo

Aguardar aprovação humana para publicação em conta Google separada do Dossiê 45.

# Template — Sombra Cinema

Composição de 45 s, 1080×1920, 30 fps, para o canal `sombra-direta`.
Baseada no `misterio-45`, mas com **efeitos visuais reforçados** via CSS + GSAP apenas:
fundo animado em escala lenta, texto com fade + escala, destaque animado, glitch sério por
CSS (sem WebGL, sem Three.js, sem shaders — regra inviolável, GPU Intel HD 620).

## O que vem

| Arquivo | Conteúdo |
|---|---|
| `index.html` | 12–16 cenas, CSS/GSAP, áudio `voz`/`bed`/`impacto`, QA por `?t=` |
| `gsap.min.js` | dependência local (sem CDN) — copiar de `templates/misterio-45/` |

**Não inclui** `voz.wav`, `bed.wav` nem `impacto.wav`: cada episódio gera os seus.

## Como usar

1. Copie a pasta para `canais\<slug>\episodios\<episodio>\` ou use como base do episódio.
2. Troque os textos de cada cena, os tempos (`data-start` / `data-duration`) e o áudio.
3. Ajuste `fonte_px` e classes `.c1`…`.c16` no CSS conforme `medir-texto.ps1`.
4. Copie `voz.wav`, `bed.wav` e `impacto.wav` para a pasta do episódio. Mantenha os `id`.
5. Render segmentado (mesmo comando do misterio-45).

## Regras do formato

- 45 s, 1080×1920, 30 fps, H.264 + AAC.
- Texto é a imagem: sem WebGL, sem Three.js, sem vídeo de fundo.
- Efeitos permitidos: scale, fade, translate, blur, flicker por CSS/GSAP.
- Máximo 5 s por cena (regra pós-004).
- Fato com fonte; lenda marcada como lenda.
- Áudio: voz em 1,0; bed audível; pulsos de impacto gerados por FFmpeg lavfi.

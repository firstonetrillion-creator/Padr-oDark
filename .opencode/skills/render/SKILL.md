---
name: Render
description: Use para renderizar a composição HyperFrames em MP4 9:16.
---

# Render

## Objetivo
Transformar roteiro + voz em MP4 1080×1920 sem estourar o tempo da máquina.

## Ferramenta
HyperFrames (HTML/CSS/GSAP → Chrome headless → FFmpeg).

## Passos
1. Criar composição a partir de `templates/misterio-45/`.
2. Colocar assets em `episodios/<slug>/assets/`.
3. Transcrever `voz.wav` com timestamps (`scripts/transcribe.py`) e derivar os tempos de cena.
4. Ajustar timelines ao áudio (`voz.wav`).
5. Renderizar em draft primeiro.
6. Aprovar enquadramento e legendas.
7. Renderizar 1080p final.

## Sincronizar cena com fala
```powershell
.\.venv\Scripts\python.exe scripts\transcribe.py `
  episodios\<slug>\voz.wav --model small --language pt `
  --output episodios\<slug>\transcricao.json
```

- Usar os `start`/`end` de cada frase como janela da cena: `data-start` = início da frase − 0,05 s; `data-duration` = próxima cena − início.
- Deixar 0,05 s de respiro entre cenas (evita dois textos no mesmo frame).
- Não confiar no texto transcrito (nomes próprios saem errados); usar só os tempos.
- Frases longas (> 4 s) podem virar duas cenas, cortando na pausa natural.
- A última cena cobre a cauda do áudio até o fim do vídeo.

## Comandos
```powershell
npx hyperframes doctor
npx hyperframes lint
npx hyperframes check
npx hyperframes render --composition index.html --output preview.mp4 --quality draft
npx hyperframes render --composition index.html --output final.mp4 --quality standard
```

## Regras
- Um render por vez.
- Fechar navegador, Spotify e apps pesados.
- Não usar WebGL/Three.js.
- Preferir CSS/GSAP e imagens estáticas com parallax.
- Se passar de 12 min em 1080p/45 s, reduzir efeitos.

## QA visual sem render (segundos, não minutos)
A composição lê `?t=12.5` e congela a timeline naquele segundo (as cenas fora da janela ficam ocultas). Serve para checar quebra de linha, margem e sobreposição antes de renderizar:
```powershell
$chrome = (Get-ChildItem "$env:USERPROFILE\.cache\hyperframes\chrome\chrome-headless-shell" -Recurse -Filter chrome-headless-shell.exe | Select-Object -First 1).FullName
$uri = [System.Uri]::new((Resolve-Path index.html)).AbsoluteUri
& $chrome --disable-gpu --hide-scrollbars --window-size=1080,1920 `
  --virtual-time-budget=1500 --screenshot=qa-frames\t12.5.png "$uri`?t=12.5"
```
Conferir um frame no meio de cada cena, não só o primeiro.

## Render em máquina apertada (8 GB)
Se o Chrome cair com `Target closed` perto do fim, usar captura segmentada: recicla o navegador a cada N frames e permite retomar.
```powershell
$env:HF_SEGMENTED_CAPTURE = "true"
$env:HF_SEGMENT_FRAMES = "300"          # 10 s a 30 fps
$env:HF_SEGMENT_BROWSER_RECYCLE = "1"
hyperframes render --output preview.mp4 --quality draft --fps 30 `
  --workers 1 --low-memory-mode --protocol-timeout 600000 --resume --keep-segments
```
O `--resume` reaproveita segmentos já concluídos; `--keep-segments` os mantém se precisar inspecionar.

## Saída
- `preview.mp4` (draft)
- `final.mp4` (1080×1920, H.264, AAC)

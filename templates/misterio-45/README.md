# Template — Mistério 45

Composição tipográfica de 45 s, 1080×1920, 30 fps, validada no episódio `001-faroleiros` (render standard em 3m18s numa máquina de 8 GB).

## O que vem

| Arquivo | Conteúdo |
|---|---|
| `index.html` | 13 cenas sincronizadas, CSS/GSAP, áudio `voz`/`drone`, QA por `?t=` |
| `gsap.min.js` | dependência local (sem CDN) |
| `beat-sheet.md` | os 13 beats, tempos de referência e limites de texto |

**Não inclui** `voz.wav` nem `drone.wav`: cada episódio gera os seus.

## Como usar

### 1. Criar o episódio
```powershell
Copy-Item -Recurse templates\misterio-45 episodios\<slug>
```

### 2. Voz
Escrever `narracao.txt` com **110–125 palavras** e gerar:
```powershell
.\.venv\Scripts\python.exe scripts\tts.py `
  --model models\vozes\pt_BR-faber-medium.onnx `
  --input episodios\<slug>\narracao.txt `
  --output episodios\<slug>\voz_raw.wav --length-scale 1.28
```
Processar para exatamente 45,00 s (ver skill `voz`) e gerar/ copiar `drone.wav` de 45 s.

### 3. Transcrever para obter tempos
```powershell
.\.venv\Scripts\python.exe scripts\transcribe.py `
  episodios\<slug>\voz.wav --model small --language pt `
  --output episodios\<slug>\transcricao.json
```

### 4. Remapear as 13 cenas
Para cada frase do JSON:

- `data-start` = `start` da frase − 0,05 s
- `data-duration` = `start` da próxima cena − `data-start` − 0,05 s
- Deixar 0,05 s entre cenas (evita dois textos no mesmo frame)
- A última cena cobre a cauda até 45,00 s
- Frases com mais de 4 s podem virar duas cenas na pausa natural

O texto transcrito serve só para tempos: nomes próprios saem errados.

### 5. Trocar textos e tamanhos
Substituir o conteúdo de cada `<h1>` e ajustar `.s1`…`.s13` no CSS. Regra prática: se a linha chega perto de 840 px, quebra antes com `<br>` ou reduz 4–8 px. O template já tem `text-wrap: balance`.

### 6. Áudio
Copiar `voz.wav` e `drone.wav` para a pasta do episódio. Manter:
```html
<audio id="voz" ... data-track-index="0" data-volume="1">
<audio id="drone" ... data-track-index="2" data-volume="0.16">
```
Sem `id`, o render sai **mudo**.

### 7. QA visual antes do render
Cada cena aceita `?t=segundo`; conferir o meio de cada uma:
```powershell
$chrome = (Get-ChildItem "$env:USERPROFILE\.cache\hyperframes\chrome\chrome-headless-shell" -Recurse -Filter chrome-headless-shell.exe | Select-Object -First 1).FullName
$uri = [System.Uri]::new((Resolve-Path index.html)).AbsoluteUri
& $chrome --disable-gpu --hide-scrollbars --window-size=1080,1920 `
  --virtual-time-budget=1500 --screenshot=qa-frames\t12.5.png "$uri`?t=12.5"
```

### 8. Render
```powershell
$env:HF_SEGMENTED_CAPTURE = "true"
$env:HF_SEGMENT_FRAMES = "300"
$env:HF_SEGMENT_BROWSER_RECYCLE = "1"
hyperframes render --output final_raw.mp4 --quality standard --fps 30 `
  --workers 1 --low-memory-mode --protocol-timeout 600000 --resume
```
Segmentar evita o `Target closed` no fim do render. Não abrir outro Chrome durante.

### 9. Normalizar loudness
Medir o cru e aplicar ganho estático (o piloto precisou de +6,2 dB):
```powershell
ffmpeg -i final_raw.mp4 -c:v copy `
  -af "volume=6.2dB,alimiter=limit=0.85:level=disabled" `
  -c:a aac -b:a 192k -movflags +faststart final.mp4
```
Alvo: −15 LUFS, pico ≤ −1,5 dBFS. Não usar `loudnorm` dinâmico em narração contínua.

### 10. QA e publicação
```powershell
.\scripts\qa.ps1 episodios\<slug>\final.mp4
```
Só publicar com `QA PASS` e `qa.md` assinado. Copiar para `<slug>_shorts_v1.mp4` e usar `capa.png`.

## Regras do formato
- 13 cenas, 45 s, 1 ideia, gancho em 2 s.
- Texto é a imagem: sem WebGL, sem Three.js, sem vídeo de fundo.
- Twist por volta de 34 s; fecho em pergunta.
- Fato com fonte; lenda marcada como lenda.

## Armadilhas já resolvidas
| Sintoma | Causa | Correção |
|---|---|---|
| Texto fantasma de outra cena | GSAP só anima entrada | `autoAlpha` por cena (já no template) |
| Render mudo | `<audio>` sem `id` | manter `id="voz"` e `id="drone"` |
| Chrome fecha em 1300/1350 | memória acumulada | captura segmentada + 1 worker |
| Linha quebra diferente no render | fonte na fronteira dos 840 px | reduzir 4–8 px ou quebrar antes |
| Áudio em −22 LUFS | TTS baixo + drone discreto | ganho estático + limitador no pós |
| `qa.ps1` falha no ffmpeg | stderr tratado como erro | rodar com `-ExecutionPolicy Bypass`; script já contorna |

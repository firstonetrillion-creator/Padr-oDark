---
name: Voz
description: Use para gerar e processar a narração com Piper TTS.
---

# Voz

## Objetivo
Gerar narração limpa, consistente e com tempo previsível.

## Ferramenta
Piper TTS, voz `pt_BR-faber-medium`, CPU. Usar **`scripts/tts.py`**, não o `piper.exe` direto: o espeak-ng falha com caminhos que têm acento (`Padrão`).

## Comando
```powershell
.\.venv\Scripts\python.exe scripts\tts.py `
  --model models\vozes\pt_BR-faber-medium.onnx `
  --input episodios\<slug>\narracao.txt `
  --output episodios\<slug>\voz_raw.wav `
  --length-scale 1.28
```

- `length_scale` > 1 = fala mais lenta.
- Para 45 s, 1.26–1.30 costuma cair entre 41 e 43 s; o restante vem de pausas.
- O script usa `C:\Users\valentim\Tools\piper-data\espeak-ng-data` (caminho ASCII).

## Processamento (FFmpeg)
```powershell
ffmpeg -y -i voz_raw.wav -af "highpass=f=80,equalizer=f=3500:t=q:w=1:g=3,acompressor=threshold=-18dB:ratio=3:attack=5:release=120,alimiter=limit=0.95,adelay=600|600,apad" -t 45 -ar 48000 -ac 2 voz.wav
```

- `adelay` = respiro inicial; `apad` + `-t 45` = cauda para o CTA visual.
- Ajustar `-t` à duração do episódio.

## Regras
- Uma locução por vídeo; não misturar vozes.
- Pausas de 0,3 s antes do twist (inserir silêncio no roteiro).
- Sem respiração artificial em cima da fala.
- Guardar `voz_raw.wav` e `voz.wav`.

## Saída
- `voz_raw.wav`
- `voz.wav`
- duração medida com `ffprobe`.

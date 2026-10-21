---
name: QA
description: Use antes de publicar para validar técnica, editorial e identidade.
---

# QA

## Objetivo
Impedir publicação de vídeo com falha técnica ou editorial.

## Automático
```powershell
.\scripts\qa.ps1 episodios\<slug>\final.mp4
```

O script confere duração, 1080×1920, 30 fps, AAC 48 kHz estéreo, loudness −17..−13 LUFS e trechos pretos inesperados (ignora o fade final e usa limiar de 2% para não confundir com o fundo escuro do canal).

## Normalizar loudness
O render cru sai baixo (TTS + drone). Medir e aplicar ganho estático com limitador, sem reencodar o vídeo:
```powershell
ffmpeg -i final_raw.mp4 -c:v copy `
  -af "volume=6.2dB,alimiter=limit=0.85:level=disabled" `
  -c:a aac -b:a 192k -movflags +faststart final.mp4
```
Ajustar o ganho para o alvo de −15 LUFS (teto de pico −1,5 dBFS). Não usar loudnorm dinâmico em narração contínua: bombeia a voz.

## Manual
Seguir `docs/QA.md`:

- Técnico: codec, resolução, fps, loudness, safe margins, legendas.
- Editorial: gancho em 2 s, uma ideia, fato verificável, twist antes do CTA.
- Identidade: paleta, tipografia, grain, voz, som.
- Publicação: título, descrição, hashtags, aviso de IA.

## Bloqueios
- Frame preto > 0,2 s
- Texto cortado
- Áudio clipando
- Fato sem fonte
- Tom fora do canal

## Saída
`episodios/<slug>/qa.md` assinado com data.

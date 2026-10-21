# QA — checklist por vídeo

## Automático

```powershell
.\scripts\qa.ps1 episodios\<slug>\final.mp4
```

Verifica duração, 1080×1920, 30 fps, AAC 48 kHz estéreo, loudness -17..-13 LUFS e trechos pretos > 0,2 s. Retorna `QA PASS` ou `QA FAIL`.

## Técnico

- [ ] `ffprobe` confere: H.264, 1080×1920 (ou 1920×1080), fps constante, duração alvo
- [ ] Áudio: AAC 48 kHz, estéreo, sem clipping
- [ ] Loudness integrado entre -14 e -16 LUFS (Short) / -14 LUFS (YouTube)
- [ ] Nenhum frame preto inesperado
- [ ] Nenhum texto cortado na safe margin (9:16: 250 px topo/base, 120 px laterais)
- [ ] Legendas sincronizadas e legíveis em tela pequena
- [ ] Arquivo nomeado: `<slug>_<formato>_v<versao>.mp4`

## Editorial

- [ ] Gancho resolve em até 2 s
- [ ] Uma ideia por vídeo
- [ ] Fato verificável ou claramente marcado como lenda/ficção
- [ ] Twist ou implicação antes do CTA
- [ ] CTA natural, sem quebrar o tom
- [ ] Sem afirmação difamatória sobre pessoa real
- [ ] Sem graphicidade gratuita (política de anúncios)

## Identidade

- [ ] Paleta e tipografia do canal aplicadas
- [ ] Grain/vinheta dentro do padrão
- [ ] Voz com o mesmo processamento (pitch, EQ, compressão, reverb)
- [ ] Drone/SFX na mesma família sonora
- [ ] Capa coerente com o frame mais forte

## Publicação

- [ ] Título com palavra-chave e curiosidade, sem clickbait vazio
- [ ] Lint de título + thumbnail rodado (`tools/youtube-agent-skill/yt-package/title.py`)
- [ ] Descrição com contexto e fontes
- [ ] Hashtags: 3–5, específicas
- [ ] Declaração de conteúdo de IA quando exigido pela plataforma
- [ ] Formato vertical para TikTok/Reels; horizontal ou vertical para YouTube
- [ ] Registro em `publicados.csv`

## Pós-publicação (48 h)

- [ ] CSV de retenção do Studio baixado e rodado com `retention.py --duration 45`
- [ ] Retenção 3 s anotada
- [ ] Retenção 10 s anotada
- [ ] Retenção média anotada
- [ ] Comentários lidos; objeções viram gancho
- [ ] Decisão: manter, ajustar ou matar o formato

# QA — 003-roanoke

**Data:** 2026-10-23
**Arquivo:** `final.mp4` (cópia de publicação: pendente)
**Render:** standard, 1080×1920, 30 fps, segmentado 5×300 frames, 1 worker,
low-memory
**Duração:** 45,013 s · **Tamanho:** 3.557.345 bytes (3,56 MB)
**Voz:** Piper `pt_BR-faber-medium`, `length_scale` 1,00; cru 44,69 s →
45,00 s

## Técnico

| Item | Medição | Status |
|---|---|---|
| Codec de vídeo | H.264, 1080×1920 | OK |
| FPS | 30/1 constante | OK |
| Áudio | AAC 48 kHz, estéreo | OK |
| Loudness | −15,4 LUFS (cru: −21,9; ganho +6,5 dB); `qa.ps1` lê −15,5 por arredondamento | OK |
| Pico | true peak −1,4 dBFS; limitador em 0,85 (−1,41 dBFS) | OK |
| Preto inesperado | nenhum; fade final intencional | OK |
| Margem lateral | 120 px | OK |
| Margem inferior | rodapé a 190 px | OK |
| Texto cortado | 13 cenas conferidas em frame; nenhuma acima de 4 linhas | OK |
| Sincronia | timestamps do faster-whisper; 13 cenas | OK |
| Fantasma de cena | `autoAlpha` por cena; transições principais conferidas | OK |
| Contrato | `check-contrato.ps1` — 29 invariantes | OK (0 avisos) |
| Marca | `DOSSIÊ 45` / dossiê `003` | OK |

## Editorial

- [x] Gancho visual em 0,0 s; texto do gancho visível no frame 1; voz em 0,66 s
- [x] CROATOAN entregue na cena 2, em 3,75 s, antes de geografia/contexto
- [x] Uma ideia por vídeo: o desaparecimento da colônia e o recado na madeira
- [x] Fatos com fonte: NPS Fort Raleigh e David Beers Quinn, *The Roanoke
  Voyages, 1584–1590*
- [x] Número **117** usado com a variação **117–118** documentada em
  `briefing.md`
- [x] “Nenhum corpo” significa ausência no sítio, não prova de morte de todos
- [x] Teorias apresentadas como não provadas; nenhuma lenda marcada como fato
- [x] Sem afirmação difamatória sobre pessoa real
- [x] Sem graphicidade gratuita
- [x] TTS com `Croatoun` em `narracao_tts.txt`; tela com `CROATOAN` e texto
  canônico com `Croatoan`
- [x] ASR ouviu “Croaton” nas duas ocorrências; com prompt de contexto também
  confirmou “criança inglesa”. O modelo pequeno ainda tropeça em “Julho”,
  “gravada” e “Ninguém”; conferir na aprovação humana

## Identidade

- [x] Paleta, tipografia, moldura, marca `DOSSIÊ 45` e dossiê `003`
- [x] Voz impessoal, sem “eu” ou “nós”
- [x] Drone a 0,16, mesma família sonora do piloto e do 002
- [x] **Correção de marca:** o primeiro render ainda exibia
  `ARQUIVO NOTURNO`; o `index.html` foi corrigido para `DOSSIÊ 45` e o vídeo
  foi renderizado de novo. Os artefatos antigos ficaram preservados como
  `*_brand-antigo`
- [ ] Capa `capa.png` — criar após aprovação
- [ ] Cópia de publicação `003-roanoke_shorts_v1.mp4` — criar após aprovação

## Publicação

- [ ] Aprovação humana do `final.mp4` — **pendente**
- [ ] Título, descrição e hashtags em `publicacao.md` — criar após aprovação
- [ ] Publicar no YouTube Shorts
- [ ] Registrar em `biblioteca/publicados.csv`
- [ ] Medir retenção em 48 h

## Veredito

**QA técnico e visual: PASS. Pronto para aprovação humana. Não publicado.**

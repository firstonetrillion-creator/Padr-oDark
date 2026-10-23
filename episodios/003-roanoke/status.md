# Status — 003

> Criado por `scripts/novo-episodio.ps1` em 2026-10-21 22:33 a partir de `templates/misterio-45`
> (sha256 `0e0a2281`, commit `ac25c1e`). Atualizado em 23/10/2026: render,
> normalização e QA concluídos; aprovação humana pendente. A marca foi
> corrigida para `DOSSIÊ 45` antes do render final.

| Etapa | Estado | Artefato |
|---|---|---|
| Briefing | pronto | `briefing.md` (fontes NPS + Quinn) |
| Gancho | pronto e aprovado | `gancho.md` (fórmula 1 — O Dado; revisão de 23/10) |
| Roteiro | pronto | `roteiro.md` (113 palavras, 13 cenas) |
| Narração | **pronta** | `voz_raw.wav` 44,69 s; `voz.wav` 45,00 s; `narracao_tts.txt` com a grafia fonética `Croatoun` |
| Transcrição | **pronta** | `transcricao.json` (45,00 s; timestamps por palavra) |
| Assets | não usado | v1 tipográfica (sem imagens) |
| Composição | **pronta** | `index.html` (13 cenas sincronizadas; marca `DOSSIÊ 45`) |
| QA visual | **pronto** | `qa-final/` (14 frames: frame 1, CROATOAN, twist, fecho, fade); `qa-frames-brand-antigo/` preserva o QA anterior |
| Render | **pronto** | `final_raw.mp4` 45,000 s; `final.mp4` 45,013 s |
| QA | **PASS** | `qa.md` (técnico + visual) |
| Publicação | pendente | aprovação humana; depois YouTube Shorts |

## Medições

- Voz crua: **44,69 s** (`length_scale` 1,00, `noise_scale` 0,65, `noise_w` 0,80)
- Voz final: **45,00 s**, 48 kHz estéreo, **−21,99 LUFS**, pico **−7,22 dB**
- Contrato (`check-contrato.ps1`): **OK, 0 avisos**
- Render: segmentado **5×300 frames**, 1 worker, low-memory; `final_raw.mp4`
  **45,000 s**, **3.559.598 bytes**
- Loudness crua: **−21,9 LUFS**, true peak **−7,2 dBFS**
- Normalização: **+6,5 dB** + `alimiter=limit=0.85:level=disabled`
- `final.mp4`: **45,013 s**, **3.557.345 bytes**, **−15,4 LUFS**, true peak
  **−1,4 dBFS**. O `qa.ps1` lê **−15,5 LUFS** por arredondamento
- QA técnico: **PASS** (`qa.ps1`); QA visual: **PASS** (`qa-final/`)

## Notas de produção

- **Correção de marca:** o primeiro render ainda exibia `ARQUIVO NOTURNO`.
  O `index.html` foi corrigido para `DOSSIÊ 45` e o vídeo foi renderizado de
  novo. Os artefatos antigos ficaram preservados como `*_brand-antigo`.
- **Pronúncia de CROATOAN:** a tela usa `CROATOAN` e o `narracao.txt` usa
  `Croatoan`; o TTS usa `Croatoun` em `narracao_tts.txt` para preservar o
  acento em “toun” e o `n` final. O ASR ouviu “Croaton” nas duas ocorrências;
  com prompt de contexto também confirmou “criança inglesa”.
- **Cenas:** 13 cenas, de 0,00 a 45,00 s; gancho sem fade no frame 1;
  CROATOAN entra em 3,75 s. Tempos conferidos contra `transcricao.json`.
- **Drone:** cópia do bed do 002 com fade-in de 1 s e fade-out de 42–45 s.
- **QA visual:** frame 1, CROATOAN, twist, fecho e fade conferidos em
  `qa-final/frame-01.png` … `frame-14.png`, sem overflow, ghosting ou marca
  errada.
- **Voz:** takes comparados; escolhido o melhor em pronúncia e estabilidade.
  Cadeia: highpass 75 Hz, de-esser leve, EQ (250 Hz −1,5 dB; 3,5 kHz +3 dB;
  8 kHz +1 dB), compressor −18 dB 3:1, limitador 0,95, 0,26 s de respiro e
  pad para 45,00 s.

## Próximos passos

1. **Aprovação humana** do `final.mp4` (assistir e ouvir).
2. Se aprovado: criar `003-roanoke_shorts_v1.mp4`, `capa.png` e
   `publicacao.md`; publicar no YouTube Shorts.
3. Atualizar `biblioteca/publicados.csv` e medir retenção em 48 h.

# Status — 003

> Criado por `scripts/novo-episodio.ps1` em 2026-10-21 22:33 a partir de `templates/misterio-45`
> (sha256 `0e0a2281`, commit `ac25c1e`). Atualizado em 23/10/2026: voz, transcrição,
> composição v1 e QA visual concluídos; render pendente.

| Etapa | Estado | Artefato |
|---|---|---|
| Briefing | pronto | `briefing.md` (fontes NPS + Quinn) |
| Gancho | pronto e aprovado | `gancho.md` (fórmula 1 — O Dado; revisão de 23/10) |
| Roteiro | pronto | `roteiro.md` (113 palavras, 13 cenas) |
| Narração | **pronta** | `voz_raw.wav` 44,69 s; `voz.wav` 45,00 s; `narracao_tts.txt` com a grafia fonética `Croatoun` |
| Transcrição | **pronta** | `transcricao.json` (45,00 s; timestamps por palavra) |
| Assets | não usado | v1 tipográfica (sem imagens) |
| Composição | **pronta** | `index.html` (13 cenas sincronizadas) |
| QA visual | **pronto** | `qa-frames/` (frame 1, 13 cenas, fade); contrato OK |
| Render | pendente | `final_raw.mp4` / `final.mp4` |
| QA | pendente | `qa.md` |
| Publicação | pendente | YouTube Shorts |

## Medições

- Voz crua: **44,69 s** (`length_scale` 1,00, `noise_scale` 0,65, `noise_w` 0,80)
- Voz final: **45,00 s**, 48 kHz estéreo, **−21,99 LUFS**, pico **−7,22 dB**
- Contrato (`check-contrato.ps1`): **OK, 0 avisos**
- Render (standard): —
- Loudness: −21,99 LUFS cru -> — LUFS final (normalizar após o render)

## Notas de produção

- **Pronúncia de CROATOAN:** a tela usa `CROATOAN` e o `narracao.txt` usa
  `Croatoan`; o TTS usa `Croatoun` em `narracao_tts.txt` para preservar o
  acento em “toun” e o `n` final. O ASR ouviu “Croaton” nas duas ocorrências.
- **Cenas:** 13 cenas, de 0,00 a 45,00 s; gancho sem fade no frame 1;
  CROATOAN entra em 3,75 s. Tempos conferidos contra `transcricao.json`.
- **Drone:** cópia do bed do 002 com fade-in de 1 s e fade-out de 42–45 s.
- **QA visual:** frame 1 + 13 cenas + fade, sem overflow. Capturas de QA
  por `?t=`; a captura do Chrome headless pode mostrar fantasma por escala
  fracionária, mas a prévia no navegador e o render não usam esse caminho.
- **Voz:** takes comparados; escolhido o melhor em pronúncia e estabilidade.
  Cadeia: highpass 75 Hz, de-esser leve, EQ (250 Hz −1,5 dB; 3,5 kHz +3 dB;
  8 kHz +1 dB), compressor −18 dB 3:1, limitador 0,95, 0,26 s de respiro e
  pad para 45,00 s.

## Próximos passos

1. Render segmentado (`HF_SEGMENTED_CAPTURE=true`, 300 frames, 1 worker).
2. Medir `final_raw.mp4`; normalizar para ~−15,3 LUFS (ganho esperado ~+6,5 dB)
   com limitador; gerar `final.mp4`.
3. Rodar `qa.ps1`, escrever `qa.md`, aprovar com o usuário e publicar.
4. Atualizar `biblioteca/publicados.csv` e medir retenção em 48 h.

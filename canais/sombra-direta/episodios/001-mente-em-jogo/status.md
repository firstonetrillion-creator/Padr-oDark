# Status — 001-mente-em-jogo (canal sombra-direta)

| Etapa | Estado | Nota |
|---|---|---|
| Canal (ficha.md) | pronto | **3 variáveis mudam vs Dossiê 45** — teste livre, sem leitura comparativa controlada |
| Briefing | pronto | |
| Gancho | pronto | "Você é manipulado agora. E não sente nada." (fórmula 4) |
| Roteiro (md) | pronto | ~101 palavras, 11 cenas |
| Roteiro (json) | pronto | |
| narracao.txt | pronto | |
| narracao_tts.txt | pronto | 11 parágrafos (1 por cena) |
| Voz | **pronta** | Piper `pt_BR-faber-medium`, `length_scale` 1.20, 45.000 s |
| Bed/áudio extra | **pronto** | bed.wav (ruído low-pass), impacto.wav (3 pulsos), voz.wav processado |
| Transcrição | não necessária | tempos vêm de `montar-voz.py` (soma de blocos) |
| index.html | **pronto** | template `sombra-cinema`, CSS+GSAP, sem WebGL |
| Medição de texto | pulada | fontes conservadoras (máx 142 px), texto curto |
| Render | **concluído** | `final_raw.mp4` 45,0 s, 1350 frames, 5 segmentos, 0 retries, 2m54s |
| Áudio normalizado | **concluído** | `final.mp4` +7,0 dB, limiter 0,85 |
| QA | **QA PASS** | `qa.ps1` aprovado, `qa.md` assinado |
| Capa | **pronta** | `capa.png` em 2,5 s |
| Cópia de publicação | **pronta** | `001-mente-em-jogo_shorts_v1.mp4` |
| publicacao.md | **pronto** | título, descrição, fontes, hashtags |
| Aprovação humana | **pendente** | obrigatória antes de publicar |
| Publicação | **pendente** | conta Google separada do Dossiê 45 |
| Retenção 48 h | **pendente** | janela fixa, registrar em `canais/sombra-direta/metricas.csv` |

**Próximo comando:** aguardar aprovação humana, então publicar em conta separada e medir 48 h.

**SHA-256 do final.mp4:** `F1466221164822E5696D0FE5B8B2112AC3E6055F61B7CD0E25B1D3D7B43ABB5E`
**Tamanho:** 1.924.576 bytes (~1,9 MB)
**Loudness:** −14,6 LUFS

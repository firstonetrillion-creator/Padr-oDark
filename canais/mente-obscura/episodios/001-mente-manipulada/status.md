# Status — 001-mente-manipulada (canal mente-obscura)

| Etapa | Estado | Nota |
|---|---|---|
| Canal (ficha.md) | rascunho | **3 variáveis mudam vs Dossiê 45** — precisa escolher 1 antes de publicar |
| Briefing | pronto | |
| Gancho | pronto | "Você é manipulado agora. E não sente nada." (fórmula 4) |
| Roteiro (md) | pronto | ~101 palavras, 15 cenas |
| Roteiro (json) | pronto | cenas sem tempo; tempos virão de `montar-voz.py` |
| narracao.txt | pronto | |
| Voz | pendente | Piper `pt_BR-faber-medium`, `length_scale` 1.20, cena por cena |
| Bed/áudio extra | pendente | FFmpeg lavfi; voz em 1.0, bed audível (drone 0.30) |
| Transcrição | pendente | `transcribe.py` para tempos |
| index.html | pendente | gerar com `gerar-episodio.py` a partir de roteiro.json |
| Medição de texto | pendente | `medir-texto.ps1` antes do render |
| Render | pendente | segmentado, 1 render por vez |
| QA | pendente | `qa.ps1` + `qa.md` assinado |
| Aprovação humana | pendente | obrigatória antes de publicar |
| Publicação | pendente | conta separada do Dossiê 45 |
| Retenção 48 h | pendente | janela fixa, registrar em `metricas.csv` |

**Bloqueio:** método de canal permite **uma** variável por canal. Este episódio propõe nicho + visual + áudio. Escolher qual é a variável única antes de avançar.

**Próximo comando:** definir a variável única do canal, então gerar voz com `montar-voz.py`.

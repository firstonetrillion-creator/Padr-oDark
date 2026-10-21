# youtube-agent-skill — vendor seletivo

- **Origem:** https://github.com/Jakeschincariol/youtube-agent-skill
- **Commit:** `a2feb2104981a375ffd4f87ee04f4f5344ac43c6`
- **Data da cópia:** 2026-10-21
- **Licença:** MIT — ver `LICENSE` (Copyright © 2026 Jake Schincariol)

Este diretório guarda apenas as peças adotadas. O pack inteiro **não** foi
instalado, e nenhuma skill global do Claude Code foi alterada.

## O que foi adotado

| Peça | Estado | Uso no projeto |
|---|---|---|
| `yt-retention/retention.py` | **modificado** | Lê o CSV de retenção do Studio e reporta 3 s, 10 s e 30 s (legado), quedas e slide. |
| `yt-script/hooks.json` | **original** | Fonte das 21 fórmulas de gancho. A versão PT-BR para trabalho está em `docs/GANCHOS-21.md`. |
| `yt-package/title.py` | **modificado** | Lint de título + thumbnail em PT-BR, com stopwords e termos vagos localizados. |

## O que foi deliberadamente deixado de fora

| Peça | Motivo |
|---|---|
| `yt-viral/swipe.py` | Adiado. Exige 4+ vídeos por canal; nossa amostra tem muitos canais com 1–5. O `scripts/nicho.py` já cobre a comparação por canal. Reavaliar após os 6 vídeos. |
| `yt-audit` | Adiado. Faz mais sentido com 6+ vídeos publicados. Reavaliar depois da Fase 2. |
| `yt-edit` | Sem dead air: a narração é TTS e o timing vem da transcrição. |
| `yt-shorts`, `yt-chapters` | Só fazem sentido em long-form. |
| `yt-comment`, `yt-plan`, `yt-seo` | Sem comentários ainda; plano e SEO já têm dono no projeto. |

## Patches aplicados

### `yt-retention/retention.py`

- Janela de gancho padrão **3 s e 10 s**; 30 s fica como métrica legada de long-form.
- Correção do eixo: um CSV em segundos de um vídeo de 45 s tem máximo 45, e a
  heurística original (`max <= 100.5`) o confundia com percentual. Agora há
  detecção por cabeçalho, por duração e por `--axis`.
- Interpolação no instante exato (3,0 s / 10,0 s), em vez de pegar o ponto anterior.
- Leitura de transcrição SRT, VTT ou JSON do faster-whisper sem depender de
  `yt-edit/deadair.py`.
- Saída em PT-BR e `--json` com chaves estáveis.

### `yt-package/title.py`

- Stopwords, termos vagos e mensagens em PT-BR.
- Normalização Unicode para comparar palavras com e sem acento.
- Detecção de nome próprio (ex.: “Mary Celeste”) como alternativa a número/data.
- O score continua heurístico: serve para achar problemas, não como gate.

## Como usar

```powershell
# retenção de um Short de 45 s
.\.venv\Scripts\python.exe tools\youtube-agent-skill\yt-retention\retention.py `
  episodios\<slug>\retencao.csv --duration 45 `
  --transcript episodios\<slug>\transcricao.json

# lint de título + thumbnail
.\.venv\Scripts\python.exe tools\youtube-agent-skill\yt-package\title.py `
  --title "Mary Celeste: o navio encontrado vazio em 1872" `
  --thumb "NAVIO VAZIO"
```

## Licença e uso comercial

MIT permite uso interno, modificação, uso comercial e inclusão no kit pago,
desde que o aviso de copyright e a licença sejam preservados. Não há cláusula
de SaaS multi-tenant como em outras ferramentas avaliadas.

## Regra de manutenção

Não editar `hooks.json` diretamente para “traduzir”: ele é a fonte upstream.
A adaptação de trabalho fica em `docs/GANCHOS-21.md`. Se o upstream mudar,
comparar o commit, atualizar o vendor e registrar a diferença neste arquivo.

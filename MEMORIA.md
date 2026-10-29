# MEMORIA — Padrao-Dark

> **Leia este arquivo primeiro.** Ele é a memória de retomada do projeto.
> Depois: `AGENTS.md` (regras) → `docs/PLANO.md` (fases) → `docs/HISTORICO.md` (o que já foi entregue).
> Última atualização: **2026-10-27**. Se você é uma sessão nova, não refaça o que está marcado como entregue.

## 1. Onde estamos

**Fase 1 concluída e piloto publicado.** O cérebro está instalado, o gate G0 passou, o piloto `001-faroleiros` foi aprovado pelo usuário ("ficou perfeito") e publicado no YouTube Shorts em 21/10/2026. O template `misterio-45` foi extraído e o QA técnico está assinado. A validação de nicho por metadados foi concluída em 21/10/2026: **Mistério/Arquivo é a âncora**. Em 21/10/2026 também foi feita a **adoção seletiva do `youtube-agent-skill`** (retenção 3 s/10 s, 21 ganchos e lint de título). O **002-mary-celeste** foi produzido, passou no QA técnico e foi **publicado no YouTube Shorts em 21/10/2026**. Em 23/10/2026 o Gate 1 foi medido: **002 passa** (3 s 91,6%; 10 s 61,8%) e **001 fica sem curva** (24,3% de retenção inicial). Decisão: manter o v1 e ajustar o gancho do **003-roanoke**, que foi **publicado no YouTube Shorts em 23/10/2026** (https://youtube.com/shorts/8ptxqKGe4Bk). A Fase 2 segue com **3/6 publicados** e os episódios 004–006 na fila.

| Frente | Estado | Evidência |
|---|---|---|
| Cérebro (Node, FFmpeg, Python, Piper, faster-whisper, yt-dlp, HyperFrames) | pronto | `docs/STACK.md` |
| Gate G0 (45 s em 1080×1920) | **PASS** | `logs/bench.json`, 2m32,8s |
| Piloto `001-faroleiros` | **aprovado** | `episodios/001-faroleiros/final.mp4`, `qa.md` |
| Template `misterio-45` | pronto | `templates/misterio-45/` |
| Documentação de retomada | pronta | este arquivo + `docs/ARQUITETURA.md` + `docs/HISTORICO.md` |
| Publicação | **6 publicados** (21/10, 21/10, 23/10, 24/10, 27/10 e 27/10) | 001: [Shorts](https://youtube.com/shorts/WKuNVjl3d5M); 002: [Shorts](https://youtube.com/shorts/n6dtveQguf4); 003: [Shorts](https://youtube.com/shorts/8ptxqKGe4Bk); 004: [Shorts](https://youtube.com/shorts/rlSArCY3bH0); 005: [Shorts](https://youtube.com/shorts/wlPEoYErlZQ); 006: [Shorts](https://youtube.com/shorts/K_sgJjNHg84) |
| Validação de nicho | **concluída (metadados)** | `logs/nicho-2026-10-21.json`, `docs/NICHO.md` |
| Versionamento | **git iniciado (21/10/2026)** | commit `782df62`, tag `ep-001-publicado` |
| 6 vídeos de validação | **6/6 publicados — Fase 2 concluída** | 001–006 no ar |
| **Gate 2 (48 h)** | **PASSA em 29/10/2026 — 3 de 6 > 50%** | 002 87,0% · 003 87,0% · 005 **54,3%** · 004 45,7% · 006 **50,0%** (limite) · 001 33,3% (fora) |
| Episódio 002 — Mary Celeste | **publicado** (21/10/2026) | `episodios/002-mary-celeste/`, [Shorts](https://youtube.com/shorts/n6dtveQguf4) |
| Episódio 003 — Roanoke | **publicado** (23/10/2026) | `episodios/003-roanoke/`, [Shorts](https://youtube.com/shorts/8ptxqKGe4Bk) |
| Canal | **Dossiê 45**: nome, avatar/banner, descrição no ar e 9 shorts antigos privados | [canal](https://youtube.com/@Dossie45), `docs/REBRANDING.md` |
| Ferramentas de análise | **adotadas seletivamente** | `tools/youtube-agent-skill/`, `docs/GANCHOS-21.md` |
| `codebase-memory-mcp` | **não instalado** (adiado) | decisão em `docs/DECISOES.md` |
| Memória de sessão | **`ESTADO.md` como `instructions`** | `opencode.jsonc`, `docs/HISTORICO.md` 2026-10-23 |
| Canais de teste | **método criado (27/10)** — um canal por modelo, uma variável | `canais/README.md`, `canais/dossie45/` |

## 2. O que já foi entregue

### Infraestrutura
- Node v22.23.3, npm 10.9.9, Git 2.56.0, FFmpeg/ffprobe 8.1.3, uv 0.13.4, Python 3.12.15.
- Piper 1.8.0 + voz `pt_BR-faber-medium`; faster-whisper 1.2.1; yt-dlp 2026.8.19.
- HyperFrames 0.8.181 + Chrome Headless Shell 152.
- Tudo em `C:\Users\valentim\Tools` e `.venv` (sem admin).
- Correções aplicadas: DLLs VC++ no onnxruntime/venv, `espeak-ng-data` em caminho ASCII, patch do `av` no faster-whisper. Detalhes em `docs/STACK.md`.

### Conteúdo e método
- 8 skills operacionais em `.opencode/skills/` (briefing, gancho, roteiro, voz, render, qa, publicacao, retencao).
- `docs/`: decisões, stack, nicho, plano, QA, identidade, `GANCHOS-21.md`.
- `biblioteca/`: ganchos, fontes, `publicados.csv`.
- `scripts/qa.ps1`: QA automático (duração, resolução, fps, áudio, loudness, preto inesperado).
- `scripts/check-contrato.ps1`: 29 invariantes da composição antes do render (resolução, cenas, áudio com duração real via ffprobe, `autoAlpha`, timeline montada).
- `scripts/novo-episodio.ps1`: cria episódio a partir do template e carimba `.template-version` (sha256 + commit).
- `scripts/gerar-episodio.py`: escreve o `index.html` a partir do `roteiro.json` (textos, tempos de `tempos_cenas.json`, fonte por cena, GSAP). Teste de aceitação: reproduz o 005 escrito à mão.
- `scripts/montar-voz.py`: sintetiza a narração **cena por cena** e escreve `tempos_cenas.json` + `voz_raw.wav` já na duração final. Substitui o caminho take único + ASR quando o `faster-whisper` erra o texto (foi o caso do 006); o tempo passa a ser soma de blocos, não inferência.
- `scripts/medir-texto.ps1`: mede a **tinta** do texto no frame (`snapshot` → PNG → `ffmpeg gray` → bbox por linha) e sugere `fonte_px`; `-Aplicar` grava no `roteiro.json`. Fecha o ciclo que custou 3 correções manuais no LAB 001.
- `scripts/nicho.py`: coleta metadados de Shorts por nicho (views/inscrito, engajamento); não baixa vídeo.
- `tools/youtube-agent-skill/`: vendor MIT com retenção 3 s/10 s, `hooks.json` e lint de título PT-BR; testes em `scripts/test_youtube_agent.py`.

### Piloto 001 — Eilean Mor
- `narracao.txt` (118 palavras) → `voz_raw.wav` 41,45 s → `voz.wav` 45,00 s.
- `transcricao.json` com timestamps por palavra; 13 cenas sincronizadas.
- `index.html` tipográfico, 1080×1920, 30 fps, 13 cenas, `autoAlpha` por cena.
- `final.mp4`: **45,01 s, 3,3 MB, −15,6 LUFS**, H.264 + AAC 48 kHz estéreo.
- `qa.md`: QA técnico **PASS**; aprovação humana registrada em 21/10/2026.
- Cópia de publicação: `001-faroleiros_shorts_v1.mp4`; capa: `capa.png`.
- **Publicado no YouTube Shorts em 21/10/2026:** https://youtube.com/shorts/WKuNVjl3d5M (canal Dossiê 45; à época, Cod Mind Million).

### Episódio 002 — Mary Celeste (21/10/2026)
- Tema: abandono documentado × lenda do “jantar servido”.
- `briefing.md`, `gancho.md` (fórmula 17), `roteiro.md` (110 palavras de tela / 121 faladas), `shotlist.md`.
- `voz_raw.wav` 43,04 s (`length_scale` 1,12) → `voz.wav` 45,00 s; `transcricao.json` por palavra.
- `index.html` com 13 cenas sincronizadas; gancho visível no frame 1; `autoAlpha` por cena.
- `check-contrato.ps1`: **OK, 0 avisos** (29 invariantes).
- `final.mp4`: **45,013 s, 3,6 MB, −15,4 LUFS, pico −1,5 dBFS**, 1080×1920, H.264, 30 fps, AAC 48 kHz estéreo.
- `qa.md`: QA técnico **PASS**; aprovação humana em 21/10/2026.
- Cópia de publicação: `002-mary-celeste_shorts_v1.mp4`; capa: `capa.png`.
- Título: `Mary Celeste: o navio encontrado sem ninguém em 1872` (52 chars; lint 98/100).
- **Publicado no YouTube Shorts em 21/10/2026:** https://youtube.com/shorts/n6dtveQguf4. Aviso de conteúdo sintético marcado; selo **AI** visível.

### Episódio 003 — Roanoke (publicado, 23/10/2026)
- Tema: colônia inglesa de Roanoke; **CROATOAN** como nome de lugar, não código.
- `briefing.md`, `gancho.md` (fórmula 1), `roteiro.md` com **113 palavras faladas** e 13 cenas; `narracao.txt` canônico.
- `narracao_tts.txt` grafa **`Croatoun`** nas duas ocorrências para o Piper; a tela usa **`CROATOAN`** e `narracao.txt` usa **`Croatoan`**.
- `voz_raw.wav` **44,69 s** (`length_scale` 1,00; `noise_scale` 0,65; `noise_w` 0,80) → `voz.wav` **45,00 s**, 48 kHz estéreo, **−21,99 LUFS**, pico **−7,22 dB**. Cadeia: highpass 75 Hz, de-esser, EQ, compressor, limitador, `adelay=260`, `apad`.
- `transcricao.json` com timestamps por palavra; `index.html` remapeado para 13 cenas em 45,00 s. Gancho sem fade no frame 1; CROATOAN entra em **3,75 s**.
- `drone.wav` de 45 s com fade-in de 1 s e fade-out de 42–45 s (bed do 002).
- `check-contrato.ps1`: **OK, 0 avisos**. QA visual em `qa-final/` (14 frames: frame 1, CROATOAN, twist, fecho, fade), sem overflow.
- **Marca:** o primeiro render ainda saiu com `ARQUIVO NOTURNO`; o `index.html` foi corrigido para `DOSSIÊ 45` e o vídeo foi renderizado de novo. Artefatos antigos preservados como `*_brand-antigo`.
- Render segmentado **5×300 frames**, 1 worker: `final_raw.mp4` **45,000 s**, **−21,9 LUFS**, TP **−7,2 dBFS**.
- `final.mp4`: **45,013 s**, **3.557.345 bytes**, **−15,4 LUFS**, TP **−1,4 dBFS**; `qa.ps1` **PASS**.
- **Aprovado pelo usuário em 23/10/2026** (“Aprovado — publicar”). Cópia de publicação `003-roanoke_shorts_v1.mp4`, idêntica ao `final.mp4` (SHA-256 `D7C9B676…`).
- Capa `capa.png` extraída em **4,0 s** (CROATOAN), 1080×1920; título `Roanoke: a colônia que sumiu e deixou uma palavra` (49 chars; lint 80/100).
- **Publicado em 23/10/2026:** https://youtube.com/shorts/8ptxqKGe4Bk. Visibilidade **Público**; **AI use = Yes**; selo **AI** visível na página pública.
- Metadados públicos via `yt-dlp` sem cookies: `availability=public`, `age_limit=0`, `duration=45`.
- Retenção de 48 h agendada para **25/10/2026**. Registro em `biblioteca/publicados.csv`.

### Episódio 004 — MV Joyita (publicado, 24/10/2026)
- 131 palavras / 13 cenas; `voz_raw` 44,117 s (`length_scale` 0,90) → `voz.wav` 45,000 s, −21,63 LUFS.
- Render segmentado 5×300, 0 retries; normalizado **+6,5 dB**: `final.mp4` **45,013 s, 3.652.954 bytes, −15,16 LUFS, TP −1,42**; `qa.ps1` **PASS**.
- **Publicado:** https://youtube.com/shorts/rlSArCY3bH0 — capa em 4,0 s (“25 PESSOAS / NENHUM SINAL”).
- Retenção 48 h: **1.200 views**, 3 s 90,9%, 10 s 43,4%, fim 17,3%, **% média 45,7%** — o miolo caiu, não o gancho. Detalhe em `episodios/004-mv-joyita/retencao.md`.

### Episódio 005 — Voo 19 (publicado, 27/10/2026)
- 111 palavras / 12 cenas (2,5 pal./s), nenhuma cena acima de 5,00 s; cena 2 sobe a aposta em vez de ser cartão de contexto.
- `voz_raw` 43,839 s (`length_scale` 1,15) → `voz.wav` 45,000 s, −16,17 LUFS; remap por `remapear.py` (107/113 tokens).
- Composição **gerada** por `scripts/gerar-episodio.py` a partir de `roteiro.json` — primeiro episódio sem HTML escrito à mão.
- Render segmentado 5×300, 0 retries, 3m11s; `final.mp4` **45,013 s, 3.344.787 bytes, −15,16 LUFS, TP −2,18** (ganho +1,05 dB); `qa.ps1` **PASS**.
- Texto medido no frame: pior linha **772 px de 840**; capa `capa.png` em 38,6 s (“27 HOMENS / NENHUM CORPO”).
- Aprovado em 26/10/2026 (“Aprovado, mas só depois do LAB 001”); **publicado em
  27/10/2026**: https://youtube.com/shorts/wlPEoYErlZQ (`wlPEoYErlZQ`).
  216 views e 5 likes no snapshot do dia 27; `duration=45` e `age_limit=0`
  conferidos por `yt-dlp` sem cookies. **48 h vencem em 29/10.**

### Episódio 006 — Passo Dyatlov (publicado, 27/10/2026)
- 114 palavras / **14 cenas** (2,5 pal./s), máx **4,17 s**. A cena 2 sobe a
  aposta (barraca cortada por dentro, botas no lugar); data e lugar entram
  colados a “nove esquiadores experientes”.
- **Voz por cena** (`scripts/montar-voz.py`, `length_scale` 1,10): 40,814 s de
  fala + 4,186 s de silêncio → `voz_raw.wav` **45,000 s**; `voz.wav` −22,15 LUFS,
  TP −8,12. Motivo: o ASR errou 28% dos tokens e o remap derrapou 1,4 s.
- 14 cenas porque no take único o veredito ficava **6,44 s** no ar; virou dois
  cartões (1959 · força natural / 2020 · avalanche).
- `medir-texto.ps1` corrigiu **6 cenas** antes do render; com 152 px a cena 4
  quebrava “UM DEGRAU” em duas linhas. Pior tinta final: **806 px de 840**.
- Render segmentado 5×300, 0 retries, 3m09,9s; `final.mp4` **45,013 s,
  3.859.117 bytes, −15,19 LUFS, TP −1,30** (ganho **+7,0 dB**); `qa.ps1`
  **PASS**; SHA-256 `B2AA85F3…0033A6`.
- Capa em 32,6 s (“DOIS TÓRAX AFUNDADOS. / UM CRÂNIO RACHADO. / SEM FERIDA NA
  PELE.”); título `Passo Dyatlov: a avalanche chegou 9 horas depois` (48 chars,
  lint 98/100). Pacote em `episodios/006-passo-dyatlov/publicacao.md`.
- **Publicado em 27/10/2026**: https://youtube.com/shorts/K_sgJjNHg84
  (`K_sgJjNHg84`), upload do usuário. `duration=45`, `age_limit=0`, canal
  `Dossiê 45` conferidos por `yt-dlp` sem cookies. **48 h em 29/10.**

### Template
- `templates/misterio-45/index.html` — composição validada, 13 cenas, áudio `voz`/`drone`, QA por `?t=`.
- `templates/misterio-45/beat-sheet.md` — 13 beats, tempos e orçamento de palavras.
- `templates/misterio-45/README.md` — passo a passo completo, incluindo armadilhas.

### Versionamento (21/10/2026)
- `git init -b main`; commit baseline `782df62` com **59 arquivos de texto/código**; tag anotada `ep-001-publicado`.
- `.gitignore` deixa fora `.venv/` (415 MB), mídia `*.mp4`/`*.wav`/`*.onnx` (123 MB), `qa-frames/`, `qa-final/` e as variantes `*-brand-antigo/`. **Nada foi apagado do disco**: evidência continua na pasta.
- `core.autocrlf false` (local) para evitar churn de CRLF.
- Identidade provisória `valentim <valentim@localhost>`; sem remote e sem chave SSH, nada foi enviado.
- Fluxo: commit por etapa, tag por episódio publicado.

## 3. O que falta (em ordem)

### 3.1 Medir os publicados 001 e 002 (48 h) — concluído (23/10/2026)
> Checklist do gate e fila provisória 003–006: `docs/PLANO.md` §Execução imediata.

1. Publicados em 21/10/2026 no YouTube Shorts; TikTok/Reels ficam como reaproveitamento opcional.
2. **002:** 234 views, 103 engaged, 1,2 h, 0:40, 48,3% ficaram, 87,0% de retenção média; **3 s = 91,6%** e **10 s = 61,8%**. CSV salvo em `episodios/002-mary-celeste/retencao.csv`.
3. **001:** 31 views, 9 engaged, 0,0 h, 0:15, 24,3% ficaram, 33,3% de retenção média. O CSV veio vazio; **3 s/10 s não disponíveis**. A tabela de “últimas 48 h” (16 views/11 s/25,3%) é uma janela rolante.
4. **Decisão:** manter o formato v1, ajustar o gancho do 003 e seguir a fila. O 002 passou as metas provisórias de 3 s/10 s; o 001 não.
5. **003:** publicado em 23/10/2026; medido em **25/10/2026**: **370 views**, 3 s **92,7%**, 10 s **68,5%**, fim **36,1%**; +1 inscrito; painel: ficaram **52,6%**, duração média **0:40**, **% média 87,0%**. Fecha o Gate 1 e melhora as duas janelas em relação ao 002, mas o fim cai (42,2% → 36,1%).
6. **004:** publicado em 24/10/2026; medido em **24 h** (25/10): **1.141 views** em 48 h (1.066 em 24 h), 21 likes, 3 s **90,9%** (PASS), 10 s **43,4%** (**abaixo** da meta de 45%), fim **17,3%**; painel: ficaram **53,4%**, duração média **0:21**, **% média 45,7%**. Quedas concentradas em 4,0–8,6 s, dentro do cartão estático de 6,57 s da cena 2 (3,03–9,60 s). Ressalva registrada: alcance 3× maior esfria a audiência (primeira amostra 123,3% contra 162,0% do 003), então a curva não isola só a composição. `retencao-24h.csv` + `retencao.md`; 48 h em 26/10.
7. **Leitura que sobrevive aos dois:** o 004 **não** perdeu mais gente no início (ficaram 53,4% contra 52,6% do 003), mas a **duração média caiu pela metade** (0:40 → 0:21). O problema é o miolo, não o gancho.
8. **Regra derivada (005/006):** nunca um cartão parado de contexto depois do gancho — data/origem/número em ≤2 s ou colados a uma consequência; um dado por cartão; fecho com consequência nova, não resumo.
9. **005 e 006 medidos em 29/10 (48 h).** **005: 224 views, ficaram 46,5%, duração média 0:25 de 0:46 → 54,3%.** **006: 79 views, ficaram 38,2%, 0:23 de 0:46 → 50,0%** (limite: o painel arredonda para o segundo, então 49,1–50,9%). **Gate 2 PASSA com 3 de 6** (002, 003, 005). O 005 — 12 cenas, nenhuma acima de 5 s, gerado do JSON — **dobrou a duração média do 004 com menos views**, o que confirma que o miolo caía por **estado parado**, não por excesso de texto. O 006, com 14 cenas, ficou no limite e **perdeu no gancho** (38,2% contra 46,5%): o próximo ajuste é o **primeiro segundo**, não o miolo. Evidência: `episodios/005-voo-19/retencao.md` (+ PNG) e `episodios/006-passo-dyatlov/retencao.md`.

### 3.2 Validação de nicho — concluída (21/10/2026)
- Coleta completa: 48 shorts de Mistério/Arquivo (14 canais) e 50 de Psicologia sombria (17 canais), canais de 100–500 mil inscritos.
- **Mistério/Arquivo:** mediana de views/inscrito por canal **0,10**; 3 canais ≥1,0 (Pequeno Contexto 1,50; Penumbroo 1,04; Crimes que Marcaram 1,02); mediana de views por canal 2.075.
- **Psicologia sombria:** mediana de views/inscrito por canal **0,06**; nenhum canal ≥0,5; mediana de views por canal 1.428.
- **Engajamento:** psicologia tem like rate maior (6,95% vs 3,37%), mas demanda relativa menor. O like não compensa a diferença de views/inscrito.
- **Decisão:** Mistério/Arquivo é a âncora da Fase 2. Psicologia fica como fallback, não como teste paralelo.
- Dados completos em `logs/nicho-2026-10-21.json` e `docs/NICHO.md`.

### 3.3 Produzir 6 vídeos
- **6 vídeos de Mistério 45** (4/6 publicados; 003 e 004 publicados; faltam 005–006), no canal rebrandado.
- **003-roanoke**: briefing, gancho aprovado, roteiro (113 palavras, 13 cenas), voz, transcrição, composição v1, render e QA técnico **PASS** prontos. Marca corrigida para `DOSSIÊ 45`. **Publicado em 23/10/2026** em https://youtube.com/shorts/8ptxqKGe4Bk; selo **AI** visível; retenção em 25/10. Gancho: “117 pessoas sumiram. Nenhum corpo. Uma palavra.”
- **004-mv-joyita**: briefing (Comissão de Inquérito NZ, Apia 1956), gancho (“O barco foi achado vazio. E ainda flutuava.”), roteiro **131 palavras / 13 cenas**, voz (`voz_raw` 44,117 s → `voz.wav` 45,000 s, −21,63 LUFS, TP −7,37), transcrição e composição remapeada; contrato **OK, 0 avisos**; cena 6 corrigida para 4 linhas.
- **004 render e QA:** segmentado 5×300, 1 worker, **1350/1350 frames, 0 retries**, 3m16s; `final_raw.mp4` 45,000 s, −21,64 LUFS. Normalizado (+6,5 dB + limitador 0,85): `final.mp4` **45,013 s, 3.652.954 bytes, −15,16 LUFS, TP −1,42 dBFS**; `qa.ps1` **PASS**; capa `capa.png` em 4,0 s.
- **004-mv-joyita publicado em 24/10/2026:** https://youtube.com/shorts/rlSArCY3bH0 — público, `duration=45`, `age_limit=0`; cópia `004-mv-joyita_shorts_v1.mp4` idêntica ao `final.mp4`. Retenção de 48 h em **26/10/2026**.
- **Próximo:** abrir o **006 Passo Dyatlov** já com o gerador — escrever `roteiro.json`, gerar, medir a tinta e só então a voz.
- **004–006**: MV Joyita, Voo 19 e Passo Dyatlov; manter o v1 e validar as fontes antes de cada roteiro.
- Manter o gate para os próximos: aprovação humana explícita e descrição do canal conferida antes de publicar.
- Usar `templates/misterio-45/` e o fluxo de `MEMORIA.md` §6.
- Meta: 5–7 shorts/semana; um render por vez.
- Se a retenção dos 6 ficar abaixo do gate (média <40% ou nenhum >40%), reavaliar: testar Psicologia sombria em canal novo antes de trocar de ferramenta.
- Diagnóstico por vídeo: 3 s ≥ 70% e 10 s ≥ 45% são metas provisórias; o gate de 40% de média continua valendo para a fase.

### 3.4 Ferramentas de análise — concluído (21/10/2026)
- Vendor seletivo de `Jakeschincariol/youtube-agent-skill` (MIT, commit `a2feb21`) em `tools/youtube-agent-skill/`.
- `retention.py` com patch para Shorts: 3 s/10 s, eixo de 45 s corrigido, transcrição SRT/VTT/JSON e normalização de retenção absoluta (>100%) do export avançado.
- `hooks.json` mantido intacto; checklist PT-BR em `docs/GANCHOS-21.md`.
- `title.py` adaptado para PT-BR (stopwords, termos vagos, nome próprio).
- `scripts/test_youtube_agent.py`: 10 testes passando (inclui retenção absoluta normalizada).
- `yt-viral` e `yt-audit` adiados para depois dos 6 vídeos; decisão em `docs/PLANO.md` e `docs/DECISOES.md`.

### 3.5 Desbloqueado pelo primeiro vídeo (21/10/2026)
- `codebase-memory-mcp` pode ser instalado e o projeto indexado, **fora de uma janela de render** (RAM de 8 GB).
- OpenMontage continua fora até o gate 3 (ver `docs/PLANO.md`).

### 3.6 Lote 007–011 — aprovado em 29/10/2026 (nada produzido)

- **Canal único** (decisão de 29/10): Dossiê 45. `sombra-direta` (001 com QA PASS,
  nunca publicado) e `mente-obscura` ficam **pausados**, arquivo em disco.
- **O lote testa uma variável: o gancho** — primeiro segundo com ação/consequência,
  nunca contexto. Fixo: 45 s, **12 cartões**, ≤5 s, v1, Piper, 1080×1920/30 fps.
- **Hipótese:** mediana de “ficaram para assistir” ≥ **46,5%** (005) e de
  `% média` > **54,3%** (005). Se só uma passar → próxima variável é ritmo/visual
  (LAB 002); se nenhuma → reavaliar formato.
- **Cadência fixa:** 1/dia, 19h de Brasília, seg–sex. Horário é **constante**, não
  variável: com 5 vídeos não se isola horário de dia da semana e de gancho.
- **Temas aprovados:** 007 Somerton (1948) · 008 Max Headroom (1987) · 009 Máscaras
  de chumbo (1966, nacional) · 010 Carroll A. Deering (1921) · 011 SS Baychimo
  (1931–1969). Reservas: Hinterkaifeck, Mulher de Isdal, Yuba County Five, Voynich.
- **Custo:** ~10 h (≈6 h de briefing/fonte) + 5 renders de ~3 min, um por vez.
  Plano completo, fontes e cuidados: `docs/PLANO.md` §“Fase 3 — lote 007–011”.
- **Aprovar temas ≠ aprovar publicar:** aprovação continua por vídeo, explícita.

### 3.7 Melhorias visuais v2 — backlog (não iniciar)
- Registro em `docs/PLANO.md` §Melhorias visuais — backlog pós-validação.
- Só depois dos 6 vídeos e do Gate 2; **003–006 ficam no v1** para não contaminar a comparação.
- ReelMimic, WebGL/Three.js e afins ficam fora do MVP; reavaliar depois do gate 3.

## 4. Ambiente e restrições

| Item | Valor |
|---|---|
| Máquina | Dell Inspiron 5468, i5-7200U 2C/4T, 8 GB RAM, Intel HD 620, Windows 10 22H2 |
| Disco | C: ~67 GB livres; D:/E: HDD USB |
| Binários | `C:\Users\valentim\Tools` (Node, FFmpeg, Git) |
| Python | `.venv` do projeto (Piper, faster-whisper, yt-dlp) |
| Render | HyperFrames + Chrome headless; **um por vez** |
| Regra | Sem WebGL/Three.js, sem Docker/WSL, sem Remotion/Hermes3D |

## 5. Mapa de arquivos

| Caminho | O que é |
|---|---|
| `MEMORIA.md` | este arquivo; estado e retomada |
| `ESTADO.md` | estado por passo; carregado como `instructions` (sobrevive à compactação) |
| `AGENTS.md` | regras invioláveis e fluxo |
| `README.md` | visão do produto e stack |
| `docs/PLANO.md` | fases, gates, capacidade, métricas |
| `docs/HISTORICO.md` | linha do tempo do que foi entregue |
| `docs/ARQUITETURA.md` | contratos do código (cenas, áudio, render, QA) |
| `docs/STACK.md` | instalação, versões, correções de ambiente |
| `docs/DECISOES.md` | decisões e descartes |
| `docs/NICHO.md` | hipóteses de nicho e critérios |
| `docs/REBRANDING.md` | textos e ordem de execução do rebranding no YouTube Studio |
| `docs/GANCHOS-21.md` | checklist PT-BR das 21 fórmulas de gancho |
| `docs/QA.md` | checklist editorial e técnico |
| `.opencode/skills/` | instruções por etapa |
| `templates/misterio-45/` | template validado |
| `episodios/<slug>/` | um diretório por vídeo, com status e QA |
| `scripts/` | instalação, voz, transcrição, QA, benchmark, testes |
| `tools/youtube-agent-skill/` | vendor MIT: retenção, hooks e lint de título |
| `biblioteca/publicados.csv` | registro de publicação e métricas |
| `canais/` | método de expansão: `README.md`, `registro.csv`, `_template/`, `dossie45/` |
| `docs/ESCALA.md` | por que o gargalo é vazão, não ideia |

## 6. Comandos canônicos

```powershell
# ambiente novo
$env:Path = "C:\Users\valentim\Tools\node;C:\Users\valentim\Tools\ffmpeg\bin;" + $env:Path

# verificar instalação
.\scripts\verify.ps1

# criar episódio novo (carimba o template usado)
.\scripts\novo-episodio.ps1 002-slug "Título do episódio"

# contrato antes do QA visual e do render
.\scripts\check-contrato.ps1 episodios\<slug>\index.html

# voz (sempre pelo wrapper, nunca piper.exe)
.\.venv\Scripts\python.exe scripts\tts.py `
  --model models\vozes\pt_BR-faber-medium.onnx `
  --input episodios\<slug>\narracao.txt `
  --output episodios\<slug>\voz_raw.wav --length-scale 1.28

# transcrição com timestamps
.\.venv\Scripts\python.exe scripts\transcribe.py `
  episodios\<slug>\voz.wav --model small --language pt `
  --output episodios\<slug>\transcricao.json

# retenção do Studio (48 h)
.\.venv\Scripts\python.exe tools\youtube-agent-skill\yt-retention\retention.py `
  episodios\<slug>\retencao.csv --duration 45 `
  --transcript episodios\<slug>\transcricao.json

# lint de título + thumbnail
.\.venv\Scripts\python.exe tools\youtube-agent-skill\yt-package\title.py `
  --title "<título>" --thumb "<texto da capa>"

# testes das ferramentas de análise
.\.venv\Scripts\python.exe scripts\test_youtube_agent.py

# QA visual de uma cena, sem render
$chrome = (Get-ChildItem "$env:USERPROFILE\.cache\hyperframes\chrome\chrome-headless-shell" -Recurse -Filter chrome-headless-shell.exe | Select-Object -First 1).FullName
$uri = [System.Uri]::new((Resolve-Path index.html)).AbsoluteUri
& $chrome --disable-gpu --hide-scrollbars --window-size=1080,1920 `
  --virtual-time-budget=1500 --screenshot=qa-frames\t12.5.png "$uri`?t=12.5"

# render segmentado (evita Target closed)
$env:HF_SEGMENTED_CAPTURE = "true"
$env:HF_SEGMENT_FRAMES = "300"
$env:HF_SEGMENT_BROWSER_RECYCLE = "1"
hyperframes.cmd render --output final_raw.mp4 --quality standard --fps 30 `
  --workers 1 --low-memory-mode --protocol-timeout 600000 --resume

# normalizar áudio (medir antes; o piloto usou +6,2 dB)
ffmpeg -i final_raw.mp4 -c:v copy `
  -af "volume=6.2dB,alimiter=limit=0.85:level=disabled" `
  -c:a aac -b:a 192k -movflags +faststart final.mp4

# QA automático
.\scripts\qa.ps1 episodios\<slug>\final.mp4
```

## 7. Armadilhas conhecidas

| Sintoma | Causa | Solução |
|---|---|---|
| `piper.exe` falha com caminho acentuado | espeak-ng não lê `Padrão` | usar `scripts/tts.py` |
| Shims `.ps1` bloqueados | execution policy | chamar `.cmd` ou `-ExecutionPolicy Bypass` |
| Render mudo | `<audio>` sem `id` | manter `id="voz"` e `id="drone"` |
| Texto fantasma de outra cena | GSAP só anima entrada | `autoAlpha` por cena (já no template) |
| Texto duplicado em `qa-frames` | screenshot do Chrome headless com escala fracionária | conferir a mesma cena em `?t=` no navegador; validar no render antes de mexer na composição |
| TTS erra a pronúncia de CROATOAN | grafia inglesa no Piper | usar `Croatoun` só em `narracao_tts.txt`; manter `CROATOAN` na tela |
| Marca antiga `ARQUIVO NOTURNO` em composição clonada | template do 001 é anterior ao rebranding | conferir `class="mark"` e usar `DOSSIÊ 45` no 002–006 |
| Chrome fecha em ~1300/1350 frames | memória acumulada | captura segmentada + 1 worker |
| Linha quebra diferente no render | fonte na fronteira dos ~840 px | reduzir 4–8 px ou quebrar antes |
| Áudio em −22 LUFS | TTS baixo + drone discreto | ganho estático + limitador no pós |
| `qa.ps1` “falha” no ffmpeg | stderr vira erro no PowerShell | o script já contorna; rodar com Bypass |
| faster-whisper quebra no `av` 19 | `metadata_errors` removido | patch em `faster_whisper/audio.py` |
| Retenção de 45 s lida como 100% no fim | eixo em segundos (máx. 45) confundido com percentual | usar o `retention.py` patchado; `--axis seconds` se preciso |
| Score de gancho estranho em PT-BR | `hookscore.py` é calibrado em inglês | não usar; consultar `docs/GANCHOS-21.md` |
| Studio Análises em branco / “Oops, something went wrong” | o módulo de gráficos falha na primeira carga do navegador controlado | abrir `.../video/<id>/analytics/tab-overview/period-default?hl=en&cb=<timestamp>` e **recarregar até 3×** até o card “Audience retention” renderizar; se insistir, exportar o CSV no Chrome do usuário |
| Aba **Content** do Analytics e a lista de vídeos do Studio nunca carregam | o widget de tabela falha em todas as tentativas (6× testado em 26/10) | não insistir: **puxar vídeo a vídeo** por `.../video/<id>/analytics/tab-overview/period-default?hl=en&cb=<ts>` (funciona em 1–2 tentativas). IDs em `docs/HISTORICO.md`; 001 `WKuNVjl3d5M`, 002 `n6dtveQguf4`, 003 `8ptxqKGe4Bk`, 004 `rlSArCY3bH0` |
| Página de analytics abre **vazia** (só “Video analytics” e um esqueleto) | módulo de gráficos falha na 1ª carga | recarregar (`location.reload()`) **esperando `load` antes de procurar texto** — no 29/10 funcionou na 1ª tentativa nas duas páginas. “Advanced mode” também carrega e serve de plano B |
| **3 s / 10 s / fim da curva não saem em texto** | os pontos só aparecem no *hover* real; `MouseEvent`/`PointerEvent` sintéticos não acionam o `yta-audience-retention-highlight-hovercard` (fica `display:none`) | registrar só o que o painel entrega em texto: views, “Stayed to watch”, duração média. `retencao_3s`/`retencao_10s` ficam **vazios** — nunca estimar |
| Aba Reach/Audience não abre por URL | `tab-reach` e `tab-audience` são redirecionados para `tab-overview` | abrir o overview, achar os `TP-YT-PAPER-TAB` no DOM e chamar `.click()` em “Reach” / “Audience” |
| `% média assistida` cai sozinha com o tempo | duração média é média global: views novas vêm de feed mais frio e assistem menos | **medir sempre em 48 h**. 002 caiu de 87,0% (25/10) para 76,1% (26/10); 003 de 87,0% para 84,8% |
| Descoberta automática de canal não funciona | **yt-dlp não respeita os filtros de busca do YouTube** (testado em 26/10 com 2026.08.19): `sp=EgIYAQ%3D%3D` (Shorts) e `sp=…,CAI%3D` (ordenar por data) são ignorados; `ytsearchdate` **não existe** nesta versão; `/hashtag/<tag>` devolve público global (`truecrime` → 135 canais quase todos em inglês) | inverter o fluxo: **humano descobre, máquina mede**. Canais em `biblioteca/canais-semente.txt`, medidos por `scripts/scout.py` |
| Aba `/shorts` não entrega `duration`, `playlist_count` nem data | limitação do modo flat | filtrar duração só quando existir; **posição na lista = recência** (a aba vem do mais novo para o mais antigo); views vêm arredondadas, então usar só razões |
| Retenção média “não derivável” | o painel não mostra o número no CSV | `% média assistida = duração média ÷ 46 s` (002: 0:40 → 87,0%; 004: 0:21 → 45,7%) |
| ASR erra e o `remapear.py` mostra o texto certo com **tempo errado** | o alinhamento depende da transcrição: palavra errada = fronteira errada (006: “cortam um degrau” → “Cota o mundo legal”, 28% dos tokens, cena 4 **1,4 s** fora; testado com `medium`, erra igual) | sintetizar **cena por cena** com `scripts/montar-voz.py`: o tempo vira soma de blocos. Se usar take único, conferir a taxa de alinhamento antes de confiar na tabela |
| `medir-texto.ps1` mostra mais linhas que o roteiro (ex.: `5/4` na cena 1) | o kicker entra como bloco de tinta, como qualquer outra linha | conferir no frame: 4 linhas de título + kicker; não é quebra |
| Frame do `final.mp4` parece ter texto duplicado | a imagem foi **exibida em escala reduzida**; serifa fina ganha fantasma | medir bandas de tinta (`ffmpeg → gray → max por linha`). No 006 a checagem deu exatamente 3 linhas + linha pequena |

## 8. Decisões que não se reabrem

- HyperFrames (Apache 2.0), Piper, faster-whisper, yt-dlp, FFmpeg.
- Vídeo **tipográfico** (texto é a imagem); sem WebGL, Three.js, shaders.
- PT-BR até o gate de expansão.
- Nada de reupload de terceiros; `yt-dlp` só metadados.
- Um render por vez; 1080×1920, 30 fps, H.264 + AAC.
- Fato precisa de fonte; lenda marcada como lenda.
- `codebase-memory-mcp` e OpenMontage só depois do primeiro vídeo publicado.
- PI-Desktop fica fora do MVP; reavaliar só depois do primeiro vídeo (ver `docs/DECISOES.md`).
- Hypit é referência conceitual, não dependência do MVP; não empacotar no kit sem licença comercial.
- Um canal = um nicho; não misturar Mistério/Arquivo com Psicologia sombria.
- Mistério/Arquivo é a âncora da Fase 2; o Cod Mind Million foi rebrandado para **Dossiê 45** (handle `@Dossie45`, avatar/banner no ar). Nome público, descrição de `identidade/descricao-canal.txt` e deslistagem dos 9 shorts antigos concluídos. Psicologia fica como fallback em canal novo, não no mesmo canal.
- `youtube-agent-skill` é adotado **seletivamente** (retenção, hooks como checklist, lint de título). `yt-viral` e `yt-audit` ficam para depois dos 6 vídeos; `hookscore.py` não é usado em PT-BR.
- **Um canal = um modelo = uma variável** (`canais/README.md`). Canal novo muda **uma** das cinco dimensões (nicho, formato, voz, cadência, visual) e mantém as outras quatro; hipótese e critério de morte escritos na `ficha.md` **antes do vídeo 1**; **N = 8** vídeos antes de decidir escalar/ajustar/matar (~16 h por canal); máx. **2 canais ativos** (1 produzindo, 1 medindo). A série de 6 do Dossiê 45 **não** é campo de teste — o v2 vira canal novo.
- Cada canal mede na **mesma janela fixa de 48 h** e registra em `canais/<slug>/metricas.csv`; o Dossiê 45 mantém também `biblioteca/publicados.csv`.

## 9. Protocolo de memória

Ao fim de **cada etapa**:

0. (A cada passo, não só etapa) Atualizar `ESTADO.md`: feito, pendente, bloqueio, próximo comando.
1. Atualizar a tabela da §1 e as listas das §2/§3 deste arquivo.
2. Acrescentar uma entrada datada em `docs/HISTORICO.md` (o que, evidência, decisão).
3. Atualizar `episodios/<slug>/status.md` e `qa.md` quando for um episódio.
4. Se mudar um contrato de código, atualizar `docs/ARQUITETURA.md`.
5. Nunca apagar evidência (áudio, frames de QA, `final_raw.mp4`).

> Regra de ouro: se uma sessão nova não conseguir retomar lendo `MEMORIA.md` + `AGENTS.md` + `docs/PLANO.md`, esta memória está incompleta.

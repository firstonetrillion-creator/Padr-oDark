# scripts — o que cada um entrega

> Scripts de infraestrutura e produção. Rodar a partir da raiz do projeto, salvo indicação.
> PowerShell 5.1 no Windows 10; Python no `.venv`.

## Mapa rápido

| Script | Quando usar | Entrada | Saída |
|---|---|---|---|
| `install-brain.ps1` | máquina nova / reinstalação | rede | binários em `C:\Users\valentim\Tools` |
| `verify.ps1` | antes de produzir | — | versões no terminal |
| `bench.ps1` | validar a máquina (G0) | `bench/index.html` | `bench/bench-45.mp4`, `logs/bench.json` |
| `tts.py` | gerar narração | `narracao.txt` | `voz_raw.wav` |
| `transcribe.py` | obter tempos das cenas | `voz.wav` | `transcricao.json` |
| `qa.ps1` | antes de publicar | `final.mp4` | `QA PASS`/`QA FAIL` |
| `nicho.py` | validar nicho | buscas + canais | `logs/nicho-<data>.json`, seção em `docs/NICHO.md` |

## install-brain.ps1

Instala o “cérebro” em espaço de usuário, sem admin:

- Node, Git, FFmpeg, uv, Python, Piper, faster-whisper, yt-dlp, HyperFrames.
- Copia DLLs do VC++ para o `onnxruntime` do `.venv`.
- Copia `espeak-ng-data` para um caminho ASCII.
- Aplica o patch do PyAV no faster-whisper quando necessário.

```powershell
.\scripts\install-brain.ps1
```

Se o Windows bloquear `.ps1`, rodar:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\install-brain.ps1
```

## verify.ps1

Imprime versões de Node, npm, Git, FFmpeg, uv, Python, Piper (via `tts.py --help`), yt-dlp, HyperFrames; confere `espeak-ng-data`, a voz `pt_BR-faber-medium.onnx` e o espaço livre em C:.

```powershell
.\scripts\verify.ps1
```

Não altera nada. É o primeiro comando de uma sessão nova.

## bench.ps1

Renderiza `bench/index.html` (45 s, 1080×1920) e grava `logs/bench.json` com segundos, tamanho e gate (`PASS` se < 720 s).

```powershell
.\scripts\bench.ps1
```

- Usa `--quality draft` para medir rápido.
- Serve para detectar regressão de performance ou memória.
- Não rodar junto com outro render.

## tts.py

Wrapper do Piper para caminhos com acento. O `piper.exe` falha porque o espeak-ng abre dados com `fopen` ANSI e não lê “Padrão”; o wrapper aponta para `C:\Users\valentim\Tools\piper-data\espeak-ng-data`.

```powershell
.\.venv\Scripts\python.exe scripts\tts.py `
  --model models\vozes\pt_BR-faber-medium.onnx `
  --input episodios\<slug>\narracao.txt `
  --output episodios\<slug>\voz_raw.wav `
  --length-scale 1.28
```

- `--length-scale` maior = fala mais lenta (1.28 no piloto).
- Saída crua; o processamento para 45,00 s é feito depois (ver skill `voz`).
- **Nunca** chamar `piper.exe` direto em caminho acentuado.

## transcribe.py

Transcreve um WAV/MP4 com faster-whisper e grava JSON com `segments` e `words` (timestamps por palavra).

```powershell
.\.venv\Scripts\python.exe scripts\transcribe.py `
  episodios\<slug>\voz.wav --model small --language pt `
  --output episodios\<slug>\transcricao.json
```

- `small` + `int8` + CPU é o equilíbrio desta máquina (~30 s para 45 s de áudio).
- `vad_filter=True` remove silêncio.
- O texto serve para **tempos**, não para legendas: nomes próprios saem errados.
- O JSON é a fonte dos `data-start`/`data-duration` das cenas.

## qa.ps1

QA técnico automático do arquivo final:

```powershell
.\scripts\qa.ps1 episodios\<slug>\final.mp4
```

Confere:

- duração 44–46 s;
- 1080×1920, H.264;
- 30/1 fps;
- AAC 48 kHz estéreo;
- loudness entre −17 e −13 LUFS;
- trechos pretos inesperados (limiar 2%, ignora o fade final).

Detalhes de implementação:

- Roda o FFmpeg com `$ErrorActionPreference = "Continue"` porque o `loudnorm`/`blackdetect` escrevem no stderr e o PowerShell trata isso como erro nativo.
- `pix_th=0.02` evita que o fundo escuro do canal (`#0A0A0B`) seja classificado como “preto”.
- O fade final (`44,3–45 s`) é intencional e ignorado.
- Sai com código 0 (`PASS`) ou 1 (`FAIL`), próprio para gate de publicação.

## nicho.py

Coleta metadados públicos de Shorts para comparar nichos. **Não baixa vídeo**: usa `yt-dlp` apenas para listar canais/Shorts e ler metadados.

```powershell
.\.venv\Scripts\python.exe scripts\nicho.py
```

- Descobre canais por buscas PT-BR e visita a aba `/shorts` de cada um.
- Filtra canais de **100 a 500 mil inscritos** (configurável) para medir demanda de canais pequenos, onde views/inscrito é mais informativo.
- Lê views, inscritos, likes, comentários, duração e data; calcula views/inscrito, taxa de like e taxa de comentário.
- Metadados **não** dão retenção real. Views/inscrito, like e comentário são proxies; retenção real só vem do YouTube Studio do nosso vídeo.
- Saída: `logs/nicho-<data>.json` (completo) e seção em `docs/NICHO.md` (top canais e shorts).
- Cache em `logs/nicho-cache/`; `--refresh` ignora o cache.
- `--limit 3` para teste rápido; `--help` lista todas as opções.
- Usa `--extractor-args "youtube:player_client=android"` para evitar o bloqueio “Sign in to confirm you're not a bot” na leitura de metadados de vídeo.
- Não usa cookies. Se o YouTube bloquear, rodar em outro horário ou de outra rede.
- Sequencial e leve: não roda junto com render.

## Convenções

- Áudio e vídeo sempre em `episodios/<slug>/`.
- Evidência não se apaga: `voz_raw.wav`, `final_raw.mp4`, `qa-frames/`.
- Um render por vez.
- Se um script mudar de contrato, atualizar `docs/ARQUITETURA.md` e `MEMORIA.md`.

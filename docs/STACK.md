# Stack e instalação

## Camadas

| Camada | Componente | Onde fica |
|---|---|---|
| Base | Node 22.23.3 | `C:\Users\valentim\Tools\node` |
| Base | Git 2.56 (portable) | `C:\Users\valentim\Tools\git` |
| Base | FFmpeg 8.1 (BtbN, GPL) | `C:\Users\valentim\Tools\ffmpeg` |
| Base | uv + Python 3.12 | `%USERPROFILE%\.local\bin` + `.venv` |
| Voz/legenda | piper-tts, faster-whisper | `.venv` |
| Pesquisa | yt-dlp | `.venv` |
| Render | hyperframes (npm global) | `%APPDATA%\npm` |
| Voz PT-BR | faber medium | `models\vozes` |

Tudo em user space — **sem admin, sem UAC**.

## Instalação

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\install-brain.ps1
```

Opções: `-SkipVoice`, `-SkipHyperFrames`, `-SkipPython`, `-SkipGit`, `-SkipFFmpeg`, `-SkipNode`.

Log: `logs\install.log`
Status: `logs\install-status.json`

## Verificação

```powershell
node -v                    # v22.23.3
npm -v                     # 10.9.9
git --version              # 2.56.0
ffmpeg -version            # n8.1.3
uv --version               # 0.13.4
.\.venv\Scripts\python.exe --version   # 3.12.15
.\.venv\Scripts\yt-dlp.exe --version   # 2026.8.19
hyperframes.cmd --version  # 0.8.181
```

Chrome Headless Shell: `%USERPROFILE%\.cache\hyperframes\chrome\chrome-headless-shell\win64-152.0.7977.30`.

## Correções de ambiente (já aplicadas)

| Problema | Causa | Correção |
|---|---|---|
| `onnxruntime` não importava | Windows sem VC++ runtime (`msvcp140.dll`, `msvcp140_1.dll`) | DLLs amd64 do VC++ Redist copiadas para `onnxruntime\capi` e `.venv\Scripts` |
| Piper quebrava no espeak-ng | caminho do projeto tem acento (`Padrão`) e o espeak usa `fopen` ANSI | dados copiados para `C:\Users\valentim\Tools\piper-data\espeak-ng-data`; usar `scripts/tts.py` |
| `hyperframes` não rodava | execution policy bloqueia `.ps1` | usar `hyperframes.cmd` ou `npx --yes hyperframes` |
| Chrome headless ausente | primeira execução | `hyperframes browser ensure` |
| `faster-whisper` quebrava no `av` 19 | `av.open(metadata_errors=...)` removido | patch em `.venv\Lib\site-packages\faster_whisper\audio.py` (remover o argumento) |

## HyperFrames

```powershell
npx hyperframes doctor          # baixa/valida Chrome + FFmpeg
npx hyperframes init piloto
cd piloto
npx hyperframes benchmark ./index.html
npx hyperframes render -o out.mp4
```

Primeira execução baixa o Chromium (~150 MB). Rodar uma vez, com paciência.

## Piper

```powershell
.\.venv\Scripts\piper.exe --model models\vozes\pt_BR-faber-medium.onnx --output_file teste.wav
```

## faster-whisper

Usado via Python; baixa o modelo na primeira execução (~75 MB para `small`).

```powershell
.\.venv\Scripts\python.exe -c "from faster_whisper import WhisperModel; WhisperModel('small', device='cpu', compute_type='int8')"
```

## yt-dlp (pesquisa)

```powershell
.\.venv\Scripts\yt-dlp.exe --dump-json --flat-playlist "ytsearch50: misterio 45 segundos"
```

## Não instalar

| Item | Motivo |
|---|---|
| Docker / WSL | RAM e disco; não é necessário |
| Hermes3D | Não produz vídeo; 1,5–2,5 GB |
| ruflo full | Swarm desnecessário; daemon |
| Remotion | Licença + peso; redundante |
| CBM Lens 3D | WebGL em iGPU; beta |
| Modelos locais de vídeo | Sem GPU |

## Limites da máquina

- 8 GB RAM, 2 núcleos, sem GPU
- Render 720p: 3–8 min por 30 s
- Render 1080p: 10–50 min por 60 s
- Um render por vez; fechar navegador e apps pesados

#requires -Version 5.1
<#
  Padrao-Dark :: install-brain.ps1
  Instala o "cerebro" do estudio sem precisar de admin (tudo em user space).

  Camadas:
    1. Node 22 (portable zip)
    2. Git (PortableGit)
    3. FFmpeg (gyan.dev essentials)
    4. uv + Python 3.12 (user space)
    5. piper-tts, faster-whisper, yt-dlp (venv do projeto)
    6. hyperframes (npm global)
    7. voz PT-BR Piper (faber medium)

  Uso:
    powershell -ExecutionPolicy Bypass -File .\scripts\install-brain.ps1
    powershell -ExecutionPolicy Bypass -File .\scripts\install-brain.ps1 -SkipVoice
#>
[CmdletBinding()]
param(
  [string]$Root = "C:\Users\valentim\Tools",
  [switch]$SkipNode,
  [switch]$SkipGit,
  [switch]$SkipFFmpeg,
  [switch]$SkipPython,
  [switch]$SkipVoice,
  [switch]$SkipHyperFrames
)

$ErrorActionPreference = "Stop"
$ProgressPreference = "SilentlyContinue"
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

$Project = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$Tmp     = Join-Path $env:TEMP "brain-install"
$Log     = Join-Path $Project "logs\install.log"

# Bootstrap do PATH: cobre o caso de rodar com -SkipNode/-SkipGit/-SkipFFmpeg
$env:Path = "$Root\node;$Root\node\node_modules\npm\bin;$Root\git\cmd;$Root\ffmpeg\bin;$env:USERPROFILE\.local\bin;$env:APPDATA\npm;" + $env:Path

New-Item -ItemType Directory -Force -Path $Root, $Tmp, (Split-Path $Log), (Join-Path $Project "models\vozes") | Out-Null

function Log([string]$msg) {
  $line = "[{0:yyyy-MM-dd HH:mm:ss}] {1}" -f (Get-Date), $msg
  Write-Host $line
  Add-Content -Path $Log -Value $line -Encoding UTF8
}

function Add-UserPath([string]$p) {
  $cur = [Environment]::GetEnvironmentVariable("Path", "User")
  if ([string]::IsNullOrWhiteSpace($cur)) { $cur = "" }
  $parts = @($cur -split ';' | Where-Object { $_ -ne "" })
  if ($parts -notcontains $p) {
    $new = (($parts + $p) -join ';')
    [Environment]::SetEnvironmentVariable("Path", $new, "User")
    Log "PATH(user) += $p"
  }
  $now = @($env:Path -split ';')
  if ($now -notcontains $p) { $env:Path = "$env:Path;$p" }
}

function Download([string]$url, [string]$out) {
  if (Test-Path $out) { Log "cache ok: $out"; return }
  Log "download: $url"
  Invoke-WebRequest -Uri $url -OutFile $out -UseBasicParsing
  Log "salvo: $out ($([math]::Round((Get-Item $out).Length / 1MB, 1)) MB)"
}

function Expand-To([string]$zip, [string]$dest, [string]$finalDir) {
  if (Test-Path $dest) { Remove-Item $dest -Recurse -Force }
  Expand-Archive -Path $zip -DestinationPath $dest -Force
  $inner = Get-ChildItem $dest -Directory | Select-Object -First 1
  if (-not $inner) { throw "zip sem pasta interna: $zip" }
  if (Test-Path $finalDir) { Remove-Item $finalDir -Recurse -Force }
  Move-Item $inner.FullName $finalDir
}

# ---------------------------------------------------------------- Node
if (-not $SkipNode) {
  $nodeDir = Join-Path $Root "node"
  if (-not (Test-Path (Join-Path $nodeDir "node.exe"))) {
    $v   = "v22.23.3"
    $zip = Join-Path $Tmp "node-$v-win-x64.zip"
    Download "https://nodejs.org/dist/$v/node-$v-win-x64.zip" $zip
    Log "extraindo Node $v"
    Expand-To $zip (Join-Path $Tmp "node") $nodeDir
  }
  Add-UserPath $nodeDir
  Log ("node: " + (& (Join-Path $nodeDir "node.exe") -v))
}

# ---------------------------------------------------------------- Git
if (-not $SkipGit) {
  $gitDir = Join-Path $Root "git"
  if (-not (Test-Path (Join-Path $gitDir "cmd\git.exe"))) {
    $exe = Join-Path $Tmp "PortableGit-2.56.0.2-64-bit.7z.exe"
    Download "https://github.com/git-for-windows/git/releases/download/v2.56.0.windows.2/PortableGit-2.56.0.2-64-bit.7z.exe" $exe
    if (Test-Path $gitDir) { Remove-Item $gitDir -Recurse -Force }
    Log "extraindo PortableGit"
    Start-Process -FilePath $exe -ArgumentList @("-o$gitDir", "-y") -Wait -NoNewWindow
  }
  Add-UserPath (Join-Path $gitDir "cmd")
  Log ("git: " + (& (Join-Path $gitDir "cmd\git.exe") --version))
}

# ---------------------------------------------------------------- FFmpeg
if (-not $SkipFFmpeg) {
  $ffDir = Join-Path $Root "ffmpeg"
  if (-not (Test-Path (Join-Path $ffDir "bin\ffmpeg.exe"))) {
    $zip = Join-Path $Tmp "ffmpeg-n8.1-win64-gpl.zip"
    Download "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-n8.1-latest-win64-gpl-8.1.zip" $zip
    Log "extraindo FFmpeg"
    Expand-To $zip (Join-Path $Tmp "ffmpeg") $ffDir
  }
  Add-UserPath (Join-Path $ffDir "bin")
  $ffLine = (& (Join-Path $ffDir "bin\ffmpeg.exe") -version 2>&1) | Select-Object -First 1
  Log ("ffmpeg: " + $ffLine)
}

# ---------------------------------------------------------------- uv + Python
$uv = Join-Path $env:USERPROFILE ".local\bin\uv.exe"
if (-not (Test-Path $uv)) {
  Log "instalando uv"
  $uvScript = Join-Path $Tmp "uv-install.ps1"
  Invoke-WebRequest "https://astral.sh/uv/install.ps1" -OutFile $uvScript -UseBasicParsing
  & $uvScript
}
Add-UserPath (Join-Path $env:USERPROFILE ".local\bin")
if (-not (Test-Path $uv)) { throw "uv nao encontrado em $uv" }
Log ("uv: " + (& $uv --version))

if (-not $SkipPython) {
  Log "uv python install 3.12"
  & $uv python install 3.12
  Push-Location $Project
  try {
    if (-not (Test-Path (Join-Path $Project ".venv\Scripts\python.exe"))) {
      Log "criando .venv (3.12)"
      & $uv venv .venv --python 3.12
    }
    Log "instalando pacotes python (piper-tts, faster-whisper, yt-dlp)"
    & $uv pip install --python (Join-Path $Project ".venv\Scripts\python.exe") --upgrade piper-tts faster-whisper yt-dlp
  } finally {
    Pop-Location
  }
  Log ("python: " + (& (Join-Path $Project ".venv\Scripts\python.exe") --version))

  $espeakSrc = Join-Path $Project ".venv\Lib\site-packages\piper\espeak-ng-data"
  $espeakDst = Join-Path $Root "piper-data\espeak-ng-data"
  if ((Test-Path $espeakSrc) -and -not (Test-Path $espeakDst)) {
    New-Item -ItemType Directory -Force -Path (Split-Path $espeakDst) | Out-Null
    Copy-Item $espeakSrc $espeakDst -Recurse -Force
    Log "espeak-ng-data copiado para $espeakDst (caminho ASCII)"
  }
}

# ---------------------------------------------------------------- HyperFrames
if (-not $SkipHyperFrames) {
  $npm = Join-Path $Root "node\npm.cmd"
  $hfDir = Join-Path $Root "node\node_modules\hyperframes"
  if (Test-Path $hfDir) { Remove-Item $hfDir -Recurse -Force -ErrorAction SilentlyContinue }
  Log "npm install -g hyperframes"
  & $npm install -g hyperframes
  Add-UserPath (Join-Path $env:APPDATA "npm")
  & $npm ls -g --depth=0
}

# ---------------------------------------------------------------- voz PT-BR
if (-not $SkipVoice) {
  $base = "https://huggingface.co/rhasspy/piper-voices/resolve/main/pt/pt_BR/faber/medium/pt_BR-faber-medium"
  $onnx = Join-Path $Project "models\vozes\pt_BR-faber-medium.onnx"
  Download "$base.onnx" $onnx
  Download "$base.onnx.json" "$onnx.json"
}

# ---------------------------------------------------------------- status
$status = [ordered]@{
  finished_at  = (Get-Date).ToString("s")
  project      = $Project
  root         = $Root
  node         = (& (Join-Path $Root "node\node.exe") -v 2>&1)
  npm          = (& (Join-Path $Root "node\npm.cmd") -v 2>&1)
  git          = (& (Join-Path $Root "git\cmd\git.exe") --version 2>&1)
  ffmpeg       = ((& (Join-Path $Root "ffmpeg\bin\ffmpeg.exe") -version 2>&1) | Select-Object -First 1)
  uv           = (& $uv --version 2>&1)
  python       = (& (Join-Path $Project ".venv\Scripts\python.exe") --version 2>&1)
  yt_dlp       = (& (Join-Path $Project ".venv\Scripts\yt-dlp.exe") --version 2>&1)
  voice_model  = (Test-Path (Join-Path $Project "models\vozes\pt_BR-faber-medium.onnx"))
  hyperframes  = (& (Join-Path $Root "node\npx.cmd") --yes hyperframes --version 2>&1)
}
$status | ConvertTo-Json -Depth 3 | Tee-Object -FilePath (Join-Path $Project "logs\install-status.json") -Encoding UTF8

Log "CONCLUIDO"

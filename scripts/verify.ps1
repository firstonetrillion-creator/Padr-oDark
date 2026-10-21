#requires -Version 5.1
<#
  Verifica o "cerebro" instalado e imprime um resumo.
#>
$ErrorActionPreference = "Continue"
$Project = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$Root = "C:\Users\valentim\Tools"

function Line($label, $cmd, $args) {
  try {
    $out = & $cmd @args 2>&1 | Select-Object -First 1
    "{0,-14} {1}" -f $label, $out
  } catch {
    "{0,-14} FALHOU: {1}" -f $label, $_.Exception.Message
  }
}

Line "node"      (Join-Path $Root "node\node.exe") @("-v")
Line "npm"       (Join-Path $Root "node\npm.cmd")  @("-v")
Line "git"       (Join-Path $Root "git\cmd\git.exe") @("--version")
Line "ffmpeg"    (Join-Path $Root "ffmpeg\bin\ffmpeg.exe") @("-version")
Line "ffprobe"   (Join-Path $Root "ffmpeg\bin\ffprobe.exe") @("-version")
Line "uv"        (Join-Path $env:USERPROFILE ".local\bin\uv.exe") @("--version")
Line "python"    (Join-Path $Project ".venv\Scripts\python.exe") @("--version")
Line "tts"       (Join-Path $Project ".venv\Scripts\python.exe") @("scripts\tts.py", "--help")
Line "yt-dlp"    (Join-Path $Project ".venv\Scripts\yt-dlp.exe") @("--version")

$espeak = "C:\Users\valentim\Tools\piper-data\espeak-ng-data"
"espeak-data    " + $(if (Test-Path $espeak) { "OK" } else { "AUSENTE" })

$voice = Join-Path $Project "models\vozes\pt_BR-faber-medium.onnx"
"voz            " + $(if (Test-Path $voice) { "OK ($([math]::Round((Get-Item $voice).Length/1MB,1)) MB)" } else { "AUSENTE" })

try {
  Push-Location $Project
  $hf = & (Join-Path $Root "node\npx.cmd") --yes hyperframes --version 2>&1 | Select-Object -First 1
  "hyperframes    $hf"
} finally {
  Pop-Location
}

"disco C        " + [math]::Round((Get-PSDrive C).Free/1GB,1) + " GB livres"

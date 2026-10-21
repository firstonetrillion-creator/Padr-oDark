#requires -Version 5.1
<#
  Benchmark G0: renderiza 45 s em 1080x1920 e mede o tempo.
  Meta: < 12 min (720 s).
#>
$ErrorActionPreference = "Stop"
$Project = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$Root = "C:\Users\valentim\Tools"
$env:Path = "$Root\node;$Root\ffmpeg\bin;" + $env:Path
$hf = Join-Path $Root "node\hyperframes.cmd"

$bench = Join-Path $Project "bench"
$out   = Join-Path $bench "bench-45.mp4"
Set-Location $bench

Write-Host "== doctor =="
& $hf doctor

Write-Host "== render 45s =="
$t0 = Get-Date
& $hf render --output $out --quality draft
$t1 = Get-Date
$sec = [math]::Round(($t1 - $t0).TotalSeconds, 1)

if (Test-Path $out) {
  $size = [math]::Round((Get-Item $out).Length / 1MB, 1)
  Write-Host "OK: $out ($size MB) em $sec s"
  $status = "PASS" ; if ($sec -gt 720) { $status = "FAIL" }
  [ordered]@{
    data = (Get-Date).ToString("s")
    segundos = $sec
    tamanho_mb = $size
    gate = $status
  } | ConvertTo-Json | Set-Content (Join-Path $Project "logs\bench.json") -Encoding UTF8
} else {
  Write-Host "FALHOU: arquivo nao gerado"
  exit 1
}

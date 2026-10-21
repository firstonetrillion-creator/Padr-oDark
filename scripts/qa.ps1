#requires -Version 5.1
<#
  QA automático de um short.
  Uso:
    .\scripts\qa.ps1 episodios\001-faroleiros\preview.mp4
#>
param(
  [Parameter(Mandatory = $true)]
  [string]$File
)

$ErrorActionPreference = "Stop"
$Root    = "C:\Users\valentim\Tools"
$ffprobe = Join-Path $Root "ffmpeg\bin\ffprobe.exe"
$ffmpeg  = Join-Path $Root "ffmpeg\bin\ffmpeg.exe"

if (-not (Test-Path $File)) { throw "arquivo nao encontrado: $File" }
$File = (Resolve-Path $File).Path

$info  = & $ffprobe -v error -show_entries format=duration -show_entries stream=codec_type,codec_name,width,height,r_frame_rate,channels,sample_rate -of json $File | ConvertFrom-Json
$video = $info.streams | Where-Object { $_.codec_type -eq "video" } | Select-Object -First 1
$audio = $info.streams | Where-Object { $_.codec_type -eq "audio" } | Select-Object -First 1
$dur   = [double]$info.format.duration

$fails = 0
function Check($label, $ok, $detail) {
  if ($ok) { Write-Host ("  OK   {0,-18} {1}" -f $label, $detail) -ForegroundColor Green }
  else     { Write-Host ("  FAIL {0,-18} {1}" -f $label, $detail) -ForegroundColor Red; $script:fails++ }
}

Write-Host "== $File"
Write-Host ("duracao: {0:N2}s" -f $dur)
Check "duracao"  ($dur -ge 44.0 -and $dur -le 46.0) ("{0:N2}s (esperado 44-46)" -f $dur)
Check "video"    ($video -and $video.width -eq 1080 -and $video.height -eq 1920) ("{0}x{1} {2}" -f $video.width, $video.height, $video.codec_name)
Check "fps"      ($video -and $video.r_frame_rate -eq "30/1") $video.r_frame_rate
Check "audio"    ($audio -and $audio.sample_rate -eq "48000" -and $audio.channels -eq 2) ("{0} {1}Hz {2}ch" -f $audio.codec_name, $audio.sample_rate, $audio.channels)

$prevEAP = $ErrorActionPreference
$ErrorActionPreference = "Continue"
$ln = & $ffmpeg -hide_banner -i $File -af "loudnorm=I=-15:TP=-1.5:LRA=11:print_format=json" -f null - 2>&1
$ErrorActionPreference = $prevEAP
$inputI = ($ln | Select-String '"input_i"').ToString() -replace '[^0-9\.\-]', ''
if ($inputI) {
  $lufs = [double]$inputI
  Check "loudness" ($lufs -ge -17.0 -and $lufs -le -13.0) ("{0:N1} LUFS (alvo -15)" -f $lufs)
} else {
  Write-Host "  WARN loudness nao medido" -ForegroundColor Yellow
}

$prevEAP = $ErrorActionPreference
$ErrorActionPreference = "Continue"
$black = & $ffmpeg -hide_banner -i $File -vf "blackdetect=d=0.5:pix_th=0.02" -an -f null - 2>&1 | Select-String "black_start"
$ErrorActionPreference = $prevEAP
$unexpected = @()
foreach ($line in $black) {
  if ($line.Line -match 'black_start:([0-9.]+) black_end:([0-9.]+)') {
    $bs = [double]$Matches[1]; $be = [double]$Matches[2]
    if (-not (($bs -le 0.5) -or ($be -ge ($dur - 0.5)))) { $unexpected += ("{0:N1}-{1:N1}s" -f $bs, $be) }
  }
}
Check "preto" ($unexpected.Count -eq 0) $(if ($unexpected.Count) { "inesperado em " + ($unexpected -join ", ") } else { "nenhum (fade final ignorado)" })

Write-Host ""
if ($fails -eq 0) { Write-Host "QA PASS" -ForegroundColor Green; exit 0 }
else { Write-Host "QA FAIL ($fails)" -ForegroundColor Red; exit 1 }

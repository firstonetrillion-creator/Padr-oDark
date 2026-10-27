#requires -Version 5.1
<#
.SYNOPSIS
  Mede a tinta do texto no frame renderizado e diz qual cena estoura os 840 px.

.DESCRIPTION
  Existe porque `getBoundingClientRect` mede a CAIXA do texto, nao a TINTA: tres
  cenas do LAB 001 estavam "ok" na caixa e saiam do quadro no render (s5 chegou a
  x=1004, 44 px fora da coluna). A medicao aqui e feita no PNG do frame:

    hyperframes snapshot -> PNG -> ffmpeg (gray/rawvideo) -> bbox por linha

  Cada frame e capturado em 60% da duracao da cena: depois da animacao de
  entrada (0,55 s) e antes do fade.

  Duas armadilhas conhecidas estao tratadas:
  - `hyperframes snapshot` sai VAZIO na cena 1. Se houver `final.mp4` na pasta,
    a cena 1 e medida dele; sem mp4, fica marcada como nao medida (nunca como
    "ok").
  - Acento de maiuscula (RÁDIO) e um bloco de tinta separado do corpo da letra.
    Por isso a contagem de linhas usa a ALTURA do bloco (>= metade da fonte), e
    nao o numero de blocos.

.PARAMETER Episodio
  Diretorio do episodio (tem index.html; roteiro.json da as fontes e as linhas).

.PARAMETER Aplicar
  Corrige `fonte_px` no roteiro.json das cenas que passam de 810 px e manda
  rodar gerar-episodio.py de novo.

.PARAMETER Limite
  Largura alvo, em px, para o calculo da fonte sugerida. Padrao 805 (margem de
  35 px sob os 840 do template).

.EXAMPLE
  .\scripts\medir-texto.ps1 episodios\005-voo-19

.EXAMPLE
  .\scripts\medir-texto.ps1 laboratorio\001-60s-fawcett -Aplicar
#>
[CmdletBinding()]
param(
  [Parameter(Mandatory = $true, Position = 0)]
  [string]$Episodio,

  [switch]$Aplicar,

  [double]$Limite = 805
)

$ErrorActionPreference = 'Stop'
$env:PYTHONIOENCODING = 'utf-8'
$inv = [Globalization.CultureInfo]::InvariantCulture
$raiz = Split-Path -Parent $PSScriptRoot
$tools = 'C:\Users\valentim\Tools'
$ffmpeg = Join-Path $tools 'ffmpeg\bin\ffmpeg.exe'
if (-not (Test-Path $ffmpeg)) { $ffmpeg = (Get-Command ffmpeg.exe).Source }
$python = Join-Path $raiz '.venv\Scripts\python.exe'

$Episodio = (Resolve-Path $Episodio).Path
$html = Join-Path $Episodio 'index.html'
$roteiroPath = Join-Path $Episodio 'roteiro.json'
if (-not (Test-Path $html)) { throw "sem index.html em $Episodio" }

# ---- 1. cenas: id, inicio, duracao -----------------------------------------
$texto = Get-Content $html -Raw -Encoding UTF8
$cenas = @()
foreach ($m in [regex]::Matches($texto, '<section class="scene (\S+) clip" id="(\S+)"[^>]*data-start="([\d.]+)"[^>]*data-duration="([\d.]+)"')) {
  $cenas += [pscustomobject]@{
    id     = $m.Groups[2].Value
    inicio = [double]::Parse($m.Groups[3].Value, $inv)
    dur    = [double]::Parse($m.Groups[4].Value, $inv)
  }
}
if ($cenas.Count -eq 0) { throw "nenhuma cena encontrada em $html" }

$roteiro = $null
if (Test-Path $roteiroPath) {
  $roteiro = Get-Content $roteiroPath -Raw -Encoding UTF8 | ConvertFrom-Json
}
$info = @{}
foreach ($c in $cenas) {
  $px = 0; $esperadas = 0
  if ($roteiro) {
    foreach ($r in $roteiro.cenas) {
      if ($r.id -eq $c.id) {
        if ($r.fonte_px) { $px = [int]$r.fonte_px }
        $esperadas = @($r.titulo).Count
      }
    }
  }
  # sem roteiro.json (laboratorio, template antigo): ler do proprio CSS/HTML
  if ($px -eq 0) {
    $mCss = [regex]::Match($texto, "\.$([regex]::Escape($c.id))\s+h1\s*\{\s*font-size:\s*(\d+)px")
    if ($mCss.Success) { $px = [int]$mCss.Groups[1].Value }
  }
  if ($esperadas -eq 0) {
    $mSec = [regex]::Match($texto, "(?s)id=`"$([regex]::Escape($c.id))`".*?<h1>(.*?)</h1>")
    if ($mSec.Success) {
      $esperadas = ([regex]::Matches($mSec.Groups[1].Value, '<br\s*/?>')).Count + 1
    }
  }
  $info[$c.id] = [pscustomobject]@{ px = $px; esperadas = $esperadas }
}

# 60% da cena: texto ja entrou, ainda nao saiu
$tempos = $cenas | ForEach-Object { [math]::Round($_.inicio + [math]::Max(0.7, $_.dur * 0.6), 2) }
$lista = ($tempos | ForEach-Object { $_.ToString($inv) }) -join ','

# ---- 2. snapshot (cena 1 sai vazia: fallback no mp4) -----------------------
# comandos nativos escrevem progresso no stderr: com ErrorActionPreference=Stop
# o PowerShell trata isso como erro e aborta. Volta para Continue aqui.
$ErrorActionPreference = 'Continue'
$saida = Join-Path $Episodio 'qa-medida'
if (Test-Path $saida) { Remove-Item $saida -Recurse -Force }
Push-Location $Episodio
try {
  Write-Host ("snapshot: {0} cenas ({1})" -f $cenas.Count, (Split-Path -Leaf $Episodio))
  & hyperframes.cmd snapshot --at $lista --no-end -o 'qa-medida' 2>&1 |
    Select-Object -Last 2 | ForEach-Object { Write-Host "  $_" }
} finally {
  Pop-Location
}

$pngs = @(Get-ChildItem (Join-Path $saida 'frame-*.png') | Sort-Object Name)
if ($pngs.Count -ne $cenas.Count) {
  throw "esperava $($cenas.Count) frames, achei $($pngs.Count)"
}

# ---- 3. tinta por linha ----------------------------------------------------
$rawDir = Join-Path $saida 'raw'
New-Item -ItemType Directory -Force -Path $rawDir | Out-Null
for ($i = 0; $i -lt $pngs.Count; $i++) {
  & $ffmpeg -y -hide_banner -loglevel error -i $pngs[$i].FullName -pix_fmt gray -f rawvideo (Join-Path $rawDir ("{0:d2}-{1}.raw" -f $i, $cenas[$i].id))
}

# cena 1: o snapshot nao a mostra; medir no mp4 se existir
$mp4 = $null
foreach ($nome in @('final.mp4', 'final_raw.mp4')) {
  $cand = Join-Path $Episodio $nome
  if (Test-Path $cand) { $mp4 = $cand; break }
}
$cena1NoMp4 = $false
if ($mp4) {
  $t1 = $tempos[0]
  & $ffmpeg -y -hide_banner -loglevel error -ss $t1 -i $mp4 -frames:v 1 -pix_fmt gray -f rawvideo (Join-Path $rawDir ("00-{0}-mp4.raw" -f $cenas[0].id))
  if (Test-Path (Join-Path $rawDir ("00-{0}-mp4.raw" -f $cenas[0].id))) { $cena1NoMp4 = $true }
}

$script = @'
import glob, json, os, sys
W, H = 1080, 1920
TOPO, BASE = 145, 1560          # ignora marca (topo) e rodape/trilho
LIMIAR, MIN_PIX = 70, 4
saida = {}
for raw in sorted(glob.glob(sys.argv[1] + '/*.raw')):
    b = open(raw, 'rb').read()
    if len(b) != W * H:
        continue
    blocos, dentro, ini = [], False, 0
    for y in range(H):
        linha = b[y * W:(y + 1) * W]
        n = sum(1 for v in linha if v > LIMIAR)
        if n >= MIN_PIX and not dentro:
            ini, dentro = y, True
        elif n < MIN_PIX and dentro:
            blocos.append((ini, y - 1)); dentro = False
    if dentro:
        blocos.append((ini, H - 1))
    detalhe, pior, px0, px1 = [], 0, 0, 0
    for (y0, y1) in blocos:
        if y1 < TOPO or y0 > BASE or (y1 - y0) < 4:
            continue
        cols = [0] * W
        for y in range(y0, y1 + 1):
            linha = b[y * W:(y + 1) * W]
            for x, v in enumerate(linha):
                if v > LIMIAR:
                    cols[x] += 1
        xs = [x for x in range(W) if cols[x]]
        if not xs:
            continue
        larg = xs[-1] - xs[0] + 1
        detalhe.append({'altura': y1 - y0 + 1, 'largura': larg,
                        'x0': xs[0], 'x1': xs[-1]})
        if larg > pior:
            pior, px0, px1 = larg, xs[0], xs[-1]
    saida[os.path.basename(raw).replace('.raw', '')] = {
        'pior': pior, 'x0': px0, 'x1': px1, 'blocos': detalhe}
print(json.dumps(saida, sort_keys=True))
'@
$medidas = & $python -c $script $rawDir | ConvertFrom-Json
# os .raw sao 2 MB por frame (47 MB numa sequencia de 18): descartaveis
if (Test-Path $rawDir) { Remove-Item $rawDir -Recurse -Force }

# ---- 4. relatorio ----------------------------------------------------------
Write-Host ''
Write-Host ('{0,-4} {1,-6} {2,-6} {3,-12} {4,-8} {5,-6} {6}' -f '#', 'cena', 'pior', 'x0-x1', 'linhas', 'fonte', 'status')
Write-Host ('-' * 66)
$estouro = @()
for ($i = 0; $i -lt $cenas.Count; $i++) {
  $c = $cenas[$i]
  $m = $medidas.("{0:d2}-{1}" -f $i, $c.id)
  $px = $info[$c.id].px
  $esperadas = $info[$c.id].esperadas

  $origem = 'snapshot'
  if ((-not $m -or $m.pior -eq 0) -and $i -eq 0 -and $cena1NoMp4) {
    $m = $medidas.("{0:d2}-{1}-mp4" -f $i, $c.id)
    $origem = 'mp4'
  }
  if (-not $m -or $m.pior -eq 0) {
    Write-Host ('{0,-4} {1,-6} {2,-6} {3,-12} {4,-8} {5,-6} {6}' -f ($i + 1), $c.id, '-', '-', '-', $px, 'NAO MEDIDO (cena 1 sem mp4)') -ForegroundColor Yellow
    continue
  }

  # linha de verdade = bloco com pelo menos metade da altura da fonte
  $grandes = @($m.blocos | Where-Object { $px -gt 0 -and $_.altura -ge ($px * 0.5) }).Count
  $linhas = if ($esperadas -gt 0) { "{0}/{1}" -f $grandes, $esperadas } else { "$grandes" }

  $status = 'ok'; $cor = 'Green'
  if ($m.pior -gt 840 -or $m.x1 -gt 960 -or $m.x0 -lt 116) { $status = 'ESTOURA'; $cor = 'Red' }
  elseif ($m.pior -gt 810) { $status = 'apertado'; $cor = 'Yellow' }
  elseif ($esperadas -gt 0 -and $grandes -ne $esperadas) { $status = 'QUEBRA'; $cor = 'Red' }
  if ($origem -eq 'mp4') { $status += ' (mp4)' }
  Write-Host ('{0,-4} {1,-6} {2,-6} {3,-12} {4,-8} {5,-6} {6}' -f ($i + 1), $c.id, $m.pior, ("{0}-{1}" -f $m.x0, $m.x1), $linhas, $px, $status) -ForegroundColor $cor

  if ($m.pior -gt 810 -and $px -gt 0) {
    $novo = [math]::Floor($px * $Limite / $m.pior / 2) * 2
    if ($novo -lt 72) { $novo = 72 }
    if ($novo -lt $px) { $estouro += [pscustomobject]@{ id = $c.id; px = $px; novo = [int]$novo; pior = $m.pior } }
  }
}

Write-Host ''
if ($estouro.Count -eq 0) {
  Write-Host 'nenhuma cena precisa de fonte menor' -ForegroundColor Green
  return
}

Write-Host ("{0} cena(s) acima de 810 px:" -f $estouro.Count) -ForegroundColor Yellow
foreach ($e in $estouro) {
  Write-Host ("  {0}: {1} px -> {2} px  (pior linha {3})" -f $e.id, $e.px, $e.novo, $e.pior)
}

if (-not $Aplicar) {
  Write-Host ''
  Write-Host 'rode com -Aplicar para gravar no roteiro.json e gerar de novo' -ForegroundColor Yellow
  return
}
if (-not $roteiro) {
  throw "sem roteiro.json em ${Episodio}: nao sei onde aplicar"
}

foreach ($c in $roteiro.cenas) {
  foreach ($e in $estouro) {
    if ($c.id -eq $e.id) { $c.fonte_px = $e.novo }
  }
}
$roteiro | ConvertTo-Json -Depth 8 | Set-Content $roteiroPath -Encoding UTF8
Write-Host ''
Write-Host ("roteiro.json atualizado: {0}" -f (($estouro | ForEach-Object { "$($_.id) $($_.px)->$($_.novo)" }) -join ', ')) -ForegroundColor Green
Write-Host ('agora: .\.venv\Scripts\python.exe scripts\gerar-episodio.py ' + (Split-Path -Leaf $Episodio))

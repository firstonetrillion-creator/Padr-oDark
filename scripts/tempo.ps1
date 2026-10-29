#requires -Version 5.1
<#
  Marca o tempo de cada etapa da producao.
  Nao mede nada sozinho: e um cronometro manual, uma chamada por fronteira.

  Uso:
    .\scripts\tempo.ps1 -Episodio 007-foo -Etapa roteiro          # abre
    .\scripts\tempo.ps1 -Episodio 007-foo -Etapa roteiro          # fecha
    .\scripts\tempo.ps1 -Episodio 007-foo -Etapa voz -Nota "ls 1.10"
    .\scripts\tempo.ps1 -Relatorio
    .\scripts\tempo.ps1 -Relatorio -Episodio 006-passo-dyatlov

  A primeira chamada com (episodio, etapa) abre; a segunda fecha.
  Grava em logs\tempo.csv, uma linha por execucao fechada.
#>
param(
  # Slug do episodio ou 'geral' para trabalho que nao pertence a um video.
  [string]$Episodio,

  # Etapa do fluxo. Lista canonica em $Etapas (abaixo); outra coisa passa com aviso.
  [string]$Etapa,

  [string]$Nota = "",

  # Imprime o relatorio agregado em vez de marcar.
  [switch]$Relatorio,

  # Fecha um cronometro aberto mesmo que seja de outro episodio/etapa.
  [switch]$Forcar,

  # Caminho alternativo do CSV (usado nos testes; o estado fica ao lado dele).
  [string]$Arquivo
)

$ErrorActionPreference = "Stop"

$Raiz = Split-Path -Parent $PSScriptRoot
if (-not $Arquivo) { $Arquivo = Join-Path $Raiz "logs\tempo.csv" }
$Arquivo = [System.IO.Path]::GetFullPath($Arquivo)
$Dir     = Split-Path -Parent $Arquivo
if (-not (Test-Path $Dir)) { New-Item -ItemType Directory -Path $Dir -Force | Out-Null }
$Estado = Join-Path $Dir ([System.IO.Path]::GetFileNameWithoutExtension($Arquivo) + ".aberto.json")

$Etapas = @(
  "briefing", "gancho", "roteiro", "shotlist", "voz", "tempos",
  "composicao", "qa-visual", "render", "qa", "publicacao", "retencao",
  "laboratorio", "doc", "outro"
)

function Min($m) {
  return [string]::Format([Globalization.CultureInfo]::InvariantCulture, "{0:N1}", $m)
}
function Campo($s) {
  # aspas duplas escapadas para CSV
  return '"' + ($s -replace '"', '""') + '"'
}
function LerAberto {
  if (-not (Test-Path $Estado)) { return $null }
  try { return Get-Content $Estado -Raw -Encoding UTF8 | ConvertFrom-Json } catch { return $null }
}

# ---------------------------------------------------------------- relatorio
if ($Relatorio) {
  if (-not (Test-Path $Arquivo)) {
    Write-Host "sem dados ainda: $Arquivo" -ForegroundColor Yellow
    exit 0
  }
  $linhas = @(Import-Csv -Path $Arquivo -Encoding UTF8)
  if ($Episodio) { $linhas = @($linhas | Where-Object { $_.episodio -eq $Episodio }) }
  if ($linhas.Count -eq 0) {
    Write-Host "nenhuma execucao registrada$(if ($Episodio) { " para $Episodio" })" -ForegroundColor Yellow
    exit 0
  }

  $total = 0.0
  $porEtapa = @{}
  foreach ($l in $linhas) {
    $m = 0.0
    [void][double]::TryParse($l.minutos, [Globalization.NumberStyles]::Any, [Globalization.CultureInfo]::InvariantCulture, [ref]$m)
    $total += $m
    if (-not $porEtapa.ContainsKey($l.etapa)) { $porEtapa[$l.etapa] = @{ total = 0.0; n = 0 } }
    $porEtapa[$l.etapa].total += $m
    $porEtapa[$l.etapa].n++
  }

  Write-Host ""
  Write-Host ("== tempo " + $(if ($Episodio) { $Episodio } else { "todo o projeto" })) -ForegroundColor Cyan
  Write-Host ("   {0} execucoes, {1} min ({2} h)" -f $linhas.Count, (Min $total), (Min ($total / 60.0)))

  $tabela = foreach ($k in $porEtapa.Keys) {
    [pscustomobject]@{
      etapa      = $k
      minutos    = [math]::Round($porEtapa[$k].total, 1)
      execucoes  = $porEtapa[$k].n
      media      = [math]::Round($porEtapa[$k].total / $porEtapa[$k].n, 1)
      pct        = if ($total -gt 0) { [math]::Round(100.0 * $porEtapa[$k].total / $total, 0) } else { 0 }
    }
  }
  $tabela | Sort-Object minutos -Descending |
    Format-Table etapa, minutos, execucoes, media, pct -AutoSize | Out-String -Width 200 | Write-Host

  if (-not $Episodio) {
    Write-Host "== por episodio" -ForegroundColor Cyan
    $linhas | Group-Object episodio | ForEach-Object {
      $t = 0.0
      foreach ($l in $_.Group) {
        $m = 0.0
        [void][double]::TryParse($l.minutos, [Globalization.NumberStyles]::Any, [Globalization.CultureInfo]::InvariantCulture, [ref]$m)
        $t += $m
      }
      [pscustomobject]@{
        episodio = $_.Name
        minutos  = [math]::Round($t, 1)
        horas    = [math]::Round($t / 60.0, 1)
        execucoes = $_.Count
      }
    } | Sort-Object minutos -Descending |
      Format-Table episodio, minutos, horas, execucoes -AutoSize | Out-String -Width 200 | Write-Host
  }

  $aberto = LerAberto
  if ($aberto) {
    Write-Host ("cronometro ABERTO: {0} / {1} desde {2}" -f $aberto.episodio, $aberto.etapa, $aberto.inicio) -ForegroundColor Yellow
  }
  Write-Host ""
  exit 0
}

# ---------------------------------------------------------------- marcar
if (-not $Episodio -or -not $Etapa) {
  throw "informe -Episodio e -Etapa (ou use -Relatorio)"
}
if ($Etapas -notcontains $Etapa) {
  Write-Host ("aviso: etapa fora da lista canonica ({0}). Lista: {1}" -f $Etapa, ($Etapas -join ", ")) -ForegroundColor Yellow
}

$agora  = Get-Date
$aberto = LerAberto

if ($aberto -and ($aberto.episodio -ne $Episodio -or $aberto.etapa -ne $Etapa) -and -not $Forcar) {
  $desde = [datetime]::Parse($aberto.inicio)
  throw ("cronometro aberto em {0} / {1} desde {2} ({3} min). Feche antes, ou use -Forcar." -f `
    $aberto.episodio, $aberto.etapa, $aberto.inicio, (Min ($agora - $desde).TotalMinutes))
}

if ($aberto) {
  $ini = [datetime]::Parse($aberto.inicio)
  $min = [math]::Max(0.0, ($agora - $ini).TotalMinutes)
  if (-not (Test-Path $Arquivo)) {
    Set-Content -Path $Arquivo -Value "data,episodio,etapa,inicio,fim,minutos,nota" -Encoding UTF8
  }
  $linha = (@(
    $agora.ToString("yyyy-MM-dd"),
    (Campo $aberto.episodio),
    (Campo $aberto.etapa),
    $ini.ToString("yyyy-MM-dd HH:mm"),
    $agora.ToString("yyyy-MM-dd HH:mm"),
    (Min $min),
    (Campo $(if ($Nota) { $Nota } else { $aberto.nota }))
  ) -join ",")
  Add-Content -Path $Arquivo -Value $linha -Encoding UTF8
  Remove-Item $Estado -Force
  Write-Host ("FECHADO  {0,-12} {1,-11} {2} min" -f $aberto.episodio, $aberto.etapa, (Min $min)) -ForegroundColor Green
  exit 0
}

$obj = [pscustomobject]@{
  episodio = $Episodio
  etapa    = $Etapa
  inicio   = $agora.ToString("o")
  nota     = $Nota
}
$obj | ConvertTo-Json -Compress | Set-Content -Path $Estado -Encoding UTF8
Write-Host ("ABERTO   {0,-12} {1,-11} {2}" -f $Episodio, $Etapa, $agora.ToString("HH:mm:ss")) -ForegroundColor Cyan

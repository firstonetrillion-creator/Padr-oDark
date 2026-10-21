#requires -Version 5.1
<#
.SYNOPSIS
  Valida o contrato da composicao antes do render (docs/ARQUITETURA.md §2, §3 e §5).

.DESCRIPTION
  Roda em ~1 s o que hoje se descobre olhando frame ou ouvindo o video mudo.
  Nao substitui o QA visual nem o scripts/qa.ps1: pega erro de contrato.

.PARAMETER Arquivo
  Caminho do index.html. Se omitido, procura episodios/*/index.html e usa o unico encontrado.

.PARAMETER SemAudio
  Pula a checagem de duracao de voz.wav/drone.wav com ffprobe.

.EXAMPLE
  .\scripts\check-contrato.ps1 episodios\002-caso\index.html

.EXAMPLE
  .\scripts\check-contrato.ps1
#>
[CmdletBinding()]
param(
  [Parameter(Position = 0)]
  [string]$Arquivo,

  [switch]$SemAudio
)

$ErrorActionPreference = 'Stop'
$inv = [Globalization.CultureInfo]::InvariantCulture

function Add-Resultado {
  param([string]$Status, [string]$Check, [string]$Detalhe)
  $script:resultados.Add([pscustomobject]@{ Status = $Status; Check = $Check; Detalhe = $Detalhe }) | Out-Null
}
function Pass  { param($c, $d = '') Add-Resultado 'PASS' $c $d }
function Warn  { param($c, $d = '') Add-Resultado 'WARN' $c $d }
function Fail  { param($c, $d = '') Add-Resultado 'FAIL' $c $d }

function Get-Atributo {
  param([string]$Tag, [string]$Nome)
  $m = [regex]::Match($Tag, '(?i)\b' + [regex]::Escape($Nome) + '\s*=\s*"([^"]*)"')
  if ($m.Success) { return $m.Groups[1].Value.Trim() }
  return $null
}

function To-Numero {
  param([string]$Valor)
  if ([string]::IsNullOrWhiteSpace($Valor)) { return $null }
  $d = 0.0
  if ([double]::TryParse($Valor, [Globalization.NumberStyles]::Float, $inv, [ref]$d)) { return $d }
  return $null
}

function Get-DuracaoAudio {
  param([string]$Caminho)
  $ffprobe = Get-Command ffprobe -ErrorAction SilentlyContinue
  if (-not $ffprobe) { return $null }
  try {
    $saida = & $ffprobe.Source -v error -show_entries format=duration -of 'default=nw=1:nk=1' $Caminho 2>$null
    return To-Numero ($saida | Select-Object -First 1)
  } catch {
    return $null
  }
}

$script:resultados = New-Object System.Collections.ArrayList

# ---------- localizar o arquivo ----------
if (-not $Arquivo) {
  $candidatos = @(Get-ChildItem -Path (Join-Path $PSScriptRoot '..\episodios') -Filter index.html -Recurse -File -ErrorAction SilentlyContinue)
  if ($candidatos.Count -eq 1) {
    $Arquivo = $candidatos[0].FullName
  } elseif ($candidatos.Count -eq 0) {
    Write-Host 'Nenhum episodios/*/index.html encontrado.' -ForegroundColor Red
    exit 1
  } else {
    Write-Host 'Mais de um episodio encontrado. Passe o caminho:' -ForegroundColor Yellow
    $candidatos | ForEach-Object { Write-Host ('  ' + $_.FullName) }
    exit 1
  }
}

if (-not (Test-Path -LiteralPath $Arquivo)) {
  Write-Host ('Arquivo nao encontrado: ' + $Arquivo) -ForegroundColor Red
  exit 1
}
$Arquivo = (Resolve-Path -LiteralPath $Arquivo).Path
$dir = Split-Path -Parent $Arquivo
$html = Get-Content -LiteralPath $Arquivo -Raw -Encoding UTF8
Pass 'arquivo' (Split-Path $Arquivo -Leaf)

# ---------- 1. raiz #stage ----------
$stageMatch = [regex]::Match($html, '(?is)<div\b[^>]*\bid\s*=\s*"stage"[^>]*>')
if (-not $stageMatch.Success) {
  Fail 'raiz #stage' 'div id="stage" nao encontrado'
} else {
  $tag = $stageMatch.Value
  $w = Get-Atributo $tag 'data-width'
  $h = Get-Atributo $tag 'data-height'
  $fps = Get-Atributo $tag 'data-fps'
  $comp = Get-Atributo $tag 'data-composition-id'
  $inicio = Get-Atributo $tag 'data-start'

  if ($w -eq '1080' -and $h -eq '1920') { Pass 'resolucao' ($w + 'x' + $h) } else { Fail 'resolucao' ('esperado 1080x1920, veio ' + $w + 'x' + $h) }
  if ($fps -eq '30') { Pass 'fps' '30' } else { Fail 'fps' ('esperado 30, veio ' + $fps) }
  if ($inicio -eq '0') { Pass 'stage data-start' '0' } else { Fail 'stage data-start' ('esperado 0, veio ' + $inicio) }
  if ([string]::IsNullOrWhiteSpace($comp)) {
    Fail 'data-composition-id' 'ausente (runtime nao monta a timeline)'
  } elseif ($comp -match '^ep\d{3}$') {
    Pass 'data-composition-id' $comp
  } else {
    Warn 'data-composition-id' ('fora do padrao epNNN: ' + $comp)
  }
}

# ---------- 2. cenas ----------
$secoes = @([regex]::Matches($html, '(?is)<section\b(?<a>[^>]*)>'))
$cenas = @()
foreach ($s in $secoes) {
  $attrs = $s.Groups['a'].Value
  $classe = Get-Atributo $attrs 'class'
  if ($classe -notmatch '(?i)\bscene\b') { continue }
  $id = Get-Atributo $attrs 'id'
  $cenas += [pscustomobject]@{
    Id       = $id
    Inicio   = To-Numero (Get-Atributo $attrs 'data-start')
    Duracao  = To-Numero (Get-Atributo $attrs 'data-duration')
    Track    = Get-Atributo $attrs 'data-track-index'
    Clipado  = ($classe -match '(?i)\bclip\b')
  }
}

if ($cenas.Count -eq 0) {
  Fail 'cenas' 'nenhuma <section class="scene"> encontrada'
} else {
  if ($cenas.Count -eq 13) { Pass 'cenas' '13' } else { Warn 'cenas' ($cenas.Count.ToString() + ' (padrao do formato: 13; divisao de frase longa e permitida)') }

  $semId = @($cenas | Where-Object { [string]::IsNullOrWhiteSpace($_.Id) })
  $semTempo = @($cenas | Where-Object { $_.Inicio -eq $null -or $_.Duracao -eq $null })
  $semTrack = @($cenas | Where-Object { $_.Track -ne '1' })
  $semClip = @($cenas | Where-Object { -not $_.Clipado })

  if ($semId.Count -eq 0) { Pass 'id por cena' 'todas nomeadas' } else { Fail 'id por cena' ($semId.Count.ToString() + ' sem id') }
  if ($semTempo.Count -eq 0) { Pass 'data-start/duration' 'todas numericas' } else { Fail 'data-start/duration' ($semTempo.Count.ToString() + ' cenas sem tempo valido') }
  if ($semTrack.Count -eq 0) { Pass 'data-track-index' '1 em todas' } else { Fail 'data-track-index' ($semTrack.Count.ToString() + ' cenas fora da track 1') }
  if ($semClip.Count -eq 0) { Pass 'classe clip' 'em todas (QA por ?t=)' } else { Warn 'classe clip' ($semClip.Count.ToString() + ' cenas sem a classe clip') }

  $ids = @($cenas | ForEach-Object { $_.Id })
  $dup = @($ids | Group-Object | Where-Object { $_.Count -gt 1 })
  if ($dup.Count -eq 0) { Pass 'ids unicos' '' } else { Fail 'ids unicos' (($dup | ForEach-Object { $_.Name }) -join ', ') }

  if ($semTempo.Count -eq 0) {
    $ord = @($cenas | Sort-Object Inicio)
    $sobreposicao = @()
    for ($i = 0; $i -lt $ord.Count - 1; $i++) {
      $fim = $ord[$i].Inicio + $ord[$i].Duracao
      if ($fim -gt $ord[$i + 1].Inicio + 0.001) {
        $sobreposicao += ($ord[$i].Id + ' termina em ' + [math]::Round($fim, 2) + ' > ' + $ord[$i + 1].Id)
      }
    }
    if ($sobreposicao.Count -eq 0) { Pass 'sem sobreposicao' 'cenas em sequencia' } else { Fail 'sem sobreposicao' ($sobreposicao -join '; ') }

    if ([math]::Abs($ord[0].Inicio) -lt 0.001) { Pass 'primeira cena em 0' '' } else { Fail 'primeira cena em 0' ('comeca em ' + $ord[0].Inicio) }

    $fimTotal = $ord[$ord.Count - 1].Inicio + $ord[$ord.Count - 1].Duracao
    if ($fimTotal -ge 44.9 -and $fimTotal -le 45.05) {
      Pass 'cobertura ate 45 s' ([math]::Round($fimTotal, 2).ToString($inv) + ' s')
    } else {
      Fail 'cobertura ate 45 s' ('ultima cena termina em ' + [math]::Round($fimTotal, 2).ToString($inv) + ' s')
    }
  }

  # CSS de fonte por cena: sem regra, o titulo cai no tamanho padrao do navegador
  $semCss = @()
  foreach ($c in $cenas) {
    if ([string]::IsNullOrWhiteSpace($c.Id)) { continue }
    if ($html -notmatch ('(?i)\.' + [regex]::Escape($c.Id) + '\s+h1\s*\{')) { $semCss += $c.Id }
  }
  if ($semCss.Count -eq 0) { Pass 'CSS por cena' 'font-size definido' } else { Warn 'CSS por cena' ('sem regra .<id> h1: ' + ($semCss -join ', ')) }
}

# ---------- 3. audio ----------
$audioVoz = [regex]::Match($html, '(?is)<audio\b[^>]*\bid\s*=\s*"voz"[^>]*>')
$audioDrone = [regex]::Match($html, '(?is)<audio\b[^>]*\bid\s*=\s*"drone"[^>]*>')

if (-not $audioVoz.Success) {
  Fail 'audio #voz' 'sem id="voz" -> render mudo'
} else {
  $t = $audioVoz.Value
  $dur = To-Numero (Get-Atributo $t 'data-duration')
  $ini = To-Numero (Get-Atributo $t 'data-start')
  $vol = To-Numero (Get-Atributo $t 'data-volume')
  $src = Get-Atributo $t 'src'
  if ($dur -ge 44.9 -and $dur -le 45.1) { Pass 'voz duracao' ($dur.ToString($inv) + ' s') } else { Fail 'voz duracao' ('esperado 45, veio ' + $dur) }
  if ($ini -eq 0) { Pass 'voz data-start' '0' } else { Fail 'voz data-start' ('esperado 0, veio ' + $ini) }
  if ($vol -eq 1) { Pass 'voz volume' '1' } else { Warn 'voz volume' ('esperado 1, veio ' + $vol) }
  if ($src) {
    $p = Join-Path $dir $src
    if (Test-Path -LiteralPath $p) {
      Pass 'voz.wav presente' $src
      if (-not $SemAudio) {
        $d = Get-DuracaoAudio $p
        if ($d -eq $null) { Warn 'voz.wav duracao' 'ffprobe indisponivel' }
        elseif ($d -ge 44.9 -and $d -le 45.1) { Pass 'voz.wav duracao' ($d.ToString('0.00', $inv) + ' s') }
        else { Fail 'voz.wav duracao' ('arquivo tem ' + $d.ToString('0.00', $inv) + ' s; o contrato pede 45,00') }
      }
    } else { Fail 'voz.wav presente' ('nao existe em ' + $dir) }
  } else { Fail 'voz src' 'sem atributo src' }
}

if (-not $audioDrone.Success) {
  Fail 'audio #drone' 'sem id="drone"'
} else {
  $t = $audioDrone.Value
  $dur = To-Numero (Get-Atributo $t 'data-duration')
  $vol = To-Numero (Get-Atributo $t 'data-volume')
  $src = Get-Atributo $t 'src'
  if ($dur -ge 44.9 -and $dur -le 45.1) { Pass 'drone duracao' ($dur.ToString($inv) + ' s') } else { Fail 'drone duracao' ('esperado 45, veio ' + $dur) }
  if ($vol -ne $null -and $vol -le 0.25) { Pass 'drone volume' ($vol.ToString($inv)) } else { Warn 'drone volume' ('a voz deve dominar (template: 0,16); veio ' + $vol) }
  if ($src) {
    $p = Join-Path $dir $src
    if (Test-Path -LiteralPath $p) {
      Pass 'drone.wav presente' $src
      if (-not $SemAudio) {
        $d = Get-DuracaoAudio $p
        if ($d -eq $null) { Warn 'drone.wav duracao' 'ffprobe indisponivel' }
        elseif ($d -ge 44.9 -and $d -le 45.1) { Pass 'drone.wav duracao' ($d.ToString('0.00', $inv) + ' s') }
        else { Fail 'drone.wav duracao' ('arquivo tem ' + $d.ToString('0.00', $inv) + ' s; o contrato pede 45,00') }
      }
    } else { Fail 'drone.wav presente' ('nao existe em ' + $dir) }
  } else { Fail 'drone src' 'sem atributo src' }
}

# ---------- 4. timeline / autoAlpha ----------
$autoAlpha = ([regex]::Matches($html, 'autoAlpha')).Count
if ($autoAlpha -ge 3) { Pass 'autoAlpha' ($autoAlpha.ToString() + ' usos (sem fantasma)') } else { Fail 'autoAlpha' 'ausente: texto de uma cena vaza na seguinte' }

$loopOk = ($html -match 'dataset\.start') -and ($html -match 'dataset\.duration')
if ($loopOk) { Pass 'loop usa dataset' 'start/duration lidos do DOM' } else { Fail 'loop usa dataset' 'a timeline nao le data-start/data-duration das cenas' }

if ($comp -and $comp -match '^ep\d{3}$') {
  if ($html -match ('window\.__timelines\s*\.\s*' + [regex]::Escape($comp) + '\s*=')) {
    Pass 'montagem da timeline' ('window.__timelines.' + $comp)
  } else {
    Fail 'montagem da timeline' ('data-composition-id="' + $comp + '" sem window.__timelines.' + $comp)
  }
}

if ($html -match '(?is)id\s*=\s*"fade"') {
  if ($html -match '(?is)#fade') { Pass 'fade final' 'presente' } else { Warn 'fade final' '#fade sem animacao' }
} else { Warn 'fade final' 'sem elemento #fade' }

if ($html -match 'URLSearchParams\(location\.search\)') { Pass 'QA por ?t=' 'suportado' } else { Warn 'QA por ?t=' 'ausente: QA visual exige render' }

# ---------- 5. risco de publicar o template ----------
# O 001 e a origem do template: o texto dele e legitimo.
if ($comp -ne 'ep001') {
  $titulo = [regex]::Match($html, '(?is)<title>(?<t>.*?)</title>')
  if ($titulo.Success -and $titulo.Groups['t'].Value -match '(?i)eilean|faroleiro') {
    Warn 'conteudo do template' 'titulo ainda e o exemplo do 001'
  }
  if ($html -match '(?i)HOMENS<br>SUMIRAM') {
    Warn 'conteudo do template' 'texto de exemplo ("TRES HOMENS...") ainda presente'
  }
}

# ---------- saida ----------
$falhas = @($script:resultados | Where-Object { $_.Status -eq 'FAIL' }).Count
$avisos = @($script:resultados | Where-Object { $_.Status -eq 'WARN' }).Count

Write-Host ''
Write-Host ('CONTRATO: ' + (Split-Path $dir -Leaf)) -ForegroundColor White
Write-Host ('arquivo: ' + $Arquivo) -ForegroundColor DarkGray
Write-Host ''
foreach ($r in $script:resultados) {
  switch ($r.Status) {
    'PASS' { $cor = 'Green' }
    'WARN' { $cor = 'Yellow' }
    default { $cor = 'Red' }
  }
  Write-Host ('[' + $r.Status + '] ' + $r.Check.PadRight(24) + ' ' + $r.Detalhe) -ForegroundColor $cor
}
Write-Host ''
if ($falhas -gt 0) {
  Write-Host ('RESULTADO: ' + $falhas + ' falha(s), ' + $avisos + ' aviso(s). NAO RENDERIZAR antes de corrigir.') -ForegroundColor Red
  exit 1
}
Write-Host ('RESULTADO: contrato OK (' + $avisos + ' aviso(s)). Pode seguir para o QA visual e o render.') -ForegroundColor Green
exit 0


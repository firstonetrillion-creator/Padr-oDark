#requires -Version 5.1
<#
.SYNOPSIS
  Cria um episodio novo a partir de templates/misterio-45, com carimbo da versao do template.

.DESCRIPTION
  Nunca sobrescreve um episodio existente (evidencia nao se apaga).
  Troca o que e contrato: data-composition-id, chave de window.__timelines,
  numero do dossie e titulo. O resto do template fica igual de proposito:
  se o template mudar, o carimbo em .template-version diz de onde o episodio saiu.

.PARAMETER Slug
  Formato NNN-nome-curto, ex.: 002-voo-914.

.PARAMETER Titulo
  Titulo interno da composicao (vai para <title>). Pode ser ajustado depois.

.PARAMETER Marca
  Texto da marca no canto superior. Padrao: mantem o que esta no template.

.EXAMPLE
  .\scripts\novo-episodio.ps1 002-voo-914 "Voo 914: o aviao que pousou vazio"

.EXAMPLE
  .\scripts\novo-episodio.ps1 003-caso-x -Marca "DOSSIÊ 45"
#>
[CmdletBinding()]
param(
  [Parameter(Mandatory = $true, Position = 0)]
  [string]$Slug,

  [Parameter(Position = 1)]
  [string]$Titulo = '',

  [string]$Marca = ''
)

$ErrorActionPreference = 'Stop'
$inv = [Globalization.CultureInfo]::InvariantCulture
$utf8SemBom = New-Object System.Text.UTF8Encoding($false)

function Gravar {
  param([string]$Caminho, [string]$Texto)
  [System.IO.File]::WriteAllText($Caminho, $Texto, $utf8SemBom)
}

if ($Slug -notmatch '^\d{3}-[a-z0-9]+(?:-[a-z0-9]+)*$') {
  Write-Host ('Slug invalido: "' + $Slug + '"') -ForegroundColor Red
  Write-Host 'Use NNN-nome-curto em minusculas, ex.: 002-voo-914' -ForegroundColor Yellow
  exit 1
}

$raiz = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$templateDir = Join-Path $raiz 'templates\misterio-45'
$templateHtml = Join-Path $templateDir 'index.html'
$templateGsap = Join-Path $templateDir 'gsap.min.js'
$destino = Join-Path (Join-Path $raiz 'episodios') $Slug

if (-not (Test-Path -LiteralPath $templateHtml)) {
  Write-Host ('Template nao encontrado: ' + $templateHtml) -ForegroundColor Red
  exit 1
}
if (Test-Path -LiteralPath $destino) {
  Write-Host ('Episodio ja existe: ' + $destino) -ForegroundColor Red
  Write-Host 'Nao sobrescrevo evidencia. Escolha outro slug ou mova a pasta antiga.' -ForegroundColor Yellow
  exit 1
}

$numero = $Slug.Substring(0, 3)
$compId = 'ep' + $numero
$agora = Get-Date
$data = $agora.ToString('yyyy-MM-dd')
$hora = $agora.ToString('HH:mm')

$hashCompleto = (Get-FileHash -LiteralPath $templateHtml -Algorithm SHA256).Hash.ToLower()
$hashCurto = $hashCompleto.Substring(0, 8)

$commit = 'sem-git'
try {
  $c = & git -C $raiz rev-parse --short HEAD 2>$null
  if ($LASTEXITCODE -eq 0 -and $c) { $commit = ($c | Select-Object -First 1).Trim() }
} catch { }

if (-not $Titulo) {
  $Titulo = $numero + ' — (definir titulo)'
  Write-Host 'Aviso: sem -Titulo, o <title> fica com marcador para preencher.' -ForegroundColor Yellow
}

# ---------- copiar ----------
New-Item -ItemType Directory -Path $destino -Force | Out-Null
Copy-Item -LiteralPath $templateGsap -Destination (Join-Path $destino 'gsap.min.js') -Force

$html = Get-Content -LiteralPath $templateHtml -Raw -Encoding UTF8

# carimbo de origem logo apos o doctype
$carimbo = '<!-- GERADO por scripts/novo-episodio.ps1 em ' + $data + ' ' + $hora +
           ' | template misterio-45 sha256:' + $hashCurto + ' | commit:' + $commit + ' -->' + "`r`n"
$html = $html -replace '(?i)^<!doctype html>', ('<!doctype html>' + "`r`n" + $carimbo)

# contrato: composicao e timeline
$html = $html.Replace('data-composition-id="ep001"', 'data-composition-id="' + $compId + '"')
$html = $html.Replace('window.__timelines.ep001', 'window.__timelines.' + $compId)
$html = $html.Replace('<div class="dossier">001</div>', '<div class="dossier">' + $numero + '</div>')

# titulo
$tituloSeguro = [System.Security.SecurityElement]::Escape($Titulo).Replace('$', '$$')
$html = [regex]::Replace($html, '(?is)<title>.*?</title>', '<title>' + $tituloSeguro + '</title>')

# marca (opcional)
if ($Marca) {
  $marcaSegura = [System.Security.SecurityElement]::Escape($Marca).Replace('$', '$$')
  $html = [regex]::Replace($html, '(?is)<div class="mark">.*?</div>', '<div class="mark">' + $marcaSegura + '</div>')
}

Gravar (Join-Path $destino 'index.html') $html

# ---------- carimbo legivel por maquina ----------
$carimboArquivo = @(
  'template=misterio-45'
  'template_sha256=' + $hashCompleto
  'template_sha256_curto=' + $hashCurto
  'gerado_em=' + $agora.ToString('yyyy-MM-ddTHH:mm:ss')
  'slug=' + $Slug
  'composicao=' + $compId
  'commit_no_momento=' + $commit
) -join "`r`n"
Gravar (Join-Path $destino '.template-version') ($carimboArquivo + "`r`n")

# ---------- status ----------
$status = @'
# Status — __NUMERO__

> Criado por `scripts/novo-episodio.ps1` em __DATA__ a partir de `templates/misterio-45`
> (sha256 `__HASH__`, commit `__COMMIT__`). Atualizar a cada etapa concluida.

| Etapa | Estado | Artefato |
|---|---|---|
| Briefing | pendente | `briefing.md` |
| Gancho | pendente | `gancho.md` |
| Roteiro | pendente | `roteiro.md` |
| Narracao | pendente | `narracao.txt`, `voz_raw.wav`, `voz.wav` (45,00 s) |
| Transcricao | pendente | `transcricao.json` |
| Assets | nao usado | v1 tipografica (sem imagens) |
| Composicao | pendente | `index.html` (13 cenas) |
| QA visual | pendente | `qa-frames/` |
| Render | pendente | `final.mp4` |
| QA | pendente | `qa.md` |
| Publicacao | pendente | YouTube Shorts |

## Medicoes

- Voz crua: —
- Voz final: —
- Contrato (`check-contrato.ps1`): —
- Render (standard): —
- Loudness: — LUFS cru -> — LUFS final

## Proximos passos

1. `briefing.md` (skill briefing) e `gancho.md` (skill gancho).
2. `roteiro.md` com 110–125 palavras.
3. TTS + processamento para 45,00 s.
4. Transcrever e remapear `data-start`/`data-duration`.
5. `.\scripts\check-contrato.ps1 episodios\__SLUG__\index.html` -> contrato OK.
6. QA visual por `?t=` e render (um por vez).
'@

$status = $status.Replace('__NUMERO__', $numero)
$status = $status.Replace('__DATA__', $data + ' ' + $hora)
$status = $status.Replace('__HASH__', $hashCurto)
$status = $status.Replace('__COMMIT__', $commit)
$status = $status.Replace('__SLUG__', $Slug)
Gravar (Join-Path $destino 'status.md') $status

# ---------- saida ----------
Write-Host ''
Write-Host ('Episodio criado: episodios\' + $Slug) -ForegroundColor Green
Write-Host ('  composicao : ' + $compId + '  (timeline: window.__timelines.' + $compId + ')') -ForegroundColor Gray
Write-Host ('  template   : misterio-45 @ ' + $hashCurto + ' (commit ' + $commit + ')') -ForegroundColor Gray
Write-Host ('  marca      : ' + $(if ($Marca) { $Marca } else { 'mantida do template' })) -ForegroundColor Gray
Write-Host ''
Write-Host 'Proximo passo: briefing -> gancho -> roteiro. O index.html ainda tem os textos do 001.' -ForegroundColor Yellow
Write-Host ('Antes do render: .\scripts\check-contrato.ps1 episodios\' + $Slug + '\index.html') -ForegroundColor Yellow
exit 0


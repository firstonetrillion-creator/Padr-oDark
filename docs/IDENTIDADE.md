# Identidade visual e sonora (provisória)

Marca de trabalho: **Dossiê 45** (handle `@Dossie45`, confirmado no canal).

## Paleta

| Uso | Hex |
|---|---|
| Fundo | `#0A0A0B` |
| Superfície | `#1A1A1D` |
| Texto | `#E8E6E1` |
| Acento | `#B23A2E` (vermelho seco) |
| Apoio | `#6B6B70` |

## Tipografia

- Título: serif condensada (ex.: Playfair Display, Cormorant, Bebas com peso)
- Corpo/legenda: sans neutra (Inter, Roboto)
- Legendas: caixa alta, tracking leve, fundo preto 60%

## Imagem

- Grain 8–12%
- Vinheta suave
- Dessaturação parcial, contraste alto
- Slow push-in e parallax leve
- Corte a cada 1,5–3 s

## Movimento

- Entradas por máscara e slide vertical curto
- Nada de bounce ou easing infantil
- Transições por corte seco e flash de 2 frames

## Som

- Drone grave contínuo (40–80 Hz)
- Riser antes do twist
- Sub-hit nos cortes principais
- Crackle de vinil em volume baixo
- Silêncio de 0,3 s antes da revelação

## Voz

- Piper `pt_BR-faber-medium`
- Pitch −2 semitons
- EQ: corte abaixo de 80 Hz, presença em 3–5 kHz
- Compressão suave, reverb curto (0,8 s)

## Estrutura narrativa (Mistério 45)

| Tempo | Beat |
|---|---|
| 0–2 s | Gancho visual + frase de choque |
| 2–10 s | Contexto mínimo |
| 10–30 s | Três pistas / escalada |
| 30–40 s | Twist |
| 40–45 s | Implicação + CTA |

## Nomes candidatos (checagem 2026-10-21)

| Nome | Handle | Status |
|---|---|---|
| **Dossiê 45** | `@Dossie45` | **adotado em 21/10/2026** (handle e assets no ar; nome de exibição a reconfirmar na página pública) |
| Arquivo 3:07 | `@Arquivo307` | 404 = disponível; nome mais único |
| Arquivo Noturno 45 | `@ArquivoNoturno45` | 404 = disponível, mas “Arquivo Noturno” já existe |
| Sala Escura | `@SalaEscura` | ocupado (“A Sala Escura”) |
| Dossiê 404 | `@Dossie404` | ocupado/redireciona |
| Canal 3AM | `@Canal3AM` | ocupado |
| O Relatório | `@ORelatorio` | ocupado |
| Arquivo Noturno | `@ArquivoNoturno` | ocupado |
| Arquivo da Meia-Noite | `@ArquivoDaMeiaNoite` | ocupado |
| Dossiê Noturno | `@DossieNoturno` | ocupado |
| Relatório Noturno | `@RelatorioNoturno` | ocupado |

> Checagem por HTTP 404 no perfil; não é garantia até confirmar dentro do YouTube Studio. “Dossiê 45” é a proposta: nome de arquivo/investigação + duração do formato.

## Arquivos de marca

| Arquivo | Uso | Especificação |
|---|---|---|
| `identidade/banner.png` | banner do canal | 2048×1152; todo o texto dentro da área segura 1235×338 |
| `identidade/avatar.png` | avatar do canal | 800×800 |
| `identidade/banner.html` | fonte editável do banner | paleta e tipografia do projeto |
| `identidade/avatar.html` | fonte editável do avatar | idem |

### Auditoria rápida dos assets (21/10/2026)

- **Banner:** 2048×1152 local; o recorte público tem 2048×339. Título e
  subtítulo estão dentro da área segura 1235×338; o recorte ao vivo não corta
  nenhum dos dois. Os microtextos dos cantos (1,6:1 de contraste) ficam fora do
  recorte e funcionam como textura, não como leitura.
- **Avatar:** 800×800 local; o canal serve 900×900. O monograma `D45` está
  centralizado e sobrevive ao corte circular. O vermelho `#B23A2E` tem 3,33:1
  sobre o fundo — passa para texto grande, mas fica no limite em tamanho de
  feed; o `D` branco tem 15,87:1.
- **Consistência:** banner e avatar usam a mesma paleta, Georgia e o motivo
  `D45`/`DOSSIÊ 45`. Não bloqueiam o 002.

Regerar depois de editar o HTML (Chrome headless, sem dependência nova):

```powershell
$chrome = "$env:USERPROFILE\.cache\hyperframes\chrome\chrome-headless-shell\win64-152.0.7977.30\chrome-headless-shell-win64\chrome-headless-shell.exe"
& $chrome --disable-gpu --hide-scrollbars --force-device-scale-factor=1 `
  --window-size=2048,1152 --virtual-time-budget=2000 `
  --screenshot="$PWD\identidade\banner.png" "file:///$($PWD.Path.Replace('\','/'))/identidade/banner.html"
```

Para o avatar, trocar `2048,1152` por `800,800` e o nome do arquivo. Se o caminho tiver acento, copiar o HTML para `%TEMP%` antes de renderizar.

## Checklist de rebranding (Cod Mind Million → Dossiê 45)

> Textos prontos e ordem de execução: `docs/REBRANDING.md`.

- [x] Confirmar `@Dossie45` no canal — **21/10/2026**, mesmo channel ID do piloto (`UCwgP68Uen2KoIh2R-j231Yw`).
- [x] Subir `identidade/avatar.png` e `identidade/banner.png` — verificados no ar em 21/10.
- [ ] Nome de exibição: usuário confirma **Dossiê 45**; a página pública ainda mostra `Dossie45` (possível cache). Reconfirmar no Studio.
- [ ] Descrição impessoal: “Arquivo de casos sem solução. Fatos com fonte; lendas marcadas como lenda.” A página pública ainda mostra vazio.
- [ ] Unlistar/privar os 9 shorts de psicologia; a aba Shorts ainda mostra 10 vídeos.
- [ ] Revisar links, país, palavras-chave e configurações de upload.
- [ ] Atualizar `docs/`, `MEMORIA.md` e `biblioteca/publicados.csv` se o nome do canal aparecer.
- [ ] Só depois publicar o vídeo 002.

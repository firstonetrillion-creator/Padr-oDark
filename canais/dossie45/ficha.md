# Canal `dossie45`

> Preenchido em **27/10/2026**, depois dos 6 vídeos. Serve de exemplo: é o único
> canal com histórico, então é a **referência** de todos os testes.

## Identidade

| Campo | Valor |
|---|---|
| Nome | Dossiê 45 |
| Handle | @Dossie45 |
| Conta Google (brand account) | a mesma desde 21/10/2026 |
| Aberto em | 2026-10-21 (6 shorts antigos ficaram privados no rebranding) |
| Slug | `dossie45` |
| Estado | `ativo` — mas **congelado** até o Gate 2 |

## Tese

> Aposto que **homens de 55+, majoritariamente no celular**, assistem **cartões
> tipográficos de 45 s** sobre **casos de arquivo e mistério com fonte primária**
> até o fim, porque **o caso é contado como documento, não como susto**.

A tese **não está confirmada**: o público medido (82,1% com 55+, 0% abaixo de 45,
78,2% masculino, 94,7% celular, Brasil 49,2%) apareceu **depois**, sem intenção.
E o miolo do 004 caiu pela metade.

## O modelo em 5 escolhas

| Dimensão | Este canal | Mudou? |
|---|---|---|
| Nicho | arquivo/mistério PT-BR, fato com fonte primária | — (é o modelo) |
| Formato | 45 s, 12–14 cenas, 1 ideia por cartão, ≤5 s por cena | — |
| Voz | Piper `pt_BR-faber-medium`, 2,2–2,5 pal./s, impessoal | — |
| Cadência | irregular: 2 em 21/10, 1 em 23/10, 1 em 24/10, 2 em 27/10 | — |
| Visual | v1 tipográfico: só texto, moldura, marca `DOSSIÊ 45`, drone inaudível (0,16) | — |

## Hipótese e critério

| Campo | Valor |
|---|---|
| Métrica primária | `% média assistida` em 48 h |
| Métrica secundária | 10 s em 48 h |
| N | 6 (é a amostra que fecha o Gate 2, não 8) |
| **Gate 2** | **≥3 dos 6** com `% média` > 50% |
| Situação em 27/10 | **2 de 3** (002 87,0%; 003 87,0%; 004 45,7%) |
| Leitura final | **29/10/2026** — 005 e 006 |

## Produção

| Item | Valor |
|---|---|
| Template | `templates/misterio-45/` (v1 congelado) |
| Episódios | `episodios/` na raiz (exceção: mover quebraria docs e commits) |
| Composição | gerada por `scripts/gerar-episodio.py` a partir de `roteiro.json` |
| Voz | take único + `remapear.py` (005) · cena por cena com `montar-voz.py` (006) |
| Duração | 45,000 s · 1080×1920 · 30 fps · H.264 + AAC |
| Loudness | −15,16 a −15,19 LUFS, TP entre −1,30 e −2,18 |

## Fontes e limites

- **Afirma:** o que está no processo, no laudo e no paper. Cada episódio tem
  `briefing.md` com as fontes numeradas.
- **Não afirma:** o que ninguém registrou (o que os tripulantes pensaram, o que
  houve com o Voo 19 depois da última transmissão).
- **Lenda marcada como lenda:** Triângulo das Bermudas, CROATOAN como mensagem
  sobrenatural, yeti/OVNI no Passo Dyatlov.
- **Nomes próprios para conferir na escuta:** por episódio, no `qa.md`.

## Riscos assumidos

- O nicho pode ser raso: a 1ª rodada do `scout.py` não achou máquina de breakout
  para copiar (`docs/ESCALA.md`).
- O visual depende de um gesto só (texto entrando e saindo). Pode ser o teto do
  formato — é o que o A/B do 007 vai atacar.
- Som praticamente inexistente nos 6 primeiros (drone a −51 LUFS, inaudível).
  Não foi testado ainda.

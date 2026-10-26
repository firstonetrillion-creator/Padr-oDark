# ESTADO — retomada por etapa

> **Arquivo de instrução do OpenCode** (`opencode.jsonc`). Atualizar a **cada passo**, não a cada etapa.
> Depois de uma compactação, a versão atual deste arquivo é relida do disco e vira a baseline da sessão.
> Memória longa continua em `MEMORIA.md`; aqui só o suficiente para retomar sem reler nada.

**Atualizado:** 2026-10-26 · **Sessão anterior:** análise do canal com login (público + 48 h do 004)

## Onde estamos

Fase 2, **4/6 publicados** (001–004). Episódio atual: **005 — Voo 19**.

## Episódio 005 — Voo 19

| Etapa | Estado |
|---|---|
| Briefing | **pronto** — fontes primárias validadas (Board of Investigation 1945, 56 achados) |
| Gancho | **aprovado** em 25/10/2026 |
| Roteiro | **pronto** — `111` palavras, **12 cenas** (2,5 palavras/s) |
| Voz → publicação | pendente |

**Gancho:** “Cinco aviões pediram socorro. Nenhum voltou. Nem o resgate.”
Capa: `27 HOMENS / NENHUM CORPO` (~39 s, cena 11).
Cena 2 **não** é cartão de contexto (regra pós-004): “O rádio funcionava. Eles
falavam com a base. Não sabiam onde estavam.”

**Próximo comando:** gerar a voz (`narracao_tts.txt`, `length_scale` a calibrar;
meta `voz_raw.wav` 43–44 s), depois transcrever e remapear os tempos reais.

## Episódio 004 — MV Joyita

| Etapa | Estado |
|---|---|
| Briefing / gancho / roteiro | prontos (`131` palavras, 13 cenas) |
| Voz | `voz_raw.wav` 44,117 s (ls 0.90) → `voz.wav` 45,000 s, **−21,63 LUFS**, TP −7,37 |
| Transcrição + remap | prontos (`transcricao.json`, 13 cenas) |
| Contrato | **OK, 0 avisos** |
| QA visual | **concluído** — frames 1–14 + `contact.png`; cena 6 em 4 linhas; frame 13 (fecho) em 2 linhas, sem overflow. frame 14 é só o fade e tem artefato de escala da captura. |
| Render | **concluído** — `final_raw.mp4` 45,000 s, −21,64 LUFS; 5 segmentos, 0 retries |
| QA / publicação | **publicado** em 24/10/2026 | https://youtube.com/shorts/rlSArCY3bH0 |

**Números finais:** `final.mp4` **45,013 s · 3.652.954 bytes · −15,16 LUFS · TP −1,42 dBFS**
(ganho +6,5 dB + limitador 0,85). SHA-256 `406906CE2F8AC652CCF33A828EF6E1E120CBD1A8EA9645ACAC5E8968BEA6EED7`.
Capa `capa.png` em 4,0 s (“25 PESSOAS / NENHUM SINAL”). Título com lint **100/100** (35 chars).

**Estado: publicado e verificado.** Aprovação humana em 24/10/2026; vídeo no ar
como Shorts público. Conferido: `availability=public`, `age_limit=0`,
`duration=45` (yt-dlp sem cookies) e selo **IA** visível na página pública.
Métricas iniciais: 276 views na primeira hora.

## Painel do Studio (relido em 26/10, com login)

| Métrica | 002 Mary Celeste | 003 Roanoke | 004 MV Joyita |
|---|---:|---:|---:|
| Views (48 h) | 234 | 370 | **1.200** |
| Ficaram para assistir | 48,6% | **53,0%** | **54,0%** |
| Duração média | 0:35 | **0:39** | **0:21** de 0:46 |
| % média assistida | 76,1% | **84,8%** | **45,7%** |
| Shorts feed | n/d | 92,2% | 98,9% |
| Espectadores únicos | n/d | n/d | **296** |

**Leitura:** o 004 não perdeu mais gente no gancho — “ficaram para assistir” é
até **um pouco maior** que no 003. Perdeu **no meio**: metade da duração média.
Isso reforça o slide e enfraquece a ideia de que o gancho piorou.

**Duas correções que a releitura trouxe:**

1. **A duração média escorrega com o tempo.** O 002 estava em 0:40 (87,0%) em
   25/10 e está em **0:35 (76,1%)** em 26/10; o 003 foi de 0:40 para 0:39. Cada
   view nova vem de feed mais frio. **O Gate 2 tem de usar janela fixa de 48 h.**
2. **O público real não é o imaginado.** 82,1% tem **55+** (zero abaixo de 45),
   78,2% masculino, 94,7% celular, e o **Brasil é só 49,2%** das views. Detalhe
   em `biblioteca/publico.md`.

## Scout de canais (novo em 26/10)

`scripts/scout.py` + `biblioteca/canais-semente.txt` — mede canais de Shorts que
estão **acelerando agora**. Fluxo invertido de propósito: **yt-dlp não descobre
canal** (não respeita filtro de busca), então o humano traz os canais e o script
mede. Segunda rodada com `--diff` dá views/dia real.

**Achado da 1ª rodada (12 canais do nicho):** só **1** tem volume (≥5k de
mediana) *e* aceleração (≥1,5×) — Wakinho, que é curiosidades, não arquivo.
Os que aceleram forte (Arquivo Sem Rastros 7×, De Olho 4×, Cofre dos Mistérios
2,5×) têm mediana de **44 a 297 views**: razão sem significância. Os que têm
volume estão parados ou caindo (Penumbroo **0,09×**, colapsando; Ossos Perdidos
1,0×). Só 3 passam de 0,5 views/inscrito.

**Leitura:** neste nicho, na amostra atual, **não há máquina de breakout para
copiar**. Ou o nicho é raso, ou os vencedores estão num nicho adjacente
(true crime / documentário), ou as sementes estão erradas.

Levantamento completo, com o raciocínio e os limites: **`docs/ESCALA.md`**.
Decisão registrada em `docs/DECISOES.md` e `docs/PLANO.md`. Ordem acordada em
26/10: **documentar → 005 → LAB 001 → gerador → A/B**. Nada de escalar o formato
antes do Gate 2.

## Laboratório (fora da fila, não publica)

`laboratorio/001-60s-fawcett/` — ensaio do **007**, com material barato.

| Item | Estado |
|---|---|
| Conceito | **pronto** — 4 variáveis, regra do trilho, critério de sucesso |
| Roteiro | **pronto** — `131` palavras, **16 cenas**, **60 s** (2,18 pal./s) |
| Narração | `narracao.txt` + `narracao_tts.txt` (148 tokens: números por extenso) |
| Voz | **pronta** — `voz_raw.wav` 59,999 s; `voz.wav` 60,000 s, −16,04 LUFS, TP −3,21 |
| Drone | **pronto** — gerado por lavfi (110/165 Hz + ruído), 60,000 s, −19,74 LUFS |
| Composição | **pronta** — 18 cenas (s8 e s10 divididas), contrato **OK, 1 aviso** |
| QA visual | **pendente** — métricas de texto medidas; falta frame |
| Render | **pendente** |

**Voz gerada por cena** (`build_voz.py`): 16 blocos sintetizados separados e
concatenados com silêncio ponderado → **46,76 s de fala + 13,24 s de silêncio
(22,1%)**. Um take único não daria respiro no meio.

**Descoberta:** o `drone.wav` do 004 está em **−51,3 LUFS** (a 0,16 vira −67 no
mix, inaudível). O bed do laboratório foi feito em −19,7 para ficar ~20 dB sob a
voz — ou seja, o 001–004 são praticamente voz seca.

**Armadilha nova:** `tremolo` exige `f ≥ 0.1`. E `-Duracao` foi adicionado a
`check-contrato.ps1` (padrão 45, nada muda para 001–006).

**Hipótese:** o que derruba o miolo não é a quantidade de texto, é o **estado
parado**. Por isso a contagem de palavras do teste é **idêntica à do 004 (131)** —
a diferença é tempo (60 s contra 45) e movimento (trilho de datas que anda).

**Tema:** Percy Fawcett, Mato Grosso, 1925 — também testa **assunto nacional**.

**Atenção:** 60 s = 1.800 frames, acima do limite de ~1.350 do Chrome; captura
segmentada obrigatória. Este teste **não** altera o v1 congelado do 003–006.

## Esperando (nada a fazer até as datas)

- ~~**2026-10-26** — retenção de 48 h do **004**~~ **feito**: painel relido com
  login em 26/10. Falta só o `Todos.csv` de curva (aba Content do Studio não
  carrega). Ver `episodios/004-mv-joyita/retencao.md`.
- Só depois disso decidir o 005. Regra nova: **nada de cartão parado de
  contexto depois do gancho**; contexto em ≤2 s ou colado a uma consequência.
- Leitura do 003: gancho melhorou (3 s e 10 s acima do 002), **mas o fim caiu**
  (36,1% vs 42,2%): slide de −32,4 p.p. entre 10 s e 44,5 s. Hipótese: a
  explicação do CROATOAN entregue cedo demais.

## Bloqueios e regras vivas

- **Aprovação é explícita por vídeo.** “publique” conta; “conclua” ou “vamos aguardar” não.
- Um render por vez; 1080×1920, 30 fps, H.264 + AAC.
- v1 congelado até o Gate 2: sem fonte/efeito novo.
- Alerta em `qa.md`: cena 2 é cartão estático de 6,57 s. Só dividir se a retenção do 003 pedir.
- `docs/PLANO.md` (correção da fonte 004 → Comissão NZ, Apia) commitado junto com o 004.
- **Gate 2 usa janela fixa de 48 h** para “% média assistida”. A duração média
  cai com o tempo (002: 87,0% → 76,1% em um dia), então medir em datas
  diferentes compara públicos diferentes.
- **Público medido (26/10):** 82,1% com 55+, 0% abaixo de 45, 78,2% masculino,
  94,7% celular, Brasil só **49,2%**. Ver `biblioteca/publico.md`. Registrar a
  mesma leitura no 005: se repetir em dois vídeos, é o canal; se não, é o vídeo.
- **Studio Análises:** abre em branco / “Oops” na primeira carga. Funciona assim: abrir
  `.../video/<id>/analytics/tab-overview/period-default?hl=en&cb=<timestamp>`, esperar e
  **recarregar até o card “Audience retention” aparecer** (1–3 tentativas). O que o card
  entrega: “Stayed to watch”, “Average view duration” e views. **% média assistida =
  duração média ÷ 46 s** (validado pelo 002: 0:40 → 87,0%).
  **A aba Content (tabela por vídeo) e a lista de vídeos nunca carregam** — puxar
  vídeo a vídeo. **Reach/Audience** só abrem clicando no `TP-YT-PAPER-TAB`, não por URL.

## Compactação

- Compactar **entre etapas**, não no meio: `opencode api post /api/session/<id>/compact --data '{}'`.
- Antes de compactar: atualizar este arquivo e commitar o que for durável.
- Saídas grandes (frames, logs, HTML) vão para arquivo; no chat, só o resumo.

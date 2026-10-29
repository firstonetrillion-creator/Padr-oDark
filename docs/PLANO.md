# Plano 30 / 60 / 90

## Fases e gates

| Fase | Prazo | Entrega | Gate |
|---|---|---|---|
| **0. Cérebro** | 2 dias | Node, FFmpeg, Python, Piper, HyperFrames instalados; benchmark medido | Short de 45 s renderiza em < 12 min |
| **1. Piloto** | 7 dias | Identidade + template Mistério 45 + 1 vídeo completo | Vídeo aprovado por você |
| **2. Validação** | 14 dias | 6 vídeos de Mistério 45 (piloto + 5) | Retenção média > 40% em 3 vídeos |
| **3. Repetição** | 30 dias | 30 shorts + 1 longo de 8 min | Retenção > 45% e tempo estável |
| **4. Serviço** | 60 dias | Kit + oferta mensal | 1 cliente pagante |

> **G0 medido em 20/10/2026:** 45 s em 1080×1920 renderizados em **2m32,8s** (158,8 s incluindo doctor e probe). Gate **PASS**. A máquina aguenta o formato; o gargalo agora é conteúdo, não render.

> **Fase 1 concluída e Fase 2 iniciada (21/10/2026):** piloto `001-faroleiros` — 13 cenas, 45,01 s, QA técnico **PASS** (−15,6 LUFS), template `misterio-45` extraído e **vídeo aprovado pelo usuário** (“ficou perfeito”). Piloto **publicado no YouTube Shorts**: https://youtube.com/shorts/WKuNVjl3d5M. **Estado em 23/10/2026:** 3/6 publicados; 003 publicado; faltam 004–006.

> **Nicho decidido em 21/10/2026:** Mistério/Arquivo é a âncora (0,10 views/inscrito por canal vs 0,06 da psicologia; 3 canais ≥1,0 vs 0). A validação passa a ser **6 vídeos de mistério** (piloto + 5), no canal **Dossiê 45** (`@Dossie45`). O rebranding visual está no ar; nome, descrição do canal e deslistagem dos 9 shorts antigos concluídos. O **002-mary-celeste** foi publicado em 21/10/2026. Psicologia fica como fallback em canal novo se a retenção falhar. Dados em `docs/NICHO.md`; decisão em `docs/DECISOES.md`.

## Execução imediata (a partir de 23/10/2026)

### Gate 1 — 23/10: retenção do 001 e do 002

- [x] Baixar o CSV de retenção do Studio para 001 e 002. O 002 veio com curva; o 001 veio vazio (sem dados).
- [x] Rodar `tools/youtube-agent-skill/yt-retention/retention.py --duration 45` nos dois arquivos. O parser foi ajustado para retenção absoluta (>100%).
- [x] Preencher `biblioteca/publicados.csv` com o que existe; salvos, compartilhados e conclusão ficam `n/d`.
- [x] Criar `episodios/001-faroleiros/retencao.md` e `episodios/002-mary-celeste/retencao.md`.
- [x] Decidir: **manter** o formato, com **ajuste de gancho** no 003. O 002 passou 3 s (91,6%) e 10 s (61,8%); o 001 ficou em 24,3% de retenção inicial e sem curva.

### 003 — publicado (23/10/2026)

- [x] Gancho aprovado, roteiro de 113 palavras e `narracao.txt`.
- [x] Voz, transcrição, composição v1, contrato e QA visual.
- [x] Render segmentado, normalização para ~−15,4 LUFS e QA técnico **PASS**.
- [x] Marca corrigida para `DOSSIÊ 45` e vídeo re-renderizado.
- [x] Aprovação humana do `final.mp4` (23/10/2026).
- [x] Publicação no YouTube Shorts — https://youtube.com/shorts/8ptxqKGe4Bk.
- [ ] Retenção em 48 h — **medida em 25/10/2026**: 3 s 92,7%, 10 s 68,5%, fim 36,1%; falta a porcentagem visualizada média do painel.

### Fila 003–006

A fila foi confirmada após o Gate 1 (23/10). Alvo: **1 vídeo a cada 2–3 dias**,
mantendo aprovação humana antes de publicar. Datas revisadas em **25/10/2026**
com o ritmo real (o 003 saiu 1 dia antes e o 004, 3 dias antes do previsto).

| Ordem | Janela real | Tema | Fonte principal | Ângulo | Status |
|---|---|---|---|---|---|
| 003 | **23/10** (feito) | Colônia de Roanoke (1590) | *The Roanoke Voyages, 1584–1590* (David Beers Quinn, Hakluyt Society); registros do Fort Raleigh/NPS | Cerca de 117 colonos desapareceram; “CROATOAN” é a pista documentada. O que os registros permitem concluir — e o que é lenda. | **publicado** em 23/10/2026; medido em 25/10 |
| 004 | **24/10** (feito) | MV Joyita (1955) | Comissão de Inquérito da Nova Zelândia em Apia (1956), relatório C. C. Marsack; Archives NZ IT1/23579122; David G. Wright, *Joyita: Solving the Mystery* | 25 pessoas desapareceram; o barco foi achado à deriva, meio submerso. O que o inquérito documenta e o que continua em aberto. | **publicado** em 24/10/2026; 24 h medido, 48 h em 26/10 |
| 005 | **26–28/10** | Voo 19 (1945) | Relatório do Board of Inquiry da Marinha dos EUA (1945); Naval History and Heritage Command | Cinco aviões e 14 homens sem destroço. O que o relatório diz — e o que a lenda do Triângulo das Bermudas acrescentou. | **em produção**; fontes a validar |
| 006 | **29–31/10** | Passo Dyatlov (1959) | Investigação soviética (1959); Gaume & Puzrin, *Communications Earth & Environment* (2021) | Nove caminhantes, uma barraca cortada por dentro e lesões graves. O que o inquérito registrou e o que a ciência propôs. | candidato; validar fontes |

### Gate 2 — 48 h após o 006 (≈ 01–02/11/2026)

**Critério decidível** (substitui “retenção média > 40% em 3 vídeos”, que não
discrimina — ver nota abaixo):

- **Principal:** **≥ 3 dos 6** vídeos com **% média assistida > 50%**
  (duração média ÷ duração do painel; 003 = 0:40/0:46 = 87,0%).
- **Guarda-corpo 1:** mediana de **10 s ≥ 50%**.
- **Guarda-corpo 2:** mediana do **fim da curva ≥ 30%**.
- **Regra de amostra:** vídeo sem curva de retenção **não entra** nem no
  numerador nem no denominador (foi o caso do 001).
- **Janela fixa:** “% média assistida” é lida **48 h após a publicação**, e só.
  A duração média cai com o tempo (002: 87,0% em 25/10 → **76,1%** em 26/10;
  003: 87,0% → **84,8%**), porque cada view nova vem de feed mais frio. Medir em
  datas diferentes compara públicos diferentes.
- **Se falhar:** a Fase 3 não escala. O v2 visual vira teste de recuperação
  (007) e a Psicologia sombria volta como fallback em canal novo.

> **Por que 50% e não 40%:** com 002 (87,0%), 003 (87,0%) e 004 (45,7%), o piso
> de 40% **já estaria cumprido hoje com 3 de 4 vídeos** — um gate que não pode
> falhar não é gate. E o 004 mostra por que o número do painel sozinho engana:
> média 45,7% com **fim de curva em 17,3%**. Daí os dois guarda-corpos.

## Fase 3 — lote 007–011 (aprovado em 2026-10-29)

**Estado: aprovado pelo usuário em 29/10/2026. Nada produzido ainda.** É a fila
imediata do canal único (Dossiê 45).

### O que o lote testa

O Gate 2 mostrou onde está o furo: **o primeiro segundo**, não o miolo.

| Vídeo | Cartões | Ficaram para assistir | `% média` |
|---|---:|---:|---:|
| 005 (12 cartões, ≤5 s, gerado do JSON) | 12 | **46,5%** | **54,3%** |
| 006 (14 cartões, mesmo visual) | 14 | **38,2%** | 50,0% |

O 005 abre com ação (“Cinco aviões pediram socorro”); o 006 abre com contexto
(“Eles cortaram a encosta para dormir”) e perde 8,3 p.p. de “ficaram”.

- **A variável única do lote é o gancho:** o primeiro segundo abre com **ação ou
  consequência**, nunca com contexto, data ou apresentação.
- **Fica igual ao 005:** 45 s, **12 cartões**, nenhum acima de 5 s, 1 ideia por
  cartão, sem cartão de contexto depois do gancho, fecho com consequência nova,
  v1 tipográfico, Piper `pt_BR-faber-medium`, 1080×1920 · 30 fps · H.264 + AAC,
  ~−15 LUFS, 2,5 pal./s.
- **Hipótese:** mediana de “ficaram para assistir” **≥ 46,5%** e mediana de
  `% média` **> 54,3%** nos 5 vídeos.
- **Critério de decisão (depois do 011, 48 h):**
  - **Adotar a regra** e escalar para os 30 shorts da Fase 3, se as duas medianas
    passarem.
  - **Se só uma passar:** o gancho não é a alavanca sozinho — a próxima variável
    é **ritmo/visual**, e aí sim o LAB 002 (layouts) entra.
  - **Se nenhuma passar:** o problema não é gancho nem miolo; reavaliar formato
    (45 s é curto?) antes de produzir mais.

### Cadência e horário (constantes, não variáveis)

- **1 vídeo por dia, 19h de Brasília, segunda a sexta.** Slot **fixo** durante o
  lote: com 5 vídeos não se testa horário (confunde com dia da semana e com o
  próprio gancho). Fixar é remover ruído, não otimizar.
- Não temos dado de horário. O que se sabe: Shorts feed foi **92,2%** das views
  do 003 e **98,9%** do 004 — o feed não respeita horário. No 005 o search já
  pesou **28,6%**, e aí horário pesa.
- **Upload é do usuário** (agendamento manual no Studio). Automação de publicação
  continua fora até depois do gate 3.

### Os 5 temas aprovados

Cada um precisa de `briefing.md` com **fontes numeradas** antes do roteiro.
Gancho = o que aparece no primeiro segundo.

| # | Slug sugerido | Tema | Gancho (1º segundo) | Fontes primárias |
|---|---|---|---|---|
| **007** | `007-homem-de-somerton` | Homem de Somerton (Adelaide, 1948) | “Um homem morto na praia. Um código costurado na roupa.” | Inquérito da polícia da Austrália do Sul (1949); identificação por genealogia genética — Univ. de Adelaide (2022) |
| **008** | `008-max-headroom` | Invasão Max Headroom (Chicago, 1987) | “Dois canais de TV foram invadidos ao vivo. Ninguém foi preso.” | Registros da FCC; transmissões da WGN-TV e WTTW (22/11/1987) |
| **009** | `009-mascaras-de-chumbo` | Máscaras de chumbo (Morro do Vintém, 1966) | “Dois homens mortos no morro. Máscaras de chumbo. Nenhuma marca.” | Inquérito da polícia do Rio; laudos do IML; imprensa de 1966 — **assunto nacional** |
| **010** | `010-carroll-a-deering` | Carroll A. Deering (1921) | “O navio apareceu vazio. E a comida ainda estava na mesa.” | Inquérito do Departamento de Comércio dos EUA (1922); Guarda Costeira |
| **011** | `011-ss-baychimo` | SS Baychimo (1931–1969) | “Abandonaram o navio no gelo. Ele navegou 38 anos sozinho.” | Registros da Hudson's Bay Company; relatos de avistamento 1931–1969 |

**Reservas aprovadas como troca:** Hinterkaifeck (1922), Mulher de Isdal (1970),
Yuba County Five (1978), Voynich (Yale, MS 408).

**Títulos sugeridos** (≤60 caracteres, sujeitos ao lint `title.py` antes de publicar):

| # | Título | Chars |
|---|---|---:|
| 007 | `Somerton: o homem sem nome por 74 anos` | 38 |
| 008 | `Max Headroom: a TV invadida que ninguém explicou` | 48 |
| 009 | `Máscaras de chumbo: dois mortos sem uma marca` | 45 |
| 010 | `Carroll Deering: o navio que voltou sem ninguém` | 47 |
| 011 | `Baychimo: o navio que navegou 38 anos sozinho` | 45 |

**Cuidados de fonte, declarados antes do roteiro:**
- **Deering:** é ligado ao Triângulo das Bermudas por literatura posterior; o
  inquérito de 1922 **não** sustenta isso. Se a lenda entrar, entra marcada.
- **Máscaras de chumbo:** o bilhete (“16:30… engolir cápsula… aguardar sinal”) é
  documento do inquérito; a **interpretação** (contato, OVNI, seita) não é.
- **Max Headroom:** o mais recente da série; se o canal ficar só em casos antigos,
  trocar por Hinterkaifeck.
- **Somerton:** a identificação de 2022 é resultado de pesquisa, não laudo
  oficial — dizer “identificado por genealogia genética”, não “caso resolvido”.

### Custo e ordem de execução

| Item | Valor |
|---|---|
| Episódio completo (com o gerador) | ~2 h |
| Lote de 5 | **~10 h** (≈6 h só de briefing/fonte) |
| Render | 5 × ~3 min, **um por vez** |
| Ciclo por vídeo | briefing → gancho → `roteiro.json` → `gerar-episodio.py` → `medir-texto.ps1` → voz (`montar-voz.py`) → contrato → render → `qa.ps1` → **aprovação humana** → upload → 48 h |

```powershell
# próximo comando, por episódio
.\scripts\novo-episodio.ps1 007-homem-de-somerton "Somerton: o homem sem nome por 74 anos"
```

**Regra que não muda:** aprovação humana **por vídeo**, explícita. Aprovar o lote
(29/10) é aprovar os temas, não autorizar publicação.

## Escala e aceleração — decisão de 26/10/2026

Levantamento completo em **`docs/ESCALA.md`**. Resumo:

- **Modelar canais que crescem copia o pacote visível** (duração, frame 0, texto
  por cartão, tema, série, título) e **não copia** curva de retenção, ritmo de
  revelação nem desenho sonoro — que é justamente onde o canal perde.
- **Views não são o modelo.** O 004 teve 3× as views do 003 e metade da
  retenção. O único proxy externo de retenção é o algoritmo insistindo
  (views/inscrito, breakout, aceleração).
- **1ª rodada do `scripts/scout.py` (12 canais):** nenhum combina volume e
  aceleração no nicho de arquivo. Quem acelera tem mediana de 44–297 views
  (ruído); quem tem volume está parado ou caindo (Penumbroo 0,09×).
- **O gargalo não é ideia, é vazão:** 4 vídeos em 6 dias ≈ 2 dias por vídeo;
  sinal estatístico exige 20–30 curvas ≈ 2 meses na cadência atual.
- **O que multiplica por 10:** episódio vira dado (`roteiro.json`) e um gerador
  emite `index.html` + tempos. Um vídeo vira ~2 h, e o A/B passa de 1 teste
  caro para 5 variantes na mesma semana.

**Ordem acordada:** documentar → **005** → LAB 001 → gerador → A/B.
**Não** escalar o formato antes do Gate 2.

---

## Melhorias visuais - backlog pós-validação

**Status: não iniciar agora.** A prioridade é validar os 6 vídeos e a retenção. O formato v1 (type-only) fica **congelado no 003–006** para não contaminar a comparação. O v2 entra depois do Gate 2, em um vídeo de teste (007) ou numa nova temporada.

### Diagnóstico
- O visual v1 é limpo, mas depende de um único gesto (texto entrando/sumindo); pode parecer “letras passando”.
- O ganho não está em trocar o HyperFrames; está em direção de arte, composição e evidência visual.

### Backlog v2 (avaliar após o Gate 2)
- 5–6 layouts: capa de dossiê, documento, mapa/rota, número, cronologia, prova e fecho.
- Tipografia como imagem: palavra gigante, corte pela borda, espaço negativo, camadas de texto.
- Textura: papel, grão, scanlines, vinheta, carimbo e faixas de redação.
- Provas visuais: mapas, recortes, documentos e fotos de domínio público, com fonte e licença registradas.
- Movimento intencional: zoom lento, parallax, máscara e carimbo; não apenas slide.
- Sound design: drone, impactos secos, papel, máquina de escrever e silêncio antes do twist.
- Capa/key art que funcione parada no feed.
- Um “frame de impacto” a cada 5–7 s.

### Critérios para adotar
- [ ] Ter fechado os 6 vídeos e o Gate 2.
- [ ] Testar em **1 vídeo A/B**, não reformar todos de uma vez.
- [ ] Comparar retenção 3 s/10 s e média com o v1; não decidir por gosto.
- [ ] Medir tempo de produção e RAM; se passar de 90 min/vídeo, recuar.

### Fora de escopo
- WebGL/Three.js, ReelMimic, OpenMontage e automação de publicação antes do gate 3.
- Trocar voz/TTS junto com o visual: uma variável por vez.

## Capacidade desta máquina

| Produção | Volume |
|---|---|
| Shorts 1080×1920, 45 s | 5–7/semana |
| Longo 8 min (a partir de shorts) | 1/semana (render noturno) |
| Render total | 2–4 h/semana |

## Rotina semanal

- Segunda: 10 ganchos + aprovação
- Terça/quarta: 3 roteiros + shotlists
- Quinta: vozes + assets
- Sexta: 3 renders + QA
- Sábado: publicação + planilha
- Domingo: análise e ajuste de gancho

## Métricas (planilha semanal)

Retenção 3 s · retenção média · conclusão · salvamentos · compartilhamentos · seguidores por vídeo.
Views e likes não decidem nada.

## Critérios de kill

- 10 vídeos sem nenhum > 40% de retenção → reescrever hooks
- 30 vídeos sem tração → trocar nicho
- > 90 min por vídeo → refazer template
- 60 dias sem cliente → reposicionar oferta

## O que NÃO entra antes do gate 3

- OpenMontage completo
- Hermes3D
- Remotion
- Automação de publicação
- Longos de 15+ min

> `codebase-memory-mcp` foi liberado após o primeiro vídeo publicado (21/10/2026); instalar fora de janela de render.

## Ferramentas de análise — youtube-agent-skill

Decisão de 21/10/2026: **adoção seletiva**, com vendor em
`tools/youtube-agent-skill/` e licença MIT preservada. O pack inteiro não foi
instalado e não substitui HyperFrames, Piper ou FFmpeg.

| Peça | Estado | Uso |
|---|---|---|
| `yt-retention/retention.py` | **adotado com patch** | CSV do Studio; 3 s e 10 s para Shorts, 30 s como legado; quedas + slide. |
| `yt-script/hooks.json` | **adotado como checklist** | Fonte das 21 fórmulas; adaptação PT-BR em `docs/GANCHOS-21.md`. |
| `yt-package/title.py` | **adotado com patch** | Lint de título + thumbnail em PT-BR. |

**Adiado para depois dos 6 vídeos:**
- `yt-viral/swipe.py` — rankeia por múltiplo sobre a mediana do canal, mas exige
  4+ vídeos por canal. Nossa amostra tem muitos canais com 1–5; o `nicho.py` já
  cobre a comparação por canal. Reavaliar quando houver mais dados.
- `yt-audit` — auditoria de canal que termina em uma correção. Faz mais sentido
  com 6+ vídeos publicados e o canal já limpo.

**Não adotado agora:** `yt-edit`, `yt-shorts`, `yt-chapters`, `yt-comment`,
`yt-plan`, `yt-seo`. Motivos em `tools/youtube-agent-skill/ORIGEM.md`.

**Não usar `hookscore.py` em PT-BR:** a heurística é em inglês e não foi
calibrada para o formato. As 21 fórmulas valem como checklist, não como score.

## Definição de pronto (por vídeo)

Ver [QA.md](QA.md).

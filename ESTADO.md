# ESTADO — retomada por etapa

> **Arquivo de instrução do OpenCode** (`opencode.jsonc`). Atualizar a **cada passo**, não a cada etapa.
> Depois de uma compactação, a versão atual deste arquivo é relida do disco e vira a baseline da sessão.
> Memória longa continua em `MEMORIA.md`; aqui só o suficiente para retomar sem reler nada.

**Atualizado:** 2026-10-25 · **Sessão anterior:** retenção de 24 h do 004

## Onde estamos

Fase 2, **4/6 publicados** (001–004). Episódio atual: **005 — Voo 19**.

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

## Esperando (nada a fazer até as datas)

- **003 medido (25/10):** 3 s **92,7%**, 10 s **68,5%**, fim **36,1%**; 370 views,
  +1 inscrito. Registro em `episodios/003-roanoke/retencao.md` e em
  `publicados.csv`. **Falta** a “porcentagem visualizada média” do painel
  (o 002 registrou 87,0%).
- **2026-10-26** — retenção de 48 h do **004**. Já medido em **24 h**: 3 s
  **90,9%**, 10 s **43,4%** (abaixo da meta), fim **17,3%**, 1.066 views.
  O colapso está na **cena 2** (cartão estático de 6,57 s com data/origem/
  número): −5,4 p.p. em 7,2–7,7 s. Ver `episodios/004-mv-joyita/retencao.md`.
- Só depois disso decidir o 005. Regra nova: **nada de cartão parado de
  contexto depois do gancho**; contexto em ≤2 s ou colado a uma consequência.
- Só depois disso decidir o 005. Leitura do 003: gancho melhorou (3 s e 10 s
  acima do 002), **mas o fim caiu** (36,1% vs 42,2%): slide de −32,4 p.p. entre
  10 s e 44,5 s. Hipótese: a explicação do CROATOAN entregue cedo demais.

## Bloqueios e regras vivas

- **Aprovação é explícita por vídeo.** “publique” conta; “conclua” ou “vamos aguardar” não.
- Um render por vez; 1080×1920, 30 fps, H.264 + AAC.
- v1 congelado até o Gate 2: sem fonte/efeito novo.
- Alerta em `qa.md`: cena 2 é cartão estático de 6,57 s. Só dividir se a retenção do 003 pedir.
- `docs/PLANO.md` (correção da fonte 004 → Comissão NZ, Apia) commitado junto com o 004.

## Compactação

- Compactar **entre etapas**, não no meio: `opencode api post /api/session/<id>/compact --data '{}'`.
- Antes de compactar: atualizar este arquivo e commitar o que for durável.
- Saídas grandes (frames, logs, HTML) vão para arquivo; no chat, só o resumo.

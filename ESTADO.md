# ESTADO — retomada por etapa

> **Arquivo de instrução do OpenCode** (`opencode.jsonc`). Atualizar a **cada passo**, não a cada etapa.
> Depois de uma compactação, a versão atual deste arquivo é relida do disco e vira a baseline da sessão.
> Memória longa continua em `MEMORIA.md`; aqui só o suficiente para retomar sem reler nada.

**Atualizado:** 2026-10-23 · **Sessão anterior:** compactada

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

**Estado: publicado.** Aprovação humana registrada em 24/10/2026; vídeo no ar
como Shorts público, com **AI use = Yes**.

## Publicado (004)

- URL: https://youtube.com/shorts/rlSArCY3bH0
- Retenção de 48 h: medir em **26/10/2026** → `biblioteca/publicados.csv` + `retencao.md`.
- Próximo: abrir o **005 — Voo 19** com `scripts/novo-episodio.ps1`, validando as
  fontes do Board of Inquiry (1945) e do Naval History and Heritage Command.

## Fila

- **2026-10-25:** retenção de 48 h do **003** → `biblioteca/publicados.csv` + `retencao.md`.
- **2026-10-26:** retenção de 48 h do **004**.
- **005** Voo 19 · **006** Passo Dyatlov (mesmo padrão de fontes do 003/004).

## Bloqueios e regras vivas

- **Não publicar sem “Aprovado — publicar”.** A frase “conclua e vamos aguardar” **não** é aprovação.
- Um render por vez; 1080×1920, 30 fps, H.264 + AAC.
- v1 congelado até o Gate 2: sem fonte/efeito novo.
- Alerta em `qa.md`: cena 2 é cartão estático de 6,57 s. Só dividir se a retenção do 003 pedir.
- `docs/PLANO.md` (correção da fonte 004 → Comissão NZ, Apia) commitado junto com o 004.

## Compactação

- Compactar **entre etapas**, não no meio: `opencode api post /api/session/<id>/compact --data '{}'`.
- Antes de compactar: atualizar este arquivo e commitar o que for durável.
- Saídas grandes (frames, logs, HTML) vão para arquivo; no chat, só o resumo.

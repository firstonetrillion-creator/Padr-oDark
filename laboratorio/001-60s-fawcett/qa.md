# QA — LAB 001 (Fawcett, 60 s)

**Data:** 2026-10-26
**Arquivo:** `final.mp4`
**Render:** standard, 1080×1920, 30 fps, segmentado 6×300 frames, 1 worker,
low-memory; 1800/1800 frames, 0 retries, 5 reciclagens (4m03s)
**Duração:** 60,010 s · **Tamanho:** 4.652.077 bytes (4,65 MB)
**Voz:** `build_voz.py` — 16 blocos separados, 46,76 s de fala + 13,24 s de
silêncio; `voz.wav` 60,000 s, −16,04 LUFS, TP −3,21
**SHA-256 (`final.mp4`):** `71A48162BDF327DB68EC4E2C10B50DFFA69DC64256C1B5BDE1BA2147606F6739`

## Técnico

| Item | Medição | Status |
|---|---|---|
| Codec de vídeo | H.264, 1080×1920 | OK |
| FPS | 30/1 constante | OK |
| Áudio | AAC 48 kHz, estéreo | OK |
| Loudness | −15,16 LUFS (cru: −16,04; ganho **+0,9 dB**) | OK |
| Pico | true peak −1,93 dBFS | OK |
| LRA | 3,70 LU (o 005 tem 2,20 — o laboratório respira mais) | OK |
| Preto inesperado | nenhum; fade final em 58,9–59,9 s | OK |
| Texto cortado | 18 cenas conferidas em frame; nenhuma passa de x=960 | OK |
| Linha mais larga | **826 px de 840** (s8a, "UM EXPLORADOR VOLTOU.") | OK |
| Contrato | `check-contrato.ps1 -Duracao 60` — OK, 1 aviso (18 cenas) | OK |
| QA automático | `qa.ps1 -Duracao 60` | **PASS** |
| Marca | `DOSSIÊ 45 · LAB` / `ARQUIVO 01` | OK |

## Três correções feitas antes do render

Medido no frame real (tinta, não caixa):

| Cena | Problema | Correção | Resultado |
|---|---|---|---|
| s5 | 882 px até x=1004 (44 px fora) | 96 → **90 px** | 825 px |
| s8a | 878 px até x=999 | 104 → **98 px** | 826 px |
| s1 | 840 px (no limite) | 90 → **88 px** | 787 px |

## O bug que quase matou o experimento

O marcador do trilho — que **é** a variável do teste — estava escrito assim:

```js
tl.fromTo(mk, { opacity: 0.15 }, { opacity: 1, duration: .28, repeat: 1, yoyo: true }, 0.15);
```

`fromTo` com `yoyo` **termina no valor de partida**: o marcador ficava a 15% de
opacidade pelo vídeo inteiro. O 1º render mediu cor `(33,10,9)`; o correto é
`(178,58,46)`. Trocado por `tl.to(mk, { opacity: .15, yoyo: true, repeat: 1 })`,
que parte de 1 e volta para 1. O marcador também foi de 2 → 3 px, com ponto de
8 → 10 px, para sobreviver à tela de um celular.

Posições medidas no `final.mp4` (x dentro do trilho, 120→960):

| t | 3 s | 12 s | 24 s | 36 s | 48 s | 57 s |
|---|---:|---:|---:|---:|---:|---:|
| x | 122 | 110 | 330 | 540 | 124 | 958 |

A ida a 110 (levemente fora do trilho, antes de 1925) e a volta a 124 são
intencionais: o mapa manda −12 em s4 e −6 em s14 para dizer "antes de 1925".

## Editorial

- [x] Gancho em 0,0 s: "ELE LEVOU O PRÓPRIO FILHO PARA A SELVA. NENHUM DOS DOIS VOLTOU."
- [x] **131 palavras faladas** — idêntico ao 004, de propósito: a variável é tempo
  (60 s contra 45) e movimento, não quantidade de texto
- [x] 18 cenas; nenhuma acima de 4 linhas
- [x] Fatos com fonte: Royal Geographical Society (1927), relatos de Orlando
  Villas Bôas, correspondência de Fawcett, laudo de 1951
- [x] "OS KALAPALO CONTAM" / "É ELE." marcam os relatos como relatos
- [x] Nenhuma imagem, áudio ou vídeo de terceiros
- [ ] **Escuta humana** pendente (o laboratório não publica no canal principal)

## Por que este arquivo existe

O LAB 001 testa uma hipótese que o Gate 2 não responde: **o que derruba o miolo
é texto ou é estado parado?** O 004 perdeu metade da duração média com cena
estática de 6,57 s. Aqui o texto é o mesmo do 004 e todas as cenas têm o trilho
andando. Se a retenção do 60 s segurar melhor que 45,7% do 004, a resposta é
movimento — e isso vira a variável do A/B do 007.

Vai para o **canal descartável**, não para o Dossiê 45.

# ARQUITETURA — Padrao-Dark

> **Memória de código.** Este arquivo registra os contratos que fazem o pipeline funcionar e o que cada parte já entregou.
> Se você mudar um contrato, atualize este arquivo no mesmo commit/etapa.
> Última atualização: **2026-10-21**.

## 1. Visão geral

```
narracao.txt
   │  scripts/tts.py (Piper)
   ▼
voz_raw.wav ──► voz.wav (45,00 s, processada)
   │  scripts/transcribe.py (faster-whisper)
   ▼
transcricao.json (tempos por palavra)
   │  mapeamento manual frase → cena
   ▼
index.html (HyperFrames + GSAP, 13 cenas)
   │  hyperframes render (segmentado)
   ▼
final_raw.mp4 ──► FFmpeg (ganho + limitador) ──► final.mp4
   │  scripts/qa.ps1
   ▼
qa.md assinado ──► cópia de publicação + capa
```

O vídeo é **tipográfico**: não há assets de imagem/vídeo. O texto é a imagem.

## 2. Contrato da composição

Arquivo de referência: `episodios/001-faroleiros/index.html` (idêntico ao template, exceto conteúdo).

### 2.1 Raiz

```html
<div id="stage"
     data-composition-id="ep001"
     data-start="0"
     data-width="1080"
     data-height="1920"
     data-fps="30">
```

- Tamanho fixo **1080×1920**, 30 fps, 45 s.
- `#stage` tem `overflow: hidden` e fundo `#0A0A0B`.
- Elementos fixos: `.bg` (gradiente + zoom lento), `.vignette`, `.frame`, `.mark` (marca), `.dossier` (número), `.foot` (fonte).

### 2.2 Cenas

Cada cena é um `<section class="scene clip">` com:

| Atributo | Função |
|---|---|
| `id` | alvo do GSAP (ex.: `s1`, `s5b`) |
| `data-start` | segundo em que a cena entra |
| `data-duration` | duração em segundos |
| `data-track-index="1"` | trilha das cenas |

**Regra crítica:** a timeline GSAP esconde e mostra cada cena com `autoAlpha`:

```js
tl.set(root, { autoAlpha: 0 }, 0);
tl.set(root, { autoAlpha: 1 }, start);
tl.set(root, { autoAlpha: 0 }, start + dur);
```

Sem isso, o texto da cena continua com `opacity: 1` depois do fim e aparece como **fantasma** sobre as cenas seguintes (o HyperFrames só controla a visibilidade do clip, não a opacidade interna).

A entrada do `<h1>` é `from({ opacity: 0, y: 36, duration: 0.55 })`, com variantes para `.kicker`, `.small` e `.accent`.

### 2.3 Áudio

```html
<audio id="voz"   data-start="0" data-duration="45" data-track-index="0" data-volume="1"    src="voz.wav"></audio>
<audio id="drone" data-start="0" data-duration="45" data-track-index="2" data-volume="0.16" src="drone.wav"></audio>
```

- Os **ids são obrigatórios**: sem `id="voz"`/`id="drone"` o render sai mudo.
- `voz.wav` e `drone.wav` precisam ter **45,00 s**.
- A voz domina; o drone entra a 0,16.

### 2.4 Timeline e fade

```js
const tl = gsap.timeline({ paused: true });
window.__timelines = { ep001: tl };
tl.to("#fade", { opacity: 1, duration: 0.7 }, 44.3);
```

- A timeline é pausada; o HyperFrames a controla no render.
- `window.__timelines.ep001` é o ponto de montagem do runtime.
- `#fade` cobre os últimos 0,7 s (fade para preto).

### 2.5 QA por `?t=`

```js
const seek = new URLSearchParams(location.search).get("t");
if (seek !== null) { tl.time(t, false); /* visibility das cenas */ }
```

- Abrir `index.html?t=12.5` congela a timeline em 12,5 s.
- Serve para screenshot de QA **sem renderizar**.
- Não afeta o render normal (sem query string).

## 3. Contrato de tempo (fala → cena)

Há dois caminhos, e a diferença é **onde o tempo nasce**.

### 3.1 Take único + ASR (001–005)

1. `transcricao.json` traz `segments[].start/end` e `words[].start/end`.
2. Para cada frase, definir a cena correspondente.
3. `data-start` = `start` da frase − 0,05 s.
4. `data-duration` = `start` da próxima cena − `data-start` − 0,05 s.
5. A última cena cobre até 45,00 s.
6. Frases longas (> 4 s) podem ser divididas na pausa natural; foi o caso de “Não havia ninguém” + “A porta estava fechada” (s5 e s5b).
7. Sempre conferir o frame do meio de cada cena com `?t=`.

**Limite do método:** o tempo é **inferido** por reconhecimento de fala. Se o ASR
erra a palavra, ele erra a fronteira. No 006, “cortam um degrau” saiu como “Cota
o mundo legal” (28% dos tokens errados) e a cena 4 ficou **1,4 s** fora. A tabela
do `remapear.py` não avisa — ela mostra o texto certo com o tempo errado.

### 3.2 Cena por cena + concatenação (006 em diante, quando o ASR falha)

`scripts/montar-voz.py` sintetiza cada parágrafo de `narracao_tts.txt` separado,
corta o silêncio das pontas, e concatena com silêncio calculado. O tempo passa a
ser **exato por construção**:

| Passo | Regra |
|---|---|
| Bloco | um parágrafo = uma cena; a contagem tem de bater com `roteiro.json` |
| Silêncio | `duração − fala − inicio − fim`, dividido entre as fronteiras por `--pesos` |
| `start` | `fala − 0,05` (cena 1 em 0; a cena entra antes da fala) |
| `duration` | próxima `fala` − `start` − 0,05; última fecha a duração |
| Respiro inicial | `--inicio` (0,6 s padrão) fica **dentro** do `voz_raw.wav` |

Consequência prática: o FFmpeg **não** leva `adelay` — o atraso já está no áudio.
Se a fala não couber, o script aborta e imprime o `--length-scale` a usar.

Trade-off: a prosódia reinicia a cada bloco. Para cartões de 2–5 s é respiro;
para raciocínio contínuo, o take único soa melhor.


## 4. Contrato de render

| Etapa | Comando/arquivo | Saída |
|---|---|---|
| Render bruto | `hyperframes render --output final_raw.mp4 --quality standard --fps 30 --workers 1 --low-memory-mode --protocol-timeout 600000 --resume` | `final_raw.mp4` |
| Captura segmentada | `HF_SEGMENTED_CAPTURE=true`, `HF_SEGMENT_FRAMES=300`, `HF_SEGMENT_BROWSER_RECYCLE=1` | 5 segmentos concatenados |
| Normalização | `ffmpeg -i final_raw.mp4 -c:v copy -af "volume=6.2dB,alimiter=limit=0.85:level=disabled" -c:a aac -b:a 192k -movflags +faststart final.mp4` | `final.mp4` |
| Publicação | copiar `final.mp4` para `<slug>_shorts_v1.mp4` | arquivo de upload |

- **Um render por vez.** Fechar Chrome/Spotify.
- `final_raw.mp4` é evidência: não apagar.
- O ganho de +6,2 dB foi medido no piloto (−21,8 → −15,6 LUFS). **Medir de novo** em cada episódio antes de aplicar.

## 5. Contrato de QA

`scripts/qa.ps1 <arquivo> [-Duracao 45]` verifica:

| Check | Critério |
|---|---|
| Duração | nominal ±1 s (`-Duracao`; padrão 45 → 44–46; LAB 001 usa `-Duracao 60`) |
| Vídeo | 1080×1920, H.264 |
| FPS | 30/1 |
| Áudio | AAC, 48 kHz, 2 canais |
| Loudness | −17 a −13 LUFS |
| Preto | nenhum trecho > 0,5 s fora do início/fim (limiar 2% para não confundir com o fundo escuro) |

O fade final para preto é intencional e ignorado. O QA **não** substitui a revisão humana: texto cortado, ghosting e sentido são conferidos em frames.

## 6. Scripts e o que entregam

| Script | Entrega | Entrada → saída |
|---|---|---|
| `scripts/install-brain.ps1` | instala Node, Git, FFmpeg, uv, Python, Piper, HyperFrames | rede → `C:\Users\valentim\Tools` |
| `scripts/verify.ps1` | imprime versões e presença de voz/espeak/disco | — → stdout |
| `scripts/bench.ps1` | benchmark G0 de 45 s | `bench/index.html` → `bench/bench-45.mp4` + `logs/bench.json` |
| `scripts/tts.py` | wrapper do Piper para caminhos acentuados | `narracao.txt` → `voz_raw.wav` |
| `scripts/montar-voz.py` | voz cena por cena + tempos exatos (sem ASR) | `narracao_tts.txt` + `roteiro.json` → `voz_raw.wav` + `tempos_cenas.json` |
| `scripts/transcribe.py` | transcrição com timestamps por palavra | `voz.wav` → `transcricao.json` |
| `scripts/remapear.py` | alinha narração × ASR e fixa o tempo de cada cena | `narracao.txt` + `transcricao.json` → `tempos_cenas.json` |
| `scripts/gerar-episodio.py` | escreve a composição a partir do roteiro | `roteiro.json` (+ `tempos_cenas.json`) → `index.html` |
| `scripts/medir-texto.ps1` | mede a tinta do texto no frame e sugere fonte | `index.html` (+ mp4) → tabela por cena + `fonte_px` |
| `scripts/qa.ps1` | QA técnico automático | `final.mp4` → `QA PASS/FAIL` |
| `scripts/check-contrato.ps1` | valida os invariantes da composição antes do render | `index.html` → `PASS/FAIL` (exit 1 em falha) |
| `scripts/novo-episodio.ps1` | cria episódio a partir do template, com carimbo de origem | `NNN-slug` → `episodios/<slug>/` + `.template-version` |
| `tools/youtube-agent-skill/yt-retention/retention.py` | lê o CSV de retenção do Studio e reporta 3 s, 10 s, 30 s (legado), quedas e slide | `retencao.csv` + `--duration` → texto ou JSON |
| `tools/youtube-agent-skill/yt-package/title.py` | lint de título + thumbnail em PT-BR | `--title`/`--thumb` ou arquivo → issues + score heurístico |
| `tools/youtube-agent-skill/yt-script/hooks.json` | fonte das 21 fórmulas de gancho | consulta; adaptação em `docs/GANCHOS-21.md` |
| `scripts/test_youtube_agent.py` | testes dos helpers de análise | `unittest` (9 casos) |

## 7. Template × episódio

- `templates/misterio-45/` é a **base validada** (13 cenas, CSS, GSAP, áudio, QA).
- Cada episódio nasce de uma cópia e muda **apenas**: textos, tempos, tamanhos de fonte e áudio.
- `scripts/novo-episodio.ps1` faz a cópia e troca só o que é contrato: `data-composition-id`, chave de `window.__timelines`, número do dossiê e título.
- Cada episódio guarda `.template-version` (sha256 do `index.html` do template + commit). Se o template mudar, comparar o hash antes de propagar para episódios já fechados.
- Se um contrato mudar (ex.: nova forma de esconder cena), mudar primeiro no template e depois propagar para episódios ativos.
- O template **não inclui** `voz.wav`/`drone.wav`; cada episódio gera os seus.

### Fonte de verdade: `roteiro.json`

Do 005 em diante, o `index.html` é **gerado**, não editado à mão. A fonte é
`episodios/<slug>/roteiro.json`:

| Campo | Vai para |
|---|---|
| `titulo[]` | `<h1>` com `<br>` entre as linhas (quebra decidida no roteiro) |
| `pequeno[]` | `<span class="small">` |
| `kicker` | etiqueta vermelha acima do título |
| `acento` | traço de 280 px sob o texto |
| `fonte_px` | regra `.<id> h1 { font-size }` |
| `fala` | `narracao.txt` (`--narracao`) e o tempo de cena |
| `start`/`duration` | vêm de `tempos_cenas.json`, nunca do JSON do roteiro |

Regenerar é barato e idempotente: `gerar-episodio.py` reescreve o HTML inteiro.
Nunca editar o `index.html` gerado à mão — a próxima geração apaga a mudança.

O HTML escrito à mão do 005 é o teste de aceitação: gerado do `roteiro.json`, ele
sai idêntico (fora comentário, `<title>` e `const DUR`).

### Fonte do tamanho de fonte: `medir-texto.ps1`

`fonte_px` não se estima no CSS, mede-se no frame. O ciclo é:

```
gerar-episodio.py -> medir-texto.ps1 -> (-Aplicar) -> gerar-episodio.py -> render
```

`getBoundingClientRect` mede a caixa do texto; a tinta é maior por causa das
hastes e do kerning. No LAB 001, três cenas passavam na caixa e estouravam o
quadro no render. A medição oficial é `ffmpeg → gray → bbox por linha` no PNG.

## 8. O que o código já entregou

- [x] Composição tipográfica de 13 cenas, 1080×1920/30 fps, 45 s.
- [x] Sincronização por transcrição (timestamps por palavra).
- [x] `autoAlpha` por cena (sem ghosting).
- [x] Áudio `voz` + `drone` com ids estáveis.
- [x] QA visual por `?t=`.
- [x] Render segmentado com reciclagem do Chrome e `--resume`.
- [x] Normalização de loudness no pós (vídeo copiado, áudio reencodado).
- [x] QA automático com tratamento de stderr do FFmpeg e fade final.
- [x] Template reutilizável + beat sheet + README de produção.

## 9. Avisos conhecidos do lint

O `hyperframes lint` emite avisos, não erros:

- `timeline_track_too_dense`: 13 elementos na track 1. Aceito no formato de 45 s.
- `nested_structure_needs_subcomposition`: cada `<section>` tem `<h1>` dentro. Aceito; subcomposições seriam overkill para este formato.

Não “corrigir” esses avisos sem medir o custo: o render atual leva ~3m18s e passou no QA.

### Armadilhas de GSAP (medidas em 26/10/2026)

- **`fromTo` + `yoyo` + `repeat` termina no valor de partida.** Um “pisca”
  escrito como `fromTo(mk, {opacity: .15}, {opacity: 1, repeat: 1, yoyo: true})`
  termina em **0,15** — e o elemento fica quase invisível pelo resto do vídeo.
  No LAB 001 isso apagou o marcador do trilho, que era a variável do teste.
  Escrever o pisca como `to(mk, {opacity: .15, yoyo: true, repeat: 1})`, que
  parte de 1 e volta para 1.
- **O último tween de uma propriedade manda.** Se um tween posterior não
  menciona `opacity`, o valor fica no que o anterior deixou — inclusive quando
  isso é um bug. Conferir o valor final em frame, não só o meio.
- **`hyperframes snapshot` sai vazio na cena 1** (0–4 s). O gancho só se confere
  em frame do `final.mp4`.

## 10. Quando atualizar este arquivo

- Mudou atributo/contrato de cena, áudio, tempo, render ou QA.
- Novo script ou mudança de entrada/saída.
- Mudança no template que afete episódios existentes.
- Mudança no parser de retenção ou nas janelas de 3 s/10 s.
- Descoberta de armadilha nova (registrar também em `MEMORIA.md` §7).

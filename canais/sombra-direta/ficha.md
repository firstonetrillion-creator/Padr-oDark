# Canal `sombra-direta`

> Preencher **antes do vídeo 1**. Campo vazio = canal não abre.
>
> **Alerta de método:** este canal propõe **três** mudanças em relação ao Dossiê 45
> (nicho, visual, áudio). A regra do `canais/README.md` é **uma variável por canal**.
> Abrir assim significa abrir mão da leitura comparativa controlada contra o 45 — o
> canal vira um teste livre, não um experimento A/B. Isso é decisão sua; a ficha
> registra a escolha consciente.

## Identidade

| Campo | Valor |
|---|---|
| Nome | Sombra Direta |
| Handle | @SombraDireta (a confirmar na conta Google) |
| Conta Google (brand account) | **separada do Dossiê 45** — histórico, público e recomendações independentes |
| Aberto em | (a definir) |
| Slug | `sombra-direta` |
| Estado | `planejado` |

## Tese (uma frase)

> Aposto que **adulto no celular** assiste a **cartões sombrios de 45 s** sobre **manipulação mental, estoicismo e Maquiavel** até o fim, porque **o vídeo expõe um mecanismo invisível que ele usa todos os dias**.

Se a frase não sai inteira, o canal não está pronto — está só uma ideia.

## O modelo em 5 escolhas

| Dimensão | Este canal | Dossiê 45 (referência) | Mudou? |
|---|---|---|---|
| Nicho | psicologia sombria / estoicismo vs Maquiavel | arquivo/mistério PT-BR | **sim** |
| Formato | 45 s, 12–16 cenas, 1 ideia por cartão, ≤5 s por cena | 45 s, 12–14 cenas, 1 ideia por cartão, ≤5 s por cena | não |
| Voz | Piper `pt_BR-faber-medium`, impessoal, seco | Piper `pt_BR-faber-medium`, impessoal | não |
| Cadência | irregular, ~1 a cada 2 dias | irregular | não |
| Visual | **novos efeitos**: fundo em movimento, texto em escala/fade, destaque animado, glitch sério por CSS | v1 tipográfico, só texto, moldura, drone inaudível | **sim** |
| Áudio | **voz em 1,0 + bed sonoro audível + pulsos de impacto** | voz + drone a 0,16 (quase inaudível) | **sim** |

**Variáveis que mudam:** nicho + visual + áudio (3 de 5).  
**Consequência:** não haverá leitura comparativa limpa contra o Dossiê 45. O canal é um teste livre.

## Hipótese e critério (escritos antes do vídeo 1)

| Campo | Valor |
|---|---|
| Métrica primária | `% média assistida` em 48 h |
| Métrica secundária | 10 s em 48 h |
| Referência | Dossiê 45: 87,0 / 87,0 / 45,7 (002–004); 10 s 61,8 / 68,5 / 43,4 |
| N (vídeos até decidir) | 8 |
| **Escalar se** | mediana de `% média` ≥ 50% **e** mediana de 10 s ≥ 50% |
| **Ajustar se** | uma das duas passa e a outra não — muda **uma** variável |
| **Matar se** | mediana de `% média` < 40% **e** views medianas < 30% da referência |
| Data prevista da leitura | (a definir após vídeo 8) |

## Produção

| Item | Valor |
|---|---|
| Template | `templates/sombra-cinema/` (novo, CSS+GSAP apenas — sem WebGL/Three.js) |
| Episódios em | `canais\sombra-direta\episodios\` |
| Voz | `pt_BR-faber-medium`, `length_scale` ~1.20, cena por cena (`montar-voz.py`) |
| Duração alvo | 45,000 s · 1080×1920 · 30 fps · H.264 + AAC |
| Loudness | −15 LUFS alvo, TP ≤ −1,5 dBFS |
| Áudio extra | bed e pulsos gerados com FFmpeg lavfi (sem áudio de terceiros) |

## Fontes e limites

- **Afirma:** estoicismo (Zenão de Cítio, c. 300 a.C.; Sêneca; Epicteto; Marco Aurélio); Nicolau Maquiavel, *O Príncipe* (1513/1532); Dark Triad / maquiavelismo como traço (Paulhus & Williams, 2002).
- **Não afirma:** o que um indivíduo específico pensa ou sente; que alguém está sendo manipulado em tempo real; conselhos de vida como fato científico.
- **Lenda marcada como lenda:** "Maquiavel ensina a ser malvado" — *O Príncipe* é descrição de poder real, não apologia do mal.
- **Nomes próprios para conferir na escuta:** Zenão, Maquiavel, Epicteto, Sêneca, Marco Aurélio.
- **Não reuploadar conteúdo de terceiros.** `yt-dlp` só para metadados.
- **Sem WebGL, Three.js ou shaders.** GPU Intel HD 620 (regra inviolável).

## Riscos assumidos

- Psicologia sombria teve mediana de views/inscrito menor que arquivo/mistério na validação de nicho (`docs/NICHO.md`, 21/10/2026): 0,06 vs 0,10. Pode ser raso.
- Três variáveis de uma vez impedem saber o que moveu a mérica, se houver mudança.
- Mais efeito visual sem WebGL limita o que é possível; depende de CSS/GSAP bem dosado para não pesar o Chrome headless de 8 GB RAM.
- Áudio mais audível exige bed gerado por FFmpeg; risco de soar artificial se não for bem dosado.

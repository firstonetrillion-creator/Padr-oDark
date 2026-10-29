# Canal `mente-obscura`

> Preencher **antes do vídeo 1**. Campo vazio = canal não abre.
> Regra: **uma** variável muda em relação ao Dossiê 45. Duas, e a leitura não existe.
>
> **Alerta:** esta ficha propõe **três** mudanças (nicho, visual, áudio). Isso
> fura a regra de uma variável só. Antes de publicar o vídeo 1, escolher qual é
> a variável única e deixar as outras duas iguais ao Dossiê 45 — ou aceitar que
> não haverá leitura comparativa contra o 45.

## Identidade

| Campo | Valor |
|---|---|
| Nome | (a definir) |
| Handle | (a definir) |
| Conta Google (brand account) | **precisa ser separada do Dossiê 45** — histórico, público e recomendações independentes |
| Aberto em | (a definir) |
| Slug | `mente-obscura` (sugestão) |
| Estado | `planejado` |

## Tese (uma frase)

> Aposto que **público adulto no celular** assiste a **cartões tipográficos sombrios de 45 s** sobre **filosofia escura e manipulação mental** até o fim, porque **o vídeo expõe um mecanismo que o espectador não sabe que usa**.

Se a frase não sai inteira, o canal não está pronto — está só uma ideia.

## O modelo em 5 escolhas

| Dimensão | Este canal | Dossiê 45 (referência) | Mudou? |
|---|---|---|---|
| Nicho | psicologia sombria / estoicismo vs Maquiavel | arquivo/mistério PT-BR | **sim** |
| Formato | 45 s, 12–16 cenas, 1 ideia por cartão, ≤5 s por cena | 45 s, 12–14 cenas, 1 ideia por cartão, ≤5 s por cena | não |
| Voz | Piper `pt_BR-faber-medium`, impessoal, seco | Piper `pt_BR-faber-medium`, impessoal | não |
| Cadência | irregular, ~1 a cada 2 dias | irregular | não |
| Visual | tipográfico + **efeitos visuais reforçados** (fundo em movimento, variação de fonte, destaque animado) | v1 tipográfico, drone inaudível | **sim** |
| Áudio | **voz em 1,0 + bed sonoro audível + pulsos de impacto** | voz + drone a 0,16 (inaudível) | **sim** |

**A variável única deste canal é:** _<escolher: nicho / visual / áudio>_ — porque _<por quê>_.

Se houver dois "sim" na coluna **Mudou?**, pare e escolha qual fica.

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
| Template | `templates/misterio-45/` (base v1, com reforço visual via CSS/GSAP — sem WebGL) |
| Episódios em | `canais/mente-obscura/episodios/` |
| Voz | `pt_BR-faber-medium`, `length_scale` ~1.20, sintetizada cena por cena (`montar-voz.py`) |
| Duração alvo | 45,000 s · 1080×1920 · 30 fps · H.264 + AAC |
| Loudness | −15 LUFS alvo, TP ≤ −1,5 dBFS |
| Áudio extra | bed e pulsos gerados com FFmpeg lavfi (sem áudio de terceiros) |

## Fontes e limites

- **Afirma:** estoicismo (Zenão de Cítio, c. 300 a.C.; Sêneca; Epicteto; Marco Aurélio); Nicolau Maquiavel, *O Príncipe* (escrito 1513, publicado 1532); Dark Triad / maquiavelismo como traço (Paulhus & Williams, 2002).
- **Não afirma:** o que um indivíduo específico pensa ou sente; que alguém está sendo manipulado em tempo real; conselhos de vida como fato.
- **Lenda marcada como lenda:** "Maquiavel ensina a ser malvado" é simplificação; *O Príncipe* é descrição de poder, não manual de maldade.
- **Nomes próprios para conferir na escuta:** Zenão, Sêneca, Epicteto, Marco Aurélio, Maquiavel.
- **Não reuploadar conteúdo de terceiros.** `yt-dlp` só para metadados.

## Riscos assumidos

- Psicologia sombria teve mediana de views/inscrito menor que arquivo/mistério na validação de nicho (`docs/NICHO.md`, 21/10/2026): 0,06 vs 0,10. Pode ser raso.
- Mais efeito visual sem WebGL/Three.js (regra inviolável, GPU Intel HD 620) limita o que é possível via CSS/GSAP.
- Áudio mais audível exige bed gerado por FFmpeg; risco de soar artificial se não for bem dosado.

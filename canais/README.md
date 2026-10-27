# canais — um canal por modelo, um modelo por canal

> Criado em **27/10/2026**, com os 6 vídeos da Fase 2 no ar.
> Este arquivo é o método. O estado de cada canal fica em `canais/<slug>/`.

## Por que existe

O Dossiê 45 é **uma** amostra: 6 vídeos do mesmo modelo (arquivo/mistério PT-BR,
45 s, tipográfico, voz Piper, cadência irregular). É a única referência limpa que
temos. Testar outro modelo **dentro** dele destrói a série — não dá para saber se
o número mudou por causa do formato novo ou porque a audiência mudou.

Canal separado resolve duas coisas de uma vez:

1. **Isola a amostra.** Cada modelo tem a própria curva, o próprio público, o
   próprio histórico no algoritmo. Nada contamina o Gate 2.
2. **Permite comparar de verdade.** Dois canais com o mesmo pipeline, medidos na
   mesma janela de 48 h, respondem "o que segura o espectador" melhor do que
   qualquer teste dentro de um canal só.

`docs/ESCALA.md` já dizia que o gargalo era **vazão, não ideia**, e que a
produção caiu de ~2 dias para ~2 h por vídeo depois do gerador. Com vazão
resolvida, o gargalo passa a ser **decisão**: produzir mais do mesmo não ensina
nada. É para isso que serve o segundo canal.

## As três regras

1. **Um canal = um modelo.** Modelo é a combinação de cinco escolhas: nicho,
   formato, voz, cadência e visual.
2. **Um canal = uma variável.** Ao abrir o canal 2, **uma** das cinco muda e as
   outras quatro ficam iguais ao Dossiê 45. Duas mudanças ao mesmo tempo não dão
   leitura nenhuma — só uma opinião nova.
3. **Hipótese e critério de morte são escritos antes do vídeo 1**, na
   `ficha.md`. No dia 30 não se decide com o número na mão; decide-se com a
   regra que foi escrita antes.

## O que conta como variável

| Dimensão | O que muda | Exemplo de teste |
|---|---|---|
| **Nicho** | assunto e público | true crime em vez de arquivo/mistério |
| **Formato** | duração, número de cartões, ritmo | 60 s contra 45 s; 1 ideia a cada 5 s contra 8 s |
| **Voz** | modelo Piper, velocidade, densidade | voz masculina grave contra a `faber-medium` |
| **Cadência** | frequência de publicação | 1/dia contra 1 a cada 2 dias |
| **Visual** | o que está na tela | v2 com imagem de arquivo contra v1 só tipografia |

**Modelos candidatos (não decididos).** Cada linha muda **uma** coisa; escolher
uma é decisão sua, e ela vai para `docs/DECISOES.md`:

- **A — mesmo formato, nicho adjacente:** true crime PT-BR, 45 s, mesmo visual.
  Testa se o furo está no nicho (arquivo/mistério é raso — ver `docs/ESCALA.md`).
- **B — mesmo nicho, formato longo:** arquivo/mistério em 60 s com mais cartões.
  Testa se 45 s é curto demais para o miolo segurar.
- **C — mesmo nicho, som audível:** 45 s, mas com desenho sonoro de verdade em
  vez de drone inaudível. É a variável que o 005 e o 006 **não** testaram.

## Anatomia

```
canais/
  README.md              este método
  registro.csv           um canal por linha: identidade, estado, última leitura
  _template/             ficha.md, metricas.csv, decisoes.md em branco
  dossie45/              canal 1, preenchido — serve de exemplo do formato
    ficha.md
    metricas.csv
    decisoes.md
  <slug>/                canal novo: cópia preenchida do _template
```

**Onde ficam os episódios de um canal novo:**

```
canais/<slug>/episodios/NNN-nome-curto/
```

Funciona sem tocar em script nenhum: `gerar-episodio.py`, `medir-texto.ps1`,
`check-contrato.ps1` e `qa.ps1` recebem **o caminho do episódio**, não um caminho
fixo. `novo-episodio.ps1` é a exceção — ele grava sempre em `episodios/`. Duas
saídas:

```powershell
# 1) criar e mover (funciona hoje, sem mexer no script)
.\scripts\novo-episodio.ps1 001-primeiro-caso "Título"
Move-Item episodios\001-primeiro-caso canais\<slug>\episodios\

# 2) pendência conhecida: dar um -Destino ao novo-episodio.ps1 (padrão: episodios)
```

**O Dossiê 45 é exceção:** os 6 episódios ficam em `episodios/` na raiz. Mover
agora quebraria caminhos em documentos, commits e no `status.md` de cada um.
`canais/dossie45/` guarda **o registro**, não os episódios.

**Template por formato:** `templates/misterio-45/` é o v1 congelado do Dossiê 45.
Se o canal novo muda o formato, ele ganha `templates/<formato>/` — não se
"ajusta" o template do 45 s para outra coisa, senão os dois ficam mentindo.

## Protocolo de medição (igual em todos os canais)

1. **Janela fixa de 48 h.** Nunca comparar um vídeo medido em 24 h com outro em
   48 h: a duração média escorrega (002 foi de 87,0% para 76,1% em um dia).
2. **Fórmula:** `% média assistida = duração média ÷ duração do vídeo`. O painel
   entrega a duração média; a divisão é nossa.
3. **Fonte:** YouTube Studio com login, **vídeo a vídeo** —
   `.../video/<id>/analytics/tab-overview/period-default?hl=en&cb=<ts>`, com 1–3
   recarregamentos até o card de retenção aparecer. A aba Content nunca carrega.
4. **Registrar cru** no episódio (`retencao.md`) e o resumo em
   `canais/<slug>/metricas.csv`. Número sem data de leitura não vale.
5. **Views não decidem nada.** O 004 teve 3× as views do 003 e metade da
   retenção. Views são sintoma; `% média assistida` é a régua.

## Critério de decisão (declarado na `ficha.md` antes do vídeo 1)

Depois de **N = 8 vídeos** (padrão; ajuste na ficha se quiser), um dos três:

| Resultado | Critério | Ação |
|---|---|---|
| **Escalar** | mediana de `% média` ≥ 50% **e** mediana de 10 s ≥ 50% | dobra a cadência, não muda nada |
| **Ajustar** | uma das duas passa e a outra não | muda **uma** variável, anota a data |
| **Matar** | mediana de `% média` < 40% **e** views medianas < 30% da referência | encerra e registra por quê |

Referência atual (Dossiê 45, 48 h): `% média` 87,0 / 87,0 / 45,7 (002–004);
3 s 90,9–92,7; 10 s 43,4–68,5; views 234 / 370 / 1.200. O 001 (**33,3%**) fica
fora: foi feito antes da disciplina de gancho e não tem curva.

**Por que 8 e não 3:** com 3 vídeos, uma mediana é o valor do meio — qualquer
oscilação muda a conclusão. 8 é o menor número em que a mediana já resiste a um
vídeo fora da curva.

## Custo e serialização

| Fato | Número |
|---|---|
| Render | 1 por vez; ~3 min por 45 s; 60 s custa ~4 min |
| Episódio completo (com o gerador) | ~2 h de trabalho |
| Vídeos até decidir um canal | 8 |
| Custo de decisão por canal | **~16 h** |
| Canais ativos simultâneos nesta máquina | **2** (1 produzindo, 1 medindo) |

**Um render por vez é regra inviolável.** Dois canais produzindo na mesma tarde
disputam Chrome e FFmpeg e o render cai.

## Checklist: abrir um canal novo

- [ ] **Conta separada.** Conta Google/brand account própria, não a do Dossiê 45 —
      histórico, público e recomendações têm de ser independentes.
- [ ] **Slug** decidido (minúsculo, sem número, ex. `arquivo2`) e linha criada em
      `canais/registro.csv` **no mesmo dia** da abertura.
- [ ] `canais/<slug>/` criada a partir de `_template/`.
- [ ] **`ficha.md` preenchida** — tese, as 5 dimensões, a variável única, a
      hipótese e o critério de morte. Ficha vazia = canal não abre.
- [ ] Template do formato escolhido (`templates/misterio-45` se a variável não é
      o formato).
- [ ] Identidade visual: marca, avatar, banner, descrição com o aviso de conteúdo
      sintético.
- [ ] Primeiro episódio pelo fluxo normal (`briefing` → `gancho` → `roteiro` →
      voz → composição → render → `qa.ps1` → aprovação humana).
- [ ] Publicar e **medir 48 h**; registrar em `metricas.csv`.
- [ ] Ler a ficha de novo no vídeo 8 e tomar uma das três decisões.

## Como registrar um vídeo

Linha nova em `canais/<slug>/metricas.csv`:

```
data,video_id,titulo,views_48h,retencao_3s,retencao_10s,fim_curva,pct_media,likes,comentarios,observacao
```

- `data` = data de **publicação**, não de leitura. A leitura vai na `observacao`
  ou no `retencao.md` do episódio.
- Campo não medido fica **vazio**, nunca `0` e nunca estimado.
- `pct_media` é sempre 48 h.

## O que NÃO fazer

- **Não abrir canal sem hipótese.** "Ver se pega" é custo sem leitura — e ainda
  ocupa a máquina.
- **Não mudar duas variáveis** no mesmo canal. A leitura morre.
- **Não usar o Dossiê 45 como campo de teste.** A série de 6 é a única
  referência; o `docs/PLANO.md` congela o v1 até o Gate 2.
- **Não medir em janelas diferentes** entre canais.
- **Não reuploadar conteúdo de terceiros.** Vale para todo canal do estúdio.
- **Não publicar sem aprovação humana explícita**, por canal e por vídeo.

## Relação com o Dossiê 45

| | Dossiê 45 | Canal novo |
|---|---|---|
| Papel | amostra de referência (6 vídeos) | laboratório de modelo |
| Formato v1 | **congelado até o Gate 2** | livre — é o ponto do canal |
| Episódios | `episodios/` | `canais/<slug>/episodios/` |
| Registro | `canais/dossie45/` | `canais/<slug>/` |
| Medição | `biblioteca/publicados.csv` + `retencao.md` | `canais/<slug>/metricas.csv` |

O Dossiê 45 continua sendo a referência até o Gate 2 fechar. Depois disso ele
passa a ser **mais um canal** no registro — com a vantagem de já ter 6 curvas.

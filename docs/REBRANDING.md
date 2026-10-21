# Rebranding — Cod Mind Million → Dossiê 45

> Execução no YouTube Studio. O que está aqui é para copiar e colar; a ordem importa.
> Referência de identidade: `docs/IDENTIDADE.md`. Decisão: `docs/DECISOES.md` (seção “Canal”).
> Última atualização: **2026-10-21**.

## Estado em 21/10/2026

| Item | Estado em 21/10/2026 |
|---|---|
| Handle `@Dossie45` | **no ar** — mesmo canal do piloto (`UCwgP68Uen2KoIh2R-j231Yw`) |
| Nome de exibição | **Dossiê 45** — confirmado na página pública em 21/10/2026 |
| Descrição / palavras-chave | descrição **pronta em `identidade/descricao-canal.txt`**, ainda vazia no canal; palavras-chave pendentes |
| Avatar / banner | **no ar** — avatar 900×900 e banner recortado em 2048×339; texto dentro da área segura |
| Shorts de psicologia | **privados** — a aba Shorts mostra **1** vídeo público (o piloto de mistério) |

## Antes de tocar em qualquer coisa

1. O handle `@Dossie45` **já está no canal**; não é mais necessário checar disponibilidade.
2. Se um dia precisar trocar de handle, lembrar: o YouTube limita a **2 trocas em 14 dias**.
3. O nome de exibição pode mudar quantas vezes quiser; o handle, não.

## Texto pronto

**Nome de exibição**

```
Dossiê 45
```

**Handle**

```
@Dossie45
```

**Descrição do canal** — 520 caracteres, também em `identidade/descricao-canal.txt`

```
Casos sem solução, contados em 45 segundos.

O Dossiê 45 é um arquivo de mistérios documentados: faróis abandonados, navios que nunca chegaram, registros que param no meio, pessoas que desapareceram sem deixar explicação.

Cada vídeo parte de um fato verificável e termina na pergunta que ninguém respondeu. Fatos têm fonte. Lendas são marcadas como lendas. Nada de reupload.

Casos novos toda semana.

Se você coleciona casos sem solução, o arquivo está aberto.

#mistério #casossemsolução #arquivo
```

**Palavras-chave do canal** (Studio → Configurações → Canal → Informações básicas)

```
mistério, casos sem solução, arquivo, documentário, história, casos reais, desaparecimento, investigação, farol, navio, relatos, lendas
```

**Links** (Studio → Personalização → Informações básicas → Links)

| Prioridade | Texto | URL |
|---|---|---|
| 1 | Playlist — Casos | criar depois do 002 e apontar aqui |

Até existir playlist, deixar links vazios. Link quebrado custa mais que link ausente.

**Padrão de descrição por vídeo**

```
<contexto em uma linha, sem repetir o título>

Fonte: <órgão, documento ou arquivo>

#misterio #casossemsolucao #arquivo
```

## Ordem de execução

| # | Onde | Ação | Por quê nesta ordem |
|---|---|---|---|
| 1 | Studio → Personalização → Informações básicas | Trocar **nome** para “Dossiê 45” | ✅ feito em 21/10 |
| 2 | Studio → Personalização → Informações básicas | Trocar **handle** para `@Dossie45` | ✅ feito em 21/10 |
| 3 | Studio → Personalização → Informações básicas | Colar descrição, palavras-chave e país | ⚠️ texto pronto; falta colar no Studio |
| 4 | Studio → Personalização → Imagem da marca | Subir avatar (800×800) e banner (2048×1152, área segura 1235×338) | ✅ avatar e banner no ar em 21/10 |
| 5 | Studio → Conteúdo | **Não listar** os 9 shorts de psicologia | ✅ feito; a aba Shorts mostra só o piloto |
| 6 | Studio → Conteúdo | Conferir que `001-faroleiros` continua **público** | ✅ é a prova social da marca nova |
| 7 | Studio → Playlists | Criar “Casos” e adicionar o 001 | Dá destino ao link da descrição |
| 8 | janela anônima | Abrir `youtube.com/@Dossie45` | Ver o canal como o público vê: nome, bio, só mistério na aba Shorts |

**Não apagar** os shorts de psicologia. Não listados é reversível; apagados, não.

## Inconsistência a resolver antes do 002

O piloto tem, no canto superior, a marca **ARQUIVO NOTURNO** — que não é o nome do canal.

Duas saídas:

| Opção | Efeito |
|---|---|
| **A. Adotar “DOSSIÊ 45” como marca de tela a partir do 002** (recomendado) | Canal e vídeo falam a mesma língua; o 001 fica como peça de transição |
| B. Manter “ARQUIVO NOTURNO” como série dentro do canal | Exige explicar a diferença na descrição; complexidade sem retorno com 6 inscritos |

Se for A:

```powershell
.\scripts\novo-episodio.ps1 002-<slug> "<título>" -Marca "DOSSIÊ 45"
```

O `001` **não** se re-renderiza por causa do nome. A regra é não gastar 3 min de render para corrigir algo que ninguém vê em 45 s.

## Depois de executar

1. Marcar o checklist em `docs/IDENTIDADE.md`.
2. Atualizar `MEMORIA.md` §1 (linha “Canal”) e §8.
3. Entrada datada em `docs/HISTORICO.md` com o handle final e o que foi deslistado.
4. Só então publicar o 002.

## Pendências que só você pode fazer

- [x] Confirmar `@Dossie45` no Studio.
- [x] Subir avatar e banner (verificados no ar em 21/10).
- [x] Salvar o nome de exibição **Dossiê 45** com acento e espaço; confirmado na página pública.
- [x] Privar os 9 shorts de psicologia; a aba Shorts mostra **1** vídeo (o piloto).
- [ ] Colar a descrição de `identidade/descricao-canal.txt` e salvar palavras-chave/país.
- [ ] Conferir o canal em janela anônima com nome novo, bio nova e **1** Short de mistério.
- [ ] Só então publicar o 002.

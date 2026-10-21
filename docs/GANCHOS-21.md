# 21 fórmulas de gancho — checklist PT-BR

> Adaptação de `tools/youtube-agent-skill/yt-script/hooks.json` (MIT, commit
> `a2feb21`) para o formato **Mistério 45**. O JSON original fica intacto; esta
> é a versão de trabalho.
>
> **Exemplos são formas, não fatos.** Se um exemplo virar roteiro, ele precisa
> de fonte como qualquer outro fato. Lenda continua marcada como lenda.

## Como usar

1. Gerar 10 ganchos.
2. Marcar qual fórmula domina cada um. Híbrido pode, mas **uma promessa**.
3. Eliminar o que depende de contexto, confirma o título errado ou não cabe em 2 s.
4. Testar em voz alta. A primeira frase tem **no máximo 9 palavras**.
5. Escolher 1 e escrever a linha visual do frame 1.
6. Registrar em `episodios/<slug>/gancho.md`, com a fórmula escolhida.

O `hooks.json` é a referência; **não** usar `hookscore.py` para decidir em
PT-BR. Ele foi calibrado em inglês e o score não é válido para nós.

## As 21 fórmulas

| # | Fórmula | Forma | Exemplo (forma, não fato) | Encaixe no Dossiê 45 |
|---:|---|---|---|---|
| 1 | **O Dado** | Um número desconhecido, dito seco, e a consequência. | “Três dos quatro relógios pararam às 3h07.” | Alto — se o número tiver fonte |
| 2 | **O Resultado de Outro** | Resultado de uma pessoa nomeada + mecanismo. | “Um pesquisador refez a rota em 1985. Achou o mesmo marco.” | Médio — exige fonte nominal |
| 3 | **O Erro** | Nomeia o erro que o espectador provavelmente comete. | “O erro não foi entrar. Foi trancar a porta por dentro.” | Alto |
| 4 | **A Virada Contrária** | Diz o consenso e o rejeita. | “Todos dizem que o navio afundou. O último registro diz outra coisa.” | Alto |
| 5 | **A Revelação** | Promete mostrar uma coisa específica e mostra. | “A última página do diário está aqui. E ela não termina.” | Alto |
| 6 | **O Superlativo** | O único, o maior, o mais rápido da categoria. | “O único farol do Atlântico que ficou 12 anos sem faroleiro.” | Médio — o superlativo precisa ser provado |
| 7 | **O Relógio** | Limita a recompensa no tempo. | “Em 45 segundos, você vai ver por que o Mary Celeste não afundou.” | Alto — a promessa tem de ser verdadeira |
| 8 | **Eu Testei** | Experimento em primeira pessoa com custo real. | “Eu refiz o trajeto do último faroleiro.” | Baixo — quebra a voz impessoal; só com teste real |
| 9 | **A Pergunta** | Faz a pergunta exata que o espectador faria. | “Por que o farol estava aceso se não havia ninguém?” | Alto |
| 10 | **Antes e Depois** | Dois estados, um corte entre eles. | “O mesmo farol em 1900 e em 1901. A janela mudou de lugar.” | Médio — precisa de duas imagens |
| 11 | **A Desmontagem** | Desmonta um objeto real em público. | “O relatório tem 14 páginas. Três linhas não fecham.” | Alto |
| 12 | **A Combinação** | Duas ferramentas nomeadas viram um resultado. | “O diário do capitão + o mapa do porto = uma rota que não existe.” | Médio — as duas peças precisam ser necessárias |
| 13 | **O Alerta** | Um custo que o espectador está prestes a pagar. | “Não leia o último registro antes do primeiro.” | Alto |
| 14 | **A Lista** | Um conjunto contado, com o número na primeira linha. | “Três detalhes do Mary Celeste que não aparecem no filme.” | Alto |
| 15 | **O Recibo** | Mostra o artefato primeiro, explica depois. | “Este é o telegrama original. Foi enviado dois dias antes.” | Alto |
| 16 | **O Insider** | Informação de dentro de um sistema. | “O catálogo do arquivo tem uma pasta sem índice.” | Médio — nunca inventar acesso |
| 17 | **A Alegação Impossível** | Algo que soa falso, seguido de prova. | “O navio foi encontrado sem ninguém. E com o jantar servido.” | Alto |
| 18 | **A Comparação** | Duas opções nomeadas, uma vencedora. | “Duas versões do mesmo relatório. Só uma tem assinatura.” | Médio |
| 19 | **A Origem** | De onde um resultado realmente veio. | “Toda lenda do farol começa no mesmo telegrama de 1900.” | Médio — funciona uma vez por canal |
| 20 | **O Prazo** | Algo muda em uma data real. | “O registro muda em 1901. Antes disso, o nome era outro.” | Médio — só com data verificável |
| 21 | **O Endereço Direto** | Nomeia o espectador exato nas primeiras palavras. | “Se você coleciona casos sem solução, este tem três datas.” | Alto |

## Checklist de aprovação

- [ ] A primeira frase tem **≤ 9 palavras**.
- [ ] Cabe em **2 segundos** em voz alta.
- [ ] Confirma a promessa do título; não abre outro assunto.
- [ ] Carrega **uma ideia só**.
- [ ] Tem número, nome, data ou objeto concreto.
- [ ] Não abre com “hoje vamos falar sobre”.
- [ ] Não usa “você não vai acreditar”.
- [ ] O vídeo entrega o que o gancho promete.
- [ ] Fato tem fonte; lenda está marcada como lenda.
- [ ] Escolhi uma fórmula dominante; não empilhei duas promessas.
- [ ] O frame 1 já conta parte da história.
- [ ] Ouvi a gravação: não ficou artificial nem longa.

## Fórmulas de baixo encaixe

**Eu Testei** e **O Resultado de Outro** pressupõem uma pessoa e uma voz
pessoal. No Dossiê 45, a voz é impessoal (“o arquivo”, “o registro”). Só usar
se houver uma pesquisa/teste real e o custo for verificável. Nunca inventar
primeira pessoa para simular autoridade.

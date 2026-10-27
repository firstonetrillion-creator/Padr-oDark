# Diagnóstico — por que a voz do 006 não veio de take único

Evidência da falha do ASR que mudou o método deste episódio. Não é artefato de
produção: é a prova de que o caminho `tts.py` → `transcribe.py` → `remapear.py`
não era confiável aqui.

| Arquivo | O que é |
|---|---|
| `asr-voz_raw.json` | transcrição do `voz_raw.wav` (take único, `small`): 117 palavras |
| `asr-probe.txt` | cinco frases isoladas usadas para testar se o erro era do áudio inteiro |
| `asr-probe.json` | transcrição do probe com `medium` — o erro **se repete** no modelo maior |

## O que o ASR ouviu

| Narração | ASR `small` |
|---|---|
| cortam um degrau | “Cota o mundo legal” |
| ao cedro | “ao cedo” |
| Igor Dyatlov | “Igor Diato” |
| Acendem fogo | “Acenda em fogo” |
| Morrem de frio | “Morrem de fio” |
| dois tórax | “dois toras” / “2 torres” |
| um crânio | “1 cânio” |
| de 9,5 a 13,5 horas | “de 9 ,6h e 6h” |
| avalanche | “avalante” |

`remapear.py` reportou **alinhamento 83/116 (72%)** e colocou a cena 4 **1,4 s**
fora do lugar (10,47 s medidos contra 11,87 s reais). A tabela mostrava o texto
certo e o tempo errado — o pior tipo de erro, porque não se vê.

## O que foi feito

`scripts/montar-voz.py`: cada parágrafo de `narracao_tts.txt` é sintetizado
separado, tem o silêncio das pontas cortado e é concatenado com silêncio
calculado. O tempo passa a ser a soma dos blocos, sem ASR.

Resultado no 006: 40,814 s de fala + 4,186 s de silêncio, `voz_raw.wav` fechando
**45,000 s** com `length_scale` 1,10.

`transcricao.json` (na pasta do episódio) é a transcrição do take único
descartado — ficou como evidência, não é usada na composição.

---
name: Retencao
description: Use para ler o CSV de retenção do YouTube Studio e decidir o próximo ajuste.
---

# Retenção

## Objetivo
Transformar o gráfico de retenção em uma decisão: o problema é gancho, momento ou ritmo.

## Quando
48 h depois de publicar. Não abrir o CSV antes de ter volume mínimo; 6 views não decidem nada.

## Onde pegar
YouTube Studio → vídeo → Analytics → Engajamento → gráfico de retenção → baixar → “Retenção da audiência”.

Salvar como `episodios/<slug>/retencao.csv`.

## Comando

```powershell
.\.venv\Scripts\python.exe tools\youtube-agent-skill\yt-retention\retention.py `
  episodios\<slug>\retencao.csv --duration 45 `
  --transcript episodios\<slug>\transcricao.json
```

Para dados brutos:

```powershell
.\.venv\Scripts\python.exe tools\youtube-agent-skill\yt-retention\retention.py `
  episodios\<slug>\retencao.csv --duration 45 --json
```

## Como ler

- **3 s:** o Short decidiu se continua. É a janela mais importante.
- **10 s:** o contexto segurou depois do gancho.
- **30 s:** legado de long-form. **Não** usar como gate de Short.
- **Quedas:** momentos. Trocar a linha, o corte ou a promessa.
- **Slide:** ritmo. Cortar o meio, não reescrever o fato.

Metas provisórias: **3 s ≥ 70%** e **10 s ≥ 45%**. Calibrar depois de 6 vídeos;
não transformar em lei antes disso.

## Saída
Criar `episodios/<slug>/retencao.md` com:

1. números de 3 s e 10 s;
2. a maior queda e o que estava sendo dito;
3. diagnóstico: gancho, momento ou ritmo;
4. **uma** correção para o próximo vídeo;
5. linha atualizada em `biblioteca/publicados.csv`.

## Regras
- Não usar views/likes como substituto de retenção.
- Não usar a janela de 30 s para julgar um Short de 45 s.
- Se o CSV vier em formato diferente, salvar o original e ajustar o parser; não editar o CSV à mão.

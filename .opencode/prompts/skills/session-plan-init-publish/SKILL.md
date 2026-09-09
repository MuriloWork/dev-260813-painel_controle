---
name: session-plan-init-publish
description: Aplica correcoes indicadas pelo usuario no relatorio de revisao e finaliza o plano
license: MIT
compatibility: opencode
metadata:
  audience: session-planner
  workflow: session-start
---

## Proposito

Ler o relatorio de revisao comentado pelo usuario e aplicar as correcoes indicadas no arquivo de plano.

## Input

Os dados veem do prompt:
- `plan_dir`: diretorio do plano
- `plan_file`: nome do arquivo de plano (ex: 260526_plan_sqlite_views_01.md)

## Fluxo

### 1. Ler arquivos

1. Leia `{plan_dir}/{plan_file}` — o plano atual.

### 2. Identificar correcoes

O usuario comenta diretamente no plan_file_. Procure por marcacoes como:
- `USUARIO: ...` — instrucao explicita de correcao
- `APROVADO` — nenhuma correcao necessaria
- Comentarios em linha indicando o que mudar

### 3. Aplicar correcoes no plano

Use `edit` para modificar o `{plan_file}` conforme as instrucoes do usuario, sem deletar os comentarios `USUARIO`.

### 4. Finalizar

Apos aplicar todas as correcoes, registre no relatorio de revisao:
- Quais correcoes foram aplicadas
- Data/hora da publicacao
- Indicacao de que o plano esta finalizado

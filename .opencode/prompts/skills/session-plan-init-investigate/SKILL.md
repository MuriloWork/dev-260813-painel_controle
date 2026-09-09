---
name: session-plan-init-investigate
description: Investiga alvos (arquivos, banco, diretorios) definidos no prompt e gera relatorio bruto em markdown
license: MIT
compatibility: opencode
metadata:
  audience: session-planner
  workflow: session-start
---

## Proposito

Executar a investigacao dos alvos definidos no prompt (arquivos, schemas SQL, banco de dados, diretorios) e gerar um arquivo markdown com os achados brutos. Nao estrutura nem organiza — apenas coleta.

## Input

Os dados da sessao veem do prompt:
- `objetivo`: descricao do que fazer
- `briefing_file`: arquivo de briefing
- `plan_dir`: diretorio do plano
- `plan_file_pattern`: padrao de nome dos arquivos
- `session_base_scripts_dir`: pasta com scripts da sessao
  - `foco`: areas a investigar
  - `alvos`: arquivos/diretorios/tabelas especificos

## Fluxo

### 1. Investigar alvos

Com base nos alvos do prompt, execute o que foi solicitado:
- Para ler arquivos: use `read`
- Para comandos SQLite: use `bash` com `sqlite3 "caminho/banco.db" ".tables"`
- Para listar diretorios: use `glob`
- Para buscar conteudo: use `grep`

Nao crie sub-tasks (tool Task). Use bash e read diretamente.

### 2. Gerar arquivo de investigacao

O formato e livre — apenas documente os achados de forma bruta. Exemplo:

```
# Investigacao: {objetivo}

## Tabelas encontradas
- tb_ast: 27321 registros, colunas: project_name, version, file_path, column...
- tb_ast_func: 1483 registros, colunas: project_name, version, file_path...

## Scripts lidos
- dev/sqlite/sqlite_sql_parse/tb_ast.sql: INSERT com CTE recursiva

## Observacoes
- tb_controle_ast nao existe no banco
- update_control existe com 4 registros
```

Nao se preocupe com formatacao — dados brutos sao suficientes.

---
name: session-plan-init-structure
description: Le template, exemplo e investigacao e gera o plano seguindo a estrutura exata do template
license: MIT
compatibility: opencode
metadata:
  audience: session-planner
  workflow: session-start
---

## Proposito

Ler o template vazio, o exemplo preenchido e o relatorio de investigacao, e gerar o plano de trabalho seguindo a estrutura exata do template.

## Input

Os dados veem do prompt:
- `plan_dir`: diretorio do plano
- `plan_pattern`: padrao de nome dos arquivos (ex: 260526_plan_sqlite_views_{version_number}.md)
- `investigate_file`: nome do arquivo de investigacao
- `version_number`: numero da versao (00, 01, etc.)
- `template_type`: (opcional) `database` ou `object_oriented` — se presente, ignora deteccao automatica

## Fluxo

### 1. Identificar tipo de projeto

Se o prompt contiver `template_type: database` ou `template_type: object_oriented`, use esse valor diretamente — ignore a deteccao automatica.

Se `template_type` nao estiver presente, leia `{plan_dir}/{investigate_file}` — o relatorio de investigacao — e determine o tipo:

- **database**: se o texto contiver palavras como `tabela`, `view`, `trigger`, `sql`, `banco`, `insert`, `schema`, `create table`
- **object_oriented**: se o texto contiver palavras como `classe`, `metodo`, `funcao`, `arquivo .dart`, `.py`, `.ts`, `heranca`, `interface`

Com base no tipo, defina:
- `template_file`: `_template_plan_db.md` (database) ou `_template_plan_oo.md` (object_oriented)
- `example_file`: `_template_plan_db_example.md` (database) ou `_template_plan_oo_example.md` (object_oriented)

### 2. Ler arquivos de referencia

1. Leia `.opencode/skills/session-plan-init-structure/{template_file}` com `read` — este e o template vazio com a estrutura exata.
2. Leia `.opencode/skills/session-plan-init-structure/{example_file}` com `read` — este e um exemplo preenchido corretamente para referir-se a ele.

### 3. Gerar o plano

Regras:
1. Siga EXATAMENTE a estrutura de secoes do template lido — mesmos nomes de secoes, mesma ordem.
2. Use o exemplo como referencia de estrutura e formatacao (lista aninhada, sem tabelas, sem ####).
3. Preencha as secoes de "## Referencias" e "## Esquemas e Estruturas Encontradas" (ou "## Funcoes de Negocio" + "## Estruturas Encontradas") e suas respectivas subseções com os dados do relatorio de investigacao.
4. Preencha as secoes ["## Modificacoes propostas", "## Plano de Acao"] e suas respectivas subseções com suas recomendações para que o objetivo do projeto seja atingido.
5. Nao adicione secoes alem das presentes no template.
6. Nao use tabelas markdown — use listas aninhadas (- item).
7. Nao adicione linhas `---` entre secoes.
8. Nao adicione `**Data:**` ou `**Versao:**` entre o titulo e as referencias.
9. Substitua `{variaveis}` pelos valores reais ao longo do texto.


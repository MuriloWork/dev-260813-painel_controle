---
name: session-plan-init-review
description: Compara o plano gerado com o exemplo e o template, reporta desvios encontrados
license: MIT
compatibility: opencode
metadata:
  audience: session-planner
  workflow: session-start
---

## Proposito

Comparar o plano gerado com o template e o exemplo, identificar desvios de estrutura e formato, e gerar um relatorio de revisao.

## Input

Os dados veem do prompt:
- `plan_dir`: diretorio do plano
- `plan_file`: nome do arquivo de plano gerado (ex: 260526_plan_sqlite_views_01.md)
- `review_file`: nome do arquivo de revisao a ser criado
- `template_file`: _template_plan_db.md (constante)
- `example_file`: _template_plan_db_example.md (constante)
- `template_dir`: .opencode/skills/session-plan-init-structure (constante)

## Fluxo

### 1. Ler arquivos

1. Leia `{template_dir}/{template_file}` — template vazio (estrutura esperada).
2. Leia `{template_dir}/{example_file}` — exemplo preenchido (formato esperado).
3. Leia `{plan_dir}/{plan_file}` — plano gerado a ser revisado.

### 2. Comparar e identificar desvios

Para cada secao do template, verifique no plano gerado:

| O que verificar        | Como detectar                                       |
| ---------------------- | --------------------------------------------------- |
| Secao presente?        | O heading exato existe no plano?                    |
| Nome da secao correto? | Comparar string do heading                          |
| Formato de lista?      | Usa `- ` em vez de (tabela) ou `####` (subheading)? |
| Secao extra?           | Ha heading no plano que nao existe no template?     |
| Elementos proibidos?   | Contem `---`, `**Data:**`, `**Versao:**`, (tabela)? |

### 3. Gerar relatorio de revisao

Crie o arquivo `{plan_dir}/{review_file}` com o formato:

```
# Revisao: {plan_file}

## Desvios Encontrados

### Secoes faltando
- `### Funcoes` — nao encontrada
- `## Modificacoes propostas` — nao encontrada

### Secoes com nome incorreto
- `### Tabelas Alvo` — deveria ser `### Tabelas`
- `### Views Existentes` — deveria ser `### Views`

### Secoes extras (nao previstas no template)
- `## Scripts Analisados`
- `## Observacoes Importantes`

### Problemas de formato
- Tabela markdown encontrada em `### Tabelas` (linhas 23-31)
- `####` usado em vez de `- ` em `### Tabelas`
- `---` horizontal rule entre secoes (linhas 6, 17, 125)

## Resumo
- Total de secoes no template: 9
- Secoes presentes corretamente: 5
- Secoes com desvio: 4
- Plano: REQUER CORRECAO / APROVADO
```

Se nenhum desvio for encontrado, o relatorio deve conter apenas:

```
# Revisao: {plan_file}

Nenhum desvio encontrado. Plano aprovado.
```

### 4. Regras de deteccao

- Um heading `### Views` no template deve corresponder exatamente a `### Views` no plano. `### Views Existentes` e desvio.
- Uma secao extra e qualquer `##` ou `###` que nao exista no template.
- O uso de `####` dentro de `### Tabelas` e desvio de formato (deveria ser `- `).
- Tabelas markdown (linhas com `|`) dentro de secoes sao desvio.

**Análise de Desvios: SRD_03 vs Documentos de Análise**

**Data:** 2026-06-29
**Objetivo:** Comparar a versão atual do SRD (`painel_controle_srd_03.md`) com as recomendações dos documentos de análise [arquitetura, pipeline, parse_md], listar desvios e priorizar correções.

---

# 1. Alinhamentos Confirmados ✅

## 1.1. Seção 3 (arquitetura do projeto)

| Item                                                                          | Origem                 | Situação                            |
| ----------------------------------------------------------------------------- | ---------------------- | ----------------------------------- |
| Layer frontend com `view_shell/painel_controle.ps1` + `painel_view.ps1`       | analise_arquitetura_02 | ✅ SRD lista ambos                   |
| Controllers separados: parse, session, sync                                   | analise_arquitetura_02 | ✅ SRD lista                         |
| Services/parse/ com md_ast_runner, md_ast_parser, script_raw, script_dart_ast | analise_arquitetura_02 | ✅ SRD lista                         |
| `dart_tools/` mantido em services/                                            | analise_arquitetura_02 | ✅ SRD confirma                      |
| `painel_settings.py` como shim compat                                         | analise_arquitetura_02 | ✅ SRD documenta                     |
| `_collect_text` em string_utils                                               | analise_arquitetura_02 | ✅ SRD lista                         |
| `pipeline_*.py` renomeados para `*_model.py`                                  | analise_arquitetura_02 | ✅ ast_dart_model, ast_md_model etc. |
| `utils_auth/` → `config/credentials/`                                         | analise_arquitetura_02 | ✅ SRD lista                         |
| `parse_docs/` → `dataMu/data_docs/data_docs_painel/`                          | analise_arquitetura_02 | ✅ SRD lista                         |
| Tabela de camadas final (frontend, backend, dados, agents, docs, temp)        | analise_pipeline_02    | ✅ SRD contém                        |

## 1.2. Seção 4 (arquitetura de funções)

| Item                                                                             | Origem              | Situação             |
| -------------------------------------------------------------------------------- | ------------------- | -------------------- |
| 4 seções h2 fixas: resumo, pipeline, automatic, agent                            | analise_pipeline_02 | ✅ SRD segue template |
| Pipeline com loop update SRD → parse → cross-reference → review                  | analise_pipeline_02 | ✅ SRD descreve       |
| Function groups (bootstrap, edit_md, parse, cross_reference, lint, session_loop) | analise_pipeline_02 | ✅ SRD lista          |

## 1.3. Seção 6 (descrições funcionais)

| Item                                              | Origem              | Situação                                    |
| ------------------------------------------------- | ------------------- | ------------------------------------------- |
| h3 com `script {path} [{funcao}]`                 | analise_pipeline_02 | ✅ SRD segue                                 |
| h4 com `classe {Nome} [{resp}]`                   | analise_pipeline_02 | ✅ SRD segue                                 |
| Tabela [metodo, assinatura, descricao]            | analise_pipeline_02 | ✅ SRD segue                                 |
| Scripts parse_md detalhados com classes e métodos | analise_pipeline_02 | ✅ SRD lista runner, parser, io, persistence |

---

# 2. Desvios Críticos 🔴

## 2.1. Seção 5 — Arquitetura de Dados: modelos JSON não especificados

**Origem:** analise_pipeline_02 (seção 4.5)
**Referência SRD:** seção 5.1.4 (modelos para code scripts)

| O que deveria ter                                                | O que tem                                                                   | Gap         |
| ---------------------------------------------------------------- | --------------------------------------------------------------------------- | ----------- |
| Tabela índice de schemas JSON [modelo, schema, dados, validação] | Nada. Só lista modelos Pydantic e schemas declarativos inline.              | **Ausente** |
| `dev/src/models/*.schema.json` referenciados                     | Nenhum arquivo .schema.json mencionado                                      | **Ausente** |
| Pipeline de validação de dados: jsonschema.validate()            | Nada sobre validação de JSON models                                         | **Ausente** |
| `dev/src/models/validation/` com scripts de verificação          | Camada `models/validation` na tabela de camadas mas sem conteúdo na seção 5 | **Ausente** |
| Distinção SQL (tabelas SRD) vs JSON (schema em arquivo)          | Secão 5 trata só modelos Pydantic e schemas inline do parser                | **Ausente** |

**Impacto:** A seção 5 não reflete a decisão de arquitetura tomada na sessão. SRD está desatualizado para JSON models.

USUARIO: 
- ajustar path para `dev/docs/spec/*.schema.json`
- 1 json para todos os schemas
- chave schema -> srd = schema name
- validation via cross reference 
- Pydantic -> json???

## 2.2. Seção 5 — `dev/src/tests/` sem conteúdo

**Origem:** analise_pipeline_02
**Referência SRD:** seção 3 (tabela de camadas) + seção 5

- Tabela de camadas cita `dev/src/tests/` como "testes de lógica, espelha src/"
- Seção 5 não tem subseção para testes
- Seção 6 não lista scripts de teste
- Nenhuma função `test_*` documentada

**Impacto:** Testes existem no conceito mas não no documento.

USUARIO:
- teste de disparo via painel 
- teste de validações 
- teste de parse [md, code]
- teste de build [md]
- teste de review [md, code]

## 2.3. `_collect_text` duplicado mesmo após refatoração

**Origem:** analise_arquitetura_02 (2.6) + analise_parse_md_00 (3.5)
**Referência SRD:** seção 6.2.5 (md_ast_persistence.py)

- SRD seção 6.2.4 lista `string_utils.py` com `collect_text` ✅
- SRD seção 6.2.5 lista `SaveOutputFiles` como classe de persistência
- analise_parse_md_00 (3.5) alerta que `md_ast_persistence.py` duplica `_collect_text()`
- SRD não deixa claro se a duplicação foi resolvida

**Recomendação original:** Remover duplicação, manter só em string_utils.
**Status no SRD:** Ambíguo. Precisa verificar código real.

## 2.4. Schema do parse_md.db desatualizado vs proposta nodes/edges

**Origem:** analise_parse_md_00 (seções 7.1.1 a 7.1.3)
**Referência SRD:** seção 5.1.2.2

| SRD atual (seção 5)                                   | Proposta analise_parse_md_00              |
| ----------------------------------------------------- | ----------------------------------------- |
| 3 tabelas com `json_data TEXT`                        | 3 tabelas: `nodes`, `edges`, `metadata`   |
| `tb_json_md_ast_blocks`                               | `nodes` (colunas estruturadas)            |
| `tb_json_md_ast_code`                                 | Eliminado (fundido em `nodes` com `kind`) |
| `tb_json_md_ast_tables`                               | Eliminado                                 |
| JSON intermediário em disco                           | Removido (insert direto)                  |
| 3 views (vw_md_doc, vw_md_ast_code, vw_md_ast_tables) | Substituído por queries diretas           |
| Versionamento por sobrescrita                         | `metadata` + `file_hash` + incremental    |

**Impacto:** SRD descreve arquitetura que a análise recomenda substituir. Se a refatoração for aprovada, seção 5 inteira do SRD precisará ser reescrita.

## 2.5. Views com `funcao` extraído de h2, mas bracket está em h3

**Origem:** analise_pipeline_02 (seção 2.4)
**Referência SRD:** seção 5.1.2.2.4 + 5.1.2.2.5 + 6.7 (scripts sql)

- Seção 5.1.2.2.4 (vw_md_doc): `funcao extraido do bracket do h2`
- Seção 5.1.2.2.5 (vw_md_ast_code): `funcao extraido do bracket do h2`
- Seção 6.7: `Views requerem atualizacao para incluir coluna funcao extraida do bracket do h2`
- **Mas** o template definido na seção 1.2.6 + seção 6 usa `h3 = script {path} [{funcao}]` — o bracket está no **h3**, não h2

**Inconsistência:** O parser descrito extrai funcao do h2, mas o template SRD_03 coloca funcao no h3. Views documentadas erram a fonte do dado.

## 2.6. `md_ast_parser.py` — God Method `_tokens_to_ast()` (207 linhas)

**Origem:** analise_parse_md_00 (3.1, 4.1)
**Referência SRD:** seção 6.2.3

- SRD lista `_tokens_to_ast` como método único
- análise recomenda extrair handlers: InlineHandler, ContainerHandler, CodeHandler, LeafHandler
- SRD não reflete essa recomendação (não é blocker, mas é gap de planejamento)

---

# 3. Desvios Médios 🟡

## 3.1. `dispatch()` monolítico em `md_ast_runner.py`

**Origem:** analise_parse_md_00 (3.4, 4.4)
**Referência SRD:** seção 6.2.2

- `MdAstRunner.dispatch()` tem 3 caminhos (md_ast, md_json, md_sqlite) em um método
- análise recomenda Strategy pattern ou classes separadas (AstAction, JsonAction, SqliteAction)
- SRD lista dispatch como método único, sem mencionar refatoração

## 3.2. Schema inline em `md_ast_parser.py`

**Origem:** analise_parse_md_00 (3.3, 4.3)
**Referência SRD:** seção 5.1.4.1

- `get_ast_model()` define schema como dict literal inline na classe
- análise recomenda mover para JSON externo ou dataclass versionado
- SRD cita `ast_model: dict declarativo` mas não indica plano de externalização

## 3.3. `parse_script_dart_ast.py` — nome ambíguo

**Origem:** analise_pipeline_02 (4.3)
**Referência SRD:** seção 3.2.2 + 6.3.2

- Nome sugere "parse de script ast para python", mas processa Dart
- SRD mantém nome original, sem sugestão de renomeação
- analise_pipeline_02 recomendava renomear para `parse_dart_code_ast.py` ou documentar

## 3.4. Acoplamento com MarkdownIt

**Origem:** analise_parse_md_00 (3.2, 4.2)
**Referência SRD:** seção 6.2.3

- `parse_file()` depende diretamente de `MarkdownIt('js-default')`
- análise recomenda Strategy pattern: `MdParser(Protocol)` → `MarkdownItParser`
- SRD não menciona plano de desacoplamento

## 3.5. `models/` vs `src/` — caminhos inconsistentes

**Origem:** analise_pipeline_02 (4.5.6)
**Referência SRD:** seção 3 (tabela de camadas)

| Tabela de camadas (seção 3)         | Seções 3.1-3.3 (detalhamento)                   |
| ----------------------------------- | ----------------------------------------------- |
| `{dev/src: tests}`                  | Seção 3 não lista pasta `tests/`                |
| `{dev/src/models: validation}`      | Seção 3.2.5 (src/models/) não lista validation/ |
| `{dev/docs: [docs, spec]}`          | Seção 3 não lista docs/                         |
| `{dev/agents: {agent_name}/skills}` | Seção 3 não lista agents/                       |

A tabela resume as camadas, mas o detalhamento das pastas (seções 3.1-3.3) não inclui `tests/`, `models/validation/`, `docs/` nem `agents/`.

---

# 4. Desvios Leves 🟢

## 4.1. Seção 1.2.1 atualizada vs PRD

**Origem:** analise_pipeline_02 (3.1)
**Referência SRD:** seção 1.2.1

- `template_PRD` citado como pendente de atualização para seguir formato SRD_03
- SRD não menciona se PRD já foi atualizado ou ainda é pendente

## 4.2. `sem_headers` não documentado

**Origem:** analise_pipeline_02 (2.4.1)
**Referência SRD:** seção 1.2.6

- Template da seção 6 usa `pasta {path}` como h2
- Template da seção 3 usa `layer {name}` como h2
- Em ambos os casos, a extração do `sem_headers` (h2 sem layer/pasta/scripts) não tem regra documentada de como o parser deve tratar

## 4.3. `sql_sqlite/.sql_tkinter/` pasta em desuso

**Origem:** analise_arquitetura_02
**Referência SRD:** seção 3.3.3

- SRD lista `src/sql_sqlite/.sql_tkinter/` como "pasta em desuso temporario"
- analise_arquitetura_02 recomenda mover pastas `.OLD *` para `src/delete/`
- `.sql_tkinter/` não foi movido nem recebeu ação de limpeza

---

# 5. Prioridades de Correção

## 5.1. 🔴 Imediatas (antes de planejar implantação)

| #   | Desvio                                                        | Ação                                                                          | Documento         |
| --- | ------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------- |
| 1   | Seção 5 sem índice de schemas JSON                            | Adicionar tabela índice [modelo, schema, dados, validação] em 5.1.4           | SRD               |
| 2   | Views com funcao extraída de h2 (errado — bracket está em h3) | Corrigir descrição das views: `funcao extraido do bracket do h3 (script)`     | SRD seção 5.1.2.2 |
| 3   | `dev/src/tests/` sem conteúdo                                 | Adicionar subseção em 5.1.4 ou seção própria detalhando a estrutura de testes | SRD               |
| 4   | `models/validation/` sem conteúdo                             | Adicionar detalhamento do que contém validation/                              | SRD               |

## 5.2. 🟡 Curto Prazo

| #   | Desvio                                                   | Ação                                                                                            | Documento     |
| --- | -------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------- |
| 5   | Schema parse_md.db desatualizado vs proposta nodes/edges | Decidir se refatora (nodes/edges) ou mantém (json_data). Se refatorar, reescrever seção 5.1.2.2 | SRD + analise |
| 6   | `_tokens_to_ast()` god method                            | Extrair handlers (InlineHandler, ContainerHandler, etc.)                                        | Plano         |
| 7   | dispatch() monolítico                                    | Separar em classes de ação (Strategy)                                                           | Plano         |
| 8   | Schema inline get_ast_model()                            | Externalizar para dataclass ou JSON                                                             | Plano         |
| 9   | Acoplamento MarkdownIt                                   | Implementar MdParser protocol                                                                   | Plano         |
| 10  | `docs/` e `agents/` sem detalhamento                     | Adicionar na seção 3 (arquitetura do projeto)                                                   | SRD           |

## 5.3. 🟢 Quando conveniente

| #   | Desvio                                  | Ação                                  |
| --- | --------------------------------------- | ------------------------------------- |
| 11  | `parse_script_dart_ast.py` nome ambíguo | Renomear ou documentar explicitamente |
| 12  | `sql_sqlite/.sql_tkinter/` em desuso    | Mover para `temp/` ou `delete/`       |
| 13  | `sem_headers` sem regra documentada     | Adicionar regra no template da seção  |

---

# 6. Resumo

| Categoria          | Qtde | Críticos                                                                                                                 |
| ------------------ | ---- | ------------------------------------------------------------------------------------------------------------------------ |
| Alinhamentos       | 14   | —                                                                                                                        |
| Desvios críticos 🔴 | 6    | Seção 5 sem schemas JSON, views com funcao errada, sem testes, sem validation, schema parse_md desatualizado, god method |
| Desvios médios 🟡   | 5    | dispatch monolítico, schema inline, nome ambíguo, acoplamento, camadas sem detalhamento                                  |
| Desvios leves 🟢    | 3    | PRD pendente, sem_headers, pasta em desuso                                                                               |

**Os 4 desvios imediatos** (índice JSON, views funcao, tests, validation) precisam ser corrigidos no SRD antes de prosseguir com planejamento de implantação, pois afetam diretamente a seção 5 (arquitetura de dados) que ainda está desatualizada.

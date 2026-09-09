**Análise de Arquitetura v3 — Incorporando USUARIO_02**

# 1. Escopo da Sessão

Plano dividido em **2 etapas**:

| Etapa       | Descrição                                                                           |
| ----------- | ----------------------------------------------------------------------------------- |
| **Etapa 1** | Criar novas pastas + mover arquivos + ajustar códigos para restaurar funcionalidade |
| **Etapa 2** | Criar novos arquivos + refatorar códigos (melhorias estruturais)                    |

---

# 2. Problemas Detectados — Revisados

## 2.1. `painel_controle.ps1` — Monolito Frontend (291 linhas)

Faz **três coisas distintas** no mesmo arquivo:

| Responsabilidade   | O que faz                                                                                  |
| ------------------ | ------------------------------------------------------------------------------------------ |
| **Bootstrap/Init** | Carrega `.env.base`, resolve `painelRoot`, valida ambiente                                 |
| **View (UI)**      | `Show-Menu` — renderiza menu no terminal                                                   |
| **Controller**     | `Run-ShellCommand` — dispatches comandos, resolve placeholders, monta pipeline de execução |

**Decisão USUARIO_01:** PS1 deve ser responsável **apenas** por orquestrar UI
e disparar ações selecionadas nos painéis.

**Recomendação revisada:**
- `view_shell/painel_controle.ps1` — orquestração fina (menu + dispatch)
- `view_shell/painel_view.ps1` — renderização de menu
- `view_shell/painel_input.ps1` — input handling
- **Bootstrap/init** → `utils/init_utils/env_loader.py`

## 2.2. `painel_settings.py` — Config Overloader (257 linhas)

Mistura **4 responsabilidades**:

| Responsabilidade                         | Linhas  |
| ---------------------------------------- | ------- |
| Constantes de path (hardcoded)           | 7–24    |
| Leitura/parse de `.env` e JSON           | 74–101  |
| Resolução de paths relativos → absolutos | 104–230 |
| Acesso a config de ações e menu          | 245–257 |

**Decisão USUARIO_01:** utils são serviços comuns consumidos por outros scripts.
Utils renomeado com subpastas por domínio.

**Recomendação revisada:**
- `utils/init_utils/env_loader.py` — leitura de `.env`
- `utils/parse_utils/path_resolver.py` — resolução de paths (absorve de `parse_utils.py`)
- `utils/io_utils/config_io.py` — acesso a JSON de configuração (ler/escrever)

## 2.3. `parse_md_ast.py` — Gigante de Parser (655 linhas)

Mistura **orquestração CLI + parse + persistência + schema inline**:

| Classe                             | Responsabilidade real                |
| ---------------------------------- | ------------------------------------ |
| `Initialize`                       | CLI e dispatch                       |
| `ReadInputFiles`                   | Scan de arquivos (IO)                |
| `GenerateAst`                      | Parse de Markdown (regra de negócio) |
| `SaveOutputFiles`                  | Persistência (JSON + SQLite + views) |
| `_INLINE_SCHEMAS` e `_load_schema` | Definição de schema (modelo)         |

**Divisão de responsabilidades por arquivo — versão final:**

| Arquivo                                | Camada  | Responsabilidade                                                 |
| -------------------------------------- | ------- | ---------------------------------------------------------------- |
| `services/parse/md_ast_runner.py`      | Service | Orquestração: CLI args, dispatch para parser, chama persistência |
| `services/parse/md_ast_parser.py`      | Service | Parse lógico: `GenerateAst` + `_tokens_to_ast`                   |
| `services/parse/script_dart_ast.py`    | Service | Parse de AST Dart (já existe, manter)                            |
| `services/parse/script_raw.py`         | Service | Parse de script raw (já existe, manter)                          |
| `utils/io_utils/md_ast_io.py`          | Utils   | Scan de arquivos (`ReadInputFiles`)                              |
| `utils/io_utils/md_ast_persistence.py` | Utils   | Persistência (`SaveOutputFiles`: JSON + SQLite)                  |

**Decisão USUARIO_02:** `md_ast_io.py` e `md_ast_persistence.py` são serviços
comuns de IO — movidos para `utils/io_utils/`.

**Análise de redundância com `utils/io_utils/` existentes:**

| Utils existente           | Relação com `md_ast_persistence.py`                                                                                                     |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `painel_sqlite_import.py` | Base genérica de upsert SQLite. `md_ast_persistence.py` é específico para AST (schema mapping + views). Podem coexistir sem duplicação. |
| `painel_sqlite_export.py` | Exporta SQLite para XLSX. Não há overlap.                                                                                               |
| `parse_export.py`         | `validate_to_model` usado por `SaveOutputFiles.save_all`. `md_ast_persistence` consumiria esta função, sem duplicar.                    |

**Conclusão:** Sem redundância, desde que `md_ast_persistence.py` consuma
`parse_export` e `painel_sqlite_import` em vez de duplicar a lógica.

## 2.4. `parse_model_pydantic.py` — Schema + Geração + Validação (395 linhas)

| Função                                  | Responsabilidade                 |
| --------------------------------------- | -------------------------------- |
| `infer_json_schema` / `finalize_schema` | Análise de schema (inteligência) |
| `generate_pydantic_code`                | Geração de código (template)     |
| `validate_json_with_pydantic`           | Validação (execução)             |

**Decisão USUARIO_02 — Investigação de código morto:**

- `schema_inferrer.py`: as funções `infer_json_schema()` + `finalize_schema()`
  são chamadas por `main()` no mesmo arquivo. **Confirmar se `main()` é
  executado** (via `__name__ == "__main__"` ou importado por outro script).
   Se `main()` nunca é chamado no pipeline, estas funções são **código morto**
   e devem ser movidas para `src/delete/`.

- `pydantic_codegen.py`: `generate_pydantic_code()` também é chamado apenas
  por `main()`. Mesma dependência.

- `ast_validator.py`: **Removido da proposta.** Pydantic já valida com 1 linha
  (`model.model_validate(data)`). A validação com dispatch por `type` já está
  encapsulada em `BaseASTNode.model_validate()` no próprio modelo gerado. Não
  justifica um arquivo separado.

**Recomendação final para `parse_model_pydantic.py`:**

| Situação                                                   | Ação                                                                       |
| ---------------------------------------------------------- | -------------------------------------------------------------------------- |
| `main()` é chamado por outro script (ex: service de parse) | Manter como `models/pydantic_tools.py` (nomes de funções auto-descritivos) |
| `main()` só roda como script standalone                    | Manter inalterado, não refatorar. Código não crítico para a arquitetura.   |
| `main()` não é usado por ninguém                           | Mover para `src/delete/`                                                    |

## 2.5. Arquivos `pipeline_*.py` — Nomes não indicam que são modelos

| Arquivo atual            | Sugestão                     |
| ------------------------ | ---------------------------- |
| `pipeline_ast_dart.py`   | `models/ast_dart_model.py`   |
| `pipeline_ast_md.py`     | `models/ast_md_model.py`     |
| `pipeline_export.py`     | `models/export_model.py`     |
| `pipeline_import.py`     | `models/import_model.py`     |
| `pipeline_raw_script.py` | `models/raw_script_model.py` |

## 2.6. `_collect_text` duplicado

Presente em `parse_md_ast.py:480`. Mover para
`utils/parse_utils/string_utils.py`.

## 2.7. `sql_sqlite` duplicado

**Decisão USUARIO_02:** Conforme verificação, `dev\src\painel\sql_sqlite\` **não
existe**. Ação removida.

---

# 3. Análise do Plano Proposto — Revisada

## 3.1. O que está ALINHADO ✅

| Mudança proposta                        | Motivo                                          |
| --------------------------------------- | ----------------------------------------------- |
| `painel_controle.ps1` → `view_shell\`   | Separa frontend do backend                      |
| `painel\services\` → `services\` (raiz) | Services como camada independente               |
| `painel\models\` → `models\` (raiz)     | Models como camada independente                 |
| `dbMu\*.db` → `dbMu\sqlite\*.db`        | Dados organizados por tipo                      |
| `painel\config\` → `repositories\`      | Config JSON vira repositório de dados de config |

## 3.2. O que precisa ser REVISADO ⚠️

| Mudança proposta                                 | Decisão final                                                                                                      |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `painel_settings.py` → `services\painel_init.py` | Separar em `utils/init_utils/env_loader.py` + `utils/parse_utils/path_resolver.py` + `utils/io_utils/config_io.py` |
| `dart_tools` → `tools\dart_tools\`               | **Manter em `services/dart_tools/`** — são scripts de parse chamados como serviço                                  |
| `painel\config\schemas\` → `repositories\`       | **Mover para `models/schemas/`** — schemas são modelos de dados                                                    |
| `utils_auth\` → `repositories\`                  | **Mover para `config/credentials/`** — são credenciais, não repositório                                            |

## 3.3. O que está INCORRETO ❌

| Mudança proposta                   | Decisão final                                                                          |
| ---------------------------------- | -------------------------------------------------------------------------------------- |
| `parse_docs\` → `dbMu\doc_painel\` | `parse_docs` contém outputs de parse. Novo local: `dataMu/data_docs/data_docs_painel/` |

---

# 4. Proposta de Arquitetura Final (revisada v3)

```
dev/
├── src/
│   ├── view_shell/                 # FRONTEND — interface de terminal
│   │   ├── painel_controle.ps1     # Orquestrador fino (menu + dispatch)
│   │   ├── painel_view.ps1         # Renderização de menu
│   │   └── painel_input.ps1        # Input handling
│   │
│   ├── controllers/                # THIN CONTROLLERS — dispatch CLI
│   │   ├── shell_controller.ps1
│   │   ├── parse_controller.py
│   │   ├── session_controller.py
│   │   └── sync_controller.py
│   │
│   ├── services/                   # SERVICES — regras de negócio
│   │   ├── logs/
│   │   ├── parse/
│   │   │   ├── md_ast_runner.py    # orquestração
│   │   │   ├── md_ast_parser.py    # parse lógico
│   │   │   ├── script_dart_ast.py  # parse de AST Dart (já existe)
│   │   │   └── script_raw.py       # parse de script raw (já existe)
│   │   ├── sessions/
│   │   ├── sync/
│   │   └── dart_tools/             # scripts Dart CLI
│   │       ├── parse_dart_ast.dart
│   │       └── validate_schema.dart
│   │
│   ├── models/                     # MODELS — dados e schemas
│   │   ├── schemas/                # schemas JSON
│   │   │   ├── schema_md_blocks.json
│   │   │   ├── schema_md_code.json
│   │   │   └── schema_md_tables.json
│   │   ├── ast_dart_model.py       # models de AST Dart
│   │   ├── ast_md_model.py         # models de AST Markdown
│   │   ├── export_model.py         # models de exportação
│   │   ├── import_model.py         # models de importação
│   │   ├── raw_script_model.py     # models de script raw
│   │   └── pydantic_tools.py       # [se for usado] schema inference + codegen
│   │
│   ├── repositories/               # REPOSITORIES — acesso a dados
│   │   ├── config_repo.py          # leitura/escrita de JSON config
│   │   └── ast_repo.py             # persistência AST (JSON + SQLite)
│   │
│   ├── utils/                      # UTILITIES — serviços comuns
│   │   ├── init_utils/
│   │   │   └── env_loader.py       # .env loading
│   │   ├── parse_utils/
│   │   │   ├── path_resolver.py    # path resolution
│   │   │   └── string_utils.py     # _collect_text e afins
│   │   └── io_utils/
│   │       ├── config_io.py        # leitura/escrita de JSON config
│   │       ├── md_ast_io.py        # file scanning (ReadInputFiles)
│   │       ├── md_ast_persistence.py # persistência AST
│   │       ├── parse_export.py
│   │       ├── painel_sqlite_export.py
│   │       └── painel_sqlite_import.py
│   │
│   ├── config/                     # CONFIG — dados de configuração (JSON)
│   │   ├── credentials/            #   gitignore
│   │   │   ├── client_secret.json
│   │   │   ├── google_oauth_tokens.json
│   │   │   └── service_account.json
│   │   ├── set_painel_pipeline_paths.json
│   │   ├── set_painel_actions_data_paths.json
│   │   ├── set_painel_menu.json
│   │   └── (schemas → models/schemas/)
│   │
│   └── sql_sqlite/                 # SQL — scripts DDL/views
│       ├── sql_parse_md/
│       └── sql_parse_script/
│
├── dataMu/                         # DATA — dados do projeto
│   ├── dbMu/
│   │   └── sqlite/
│   │       ├── parse_dart.db
│   │       └── parse_md.db
│   └── data_docs/
│       └── data_docs_painel/       # docs como dados [json, csv, xlsx]
│           ├── json_md_ast/
│           ├── json_script_dart_ast/
│           ├── json_script_dart_ast_func/
│           ├── json_script_raw/
│           └── logs/
│
└── tests/                          # TESTES
    └── (test files)
```

---

# 5. Resumo de Ações Recomendadas (dividido em 2 etapas)

## 5.1. Etapa 1 — Pastas + Mover + Ajustar (funcionalidade primeiro)

| #   | Ação                                                                                                                                                           | Prioridade |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 1   | Criar `view_shell/`, `controllers/`, `utils/init_utils/`, `utils/parse_utils/`, `utils/io_utils/`, `dataMu/data_docs/data_docs_painel/`, `dataMu/dbMu/sqlite/` | Alta       |
| 2   | Mover `painel_controle.ps1` → `view_shell/`                                                                                                                    | Alta       |
| 3   | Mover `painel_settings.py` → separar em `env_loader.py`, `path_resolver.py`, `config_io.py`                                                                    | Alta       |
| 4   | Mover `services/parse/*` → `services/parse/` (manter estrutura)                                                                                                | Alta       |
| 5   | Mover `models/pipeline_*.py` → `models/*_model.py` (renomear)                                                                                                  | Alta       |
| 6   | Mover `dart_tools/` → `services/dart_tools/`                                                                                                                   | Alta       |
| 7   | Mover `config/schemas/` → `models/schemas/`                                                                                                                    | Alta       |
| 8   | Mover `utils_auth/` → `config/credentials/`                                                                                                                    | Alta       |
| 9   | Mover `parse_docs/` outputs → `dataMu/data_docs/data_docs_painel/`                                                                                             | Alta       |
| 10  | Mover `set_painel_*.json` → `config/` (e schemas → `models/schemas/`)                                                                                          | Alta       |
| 11  | Mover pastas `.OLD *` para `src/delete/`                                                                                                                               | Média      |

## 5.2. Etapa 2 — Refatoração e novos arquivos

| #   | Ação                                                                               | Prioridade |
| --- | ---------------------------------------------------------------------------------- | ---------- |
| 12  | Extrair `_collect_text` para `utils/parse_utils/string_utils.py`                   | Média      |
| 13  | Separar `parse_md_ast.py` em runner + parser + io_utils + persistence_utils        | Alta       |
| 14  | Investigar se `parse_model_pydantic.py.main()` é código morto; decidir refatoração | Média      |
| 15  | Renomear `pipeline_*.py` conforme convenção `*_model.py`                           | Média      |

---

# 6. Conceitos — Esclarecimentos

## 6.1. Repositories

Camada de **acesso a dados persistentes** (JSON, SQLite, CSV, XLSX).
Responsabilidades:
- CRUD em arquivos JSON de configuração
- Inserir/consultar dados em SQLite
- Encapsular a lógica de IO (quem chama não precisa saber se é JSON ou SQLite)

Não contêm regras de negócio — apenas **persistência e recuperação**.

## 6.2. Config

Camada de **configuração estática + credenciais**.
Responsabilidades:
- Credenciais (client_secret, tokens OAuth)
- Constantes de ambiente
- Tudo que é sensível (gitignore) ou imutável em tempo de execução

## 6.3. DataMu

Camada de **dados persistentes do projeto**, dividida em:
- `dbMu/` — bancos SQLite
- `data_docs/` — documentos de dados, com subpastas por domínio:
  - `data_docs_painel/` — outputs de parse em JSON, CSVs, logs

---

# 7. `set_painel_*.json` — Onde ficam?

## 7.1. Situação atual

| Arquivo                                     | Path atual                       |
| ------------------------------------------- | -------------------------------- |
| `set_painel_pipeline_paths.json`            | `dev\src\painel\config\`         |
| `set_painel_actions_data_paths.json`        | `dev\src\painel\config\`         |
| `set_painel_menu.json`                      | `dev\src\painel\config\`         |
| `set_painel_actions_data_paths_schema.json` | `dev\src\painel\config\schemas\` |
| `set_painel_pipeline_paths_schema.json`     | `dev\src\painel\config\schemas\` |

## 7.2. Proposta

| Arquivo                                     | Novo path                                   | Justificativa               |
| ------------------------------------------- | ------------------------------------------- | --------------------------- |
| `set_painel_pipeline_paths.json`            | `config/set_painel_pipeline_paths.json`     | Config de ambiente/pipeline |
| `set_painel_actions_data_paths.json`        | `config/set_painel_actions_data_paths.json` | Config de paths de dados    |
| `set_painel_menu.json`                      | `config/set_painel_menu.json`               | Config de estrutura de menu |
| `set_painel_actions_data_paths_schema.json` | `models/schemas/...`                        | Schema é modelo             |
| `set_painel_pipeline_paths_schema.json`     | `models/schemas/...`                        | Schema é modelo             |

**Quem lê:** `repositories/config_repo.py` faz o IO destes arquivos.
**Quem consome:** `utils/init_utils/env_loader.py` e `utils/parse_utils/path_resolver.py`
usam o `config_repo.py` para obter os dados.

---

# 8. Decisões USUARIO_02 — Resumo

| #   | Comentário                                                               | Decisão aplicada                                      |
| --- | ------------------------------------------------------------------------ | ----------------------------------------------------- |
| 1   | `md_ast_io.py` e `md_ast_persistence.py` devem ir para `utils/io_utils/` | Movidos na árvore. Análise de redundância incluída.   |
| 2   | `schema_inferrer.py` e `pydantic_codegen.py` podem ser código morto      | Ação #14: investigar. Se não usado, mover para `src/delete/`. |
| 3   | `ast_validator.py` é redundante com Pydantic nativo                      | Removido da proposta.                                 |
| 4   | `dev\src\painel\sql_sqlite\` não existe                                  | Ação removida.                                        |
| 5   | Path correto: `dataMu/data_docs/data_docs_painel/`                       | Atualizado na árvore e ações.                         |

---

# 9. Próximos Passos

1. Validar este documento com USUARIO_01
2. Iniciar Etapa 1 (criar pastas + mover + ajustar imports)
3. Testar funcionalidade básica após cada movimentação
4. Iniciar Etapa 2 (refatoração)

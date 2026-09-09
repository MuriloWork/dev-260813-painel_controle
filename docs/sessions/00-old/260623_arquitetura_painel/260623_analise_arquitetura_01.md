**Análise de Arquitetura v2 — SRP + Comentários USUARIO_01**

# 1. Escopo da Sessão

Com base no feedback do USUARIO_01, o plano de reorganização será dividido em
**2 etapas**:

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

**Missing no PRD:** `parse_script_dart_ast.py` e `parse_script_raw.py` precisam ser mapeados. Ambos estão em `services/parse/` e seguem o mesmo padrão — devem ser incluídos na nova estrutura.

**Divisão de responsabilidades por arquivo (revisada):**

| Arquivo                                | Responsabilidade                                                 |
| -------------------------------------- | ---------------------------------------------------------------- |
| `services/parse/md_ast_runner.py`      | Orquestração: CLI args, dispatch para parser, chama persistência |
| `services/parse/md_ast_parser.py`      | Parse lógico: `GenerateAst` + `_tokens_to_ast`                   |
| `services/parse/md_ast_io.py`          | IO: `ReadInputFiles` (scan de arquivos)                          |
| `services/parse/md_ast_persistence.py` | Persistência: `SaveOutputFiles` (JSON + SQLite)                  |
| `services/parse/script_dart_ast.py`    | Parse de AST Dart (já existe, manter)                            |
| `services/parse/script_raw.py`         | Parse de script raw (já existe, manter)                          |

**Schemas inline** (`_INLINE_SCHEMAS`) → `models/schemas/` (arquivos .json já existentes, remover fallback inline).

USUARIO: se [md_ast_io.py, md_ast_persistence.py] são serviços comuns devem estar em `utils/utils_io` mas também é necessario avaliar se teriam redundancia com os scripts já previstos para `utils/utils_io`

## 2.4. `parse_model_pydantic.py` — Schema + Geração + Validação (395 linhas)

| Função                                  | Responsabilidade                 |
| --------------------------------------- | -------------------------------- |
| `infer_json_schema` / `finalize_schema` | Análise de schema (inteligência) |
| `generate_pydantic_code`                | Geração de código (template)     |
| `validate_json_with_pydantic`           | Validação (execução)             |

**Comentário USUARIO_01:** validar se o nome do arquivo reflete a responsabilidade. O nome atual (`parse_model_pydantic.py`) sugere "modelo de parse para Pydantic", mas o arquivo faz **inferência + geração + validação**.

**Recomendação revisada:** Dividir em 3 arquivos com nomes auto-descritivos:

| Novo arquivo                      | Responsabilidade                            |
| --------------------------------- | ------------------------------------------- |
| `models/schema_inferrer.py`       | Infere schema de ASTs a partir de JSON      |
| `models/pydantic_codegen.py`      | Gera código Pydantic a partir do schema     |
| `utils/io_utils/ast_validator.py` | Valida AST contra modelo Pydantic carregado |

**Sobre o local do validador:** O USUARIO_01 notou que "validation" não é um serviço em si. Correto — a validação de AST contra modelo é uma **utilidade de IO** (recebe dados, valida, retorna). Mover para `utils/io_utils/`.

USUARIO:
- sobre [schema_inferrer.py, pydantic_codegen.py]: talvez sejam codigos mortos, precisamos confirmar se/onde estao sendo usados no pipeline
- ast_validator.py: faz sentido um script para validar contra modelo pydantic, se ele já é naturalmente validado com 1 linha de codigo?

## 2.5. Arquivos `pipeline_*.py` — Nomes não indicam que são modelos

Arquivos atuais em `models/`:

| Arquivo atual            | Problema                             | Sugestão                     |
| ------------------------ | ------------------------------------ | ---------------------------- |
| `pipeline_ast_dart.py`   | Nome sugere "pipeline", não "modelo" | `models/ast_dart_model.py`   |
| `pipeline_ast_md.py`     | Nome sugere "pipeline", não "modelo" | `models/ast_md_model.py`     |
| `pipeline_export.py`     | Nome genérico                        | `models/export_model.py`     |
| `pipeline_import.py`     | Nome genérico                        | `models/import_model.py`     |
| `pipeline_raw_script.py` | Nome genérico                        | `models/raw_script_model.py` |

**Convenção:** `models/<dominio>_model.py` para arquivos que definem
estruturas de dados (Pydantic, dataclasses, typed dicts).

## 2.6. `_collect_text` duplicado

Presente em `parse_md_ast.py:480`. Deve ser movido para utils.

**Recomendação:** Mover para `utils/parse_utils/path_resolver.py` ou
`utils/parse_utils/string_utils.py`.

## 2.7. `sql_sqlite` duplicado

`dev\src\painel\sql_sqlite\` e `dev\src\sql_sqlite\` — remover o duplicado.

USUARIO: `dev\src\painel\sql_sqlite\` não existe, essa ação não é necessaria
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

| Mudança proposta                                 | Decisão USUARIO_01                                                                                                 |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `painel_settings.py` → `services\painel_init.py` | Separar em `utils/init_utils/env_loader.py` + `utils/parse_utils/path_resolver.py` + `utils/io_utils/config_io.py` |
| `dart_tools` → `tools\dart_tools\`               | **Manter em `services/dart_tools/`** — são scripts de parse chamados como serviço                                  |
| `painel\config\schemas\` → `repositories\`       | **Mover para `models/schemas/`** — schemas são modelos de dados                                                    |
| `utils_auth\` → `repositories\`                  | **Mover para `config/credentials/`** — são credenciais, não repositório                                            |

## 3.3. O que está INCORRETO ❌

| Mudança proposta                   | Decisão USUARIO_01                                                           |
| ---------------------------------- | ---------------------------------------------------------------------------- |
| `parse_docs\` → `dbMu\doc_painel\` | `parse_docs` contém outputs de parse. Novo local: `dataMu/data_docs_painel/` |

USUARIO: local correto `dataMu/data_docs/data_docs_painel/`

## 3.4. Sobre `controllers/` — Esclarecimento

USUARIO_01 perguntou: **"responsabilidade = CLI?"**

Sim — `controllers/` são scripts responsáveis por:
- Receber o comando vindo do painel (frontend)
- Parsear argumentos (CLI)
- Chamar o service apropriado
- Retornar resultado para exibição

Não contêm regras de negócio — são **orquestradores finos** (thin controllers).

Exemplo: `parse_controller.py` recebe `--action md_ast --input path/`, chama
`services/parse/md_ast_runner.py`, retorna status.

---

# 4. Proposta de Arquitetura Final (revisada)

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
│   │   │   ├── md_ast_io.py        # file scanning
│   │   │   ├── md_ast_persistence.py # persistência
│   │   │   ├── parse_script_dart_ast.py  # já existe
│   │   │   └── parse_script_raw.py       # já existe
│   │   ├── sessions/
│   │   ├── sync/
│   │   └── dart_tools/             # scripts Dart CLI (mantido em services/)
│   │       ├── parse_dart_ast.dart
│   │       └── validate_schema.dart
│   │
│   ├── models/                     # MODELS — dados e schemas
│   │   ├── schemas/                # schemas JSON
│   │   │   ├── schema_md_blocks.json
│   │   │   ├── schema_md_code.json
│   │   │   └── schema_md_tables.json
│   │   ├── schema_inferrer.py      # infere schema de ASTs
│   │   ├── pydantic_codegen.py     # gera código Pydantic
│   │   ├── ast_dart_model.py       # models de AST Dart
│   │   ├── ast_md_model.py         # models de AST Markdown
│   │   ├── export_model.py         # models de exportação
│   │   ├── import_model.py         # models de importação
│   │   └── raw_script_model.py     # models de script raw
│   │
│   ├── repositories/               # REPOSITORIES — acesso a dados
│   │   ├── config_repo.py          # leitura/escrita de JSON config
│   │   └── ast_repo.py             # persistência AST (JSON + SQLite)
│   │
│   ├── utils/                      # UTILITIES — serviços comuns
│   │   ├── init_utils/
│   │   │   └── env_loader.py       # .env loading
│   │   ├── parse_utils/
│   │   │   ├── path_resolver.py    # path resolution (+ herda de parse_utils.py)
│   │   │   └── string_utils.py     # _collect_text e afins
│   │   └── io_utils/
│   │       ├── config_io.py        # leitura/escrita de JSON config
│   │       ├── ast_validator.py    # valida AST contra modelo Pydantic
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
│   └── data_docs_painel/           # docs como dados [json, csv, xlsx]
│       ├── json_md_ast/
│       ├── json_script_dart_ast/
│       ├── json_script_dart_ast_func/
│       ├── json_script_raw/
│       └── logs/
│
└── tests/                          # TESTES
    └── (test files)
```

---

# 5. Resumo de Ações Recomendadas (dividido em 2 etapas)

## 5.1. Etapa 1 — Pastas + Mover + Ajustar (funcionalidade primeiro)

| #   | Ação                                                                                                                                                 | Prioridade |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 1   | Criar `view_shell/`, `controllers/`, `utils/init_utils/`, `utils/parse_utils/`, `utils/io_utils/`, `dataMu/data_docs_painel/`, `dataMu/dbMu/sqlite/` | Alta       |
| 2   | Mover `painel_controle.ps1` → `view_shell/`                                                                                                          | Alta       |
| 3   | Mover `painel_settings.py` → separar em `env_loader.py`, `path_resolver.py`, `config_io.py`                                                          | Alta       |
| 4   | Mover `services/parse/*` → `services/parse/` (já está, manter)                                                                                       | Alta       |
| 5   | Mover `models/pipeline_*.py` → `models/*_model.py` (renomear)                                                                                        | Alta       |
| 6   | Mover `dart_tools/` → `services/dart_tools/`                                                                                                         | Alta       |
| 7   | Mover `config/schemas/` → `models/schemas/`                                                                                                          | Alta       |
| 8   | Mover `utils_auth/` → `config/credentials/`                                                                                                          | Alta       |
| 9   | Mover `parse_docs/` outputs → `dataMu/data_docs_painel/`                                                                                             | Alta       |
| 10  | Remover `src/painel/sql_sqlite/` duplicado                                                                                                           | Alta       |
| 11  | Mover `set_painel_*.json` → `config/` (e schemas → `models/schemas/`)                                                                                | Alta       |
| 12  | Remover/arquivar pastas `.OLD *`                                                                                                                     | Média      |

## 5.2. Etapa 2 — Refatoração e novos arquivos

| #   | Ação                                                                | Prioridade |
| --- | ------------------------------------------------------------------- | ---------- |
| 13  | Extrair `_collect_text` para `utils/parse_utils/string_utils.py`    | Média      |
| 14  | Separar `parse_md_ast.py` em runner + parser + io + persistence     | Alta       |
| 15  | Separar `parse_model_pydantic.py` em inferrer + codegen + validator | Média      |
| 16  | Renomear `pipeline_*.py` conforme convenção `*_model.py`            | Média      |

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
- `data_docs_painel/` — documentos de dados (outputs de parse em JSON, CSVs, logs)

# 7. `set_painel_*.json` — Onde ficam?

## 7.1. Situação atual

| Arquivo                                     | Path atual                       |
| ------------------------------------------- | -------------------------------- |
| `set_painel_pipeline_paths.json`            | `dev\src\painel\config\`         |
| `set_painel_actions_data_paths.json`        | `dev\src\painel\config\`         |
| `set_painel_menu.json`                      | `dev\src\painel\config\`         |
| `set_painel_actions_data_paths_schema.json` | `dev\src\painel\config\schemas\` |
| `set_painel_pipeline_paths_schema.json`     | `dev\src\painel\config\schemas\` |

## 7.2. Problema

Estes são **dados de configuração** (JSON), não código Python. Estão
misturados com `painel_settings.py` (código) e `schemas/` (modelos).

## 7.3. Proposta

| Arquivo                                     | Novo path                                                  | Justificativa               |
| ------------------------------------------- | ---------------------------------------------------------- | --------------------------- |
| `set_painel_pipeline_paths.json`            | `config/set_painel_pipeline_paths.json`                    | Config de ambiente/pipeline |
| `set_painel_actions_data_paths.json`        | `config/set_painel_actions_data_paths.json`                | Config de paths de dados    |
| `set_painel_menu.json`                      | `config/set_painel_menu.json`                              | Config de estrutura de menu |
| `set_painel_actions_data_paths_schema.json` | `models/schemas/set_painel_actions_data_paths_schema.json` | Schema é modelo             |
| `set_painel_pipeline_paths_schema.json`     | `models/schemas/set_painel_pipeline_paths_schema.json`     | Schema é modelo             |

**Quem lê:** `repositories/config_repo.py` faz o IO destes arquivos.
**Quem consome:** `utils/init_utils/env_loader.py` e `utils/parse_utils/path_resolver.py`
usam o `config_repo.py` para obter os dados.

## 7.4. Arquitetura revisada (extraindo os JSON de config)

```
dev/
├── src/
│   ├── config/                     # CONFIG DATA — arquivos .json de configuração
│   │   ├── credentials/            #   gitignore
│   │   ├── set_painel_pipeline_paths.json
│   │   ├── set_painel_actions_data_paths.json
│   │   └── set_painel_menu.json
│   │
│   ├── repositories/               # REPOSITORIES — código que acessa dados
│   │   ├── config_repo.py          #   lê/escreve set_painel_*.json
│   │   └── ast_repo.py             #   persiste AST em JSON + SQLite
```

**Importante:** Os schemas (`*_schema.json`) vão para `models/schemas/` porque
definem a **estrutura/contrato** dos dados, não são config em si.

---

# 8. Próximos Passos

1. Validar este documento com USUARIO_01
2. Iniciar Etapa 1 (criar pastas + mover + ajustar imports)
3. Testar funcionalidade básica após cada movimentação
4. Iniciar Etapa 2 (refatoração)

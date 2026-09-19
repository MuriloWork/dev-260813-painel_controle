**Análise de Arquitetura — SRP (Single Responsibility Policy)**

# 1. Resumo

Análise da arquitetura atual do projeto "painel controle" e do plano de
reorganização proposto no PRD (`260623_arquitetura_painel_prd_00.md`), com foco
no princípio SRP (cada módulo/pasta deve ter **uma única responsabilidade
bem definida**).

---

# 2. Problemas Detectados na Arquitetura Atual

## 2.1. `painel_controle.ps1` — Monolito Frontend (291 linhas)

Faz **três coisas distintas** no mesmo arquivo:

| Responsabilidade   | O que faz                                                                                  |
| ------------------ | ------------------------------------------------------------------------------------------ |
| **Bootstrap/Init** | Carrega `.env.base`, resolve `painelRoot`, valida ambiente                                 |
| **View (UI)**      | `Show-Menu` — renderiza menu no terminal                                                   |
| **Controller**     | `Run-ShellCommand` — dispatches comandos, resolve placeholders, monta pipeline de execução |

**Recomendação:** Separar em 3 camadas:
- `view_shell/painel_view.ps1` — só renderização de menu/input
- `controllers/painel_controller.ps1` — dispatch e pipeline de execução
- `services/painel_init.ps1` — bootstrap e validação de ambiente

## 2.2. `painel_settings.py` — Config Overloader (257 linhas)

Mistura **4 responsabilidades**:

| Responsabilidade                         | Linhas  |
| ---------------------------------------- | ------- |
| Constantes de path (hardcoded)           | 7–24    |
| Leitura/parse de `.env` e JSON           | 74–101  |
| Resolução de paths relativos → absolutos | 104–230 |
| Acesso a config de ações e menu          | 245–257 |

**Recomendação:** Separar em:
- `services/env_loader.py` — leitura de `.env` e variáveis de ambiente
- `services/path_resolver.py` — resolução de paths (relativo → absoluto)
- `repositories/config_repo.py` — acesso a JSON de configuração (ler/escrever)

## 2.3. `parse_md_ast.py` — Gigante de Parser (655 linhas)

Mistura **orquestração CLI + parse + persistência + schema inline**:

| Classe                             | Responsabilidade real                |
| ---------------------------------- | ------------------------------------ |
| `Initialize`                       | CLI e dispatch                       |
| `ReadInputFiles`                   | Scan de arquivos (IO)                |
| `GenerateAst`                      | Parse de Markdown (regra de négocio) |
| `SaveOutputFiles`                  | Persistência (JSON + SQLite + views) |
| `_INLINE_SCHEMAS` e `_load_schema` | Definição de schema (modelo)         |

**Recomendação:** Extrair para:
- `services/parse/md_ast_runner.py` — orquestração (CLI + dispatch fino)
- `services/parse/md_ast_parser.py` — só lógica de parse (GenerateAst)
- `services/parse/md_ast_io.py` — scan de arquivos
- `repositories/ast_repo.py` — persistência (JSON + SQLite)
- `models/schemas/md_*.json` — schemas (já existem, mas misturados)

## 2.4. `parse_model_pydantic.py` — Schema + Geração + Validação (395 linhas)

Três responsabilidades distintas:

| Função                                  | Responsabilidade                 |
| --------------------------------------- | -------------------------------- |
| `infer_json_schema` / `finalize_schema` | Análise de schema (inteligência) |
| `generate_pydantic_code`                | Geração de código (template)     |
| `validate_json_with_pydantic`           | Validação (execução)             |

**Recomendação:** Separar em:
- `models/schema_inferrer.py` — infere schema de ASTs
- `services/codegen/pydantic_generator.py` — gera código Pydantic
- `services/validation/ast_validator.py` — valida AST contra modelo

## 2.5. Método `_collect_text` duplicado

Presente em **`parse_md_ast.py:480`** e potencialmente replicado em outras
classes. Viola DRY (Don't Repeat Yourself).

**Recomendação:** Mover para `utils_io/ast_utils.py` como função pública.

## 2.6. `sql_sqlite` duplicado em dois locais

`dev\src\painel\sql_sqlite\` e `dev\src\sql_sqlite\` contêm os mesmos arquivos
SQL. O PRD mantém apenas `dev\src\sql_sqlite\`, o que está correto — mas é
preciso **remover o duplicado** para evitar confusão.

---

# 3. Análise do Plano Proposto (PRD vs SRP)

## 3.1. O que está ALINHADO com SRP ✅

| Mudança proposta                                 | Motivo                             |
| ------------------------------------------------ | ---------------------------------- |
| `painel_controle.ps1` → `view_shell\`            | Separa frontend do backend         |
| `painel\services\` → `services\` (raiz)          | Services como camada independente  |
| `painel\models\` → `models\` (raiz)              | Models como camada independente    |
| `painel\services\utils_io\` → `utils_io\` (raiz) | Utilitário genérico, não é service |
| `dbMu\*.db` → `dbMu\sqlite\*.db`                 | Dados organizados por tipo         |

## 3.2. O que precisa ser REVISADO ⚠️

| Mudança proposta                                 | Problema SRP                                                                                                                                                       |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `painel_settings.py` → `services\painel_init.py` | Nome "init" sugere bootstrap, mas arquivo ainda faz **config loading + env + path resolution** juntos. Separar em 2–3 arquivos.                                    |
| `dart_tools` → `services\dart_tools\`            | `dart_tools` contém **scripts Dart CLI** (parse_dart_ast.dart, validate_schema.dart). São ferramentas/scripts, não serviços. Sugestão: `dev\src\tools\dart_tools\` |
| `painel\config\` → `repositories\` (schemas)     | Schemas JSON (schema_md_blocks.json etc) são **modelos**, não repositórios. Subpasta `schemas\` deveria ir para `models\schemas\`                                  |
| `utils_auth\` → `repositories\`                  | **Auth não é repositório.** `client_secret.json`, `google_oauth_tokens.json` são **credenciais/config**. Sugestão: `config\credentials\` (em `.gitignore`)         |

## 3.3. O que está INCORRETO ❌

| Mudança proposta                   | Problema                                                                                                                                                                |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `parse_docs\` → `dbMu\doc_painel\` | `parse_docs` contém **outputs de parse** (ASTs JSON, logs, PDFs de teste), não é banco de dados. Sugestão: `dev\data\outputs\` ou manter como `dev\docs\parse_outputs\` |

## 3.4. Oportunidades não mapeadas

- **`dev\src\temp\`** (testes): bom, mas considerar `dev\tests\` em vez de `dev\src\temp\`
- **Controllers**: PRD cria `dev\src\controllers\` mas está vazio. Definir quais controllers:
  - `controllers\shell_controller.ps1` — painel shell
  - `controllers\parse_controller.py` — painel parse
  - `controllers\sync_controller.py` — painel sync
- **`dev\.*` ignorado**: pastas `.OLD config`, `.OLD tests`, `.understand-anything` precisam ser revisadas (arquivar ou deletar)

---

# 4. Proposta de Arquitetura Final (camadas)

```
dev/
├── src/
│   ├── view_shell/                 # FRONTEND — interface de terminal
│   │   ├── painel_controle.ps1     # Orquestrador principal (fino)
│   │   ├── painel_view.ps1         # Renderização de menu
│   │   └── painel_input.ps1        # Input handling
│   │
│   ├── controllers/                # CONTROLLERS — dispatch de ações
│   │   ├── shell_controller.ps1
│   │   ├── parse_controller.py
│   │   ├── session_controller.py
│   │   └── sync_controller.py
│   │
│   ├── services/                   # SERVICES — regras de negócio
│   │   ├── env_loader.py           # .env loading
│   │   ├── path_resolver.py        # path resolution
│   │   ├── logs/
│   │   ├── parse/
│   │   │   ├── md_ast_runner.py    # orquestração
│   │   │   ├── md_ast_parser.py    # parse lógico
│   │   │   └── md_ast_io.py        # file scanning
│   │   ├── sessions/
│   │   ├── sync/
│   │   └── validation/
│   │       └── ast_validator.py    # validação de modelos
│   │
│   ├── models/                     # MODELS — dados e schemas
│   │   ├── schemas/                # schemas JSON
│   │   │   ├── schema_md_blocks.json
│   │   │   ├── schema_md_code.json
│   │   │   └── schema_md_tables.json
│   │   ├── schema_inferrer.py      # infere schema de ASTs
│   │   ├── parse_model_pydantic.py # modelos Pydantic (gerados)
│   │   ├── pipeline_ast_dart.py
│   │   ├── pipeline_ast_md.py
│   │   └── pipeline_*.py
│   │
│   ├── repositories/               # REPOSITORIES — acesso a dados
│   │   ├── config_repo.py          # leitura/escrita de JSON config
│   │   └── ast_repo.py             # persistência AST (JSON + SQLite)
│   │
│   ├── tools/                      # TOOLS — scripts CLI auxiliares
│   │   └── dart_tools/
│   │       ├── parse_dart_ast.dart
│   │       └── validate_schema.dart
│   │
│   ├── utils_io/                   # UTILITIES — helpers genéricos
│   │   ├── ast_utils.py            # _collect_text e afins
│   │   ├── parse_export.py
│   │   ├── parse_utils.py
│   │   ├── painel_sqlite_export.py
│   │   └── painel_sqlite_import.py
│   │
│   ├── config/                     # CONFIG — credenciais (gitignore)
│   │   └── credentials/
│   │       ├── client_secret.json
│   │       ├── google_oauth_tokens.json
│   │       └── service_account.json
│   │
│   └── sql_sqlite/                 # SQL — scripts DDL/views
│       ├── sql_parse_md/
│       └── sql_parse_script/
│
├── dbMu/
│   ├── sqlite/                     # bancos SQLite
│   │   ├── parse_dart.db
│   │   └── parse_md.db
│   └── doc_painel/                 # documentação do painel
│
├── data/                           # DATA — outputs de execução
│   └── outputs/
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

# 5. Resumo de Ações Recomendadas

| #   | Ação                                                                     | Prioridade | SRP      |
| --- | ------------------------------------------------------------------------ | ---------- | -------- |
| 1   | Separar `painel_controle.ps1` em view + controller + init                | Alta       | Frontend |
| 2   | Separar `painel_settings.py` em env_loader + path_resolver + config_repo | Alta       | Config   |
| 3   | Extrair `_collect_text` para `utils_io/ast_utils.py`                     | Média      | DRY      |
| 4   | Separar `parse_md_ast.py` em runner + parser + io + repo                 | Alta       | Parse    |
| 5   | Separar `parse_model_pydantic.py` em inferrer + generator + validator    | Média      | Models   |
| 6   | Mover `schemas/` para `models/schemas/` (não repositories)               | Média      | Models   |
| 7   | Mover `credentials/` para `config/credentials/` (não repositories)       | Alta       | Infra    |
| 8   | Mover `dart_tools/` para `tools/dart_tools/` (não services)              | Baixa      | Tools    |
| 9   | Remover `src/painel/sql_sqlite/` duplicado                               | Alta       | Limpeza  |
| 10  | Renomear `parse_docs/` → `data/outputs/` (não dbMu)                      | Média      | Dados    |
| 11  | Remover/arquivar pastas `.OLD *`                                         | Baixa      | Limpeza  |

# 6. interações [usuario, agente]

## 6.1. comentarios USUARIO_01
- prefiro dividir o plano em 2 etapas:
  1. criar novas pastas + mover arquivos + ajustar codigos para restaurar funcionalidade do codigo
  2. criar novos arquivos + refatorar codigos

### 6.1.1. arquitetura proposta revisada e comentada {USUARIO: comment}
- dev/
  - src/
    - view_shell/                 # FRONTEND — interface de terminal
      - painel_controle.ps1     # Orquestrador principal (fino) {USUARIO: ver "ps1 scripts" na proxima seção}
      - painel_view.ps1         # Renderização de menu          {USUARIO: ver "ps1 scripts" na proxima seção}
      - painel_input.ps1        # Input handling                {USUARIO: ver "ps1 scripts" na proxima seção}
    - controllers/                # CONTROLLERS — dispatch de ações
      - shell_controller.ps1                                    {USUARIO: ver "ps1 scripts" na proxima seção}
      - parse_controller.py                                     {USUARIO: responsabilidade=CLI ?}
      - session_controller.py                                   {USUARIO: responsabilidade=CLI ?}
      - sync_controller.py                                      {USUARIO: responsabilidade=CLI ?}
    - services/                   # SERVICES — regras de negócio
      - env_loader.py           # .env loading                  {USUARIO: ver "utils_io" na proxima seção}
      - path_resolver.py        # path resolution               {USUARIO: ver "utils_io" na proxima seção}
      - logs/
      - parse/                                                  {USUARIO: onde estão [parse_script_dart_ast.py, parse_script_raw.py]?}
        - md_ast_runner.py    # orquestração                    {USUARIO: explicar divisão de responsabilidades}
        - md_ast_parser.py    # parse lógico                    {USUARIO: explicar divisão de responsabilidades}
        - md_ast_io.py        # file scanning                   {USUARIO: explicar divisão de responsabilidades}
      - sessions/
      - sync/
      - validation/                                   {USUARIO: não vejo "validation" como um serviço em si, mas como um serviço comum que poderia estar em models/ ou utils/}
        - ast_validator.py    # validação de modelos  {USUARIO: validação de quais modelos?}
    - models/                     # MODELS — dados e schemas   {USUARIO: ver "models" na proxima seção}
      - schemas/                # schemas JSON
        - schema_md_blocks.json
        - schema_md_code.json
        - schema_md_tables.json
      - schema_inferrer.py      # infere schema de ASTs
      - parse_model_pydantic.py # modelos Pydantic (gerados)
      - pipeline_ast_dart.py
      - pipeline_ast_md.py
      - pipeline_*.py
    - repositories/               # REPOSITORIES — acesso a dados   {USUARIO: explicar conceito de "repositories" e divisão de responsabilidades}
      - config_repo.py          # leitura/escrita de JSON config
      - ast_repo.py             # persistência AST (JSON + SQLite)
    - tools/                      # TOOLS — scripts CLI auxiliares
      - dart_tools/                                             {USUARIO: mover para services/}
        - parse_dart_ast.dart
        - validate_schema.dart
    - utils_io/                   # UTILITIES — helpers genéricos
      - ast_utils.py            # _collect_text e afins         {USUARIO: explicar divisão de responsabilidades}
      - parse_export.py                                         {USUARIO: ver "utils_io" na proxima seção}
      - parse_utils.py                                          {USUARIO: ver "utils_io" na proxima seção}
      - painel_sqlite_export.py                                 {USUARIO: ver "utils_io" na proxima seção}
      - painel_sqlite_import.py                                 {USUARIO: ver "utils_io" na proxima seção}
    - config/                     # CONFIG — credenciais (gitignore)   {USUARIO: explicar conceito de "config" e divisão de responsabilidades}
      - credentials/
        - client_secret.json
        - google_oauth_tokens.json
        - service_account.json
    - sql_sqlite/                 # SQL — scripts DDL/views
      - sql_parse_md/
      - sql_parse_script/
  - dbMu/                                                          {USUARIO: ver "dataMu" na proxima seção}
    - sqlite/                     # bancos SQLite
      - parse_dart.db
      - parse_md.db
    - doc_painel/                 # documentação do painel         
  - data/                           # DATA — outputs de execução   {USUARIO: ver "dataMu" na proxima seção}
    - outputs/
      - json_md_ast/
      - json_script_dart_ast/
      - json_script_dart_ast_func/
      - json_script_raw/
      - logs/
  - tests/                          # TESTES
    - (test files)

### 6.1.2. sobre os ajustes nas responsabilidades

- ps1 scripts                       {USUARIO: na nova divisao de responsabilidades prefiro que o ps1 seja responsavel apenas por [orquestrar UI, disparar ações selecionadas nos paineis]}
- utils_io                          {USUARIO: com base no entendimento de que utils são serviços comuns, consumidos por outros scripts, renomear para "utils" e sugestao de arquitetura revisada abaixo}
  - init_utils/                     {USUARIO: utilidades de inicialização}
    - env_loader.py
  - parse_utils/                    {USUARIO: utilidades de parsing}
    - path_resolver.py   
    - parse_utils.py                {USUARIO: mover [classes, metodos] para path_resolver.py}
  - io_utils/                       {USUARIO: utilidades de io}
    - parse_export.py
    - painel_sqlite_export.py
    - painel_sqlite_import.py
- models
  - schemas/                # schemas JSON
  - schema_inferrer.py      # infere schema de ASTs        {USUARIO: explicar divisão de responsabilidades}
  - parse_model_pydantic.py # modelos Pydantic (gerados)   {USUARIO: revisar analise para nome do arquivo e responsabilidade}
  - pipeline_ast_dart.py                                   {USUARIO: revisar analise para nome do arquivo, pois o nome não indica que é modelo}
  - pipeline_ast_md.py                                     {USUARIO: revisar analise para nome do arquivo, pois o nome não indica que é modelo}
  - pipeline_*.py                                          {USUARIO: revisar analise para nome do arquivo, pois o nome não indica que é modelo}
- dataMu                                                   {USUARIO: esclarecimento e sugestão de arquitetura abaixo}
  - dbMu/
  - data_docs/
    - data_docs_painel                                     {USUARIO: esclarecendo sobre "docs" como "data docs" dos tipos [json, csv, etc]}

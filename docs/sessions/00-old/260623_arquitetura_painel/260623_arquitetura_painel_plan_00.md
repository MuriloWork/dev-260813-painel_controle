**Plano Etapa 2 — Refatoração e Novos Arquivos**

**Base:** `sessions/260623_arquitetura_painel/260623_analise_arquitetura_02.md`
**Etapa 1 concluída em:** 23/06/2026

---

# 1. Visão Geral

Refatorar os 3 maiores arquivos identificados na análise arquitetural +
criar as camadas `controllers/` e `repositories/` + extrair view/input do PS1.

## Arquivos-alvo da refatoração

| Arquivo                               | Linhas | Ação                                              |
| ------------------------------------- | ------ | ------------------------------------------------- |
| `utils/init_utils/painel_settings.py` | 257    | Split em 3 (env_loader, path_resolver, config_io) |
| `services/parse/parse_md_ast.py`      | 655    | Split em 4 (runner, parser, io, persistence)      |
| `view_shell/painel_controle.ps1`      | 291    | Extrair view + input para arquivos separados      |
| `models/parse_model_pydantic.py`      | 395    | Investigar dead code                              |

---

# 2. Ações Detalhadas

## Ação 1 — Split `painel_settings.py` em 3

**Origem:** `utils/init_utils/painel_settings.py` (257 linhas)
**Destino:** 3 arquivos em `utils/init_utils/`

### 1A. `utils/init_utils/env_loader.py`

Conteúdo extraído:
- `load_env_file()` (linhas 74-85)
- `load_env_base()` (linhas 88-93)
- `load_painel_pipeline_paths()` (linhas 104-128)
- `load_environment_main()` (linhas 233-242)
- Constantes de path fixo (linhas 7-24)
- Globais de estado: `PAINEL_ROOT`, `ABS_PATH_DART_EXECUTABLE`, `ABS_PATH_DART_SDK`

**Responsabilidade:** Carregar variáveis de ambiente + pipeline paths + expor `PAINEL_ROOT`.

### 1B. `utils/parse_utils/path_resolver.py`

Conteúdo extraído:
- `_save_absolute_paths()` (linhas 96-101)
- `_resolve_data_paths()` (linhas 130-149)
- Funções auxiliares de resolução de path

**Responsabilidade:** Resolver paths relativos contra `PAINEL_ROOT`.

### 1C. `utils/io_utils/config_io.py`

Conteúdo extraído:
- `load_painel_actions_data_paths()` (linhas 152-231)
- `get_action_config()` (linhas 245-250)
- `load_menu_targets()` (linhas 253-257)
- Globais de data paths: `DB_PARSE_DART`, `DB_PARSE_MD`, `SOURCE_DART`, `TARGET_MD`, etc.

**Responsabilidade:** Ler JSON de configuração e expor dados de actions/menu.

### Dependências entre os 3:

```
env_loader.py  (define PAINEL_ROOT)
      |
      v
path_resolver.py  (usa PAINEL_ROOT para resolver paths)
      |
      v
config_io.py  (usa path_resolver + env_loader para carregar config completa)
```

Atualizar imports em:
- `services/parse/parse_script_dart_ast.py` (linhas 8-10)
- `services/parse/parse_script_raw.py` (linhas 8-10)
- `services/parse/parse_md_ast.py` (linha 9)
- `utils/io_utils/painel_sqlite_import.py`
- `utils/io_utils/painel_sqlite_export.py`
- `view_shell/painel_controle.ps1` (linha 46: import `env_loader` em vez de `painel_settings`)

---

## Ação 2 — Split `parse_md_ast.py` em 4

**Origem:** `services/parse/parse_md_ast.py` (655 linhas)

### 2A. `utils/io_utils/md_ast_io.py`

Classe extraída: `ReadInputFiles` (linhas 93-111)
- `scan()` — varre diretório por arquivos `.md`
- `_get_project_name()`, `_get_session_version()`

**Responsabilidade:** File scanning (entrada).

### 2B. `services/parse/md_ast_parser.py`

Classe extraída: `GenerateAst` (linhas 114-417)
- `get_ast_model()` — dispatch por tipo
- `_tokens_to_ast()` — lógica central de parsing
- `build_entry()` — monta entrada AST

**Responsabilidade:** Parse de Markdown → modelo AST.

### 2C. `utils/io_utils/md_ast_persistence.py`

Classe extraída: `SaveOutputFiles` (linhas 420-580)
- `save_json()`, `save_sqlite()`, `create_views()`
- `save_all()` — orquestra save
- `_extract()` + `_collect_text()` — extração de dados

**Responsabilidade:** Persistência (JSON + SQLite).

### 2D. `services/parse/md_ast_runner.py`

Classe extraída: `Initialize` (linhas 21-91)
- `parse_args()`, `dispatch()`, `run()`
- `load_environment()` — setup inicial

**Responsabilidade:** Orquestração CLI + dispatch.

### Arquivo original `parse_md_ast.py`:

Após extração, manter como entry point que importa `md_ast_runner`:
```python
from services.parse.md_ast_runner import Initialize

if __name__ == '__main__':
    app = Initialize()
    app.run()
```

### Esquema de dependências:

```
md_ast_runner.py
  ├── md_ast_parser.py       (GenerateAst)
  ├── md_ast_io.py           (ReadInputFiles)
  ├── md_ast_persistence.py  (SaveOutputFiles)
  ├── env_loader.py          (PAINEL_ROOT)
  └── config_io.py           (DB_PARSE_MD, TARGET_MD)
```

---

## Ação 3 — Extrair `_collect_text`

**Origem:** Duplicado em `parse_md_ast.py` (linhas 176 e 480)
**Destino:** `utils/parse_utils/string_utils.py`

```python
def collect_text(children):
    text = ' '.join(child.get('text', '') for child in children if child.get('text'))
    return ' '.join(text.split())
```

Atualizar referências:
- `md_ast_parser.py` (substituir `self._collect_text()` por `collect_text()`)
- `md_ast_persistence.py` (substituir `self._collect_text()` por `collect_text()`)
- `.temp/debug_ast.py` (atualizar import)

---

## Ação 4 — Investigar `parse_model_pydantic.py`

**Conclusão da análise:** `main()` é chamado apenas como script standalone
(`if __name__ == '__main__'`). **Nenhum arquivo importa** `parse_model_pydantic`
como módulo. Apenas referência em `delete/.old/OLD painel_tkinter.py` via `subprocess`.

**Decisão:** Mover para `src/delete/` — código morto não crítico.

---

## Ação 5 — Criar `repositories/`

### 5A. `repositories/config_repo.py`

Encapsular leitura/escrita dos JSONs de configuração:
- `get_pipeline_paths()` — lê `config/set_painel_pipeline_paths.json`
- `get_actions_data_paths()` — lê `config/set_painel_actions_data_paths.json`
- `get_menu()` — lê `config/set_painel_menu.json`
- `save_pipeline_paths(data)` — escreve pipeline paths

Consome `env_loader.py` (para `PAINEL_ROOT`).

### 5B. `repositories/ast_repo.py`

Encapsular persistência de AST:
- `save_json_ast(data, target_dir, session_version)` — salva JSON
- `save_sqlite_ast(data, db_path, table_name)` — upsert via `painel_sqlite_import`
- `load_json_ast(file_path)` — carrega JSON do disco

Consome `config_io.py` (para `DB_PARSE_MD`, `TARGET_MD`).

---

## Ação 6 — Criar `controllers/`

### 6A. `controllers/parse_controller.py`

Orquestra pipeline de parse:
- `run_md_ast(action, input_path)` — dispara parse de Markdown
- `run_dart_ast(action, input_path)` — dispara parse de Dart
- `run_raw(action, input_path)` — dispara parse raw

Substitui `Initialize.dispatch()` de `parse_md_ast.py`.

### 6B. `controllers/session_controller.py`

Gerencia sessões de execução:
- `start_session(name)` — inicia nova sessão
- `end_session()` — finaliza sessão atual
- `list_sessions()` — lista sessões existentes

### 6C. `controllers/sync_controller.py`

Sincroniza dados entre formatos:
- `sync_json_to_sqlite(source, target)` — JSON → SQLite
- `sync_sqlite_to_json(source, target)` — SQLite → JSON
- `sync_export(target, format)` — exporta dados

---

## Ação 7 — Extrair view/input do PS1

**Origem:** `view_shell/painel_controle.ps1` (291 linhas)

### 7A. `view_shell/painel_view.ps1`

Conteúdo extraído:
- `Show-Menu()` (linhas 143-175)
- Funções de renderização de template

### 7B. `view_shell/painel_input.ps1`

Conteúdo extraído:
- Laço `do...while` com `Read-Host` (linhas 279-291)
- Validação de input

### `painel_controle.ps1` após extração:

Mantém apenas:
- Bootstrap/init (linhas 1-98)
- Spawning de abas (linhas 100-118)
- Carregamento de menu (linhas 120-141)
- `Run-ShellCommand()` — dispatch (linhas 177-277)

```powershell
. .\view_shell\painel_view.ps1
. .\view_shell\painel_input.ps1
```

---

# 3. Ordem de Execução

| Fase       | Ações          | Descrição                                                                                        |
| ---------- | -------------- | ------------------------------------------------------------------------------------------------ |
| **Fase 1** | 1A, 1B, 1C     | Split `painel_settings.py` em 3. **Fazer primeiro** porque outros itens dependem.                |
| **Fase 2** | 3              | Extrair `_collect_text` → `string_utils.py`. Rápido, desbloqueia Ação 2.                         |
| **Fase 3** | 2A, 2B, 2C, 2D | Split `parse_md_ast.py` em 4. Depende de Fase 1 (env_loader, config_io) e Fase 2 (string_utils). |
| **Fase 4** | 5A, 5B         | Criar `repositories/`. Depende de Fase 1 (env_loader, config_io).                                |
| **Fase 5** | 6A, 6B, 6C     | Criar `controllers/`. Depende de Fase 3 (md_ast_runner) e Fase 4 (ast_repo).                     |
| **Fase 6** | 7A, 7B         | Extrair view/input do PS1. Independente, pode ser feito em paralelo com Fases 4-5.               |
| **Fase 7** | 4              | Mover `parse_model_pydantic.py` → `src/delete/`. Independente.                                   |

---

# 4. Testes por Fase

| Fase   | Teste                                                                                                                    |
| ------ | ------------------------------------------------------------------------------------------------------------------------ |
| Fase 1 | `python -c "from utils.init_utils.env_loader import load_environment_main; load_environment_main(); print(PAINEL_ROOT)"` |
| Fase 2 | `python -c "from utils.parse_utils.string_utils import collect_text; print(collect_text([{'text': 'a'}]))"`              |
| Fase 3 | `python services/parse/md_ast_runner.py --action md_json --input <dir>`                                                  |
| Fase 4 | `python -c "from repositories.config_repo import get_pipeline_paths; print(get_pipeline_paths())"`                       |
| Fase 5 | `python -c "from controllers.parse_controller import run_md_ast; ..."`                                                   |
| Fase 6 | `powershell -File view_shell/painel_controle.ps1 -Aba shell`                                                             |
| Fase 7 | Verificar que `parse_model_pydantic.py` está em `delete/`                                                                |

---

# 5. Arquivos Afetados

| Arquivo                                   | Ação                                                         |
| ----------------------------------------- | ------------------------------------------------------------ |
| `utils/init_utils/painel_settings.py`     | **DELETAR** após split                                       |
| `utils/init_utils/env_loader.py`          | **CRIAR** (split de painel_settings)                         |
| `utils/parse_utils/path_resolver.py`      | **CRIAR** (split de painel_settings)                         |
| `utils/io_utils/config_io.py`             | **CRIAR** (split de painel_settings)                         |
| `services/parse/parse_md_ast.py`          | **REDUZIR** a entry point                                    |
| `services/parse/md_ast_runner.py`         | **CRIAR** (split de parse_md_ast)                            |
| `services/parse/md_ast_parser.py`         | **CRIAR** (split de parse_md_ast)                            |
| `utils/io_utils/md_ast_io.py`             | **CRIAR** (split de parse_md_ast)                            |
| `utils/io_utils/md_ast_persistence.py`    | **CRIAR** (split de parse_md_ast)                            |
| `utils/parse_utils/string_utils.py`       | **CRIAR** (collect_text)                                     |
| `repositories/config_repo.py`             | **CRIAR**                                                    |
| `repositories/ast_repo.py`                | **CRIAR**                                                    |
| `controllers/parse_controller.py`         | **CRIAR**                                                    |
| `controllers/session_controller.py`       | **CRIAR**                                                    |
| `controllers/sync_controller.py`          | **CRIAR**                                                    |
| `view_shell/painel_view.ps1`              | **CRIAR** (extrair de painel_controle)                       |
| `view_shell/painel_input.ps1`             | **CRIAR** (extrair de painel_controle)                       |
| `view_shell/painel_controle.ps1`          | **REDUZIR** (remover view/input)                             |
| `models/parse_model_pydantic.py`          | **MOVER** para `src/delete/`                                 |
| `.temp/debug_ast.py`                      | Atualizar import de `_collect_text`                          |
| `services/parse/parse_script_dart_ast.py` | Atualizar imports (painel_settings → env_loader + config_io) |
| `services/parse/parse_script_raw.py`      | Atualizar imports                                            |
| `utils/io_utils/painel_sqlite_import.py`  | Atualizar imports                                            |
| `utils/io_utils/painel_sqlite_export.py`  | Atualizar imports                                            |
| `view_shell/painel_controle.ps1`          | Atualizar linha 46 (import env_loader)                       |

---

# 6. Não Alterado

- `config/set_painel_*.json` — sem mudanças (já movidos na Etapa 1)
- `services/dart_tools/` — sem mudanças
- `models/schemas/` — sem mudanças
- `models/ast_dart_model.py`, `ast_md_model.py`, `export_model.py`, `import_model.py`, `raw_script_model.py` — sem mudanças (já renomeados)
- `utils/io_utils/parse_export.py` — sem mudanças (consumido por md_ast_persistence)
- `utils/io_utils/painel_sqlite_import.py` — sem mudanças de lógica (só imports)
- `utils/io_utils/painel_sqlite_export.py` — sem mudanças de lógica (só imports)
- `services/logs/` — sem mudanças
- `sql_sqlite/` — sem mudanças
- `dataMu/` — sem mudanças
- `.env.base` — sem mudanças

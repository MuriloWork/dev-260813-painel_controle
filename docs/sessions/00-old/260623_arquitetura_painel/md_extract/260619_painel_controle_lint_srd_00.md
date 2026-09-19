# 1. Sobre este documento

## 1.1. resumo
{template SRD}

## 1.2. instruções

### 1.2.1. instruções gerais
{template SRD}

### 1.2.2. sobre a seção "contexto do projeto"
{template PRD}

### 1.2.3. sobre a seção "arquitetura do projeto"
{template PRD}

### 1.2.4. sobre a seção "arquitetura de funções"
{template SRD}

### 1.2.5. sobre a seção "arquitetura de dados"
{template SRD}

### 1.2.6. sobre a seção "descrições funcionais"
{template SRD}

# 2. contexto do projeto

## 2.1. objetivos e resumo 
{from PRD}

## 2.2. stack do projeto 
{from PRD}

## 2.3. caminhos do projeto (relativos a project_path) 
{from PRD}

# 3. arquitetura do projeto
{from PRD}

# 4. arquitetura de funções

## 4.1. resumo
{from PRD}

## 4.2. pipeline [type, function]
{from PRD}

## 4.3. automatic functions
{from PRD}

### 4.3.1. script painel\test_parse_md_ast.py

script com algumas funções similares: `C:\Users\muril\OneDrive\01 mycloud\01 sistMu\10.01 scripts\01_root\main\260511_meta_api\dev\painel\parse\parse_dart_ast.py`

#### 4.3.1.1. classe Initialize [coordenação]

Responsável por setup do ambiente e roteamento de ações CLI.

| Método             | Assinatura                                       | Descrição                                                                                  |
| ------------------ | ------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `load_environment` | `load_environment() -> bool`                     | Carrega env vars via `painel_settings.load_environment_main()`, expõe paths como atributos |
| `parse_args`       | `parse_args() -> argparse.Namespace`             | Parseia `--action` (md_ast, md_json, md_sqlite) e `--input` (paths opcionais)              |
| `dispatch`         | `dispatch(action: str, args: Namespace) -> None` | Roteia para o pipeline conforme action: instancia classes e coordena o fluxo               |
| `run`              | `run()`                                          | Método único público: load → parse → dispatch                                              |

Fluxo de `run()`:

```
run()
  → load_environment()
  → parse_args()
  → dispatch(args.action, args)
      md_ast   → ReadInputFiles.scan → GenerateAst.parse_file
                 → SaveOutputFiles.save_all (3 recortes: blocks, code, tables)
                 → SaveOutputFiles.create_views (automático via save_all)
      md_json  → ReadInputFiles.scan → GenerateAst.parse_file
                 → SaveOutputFiles.save_json (3 recortes)
      md_sqlite → painel_sqlite_import.upsert_sqlite (reusa fluxo existente)
                 → SaveOutputFiles.create_views
```

#### 4.3.1.2. classe ReadInputFiles [extração]

| Método                 | Assinatura                                          | Descrição                                                    |
| ---------------------- | --------------------------------------------------- | ------------------------------------------------------------ |
| `scan`                 | `scan(paths: List[str]) -> List[Path]`              | Varre paths (arquivos ou diretórios), retorna lista de `.md` |
| `_filter_md_files`     | `_filter_md_files(paths: List[Path]) -> List[Path]` | Filtra apenas arquivos com extensão `.md`                    |
| `_get_project_name`    | `_get_project_name() -> str`                        | Extrai nome da pasta do `PROJECT_ROOT`                       |
| `_get_session_version` | `_get_session_version() -> str`                     | Timestamp ISO da sessão de extração                          |

#### 4.3.1.3. classe GenerateAst [transformação]

| Método           | Assinatura                                                                                      | Descrição                                                                                                                  |
| ---------------- | ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `get_ast_model`  | `get_ast_model() -> dict`                                                                       | Retorna dict declarativo blueprint com `type`, `fields`, `children` definindo hierarquia e campos da AST extraída          |
| `parse_file`     | `parse_file(md_path: Path, ast_model: dict) -> dict`                                            | Lê `.md`, tokeniza com `markdown-it-py` (preset `js-default`) e extrai AST percorrendo o `ast_model` como referência       |
| `_tokens_to_ast` | `_tokens_to_ast(tokens: list, ast_model: dict) -> dict`                                         | Converte token list flat em árvore; propaga heading_ctx (h1-h4) para todos os blocos via `attach_heading_ctx`              |
| `build_entry`    | `build_entry(md_path: Path, ast: dict, project_name: str, version: str, root_dir: str) -> dict` | Monta dict com dados do arquivo para os schemas de extração (`project_name`, `version`, `folder_path`, `file_path`, `ast`) |
| `_collect_text`  | `_collect_text(children: list) -> str`                                                          | Extrai texto plano de children incluindo inlineCode (não apenas text)                                                      |

#### 4.3.1.4. classe SaveOutputFiles [exportação]

| Método         | Assinatura                                                              | Descrição                                                                       |
| -------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `save_json`    | `save_json(data: list, suffix: str, entry: dict, output_dir: str)`      | Salva JSON dos recortes em `{timestamp}_{child_path}^{file_name}.{suffix}.json` |
| `save_sqlite`  | `save_sqlite(data: list, table_name: str, entry: dict, db_path: str)`   | Cria tabela se não existe, upsert por `file_path`                               |
| `create_views` | `create_views(db_path: str)`                                            | Executa todos os `vw_*.sql` do diretório de views contra o banco                |
| `_extract`     | `_extract(entry: dict, schema: dict) -> list`                           | Aplica schema ao AST → lista flat de objetos                                    |
| `save_all`     | `save_all(entries: list, schemas: dict, output_dir: str, db_path: str)` | Orquestra extração pelos 3 schemas → JSON + SQLite + views para cada um         |

### 4.3.2. script sqlite\sqlite_sql_parse_md\vw_md_doc.sql, vw_md_ast_code.sql, vw_md_ast_tables.sql

Scripts SQL com `DROP VIEW IF EXISTS` + `CREATE VIEW IF NOT EXISTS`.

| View               | Fonte                   | Extração                                                                                                                                                                                 |
| ------------------ | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `vw_md_doc`        | `tb_json_md_ast_blocks` | `json_each(json_data)` → `[file_path, line, block_type, level, script, classe, metodo, content]`. `level` com `NULLIF(0)`. Exclui code, table, thematicBreak. `ORDER BY file_path, line` |
| `vw_md_ast_code`   | `tb_json_md_ast_code`   | `json_each(json_data)` → `[file_path, line, lang, script, classe, metodo, value]`. `lang` vazia → `'(sem tag)'`. `ORDER BY file_path, line`                                              |
| `vw_md_ast_tables` | `tb_json_md_ast_tables` | `json_each(json_data)` → `[file_path, line, row, col, cell_type, script, classe, metodo, value]`. `ORDER BY file_path, line, row, col`                                                   |

Views são recriadas automaticamente via `SaveOutputFiles.create_views()` ao final de `save_all()`.


## 4.4. agent functions 
usar project documents rules  
- rule-edit [naming_rules, variables_rules, data_object_rules, orchestrator_rules] 
- spec-edit [SRD, session_code_blocks] 
- spec-review [SRD, session_code_blocks] ⟶ [review_srd_{version}.md, review_code_blocks_{version}.md]  
- code-script-edit [code_scripts] 
- code-script-edit-comments [comments, tags] 
- code-script-review [code_scripts] ⟶ review_code_scripts_{version}.md 
- control-map-edit
- control-map-review

# 5. arquitetura de dados

## 5.1. instruções e resumo

### 5.1.1. instruções

**Instrução de preenchimento**:
- subseções
  - resumo
    - Propósito: Escrever um parágrafo introdutório explicando que esta seção define a arquitetura funcional de alto nível.
    - Listar o que está FORA do escopo (ex: detalhes de implementação interna, estruturas de dados específicas) com referências para outras seções do documento onde esses tópicos são abordados.
    - tipo de arquitetura utilizada: marcar cada tipo de estrutura de dados utilizada, sem eliminar as linhas para estruturas não utilizadas
  - script models
    - schemas de extração/importação
    - schemas internos para transofrmações intermediarias
    - schemas de exportação
  - documentos externos de dados
  - banco: preencher database_name
    - tabelas: uma subseção para cada tabela, preencher o template
    - views: uma subseção para cada view, preencher o template

### 5.1.2. resumo

**Propósito**:
Mapear toda a arquitetura funcional do sistema até o nível de métodos/objetos relevantes. É a seção mais detalhada e a principal fonte de dados para o hierarchy tracking (script → classe → método).
Documentar todas as estruturas de dados do sistema: tabelas, schemas, formatos de arquivo.

**tipo de arquitetura utilizada**:
- [X] script models
  - [X] schemas de extração/importação
  - [ ] schemas internos para transofrmações intermediarias
  - [X] schemas de exportação
- [X] documentos externos de dados
- [X] banco
  - [X] tabelas
  - [X] views

## 5.2. modelos de dados

### 5.2.1. script models

#### 5.2.1.1. schemas de extração/importação

**Propósito**: Documentar os schemas declarativos usados pelo sistema (ast_model, json_schema_*).

Dois tipos de schema declarativo:

- **`ast_model`** (classe GenerateAst): modelo para extração completa da AST. Define hierarquia e campos de cada nó markdown que o parser deve reconhecer.
- **`json_schema_*`** (classe SaveOutputFiles): modelos para output. Cada um define um recorte do AST que será serializado em JSON e persistido no SQLite.

Os 3 schemas de output abaixo seguem a mesma sintaxe do `ast_model` (type + fields + children), mas produzem listas flat de objetos, não árvores.

`ast_model` é um dict declarativo que mapeia cada nó AST com seus campos e hierarquia de filhos. Serve como blueprint para extração e documentação visual:

```python
ast_model = {
    "type": "root",
    "children": [
        {"type": "heading", "fields": {"depth": "int", "start_line": "int", "end_line": "int"}, "children": [{"type": "text", "fields": {"start_line": "int", "end_line": "int"}}]},
        {"type": "paragraph", "children": [
            {"type": "text", "fields": {"start_line": "int", "end_line": "int"}},
            {"type": "strong", "children": [{"type": "text"}]},
            {"type": "em", "children": [{"type": "text"}]},
            {"type": "inlineCode"},
            {"type": "link", "fields": {"url": "str", "title": "str", "start_line": "int", "end_line": "int"}, "children": [{"type": "text"}]}
        ]},
        {"type": "code", "fields": {"lang": "str", "value": "str", "start_line": "int", "end_line": "int"}},
        {"type": "list", "fields": {"ordered": "bool", "start_line": "int", "end_line": "int"}, "children": [
            {"type": "listItem", "fields": {"start_line": "int", "end_line": "int"}, "children": [
                {"type": "paragraph", "children": [{"type": "text"}]}
            ]}
        ]},
        {"type": "blockquote", "fields": {"start_line": "int", "end_line": "int"}, "children": [
            {"type": "paragraph", "children": [{"type": "text"}]}
        ]},
        {"type": "thematicBreak", "fields": {"start_line": "int", "end_line": "int"}},
        {"type": "table", "fields": {"start_line": "int", "end_line": "int"}, "children": [
            {"type": "tableRow", "fields": {"start_line": "int", "end_line": "int"}, "children": [
                {"type": "tableCell", "fields": {"start_line": "int", "end_line": "int"}, "children": [{"type": "text"}]}
            ]}
        ]}
    ]
}
```

Campos implícitos em todo nó: `type`, `children`. Campos extras declarados em `fields`. `start_line` e `end_line` (0-indexed do `markdown-it-py token.map`) permitem reconstruir a hierarquia de linhas no SQLite.

```python
json_schema_blocks = {
    "type": "blocks",
    "fields": [
        {"name": "file_path", "source": "entry"},
        {"name": "line",      "source": "ast.node.start_line"},
        {"name": "block_type","source": "ast.node.type"},
        {"name": "level",     "source": "ast.node.depth", "default": 0},
        {"name": "script",    "source": "ast.node.h2", "default": ""},
        {"name": "classe",    "source": "ast.node.h3", "default": ""},
        {"name": "metodo",    "source": "ast.node.h4", "default": ""},
        {"name": "content",   "source": "ast", "method": "collect_text"},
    ]
}

json_schema_code = {
    "type": "code",
    "fields": [
        {"name": "file_path", "source": "entry"},
        {"name": "line",      "source": "ast.node.start_line"},
        {"name": "lang",      "source": "ast.node.lang"},
        {"name": "script",    "source": "ast.node.h2", "default": ""},
        {"name": "classe",    "source": "ast.node.h3", "default": ""},
        {"name": "metodo",    "source": "ast.node.h4", "default": ""},
        {"name": "value",     "source": "ast.node.value"},
    ]
}

json_schema_tables = {
    "type": "tables",
    "fields": [
        {"name": "file_path", "source": "entry"},
        {"name": "line",      "source": "ast.node.start_line"},
        {"name": "row",       "source": "ast.row_index"},
        {"name": "col",       "source": "ast.cell_index"},
        {"name": "cell_type", "source": "ast.cell.type"},
        {"name": "script",    "source": "ast.node.h2", "default": ""},
        {"name": "classe",    "source": "ast.node.h3", "default": ""},
        {"name": "metodo",    "source": "ast.node.h4", "default": ""},
        {"name": "value",     "source": "ast", "method": "collect_text"},
    ]
}
```

Campos `script`, `classe`, `metodo` são populados pelo `heading_ctx` tracking durante `_tokens_to_ast`. A ordem de precedência: o heading mais próximo (nível mais profundo) prevalece.

#### 5.2.1.2. schemas internos para transofrmações intermediarias

(não aplicável — não há transformações intermediárias entre schemas no pipeline atual)

#### 5.2.1.3. schemas de exportação

Os mesmos `json_schema_blocks`, `json_schema_code`, `json_schema_tables` (seção 3.2.1.1) servem como schemas de exportação — são aplicados ao AST para gerar os JSONs de saída e as tabelas SQLite.

### 5.2.2. documentos externos de dados

Arquivos JSON (3 por arquivo .md processado) salvos em `dev\parse\json_md_ast\`:

| Schema                | Template                                              | Tabela destino               |
| ------------------    | ----------------------------------------------------- | ---------------------------- |
| `json_schema_blocks`  | `{timestamp}_{child_path}^{file_name}.blocks.json`    | `tb_json_md_ast_blocks`      |
| `json_schema_code`    | `{timestamp}_{child_path}^{file_name}.code.json`      | `tb_json_md_ast_code`        |
| `json_schema_tables`  | `{timestamp}_{child_path}^{file_name}.tables.json`    | `tb_json_md_ast_tables`      |

Exemplo: `20260606T160039.778324_publish^post_builder_instagram.blocks.json`

### 5.2.3. banco `parse_md.db`

Banco SQLite em `dev\sqlite\parse_md.db`. Contém 3 tabelas e 3 views.

#### 5.2.3.1. tabela `tb_json_md_ast_blocks` — blocos do documento

| campo        | tipo    | descrição                                                                                       |
| ------------ | ------- | ----------------------------------------------------------------------------------------------- |
| id           | INTEGER | PK autoincrement                                                                                |
| project_name | TEXT    | extração dinamica apenas do nome da pasta do projeto principal, resultando em `260511_meta_api` |
| version      | TEXT    | timestamp da sessão de extração                                                                 |
| folder_path  | TEXT    | caminho absoluto da pasta raiz da extração                                                      |
| file_path    | TEXT    | caminho relativo a pasta raiz da extração, UNIQUE                                               |
| json_data    | TEXT    | JSON array de objetos `{line, block_type, level, script, classe, metodo, content}`              |

#### 5.2.3.2. tabela `tb_json_md_ast_code` — blocos de código

| campo        | tipo    | descrição                                                                                       |
| ------------ | ------- | ----------------------------------------------------------------------------------------------- |
| id           | INTEGER | PK autoincrement                                                                                |
| project_name | TEXT    | extração dinamica apenas do nome da pasta do projeto principal, resultando em `260511_meta_api` |
| version      | TEXT    | timestamp da sessão de extração                                                                 |
| folder_path  | TEXT    | caminho absoluto da pasta raiz da extração                                                      |
| file_path    | TEXT    | caminho relativo a pasta raiz da extração, UNIQUE                                               |
| json_data    | TEXT    | JSON array de objetos `{line, lang, script, classe, metodo, value}`                             |

#### 5.2.3.3. tabela `tb_json_md_ast_tables` — tabelas

| campo        | tipo    | descrição                                                                                       |
| ------------ | ------- | ----------------------------------------------------------------------------------------------- |
| id           | INTEGER | PK autoincrement                                                                                |
| project_name | TEXT    | extração dinamica apenas do nome da pasta do projeto principal, resultando em `260511_meta_api` |
| version      | TEXT    | timestamp da sessão de extração                                                                 |
| folder_path  | TEXT    | caminho absoluto da pasta raiz da extração                                                      |
| file_path    | TEXT    | caminho relativo a pasta raiz da extração, UNIQUE                                               |
| json_data    | TEXT    | JSON array de objetos `{line, row, col, cell_type, script, classe, metodo, value}`              |

#### 5.2.3.4. view `vw_md_doc`

Fonte: `tb_json_md_ast_blocks` → `json_each(json_data)`

| campo saida | tipo | descrição                                                          |
| ----------- | ---- | ------------------------------------------------------------------ |
| file_path   | TEXT | caminho relativo do arquivo de origem no banco                     |
| line        | INT  | linha inicial do bloco no arquivo markdown (0-indexed)             |
| block_type  | TEXT | tipo do nó markdown (paragraph, heading, listItem, blockquote etc) |
| level       | INT  | profundidade do heading (NULL para não-headings)                   |
| script      | TEXT | texto do heading h2 ancestral                                      |
| classe      | TEXT | texto do heading h3 ancestral                                      |
| metodo      | TEXT | texto do heading h4 ancestral                                      |
| content     | TEXT | texto plano do bloco incluindo inlineCode                          |

Blocos code, table e thematicBreak excluídos. `ORDER BY file_path, line`.

#### 5.2.3.5. view `vw_md_ast_code`

Fonte: `tb_json_md_ast_code` → `json_each(json_data)`

| campo saida | tipo | descrição                                                          |
| ----------- | ---- | ------------------------------------------------------------------ |
| file_path   | TEXT | caminho relativo do arquivo de origem no banco                     |
| line        | INT  | linha inicial do bloco de código no arquivo markdown (0-indexed)   |
| lang        | TEXT | linguagem declarada no code fence; '(sem tag)' quando vazio        |
| script      | TEXT | texto do heading h2 ancestral                                      |
| classe      | TEXT | texto do heading h3 ancestral                                      |
| metodo      | TEXT | texto do heading h4 ancestral                                      |
| value       | TEXT | conteúdo integral do bloco de código                               |

`ORDER BY file_path, line`.

#### 5.2.3.6. view `vw_md_ast_tables`

Fonte: `tb_json_md_ast_tables` → `json_each(json_data)`, transpose e derivação de colunas.

| campo saida   | tipo | descrição                                                                   |
| ------------- | ---- | --------------------------------------------------------------------------- |
| file_path     | TEXT | caminho relativo do arquivo de origem no banco                              |
| section_01    | TEXT | texto do heading h1 ancestral                                               |
| section_02    | TEXT | texto do heading h2 ancestral                                               |
| section_03    | TEXT | texto do heading h3 ancestral                                               |
| section_04    | TEXT | texto do heading h4 ancestral                                               |
| section_05    | TEXT | texto do heading h5 ancestral                                               |
| section_06    | TEXT | texto do heading h6 ancestral                                               |
| line          | INT  | linha inicial da tabela no arquivo markdown (0-indexed)                     |
| script        | TEXT | extraído da section_N que contém "script "                                  |
| tag_classe    | TEXT | extraído entre "[" e "]" da section_N que contém "classe "                  |
| classe        | TEXT | extraído entre "classe " e "[" da section_N que contém "classe "            |
| row           | INT  | índice da linha na tabela (0-indexed)                                       |
| col_01        | TEXT | valor da coluna 0 (transpose), contém o nome do método (metodo)             |
| col_02        | TEXT | valor da coluna 1 (transpose), contém a assinatura do método                |
| col_03        | TEXT | valor da coluna 2 (transpose), contém a descrição do método                 |

Colunas `section_01..06` populadas via heading_ctx tracking estendido para h1-h6. `script`, `classe`, `tag_classe` derivados na view via INSTR/CASE. Transpose de col+value para col_01-03 agrupado por [file_path, section_01..06, line, script, classe, row]. `ORDER BY file_path, section_01..06, line, row`. Views recriadas automaticamente via `SaveOutputFiles.create_views()` ao final de `save_all()`.


# 6. descrições funcionais

## 6.2. lógicas, responsabilidades e requisitos por classe/metodo

### 6.2.1. script `painel\test_parse_md_ast.py`

#### 6.2.1.1. pipeline principal

CLI actions:
- `md_ast` → pipeline completo (json + sqlite + views)
- `md_json` → apenas json
- `md_sqlite` → apenas sqlite upsert + views

| classe / metodo            | Input esperado       | responsabilidade              | Output gerado                                               |
| -------------------------- | -------------------- | ----------------------------- | ----------------------------------------------------------- |
| `Initialize.run`           | Nenhum               | Orquestrar pipeline completo  | Pipeline executado conforme action CLI                      |
| `ReadInputFiles.scan`      | paths CLI            | Varrer e filtrar arquivos .md | `List[Path]` de markdown                                    |
| `GenerateAst.parse_file`   | Path .md + ast_model | Tokenizar e extrair AST       | Dict com project_name, version, folder_path, file_path, ast |
| `SaveOutputFiles.save_all` | entries + schemas    | Extrair recortes + persistir  | 3 JSONs + 3 tabelas + 3 views                               |

Restrições: schedule não aplicável (processamento sob demanda via CLI)

#### 6.2.1.2. classe Initialize

##### 6.2.1.2.1. load_environment - data_io

- responsabilidade: Carregar variáveis de ambiente e expor paths como atributos da instância
- Input esperado: Nenhum (lê de `.env.projeto` + variáveis de ambiente do sistema)
- Transformação aplicada: Invoca `painel_settings.load_environment_main()`, mapeia resultados para atributos
- Output gerado: `bool` indicando sucesso; atributos da instância populados
- Restrições: Deve ser chamado antes de qualquer operação que dependa de paths

##### 6.2.1.2.2. parse_args - data_io

- responsabilidade: Parsear argumentos da linha de comando
- Input esperado: `sys.argv` (argumentos CLI)
- Transformação aplicada: `argparse` parseia `--action` (md_ast, md_json, md_sqlite) e `--input`
- Output gerado: `argparse.Namespace` com `action` e `input`
- Restrições: `--action` obrigatório; `--input` opcional (default: diretório corrente)

##### 6.2.1.2.3. dispatch - workflow

- responsabilidade: Rotear para o pipeline conforme action
- Input esperado: `action: str`, `args: Namespace`
- Transformação aplicada: Instancia classes (ReadInputFiles, GenerateAst, SaveOutputFiles) e coordena fluxo conforme a action
- Output gerado: Execução do pipeline correspondente
- Restrições: Action inválida → erro; md_sqlite reusa `painel_sqlite_import.upsert_sqlite`

##### 6.2.1.2.4. run - workflow

- responsabilidade: Método único público que orquestra o init completo
- Input esperado: Nenhum
- Transformação aplicada: `load_environment() → parse_args() → dispatch(args.action, args)`
- Output gerado: Pipeline executado
- Restrições: Ponto de entrada único da classe

#### 6.2.1.3. classe ReadInputFiles

##### 6.2.1.3.1. scan - data_io

- responsabilidade: Varrer paths e retornar lista de arquivos .md
- Input esperado: `paths: List[str]` (arquivos ou diretórios)
- Transformação aplicada: Para cada path, se diretório → varredura recursiva; se arquivo → valida extensão; filtra apenas `.md`
- Output gerado: `List[Path]` de arquivos markdown
- Restrições: Paths inexistentes são ignorados

#### 6.2.1.4. classe GenerateAst

##### 6.2.1.4.1. parse_file - workflow

- responsabilidade: Tokenizar arquivo .md e extrair AST hierárquica
- Input esperado: `md_path: Path`, `ast_model: dict`
- Transformação aplicada:
  1. Lê conteúdo bruto do arquivo .md (str)
  2. `markdown-it-py` (preset `js-default`) tokeniza em lista flat
     - cada token contém: type, tag, attrs, map (linha inicial/final), nesting (-1/0/1), level, children, content, markup, info, meta, block
     - nesting=1 → abertura de container, nesting=0 → nó atômico, nesting=-1 → fechamento de container
     - `js-default` inclui tabelas (`table_open`/`th_open`/`td_open` com nesting=1)
  3. `_tokens_to_ast` converte lista flat em árvore hierárquica
- Output gerado: `dict` com AST mdast completa
- Restrições: Preset js-default obrigatório para suporte a tabelas

##### 6.2.1.4.2. _tokens_to_ast - data_transform

- responsabilidade: Converter token list flat do markdown-it-py em árvore mdast hierárquica, propagando heading_ctx
- Input esperado: `tokens: list`, `ast_model: dict`
- Transformação aplicada:
  - nesting=1: cria nó container, empilha como parent dos próximos até encontrar nesting=-1 correspondente
  - nesting=0: nó atômico (text, inlineCode, code, thematicBreak, br)
  - `close_type` para tokens `_close` é resolvido via `MD_TYPE_MAP.get({type}_open)` em vez de raw `token.type`
  - Mantém `heading_ctx` tracking: a cada heading_open, captura texto e `attach_heading_ctx` copia h1..h4 para o nó
  - `thead_open` mapeado como `None` para evitar nível extra na árvore
  - mapeamento markdown-it-py → mdast: inline → text/strong/em/s/link/image/code_inline; block → paragraph/heading/code/blockquote/list/list_item/table/hr
    - Todos os containers (paragraph, list, table, code) recebem `h1..h4` via `attach_heading_ctx`. Isso permite que blocos sob um heading herdem o contexto do heading ancestral.
    - `h2` → `script` (ex: "1.3. funções de automação")
    - `h3` → `classe` (ex: "1.3.2. painel\test_parse_md_ast.py — [extração]")
    - `h4` → `metodo` (ex: "Initialize")
- Output gerado: `dict` AST mdast com nós contendo `h1..h4` do heading ancestral
- Restrições: Correções aplicadas — close_type via MD_TYPE_MAP.get, thead mapeado como None, inlineCode incluído no collect_text

##### 6.2.1.4.3. build_entry - data_transform

- responsabilidade: Montar dict padronizado com dados do arquivo para os schemas de extração
- Input esperado: `md_path: Path`, `ast: dict`, `project_name: str`, `version: str`, `root_dir: str`
- Transformação aplicada: Extrai caminho relativo a root_dir, extrai folder_path e file_path, monta dict com metadados + AST
- Output gerado: `dict` com `project_name`, `version`, `folder_path`, `file_path`, `ast`

#### 6.2.1.5. classe SaveOutputFiles

##### 6.2.1.5.1. save_json - data_io

- responsabilidade: Salvar recorte AST em arquivo JSON
- Input esperado: `data: list`, `suffix: str`, `entry: dict`, `output_dir: str`
- Transformação aplicada: Extrai timestamp de version e sanitiza para nome de arquivo; extrai child_path e file_name → child_path^file_name; serializa lista flat para JSON
- Output gerado: Arquivo `{timestamp}_{child_path}^{file_name}.{suffix}.json` em output_dir

##### 6.2.1.5.2. save_sqlite - data_io

- responsabilidade: Persistir recorte AST em tabela SQLite (upsert por file_path)
- Input esperado: `data: list`, `table_name: str`, `entry: dict`, `db_path: str`
- Transformação aplicada: Cria tabela se não existe; converte lista flat para json_data (array JSON); upsert usando `file_path` como chave
- Output gerado: Linha inserida/atualizada na tabela

##### 6.2.1.5.3. create_views - workflow

- responsabilidade: Recriar views SQLite a partir dos scripts .sql
- Input esperado: `db_path: str`
- Transformação aplicada: Varre diretório de views; executa cada `vw_*.sql` (DROP VIEW IF EXISTS + CREATE VIEW IF NOT EXISTS)
- Output gerado: Views recriadas no banco
- Restrições: Deve ser chamado após upsert das tabelas; chamado automaticamente ao final de save_all

##### 6.2.1.5.4. save_all - workflow

- responsabilidade: Orquestrar extração pelos 3 schemas + persistência JSON/SQLite + recriação de views
- Input esperado: `entries: list`, `schemas: dict`, `output_dir: str`, `db_path: str`
- Transformação aplicada:
  1. Para cada schema, aplica `_extract(entry, schema)` → lista flat
  2. `save_json` + `save_sqlite` para cada recorte
  3. `create_views` ao final
- Output gerado: 3 JSONs + 3 tabelas populadas + 3 views recriadas
- Restrições: Depende dos schemas declarativos estarem corretos

Transformação detalhada para JSON:
  1. extrai timestamp de version, sanitiza para nome de arquivo
  2. extrai child_path e file_name de file_path → child_path^file_name
  3. extrai recortes aplicando cada schema:
     - `extract_blocks(entry, json_schema_blocks)` → lista flat com script, classe, metodo
     - `extract_code(entry, json_schema_code)` → lista flat com script, classe, metodo
     - `extract_tables(entry, json_schema_tables)` → lista flat com script, classe, metodo, cell_type
  4. salva cada recorte como `{timestamp}_{child_path}^{file_name}.{schema}.json`
  5. `_collect_text` extrai texto plano incluindo inlineCode (não apenas text)

Transformação detalhada para SQLite:
  1. cada schema produz 1 json_data (array dos objetos flat)
  2. upsert nas tabelas: 1 linha por arquivo, file_path como chave
     - `tb_json_md_ast_blocks` ← json_schema_blocks (json_data)
     - `tb_json_md_ast_code` ← json_schema_code (json_data)
     - `tb_json_md_ast_tables` ← json_schema_tables (json_data)
  3. create_views executa vw_md_doc.sql, vw_md_ast_code.sql, vw_md_ast_tables.sql

### 6.2.2. script `sqlite\sqlite_sql_parse_md\vw_md_doc.sql`

- dados fonte: `tb_json_md_ast_blocks`
- colunas agrupadoras: [file_path]
  - `file_path`: caminho relativo do arquivo de origem — agrupa todos os blocos que pertencem ao mesmo arquivo markdown processado
- colunas de valores resultantes: [line, block_type, level, script, classe, metodo, content]
  - `line`: linha inicial do bloco extraída do campo `start_line` do nó AST; usada para ordenação sequencial dos blocos dentro de cada arquivo
  - `block_type`: tipo do nó markdown (paragraph, heading, listItem, blockquote etc); blocos code, table e thematicBreak são excluídos do resultado
  - `level`: profundidade do heading obtida do campo `depth`; heading sem profundidade recebe NULL via NULLIF(0)
  - `script`, `classe`, `metodo`: hierarquia do heading ancestral propagada pelo heading_ctx tracking (h2→script, h3→classe, h4→metodo)
  - `content`: texto plano do bloco combinando nós text e inlineCode via `_collect_text`
- Restrições: DROP VIEW IF EXISTS antes de CREATE VIEW IF NOT EXISTS; ORDER BY file_path, line

### 6.2.3. script `sqlite\sqlite_sql_parse_md\vw_md_ast_code.sql`

- dados fonte: `tb_json_md_ast_code`
- colunas agrupadoras: [file_path]
  - `file_path`: caminho relativo do arquivo de origem — agrupa todos os blocos de código do mesmo arquivo
- colunas de valores resultantes: [line, lang, script, classe, metodo, value]
  - `line`: linha inicial do bloco de código; usada para ordenação sequencial dentro de cada arquivo
  - `lang`: linguagem declarada no code fence (ex: python, dart, sql); campos vazios são normalizados para '(sem tag)' via COALESCE
  - `script`, `classe`, `metodo`: hierarquia do heading ancestral propagada pelo heading_ctx tracking
  - `value`: conteúdo integral do bloco de código (preserva indentação e quebras de linha originais)
- Restrições: DROP VIEW IF EXISTS antes de CREATE VIEW IF NOT EXISTS; ORDER BY file_path, line

### 6.2.4. script `sqlite\sqlite_sql_parse_md\vw_md_ast_tables.sql`

- dados fonte: `tb_json_md_ast_tables`
- colunas agrupadoras: [file_path, section_01, section_02, section_03, section_04, section_05, section_06, line, script, classe, row]
  - `file_path`: caminho relativo do arquivo de origem — agrupa tabelas do mesmo arquivo
  - `section_01..06`: headings ancestrais h1-h6 propagados pelo heading_ctx tracking — agrupam tabelas que estão sob a mesma hierarquia de seção
  - `line`: linha inicial da tabela — agrupa células pertencentes à mesma tabela
  - `script`, `classe`: extraídos das section_N que contêm "script " e "classe " — agrupam por script e classe do documento
  - `row`: índice da linha — agrupa células da mesma linha para transpose
- colunas de valores resultantes: [col_01, col_02, col_03, tag_classe]
  - `col_01`, `col_02`, `col_03`: transpose das colunas individuais (col+value) usando MAX(CASE WHEN col = N THEN value END) — col_01 equivale ao nome do método na tabela markdown
  - `tag_classe`: extraído entre "[" e "]" da section_N que contém "classe " — representa a responsabilidade da classe (ex: coordenação, extração, transformação, exportação)
- Restrições: DROP VIEW IF EXISTS antes de CREATE VIEW IF NOT EXISTS; ORDER BY file_path, section_01..06, line, row




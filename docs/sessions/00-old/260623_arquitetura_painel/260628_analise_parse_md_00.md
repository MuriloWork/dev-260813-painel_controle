**Análise de Refatoração: parse-ast (Markdown Parse)**

**Data:** 2026-06-28  
**Objetivo:** Mapear a comunidade parse-ast e identificar oportunidades de refatoração

---

# 1. Comunidade parse-ast

**14 nós** | Coesão: 0.191 | Linguagem: Python

## 1.1. Arquivos

| Arquivo            | Classe/Função | Linhas | Responsabilidade                |
| ------------------ | ------------- | ------ | ------------------------------- |
| `md_ast_parser.py` | `GenerateAst` | 9-304  | Parser principal (296 linhas)   |
| `md_ast_runner.py` | `MdAstRunner` | 17-86  | Runner/orquestrador (70 linhas) |

## 1.2. Métodos de GenerateAst

| Método                 | Linhas  | O que faz                                      |
| ---------------------- | ------- | ---------------------------------------------- |
| `get_ast_model()`      | 10-38   | Define o schema do AST (28 linhas)             |
| `parse_file()`         | 74-80   | Lê arquivo MD e chama parser (7 linhas)        |
| `_tokens_to_ast()`     | 82-288  | Converte tokens MarkdownIt em AST (207 linhas) |
| `_collect_text()`      | 71-72   | Extrai texto de nós filhos (2 linhas)          |
| `attach_heading_ctx()` | 88-95   | Anexa contexto h1-h6 ao nó (8 linhas)          |
| `flush_inline()`       | 97-100  | Descarrega buffer inline (4 linhas)            |
| `build_entry()`        | 290-304 | Monta entry dict para persistência (15 linhas) |

## 1.3. Métodos de MdAstRunner

| Método               | Linhas | O que faz                                      |
| -------------------- | ------ | ---------------------------------------------- |
| `load_environment()` | 22-24  | Carrega variáveis de ambiente                  |
| `parse_args()`       | 26-34  | Parse de argumentos CLI (argparse)             |
| `dispatch()`         | 36-81  | Roteador de ações (md_ast, md_json, md_sqlite) |
| `run()`              | 83-86  | Entry point                                    |

---

# 2. Fluxos de Execução

## 2.1. Fluxo principal: `run` (criticalidade: 0.445)

```
MdAstRunner.run()                    [md_ast_runner.py:83]
  ├── load_environment()             [md_ast_runner.py:22]
  ├── parse_args()                   [md_ast_runner.py:26]
  └── dispatch(action, args)         [md_ast_runner.py:36]
        └── GenerateAst()            [md_ast_parser.py:9]
```

## 2.2. Fluxo de parse: `parse_file` (criticalidade: 0.453)

```
GenerateAst.parse_file()             [md_ast_parser.py:74]
  └── _tokens_to_ast()               [md_ast_parser.py:82]
        └── attach_heading_ctx()     [md_ast_parser.py:88]
```

## 2.3. Fluxo de persistência: `save_all` (criticalidade: 0.412)

```
SaveOutputFiles.save_all()           [md_ast_persistence.py:156]
  ├── _extract()                     [md_ast_persistence.py:21]
  ├── save_json()                    [md_ast_persistence.py:83]
  ├── save_sqlite()                  [md_ast_persistence.py:97]
  ├── _collect_text()                [md_ast_persistence.py:80]
  └── create_views()                 [md_ast_persistence.py:142]
```

## 2.4. Entry point CLI: `run_md_ast` (criticalidade: 0.320)

```
run_md_ast()                         [parse_controller.py:7]
  └── Args                           [parse_controller.py:13]
```

---

# 3. Problemas Identificados

## 3.1. `_tokens_to_ast()` — God Method (207 linhas)

- Método único com lógica complexa de parsing
- Mistura: parsing de inline, containers, headings, code blocks, tables
- Aninhamento profundo (while + if + if)
- Difícil de testar individualmente

## 3.2. Acoplamento com MarkdownIt

- `parse_file()` depende diretamente do `MarkdownIt('js-default')`
- Trocar de parser requer modificar `_tokens_to_ast()` inteiro

## 3.3. Schema inline

- `get_ast_model()` define o schema como dict literal (28 linhas)
- Schema duplicado: se o AST muda, precisa atualizar `_tokens_to_ast()` também

## 3.4. Dispatch monolítico

- `dispatch()` tem 3 caminhos (md_ast, md_json, md_sqlite) em um único método
- Lógica de IO misturada com lógica de parsing

## 3.5. `md_ast_parser.py` e `md_ast_persistence.py` duplicam `_collect_text()`

- `GenerateAst._collect_text()` (linha 71)
- `SaveOutputFiles._collect_text()` (linha 80)
- Ambos delegam para `string_utils.collect_text()`

---

# 4. Oportunidades de Refatoração

## 4.1. Extrair subclasses de `_tokens_to_ast()`

| Handler            | Responsabilidade                            |
| ------------------ | ------------------------------------------- |
| `InlineHandler`    | text, code_inline, strong, em, link, image  |
| `ContainerHandler` | heading, paragraph, list, blockquote, table |
| `CodeHandler`      | fence, code_block                           |
| `LeafHandler`      | hr, thematicBreak                           |

**Ganho:** testes unitários por tipo de nó, manutenção isolada

## 4.2. Strategy pattern para parser

```python
class MdParser(Protocol):
    def parse(self, source: str) -> list: ...

class MarkdownItParser(MdParser):
    def parse(self, source: str) -> list:
        md = MarkdownIt('js-default')
        return md.parse(source)
```

**Ganho:** trocar MarkdownIt por outro parser sem modificar o restante

## 4.3. Schema centralizado

Mover `get_ast_model()` para arquivo JSON externo ou dataclass:

```python
@dataclass
class AstModel:
    type: str
    children: list
    fields: dict
```

**Ganho:** schema versionado, validação automática

## 4.4. Separar dispatch em classes

```python
class MdAstAction(Protocol):
    def execute(self, entries, schemas, output_dir, db_path): ...

class AstAction(MdAstAction): ...
class JsonAction(MdAstAction): ...
class SqliteAction(MdAstAction): ...
```

**Ganho:** Open/Closed Principle, fácil adicionar novas ações

## 4.5. Consolidar `_collect_text()`

Remover a duplicação mantendo só em `string_utils` e chamando diretamente.

---

# 5. Dependências Externas

| Dependência       | Uso                  | Pode substituir?        |
| ----------------- | -------------------- | ----------------------- |
| `markdown-it-py`  | Tokenização Markdown | Sim (outros parsers MD) |
| `string_utils`    | Coleta de texto      | Não (interno)           |
| `painel_settings` | Configurações        | Não (interno)           |
| `ast_md_model`    | Modelos Pydantic     | Não (interno)           |
| `parse_export`    | Validação e escrita  | Não (interno)           |

---

# 6. Tamanho dos Arquivos

| Arquivo                 | Linhas | Complexidade                       |
| ----------------------- | ------ | ---------------------------------- |
| `md_ast_parser.py`      | 304    | Alta (_tokens_to_ast = 207 linhas) |
| `md_ast_runner.py`      | 91     | Baixa                              |
| `md_ast_persistence.py` | 242    | Média                              |

---

# 7. Objetivo: fluxo similar ao CRG

Refatoração visando eliminar JSON intermediário, usar schema SQLite similar ao graph.db e adicionar versionamento.

### 7.1.1. Fluxo atual (com JSON intermediário)

```
Markdown file
  → MarkdownIt.tokenize()
  → GenerateAst._tokens_to_ast()     → AST dict em memória
  → SaveOutputFiles._extract()       → lista de dicts
  → save_json()                      → arquivo .json (intermediário)
  → save_sqlite()                    → INSERT com json_data TEXT
  → create_views()                   → views SQL
```

**Problemas:**
- JSON intermediário é escrito e lido sem necessidade
- `json_data TEXT` no SQLite dificulta consultas索引
- Sem versionamento (sobrescreve dados anteriores)

### 7.1.2. Fluxo proposto (similar ao CRG)

```
Markdown file
  → MarkdownIt.tokenize()
  → GenerateAst._tokens_to_ast()     → AST dict em memória
  → InsertNodes()                    → INSERT direto na tabela nodes
  → InsertEdges()                    → INSERT direto na tabela edges
  → (sem JSON intermediário)
```

### 7.1.3. Schema proposto: `parse_md.db`

#### 7.1.3.1. Tabela `nodes`

```sql
CREATE TABLE nodes (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    kind            TEXT NOT NULL,           -- heading, paragraph, code, table, list, blockquote, text, link, image
    name            TEXT,                    -- texto extraído ou tipo do nó
    qualified_name  TEXT UNIQUE,             -- file_path::type::start_line
    file_path       TEXT NOT NULL,
    line_start      INTEGER,
    line_end        INTEGER,
    language        TEXT,                    -- lang dos code blocks (dart, python, etc.)
    parent_name     TEXT,                    -- nó pai (h1, h2, etc.)
    extra           TEXT,                    -- JSON com campos extras (url, depth, ordered, etc.)
    file_hash       TEXT,                    -- SHA-256 do conteúdo do arquivo
        version         TEXT NOT NULL,           -- timestamp do build
        created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### 7.1.3.2. Tabela `edges`

```sql
CREATE TABLE edges (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    kind            TEXT NOT NULL,           -- CONTAINS, HAS_HEADING, HAS_CODE, HAS_TABLE, REFERENCES
    source_qualified TEXT NOT NULL,          -- nó pai
    target_qualified TEXT NOT NULL,          -- nó filho
    file_path       TEXT,
    confidence      REAL DEFAULT 1.0,
    version         TEXT NOT NULL,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### 7.1.3.3. Tabela `metadata`

```sql
CREATE TABLE metadata (
    key     TEXT PRIMARY KEY,
    value   TEXT
);

-- Valores iniciais:
INSERT INTO metadata VALUES ('schema_version', '1');
INSERT INTO metadata VALUES ('last_updated', '<timestamp>');
INSERT INTO metadata VALUES ('last_build_type', 'full');
```

### 7.1.4. Mapeamento: AST → Nodes

| Nó AST | kind | name | extra |
|--------|------|------|-------|
| heading | `heading` | texto do heading | `{"depth": 1, "h1": "", "h2": ""}` |
| paragraph | `paragraph` | texto coletado | `{"h1": "", "h2": ""}` |
| code | `code` | valor do código | `{"lang": "dart", "h1": ""}` |
| table | `table` | - | `{"rows": N, "cols": M}` |
| list | `list` | - | `{"ordered": true/false}` |
| blockquote | `blockquote` | texto coletado | `{}` |
| link | `link` | texto do link | `{"url": "https://..."}` |
| image | `image` | alt text | `{"url": "img.png"}` |
| text | `text` | conteúdo | `{}` |
| thematicBreak | `thematicBreak` | - | `{}` |

### 7.1.5. Mapeamento: AST → Edges

| Relação | kind | Exemplo |
|---------|------|---------|
| Arquivo contém nó | `CONTAINS` | `file.md → heading` |
| Heading pai de conteúdo | `HAS_HEADING` | `h1 → paragraph` |
| Código dentro de seção | `HAS_CODE` | `h2 → code` |
| Tabela dentro de seção | `HAS_TABLE` | `h2 → table` |
| Link referencia arquivo | `REFERENCES` | `link → outro_arquivo.md` |

### 7.1.6. Versionamento

O CRG não mantém histórico — sobrescreve os dados a cada build. O controle é feito via `metadata`:

- `last_updated` — timestamp do último build
- `last_build_type` — `full` ou `incremental`
- `schema_version` — versão do schema (para migrations futuras)

Não existe tabela `versions`. O versionamento real é feito pelo **git**.

### 7.1.7. Eliminação do JSON intermediário

| Componente atual | O que faz | Substituir por |
|------------------|-----------|----------------|
| `save_json()` | Escreve .json em disco | **Removido** |
| `json_data TEXT` | Armazena JSON no SQLite | **Colunas estruturadas** em `nodes` |
| `_extract()` | Converte AST para lista de dicts | **InsertNodes** que vai direto ao SQLite |

### 7.1.8. Query de exemplo (similar ao CRG)

```sql
-- Todos os code blocks com linguagem detectada
SELECT n.name, n.file_path, n.line_start, n.extra
FROM nodes n
WHERE n.kind = 'code'
  AND json_extract(n.extra, '$.lang') = 'dart';

-- Estrutura de um arquivo (hierarquia de headings)
SELECT n1.name AS heading, n2.name AS content, n2.kind
FROM edges e
JOIN nodes n1 ON e.source_qualified = n1.qualified_name
JOIN nodes n2 ON e.target_qualified = n2.qualified_name
WHERE e.kind = 'HAS_HEADING'
  AND n1.file_path = 'docs/README.md'
ORDER BY n1.line_start;

-- Último build
SELECT * FROM metadata WHERE key = 'last_updated';
```

### 7.1.9. Impacto na refatoração

| Arquivo | Mudança |
|---------|---------|
| `md_ast_parser.py` | Manter `_tokens_to_ast()`, adicionar `InsertNodes` |
| `md_ast_persistence.py` | Substituir `save_json()` + `save_sqlite()` por insert direto |
| `md_ast_runner.py` | Remover ação `md_json`, manter `md_ast` e `md_sqlite` |
| `md_ast_model.py` | Simplificar (não precisa mais de MdBlockRow, MdCodeRow, etc.) |

### 7.1.10. Prioridade atualizada

| Prioridade | Ação | Esforço | Impacto |
|------------|------|---------|---------|
| **1** | Schema `parse_md.db` com nodes/edges/metadata | Alto | Alto |
| **2** | InsertNodes direto (sem JSON intermediário) | Alto | Alto |
| **3** | Versionamento por timestamp | Médio | Alto |
| **4** | Incremental update via `file_hash` + `git diff` | Médio | Alto |
| **5** | Extrair handlers de `_tokens_to_ast()` | Alto | Médio |
| **6** | Strategy pattern para parser MD | Médio | Médio |
| **7** | Consolidar `_collect_text()` | Baixo | Baixo |

### 7.1.11. Incremental update (mesma lógica do CRG)

O CRG não mantém histórico — sobrescreve o grafo a cada build. Usa `file_hash` (SHA-256) para saber quais arquivos mudaram e re-parse só esses.

#### Lógica do CRG

```
1. git diff → arquivos changed
2. Para cada arquivo changed:
   - Lê conteúdo atual → calcula SHA-256
   - Compara com file_hash salvo no graph.db
   - Se hash diferente → re-parse esse arquivo
   - Se hash igual → skip
3. Re-parse: sobrescreve os nós antigos desse arquivo
```

#### Aplicação ao parse MD

```
1. git diff HEAD~1 -- '*.md'          → lista de arquivos MD que mudaram
2. Para cada arquivo changed:
   - Lê conteúdo → calcula SHA-256
   - Compara com file_hash no parse_md.db
   - Se hash diferente → re-parse (insere nodes/edges novos, remove antigos)
   - Se hash igual → skip
3. Registra build na tabela versions
```

#### Tabela `metadata` (adicionar ao schema)

```sql
CREATE TABLE metadata (
    key     TEXT PRIMARY KEY,
    value   TEXT
);

-- Valores iniciais:
INSERT INTO metadata VALUES ('schema_version', '1');
INSERT INTO metadata VALUES ('last_updated', '<timestamp>');
INSERT INTO metadata VALUES ('last_build_type', 'full');
```

#### Fluxo completo

```
┌─────────────────────────────────────────────────┐
│  1. Detectar arquivos changed (git diff)        │
│     git diff HEAD~1 --name-only -- '*.md'       │
└──────────────────────┬──────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────┐
│  2. Para cada arquivo changed:                  │
│     - Calcula SHA-256 do conteúdo atual         │
│     - Compara com file_hash no parse_md.db      │
│     - Se igual → skip                           │
│     - Se diferente → continua                   │
└──────────────────────┬──────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────┐
│  3. Remove nós antigos desse arquivo:           │
│     DELETE FROM edges WHERE file_path = ?       │
│     DELETE FROM nodes WHERE file_path = ?       │
└──────────────────────┬──────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────┐
│  4. Re-parse: MarkdownIt → AST → nodes/edges    │
│     INSERT INTO nodes (...) ON CONFLICT UPDATE  │
│     INSERT INTO edges (...)                     │
└──────────────────────┬──────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────┐
│  5. Atualiza metadata:                          │
│     UPDATE metadata SET value = <timestamp>     │
│     WHERE key = 'last_updated'                  │
└─────────────────────────────────────────────────┘
```

#### Comando CLI proposto

```bash
# Full build (todos os .md)
python md_ast_runner.py --action md_ast

# Incremental (só changed desde último build)
python md_ast_runner.py --action md_ast --incremental

# Forçar full rebuild
python md_ast_runner.py --action md_ast --full
```

#### Queries de versionamento

```sql
-- Último build
SELECT * FROM metadata WHERE key = 'last_updated';

-- Arquivos com hash diferente (mudaram desde último build)
SELECT file_path, file_hash FROM nodes
WHERE file_hash != (
    SELECT value FROM metadata WHERE key = 'last_file_hash'
);
```

---

# 8. Próximos passos

1. Criar migration do schema `parse_md.db` (nodes, edges, metadata)
2. Implementar `InsertNodes` que converte AST → nodes direto
3. Implementar `InsertEdges` que converte relações AST → edges
4. Implementar incremental update: `file_hash` + `git diff`
5. Adicionar comando `--incremental` ao CLI
6. Remover `save_json()` e `json_data` do fluxo
7. Validar com arquivos MD de teste

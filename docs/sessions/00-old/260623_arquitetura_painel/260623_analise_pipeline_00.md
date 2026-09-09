**Analise do Pipeline Principal e Formatacao — v00**

# 1. Visao Geral do Pipeline

```
dados fonte ──┬── markdown [PRD, SRD, session_code_blocks]
              └── code scripts [ps1, python, dart]

fluxo principal (combinacao de funcoes, algumas em loop):

  ┌─────────────────────────────────────────────────────────────┐
  │                       OUTER LOOP                            │
  │                                                             │
  │  [session/agent] update SRD                                 │
  │       │                                                     │
  │       ▼                                                     │
  │  [automatic] parse SRD ──────────> SQLite spec:             │
  │       │                          [folder, script, classe,   │
  │       │                           metodo, responsabilidades]│
  │       │                                                     │
  │  [session/agent] update code_scripts                        │
  │       │                                                     │
  │       ▼                                                     │
  │  [automatic] parse code_scripts ──> SQLite code:            │
  │       │                          [folder, script, classe,   │
  │       │                           metodo]                   │
  │       │                                                     │
  │       ▼                                                     │
  │  ┌─── CODE CHECK ───────────────────────────────────────┐   │
  │  │                                                      │   │
  │  │  Step A — Cross-reference (automatic):               │   │
  │  │    spec vs code → gaps: [missing, extra, mismatch]   │   │
  │  │                                                      │   │
  │  │  Step B — Lint tools (automatic):                    │   │
  │  │    import-linter, pylint, mypy, radon, vulture,      │   │
  │  │    pep8-naming, isort, eradicate, architecture_enforcer│  │
  │  │    → violations.json                                 │   │
  │  │                                                      │   │
  │  │  Step C — Intelligent check (agent + skills):        │   │
  │  │    agents usam dados SQLite + violations.json        │   │
  │  │    para verificar SOLID/SRP contra regras reais      │   │
  │  │                                                      │   │
  │  └──────────────────────────────────────────────────────┘   │
  │       │                                                     │
  │       ▼                                                     │
  │  review ──> update [SRD, code_scripts] ──> repeat           │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘
```

## 1.1. Tipos de Funcao no Pipeline

| Tipo | Quem executa | Entrada | Saida | Exemplos |
| --- | --- | --- | --- | --- |
| automatic | scripts python/ps1 | markdown, code scripts | SQLite, JSON, relatorios | parse_md_ast, lint tools |
| session | usuario + agente | prompts, regras | documentos atualizados | update PRD, update SRD |
| agent | agente IA sozinho | regras, templates, dados | documentos, revisoes | rule-edit, spec-review, code-script-edit |

## 1.2. Loops Identificados

**Loop A — SRD (mais lento, versoes):**
```
session/agent update SRD → automatic parse SRD → SQLite spec → 
agent review SRD → review_srd_NN.md → session/agent update → repeat
```
Disparo: quando PRD muda ou arquitetura evolve.

**Loop B — code_scripts (mais rapido, versoes):**
```
agent create code_scripts → automatic parse → automatic lint → 
agent review → review_code_NN.md → session/agent update → repeat
```
Disparo: quando SRD/session_code_blocks mudam ou codigo e refatorado.

**Loop C — consolidacao (combinado):**
```
automatic parse SRD + code_scripts → SQLite spec + code →
cross-reference → gaps → violations.json → 
agent deep-review (SOLID/SRP sobre dados reais) →
review consolidado → session update [SRD, code_scripts] → repeat
```

---

# 2. Formatacao: Onde o Parse Depende de Estrutura

## 2.1. Parsing de Markdown (SRD, PRD, session_code_blocks)

O parser md_ast_parser.py usa heading_ctx tracking (h1-h6). As tabelas SQLite resultantes tem os campos `script, classe, metodo` populados por h2, h3, h4.

**Regras que o markdown DEVE seguir para o parse funcionar:**

| Elemento | Regra | Consequencia se quebrada |
| --- | --- | --- |
| Heading h2 | Deve conter "script " para ser detectado como script | script fica vazio no SQLite |
| Heading h3 | Deve conter "classe " entre "classe " e "[" | classe fica vazio |
| Heading h3 | Responsabilidade entre "[" e "]" | tag_classe fica vazio |
| Heading h4 | Nome do metodo | metodo fica vazio |
| Tabelas markdown | Primeira linha = header, segunda = separador `\|---\|` | Transpose falha |
| Tabelas markdown | Colunas na ordem: Metodo, Assinatura, Descricao | Campos col_01/02/03 trocados |
| Code blocks | Precisam de lang tag (\`\`\`python) | lang fica '(sem tag)' |

## 2.2. Problema Atual de Formatacao no SRD_01

O SRD_01 que criamos nesta sessao NAO segue as regras de heading que o parser espera.
Exemplo: secao 6.2.1 usa `### 6.2.1. script services/parse/parse_md_ast.py` (h3), mas deveria ter `classe` no heading para que o parser identifique classes e metodos.

**Diagnostico**: O SRD_01 tem a estrutura de secoes correta (h3 para scripts, h4 para classes, tabelas de metodos) MAS:
- h2 usa `{numero}. {nome}` em vez de `script {path}` → parser nao reconhece como script
- h3 NAO contem "classe " → parser nao extrai responsabilidade
- h4 NAO contem nome do metodo puro → parser nao extrai metodo

**Tabela de comparacao: formato esperado vs formato atual no SRD_01:**

| Elemento | Formato esperado pelo parser | Formato atual no SRD_01 |
| --- | --- | --- |
| h2 - script | `script {caminho_relativo}` | `{numero}. {descricao}` |
| h3 - classe | `classe {Nome} [{responsabilidade}]` | `{numero}.{numero}. {descricao}` |
| h4 - metodo | `{nome_metodo} - {type}` | `{numero}.{numero}.{numero}. {nome_metodo} - {type}` |

## 2.3. Recomendacao de Formatacao para SRD

Adotar o formato que o parser entende:

```markdown
# script src/services/parse/md_ast_parser.py

## classe GenerateAst [transformacao]

### parse_file - workflow

| Metodo | Assinatura | Descricao |
| --- | --- | --- |
| parse_file | parse_file(md_path, ast_model) | Tokeniza .md e extrai AST |

### _tokens_to_ast - data_transform

| Metodo | Assinatura | Descricao |
| --- | --- | --- |
| _tokens_to_ast | _tokens_to_ast(tokens, ast_model) | Converte token list flat em arvore |
```

Isso garante que:
- h2 contem "script " → `script = "services/parse/md_ast_parser.py"`
- h3 contem "classe " e "[" → `classe = "GenerateAst"`, `tag_classe = "transformacao"`
- h4 contem nome do metodo puro → `metodo = "parse_file"`
- Tabela markdown na subsecao do metodo → `col_01 = "parse_file"`, `col_02 = "parse_file(md_path, ast_model)"`, `col_03 = "Tokeniza .md e extrai AST"`

## 2.4. Parsing de Code Scripts (ps1, python, dart)

**Python**:
- `parse_script_raw.py` extrai linhas, comentarios e tags
- `parse_script_dart_ast.py` (nome confuso — processa AST Dart, nao python)
- Para python, seria necessario um parser AST similar ao dart, usando `ast` module padrao

**PowerShell**:
- Nao ha parser AST para PS1 atualmente
- `parse_script_raw.py` consegue extrair linhas/comentarios mas sem AST

**Dart**:
- `parse_script_dart_ast.py` + `parse_dart_ast.dart` via subprocess
- `AstNode` model: type, offset, length, line, column, children

**Lacuna identificada**: nao existe parser AST generico para python e ps1. Apenas o raw parser e o dart parser estao implementados.

---

# 3. Recomendacoes

## 3.1. Imediatas (antes da proxima sessao)

1. **Corrigir formatacao do SRD_01** para seguir o formato parseavel (h2="script path", h3="classe Nome [resp]", h4="metodo - type") — ou criar SRD_02 com essa correcao
2. **Criar script de cross-reference** que compara SQLite spec vs code e produz gaps:
   - Classes na spec mas ausentes no codigo → `missing`
   - Classes no codigo mas ausentes na spec → `extra`
   - Metodos na spec mas com assinatura diferente → `mismatch`

## 3.2. Curto Prazo (proxima sessao)

3. **Criar architecture_enforcer.py** conforme especificado no documento de lint tools:
   - SRP por nome (Save → metodos write/save apenas)
   - Metodo unificado (json.dump → write_json)
   - Acoplamento de orquestrador (nao chamar metodos privados)
4. **Configurar import-linter** com camadas do projeto atual (controllers → services → utils → repositories → models)
5. **Corrigir nome do script** `parse_script_dart_ast.py` — ele processa AST Dart, nao python. Sugestao: `parse_dart_ast.py` (mas esse nome ja existe em services/dart_tools/). Melhor: manter como esta e documentar.

## 3.3. Medio Prazo

6. **Criar parser AST para python** usando `ast` module padrao da stdlib — mesma logica do dart parser, extrair classes, metodos, funcoes, variaveis
7. **Criar parser AST para powershell** (mais complexo — PS1 nao tem AST padrao facil; usar regex + indentacao como heuristica)
8. **Integrar lint_arch.bat** no pipeline automatico (Step B do CODE CHECK)

## 3.4. Pipeline de Qualidade (visao completa)

```
[spec] SRD ──parse──> SQLite spec_tables
                        │
[code] scripts ─parse──> SQLite code_tables
                        │
                        ├── cross-reference ──> gaps_report.md
                        │
                        ├── lint_arch.bat ─────> violations.json
                        │     ├── import-linter
                        │     ├── pylint
                        │     ├── mypy
                        │     ├── radon/xenon
                        │     ├── pep8-naming
                        │     ├── vulture
                        │     ├── isort
                        │     ├── eradicate
                        │     └── architecture_enforcer.py
                        │
                        └── agent review ──────> review_NN.md
                              ├── le SQLite spec vs code
                              ├── le violations.json
                              ├── avalia SOLID/SRP sobre dados reais
                              └── recomenda refatoracoes
```

---

# 4. Observacoes Finais

## 4.1. Dependencia Circular entre SRD e Parser

O SRD especifica o parser, mas o parser so funciona se o SRD seguir a formatacao esperada. Isso cria uma dependencia ciclica:
- O SRD precisa ser parseavel para gerar dados de controle
- Mas o SRD so sera parseavel se seguir as regras do parser que ele mesmo especifica

**Solucao**: o template do SRD (secao de instrucoes) ja define as regras de formatacao. O documento deve SEGUIR essas regras desde a criacao. O SRD_01 foi criado sem seguir as regras de heading — isso precisa ser corrigido no SRD_02.

## 4.2. Lacuna de Parser PS1

Atualmente nao ha parser PS1. Como o frontend do painel e em PS1 (`painel_controle.ps1`, 258 linhas), isso significa que:
- O script principal do sistema nao pode ser analisado pelo pipeline de qualidade
- Nao ha como verificar SOLID/SRP no codigo PS1
- Nao ha como extrair AST do codigo PS1

**Sugestao**: implementar parser heuristico para PS1 baseado em regex (function, class (se houver), parametros, chamadas) ate que uma solucao mais robusta seja necessaria.

## 4.3. Nomenclatura

O script `parse_script_dart_ast.py` (services/parse/) tem nome ambiguo. Ele:
- Processa AST de codigo Dart via subprocess (chama `dart run parse_dart_ast.dart`)
- NAO faz parse de script python

Sugestao renomear para `parse_dart_code_ast.py` para clareza, ou manter e documentar em AGENTS.md.

## 4.4. Sobre o SRD_01

O SRD_01 e valido como **documento de consulta humana** (tem descricoes detalhadas, tabelas de linhas, status de implementacao). Porem, para ser parseavel, precisa de uma segunda versao (SRD_02) que:
- Reorganize os headings para o formato parser-friendly
- Mantenha o conteudo detalhado nas secoes de descricoes funcionais (secao 6)
- Use a secao 4 (arquitetura de funcoes) para o formato parseavel com headings padrao

Sugestao: manter SRD_01 como referencia humana e criar SRD_02 como versao parseavel.

**Analise de Ferramentas de Lint para Validacao de Arquitetura — v00**

# 1. Problema

O codigo e refatorado a cada sessao. Instrucoes em AGENTS.md e testes arquiteturais manuais ficam invalidos assim que a proxima sessao comeca. O ciclo de refatoracao e mais rapido que a documentacao.

E preciso algo **imediato, generico e que nao exija manutencao entre sessoes** para garantir que novos refatoramentos nao corrompam a arquitetura pretendida.

# 2. Tipos de violacao

| Tipo de violacao                       | Desvios possiveis                                                                                                                                                                                                                                                                                                                                                                                                                  |      |                           |         |                                                                                           |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ------------------------- | ------- | ----------------------------------------------------------------------------------------- |
| **Nomeacao inadequada**                | (1) desvios sobre regras basicas de nomeação; (2)"Nome do método não corresponde ao verbo de ação esperado para o nome da classe que o contém" — mesma regra do SRP: o nome da classe dita o vocabulário permitido para métodos; (3) nome generico `data` para objetos de tipos diferentes; (4) `tmp`/`temp` sem contexto; (5) desvios sobre tabela `naming rules`                                                                 |      |                           |         |                                                                                           |
| **Acoplamento indevido**               | (1) Classe de baixo nivel importa configuracao especifica de alto nivel; (2) "Módulo da camada N importa módulo da camada N+2 (pulando uma camada intermediária)" ou "módulo importa algo fora do seu grafo de dependência permitido". É exatamente o que import-linter já verifica com a config de layers; (3) orquestrador conhece detalhes de schema interno; (4) incompatibilidade de responsabilidades entre classe e metodos |      |                           |         |                                                                                           |
| **Violaçao de SRP — escopo da classe** | (1) "Classe com nome indicando responsabilidade X contém método cuja ação pertence a responsabilidade Y" — regra: prefixo do nome da classe define um conjunto de prefixos de métodos permitidos. Save* → write                                                                                                                                                                                                                    | save | serialize. Parse* → parse | extract | tokenize; (2) classe que inicializa, coordena e executa; (3) classe que valida e persiste |
| **Não uso de metodo unificado**        | (1) se o nome da [classe, metodo] indica responsabilidade coberta por metodo unificado mas não foi usado                                                                                                                                                                                                                                                                                                                           |      |                           |         |                                                                                           |
| **Duplicacao de codigo**               | (1) "Mesmo algoritmo/expressão implementado em 2+ locais diferentes" — independe do que o algoritmo faz. A detecção é puramente estrutural (similaridade de AST); (2) logica de extracao replicada em scripts diferentes                                                                                                                                                                                                           |      |                           |         |                                                                                           |
| **Uso indevido de variaveis**          | (1) Variavel declarada e nunca usada; (2) mesmo nome para conceitos diferentes no mesmo escopo; (3) tratamento inconsistente de `None`/valores padrao; (4) variavel mutada apos uso pretendido; (5) desvios sobre tabela `variables rules`                                                                                                                                                                                         |      |                           |         |                                                                                           |
| **Uso indevido de objetos de dados**   | (1) Dict solto sem modelo Pydantic sendo trafegado entre camadas; (2) schema definido em comentario em vez de modelo tipado; (3) campo acessado por `dict['key']` sem garantia de existencia; (4) mesmo objeto de dados construido de formas diferentes em cada script; (5) desvios sobre tabela `data object rules`                                                                                                               |      |                           |         |                                                                                           |
| **Import de camada proibida**          | (1) Script de parse importa modulo de output diretamente; (2) camada de modelo importa de servico; (3) quebra da direcao de dependencia                                                                                                                                                                                                                                                                                            |      |                           |         |                                                                                           |
| **Complexidade / classe grande**       | (1) Classe com +15 metodos publicos; (2) metodo unico com +100 linhas; (3) classe que faz leitura, transformacao e escrita ao mesmo tempo; (4) muitos parametros por funcao (+5)                                                                                                                                                                                                                                                   |      |                           |         |                                                                                           |

# 3. Ferramentas

## 3.1. linters existentes

| Tipo de violacao                                                                | Ferramenta                                                                                                                                                                                              | Configuracao                                                        | Manutencao                                              |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------- |
| **Nomeacao de classes e metodos**                                               | `pep8-naming` (snake_case, CamelCase, metodos privados); `pylint` naming conventions (`--const-rgx`, `--class-rgx`, `--method-rgx`, `--function-rgx`, `--attr-rgx`, `--argument-rgx`, `--variable-rgx`) | `pep8-naming`: plugin flake8; `pylint`: regexes em `.pylintrc`      | Zero                                                    |
| **Duplicacao de codigo** (`_collect_text` em 2+ classes)                        | `pylint --enable=duplicate-code`                                                                                                                                                                        | Ajustar threshold de similaridade                                   | Zero                                                    |
| **Uso indevido de variaveis** (unused, redeclaradas, import nao utilizado)      | `pylint --enable=unused-variable,unused-import,wildcard-import` + `vulture` (codigo morto: funcoes, parametros, atributos nunca usados)                                                                 | `vulture`: `vulture . --min-confidence 80`                          | Zero                                                    |
| **Uso indevido de objetos de dados** (type mismatch, erros de tipo)             | `mypy` ou `pyright` strict mode                                                                                                                                                                         | `strict = true` no `pyproject.toml` (uma vez)                       | Zero (pode exigir anotacoes de tipo ao escrever codigo) |
| **Import de camada proibida** (ex: `parse/` importar `painel_sqlite_import.py`) | `import-linter`                                                                                                                                                                                         | TOML/INI uma vez na raiz                                            | Zero — regras sao sobre diretorios, nao sobre codigo    |
| **Complexidade / classe grande**                                                | `radon` + `xenon` (cyclomatic complexity, maintainability index por modulo); `pylint` (`--max-locals`, `--max-public-methods`, `--max-args`)                                                            | `radon` cfg via `pyproject.toml`; `xenon` com thresholds por commit | Zero — metricas universais                              |
| **import circular**                                                             | `import-linter` (camadas) + `pycycle` (circular imports especifico); `pylint --enable=cyclic-import`                                                                                                    | `import-linter`: TOML/INI; `pycycle`: CLI direto                    | Zero — regras sobre estrutura de diretorios             |
| **Ordem de imports fora do padrao**                                             | `isort` (stdlib → third-party → local)                                                                                                                                                                  | `isort . --check-only` ou `pyproject.toml` `[tool.isort]`           | Zero                                                    |
| **Codigo comentado esquecido**                                                  | `eradicate` (detecta blocos de codigo comentados)                                                                                                                                                       | Plugin flake8 ou CLI `eradicate .`                                  | Zero                                                    |

## 3.2. cobertura das linters tools existentes sobre os desvios possiveis 

| validação usuario | Ferramenta      | configuração                                                           | Tipo de violacao                     | desvios possiveis cobertos                                                                                                                                     | desvios possiveis não cobertos                                                                                                                                                                                                                                                                                       |
| ----------------- | --------------- | ---------------------------------------------------------------------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| não               | `pep8-naming`   | snake_case, CamelCase, metodos privados                                | **Nomeacao de classes e metodos**    | (1) desvios sobre regras basicas de nomeação                                                                                                                   | (2)"Nome do método não corresponde ao verbo de ação esperado para o nome da classe que o contém" — mesma regra do SRP: o nome da classe dita o vocabulário permitido para métodos; (3) nome generico `data` para objetos de tipos diferentes; (4) `tmp`/`temp` sem contexto; (5) desvios sobre tabela `naming rules` |
| sim               | `pylint`        | naming conventions (`--const-rgx`, `--class-rgx`, `--method-rgx`, ...) | **Nomeacao de classes e metodos**    | (1) desvios sobre regras basicas de nomeação; (3) nome generico `data` para objetos de tipos diferentes (com regex); (4) `tmp`/`temp` sem contexto (com regex) | (2) semantica "Save → metodos devem ser write/save" — regex global nao consegue associar classe a metodo; (5) desvios sobre tabela `naming rules`                                                                                                                                                                    |
| sim               | `import-linter` | camadas + pycycle                                                      | **Acoplamento indevido**             | (1) classe baixo nivel importa alto nivel; (2) modulo N importa N+2                                                                                            | (3) orquestrador conhece schema interno (import-linter nao ve chamadas de metodo); (4) incompatibilidade responsabilidades                                                                                                                                                                                           |
| não               | `pycycle`       | CLI direto                                                             | **Acoplamento indevido**             | (2) import circular entre modulos                                                                                                                              | (1), (3), (4) — pycycle so detecta ciclo, nao direcao de dependencia                                                                                                                                                                                                                                                 |
| sim               | `pylint`        | `--enable=duplicate-code`                                              | **Duplicacao de codigo**             | (1) mesmo algoritmo em 2+ locais; (2) logica replicada em scripts diferentes                                                                                   | —                                                                                                                                                                                                                                                                                                                    |
| sim               | `pylint`        | `--enable=unused-variable,unused-import,wildcard-import`               | **Uso indevido de variaveis**        | (1) variavel declarada nunca usada; (5) desvios sobre `variables rules` (unused, redeclared)                                                                   | (2) mesmo nome para conceitos diferentes; (3) `None` inconsistente; (4) variavel mutada apos uso                                                                                                                                                                                                                     |
| não               | `vulture`       | `--min-confidence 80`                                                  | **Uso indevido de variaveis**        | (1) codigo morto (funcoes, parametros, atributos nunca usados) — mais profundo que pylint                                                                      | (2)-(5) mesmas lacunas do pylint                                                                                                                                                                                                                                                                                     |
| sim               | `mypy`          | `--strict`                                                             | **Uso indevido de objetos de dados** | (1) dict solto sem modelo (se codigo tipado); (3) `dict['key']` sem garantia (TypedDict); (4) mesmo objeto construido diferente (se funcao construtora tipada) | (2) schema em comentario vs modelo tipado (intencao do dev); (5) desvios sobre `data object rules`                                                                                                                                                                                                                   |
| sim               | `pylint`        | `--max-args=5 --max-locals=15 --max-public-methods=10`                 | **Complexidade / classe grande**     | (1) +15 metodos publicos; (4) +5 parametros                                                                                                                    | (2) metodo +100 linhas (pylint nao mede linhas por funcao); (3) classe que faz leitura+transformacao+escrita                                                                                                                                                                                                         |
| sim               | `radon+xenon`   | thresholds em `pyproject.toml`                                         | **Complexidade / classe grande**     | (2) metodo com +100 linhas (complexidade ciclomatica); (3) classe multifuncao (baixo maintainability index indica isso)                                        | (1), (4) — radon mede funcao, nao classe; nao conta metodos publicos nem parametros                                                                                                                                                                                                                                  |
| sim               | `import-linter` | TOML/INI com camadas                                                   | **Import de camada proibida**        | (1) parse importa output; (2) modelo importa servico; (3) quebra direcao de dependencia                                                                        | —                                                                                                                                                                                                                                                                                                                    |
| não               | `isort`         | `--check-only` + `pyproject.toml`                                      | **Ordem de imports**                 | (1) imports fora da ordem stdlib → third-party → local                                                                                                         | —                                                                                                                                                                                                                                                                                                                    |
| não               | `eradicate`     | CLI ou plugin flake8 (ERA001)                                          | **Codigo comentado**                 | (1) blocos de codigo deixados como comentario                                                                                                                  | —                                                                                                                                                                                                                                                                                                                    |


## 3.3. linters personalizados

| Tipo de violacao                                                           | Ferramenta                              | Configuracao                                                                                 | Manutencao                                                                  |
| -------------------------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **SRP no nome da classe** (classe "Save" com metodo `_extract` — extracao) | Script custom + `ast` puro (~30 linhas) | Padrao regex: "se nome tem Save/Write/Export, metodos devem ser write/save/serialize apenas" | Zero — regra generica                                                       |
| **Padronizacao do uso de metodos unificados**                              | Script custom + `ast` (~40 linhas)      | Lista de metodos canonicos por operacao (ex: SQLite so via `write_to_sqlite`)                | **Baixa** — lista precisa ser atualizada quando surgir novo metodo canonico |
| **Acoplamentos indevidos** (orquestrador chama metodo privado/IO direto)   | `architecture_enforcer.py` (4.9.3)      | Lista de classes orquestradoras + regras de encapsulamento                                   | **Baixa** — lista ORCHESTRATOR_CLASSES raramente muda                       |

## 3.4. cobertura complementar linter personalizado architecture_enforcer.py

| modulo            | tipo de violação                              | desvios possiveis ainda não cobertos                                                                                                                                                                                       | configuração necessaria                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ----------------- | --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| naming            | **Nomeacao de classes e metodos**             | (2)"Nome do método não corresponde ao verbo de ação esperado para o nome da classe que o contém" — mesma regra do SRP: o nome da classe dita o vocabulário permitido para métodos; (5) desvios sobre tabela `naming rules` | Tabela `naming_rules` com colunas `[class_prefix, allowed_method_prefixes]`. `architecture_enforcer` le a tabela e valida: se classe comeca com "Save", metodos devem comecar com `write\|save\|serialize`. Tabela pode ser populada manualmente ou via parse de AST (DART extrai classes + metodos → sugestao de regras)                                                                                                                                                             |
| coupling          | **Acoplamentos indevidos**                    | (3) orquestrador conhece detalhes de schema interno; (4) incompatibilidade de responsabilidades entre classe e metodos                                                                                                     | Lista `ORCHESTRATOR_CLASSES` em JSON (`orchestrator_rules.json`). Colunas: `[class_name, allowed_call_prefixes, blocked_modules]`. `architecture_enforcer` varre chamadas de metodos dentro de orquestradores. Se chamar metodo privado `.*\._.*` ou IO direto `json.dump\|sqlite3.connect\|open`, alerta. Regras podem ser enriquecidas pelo parse de AST: analisar grafos de chamada e sugerir limites                                                                              |
| srp               | **Violaçao de SRP — escopo da classe**        | (1) "Classe com nome indicando responsabilidade X contém método cuja ação pertence a responsabilidade Y" — regra: prefixo do nome da classe define um conjunto de prefixos de métodos permitidos. Save* → write            | Mesma tabela `naming_rules` do modulo `naming`. Unificar: coluna extra `[class_prefix, responsibility, allowed_method_prefixes]`. `architecture_enforcer` varre AST dos arquivos Python e verifica cada metodo publico contra a tabela                                                                                                                                                                                                                                                |
| unique_method_use | **Padronizacao do uso de metodos unificados** | (1) se o nome da [classe, metodo] indica responsabilidade coberta por metodo unificado mas não foi usado                                                                                                                   | Tabela `canonical_methods.json` com colunas `[operation, authorized_path, banned_patterns]`. Ex: `{operation: "write_sqlite", authorized_path: "parse_export.sqlite_update.write", banned_patterns: ["cursor.execute.*INSERT", "sqlite3.connect"]}`. `architecture_enforcer` varre imports e chamadas; se encontrar `json.dump()`, procura na tabela se ha um canonico para "write_json"                                                                                              |
| variables_use     | **Uso indevido de variaveis**                 | (2) mesmo nome para conceitos diferentes no mesmo escopo; (3) tratamento inconsistente de `None`/valores padrao; (4) variavel mutada apos uso pretendido; (5) desvios sobre tabela `variables rules`                       | Tabela `variables_rules.json` com colunas `[context_pattern, allowed_names_regex, blocked_names]`. Ex: `{context_pattern: ".*_main.*", allowed_names: "^[a-z][a-z_]+$", blocked: ["data", "tmp", "temp"]}`. Para (2),(4): `architecture_enforcer` faz analise estatica basica — se mesma variavel recebe 2 tipos diferentes de atribuicao no mesmo escopo, alerta. Para (3): `mypy` ja cobre Optional; complementar com regra: "parametro com default=None deve ter tipo Optional[T]" |
| data_objetcs_use  | **Uso indevido de objetos de dados**          | (2) schema definido em comentario em vez de modelo tipado; (5) desvios sobre tabela `data object rules`                                                                                                                    | Tabela `data_object_rules.json` com colunas `[module_pattern, required_model, banned_access_pattern]`. Ex: `{module_pattern: "parse.*", required_model: "RawScriptRow\|MdBlockRow", banned_access_pattern: "dict\[.*\]"}`. `architecture_enforcer` varre AST: se encontra `dict['...']` em modulo que deveria usar Pydantic, alerta. Parse de AST (DART/MD) pode alimentar essa tabela: se modulo X sempre usou modelo Y nos ultimos N commits, sugerir `required_model`              |

USUARIO:
- preencher coluna "configurações necessarias" 
- para definição das "configurações necessarias" considerar
	- todos os "desvios possiveis ainda não cobertos" devem ser tratados, mesmo que de forma parcial
	- utilização de dados [json, sqlite] que são gerados pelo painel controle parse, exemplos: 
		- tabela de dados ast permite identificar classes, metodos e variaveis)
		- parse dos markdown [tables, code blocks] padronizados permite identificar hierarquias de [modulos, classes, metodos]
	- criação de tabelas de apoio [naming_rules, variables_rules, data_object_rules] para aplicação de regex
	- seja criativo, proponha configurações com uso de dados (regras) de apoio e integração com agente de IA em etapas específicas

# 4. como fazer

## 4.1. regras e instruções

## 4.2. lint tools

### 4.2.1. Todas as ferramentas abaixo agrupadas num unico comando:

```
lint_arch.bat
    ├── import-linter              # camadas proibidas
    ├── pycycle                    # import circular
    ├── radon & xenon              # complexidade
    ├── pep8-naming                # convencao de nomes
    ├── vulture                    # codigo morto
    ├── isort --check-only         # ordem de imports
    ├── eradicate                  # codigo comentado
    ├── mypy --strict              # tipos
    ├── pylint (gerais)            # duplicate-code, unused-*, cyclic-import
    └── architecture_enforcer.py   # SRP + metodo unificado + acoplamento
```

---

### 4.2.2. pep8-naming — Nomeacao

Plugin flake8 que valida snake_case, CamelCase, metodos privados.

```
pip install flake8 pep8-naming
flake8 --select=N dev/src/painel
```

```ini
[flake8]
select = N
per-file-ignores = __init__.py:N801
```

**Nao cobre** a regra semantica "Save → metodos devem ser write/save". Responsabilidade do `architecture_enforcer.py`.

---

### 4.2.3. architecture_enforcer.py — SRP + Metodo unificado + Acoplamento (custom)

Script unico que varre AST dos arquivos Python e aplica 3 regras.

#### 4.2.3.1. SRP por nome

```python
VIOLATION_PATTERNS = {
    'save': ('_extract', '_parse', '_transform', '_collect'),
    'write': ('_extract', '_parse', '_transform', '_collect'),
    'export': ('_extract', '_parse', '_transform', '_collect'),
    'parse': ('_save', '_write', '_export'),
}
```

Regra: se classe tem `Save` no nome, metodos devem comecar com `write|save|serialize`. Se tem `Parse`, metodos devem comecar com `parse|extract|tokenize`.

#### 4.2.3.2. Metodo unificado

```python
CANONICAL_METHODS = {
    'write_json':    'parse_export.json_writer.write',
    'write_sqlite':  'parse_export.sqlite_update.write',
    'write_csv':     'parse_export.csv_writer.write',
    'validate_model':'parse_export.validate',
    'select_json':   'parse_export.sqlite_update.select_json_from_dir',
}
```

Varre chamadas. Se encontrar `json.dump()` (deveria ser `write_json`) ou `cursor.execute("INSERT...")` inline (deveria ser `write_sqlite`), alerta.

#### 4.2.3.3. Acoplamento orquestrador → detalhe interno

**Regra**: metodos de classes orquestradoras nao podem chamar metodos privados (`_*`) de outras classes, nem fazer IO direto (`open()`, `sqlite3.connect()`, `json.dump()`), nem resolver logica de extracao/dominio.

```python
ORCHESTRATOR_CLASSES = ('Initialize', 'Dispatcher', 'Pipeline', 'Orchestrator')

## Para cada metodo em classe orquestradora:
##   1. Se chamar metodo privado (._*) de outra classe → alerta: quebra encapsulamento
##   2. Se chamar open()/sqlite3.connect()/json.dump() → alerta: IO direto, delegar a parse_export
##   3. Se chamar metodo de extracao/parse → alerta: logica de dominio, usar servico intermediario
```

Exemplos flagrados:

| Codigo                                                 | Alerta                                                |
| ------------------------------------------------------ | ----------------------------------------------------- |
| `Initialize.dispatch()` → `SaveOutputFiles._extract()` | Orquestrador chama metodo privado                     |
| `Initialize.dispatch()` → `save_json()`                | Orquestrador faz IO direto                            |
| `Initialize.dispatch()` → `_get_session_version()`     | Orquestrador chama metodo privado de `ReadInputFiles` |

**Manutencao**: `ORCHESTRATOR_CLASSES` raramente muda.

---

### 4.2.4. pylint — Checks gerais

Complemento para violacoes nao capturadas pelas ferramentas especializadas.

```ini
[pylint]
load-plugins = pylint.extensions.mccabe
enable = duplicate-code, unused-variable, unused-import,
         wildcard-import, cyclic-import
max-args = 5
max-locals = 15
max-public-methods = 10
```

```
pylint dev/src/painel --rcfile=.pylintrc
```

---

### 4.2.5. import-linter — Camadas proibidas

Le `.import-linter.cfg` ou `pyproject.toml` e verifica contratos entre pacotes. Falha se um import cruza camada proibida.

#### 4.2.5.1. Config

```toml
[tool.importlinter]
root_packages = ["dev.src.painel"]

[[tool.importlinter.contracts]]
name = "Camadas fixas"
type = "layers"
layers = [
  "models",          # 0 — schemas Pydantic, sem dependencias do projeto
  "config",          # 1 — painel_settings (depende de models)
  "services.utils_io",  # 2 — parse_export, parse_utils (depende de models, config)
  "services.parse",     # 3 — parse_md_ast, etc (depende de utils_io, models, config)
  "scripts"             # 4 — orquestracao (chama apenas services.* e config)
]
containers = ["dev.src.painel"]
```

#### 4.2.5.2. Execucao

```
lint-imports
```

**Nao precisa atualizar entre sessoes** — a regra e sobre estrutura de diretorios, que muda pouco.

---

### 4.2.6. pycycle — Import circular

Detector dedicado a ciclos de import.

```
pip install pycycle
pycycle dev.src.painel
```

---

### 4.2.7. isort — Ordem de imports

stdlib → third-party → local.

```
pip install isort
isort . --check-only --diff
```

```toml
[tool.isort]
profile = "black"
line_length = 120
known_first_party = ["painel"]
```

---

### 4.2.8. vulture — Codigo morto

Funcoes, parametros e atributos nunca usados.

```
pip install vulture
vulture . --min-confidence 80
```

Whitelist para falsos positivos: `vulture_whitelist.py`.

---

### 4.2.9. eradicate — Codigo comentado

```
pip install eradicate
eradicate .
```

Plugin flake8: `flake8 --select=ERA001`.

---

### 4.2.10. mypy/pyright — Tipos

```
pip install mypy
mypy dev/src/painel --strict
```

```toml
[tool.mypy]
strict = true
ignore_missing_imports = true
```

---

### 4.2.11. radon + xenon — Complexidade

`radon` calcula metricas (cyclomatic complexity, maintainability index). `xenon` define thresholds.

```toml
[tool.xenon]
max_cyclomatic_complexity = 10
max_average_complexity = 5
max_maintainability_index = 65
```

```
xenon . --max-cyclomatic-complexity 10 --max-average-complexity 5 --max-maintainability-index 65
```

---

# 5. Proximo passo

Implementar:

1. `import-linter` config com as camadas do projeto
2. `architecture_enforcer.py` (SRP por nome)
3. Script unificado de validacao (`npm run lint:arch` ou `lint_arch.bat`)
4. Integrar ao workflow local (sem bloquear, apenas alertar)

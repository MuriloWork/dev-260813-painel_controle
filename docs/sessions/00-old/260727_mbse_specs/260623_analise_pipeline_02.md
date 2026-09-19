**Analise do Pipeline Principal e Formatacao — v02**

# 1. arquitetura de funções

## 1.1. resumo

| Tipo      | Quem executa       | Entrada                  | Saida                    | Exemplos                                 |
| --------- | ------------------ | ------------------------ | ------------------------ | ---------------------------------------- |
| automatic | scripts python/ps1 | markdown, code scripts   | SQLite, JSON, relatorios | parse_md_ast, lint tools                 |
| session   | usuario + agente   | prompts, regras          | documentos atualizados   | update PRD, update SRD                   |
| agent     | agente IA sozinho  | regras, templates, dados | documentos, revisoes     | rule-edit, spec-review, code-script-edit |

## 1.2. Pipeline [type, function]

- [automatic] update PRD: [PRD_00, template_PRD] ⟶ PRD_01
- [automatic] update AGENTS.md: [AGENTS, PRD_01] ⟶ AGENTS.md
- [session] update PRD
- [automatic] create SRD: [PRD_02, template_SRD] ⟶ SRD_00
- loop update SRD
  - [session] update SRD
  - [automatic] parse [PRD, SRD] ⟶ [json, sqlite]
  - [automatic] cross-reference spec vs code ⟶ gaps_report.md
    - compara SQLite spec com SQLite code
    - produz gaps: [missing, extra, mismatch]
  - [agent] review SRD ⟶ review_srd_{version}.md
- [session] update tables [naming_rules, variables_rules, data_object_rules, orchestrator_rules]
- [agent] create session_code_blocks
- loop update session_code_blocks
  - [automatic] parse [SRD, session_code_blocks] ⟶ [json, sqlite]
  - [agent] review session_code_blocks ⟶ review_code_blocks_{version}.md
  - [session] update session_code_blocks
- [agent] create code_scripts
- loop update code_scripts
  - [automatic] parse code_scripts ⟶ [json, sqlite]
  - [automatic] cross-reference spec vs code ⟶ gaps_report.md
  - [automatic] lint code_scripts ⟶ violations.json
    - import-linter: camadas proibidas
    - pylint: duplicate-code, unused-*, cyclic-import
    - mypy strict: tipos
    - radon + xenon: complexidade
    - pep8-naming: convencao de nomes
    - vulture: codigo morto
    - isort: ordem de imports
    - eradicate: codigo comentado
    - architecture_enforcer: SRP, metodo unificado, acoplamento
  - [agent] review code_scripts ⟶ review_code_scripts_{version}.md
    - le SQLite spec + SQLite code + gaps_report.md + violations.json
    - avalia SOLID/SRP sobre dados reais
    - recomenda refatoracoes
  - [session] update [SRD, session_code_blocks, code_scripts]
  - codigo funcionando? sim, entao proximo loop
- loop update [SRD, session_code_blocks, code_scripts]
  - [automatic] parse [SRD, session_code_blocks, code_scripts] ⟶ [json, sqlite]
  - [automatic] cross-reference spec vs code ⟶ gaps_report.md
  - [automatic] lint code_scripts ⟶ violations.json
  - [agent] review [SRD, session_code_blocks, code_scripts] ⟶ [review_srd_{version}.md, review_code_blocks_{version}.md, review_code_scripts_{version}.md]
  - [session] update [SRD, session_code_blocks, code_scripts]
  - [session] update tables [naming_rules, variables_rules, data_object_rules, orchestrator_rules]

## 1.3. Automatic Functions

| Funcao                       | Descricao                                                      | Requisitos                                                                                                                                                                                               |
| ---------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| update PRD                   | Le PRD_00 + template_PRD, produz PRD_01                        | template_PRD existente; regras de formatacao de documento                                                                                                                                                |
| update AGENTS.md             | Le AGENTS + PRD_01, transclui hipertextos                      | AGENTS.md existente; PRD_01 disponivel                                                                                                                                                                   |
| create SRD                   | Le PRD_02 + template_SRD, produz SRD_00                        | template_SRD existente; regras de heading definidas nas instrucoes                                                                                                                                       |
| parse PRD, SRD               | Extrai AST de markdown -> json, sqlite                         | markdown-it-py; documento segue formato de heading esperado                                                                                                                                              |
| parse session_code_blocks    | Extrai AST de markdown -> json, sqlite                         | markdown-it-py; code blocks com lang tag; tabelas com 3 colunas padrao                                                                                                                                   |
| parse code_scripts           | Extrai AST de codigo ps1, python, dart -> json, sqlite         | Para dart: subprocess + parse_dart_ast.dart. Para python: ast module (stdlib). Para ps1: parser heuristico (regex)                                                                                       |
| cross-reference spec vs code | Compara SQLite spec (SRD) com SQLite code (parse), produz gaps | SQLite spec populado; SQLite code populado; script de cruzamento                                                                                                                                         |
| lint code_scripts            | 9 ferramentas em sequencia -> violations.json                  | import-linter config de camadas; pylint .pylintrc; mypy strict; radon/xenon thresholds; pep8-naming plugin; vulture whitelist; isort profile; eradicate CLI; architecture_enforcer com tabelas de regras |

## 1.4. Agent Functions

| Funcao                     | Descricao                                                         | Requisitos                                                                      |
| -------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| spec-edit                  | Edita SRD, session_code_blocks                                    | Documento existente; regras de heading e formatacao                             |
| spec-review                | Revisa SRD, session_code_blocks -> review_srd, review_code_blocks | SQLite spec + SQLite code + gaps_report.md + violations.json; skill spec-review |
| create session_code_blocks | Cria session_code_blocks a partir de SRD + regras                 | SRD existente; tabelas de regras definidas; template de code blocks             |
| code-script-edit           | Cria ou edita code_scripts a partir de session_code_blocks        | session_code_blocks existente; SRD como referencia                              |
| code-script-review         | Revisa code_scripts -> review_code_scripts                        | SQLite code + violations.json + gaps_report.md; skill code-review               |

---

# 2. Formatacao: Template Final das Secoes (SRD_03)

O SRD_03 definiu o template definitivo para cada secao. Abaixo o mapeamento de headings, campos extraidos e regras de formatacao.

## 2.1. Secao 3 — arquitetura do projeto

h2 = `layer {layer_name}` (layer frontend, layer backend, layer dados)
h3 = `pasta {caminho_relativo_da_pasta}`

Tabela de arquivos:

| pasta | arquivo | descricao |
| ----- | ------- | --------- |

Campos extraidos por pattern matching:
- `layer {name}`: h2 text apos "layer "
- `pasta {path}`: h3 text apos "pasta "

## 2.2. Secao 4 — arquitetura de funcoes

4 secoes h2 fixas: resumo, pipeline, automatic functions, agent functions

Pipeline: lista nao ordenada com `[function_type] {function_name}`
Tabela de funcoes:

| funcao | arquivos principais | descricao |
| ------ | ------------------- | --------- |

Campos extraidos:
- funcao: primeira coluna da tabela
- scripts: segunda coluna (lista de scripts associados)
- descricao: terceira coluna

## 2.3. Secao 5 — arquitetura de dados

hierarquia: dados de negocio > dados fonte/transformados/run time > modelos
Tabelas de campos com [campo, tipo, descricao]

## 2.4. Secao 6 — descricoes funcionais

h2 = `scripts {function_group}`
h3 = `script {caminho_relativo} [{funcao1}, {funcao2}]`
h4 = `classe {Nome} [{responsabilidade}]`

Tabela de metodos:

| metodo | assinatura | descricao |
| ------ | ---------- | --------- |

Campos extraidos por pattern matching:
- function_group: h2 text apos "scripts "
- script: h3 text entre "script " e " ["
- funcao: h3 text entre "[" e "]"
- classe: h4 text entre "classe " e " ["
- tag_classe: h4 text entre "[" e "]"
- metodo: primeira coluna da tabela
- assinatura: segunda coluna da tabela
- descricao: terceira coluna da tabela

### 2.4.1. Regras de parse para secao 6

| Elemento | Formato                                | Exemplo                                                 | Campo extraido                |
| -------- | -------------------------------------- | ------------------------------------------------------- | ----------------------------- |
| h2       | `scripts {group}`                      | `scripts parse_md`                                      | function_group                |
| h3       | `script {path} [{funcao}]`             | `script src/services/parse/md_ast_parser.py [parse_md]` | script, funcao                |
| h4       | `classe {Nome} [{resp}]`               | `classe GenerateAst [transformacao]`                    | classe, tag_classe            |
| tabela   | colunas: metodo, assinatura, descricao |                                                         | metodo, assinatura, descricao |

### 2.4.2. Regras que o markdown DEVE seguir

- h3 deve comecar com "script " para ser detectado como script
- h3 deve conter "[{funcao}]" (bracket apos o path)
- h4 deve comecar com "classe " e conter "[{responsabilidade}]"
- Tabelas: primeira linha = header, segunda = separador |---|
- Colunas da tabela na ordem exata: Metodo, Assinatura, Descricao
- Code blocks: lang tag obrigatoria (```python, ```dart, etc.)

## 2.5. Parsing de Code Scripts (ps1, python, dart)

**Python**: parse_script_raw.py extrai linhas/comentarios/tags. Parser AST com `ast` module nao implementado.

**PowerShell**: sem parser AST. parse_script_raw.py funciona para extracao basica. PS1 e o frontend do painel (258 linhas).

**Dart**: parse_script_dart_ast.py + parse_dart_ast.dart via subprocess. AstNode model: type, offset, length, line, column, children.

**Lacuna**: parser AST para python e ps1 nao implementados. Apenas raw parser e dart parser existem.

---

# 3. Recomendacoes

## 3.1. Formatacao

Acoes para garantir que documentos sigam o template do SRD_03 e sejam parseaveis.

| Prioridade  | Acao                                      | Descricao                                                                           | Impacto                                      | Dependencia              |
| ----------- | ----------------------------------------- | ----------------------------------------------------------------------------------- | -------------------------------------------- | ------------------------ |
| imediatas   | Validar SRD_03 contra template            | Verificar se todas as secoes seguem os templates definidos em 1.2.3 a 1.2.6         | Garantir que SRD_03 e parseavel              | Template definido        |
| imediatas   | Testar extracao real do SRD_03            | Executar parse_md_ast contra SRD_03 e verificar tabelas SQLite                      | Validacao pratica de que o template funciona | parse_md_ast funcionando |
| curto prazo | Documentar templates em AGENTS.md         | Instrucao clara para o agente: templates de cada secao do SRD, exemplos de headings | Agentes geram documentos no formato correto  | Templates definidos      |
| curto prazo | Criar script validador de headings        | Script que varre .md e alerta se h2/h3/h4 nao seguem padrao do SRD_03               | Prevencao contra documentos nao parseaveis   | Regras do SRD_03         |
| curto prazo | Atualizar template_PRD                    | Garantir que PRD tambem siga a formatacao de headings do SRD_03                     | Documentos de projeto consistentes           | Template do SRD_03       |
| medio prazo | Adicionar funcao ao heading_ctx do parser | Extrair bracket de funcao do h3 na secao 6 (ou do h2, dependendo do contexto)       | funcao disponivel no SQLite                  | Decisao de onde extrair  |

## 3.2. Automatic Functions

Acoes para implementar as ferramentas do pipeline.

| Prioridade  | Acao                                      | Descricao                                                                      | Impacto                                | Dependencia                          |
| ----------- | ----------------------------------------- | ------------------------------------------------------------------------------ | -------------------------------------- | ------------------------------------ |
| imediatas   | Extrair campo funcao no parser            | Adicionar extracao do bracket `[{...}]` no heading do script (h3 na secao 6)   | funcao disponivel para cross-reference | Nenhuma                              |
| imediatas   | Adicionar coluna funcao nas views SQLite  | Incluir `funcao` em vw_md_doc, vw_md_ast_code, vw_md_ast_tables                | Cross-reference funcional              | Campo funcao no parser               |
| imediatas   | Criar script cross-reference spec vs code | Compara SQLite spec vs SQLite code, produz gaps                                | Fecha o loop do pipeline               | Parse + views com funcao             |
| curto prazo | Criar architecture_enforcer.py            | SRP por nome (Save->write/save), metodo unificado, acoplamento de orquestrador | Detecta violacoes SRP                  | Nenhuma                              |
| curto prazo | Configurar import-linter                  | Camadas: controllers, services, utils, repositories, models                    | Impede imports proibidos               | Nenhuma                              |
| curto prazo | Criar lint_arch.bat                       | Script unificado com todas as 9 ferramentas de lint                            | Um comando para validacao completa     | architecture_enforcer, import-linter |
| medio prazo | Criar parser AST python                   | Usar `ast` module stdlib: classes, metodos, funcoes, variaveis                 | Fecha lacuna de parse para python      | Nenhuma                              |
| medio prazo | Criar parser heuristico PS1               | Regex + indentacao: function, parametros, chamadas                             | Fecha lacuna de parse para PS1         | Nenhuma                              |
| medio prazo | Integrar lint_arch.bat no pipeline        | Disparo automatico apos parse, antes do agent review                           | Pipeline de qualidade completo         | lint_arch.bat                        |

## 3.3. Agent Functions

Acoes para integrar agentes de IA no pipeline de revisao.

| Prioridade  | Acao                                   | Descricao                                                                                 | Impacto                               | Dependencia                          |
| ----------- | -------------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------- | ------------------------------------ |
| imediatas   | Criar prompt padrao agent-review       | Instruir agente: ler SQLite spec + code + violations, avaliar SOLID/SRP, produzir review  | Revisao consistente                   | Cross-reference, lint_arch           |
| curto prazo | Criar skill spec-review                | Validar: consistencia spec vs code, funcoes declaradas no bracket, toda funcao com script | Revisao automatizada de especificacao | Cross-reference                      |
| curto prazo | Criar skill code-review                | Verificar: SOLID/SRP contra dados reais, scripts executam apenas funcoes declaradas       | Deteccao de violacoes estruturais     | architecture_enforcer, import-linter |
| medio prazo | Alimentar tabelas de regras via agente | Agente sugere atualizacoes para naming_rules, variables_rules, data_object_rules          | Regras evoluem com o codigo           | Skills de review                     |

## 3.4. Pipeline de Qualidade (visao completa)

```
[spec] SRD_03 ──parse──> SQLite spec_tables (funcao, script, classe, metodo)
                            │
[code] scripts ──parse──> SQLite code_tables (script, classe, metodo, assinatura)
                            │
                            ├── cross-reference ──> gaps_report.md
                            │      spec vs code: [missing, extra, mismatch]
                            │
                            ├── lint_arch.bat ─────> violations.json
                            │      import-linter, pylint, mypy, radon/xenon,
                            │      pep8-naming, vulture, isort, eradicate,
                            │      architecture_enforcer
                            │
                            └── agent review ──────> review_NN.md
                                   le SQLite spec + code + gaps + violations
                                   avalia SOLID/SRP sobre dados reais
                                   recomenda refatoracoes
```

---

# 4. Observacoes Finais

## 4.1. SRD_03: Template Validado

O SRD_03 definiu o template final. Os templates das secoes 3, 4 e 6 foram testados em Excel e confirmados como parseaveis.

Diferencas entre SRD_02 e SRD_03:
- Secao 3: mudou de tabela com linhas/status para `layer` > `pasta` > tabela [pasta, arquivo, descricao]
- Secao 4: secoes h2 fixas (resumo, pipeline, automatic, agent) com tabelas de funcoes
- Secao 6: h2=`scripts {group}`, h3=`script {path} [{funcao}]`, h4=`classe {Nome} [{resp}]` — formato final
- Secao 5: reestruturada para dados de negocio vs dados de controle

A Opcao B (bracket `[{funcao}]`) foi mantida, mas no h3 (script), nao no h2 como proposto inicialmente.

## 4.2. Lacuna de Parser PS1

Frontend do painel em PS1 (258 linhas) sem parser AST. parse_script_raw.py funciona para extracao basica, mas sem hierarquia de classes/metodos. Recomendado parser heuristico.

## 4.3. Nomenclatura

parse_script_dart_ast.py (services/parse/) tem nome ambiguo: processa AST Dart, nao python. Sugestao: renomear para parse_dart_code_ast.py ou manter e documentar em AGENTS.md.

## 4.4. Proximos Passos

1. Testar parse real do SRD_03: executar parse_md_ast contra o documento
2. Adicionar extracao de funcao no parser (bracket do h3)
3. Atualizar views SQLite com coluna funcao
4. Criar cross-reference spec vs code
5. Implementar architecture_enforcer.py
6. Configurar import-linter
7. Criar tabela indice de schemas JSON no SRD (secao 5)
8. Criar script validador jsonschema (pipeline dados)

## 4.5. Decisoes de Arquitetura para Dados

### 4.5.1. Problema

JSON models (`post_model_NN.json`, `posts_config.json`) tem estrutura aninhada que tabelas markdown nao representam com fidelidade (perde nesting, tipos compostos, enums).

### 4.5.2. Solucao

O SRD **nao** contem o schema inline. Contem uma **tabela indice** em `secao 5 > modelos para code scripts` listando os pares:

| modelo      | schema                                    | dados                                    | validacao        |
| ----------- | ----------------------------------------- | ---------------------------------------- | ---------------- |
| post_config | `dev/src/models/post_config.schema.json`  | `dev/dataMu/posts_config.json`           | jsonschema       |
| post_model  | `dev/src/models/post_model.schema.json`   | `dev/dataMu/post_model_NN.json`         | jsonschema       |

O cross-check e feito via `jsonschema.validate()` **direto nos arquivos**, sem inducao por SQLite. O SQLite serve apenas como catalogo dos pares.

### 4.5.3. SQL vs JSON: pipelines diferentes

| Tipo | Spec reside em | Validacao | SQLite agrega? |
| --- | --- | --- | --- |
| Tabelas SQL | Tabelas no SRD (colunas, tipos) | Query SQL compara spec vs codigo | **Sim** — JOIN entre tabelas |
| JSON models | `dev/src/models/*.schema.json` | `jsonschema.validate()` direto | **Nao** — so catalogo |

### 4.5.4. Pipeline de validacao de dados

```
SRD (tabela indice) ──parse──> SQLite (catalogo de pares schema/data)
                                      │
                                      ├── jsonschema.validate(schema, data) ──> gaps_report.json
                                      │    para cada par [modelo, schema_path, data_path]
                                      │
                                      └── dev/src/models/validation/ ──> scripts de verificacao
                                           (validaçao estrutural, nao teste de logica)
```

### 4.5.5. Testes vs Validacao

| Artefato | O que faz | Onde fica | Exemplo |
| --- | --- | --- | --- |
| Test | Chama funcao real, asserta resultado esperado | `dev/src/tests/` (espelha src/) | `test_tokens_to_ast()` |
| Validation | Verifica dados contra schema | `dev/src/models/validation/` | `validate_post_model()` |

Testes de logica seguem TDD (red > green > refactor), versionados em **main**. Servem como rede de seguranca para refatoracoes.

### 4.5.6. Camadas finais do projeto

Conforme acordado na sessao, as camadas finais do projeto sao:

| camada   | pastas                                                                 | comentario                                                                     |
| -------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| frontend | `dev/src/view_shell/`                                                  | PS1 UI — existente                                                             |
| backend  | `dev/src/{controllers, repositories, services, utils}`                | logica de negocio — existente                                                  |
| backend  | `dev/src/models/validation/`                                           | validacao de schemas e dados                                                   |
| backend  | `dev/src/tests/`                                                       | testes de logica, espelha src/                                                 |
| dados    | `dev/dataMu/{data_docs, dbMu}`                                         | documentos e bancos SQLite — existentes                                        |
| dados    | `dev/src/{config, models, sql_sqlite}`                                 | configuracoes, schemas JSON, scripts SQL — existentes                          |
| agents   | `dev/agents/{agent_name}/skills/`                                      | fora do padrao opencode de deteccao automatica ate validacao intensa           |
| docs     | `dev/docs/docs/`                                                       | especificacoes ja implementadas                                                |
| docs     | `dev/docs/spec/`                                                       | especificacoes para implementar                                                |
| temp     | `dev/temp/{branch}/`                                                   | POC alinhadas com branches, .gitignore — uso eventual                          |


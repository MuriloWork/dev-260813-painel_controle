**Analise do Pipeline Principal e Formatacao — v01**

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

| Funcao                       | Descricao                                                                                 | Requisitos                                                                                                                                                                                               |
| ---------------------------- | ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| update PRD                   | Le PRD_00 + template_PRD, produz PRD_01                                                   | template_PRD existente; regras de formatacao de documento                                                                                                                                                |
| update AGENTS.md             | Le AGENTS + PRD_01, transclui hipertextos                                                 | AGENTS.md existente; PRD_01 disponivel                                                                                                                                                                   |
| create SRD                   | Le PRD_02 + template_SRD, produz SRD_00                                                   | template_SRD existente; regras de heading (h2="script path", h3="classe Nome [resp]", h4="metodo - type")                                                                                                |
| parse PRD, SRD               | Extrai AST de markdown -> json, sqlite                                                    | markdown-it-py; documento segue formato de heading esperado                                                                                                                                              |
| parse session_code_blocks    | Extrai AST de markdown -> json, sqlite                                                    | markdown-it-py; code blocks com lang tag; tabelas com 3 colunas padrao                                                                                                                                   |
| parse code_scripts           | Extrai AST de codigo ps1, python, dart -> json, sqlite                                    | Para dart: subprocess + parse_dart_ast.dart. Para python: ast module (stdlib). Para ps1: parser heuristico (regex)                                                                                       |
| cross-reference spec vs code | Compara SQLite spec (SRD) com SQLite code (parse) e produz gaps: missing, extra, mismatch | SQLite spec populado; SQLite code populado; script de cruzamento                                                                                                                                         |
| lint code_scripts            | 9 ferramentas em sequencia -> violations.json                                             | import-linter config de camadas; pylint .pylintrc; mypy strict; radon/xenon thresholds; pep8-naming plugin; vulture whitelist; isort profile; eradicate CLI; architecture_enforcer com tabelas de regras |

## 1.4. Agent Functions

| Funcao                     | Descricao                                                         | Requisitos                                                                      |
| -------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| spec-edit                  | Edita SRD, session_code_blocks                                    | Documento existente; regras de heading e formatacao                             |
| spec-review                | Revisa SRD, session_code_blocks -> review_srd, review_code_blocks | SQLite spec + SQLite code + gaps_report.md + violations.json; skill spec-review |
| create session_code_blocks | Cria session_code_blocks a partir de SRD + regras                 | SRD existente; tabelas de regras definidas; template de code blocks             |
| code-script-edit           | Cria ou edita code_scripts a partir de session_code_blocks        | session_code_blocks existente; SRD como referencia                              |
| code-script-review         | Revisa code_scripts -> review_code_scripts                        | SQLite code + violations.json + gaps_report.md; skill code-review               |

---

# 2. Formatacao: Onde o Parse Depende de Estrutura

## 2.1. Parsing de Markdown (SRD, PRD, session_code_blocks)

O parser md_ast_parser.py usa heading_ctx tracking (h1-h6). As tabelas SQLite resultantes tem os campos `script, classe, metodo` populados por h2, h3, h4.

**Regras que o markdown DEVE seguir para o parse funcionar:**

| Elemento         | Regra                                                  | Consequencia se quebrada     |
| ---------------- | ------------------------------------------------------ | ---------------------------- |
| Heading h2       | Deve conter "script " para ser detectado como script   | script fica vazio no SQLite  |
| Heading h3       | Deve conter "classe " entre "classe " e "["            | classe fica vazio            |
| Heading h3       | Responsabilidade entre "[" e "]"                       | tag_classe fica vazio        |
| Heading h4       | Nome do metodo                                         | metodo fica vazio            |
| Tabelas markdown | Primeira linha = header, segunda = separador `\|---\|` | Transpose falha              |
| Tabelas markdown | Colunas na ordem: Metodo, Assinatura, Descricao        | Campos col_01/02/03 trocados |
| Code blocks      | Precisam de lang tag (\`\`\`python)                    | lang fica '(sem tag)'        |

## 2.2. Problema Atual de Formatacao no SRD_01

O SRD_01 que criamos nesta sessao NAO segue as regras de heading que o parser espera.
Exemplo: secao 6.2.1 usa `### 6.2.1. script services/parse/parse_md_ast.py` (h3), mas deveria ter `classe` no heading para que o parser identifique classes e metodos.

**Diagnostico**: O SRD_01 tem a estrutura de secoes correta (h3 para scripts, h4 para classes, tabelas de metodos) MAS:
- h2 usa `{numero}. {nome}` em vez de `script {path}` → parser nao reconhece como script
- h3 NAO contem "classe " → parser nao extrai responsabilidade
- h4 NAO contem nome do metodo puro → parser nao extrai metodo

**Tabela de comparacao: formato esperado vs formato atual no SRD_01:**

| Elemento    | Formato esperado pelo parser         | Formato atual no SRD_01                              |
| ----------- | ------------------------------------ | ---------------------------------------------------- |
| h2 - script | `script {caminho_relativo}`          | `{numero}. {descricao}`                              |
| h3 - classe | `classe {Nome} [{responsabilidade}]` | `{numero}.{numero}. {descricao}`                     |
| h4 - metodo | `{nome_metodo} - {type}`             | `{numero}.{numero}.{numero}. {nome_metodo} - {type}` |

## 2.3. Recomendacao de Formatacao para SRD (Opcao B)

Adotar o formato que o parser entende, com bracket `[{funcao}]` no h2:

```
# script src/services/parse/md_ast_parser.py [parse_md]

## classe GenerateAst [transformacao]

### parse_file - workflow

| Metodo     | Assinatura                     | Descricao                 |
| ---------- | ------------------------------ | ------------------------- |
| parse_file | parse_file(md_path, ast_model) | Tokeniza .md e extrai AST |

### _tokens_to_ast - data_transform

| Metodo         | Assinatura                        | Descricao                          |
| -------------- | --------------------------------- | ---------------------------------- |
| _tokens_to_ast | _tokens_to_ast(tokens, ast_model) | Converte token list flat em arvore |
```

Isso garante que:
- h2 contem "script " e "[...]" → `script = "services/parse/md_ast_parser.py"`, `funcao = "parse_md"`
- h3 contem "classe " e "[" → `classe = "GenerateAst"`, `tag_classe = "transformacao"`
- h4 contem nome do metodo puro → `metodo = "parse_file"`
- Relacao N:M funcao → script: `[parse_md, lint_code]` → funcao carrega ambas
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

## 3.1. Formatacao

Acoes para garantir que documentos e codigos sejam parseaveis pelo pipeline.

| Prioridade  | Acao                                               | Descricao                                                                                              | Impacto                                                    | Dependencia                                  |
| ----------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------- | -------------------------------------------- |
| imediatas   | Corrigir headings do SRD com Opcao B               | Criar SRD_02 com h2="script {path} [{funcao}]", h3="classe {Nome} [{resp}]", h4="{metodo} - {type}"   | Permite parse correto e vinculo funcao→script no SQLite    | Nenhuma                                      |
| imediatas   | Padronizar template de tabelas de metodo           | Tabelas markdown com 3 colunas fixas: Metodo, Assinatura, Descricao                                    | Campos col_01/02/03 corretos no SQLite                     | Nenhuma                                      |
| curto prazo | Validar formatacao de todos os .md do projeto      | Script que varre arquivos .md e alerta se h2/h3/h4 nao seguem o padrao                                 | Prevencao contra documentos nao parseaveis                 | Regras de formatacao definidas               |
| curto prazo | Documentar em AGENTS.md o formato exato de heading | Instrucao clara: "h2='script path [funcao1, funcao2]', h3='classe Nome [resp]', h4='metodo - type'"    | Agentes geram documentos no formato correto desde a origem | Nenhuma                                      |
| curto prazo | Incluir nos templates de PRD/SRD a Opcao B         | Atualizar template_SRD e template_PRD para incluir o bracket de funcao no h2 dos scripts               | Documentos novos ja nascem no formato parseavel            | Template existente                           |
| medio prazo | Validar estrutura de tabelas de metodo por AST     | Script que parseia tabelas markdown existentes e alerta se colunas diferem do padrao                   | Deteccao precoce de documentos legados com formato errado  | Parser de markdown funcionando               |

## 3.2. Automatic Functions

Acoes para implementar e integrar ferramentas automaticas de parse, lint e cross-reference no pipeline.

| Prioridade  | Acao                                         | Descricao                                                                                                     | Impacto                                                       | Dependencia                                                 |
| ----------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ----------------------------------------------------------- |
| imediatas   | Adicionar campo funcao no heading_ctx do parser | Extrair bracket `[{...}]` do h2 em md_ast_parser.py, junto com h1-h6 existentes | Cada linha no SQLite tera `funcao` preenchido              | Nenhuma (mudanca local no parser)                          |
| imediatas   | Adicionar coluna funcao nas views SQLite         | Incluir `funcao` em vw_md_doc, vw_md_ast_code e vw_md_ast_tables extraindo do heading_ctx do h2           | Dado disponivel para cross-reference e agent review          | Campo funcao no parser funcionando                         |
| imediatas   | Atualizar schema tb_json_md_ast_*                | Se necessario, adicionar coluna `funcao` nas tabelas base (ou extrair via view apenas)                    | Consistencia entre tabelas e views                          | Decisao sobre armazenar ou extrair via view                |
| imediatas   | Criar script de cross-reference spec vs code | Compara SQLite spec (SRD) vs SQLite code (parse) e produz gaps: missing, extra, mismatch                      | Fecha o loop A do pipeline — dados cruzados pela primeira vez | Parse do SRD funcionando; parse de code scripts funcionando |
| curto prazo | Criar architecture_enforcer.py               | 3 regras: SRP por nome (Save → write), metodo unificado (json.dump → write_json), acoplamento de orquestrador | Detecta violacoes SRP que nenhuma ferramenta existente cobre  | Nenhuma (script standalone)                                 |
| curto prazo | Configurar import-linter                     | Camadas: controllers → services → utils → repositories → models                                               | Impede imports de camada proibida automaticamente             | Nenhuma (config-only)                                       |
| curto prazo | Renomear parse_script_dart_ast.py            | Nome atual e ambíguo: sugestao parse_dart_code_ast.py                                                         | Clareza — nome reflete que processa AST Dart, nao python      | Nenhuma (rename + update imports)                           |
| curto prazo | Criar lint_arch.bat                          | Script unificado que executa todas as ferramentas de lint em sequencia                                        | Um comando para validacao completa (Step B do CODE CHECK)     | architecture_enforcer.py, import-linter config              |
| medio prazo | Criar parser AST para python                 | Usar `ast` module padrao da stdlib: extrair classes, metodos, funcoes, variaveis                              | Fecha lacuna de parse para python (maioria do backend)        | Nenhuma (stdlib pura)                                       |
| medio prazo | Criar parser heuristico para PS1             | Regex + indentacao: extrair function, parametros, chamadas                                                    | Fecha lacuna de parse para PS1 (frontend do painel)           | Nenhuma (regex puro)                                        |
| medio prazo | Integrar lint_arch.bat no pipeline           | Step B disparado automaticamente apos parse, antes do agent review                                            | Pipeline de qualidade completo e automatico                   | lint_arch.bat funcionando                                   |
| medio prazo | Alimentar tabelas de regras via parse        | Parse de AST (DART/python) pode sugerir automaticamente entradas para naming_rules, canonical_methods         | Reduz manutencao manual das tabelas de regras                 | Parser AST python; parser AST dart existente                |

## 3.3. Agent Functions

Acoes para integrar agentes de IA no pipeline de revisao, usando dados estruturados (SQLite, violations.json) como insumo.

| Prioridade  | Acao                                     | Descricao                                                                                                                                                                      | Impacto                                                                                                         | Dependencia                                                                 |
| ----------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| imediatas   | Mapear skills existentes para o pipeline | Skills: post-model-reviewer-config, post-model-reviewer-content, post-model-reviewer-result, meta-api-code-block-reviewer — podem ser adaptadas para revisar SRD e code_blocks | Reuso de skills existentes em vez de criar do zero                                                              | Nenhuma (skills ja existem)                                                 |
| imediatas   | Criar prompt padrao para agent-review    | Prompt que instrui o agente a: (1) ler SQLite spec, (2) ler SQLite code, (3) ler violations.json, (4) avaliar SOLID/SRP, (5) produzir review_NN.md                             | Revisao consistente entre sessoes                                                                               | Cross-reference funcionando; lint_arch.bat funcionando                      |
| curto prazo | Criar skill spec-review unificada        | Skill que le SRD + SQLite spec + gaps_report.md e verifica: (1) consistencia entre especificacao e dados extraidos; (2) se h2 declaram bracket de funcao valido (nomes reconhecidos no PRD/pipeline); (3) se toda funcao do pipeline tem ao menos um script mapeado | Revisao automatizada de especificacao; validacao do vinculo funcao→script | Cross-reference funcionando; lista de funcoes validas (do pipeline)       |
| curto prazo | Criar skill code-review com dados reais  | Skill que le SQLite code + violations.json + funcao field e verifica: (1) SOLID/SRP contra dados reais; (2) se os scripts executam apenas as funcoes que declararam no bracket do h2; (3) se classes/metodos estao no SRD correspondente | Deteccao de violacoes que ferramentas estaticas nao pegam (ex: classe orquestradora com responsabilidade dupla; script executando funcao nao declarada) | architecture_enforcer.py; import-linter; campo funcao no parser e views    |
| medio prazo | Alimentar tabelas de regras via agente   | Agente, durante code-review, sugere atualizacoes para naming_rules, variables_rules, data_object_rules baseado em padroes observados no codigo real                            | Regras evoluem junto com o codigo, sem intervencao manual                                                       | Skills de review funcionando; tabelas de regras existem                     |
| medio prazo | Loop autonomo agente → PRD → SRD         | Agente, ao detectar gap estrutural (ex: classe no codigo sem correspondente no SRD), pode iniciar automaticamente uma atualizacao do PRD/SRD                                   | Fecho do loop C — pipeline autonomo entre deteccao e correcao                                                   | Todas as skills de review; cross-reference; agente com permissao de escrita |

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

**Sugestao**: implementar parser heuristico para PS1 baseado em regex (function, class, parametros, chamadas) ate que uma solucao mais robusta seja necessaria.

## 4.3. Nomenclatura

O script `parse_script_dart_ast.py` (services/parse/) tem nome ambiguo. Ele:
- Processa AST de codigo Dart via subprocess (chama `dart run parse_dart_ast.dart`)
- NAO faz parse de script python

Sugestao renomear para `parse_dart_code_ast.py` para clareza, ou manter e documentar em AGENTS.md.

## 4.4. Sobre o SRD_01 e o Proximo SRD_02

O SRD_01 e valido como **documento de consulta humana** (tem descricoes detalhadas, tabelas de linhas, status de implementacao). Porem, para ser parseavel, precisa de uma segunda versao (SRD_02) que:
- Reorganize os headings para o formato parser-friendly
- Mantenha o conteudo detalhado nas secoes de descricoes funcionais (secao 6)
- Use a secao 4 (arquitetura de funcoes) para o formato parseavel com headings padrao
- Inclua todas as classes e metodos que existem no codigo real (nao apenas os principais)

Sugestao: manter SRD_01 como referencia humana e criar SRD_02 como versao parseavel.

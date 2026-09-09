# 1. Sobre este documento

## 1.1. resumo
SRD (Software Requirements Document, ou Documento de Requisitos do Produto), documento nº 2 da familia de documentos de projeto [PRD, SRD, session_code_blocks, code_scripts, plan, plan_control].
O SRD define as especificações detalhadas para o desenvolvimento do projeto, sob a ótica funcional, suas responsabilidades, lógicas e modelos de funções e de dados. As especificações do SRD terão os nomes de todos os [code_scripts, classes, metodos] com descrições em linguagem natural das responsabilidades e logicas, ficando a cargo do documento session_code_blocks (blocos de codigo em documento markdown) especificar explicitamente os algoritmos de cada [classe, metodo] em snippets de codigo.

**Conceitos base**:
- Arquitetura em camadas [frontend, backend, dados]
- Arquitetura SOLID:  
	- SRP - Single Responsbility Principle (Responsabilidade Única)
		- Uma classe deve ter um, e somente um, motivo para mudar. Ela deve ser especializada em um único assunto e possuir apenas uma única responsabilidade dentro do seu software.
	- OCP - Open Closed Principle (Aberto Fechado)
		- Suas camadas de domínio e casos de uso devem ser abertas para extensão, mas fechadas para modificação. Você adiciona novas regras ou integrações criando novos componentes, sem alterar o código central que já funciona
	- LSP - Liskov Substitution Principle (Substituição de Liskov)
		- Classes derivadas devem poder ser substitutas de suas classes base
	- ISP - Interface Segregation Principle (Segregação de Interfaces)
		- Interfaces específicas são melhores do que uma interface única e genérica. As camadas da Clean Architecture comunicam-se através de contratos enxutos, forçando o baixo acoplamento.
	- DIP - Dependence Inversion Principle (Inversão de Dependências)
		- Módulos de alto nível (regras de negócio) não devem depender de módulos de baixo nível (banco de dados, frameworks); ambos devem depender de abstrações. As dependências sempre apontam para dentro, em direção ao domínio.

## 1.2. instruções

### 1.2.1. instruções gerais
Como este documento é utilizado:
- 3 formas de atualização: 
	1. **manualmente** pelo usuario
	2. em **sessões interativas** com agente de IA
	3. **automaticamente** por code scripts, portanto é importante que o template seja respeitado, principalmente a estrutura de seções (headings) e seus titulos.
- extração de conteúdo da AST (Abstract Syntax Tree) das seções [arquitetura de funções,arquitetura de dados] por parsing code scripts para tabelas de dados para controle de conformidade, qualidade e implementação dos códigos.

Considerar como conteúdos **não editáveis**:
- textos das seções com titulo "instruções"
- titulos das seções existentes no inicio de uma "sessão interativa"
- estrutura (seções, subseções, titulos) das seções [arquitetura de funções,arquitetura de dados]

Considerar como conteúdos **editáveis**:
- titulos de seções novas, criadas durante uma "sessão interativa", seguir os name templates definidos nas instruçoes de cada seção
- textos solicitados pelo usuario durante uma "sessão interativa" 

spec document name templates, sempre usar a versao mais recente
- PRD: `{ref_date}_(name)_prd_{version}.md`, onde
  - ref_date: data de referencia no formato YYMMDD
  - name: nome do projeto ou da sessão
  - version: sequencial no formato NN
- SRD: `{ref_date}_(name)_srd_{version}.md`, onde
  - ref_date: data de referencia no formato YYMMDD
  - name: nome do projeto ou da sessão
  - version: sequencial no formato NN
- plano: `{ref_date}_(name)_session_plan_{version}.md`, onde
  - ref_date: data de referencia no formato YYMMDD
  - name: nome do projeto ou da sessão
  - version: sequencial no formato NN
- controle: `{ref_date}_(name)_control_{version}.md`, onde
  - ref_date: data de referencia no formato YYMMDD
  - name: nome do projeto ou da sessão
  - version: sequencial no formato NN

"arquitetura do projeto"
- estrutura de layers [frontend, backend, dados] 
- pastas de cada layer
- code scripts de cada pasta

### 1.2.2. sobre a seção "contexto do projeto"
informações gerais e referencias do projeto

name templates, sempre usar a versao mais recente
- PRD: `{ref_date}_(name)_prd_{version}.md`, onde
  - ref_date: data de referencia no formato YYMMDD
  - name: nome do projeto ou da sessão
  - version: sequencial no formato NN
- SRD: `{ref_date}_(name)_srd_{version}.md`, onde
  - ref_date: data de referencia no formato YYMMDD
  - name: nome do projeto ou da sessão
  - version: sequencial no formato NN
- plano: `{ref_date}_(name)_session_plan_{version}.md`, onde
  - ref_date: data de referencia no formato YYMMDD
  - name: nome do projeto ou da sessão
  - version: sequencial no formato NN
- controle: `{ref_date}_(name)_control_{version}.md`, onde
  - ref_date: data de referencia no formato YYMMDD
  - name: nome do projeto ou da sessão
  - version: sequencial no formato NN

### 1.2.3. sobre a seção "arquitetura do projeto"
estrutura de layers [frontend, backend, dados] 
pastas de cada layer
code scripts de cada pasta

### 1.2.4. sobre a seção "arquitetura de funções"
Detalhamento da arquitetura de funções definida no PRD para layers [frontend, backend], sob a ótica lógica, nomeando e especificando brevemente cada [code script, classe, metodo] hierarquicamente nas seções do documento.

Sobre o template da seção
- uma subseção para cada code script, name template `script {caminho_relativo_do_script}`
- uma subseção para cada classe de cada subseção code script, name template: `classe {class_name} [{responsabilidade_1}, {responsabilidade_2}, ...]`, onde 
  - `{responsabilidade}` = papel do script no pipeline: [coordenação, extração, transformação, exportação]
- Tabela de métodos conforme template

Estilos de **formatação** da seção
- sempre usar: [texto simples, listas não ordenadas, tabelas]
- nunca usar: [thematicBreak, listas ordenadas, code blocks, backtick blocks]

- legenda: status implementação  
  - 🟢 finalizado  
  - 🔵 funcionando, falta organizar e testar consistencia  
  - 🟤 implementação script iniciada  
  - 🟡 code blocks definidos e revisados  
  - 🟠 descrição funcional definida e revisada  
  - ⚪️ descrição funcional não iniciada ou parcial  

### 1.2.5. sobre a seção "arquitetura de dados"
Detalhamento da arquitetura de dados definida no PRD para layers [frontend, backend], sob a ótica estrutural, nomeando e especificando brevemente cada [repositorio de dados fonte, tipo de armazenamento, modelo de dados usado nos code scripts] hierarquicamente nas seções do documento.

Tipos de dados:
- dados de negocio: dados principais, ligados aos objetivos do projeto
- dados de controle 
	- auth: endereços, tokens e senhas de autenticação de acesso para API e serviços
	- config: configurações estáticas de operação do sistema (projeto)
	- actions: configurações dinâmicas do pipeline do sistema (projeto), definem os tipos de ações que podem ser selecionados no disparo ou durante a operação do sistema
	- state: configurações de estado do sistema ou da interface do usuario

Distinção de conteúdo para seção "descrições funcionais" em relação aos dados do projeto:
- seção "arquitetura de dados": apenas os modelos [tabelas, campos, tipos, constraints], com formatação preferencial em tabelas
- seção "descrições funcionais": os scripts [ps1, python, dart, sql] de transformação de dados

Sobre o template da seção:
- em cada uma das subseções [dados fonte, demais dados*, modelos] criar subseção para cada [fonte, pasta, modelo] previsto no escopo do projeto
- uma subseção para cada code script, name template `script {caminho_relativo_do_script}`
- uma subseção para cada classe de cada subseção code script, name template: `classe {class_name} [{responsabilidade_1}, {responsabilidade_2}, ...]`, onde 
  - `{responsabilidade}` = papel do script no pipeline: [coordenação, extração, transformação, exportação]

Estilos de **formatação** da seção
- sempre usar: [texto simples, listas não ordenadas, tabelas]
- nunca usar: [thematicBreak, listas ordenadas, code blocks, backtick blocks]

### 1.2.6. sobre a seção "descrições funcionais"
Continuação e detalhamento das seções [arquitetura de funções, arquitetura de dados], separadamente das seções iniciais para cobrir a necessidade de conteúdo adicional em formato mais livre, que não será usado na extração de conteúdo da AST (Abstract Syntax Tree) por parsing code scripts. Ainda assim é importante respeitar a estrutura de seções (headings) do template.

Distinção de conteúdo para seção "arquitetura de dados" em relação aos dados do projeto:
- seção "arquitetura de dados": apenas os modelos [tabelas, campos, tipos, constraints], com formatação preferencial em tabelas
- seção "descrições funcionais": os scripts [ps1, python, dart, sql] de transformação de dados

Estilos de **formatação** da seção
- sempre usar: [texto simples, listas não ordenadas]
- usar moderadamente: [listas ordenadas, tabelas, backtick blocks]
- nunca usar: [thematicBreak, code blocks]

# 2. contexto do projeto

## 2.1. objetivos e resumo 

project_name: painel controle

Ferramentas de apoio para vibe coding, com interface em terminal powershell organizado em abas (paineis): shell, session, parse, logs, sync.

- painel shell: dispara comandos shell genéricos
- painel session: dispara code scripts para edição de markdown e lint tools
- painel parse: dispara parsers de markdown e code scripts (python, powershell, dart)
- painel logs: deprecated
- painel sync: dispara code scripts para sincronização de dados entre json, sqlite, csv e xlsx

## 2.2. stack do projeto 

- ambiente/servidor: local (Windows)
- UI: powershell 5.1
- script languages: ps1, python 3.10+, dart
- dados: sqlite 3, json
- dependencias python: pydantic, markdown-it-py
- dependencias dart: analyzer, http, path

## 2.3. caminhos do projeto (relativos a project_path) 

| path type | path name      | path                                                                                    |
| --------- | -------------- | --------------------------------------------------------------------------------------- |
| session   | project_path   | C:\Users\muril\OneDrive\01 mycloud\01 sistMu\10.01 scripts\01_root\main\260511_meta_api |
| target    | target_folder  | dev                                                                                     |
| ignore    | ignore_pattern | dev\.*                                                                                  |

# 3. arquitetura do projeto

## 3.1. camada frontend

Scripts de interface com usuario.

| script                         | linhas | status | responsabilidade                          |
| ------------------------------ | ------ | ------ | ----------------------------------------- |
| view_shell/painel_controle.ps1 | 258    | 🟢      | bootstrap, menu loop, dispatch de acoes   |
| view_shell/painel_view.ps1     | 28     | 🟢      | funcao Show-Menu (extraida do controle)   |
| view_shell/painel_controle.bat | 11     | 🟢      | launcher batch para abrir PS1 no terminal |

## 3.2. camada backend

Subdividida em controllers (orquestracao), services (logica de negocios), utils (utilitarios), repositories (acesso a dados), models (schemas) e config (configuracoes estaticas).

### 3.2.1. controllers

| script                            | linhas | status | responsabilidade                      |
| --------------------------------- | ------ | ------ | ------------------------------------- |
| controllers/parse_controller.py   | 22     | 🟢      | orquestracao do pipeline de parse md  |
| controllers/session_controller.py | 24     | 🟢      | gerenciamento de sessoes em memoria   |
| controllers/sync_controller.py    | 14     | 🟢      | orquestracao de sincronia json-sqlite |

### 3.2.2. services

| script                                        | linhas | status | responsabilidade                                    |
| --------------------------------------------- | ------ | ------ | --------------------------------------------------- |
| services/parse/parse_md_ast.py                | 7      | 🟢      | entry point CLI para parse de markdown              |
| services/parse/md_ast_runner.py               | 76     | 🟢      | orquestrador do pipeline md_ast (load, dispatch)    |
| services/parse/md_ast_parser.py               | 284    | 🟢      | gera AST de markdown usando markdown-it-py          |
| services/parse/parse_script_raw.py            | 271    | 🔵      | extrai linhas, comentarios e tags de scripts        |
| services/parse/parse_script_dart_ast.py       | 352    | 🔵      | processa AST de codigo Dart via subprocess analyzer |
| services/logs/logs_dart.py                    | 482    | 🔵      | aplica logs automaticamente em codigo Dart          |
| services/logs/analyze_logs.py                 | 335    | 🔵      | baixa e analisa logs do emulador Android via ADB    |
| services/dart_tools/parse_dart_ast.dart       | 598    | 🔵      | analisa AST de projetos Dart/Flutter localmente     |
| services/dart_tools/validate_schema.dart      | 219    | 🔵      | valida schemas no Supabase via API REST             |
| services/dart_tools/list_exposed_schemas.dart | 47     | 🔵      | lista schemas expostos na API REST do Supabase      |

### 3.2.3. utils

| script                                 | linhas | status | responsabilidade                                              |
| -------------------------------------- | ------ | ------ | ------------------------------------------------------------- |
| utils/init_utils/env_loader.py         | 78     | 🟢      | carrega variaveis de ambiente e paths do projeto              |
| utils/init_utils/painel_settings.py    | 13     | 🟢      | shim compat __getattr__ delegando para env_loader e config_io |
| utils/parse_utils/path_resolver.py     | 22     | 🟢      | resolve paths relativos contra PAINEL_ROOT                    |
| utils/parse_utils/string_utils.py      | 13     | 🟢      | coleta texto de nos AST recursivamente (collect_text)         |
| utils/io_utils/config_io.py            | 112    | 🟢      | carrega e expoe configuracoes dos JSONs do projeto            |
| utils/io_utils/parse_utils.py          | 106    | 🔵      | utilitarios de io: filtra arquivos por extensao/glob          |
| utils/io_utils/parse_export.py         | 55     | 🔵      | exporta dados para CSV e models Pydantic do SQLite            |
| utils/io_utils/painel_sqlite_import.py | 455    | 🔵      | importa dados para SQLite (upsert, triggers)                  |
| utils/io_utils/painel_sqlite_export.py | 129    | 🔵      | exporta dados do SQLite para JSON estruturado                 |
| utils/io_utils/md_ast_io.py            | 27     | 🟢      | le arquivos markdown do disco (ReadInputFiles)                |
| utils/io_utils/md_ast_persistence.py   | 217    | 🟢      | persiste AST markdown em JSON e SQLite (SaveOutputFiles)      |

### 3.2.4. repositories

| script                      | linhas | status | responsabilidade                          |
| --------------------------- | ------ | ------ | ----------------------------------------- |
| repositories/config_repo.py | 23     | 🟢      | le config JSONs (pipeline, actions, menu) |
| repositories/ast_repo.py    | 44     | 🟢      | persiste e carrega AST (json, sqlite)     |

### 3.2.5. models

| script                     | linhas | status | responsabilidade                             |
| -------------------------- | ------ | ------ | -------------------------------------------- |
| models/ast_dart_model.py   | 40     | 🟢      | modelos Pydantic para AST Dart               |
| models/ast_md_model.py     | 54     | 🟢      | modelos Pydantic para AST Markdown           |
| models/export_model.py     | 18     | 🟢      | modelos para exportacao (funcoes, variaveis) |
| models/import_model.py     | 13     | 🟢      | modelos para importacao (tag_map, logs)      |
| models/raw_script_model.py | 17     | 🟢      | modelos para script raw                      |

## 3.3. camada dados

| recurso                            | tipo      | descricao                                                            |
| ---------------------------------- | --------- | -------------------------------------------------------------------- |
| dataMu/dbMu/sqlite/parse_dart.db   | sqlite    | banco de dados de AST de codigo Dart                                 |
| dataMu/dbMu/sqlite/parse_md.db     | sqlite    | banco de dados de AST de markdown                                    |
| dataMu/data_docs/data_docs_painel/ | diretorio | JSONs de saida dos parsers (json_md_ast, json_script_dart_ast, etc.) |
| sql_sqlite/                        | diretorio | scripts SQL de DDL, views e triggers (27 arquivos)                   |
| config/                            | diretorio | JSONs de configuracao (pipeline, menu, actions, credentials)         |

# 4. arquitetura de funções

## 4.1. resumo

Pipeline organizado por tipo e grupo de funcao:
- automatic: criacao de markdown, extracao de AST markdown
- session: edicao de markdown e code scripts em sessoes interativas
- agent: edicao e revisao de markdown e code scripts com base em instrucoes padronizadas

Funcoes automaticas por secao do painel:
- secao parse: parse md, parse code_scripts ast, parse code_scripts raw
- secao session: update AGENTS.md, create PRD, create SRD, lint code_scripts
- secao sync: sync json-sqlite-csv-xlsx
- sql views: logic_map_functions, logic_map_functions_data, control_map_code, control_map_data

## 4.2. pipeline [type, function]

- automatic update PRD: PRD_00 + template_PRD -> PRD_01
- automatic update AGENTS.md: AGENTS + PRD_01 -> AGENTS.md
- session update PRD
- automatic create SRD: PRD_02 + template_SRD -> SRD_00
- loop update SRD (session update, automatic parse, agent review)
- session update tables (naming_rules, variables_rules, data_object_rules, orchestrator_rules)
- agent create session_code_blocks
- loop update session_code_blocks (automatic parse, agent review, session update)
- agent create code_scripts
- loop update code_scripts (automatic parse, automatic lint, agent review, session update)
- loop update SRD + session_code_blocks + code_scripts

## 4.3. automatic functions

### 4.3.1. painel controle, secao parse
- parse md: PRD, SRD, session_code_blocks -> AST (text blocks, tables, code blocks) -> json, sqlite
- parse code_scripts ps1, python, dart -> AST -> json, sqlite
- parse code_scripts ps1, python, dart -> raw -> json, sqlite

### 4.3.2. painel controle, secao session
- update PRD: input PRD_00 + template_PRD, output PRD_01
- update AGENTS.md: prompt + PRD sections + templates + rules -> AGENTS.md
- create SRD: template_SRD + rules -> SRD
- lint code_scripts: ps1, python, dart -> json, sqlite

### 4.3.3. painel controle, secao sync
- sync json-sqlite-csv-xlsx
- mirroring md, json, toml, csv, xlsx

### 4.3.4. sql views
- logic_map_functions: arquitetura funcoes x arquitetura funcoes = descricoes
- logic_map_functions_data: arquitetura funcoes x arquitetura dados = descricoes
- control_map_code: files, classes, metodos x funcoes negocio = tags pendencia, maturidade
- control_map_data: files, classes, metodos x data blocks = tags pendencia, maturidade

## 4.4. agent functions

- rule-edit: naming_rules, variables_rules, data_object_rules, orchestrator_rules
- spec-edit: SRD, session_code_blocks
- spec-review: SRD, session_code_blocks -> review_srd, review_code_blocks
- code-script-edit: code_scripts
- code-script-edit-comments: comments, tags
- code-script-review: code_scripts -> review_code_scripts
- control-map-edit
- control-map-review

# 5. arquitetura de dados

## 5.1. instrucoes e resumo

### 5.1.1. instrucoes

**Instrucao de preenchimento**:
- subsecoes
  - resumo
    - Proposito: Escrever um paragrafo introdutorio explicando que esta secao define a arquitetura funcional de alto nivel.
    - Listar o que esta FORA do escopo (ex: detalhes de implementacao interna, estruturas de dados especificas) com referencias para outras secoes do documento onde esses topicos sao abordados.
    - tipo de arquitetura utilizada: marcar cada tipo de estrutura de dados utilizada, sem eliminar as linhas para estruturas nao utilizadas
  - script models
    - schemas de extracao/importacao
    - schemas internos para transformacoes intermediarias
    - schemas de exportacao
  - documentos externos de dados
  - banco: preencher database_name
    - tabelas: uma subsecao para cada tabela, preencher o template
    - views: uma subsecao para cada view, preencher o template

### 5.1.2. resumo

**Proposito**:
Mapear toda a arquitetura funcional do sistema ate o nivel de metodos/objetos relevantes. E a secao mais detalhada e a principal fonte de dados para o hierarchy tracking (script, classe, metodo).
Documentar todas as estruturas de dados do sistema: tabelas, schemas, formatos de arquivo.

**tipo de arquitetura utilizada**:
- X script models
  - X schemas de extracao/importacao
  - schemas internos para transformacoes intermediarias
  - X schemas de exportacao
- X documentos externos de dados
- X banco
  - X tabelas
  - X views

## 5.2. modelos de dados

### 5.2.1. script models

#### 5.2.1.1. schemas de extracao/importacao

**Modelos Pydantic** (dev/src/models/):

ast_md_model.py:
- MdAstField, MdAstModel, MdTypeMap: schemas para AST de markdown
- MdBlockRow, MdCodeRow, MdTableRow: linhas para persistencia em SQLite

ast_dart_model.py:
- AstNode: no recursivo da AST Dart (type, offset, length, line, column, children)
- FlutterAppAst: raiz com project_name, file_path, ast

raw_script_model.py:
- RawScriptRow, RawScriptEntry: linhas e entradas de script raw (linha, coluna, string, comment, tag)

import_model.py:
- TagMapEntry: mapeamento de tags
- LogsStringEntry: entradas de logs string

export_model.py:
- FuncVariable, FuncOutput, FileOutput: modelos de saida
- FuncMap1DOutput, FuncMap2DOutput: mapas de funcoes 1D e 2D

**Schema declarativo para AST Markdown** (classe GenerateAst em md_ast_parser.py):

ast_model: dict declarativo que mapeia cada no AST com seus campos e hierarquia de filhos. Tipos reconhecidos: heading, paragraph, text, strong, em, inlineCode, link, code, list, listItem, blockquote, thematicBreak, table, tableRow, tableCell.

Campos implicitos em todo no: type, children. Campos extras declarados em fields: depth, start_line, end_line, url, title, lang, value, ordered.

#### 5.2.1.2. schemas internos para transformacoes intermediarias

Nao aplicavel: nao ha transformacoes intermediarias entre schemas no pipeline atual.

#### 5.2.1.3. schemas de exportacao

Tres schemas declarativos (json_schema_blocks, json_schema_code, json_schema_tables) aplicados ao AST para gerar JSONs de saida e tabelas SQLite:

json_schema_blocks:
- file_path, line, block_type, level, script, classe, metodo, content
- Fonte: entry e ast.node, com heading_ctx tracking para script/classe/metodo

json_schema_code:
- file_path, line, lang, script, classe, metodo, value
- Conteudo integral do bloco de codigo

json_schema_tables:
- file_path, line, row, col, cell_type, script, classe, metodo, value
- Transpose de celulas para linhas individuais

### 5.2.2. documentos externos de dados

Diretorio dataMu/dbMu/sqlite/:
- parse_dart.db: banco SQLite com AST de codigo Dart
- parse_md.db: banco SQLite com AST de markdown (3 tabelas + 3 views)

Diretorio dataMu/data_docs/data_docs_painel/:
- json_md_ast/: JSONs de saida do parser markdown
- json_script_dart_ast/: JSONs de saida do parser Dart AST
- json_script_dart_ast_func/: JSONs de saida de funcoes Dart
- json_script_raw/: JSONs de saida do parser raw
- json_xls/: JSONs de saida de planilhas
- logs/: arquivos de log

Diretorio config/:
- set_painel_pipeline_paths.json: paths do pipeline (db, source, target)
- set_painel_menu.json: definicoes de abas e comandos do menu
- set_painel_actions_data_paths.json: paths de dados por acao (488 linhas)
- credentials/: service_account.json, google_oauth_tokens.json, client_secret.json

### 5.2.3. banco parse_md.db

Banco SQLite em dataMu/dbMu/sqlite/parse_md.db. Contem 3 tabelas e 3 views.

#### 5.2.3.1. tabela tb_json_md_ast_blocks - blocos do documento

| campo        | tipo    | descricao                                                                        |
| ------------ | ------- | -------------------------------------------------------------------------------- |
| id           | INTEGER | PK autoincrement                                                                 |
| project_name | TEXT    | nome da pasta do projeto principal (ex: 260511_meta_api)                         |
| version      | TEXT    | timestamp da sessao de extracao                                                  |
| folder_path  | TEXT    | caminho absoluto da pasta raiz da extracao                                       |
| file_path    | TEXT    | caminho relativo a pasta raiz da extracao, UNIQUE                                |
| json_data    | TEXT    | JSON array de objetos {line, block_type, level, script, classe, metodo, content} |

#### 5.2.3.2. tabela tb_json_md_ast_code - blocos de codigo

| campo        | tipo    | descricao                                                         |
| ------------ | ------- | ----------------------------------------------------------------- |
| id           | INTEGER | PK autoincrement                                                  |
| project_name | TEXT    | nome da pasta do projeto principal                                |
| version      | TEXT    | timestamp da sessao de extracao                                   |
| folder_path  | TEXT    | caminho absoluto da pasta raiz da extracao                        |
| file_path    | TEXT    | caminho relativo, UNIQUE                                          |
| json_data    | TEXT    | JSON array de objetos {line, lang, script, classe, metodo, value} |

#### 5.2.3.3. tabela tb_json_md_ast_tables - tabelas

| campo        | tipo    | descricao                                                                        |
| ------------ | ------- | -------------------------------------------------------------------------------- |
| id           | INTEGER | PK autoincrement                                                                 |
| project_name | TEXT    | nome da pasta do projeto principal                                               |
| version      | TEXT    | timestamp da sessao de extracao                                                  |
| folder_path  | TEXT    | caminho absoluto da pasta raiz da extracao                                       |
| file_path    | TEXT    | caminho relativo, UNIQUE                                                         |
| json_data    | TEXT    | JSON array de objetos {line, row, col, cell_type, script, classe, metodo, value} |

#### 5.2.3.4. view vw_md_doc

Fonte: tb_json_md_ast_blocks -> json_each(json_data)

| campo saida | tipo | descricao                                               |
| ----------- | ---- | ------------------------------------------------------- |
| file_path   | TEXT | caminho relativo do arquivo de origem                   |
| line        | INT  | linha inicial do bloco (0-indexed)                      |
| block_type  | TEXT | tipo do no markdown (paragraph, heading, listItem, etc) |
| level       | INT  | profundidade do heading (NULL para nao-headings)        |
| script      | TEXT | texto do heading h2 ancestral                           |
| classe      | TEXT | texto do heading h3 ancestral                           |
| metodo      | TEXT | texto do heading h4 ancestral                           |
| content     | TEXT | texto plano do bloco incluindo inlineCode               |

Blocos code, table e thematicBreak excluidos. ORDER BY file_path, line.

#### 5.2.3.5. view vw_md_ast_code

Fonte: tb_json_md_ast_code -> json_each(json_data)

| campo saida | tipo | descricao                                         |
| ----------- | ---- | ------------------------------------------------- |
| file_path   | TEXT | caminho relativo do arquivo de origem             |
| line        | INT  | linha inicial do bloco de codigo (0-indexed)      |
| lang        | TEXT | linguagem do code fence; '(sem tag)' quando vazio |
| script      | TEXT | texto do heading h2 ancestral                     |
| classe      | TEXT | texto do heading h3 ancestral                     |
| metodo      | TEXT | texto do heading h4 ancestral                     |
| value       | TEXT | conteudo integral do bloco de codigo              |

ORDER BY file_path, line.

#### 5.2.3.6. view vw_md_ast_tables

Fonte: tb_json_md_ast_tables -> json_each(json_data), transpose

| campo saida    | tipo | descricao                                                |
| -------------- | ---- | -------------------------------------------------------- |
| file_path      | TEXT | caminho relativo do arquivo de origem                    |
| section_01..06 | TEXT | headings ancestrais h1-h6                                |
| line           | INT  | linha inicial da tabela (0-indexed)                      |
| script         | TEXT | extraido da section_N com conteudo script                |
| tag_classe     | TEXT | extraido entre [ e ] da section_N com conteudo classe    |
| classe         | TEXT | extraido entre classe [ da section_N com conteudo classe |
| row            | INT  | indice da linha na tabela (0-indexed)                    |
| col_01..03     | TEXT | transpose de col+value (col_01 = nome do metodo)         |

ORDER BY file_path, section_01..06, line, row.

### 5.2.4. banco parse_dart.db

Banco SQLite em dataMu/dbMu/sqlite/parse_dart.db. Contem tabelas de AST de codigo Dart.

#### 5.2.4.1. tabela tb_ast

| campo   | tipo    | descricao                                   |
| ------- | ------- | ------------------------------------------- |
| id      | INTEGER | PK autoincrement                            |
| project | TEXT    | nome do projeto Dart                        |
| source  | TEXT    | arquivo de origem                           |
| type    | TEXT    | tipo do no (class, function, variable, etc) |
| name    | TEXT    | nome do no                                  |
| offset  | INTEGER | posicao no arquivo                          |
| length  | INTEGER | tamanho                                     |
| line    | INTEGER | linha                                       |
| column  | INTEGER | coluna                                      |

#### 5.2.4.2. tabela tb_ast_func

Tabela derivada de funcoes extraidas da AST Dart.

#### 5.2.4.3. tabela tb_ast_func_map_1d e tb_ast_func_map_2d

Mapas de funcoes 1D (linear) e 2D (bidimensional) para analise de acoplamento.

#### 5.2.4.4. tabela tb_controle_ast

Controle de versao e estado das extracoes de AST.

#### 5.2.4.5. views do banco parse_dart.db

Views em sql_sqlite/sql_parse_script/:
- vw_ast_func: funcoes extraidas da AST
- vw_ast_group: agrupamento de nos AST
- vw_data_flow_flat_mu: fluxo de dados (flat)
- vw_raw_ast: AST raw
- vw_raw_flat_01, vw_raw_flat_02: visoes flat de dados raw
- vw_widget: widgets detectados na AST

Views de controle:
- vw_func_tag_map: mapa de funcoes por tag
- vw_tag_map: mapa de tags

### 5.2.5. dados de controle

#### 5.2.5.1. auth

Arquivos em config/credentials/:
- service_account.json: credencial Google Service Account
- google_oauth_tokens.json: token OAuth Google
- client_secret.json: client secret OAuth

#### 5.2.5.2. config (estatico)

- config/set_painel_pipeline_paths.json: paths de banco, fonte e alvo do pipeline
- config/set_painel_menu.json: definicao de abas e comandos do menu

#### 5.2.5.3. actions (dinamico)

- config/set_painel_actions_data_paths.json: paths especificos por acao do pipeline

#### 5.2.5.4. state

Nao implementado: estado do sistema e da interface gerenciado em memoria pelas classes SessionManager (session_controller.py) e pelas variaveis em env_loader.py (PAINEL_ROOT, PAINEL_SRC_DIR, etc.)

# 6. descricoes funcionais

## 6.1. script services/parse/parse_md_ast.py

Entry point CLI para o pipeline de parse de markdown. Reduzido a 7 linhas: importa MdAstRunner de md_ast_runner.py e executa app.run().

### 6.1.1. pipeline principal

CLI actions:
- md_ast: pipeline completo (json + sqlite + views)
- md_json: apenas json
- md_sqlite: apenas sqlite upsert + views

| metodo / classe                           | Input esperado       | responsabilidade             | Output gerado                                               |
| ----------------------------------------- | -------------------- | ---------------------------- | ----------------------------------------------------------- |
| MdAstRunner.run                           | Nenhum               | Orquestrar pipeline completo | Pipeline executado conforme action CLI                      |
| ReadInputFiles.scan (md_ast_io)           | paths CLI            | Varrer e filtrar .md         | List[Path] de markdown                                      |
| GenerateAst.parse_file (md_ast_parser)    | Path .md + ast_model | Tokenizar e extrair AST      | Dict com project_name, version, folder_path, file_path, ast |
| SaveOutputFiles.save_all (md_ast_persist) | entries + schemas    | Extrair recortes + persistir | 3 JSONs + 3 tabelas + 3 views                               |

Restricoes: schedule nao aplicavel (processamento sob demanda via CLI)

## 6.2. script services/parse/md_ast_runner.py

Classe MdAstRunner: orquestrador do pipeline de parse markdown.

### 6.2.1. load_environment - data_io

- Responsabilidade: Carregar variaveis de ambiente e expor paths
- Input: Nenhum (le de env_loader + config_io)
- Transformacao: Invoca painel_settings (shim) para acessar PAINEL_ROOT, DB_PARSE_MD, SOURCE_MD
- Output: Atributos da instancia populados
- Restricoes: Deve ser chamado antes de qualquer operacao que dependa de paths

### 6.2.2. dispatch - workflow

- Responsabilidade: Rotear para o pipeline conforme action
- Input: action: str, args: Namespace
- Transformacao: Instancia ReadInputFiles, GenerateAst, SaveOutputFiles e coordena fluxo
- Output: Execucao do pipeline conforme action (md_ast, md_json, md_sqlite)

## 6.3. script services/parse/md_ast_parser.py

Classe GenerateAst: parser de markdown para AST hierarquica.

### 6.3.1. parse_file - workflow

- Responsabilidade: Tokenizar arquivo .md e extrair AST
- Input: md_path: Path, ast_model: dict
- Transformacao: markdown-it-py (preset js-default) tokeniza lista flat; _tokens_to_ast converte em arvore com heading_ctx propagation
- Output: dict com AST completa (type, children, start_line, end_line, h1-h6 context)

### 6.3.2. _tokens_to_ast - data_transform

- Responsabilidade: Converter token list flat em arvore hierarquica
- Input: tokens: list, ast_model: dict
- Transformacao: nesting=1 cria container, nesting=0 no atomico; heading_ctx tracking h1-h4 propagado via attach_heading_ctx; close_type resolvido via MD_TYPE_MAP
- Output: dict AST com nos contendo h1..h4 do heading ancestral

## 6.4. script utils/io_utils/md_ast_io.py

Classe ReadInputFiles: leitura e varredura de arquivos markdown.

### 6.4.1. scan - data_io

- Responsabilidade: Varrer paths e retornar lista de arquivos .md
- Input: paths: List[str], source_config: dict
- Transformacao: Usa parse_utils.get_files_from_paths para filtrar por extensao
- Output: List[Path] de arquivos markdown
- Restricoes: Paths inexistentes sao ignorados

## 6.5. script utils/io_utils/md_ast_persistence.py

Classe SaveOutputFiles: persistencia de AST markdown em JSON e SQLite.

### 6.5.1. save_json - data_io

- Responsabilidade: Salvar recorte AST em arquivo JSON
- Input: data: list, suffix: str, entry: dict, output_dir: str
- Transformacao: Sanitiza timestamp para nome; extrai child_path e file_name; serializa lista flat
- Output: Arquivo {timestamp}_{child_path}^{file_name}.{suffix}.json

### 6.5.2. save_sqlite - data_io

- Responsabilidade: Persistir recorte AST em tabela SQLite (upsert por file_path)
- Input: data: list, table_name: str, entry: dict, db_path: str
- Transformacao: Cria tabela se nao existe; converte para json_data (array JSON); upsert

### 6.5.3. create_views - workflow

- Responsabilidade: Recriar views SQLite a partir dos scripts .sql
- Input: db_path: str
- Transformacao: Varre diretorio sql_sqlite/sql_parse_md/; executa cada vw_*.sql
- Restricoes: Chamado automaticamente ao final de save_all

## 6.6. script services/parse/parse_script_raw.py

Parseia script raw para extrair linhas, comentarios e tags. Faz export para CSV, JSON e SQLite.

## 6.7. script services/parse/parse_script_dart_ast.py

Processa AST de codigo Dart via subprocess (Dart analyzer). Gera JSON, persiste no SQLite, exporta dados estruturados.

## 6.8. script services/logs/logs_dart.py

Aplica logs automaticamente em codigo Dart: le config de logs_string.json, substitui placeholders, injeta logger.* no codigo fonte.

### 6.8.1. pipeline principal

- Input: config logs_string.json + codigo Dart fonte
- Processo: Le mapeamento de logs, encontra placeholders no codigo, substitui por chamadas logger.*
- Output: Codigo Dart modificado com logs injetados
- Restricoes: Preserva estrutura original do codigo; nao remove logs existentes

## 6.9. script utils/io_utils/painel_sqlite_import.py

Importa dados para SQLite: upsert de AST, triggers, TagMap, LogsString.

### 6.9.1. upsert_sqlite - data_io

- Responsabilidade: Inserir ou atualizar dados no SQLite
- Input: db_path, table_name, dados
- Transformacao: Cria tabela se nao existe; upsert por chave (file_path ou equivalente)
- Output: Linhas inseridas/atualizadas

### 6.9.2. sqlite_triggers - workflow

- Responsabilidade: Executar gatilhos SQL (criacao de views, triggers)
- Input: db_path, action
- Transformacao: Le scripts SQL de sql_sqlite/ e executa contra o banco

## 6.10. script sql_sqlite/

27 scripts SQL distribuidos em 3 subdiretorios:

sql_parse_script/:
- ddl_tb_ast.sql: DDL da tabela tb_ast
- tb_ast.sql, tb_ast_func.sql, tb_ast_func_map_1d.sql, tb_ast_func_map_2d.sql: DDL de tabelas de AST
- tb_controle_ast.sql: tabela de controle
- trg_vw_ast.sql, trg_vw_ast_func.sql, trg_vw_ast_func_map_1d.sql, trg_vw_ast_func_map_2d.sql: triggers de view
- vw_*.sql: 7 views (ast_func, ast_group, data_flow_flat_mu, raw_ast, raw_flat_01, raw_flat_02, widget)
- migrate_tb_ast_line_int.sql: migracao de schema

sql_parse_md/:
- vw_md_doc.sql, vw_md_ast_code.sql, vw_md_ast_tables.sql: views do banco parse_md.db

.sql_tkinter/:
- vw_func_tag_map.sql, vw_tag_map.sql: views de controle de tags

## 6.11. script services/dart_tools/parse_dart_ast.dart

Analisador de AST Dart usando package:analyzer. Conta classes, funcoes, variaveis e exporta JSON.

### 6.11.1. pipeline principal

- Input: caminho de projeto Dart/Flutter
- Processo: AstCounterVisitor percorre a AST, conta declaracoes (classes, funcoes, variaveis, getters, setters, enums, mixins)
- Output: JSON com contagens e estrutura do projeto
- Restricoes: Requer package:analyzer; execucao via dart run

## 6.12. script controllers/parse_controller.py

Controlador que orquestra o pipeline de parse markdown via config_io e MdAstRunner.

## 6.13. script controllers/session_controller.py

Classe SessionManager: gerenciamento de sessoes em memoria.

### 6.13.1. SessionManager - coordenacao

- Responsabilidade: Gerenciar sessoes de trabalho em memoria
- Metodos: start_session, end_session, list_sessions, clear
- Input: nome da sessao
- Output: session_id (string)

## 6.14. script controllers/sync_controller.py

Controlador de sincronia entre formatos de dados.

- sync_json_to_sqlite(source_type): JSON -> SQLite (dart ou md)
- sync_triggers(action): executa gatilhos SQL

## 6.15. script repositories/config_repo.py

Repositorio de config: le JSONs de pipeline paths, actions data paths e menu.

- get_pipeline_paths(): dict de paths do pipeline
- get_actions_data_paths(): dict de paths por acao
- get_menu(): dict de definicoes do menu

## 6.16. script repositories/ast_repo.py

Repositorio de AST: operacoes de persistencia e leitura.

- save_json_ast(data, output_dir, filename): salva AST em JSON
- load_json_ast(file_path): carrega AST de JSON
- save_sqlite_ast(data, db_path, table_name): persiste AST no SQLite

## 6.17. script view_shell/painel_controle.ps1

Script principal do painel. Bootstrap, menu loop e dispatch de acoes.

### 6.17.1. pipeline principal

- Input: parametros opcionais Aba e Choice
- Processo:
  1. Carrega .env.base via env_loader
  2. Carrega set_painel_menu.json via config_io
  3. Exibe menu via Show-Menu (painel_view.ps1)
  4. Dispara comando selecionado via Run-ShellCommand
  5. Registra sessoes de execucao
- Output: Comando shell executado conforme acao selecionada
- Restricoes: Depende de env_loader, config_io, painel_view.ps1

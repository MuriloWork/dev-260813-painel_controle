# 1. Sobre este documento

## 1.1. resumo
SRD (Software Requirements Document, ou Documento de Requisitos do Produto), documento nº 2 da familia de documentos de projeto [PRD, SRD, session_code_blocks, code_scripts, plan, plan_control].
O SRD define as especificações detalhadas para o desenvolvimento do projeto, sob a ótica funcional, suas responsabilidades, lógicas e modelos de funções e de dados. As especificações do SRD terão os nomes de todos os [code_scripts, classes, metodos] com descrições em linguagem natural das responsabilidades e logicas, ficando a cargo do documento session_code_blocks (blocos de codigo em documento markdown) especificar explicitamente os algoritmos de cada [classe, metodo] em snippets de codigo.

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

Estilos de **formatação** dos headings das seções
- sempre usar: numeração sequencial, template `{N.N.N.N.N.N.}`, exemplo `###### 1.1.1.1.1.1. titulo`
- nunca usar: [h1 para titulo do documento, thematicBreak, code blocks]

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
**Conceitos base**:
- Arquitetura em layers [frontend, backend, dados]
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

Sobre os **caminhos relativos** de [pastas, scripts]:
- usar `target_folder` como base_path

Sobre o **template** da seção
- uma seção h2 para cada layer [frontend, backend, dados], template `layer {layer_name}` 
- em cada seção h2 uma subseção h3 para cada pasta principal (filha direta de target_folder), template `pasta {caminho_relativo_da_pasta}`
- em cada subseção "pasta" uma tabela dos arquivos da pasta e subpastas, template:
| pasta         | arquivo     | descricao                    |
| ------------- | ----------- | ---------------------------- |
| {folder_path} | {file_name} | {descricao breve do arquivo} |

Estilos de **formatação** da seção
- sempre usar: [texto simples, tabelas]
- nunca usar: [thematicBreak, listas não ordenadas, listas ordenadas, code blocks, backtick blocks]

### 1.2.4. sobre a seção "arquitetura de funções"
Funções de negocio do projeto, transversais aos layers, suficientemente detalhadas para atingir os objetivos do projeto.

Sobre o **template** da seção
- 4 seções h2: [resumo, pipeline, function type automatic, function type agent]
  - resumo: tipos e grupos de função de negocio
  - pipeline: lista não ordenada dos pipelines do projeto, template `[function_type] {function_name}`
    - function_name: relacionado aos tipos de [input, processamento, output] da função de negocio, exemplos:
      - parse_md: parsing de documentos markdown
      - parse_code: parsing de code scripts
      - lint_code: lint tools
- opcional (ver regra baixo): para as seções [function type automatic, function type agent] uma subseção h3 para cada grupo de função do pipeline, template `function group {function_group_name}`
- regra para identificação de grupos de funções de negocio: a partir de 3 funções com tipos de [input, processamento, output] similares criar grupo
- para cada seção h2 (ou h3=grupo) uma tabela das funções existentes ou priorizadas, template:

| funcao          | arquivos principais                                    | descricao                                  |
| --------------- | ------------------------------------------------------ | ------------------------------------------ |
| {function_name} | {lista dos code scripts mais relevantes}               | {{responsabilidades principais da função}} |
| {function_name} | {lista das instruções [agent, skills] mais relevantes} | {{responsabilidades principais da função}} |

Estilos de **formatação** da seção
- sempre usar: [texto simples, listas não ordenadas, tabelas]
- nunca usar: [thematicBreak, listas ordenadas, code blocks, backtick blocks]

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
Continuação e detalhamento das seções [arquitetura do projeto, arquitetura de dados], separadamente das seções iniciais para cobrir a necessidade de avanços parciais do detalhamento para implantação. Então nem todos os arquivos da arquitetura do projeto estarão detalhados, mas apenas os [já implantados, priorizados para implantação]. É importante seguir o template, pois essa seção também será extraida por parse da AST markdown.

Distinção de conteúdo da seção "arquitetura de dados" em relação aos dados do projeto:
- seção "arquitetura de dados": apenas os modelos [tabelas, campos, tipos, constraints], com formatação em tabelas
- seção "descrições funcionais": os scripts [ps1, python, dart, sql] de transformação de dados, com formatação em tabelas

Sobre os **caminhos relativos** de [pastas, scripts]:
- usar `target_folder` como base_path

Sobre o **template** da seção
- uma subseção h2 para cada [pasta, subpasta] do projeto, template `pasta {caminho_relativo_da_pasta}`
- em cada seção h2 uma subseção h3 para cada arquivo existente ou priorizado para detalhamento, template `arquivo {file_name}`
- em cada seção h3 uma subseção h4 para cada classe existente ou priorizada para detalhamento, template `classe {class_name}`
- em cada subseção "classe" uma tabela dos metodos existentes ou priorizados, template:
| metodo        | assinatura           | descricao                                     |
| ------------- | -------------------- | --------------------------------------------- |
| {method_name} | {method_declaration} | {{input, transformações, output, restrições}} |


Estilos de **formatação** da seção
- sempre usar: [texto simples, tabelas]
- usar moderadamente: [listas não ordenadas, listas ordenadas, backtick blocks]
- nunca usar: [thematicBreak, code blocks]

- legenda: status implementação  
  - 🟢 finalizado  
  - 🔵 funcionando, falta organizar e testar consistencia  
  - 🟤 implementação script iniciada  
  - 🟡 code blocks definidos e revisados  
  - 🟠 descrição funcional definida e revisada  
  - ⚪️ descrição funcional não iniciada ou parcial  

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

| camada   | pastas                                                                | comentario                                                                 |
| -------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| frontend | {dev/src: view_shell}                                                 | existente                                                                  |
| backend  | {dev/src: [controllers, repositories, services, utils]}               | existente                                                                  |
| backend  | {dev/src/models: validation}                                          | validação de schemas e dados                                               |
| backend  | {dev/src: tests}                                                      | testes de lógica, espelha src/                                             |
| dados    | {dev/dataMu: [data_docs, dbMu]; dev/src:[config, models, sql_sqlite]} | existentes                                                                 |
| agents   | {dev/agents: {agent_name}/skills}                                     | fora do padrao opencode de detecção automatica                             |
| docs     | {dev/docs: [docs, spec]}                                              | docs=especificações já implementadas; spec=especificações para implementar |
| temp     | {dev/temp: {git_branch_name}}                                         | POC (Proof Of Concept) alinhadas com branches existentes, uso eventual     |

## 3.1. layer frontend

### 3.1.1. pasta src/view_shell/

Scripts de interface com usuario.

| pasta           | arquivo             | descricao                                 |
| --------------- | ------------------- | ----------------------------------------- |
| src/view_shell/ | painel_controle.ps1 | bootstrap, menu loop, dispatch de acoes   |
| src/view_shell/ | painel_view.ps1     | funcao Show-Menu (extraida do controle)   |
| src/view_shell/ | painel_controle.bat | launcher batch para abrir PS1 no terminal |

## 3.2. layer backend

Subdividida em controllers (orquestracao), services (logica de negocios), utils (utilitarios), repositories (acesso a dados), models (schemas) e config (configuracoes estaticas).

### 3.2.1. pasta src/controllers/

| pasta            | arquivo               | descricao                             |
| ---------------- | --------------------- | ------------------------------------- |
| src/controllers/ | parse_controller.py   | orquestracao do pipeline de parse md  |
| src/controllers/ | session_controller.py | gerenciamento de sessoes em memoria   |
| src/controllers/ | sync_controller.py    | orquestracao de sincronia json-sqlite |

### 3.2.2. pasta src/services/

| pasta                    | arquivo                   | descricao                                           |
| ------------------------ | ------------------------- | --------------------------------------------------- |
| src/services/parse/      | parse_md_ast.py           | entry point CLI para parse de markdown              |
| src/services/parse/      | md_ast_runner.py          | orquestrador do pipeline md_ast (load, dispatch)    |
| src/services/parse/      | md_ast_parser.py          | gera AST de markdown usando markdown-it-py          |
| src/services/parse/      | parse_script_raw.py       | extrai linhas, comentarios e tags de scripts        |
| src/services/parse/      | parse_script_dart_ast.py  | processa AST de codigo Dart via subprocess analyzer |
| src/services/logs/       | logs_dart.py              | aplica logs automaticamente em codigo Dart          |
| src/services/logs/       | analyze_logs.py           | baixa e analisa logs do emulador Android via ADB    |
| src/services/dart_tools/ | parse_dart_ast.dart       | analisa AST de projetos Dart/Flutter localmente     |
| src/services/dart_tools/ | validate_schema.dart      | valida schemas no Supabase via API REST             |
| src/services/dart_tools/ | list_exposed_schemas.dart | lista schemas expostos na API REST do Supabase      |

### 3.2.3. pasta src/utils/

| pasta                  | arquivo                 | descricao                                                     |
| ---------------------- | ----------------------- | ------------------------------------------------------------- |
| src/utils/init_utils/  | env_loader.py           | carrega variaveis de ambiente e paths do projeto              |
| src/utils/init_utils/  | painel_settings.py      | shim compat __getattr__ delegando para env_loader e config_io |
| src/utils/parse_utils/ | path_resolver.py        | resolve paths relativos contra PAINEL_ROOT                    |
| src/utils/parse_utils/ | string_utils.py         | coleta texto de nos AST recursivamente (collect_text)         |
| src/utils/io_utils/    | config_io.py            | carrega e expoe configuracoes dos JSONs do projeto            |
| src/utils/io_utils/    | parse_utils.py          | utilitarios de io: filtra arquivos por extensao/glob          |
| src/utils/io_utils/    | parse_export.py         | exporta dados para CSV e models Pydantic do SQLite            |
| src/utils/io_utils/    | painel_sqlite_import.py | importa dados para SQLite (upsert, triggers)                  |
| src/utils/io_utils/    | painel_sqlite_export.py | exporta dados do SQLite para JSON estruturado                 |
| src/utils/io_utils/    | md_ast_io.py            | le arquivos markdown do disco (ReadInputFiles)                |
| src/utils/io_utils/    | md_ast_persistence.py   | persiste AST markdown em JSON e SQLite (SaveOutputFiles)      |

### 3.2.4. pasta src/repositories/

| pasta             | arquivo        | descricao                                 |
| ----------------- | -------------- | ----------------------------------------- |
| src/repositories/ | config_repo.py | le config JSONs (pipeline, actions, menu) |
| src/repositories/ | ast_repo.py    | persiste e carrega AST (json, sqlite)     |

### 3.2.5. pasta src/models/

| pasta       | arquivo             | descricao                                    |
| ----------- | ------------------- | -------------------------------------------- |
| src/models/ | ast_dart_model.py   | modelos Pydantic para AST Dart               |
| src/models/ | ast_md_model.py     | modelos Pydantic para AST Markdown           |
| src/models/ | export_model.py     | modelos para exportacao (funcoes, variaveis) |
| src/models/ | import_model.py     | modelos para importacao (tag_map, logs)      |
| src/models/ | raw_script_model.py | modelos para script raw                      |

## 3.3. layer dados

### 3.3.1. pasta src/dataMu/

| pasta                                  | arquivo              | descricao                                                            |
| -------------------------------------- | -------------------- | -------------------------------------------------------------------- |
| src/dataMu/dbMu/sqlite/                | parse_dart.db        | banco de dados de AST de codigo Dart                                 |
| src/dataMu/dbMu/sqlite/                | parse_md.db          | banco de dados de AST de markdown                                    |
| src/dataMu/data_docs/data_docs_painel/ |                      | JSONs de saida dos parsers (json_md_ast, json_script_dart_ast, etc.) |

### 3.3.2. pasta src/config/

| pasta                   | arquivo                            | descricao                        |
| ----------------------- | ---------------------------------- | -------------------------------- |
| src/config/             | set_painel_pipeline_paths.json     | configuracao (pipeline, actions) |
| src/config/             | set_painel_actions_data_paths.json | configuracao (actions)           |
| src/config/             | set_painel_menu.json               | configuracao (painel view_shell) |
| src/config/credentials/ | client_secret.json                 | configuracao (credentials)       |
| src/config/credentials/ | google_oauth_tokens.json           | configuracao (credentials)       |
| src/config/credentials/ | service_account.json               | configuracao (credentials)       |

### 3.3.3. pasta src/sql_sqlite/

| pasta                                  | arquivo              | descricao                                                            |
| -------------------------------------- | -------------------- | -------------------------------------------------------------------- |
| src/sql_sqlite/.sql_tkinter/           |                      | pasta em desuso temporario                                           |
| src/sql_sqlite/sql_parse_md/           | vw_md_ast_code.sql   | cria view vw_md_ast_code no banco parse_md.db                        |
| src/sql_sqlite/sql_parse_md/           | vw_md_ast_tables.sql | cria view vw_md_ast_tables no banco parse_md.db                      |
| src/sql_sqlite/sql_parse_md/           | vw_md_doc.sql        | cria view vw_md_doc no banco parse_md.db                             |
| src/sql_sqlite/sql_parse_script/       |                      | scripts SQL de DDL, views e triggers (19 arquivos)                   |

# 4. arquitetura de funções

## 4.1. resumo

Resumo organizado por seções do painel de controle, tipos e grupos de funcao.

Tipos de funcao:
- automatic: criacao de markdown, extracao de AST markdown
- session: edicao de markdown e code scripts em sessoes interativas
- agent: edicao e revisao de markdown e code scripts com base em instrucoes padronizadas

Exemplos de funcoes por secao do painel, detalhadas nas seções "function type *":
- seções do painel controle
  - shell
    - funções existentes (manter)
    - {function_type: automatic; function_group: bootstrap}: reload_env
    - sync (nova feature, fora do escopo deste projeto)
  - section parse ⟶ `markdown`
    - {function_type: automatic; function_group: edit_md}: update_md [AGENTS, PRD, SRD]
    - {function_type: automatic; function_group: parse}: parse_md [SRD]
    - {function_type: automatic; function_group: cross_reference}: cross_reference_spec
  - section parse ⟶ `code`
    - {function_type: automatic; function_group: parse}: parse_code [code-review-graph, tree-sitter-variables]
    - {function_type: automatic; function_group: lint}: lint_code
    - {function_type: automatic; function_group: cross_reference}: cross_reference_code
    - logs (neste projeto será apenas movida, mas não melhorada)
  - section `sessions`
  	- {function_type: agent; function_group: session_loop}
    	- spec-review
      - code-script-edit
      - code-script-review
      - code-script-edit-comments
      - rule-edit

## 4.2. pipeline [function type]

Pipeline organizado por tipo de funcao [automatic, agent] que opera sobre dados fonte [markdown, code scripts].

O pipeline principal e uma combinacao das funcoes abaixo, algumas em loop:

- [automatic] update PRD: [PRD_00, template_PRD] -> PRD_01
- [automatic] update AGENTS.md: [AGENTS, PRD_01] -> AGENTS.md
- [session] update PRD
- [automatic] create SRD: [PRD_02, template_SRD] -> SRD_00
- loop update SRD
  - [session] update SRD
  - [automatic] parse [PRD, SRD] -> [json, sqlite]
  - [automatic] cross_reference spec vs code -> gaps_report.md
  - [agent] review SRD -> review_srd_{version}.md
- [session] update tables [naming_rules, variables_rules, data_object_rules, orchestrator_rules]
- [agent] create session_code_blocks
- loop update session_code_blocks
  - [automatic] parse [SRD, session_code_blocks] -> [json, sqlite]
  - [agent] review session_code_blocks -> review_code_blocks_{version}.md
  - [session] update session_code_blocks
- [agent] create code_scripts
- loop update code_scripts
  - [automatic] parse code_scripts -> [json, sqlite]
  - [automatic] cross_reference spec vs code -> gaps_report.md
  - [automatic] lint code_scripts -> violations.json
  - [agent] review code_scripts -> review_code_scripts_{version}.md
  - [session] update [SRD, session_code_blocks, code_scripts]
- loop update [SRD, session_code_blocks, code_scripts]
  - [automatic] parse [SRD, session_code_blocks, code_scripts] -> [json, sqlite]
  - [automatic] cross_reference spec vs code -> gaps_report.md
  - [automatic] lint code_scripts -> violations.json
  - [agent] review [SRD, session_code_blocks, code_scripts] -> consolidated review
  - [session] update [SRD, session_code_blocks, code_scripts]
  - [session] update tables

## 4.3. function type automatic

### 4.3.1. function group bootstrap

| Funcao              | arquivos principais                                                                     | Descricao                                                                |
| ------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| general_bootstrap   | env_loader, painel_settings, path_resolver, config_io, config_repo, painel_controle.ps1 | nova versao: Carrega ambiente, paths e configuracoes do projeto          |
| base_config_load    | env_loader, painel_settings, path_resolver, config_io, config_repo, painel_controle.ps1 | nova feature: Carrega ambiente, paths e configuracoes basicas do projeto |
| session_config_load | env_loader, painel_settings, path_resolver, config_io, config_repo, painel_controle.ps1 | nova feature: carrega configuracoes da sessao                            |

### 4.3.2. function group edit_md

| Funcao    | arquivos principais | Descricao                               |
| --------- | ------------------- | --------------------------------------- |
| create_md | a definir           | AGENTS.md, PRD_{version}, SRD_{version} |
| update_md | a definir           | AGENTS.md, PRD_{version}, SRD_{version} |

### 4.3.3. function group parse

| Funcao                | arquivos principais                                                                     | Descricao                                                              |
| --------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| parse_md              | md_ast_runner, md_ast_parser, md_ast_io, md_ast_persistence, string_utils               | Extrai AST de markdown [PRD, SRD, session_code_blocks] -> json, sqlite |
| vw_md_doc             | parse_md.db, md_ast_parser.py                                                           | view ast markdown blocks                                               |
| vw_md_ast_tables      | parse_md.db, md_ast_parser.py                                                           | view ast markdown tables                                               |
| vw_md_ast_code        | parse_md.db, md_ast_parser.py                                                           | view ast markdown code blocks                                          |
| parse_code            | parse_script_raw, parse_script_dart_ast, parse_dart_ast.dart, parse_utils, parse_export | Extrai AST de code scripts [ps1, python, dart] -> json, sqlite         |
| vw_flow_steps         | code_review.db, a definir                                                               | view code-review-graph                                                 |
| vw_call_graph         | code_review.db, a definir                                                               | view code-review-graph                                                 |
| vw_communities_detail | code_review.db, a definir                                                               | view code-review-graph                                                 |

### 4.3.4. function group cross_reference

| Funcao                        | arquivos principais | Descricao                                                              |
| ----------------------------- | ------------------- | ---------------------------------------------------------------------- |
| cross_reference_spec          |                     | Compara spec docs via SQLite gaps [missing, extra, mismatch]           |
| cross_reference_spec_versions |                     | Compara versoes via SQLite gaps [missing, extra, mismatch]             |
| cross_reference_code          | parse_controller    | Compara SQLite spec vs SQLite code -> gaps [missing, extra, mismatch]  |
| cross_reference_code_versions | parse_controller    | Compara versoes git via SQLite code -> gaps [missing, extra, mismatch] |

### 4.3.5. function group lint

| Funcao             | arquivos principais                                                                               | Descricao                                                                                                                    |
| ------------------ | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| lint_code_standard | import-linter, pylint, mypy, radon, pep8-naming, vulture, isort, eradicate, architecture_enforcer | Ferramentas de lint em sequencia -> violations.json (mais detalhes em [analise_lint_tools](260617_analise_lint_tools_00.md)) |
| lint_code_custom   | a definir                                                                                         | Lints personalizados (mais detalhes em [analise_lint_tools](260617_analise_lint_tools_00.md))                                |

## 4.4. function type agent

### 4.4.1. function group session_loop

| Funcao                         | Descricao                                                                          | Inputs                                             |
| ------------------------------ | ---------------------------------------------------------------------------------- | -------------------------------------------------- |
| spec-review                    | Revisa SRD, session_code_blocks -> review_srd, review_code_blocks                  | SQLite spec + code + gaps_report + violations.json |
| code-script-review             | Revisa code_scripts -> review_code_scripts                                         | SQLite code + violations.json + gaps_report        |
| code-script-edit               | Cria ou edita code_scripts a partir de session_code_blocks                         | session_code_blocks existente; SRD                 |
| code-script-edit-comments      | edição padronizada de comentarios nos codigos                                      | comments rules                                     |
| rule-edit                      | Edita tabelas naming_rules, variables_rules, data_object_rules, orchestrator_rules | Tabelas existentes em JSON; regras de formato      |
| ~~consolidated-review~~        | Revisa SRD + session_code_blocks + code_scripts em conjunto                        | Todos os SQLite, gaps e violations disponiveis     |
| ~~create session_code_blocks~~ | Cria session_code_blocks a partir de SRD + regras                                  | SRD existente; tabelas de regras; template         |
| ~~spec-edit~~                  | Edita SRD, session_code_blocks conforme regras de heading                          | Documento existente; rules de formatacao           |

# 5. arquitetura de dados

## 5.1. dados de negocio

### 5.1.1. dados fonte, armazenamento fisico

#### 5.1.1.1. fonte de dados de negocio `data_source_path`

### 5.1.2. dados transformados, armazenamento fisico

#### 5.1.2.1. documentos de dados

Diretorio dataMu/data_docs/data_docs_painel/:
- json_md_ast/: JSONs de saida do parser markdown
- json_script_dart_ast/: JSONs de saida do parser Dart AST
- json_script_dart_ast_func/: JSONs de saida de funcoes Dart
- json_script_raw/: JSONs de saida do parser raw
- json_xls/: JSONs de saida de planilhas
- logs/: arquivos de log

#### 5.1.2.2. banco de dados `src/dataMu/dbMu/sqlite/parse_md.db`

Banco SQLite em dataMu/dbMu/sqlite/parse_md.db. banco SQLite com AST de markdown (3 tabelas + 3 views).

##### 5.1.2.2.1. tabela tb_json_md_ast_blocks - blocos do documento

| campo        | tipo    | descricao                                                                                |
| ------------ | ------- | ---------------------------------------------------------------------------------------- |
| id           | INTEGER | PK autoincrement                                                                         |
| project_name | TEXT    | nome da pasta do projeto principal (ex: 260511_meta_api)                                 |
| version      | TEXT    | timestamp da sessao de extracao                                                          |
| folder_path  | TEXT    | caminho absoluto da pasta raiz da extracao                                               |
| file_path    | TEXT    | caminho relativo a pasta raiz da extracao, UNIQUE                                        |
| json_data    | TEXT    | JSON array de objetos {line, block_type, level, script, classe, metodo, content, funcao} |

##### 5.1.2.2.2. tabela tb_json_md_ast_code - blocos de codigo

| campo        | tipo    | descricao                                                                 |
| ------------ | ------- | ------------------------------------------------------------------------- |
| id           | INTEGER | PK autoincrement                                                          |
| project_name | TEXT    | nome da pasta do projeto principal                                        |
| version      | TEXT    | timestamp da sessao de extracao                                           |
| folder_path  | TEXT    | caminho absoluto da pasta raiz da extracao                                |
| file_path    | TEXT    | caminho relativo, UNIQUE                                                  |
| json_data    | TEXT    | JSON array de objetos {line, lang, script, classe, metodo, value, funcao} |

##### 5.1.2.2.3. tabela tb_json_md_ast_tables - tabelas

| campo        | tipo    | descricao                                                                                |
| ------------ | ------- | ---------------------------------------------------------------------------------------- |
| id           | INTEGER | PK autoincrement                                                                         |
| project_name | TEXT    | nome da pasta do projeto principal                                                       |
| version      | TEXT    | timestamp da sessao de extracao                                                          |
| folder_path  | TEXT    | caminho absoluto da pasta raiz da extracao                                               |
| file_path    | TEXT    | caminho relativo, UNIQUE                                                                 |
| json_data    | TEXT    | JSON array de objetos {line, row, col, cell_type, script, classe, metodo, value, funcao} |

##### 5.1.2.2.4. view vw_md_doc

Fonte: tb_json_md_ast_blocks -> json_each(json_data)

| campo saida | tipo | descricao                                               |
| ----------- | ---- | ------------------------------------------------------- |
| file_path   | TEXT | caminho relativo do arquivo de origem                   |
| line        | INT  | linha inicial do bloco (0-indexed)                      |
| block_type  | TEXT | tipo do no markdown (paragraph, heading, listItem, etc) |
| level       | INT  | profundidade do heading (NULL para nao-headings)        |
| funcao      | TEXT | extraido do bracket do h2                               |
| script      | TEXT | texto do heading h2 ancestral                           |
| classe      | TEXT | texto do heading h3 ancestral                           |
| metodo      | TEXT | texto do heading h4 ancestral                           |
| content     | TEXT | texto plano do bloco incluindo inlineCode               |

Blocos code, table e thematicBreak excluidos. ORDER BY file_path, line.

##### 5.1.2.2.5. view vw_md_ast_code

Fonte: tb_json_md_ast_code -> json_each(json_data)

| campo saida | tipo | descricao                                         |
| ----------- | ---- | ------------------------------------------------- |
| file_path   | TEXT | caminho relativo do arquivo de origem             |
| line        | INT  | linha inicial do bloco de codigo (0-indexed)      |
| lang        | TEXT | linguagem do code fence; '(sem tag)' quando vazio |
| funcao      | TEXT | extraido do bracket do h2                         |
| script      | TEXT | texto do heading h2 ancestral                     |
| classe      | TEXT | texto do heading h3 ancestral                     |
| metodo      | TEXT | texto do heading h4 ancestral                     |
| value       | TEXT | conteudo integral do bloco de codigo              |

ORDER BY file_path, line.

##### 5.1.2.2.6. view vw_md_ast_tables

Fonte: tb_json_md_ast_tables -> json_each(json_data), transpose

| campo saida    | tipo | descricao                                                |
| -------------- | ---- | -------------------------------------------------------- |
| file_path      | TEXT | caminho relativo do arquivo de origem                    |
| section_01..06 | TEXT | headings ancestrais h1-h6                                |
| line           | INT  | linha inicial da tabela (0-indexed)                      |
| funcao         | TEXT | extraido do bracket do h2                                |
| script         | TEXT | extraido da section_N com conteudo script                |
| tag_classe     | TEXT | extraido entre [ e ] da section_N com conteudo classe    |
| classe         | TEXT | extraido entre classe [ da section_N com conteudo classe |
| row            | INT  | indice da linha na tabela (0-indexed)                    |
| col_01..03     | TEXT | transpose de col+value (col_01 = nome do metodo)         |

ORDER BY file_path, section_01..06, line, row.

#### 5.1.2.3. banco de dados `src/dataMu/dbMu/sqlite/parse_dart.db`

Banco SQLite em dataMu/dbMu/sqlite/parse_dart.db. Contem tabelas de AST de codigo Dart.

##### 5.1.2.3.1. tabela tb_ast

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

##### 5.1.2.3.2. tabela tb_ast_func, tb_ast_func_map_1d, tb_ast_func_map_2d, tb_controle_ast

Tabelas derivadas de funcoes, mapas de acoplamento e controle de versao das extracoes.

##### 5.1.2.3.3. views do banco parse_dart.db

Views em sql_sqlite/sql_parse_script/: vw_ast_func, vw_ast_group, vw_data_flow_flat_mu, vw_raw_ast, vw_raw_flat_01, vw_raw_flat_02, vw_widget.
Views de controle: vw_func_tag_map, vw_tag_map.

### 5.1.3. dados transformados, armazenamento temporario no run time
variaveis de ambiente

### 5.1.4. modelos para code scripts

#### 5.1.4.1. schemas de extracao/importacao

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

#### 5.1.4.2. schemas internos para transformacoes intermediarias

Nao aplicavel: nao ha transformacoes intermediarias entre schemas no pipeline atual.

#### 5.1.4.3. schemas de exportacao

Tres schemas declarativos (json_schema_blocks, json_schema_code, json_schema_tables) aplicados ao AST para gerar JSONs de saida e tabelas SQLite:

json_schema_blocks:
- file_path, line, block_type, level, script, classe, metodo, content, funcao
- Fonte: entry e ast.node, com heading_ctx tracking para funcao(h2)/script/h3/classe/h4/metodo

json_schema_code:
- file_path, line, lang, script, classe, metodo, value, funcao
- Conteudo integral do bloco de codigo

json_schema_tables:
- file_path, line, row, col, cell_type, script, classe, metodo, value, funcao
- Transpose de celulas para linhas individuais

## 5.2. dados de controle

### 5.2.1. auth

Arquivos em config/credentials/: service_account.json, google_oauth_tokens.json, client_secret.json

### 5.2.2. config (estatico)

Diretorio config/:
- set_painel_pipeline_paths.json: paths do pipeline (db, source, target)
- set_painel_menu.json: definicoes de abas e comandos do menu
- set_painel_actions_data_paths.json: paths de dados por acao
- credentials/: service_account.json, google_oauth_tokens.json, client_secret.json

### 5.2.3. actions (dinamico)

config/set_painel_actions_data_paths.json

### 5.2.4. state

Gerenciado em memoria por env_loader.py (PAINEL_ROOT, PAINEL_SRC_DIR, etc.) e SessionManager (session_controller.py).

# 6. descricoes funcionais

## 6.1. divisao de responsabilidades

- Bootstrap e menu: painel_controle.ps1 + painel_view.ps1 + env_loader + config_io + config_repo
- Parse de markdown: md_ast_runner, md_ast_parser, md_ast_io, md_ast_persistence, string_utils
- Parse de code scripts: parse_script_raw, parse_script_dart_ast, parse_dart_ast.dart, parse_utils, parse_export
- Persistencia: ast_repo, painel_sqlite_import, painel_sqlite_export
- Logs: logs_dart, analyze_logs
- Ferramentas Dart: parse_dart_ast.dart, validate_schema.dart, list_exposed_schemas.dart
- Orquestracao: parse_controller, session_controller, sync_controller
- SQL views: scripts em sql_sqlite/ (27 arquivos de DDL, triggers e views)

## 6.2. scripts parse_md

### 6.2.1. script src/services/parse/parse_md_ast.py [parse_md]

Entry point CLI para o pipeline de parse de markdown. Importa MdAstRunner de md_ast_runner.py e executa app.run().

CLI actions: md_ast (completo), md_json (apenas json), md_sqlite (apenas sqlite + views)

### 6.2.2. script src/services/parse/md_ast_runner.py [parse_md]

classe MdAstRunner [coordenacao]

| Metodo           | Assinatura             | Descricao                                         |
| ---------------- | ---------------------- | ------------------------------------------------- |
| load_environment | load_environment()     | Carrega env vars via painel_settings, expoe paths |
| dispatch         | dispatch(action, args) | Roteia para pipeline conforme action              |

### 6.2.3. script src/services/parse/md_ast_parser.py [parse_md]

classe GenerateAst [transformacao]

| Metodo         | Assinatura                                                 | Descricao                                                           |
| -------------- | ---------------------------------------------------------- | ------------------------------------------------------------------- |
| parse_file     | parse_file(md_path, ast_model)                             | Tokeniza .md com markdown-it-py, extrai AST hierarquica             |
| _tokens_to_ast | _tokens_to_ast(tokens, ast_model)                          | Converte token list flat em arvore com heading_ctx (h1-h6 + funcao) |
| build_entry    | build_entry(md_path, ast, project_name, version, root_dir) | Monta dict padronizado para schemas de extracao                     |

### 6.2.4. script src/utils/io_utils/md_ast_io.py [parse_md]

classe ReadInputFiles [extracao]

| Metodo | Assinatura                 | Descricao                                   |
| ------ | -------------------------- | ------------------------------------------- |
| scan   | scan(paths, source_config) | Varre paths e retorna lista de arquivos .md |

### 6.2.5. script src/utils/io_utils/md_ast_persistence.py [parse_md]

classe SaveOutputFiles [exportacao]

| Metodo       | Assinatura                                      | Descricao                                         |
| ------------ | ----------------------------------------------- | ------------------------------------------------- |
| save_json    | save_json(data, suffix, entry, output_dir)      | Salva recorte AST em JSON                         |
| save_sqlite  | save_sqlite(data, table_name, entry, db_path)   | Persiste recorte em SQLite (upsert)               |
| create_views | create_views(db_path)                           | Recria views SQLite a partir de scripts .sql      |
| save_all     | save_all(entries, schemas, output_dir, db_path) | Orquestra extracao pelos 3 schemas + persistencia |

### 6.2.6. script src/utils/parse_utils/string_utils.py [parse_md]

Funcao collect_text: coleta texto de nos AST recursivamente (heading, paragraph, inlineCode, etc.)

## 6.3. scripts parse_code

### 6.3.1. script src/services/parse/parse_script_raw.py [parse_code]

Parseia script raw para extrair linhas, comentarios e tags. Exporta para CSV, JSON e SQLite.

### 6.3.2. script src/services/parse/parse_script_dart_ast.py [parse_code]

Processa AST de codigo Dart via subprocess (Dart analyzer). Gera JSON e persiste no SQLite.

### 6.3.3. script src/services/dart_tools/parse_dart_ast.dart [parse_code]

Analisador de AST Dart usando package:analyzer. AstCounterVisitor percorre a AST, conta declaracoes (classes, funcoes, variaveis, getters, setters, enums, mixins) e exporta JSON.

### 6.3.4. script src/utils/io_utils/parse_utils.py [parse_code]

Utilitarios de IO: filtra arquivos por extensao/glob, varre diretorios, monta dict de file_info.

### 6.3.5. script src/utils/io_utils/parse_export.py [parse_code]

Exporta dados para CSV e exporta models Pydantic do SQLite.

## 6.4. scripts bootstrap

### 6.4.1. script src/view_shell/painel_controle.ps1 [bootstrap]

Script principal do painel. Bootstrap, menu loop e dispatch de acoes.

Pipeline:
1. Carrega .env.base via env_loader
2. Carrega set_painel_menu.json via config_io
3. Exibe menu via Show-Menu (painel_view.ps1)
4. Dispara comando selecionado via Run-ShellCommand
5. Registra sessoes de execucao

### 6.4.2. script src/view_shell/painel_view.ps1 [bootstrap]

Funcao Show-Menu: exibe cabecalho, lista comandos numerados, le entrada do usuario.

### 6.4.3. script src/view_shell/painel_controle.bat [bootstrap]

Launcher batch que abre o PowerShell no Windows Terminal.

### 6.4.4. script src/utils/init_utils/env_loader.py [bootstrap]

Carrega variaveis de ambiente e paths do projeto. Define PAINEL_ROOT, PAINEL_SRC_DIR, carrega .env.base, pipeline_paths.json, actions_data_paths.json.

classe/symbols:
- PAINEL_SETTINGS_DIR, ENV_PAINEL_JSON: paths absolutos
- load_environment_main(): funcao principal de bootstrap

### 6.4.5. script src/utils/init_utils/painel_settings.py [bootstrap]

Shim compat __getattr__ que delega para env_loader e config_io. Mantido para compatibilidade com imports existentes.

### 6.4.6. script src/utils/parse_utils/path_resolver.py [bootstrap]

Resolve caminhos relativos em paths absolutos a partir de PAINEL_ROOT.

### 6.4.7. script src/utils/io_utils/config_io.py [bootstrap]

Carrega e expoe configuracoes dos JSONs de pipeline paths, actions data paths e menu. Variaveis globais: DB_PARSE_DART, DB_PARSE_MD, SOURCE_DART, SOURCE_MD, TB_AST.

### 6.4.8. script src/repositories/config_repo.py [bootstrap]

classe/symbols:
- get_pipeline_paths(): le pipeline_paths.json
- get_actions_data_paths(): le actions_data_paths.json
- get_menu(): le menu.json

## 6.5. scripts cross_reference

### 6.5.1. script src/controllers/parse_controller.py [parse_md, cross_reference]

Controlador que orquestra o pipeline de parse markdown via config_io e MdAstRunner.

### 6.5.2. script src/controllers/session_controller.py [spec-edit]

classe SessionManager [coordenacao]

| Metodo        | Assinatura              | Descricao                         |
| ------------- | ----------------------- | --------------------------------- |
| start_session | start_session(name)     | Inicia sessao, retorna session_id |
| end_session   | end_session(session_id) | Encerra sessao                    |
| list_sessions | list_sessions()         | Lista sessoes ativas              |
| clear         | clear()                 | Limpa todas as sessoes            |

### 6.5.3. script src/controllers/sync_controller.py [sync]

- sync_json_to_sqlite(source_type): JSON -> SQLite (dart ou md)
- sync_triggers(action): executa gatilhos SQL

## 6.6. scripts lint_code

### 6.6.1. script src/services/logs/logs_dart.py [lint_code]

Aplica logs automaticamente em codigo Dart: le config de logs_string.json, substitui placeholders, injeta logger.* no codigo fonte.

### 6.6.2. script src/services/logs/analyze_logs.py [lint_code]

Baixa e analisa logs do emulador Android via ADB, filtra por pacote, exporta para CSV, exibe no terminal.

### 6.6.3. script src/services/dart_tools/validate_schema.dart [lint_code]

Valida schemas no Supabase via API REST.

### 6.6.4. script src/services/dart_tools/list_exposed_schemas.dart [lint_code]

Lista schemas expostos na API REST do Supabase.

## 6.7. scripts sql

### 6.7.1. script sql_sqlite/ [parse_md, parse_code]

27 scripts SQL em 3 subdiretorios:
- sql_parse_script/: DDL, views e triggers do banco parse_dart.db
- sql_parse_md/: views do banco parse_md.db (vw_md_doc, vw_md_ast_code, vw_md_ast_tables)
- .sql_tkinter/: views de controle de tags

Views requerem atualizacao para incluir coluna funcao extraida do bracket do h2.

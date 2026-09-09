
# 1. Template PRD

## 1.1. Sobre este documento

### 1.1.1. resumo
PRD (Product Requirements Document, ou Documento de Requisitos do Produto), documento nº 1 da familia de documentos de projeto [PRD, SRD, session_code_blocks, code_scripts, plano].
O PRD define as especificações desenvolvimento de alto nível do projeto, sob a ótica do negócio, suas arquiteturas e modelos de funções e de dados. As especificações do PRD sempre serão decrescentes em precisão, ou seja, mais precisas nas primeiras camadas de especificação e menos precisas nas últimas camadas, ficando a cargo do documento SRD (Software Requirements Document) aprofundar o detalhamento das especificações.

Na arquitetura de funções de negócio serão definidos [layers, folders, code scripts].

Na arquitetura de dados serão definidos [layers, folders, armazenamento, modelos]

### 1.1.2. instruções

#### 1.1.2.1. instruções gerais
Este documento é atualizado de 3 formas:
1. **manualmente** pelo usuario
2. em **sessões interativas** com agente de IA
3. **automaticamente** por code scripts, portanto é importante que o template seja respeitado, principalmente a estrutura de seções (headings) e seus titulos.

Considerar como conteúdos **não editáveis**:
- textos das seções com titulo "instruções"
- titulos das seções existentes no inicio de uma "sessão interativa", seguir os name templates definidos nas instruçoes de cada seção
- estrutura (seções, subseções, titulos) das seções [arquitetura de funções,arquitetura de dados]

Considerar como conteúdos **editáveis**:
- titulos de seções novas, criadas durante uma "sessão interativa"
- textos solicitados pelo usuario durante uma "sessão interativa" 

Estilos de **formatação** do documento
- sempre usar: [texto simples, listas não ordenadas]
- evitar, se possível: [listas ordenadas, tabelas, backtick blocks]
  - usar apenas se fizer diferença para a clareza do conteudo
- nunca usar: [thematicBreak, code blocks]

name templates, sempre usar a versao mais recente

#### 1.1.2.2. sobre a seção "contexto do projeto"
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

#### 1.1.2.3. sobre a seção "arquitetura do projeto"
estrutura de layers [frontend, backend, dados] 
pastas de cada layer
code scripts de cada pasta

#### 1.1.2.4. sobre a seção "arquitetura de funções"
continuação da arquitetura do projeto para layers [frontend, backend], sob a ótica funcional, podendo atravessar varios code scripts

legenda: status implementação  
- 🟢 finalizado  
- 🔵 funcionando, falta organizar e testar consistencia  
- 🟤 implementação script iniciada  
- 🟡 code blocks definidos e revisados  
- 🟠 descrição funcional definida e revisada  
- ⚪️ descrição funcional não iniciada ou parcial  

#### 1.1.2.5. sobre a seção "arquitetura de dados"
continuação da arquitetura do projeto para layers [data, backend], sob a ótica estrutural, podendo atravessar varios code scripts

Tipos de dados:
- dados de negocio: dados principais, ligados aos objetivos do projeto
- dados de controle 
	- auth: endereços, tokens e senhas de validação de acesso para API e serviços
	- config: configurações estáticas de operação do sistema (projeto)
	- actions: configurações dinâmicas do pipeline do sistema (projeto), definem os tipos de ações que podem ser selecionados no disparo ou durante a operação do sistema
	- state: configurações de estado do sistema ou da interface do usuario

## 1.2. contexto do projeto 

### 1.2.1. objetivos e resumo 
Exemplos:
- meta_api
	- crm para venda de produtos afiliados 
	- gerenciamento de redes sociais 
	- produção de [pesquisas, postagens, mensagens]
- painel_controle
	- automatizar meu fluxo de vibe coding 
	- uma parte com code scripts para extração e transformação de conteúdos de [documentos markdown, code scripts], outra com agentes e skills com regras para edição e revisão de [documentos markdown, code scripts]
	- a maior ênfase será em code scripts para: 
		- criação de documentos a partir de templates 
		- lint tests de mercado 
		- lint tests personalizados, utilizando tabelas auxiliares de padrões esperados no código 
	- documentos de projeto
	- documentos de sessão

### 1.2.2. stack do projeto 
Exemplo:
- ambiente/servidor: local
- UI: flutter windows, flutter web, powershell
- script languages: dart, python, ps1, sqlite
- api: 
- dados: sqlite, json 

### 1.2.3. caminhos do projeto
Exemplo:
| path type | path name      | path                                                                                                                         |
| --------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| session   | project_path   | `C:\Users\muril\OneDrive\01 mycloud\01 sistMu\10.01 scripts\01_root\main\260511_meta_api`                                    |
| session   | session_folder | `C:\Users\muril\OneDrive\01 mycloud\01 sistMu\10.01 scripts\01_root\main\260511_meta_api\sessions\260623_arquitetura_painel` |
| target    | target_folder  | `C:\Users\muril\OneDrive\01 mycloud\01 sistMu\10.01 scripts\01_root\main\260511_meta_api\dev`                                |
| ignore    | ignore_pattern | `C:\Users\muril\OneDrive\01 mycloud\01 sistMu\10.01 scripts\01_root\main\260511_meta_api\dev\.*`                             |

pastas no `ignore_pattern` não são necessarias para edição de codigo, mas deverão ser movidas conforme a nova arquitetura


### 1.2.4. templates do projeto
Exemplo:
- project_name: `C:\Users\muril\OneDrive\01 mycloud\01 sistMu\10.01 scripts\01_root\main\260511_meta_api`
- session_name: `sessions\260618_painel_controle_lint`
  - PRD (este documento): `sessions\260618_painel_controle_lint\260618_painel_controle_lint_prd_{version}.md`
  - SRD (documento base das especificações detalhadas): `sessions\260618_painel_controle_lint\260619_painel_controle_lint_srd_{version}.md`
  - plano de execução: `sessions\260618_painel_controle_lint\260618_session_plan_{version}.md` 
- documentos alvo da sessão
  - code_scripts_folder: `dev\src`
  - json_docs_folder: `dev\parse_docs`
  - sqlite_folder: `dev\dbMu`
  - markdown rules: `sessions\260618_painel_controle_lint\260618_agent_scripts_rules_{version}.md`
  - markdown templates: `sessions\260618_painel_controle_lint\260618_templates_{type}_{version}.md`

## 1.3. arquitetura do projeto 
### 1.3.1. camada frontend
#### 1.3.1.1. src/view_shell/
### 1.3.2. camada backend
#### 1.3.2.1. src/controllers/
#### 1.3.2.2. src/services/
##### 1.3.2.2.1. src/services/~~painel_settings~~painel_init.py
##### 1.3.2.2.2. src/services/parse
##### 1.3.2.2.3. src/services/logs
##### 1.3.2.2.4. src/services/dart_tools
#### 1.3.2.3. src/utils_io/
#### 1.3.2.4. src/sql_sqlite/
##### 1.3.2.4.1. src/sql_sqlite/sql_parse_md
##### 1.3.2.4.2. src/sql_sqlite/sql_tkinter
##### 1.3.2.4.3. src/sql_sqlite/sql_parse_script
#### 1.3.2.5. src/sql_supabase/
#### 1.3.2.6. src/models/
##### 1.3.2.6.1. src/models/schemas
#### 1.3.2.7. src/~~config~~ repositories/
##### 1.3.2.7.1. src/config/schemas
##### 1.3.2.7.2. src/~~utils_auth~~/auth_data*.json
#### 1.3.2.8. src/temp
### 1.3.3. camada dados
#### 1.3.3.1. dbMu/
- files
  - parse_dart.db
  - parse_md.db
#### 1.3.3.2. doc_painel/

## 1.4. arquitetura de funções 

### 1.4.1. resumo
Exemplo:
- pipeline [type, function group]
	- [automatic] create PRD: [template_PRD, rules] ⟶ PRD
	- [session] update PRD 
	- [automatic] create SRD: [template_SRD, rules] ⟶ SRD
  - loop update SRD 
    - [session] update SRD 
    - [automatic] parse [PRD, SRD] ⟶ [json, sqlite]
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
  	- [automatic] lint code_scripts ⟶ [json, sqlite] 
  	- [agent] review code_scripts ⟶ review_code_scripts_{version}.md 
  	- [session] update [SRD, session_code_blocks, code_scripts] 
  	- codigo funcionando? sim, então proximo loop
  - loop update [SRD, session_code_blocks, code_scripts] 
  	- [automatic] parse [SRD, session_code_blocks, code_scripts] ⟶ [json, sqlite] 
  	- [automatic] lint code_scripts ⟶ [json, sqlite] 
  	- [agent] review [SRD, session_code_blocks, code_scripts] ⟶ [review_srd_{version}.md, review_code_blocks_{version}.md, review_code_scripts_{version}.md] 
  	- [session] update [SRD, session_code_blocks, code_scripts] 
    - [session] update tables [naming_rules, variables_rules, data_object_rules, orchestrator_rules] 
- automatic functions (painel controle)
  - section parse 
    - parse md [PRD, SRD, session_code_blocks] ast [tables, code blocks] ⟶ [json, sqlite]
  	- parse code_scripts [ps1, python, dart] ast ⟶ [json, sqlite]  
  	- parse code_scripts [ps1, python, dart] raw ⟶ [json, sqlite] 
  - section session 
    - create PRD: [template_PRD, rules] ⟶ PRD 
    - create SRD: [template_SRD, rules] ⟶ SRD 
    - lint code_scripts [ps1, python, dart] ⟶ [json, sqlite] 
  - section sync 
    - sync json ⟷ sqlite ⟷ csv ⟷ xlsx
- session functions: interações [user, agent] via prompt, sem regras 
- agent functions 
	- spec_edit [SRD, session_code_blocks] 
	- spec_review [SRD, session_code_blocks] ⟶ [review_srd_{version}.md, review_code_blocks_{version}.md]  
	- code_script_edit [code_scripts] 
	- code_script_edit_comments [comments, tags] 
	- code_script_review [code_scripts] ⟶ review_code_scripts_{version}.md 
	- rule_edit [naming_rules, variables_rules, data_object_rules, orchestrator_rules] 

### 1.4.2. pipeline [type, function]
Exemplo:
- [==automatic==] create PRD: [template_PRD, rules] ⟶ PRD
- [session] update PRD 
- [==automatic==] create SRD: [template_SRD, rules] ⟶ SRD
- loop update SRD 
  - [session] update SRD 
  - [==automatic==] parse [PRD, SRD] ⟶ [json, sqlite]
	- [agent] review SRD ⟶ review_srd_{version}.md
- [session] update tables [naming_rules, variables_rules, data_object_rules, orchestrator_rules] 
- [agent] create session_code_blocks 
- loop update session_code_blocks  
	- [==automatic==] parse [SRD, session_code_blocks] ⟶ [json, sqlite]
	- [agent] review session_code_blocks ⟶ review_code_blocks_{version}.md 
	- [session] update session_code_blocks 
- [agent] create code_scripts 
- loop update code_scripts 
	- [==automatic==] parse code_scripts ⟶ [json, sqlite] 
	- [==automatic==] lint code_scripts ⟶ [json, sqlite] 
	- [agent] review code_scripts ⟶ review_code_scripts_{version}.md 
	- [session] update [SRD, session_code_blocks, code_scripts] 
	- codigo funcionando? sim, então proximo loop
- loop update [SRD, session_code_blocks, code_scripts] 
	- [==automatic==] parse [SRD, session_code_blocks, code_scripts] ⟶ [json, sqlite] 
	- [==automatic==] lint code_scripts ⟶ [json, sqlite] 
	- [agent] review [SRD, session_code_blocks, code_scripts] ⟶ [review_srd_{version}.md, review_code_blocks_{version}.md, review_code_scripts_{version}.md] 
	- [session] update [SRD, session_code_blocks, code_scripts] 
  - [session] update tables [naming_rules, variables_rules, data_object_rules, orchestrator_rules] 

### 1.4.3. automatic functions

#### 1.4.3.1. painel controle, section parse
Exemplo:
- parse md [PRD, SRD, session_code_blocks] ast [tables, code blocks] ⟶ [json, sqlite]
- parse code_scripts [ps1, python, dart] ast ⟶ [json, sqlite]  
- parse code_scripts [ps1, python, dart] raw ⟶ [json, sqlite] 

#### 1.4.3.2. painel controle, section session 

##### 1.4.3.2.1. create PRD 

[template_PRD, rules] ⟶ PRD 

##### 1.4.3.2.2. create SRD 
aplicar hierarquia funcional com base nos modelos de dados
[template_SRD, rules] ⟶ SRD 

##### 1.4.3.2.3. lint tools

- lint code_scripts [ps1, python, dart] ⟶ [json, sqlite] 

| tipo de violação\ tool                 | architecture_enforcer | pylint | import-linter | mypy  | radon+xenon |
| -------------------------------------- | :-------------------: | :----: | :-----------: | :---: | :---------: |
| **Nomeacao inadequada**                |                       |   x    |               |       |             |
| **Acoplamento indevido**               |           x           |        |       x       |       |             |
| **Violaçao de SRP — escopo da classe** |           x           |        |               |       |             |
| **Não uso de metodo unificado**        |           x           |        |               |       |             |
| **Duplicacao de codigo**               |                       |   x    |               |       |             |
| **Uso indevido de variaveis**          |           x           |   x    |               |       |             |
| **Uso indevido de objetos de dados**   |           x           |        |               |   x   |             |
| **Import de camada proibida**          |                       |        |       x       |       |             |
| **Complexidade / classe grande**       |                       |   x    |               |       |      x      |

#### 1.4.3.3. painel controle, section sync
Transformações entre os modelos de dados.
- sync json ⟷ sqlite ⟷ csv ⟷ xlsx

### 1.4.4. agent functions
- inteligentes
  - interpretar com base nos conteudos [texto, lista]
    - logica funcional aplicada a [seções do documento, hierarquia funcional]
    - hierarquia funcional  
    - status de implementação
  - resumir conteudos
  - verificar a aderencia dos modelos [md, json]

#### 1.4.4.1. project documents rules  

- general rules: 
	- naming 
	- versioning 
	- mirroring [md, json, toml, csv, xlsx]  
- spec docs  
- plan docs  
	- plan & control rules: tag system    
- script docs  
	- build rules
		- metodos
			- factory para boco de dados 
				- Factory: recebe parâmetros tipados nomeados e cria um Map novo — assetsEntry(fileName: x, timestamp: y) => {'fileName': x, 'timestamp': y}.
			- transformador para alimentar o bloco 
				- Transformador: recebe um Map pronto, extrai com casts, transforma em outro Map — _toConfigMap(entry) { final x = entry['fileName'] as String; ... return {...} }.
	- review rules: spec, quality  


## 1.5. arquitetura de dados

### 1.5.1. dados de negocio 

#### 1.5.1.1. dados fonte, armazenamento fisico
{conteudo obrigatorio, conforme o escopo do projeto}

##### 1.5.1.1.1. fonte de dados de negocio `data_source_path`
**Data source name template**: para o caso de documentos com name template

{tabela, se aplicavel}
| campo        | tipo    | descrição                              |
| ------------ | ------- | -------------------------------------- |
| id           | INTEGER | PK autoincrement                       |
| project_name | TEXT    | descrição do que esse campo representa |


{exemplo json schema, se aplicavel}
```json
{
  "type": "root",
  "children": [
    {"type": "heading", "fields": {"depth": "int", "start_line": "int", "end_line": "int"},
     "children": [{"type": "text", "fields": {"start_line": "int", "end_line": "int"}}]},
    {"type": "paragraph", "children": [
      {"type": "text"}, {"type": "strong"}, {"type": "em"},
      {"type": "inlineCode"}, {"type": "link", "fields": {"url": "str", "title": "str"}
    }]},
    {"type": "code", "fields": {"lang": "str", "value": "str", "start_line": "int", "end_line": "int"}},
    {"type": "list", "fields": {"ordered": "bool"},
     "children": [{"type": "listItem", "children": [{"type": "paragraph"}]}]},
    {"type": "blockquote", "children": [{"type": "paragraph"}]},
    {"type": "thematicBreak"},
    {"type": "table", "children": [
      {"type": "tableRow", "children": [{"type": "tableCell", "children": [{"type": "text"}]}]}
    ]}
  ]
}
```


#### 1.5.1.2. demais dados, armazenamento fisico

##### 1.5.1.2.1. documentos de dados
{conteudo opcional, conforme o escopo do projeto}
geralmente documentos json

##### 1.5.1.2.2. banco de dados `database_name`
{conteudo opcional, conforme o escopo do projeto}

###### 1.5.1.2.2.1. tabela `table_name`
{conteudo opcional, conforme o escopo do projeto}

| campo        | tipo    | descrição                              |
| ------------ | ------- | -------------------------------------- |
| id           | INTEGER | PK autoincrement                       |
| project_name | TEXT    | descrição do que esse campo representa |

###### 1.5.1.2.2.2. view `view_name`
{conteudo opcional, conforme o escopo do projeto}

| campo saida | tipo | descrição                                             |
| ----------- | ---- | ----------------------------------------------------- |
| field_1     | TEXT | breve descrição da transformação em linguagem natural |

#### 1.5.1.3. demais dados, armazenamento temporario no run time 
{conteudo opcional, conforme o escopo do projeto}

#### 1.5.1.4. dados de negocio, modelos para code scripts
SRP, responsabilidades de classes, métodos 
classes/methods data flow
##### 1.5.1.4.1. schemas de extração/importação
**Responsabilidade**: Documentar os schemas declarativos usados pelo sistema (ast_model, json_schema_*).

**Instrução de preenchimento**: Explicar o que cada schema faz e qual sua relação com os demais. Incluir code blocks com a definição dos schemas (Python dicts ou JSON). Incluir tabela de template de arquivos gerados (se aplicável).

##### 1.5.1.4.2. schemas internos para transformações intermediarias

##### 1.5.1.4.3. schemas de exportação

### 1.5.2. dados de controle 

#### 1.5.2.1. dados de controle, armazenamento fisico
{conteudo obrigatorio, conforme o escopo do projeto}
tipos de dados: [auth, config, actions, state]

##### 1.5.2.1.1. fonte de dados de controle `data_source_path`
**Data source name template**: para o caso de documentos com name template

{tabela, se aplicavel}
| campo        | tipo    | descrição                              |
| ------------ | ------- | -------------------------------------- |
| id           | INTEGER | PK autoincrement                       |
| project_name | TEXT    | descrição do que esse campo representa |


{exemplo json schema, se aplicavel}
```json
{
  "type": "root",
  "children": [
    {"type": "heading", "fields": {"depth": "int", "start_line": "int", "end_line": "int"},
     "children": [{"type": "text", "fields": {"start_line": "int", "end_line": "int"}}]},
    {"type": "paragraph", "children": [
      {"type": "text"}, {"type": "strong"}, {"type": "em"},
      {"type": "inlineCode"}, {"type": "link", "fields": {"url": "str", "title": "str"}
    }]},
    {"type": "code", "fields": {"lang": "str", "value": "str", "start_line": "int", "end_line": "int"}},
    {"type": "list", "fields": {"ordered": "bool"},
     "children": [{"type": "listItem", "children": [{"type": "paragraph"}]}]},
    {"type": "blockquote", "children": [{"type": "paragraph"}]},
    {"type": "thematicBreak"},
    {"type": "table", "children": [
      {"type": "tableRow", "children": [{"type": "tableCell", "children": [{"type": "text"}]}]}
    ]}
  ]
}
```

#### 1.5.2.2. dados de controle, armazenamento temporario no run time 
{conteudo opcional, conforme o escopo do projeto}

#### 1.5.2.3. dados de controle, modelos para code scripts

##### 1.5.2.3.1. schemas de extração/importação

##### 1.5.2.3.2. schemas internos para transformações intermediarias

##### 1.5.2.3.3. schemas de exportação

# 2. Template SRD

## 2.1. Sobre este documento

### 2.1.1. resumo
SRD (Software Requirements Document, ou Documento de Requisitos do Produto), documento nº 2 da familia de documentos de projeto [PRD, SRD, session_code_blocks, code_scripts, plan, plan_control].
O SRD define as especificações detalhadas para o desenvolvimento do projeto, sob a ótica funcional, suas responsabilidades, lógicas e modelos de funções e de dados. As especificações do SRD terão os nomes de todos os [code_scripts, classes, metodos] com descrições em linguagem natural das responsabilidades e logicas, ficando a cargo do documento session_code_blocks (blocos de codigo em documento markdown) especificar explicitamente os algoritmos de cada [classe, metodo] em snippets de codigo.

### 2.1.2. instruções

#### 2.1.2.1. instruções gerais
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

#### 2.1.2.2. sobre a seção "contexto do projeto"
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

#### 2.1.2.3. sobre a seção "arquitetura do projeto"
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

#### 2.1.2.4. sobre a seção "arquitetura de funções"
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
| {fucntion_name} | {lista dos code scripts mais relevantes}               | {{responsabilidades principais da função}} |
| {fucntion_name} | {lista das instruções [agent, skills] mais relevantes} | {{responsabilidades principais da função}} |

Estilos de **formatação** da seção
- sempre usar: [texto simples, listas não ordenadas, tabelas]
- nunca usar: [thematicBreak, listas ordenadas, code blocks, backtick blocks]

#### 2.1.2.5. sobre a seção "arquitetura de dados"
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

#### 2.1.2.6. sobre a seção "descrições funcionais"
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

## 2.2. contexto do projeto 

### 2.2.1. objetivos e resumo 
{from PRD}

### 2.2.2. stack do projeto 
{from PRD}

### 2.2.3. caminhos do projeto (relativos a project_path) 
{from PRD}

## 2.3. arquitetura do projeto 
### 2.3.1. camada frontend
#### 2.3.1.1. src/view_shell/
### 2.3.2. camada backend
#### 2.3.2.1. src/controllers/
#### 2.3.2.2. src/services/
##### 2.3.2.2.1. src/services/~~painel_settings~~painel_init.py
##### 2.3.2.2.2. src/services/parse
##### 2.3.2.2.3. src/services/logs
##### 2.3.2.2.4. src/services/dart_tools
#### 2.3.2.3. src/utils_io/
#### 2.3.2.4. src/sql_sqlite/
##### 2.3.2.4.1. src/sql_sqlite/sql_parse_md
##### 2.3.2.4.2. src/sql_sqlite/sql_tkinter
##### 2.3.2.4.3. src/sql_sqlite/sql_parse_script
#### 2.3.2.5. src/sql_supabase/
#### 2.3.2.6. src/models/
##### 2.3.2.6.1. src/models/schemas
#### 2.3.2.7. src/~~config~~ repositories/
##### 2.3.2.7.1. src/config/schemas
##### 2.3.2.7.2. src/~~utils_auth~~/auth_data*.json
#### 2.3.2.8. src/temp
### 2.3.3. camada dados
#### 2.3.3.1. dbMu/
- files
  - parse_dart.db
  - parse_md.db
#### 2.3.3.2. doc_painel/

## 2.4. arquitetura de funções

### 2.4.1. resumo
{from PRD}

### 2.4.2. pipeline [function_type]
{from PRD}

### 2.4.3. function type automatic

##### 2.4.3.1.1. function group <function_group_name>
| funcao          | arquivos principais                                    | descricao                                  |
| --------------- | ------------------------------------------------------ | ------------------------------------------ |
| {fucntion_name} | {lista dos code scripts mais relevantes}               | {{responsabilidades principais da função}} |
| {fucntion_name} | {lista das instruções [agent, skills] mais relevantes} | {{responsabilidades principais da função}} |

##### 2.4.3.1.2. classe `class_name`
**Responsabilidade**: responsabilidade da classe 
**Fora do escopo**: descrição breve das responsabilidades que estão fora do escopo

| Método        | Assinatura                                    | Descrição                                                                     |
| ------------- | --------------------------------------------- | ----------------------------------------------------------------------------- |
| `method_name` | Exemplo: `parse_args() -> argparse.Namespace` | Parseia `--action` (md_ast, md_json, md_sqlite) e `--input` (paths opcionais) |

### 2.4.4. function type agent
#### 2.4.4.1. agent `agent_name` 
**Responsabilidade**: responsabilidade do agente 
**Fora do escopo**: descrição breve das responsabilidades que estão fora do escopo
**Prompt**: prompt do agente

##### 2.4.4.1.1. skill `skill_name` 
**Responsabilidade**: responsabilidade da skill 
**Fora do escopo**: descrição breve das responsabilidades que estão fora do escopo
**Prompt**: prompt da skill

## 2.5. arquitetura de dados

### 2.5.1. dados de negocio 

#### 2.5.1.1. dados fonte, armazenamento fisico
{conteudo obrigatorio, conforme o escopo do projeto}

##### 2.5.1.1.1. fonte de dados de negocio `data_source_path`
**Data source name template**: para o caso de documentos com name template

{tabela, se aplicavel}
| campo        | tipo    | descrição                              |
| ------------ | ------- | -------------------------------------- |
| id           | INTEGER | PK autoincrement                       |
| project_name | TEXT    | descrição do que esse campo representa |


{exemplo json schema, se aplicavel}
```json
{
  "type": "root",
  "children": [
    {"type": "heading", "fields": {"depth": "int", "start_line": "int", "end_line": "int"},
     "children": [{"type": "text", "fields": {"start_line": "int", "end_line": "int"}}]},
    {"type": "paragraph", "children": [
      {"type": "text"}, {"type": "strong"}, {"type": "em"},
      {"type": "inlineCode"}, {"type": "link", "fields": {"url": "str", "title": "str"}
    }]},
    {"type": "code", "fields": {"lang": "str", "value": "str", "start_line": "int", "end_line": "int"}},
    {"type": "list", "fields": {"ordered": "bool"},
     "children": [{"type": "listItem", "children": [{"type": "paragraph"}]}]},
    {"type": "blockquote", "children": [{"type": "paragraph"}]},
    {"type": "thematicBreak"},
    {"type": "table", "children": [
      {"type": "tableRow", "children": [{"type": "tableCell", "children": [{"type": "text"}]}]}
    ]}
  ]
}
```


#### 2.5.1.2. dados transformados, armazenamento fisico

##### 2.5.1.2.1. documentos de dados
{conteudo opcional, conforme o escopo do projeto}
geralmente documentos json

##### 2.5.1.2.2. banco de dados `database_name`
{conteudo opcional, conforme o escopo do projeto}

###### 2.5.1.2.2.1. tabela `table_name`
{conteudo opcional, conforme o escopo do projeto}

| campo        | tipo    | descrição                              |
| ------------ | ------- | -------------------------------------- |
| id           | INTEGER | PK autoincrement                       |
| project_name | TEXT    | descrição do que esse campo representa |

###### 2.5.1.2.2.2. view `view_name`
{conteudo opcional, conforme o escopo do projeto}

| campo saida | tipo | descrição                                             |
| ----------- | ---- | ----------------------------------------------------- |
| field_1     | TEXT | breve descrição da transformação em linguagem natural |

#### 2.5.1.3. dados transformados, armazenamento temporario no run time 
{conteudo opcional, conforme o escopo do projeto}

#### 2.5.1.4. modelos para code scripts

##### 2.5.1.4.1. schemas de extração/importação
**Responsabilidade**: Documentar os schemas declarativos usados pelo sistema (ast_model, json_schema_*).

**Instrução de preenchimento**: Explicar o que cada schema faz e qual sua relação com os demais. Incluir code blocks com a definição dos schemas (Python dicts ou JSON). Incluir tabela de template de arquivos gerados (se aplicável).

Template: 


| schema name | code scripts | descricao |
| ----------- | ------------ | --------- |
|             |              |           |


- arquivo `dev/docs/spec/srd.schema.json` (único para todos os schemas do srd)
```json
{schema_name: {schema}}
```
- schema_name = chave -> srd
- code scripts: lista de scripts que utilizam o schema
##### 2.5.1.4.2. schemas internos para transformações intermediarias

##### 2.5.1.4.3. schemas de exportação

### 2.5.2. dados de controle [auth, config, actions, state]


## 2.6. descrições funcionais

### 2.6.1. lógicas, responsabilidades e requisitos por classe/metodo
{conteudo conforme instruções}
- tipo [coordenação de processo, execução de processo, processamento de dados]
- descrições interfuncionais (coordenação, invocação)
- descrições intrafuncionais (execução, implementação)
- responsabilidades comuns 
	- etapas em serie, onde cada etapa
	- busca os dados na fonte (input)
	- executa as tranformações necessarias
	- constroi o mapa de dados para a proxima etapa (output)
- processamento de dados (data block, input, transformação, output)
    - BuildAssets 
      - input: diretório de assets no disco 
      - transformações: scan pastas `{platform}.{content_type}`, parse timestamp + frontmatter + body, classificar por tipo (textOnly/textWithMedia/mediaOnly) 
      - output: `List<AssetsContent>` (AssetsContent = agrupamento por pasta + List.AssetsEntry) 
      - data blocks processados: 
        - post type: platform, content_type inferidos da pasta; media_type inferido da extensão 
        - texto: frontmatter.title + .md body 
        - media: image_path / video_path resolvidos via media_file do frontmatter 
        - schedule: timestamp extraído do nome do arquivo 
    - BuildPostConfig 
      - input: `List<AssetsContent>`
      - transformações: mapear AssetsContent.Content → Map post_config (fromAssetsContent), resolver campos de texto (titleFrom + bodyFrom + defaultTextForType), formatar schedule
      - output: `List<Map post_config>` no schema definido
      - data blocks processados:
        - post type: platform, content_type, media_type (copia direta)
        - texto: text_values.title + text_values.body (de AssetsContent ou fallback defaultTextForType)
        - media: image_path, video_path (resolvidos do AssetsContent)
        - schedule: published (bool), scheduled_publish_time (ISO8601 ou null)
    - BuildPostContent 
      - input: `Map post_config` (um post)
      - transformações: copiar fields fixos (platform, content_type, media_type, published, scheduled_publish_time, retry_config), copiar paths (image_path, video_path), resolver texto no field correto (postType.textField = message / caption / description)
      - output: `Map post_content`
      - data blocks processados:
        - post type: platform, content_type, media_type (copia direta)
        - texto: title (de text_values.title) + body no textField correto (de text_values.body)
        - media: image_path, video_path (copia direta)
        - schedule: published, scheduled_publish_time (copia direta)
    - BuildPayload 
      - input: `Map post_content`
      - transformações: construir objeto PostContent Dart (TextContent / ImageContent / VideoContent) com base em media_type + campos preenchidos, validar existência dos paths
      - output: `PostContent`
      - data blocks processados:
        - post type: endpoint, uploadFlow (via PostType)
        - texto: extrair do textField correto (caption / description / message)
        - media: validar image_path / video_path no disco 
        - schedule: passed through via PostType.decorate 

# 3. template srd session code blocks 

- resumo do srd: selected logic map maps review rules   
- resumo do control map + tag system 
- selected code blocks 

# 4. schema logic maps 
- [arquitetura funções] x [arquitetura funções] = [descrições]
- [arquitetura funções] x [arquitetura dados] = [descrições]

# 5. template plano 
- plano integral: etapas 
- plano sessão

# 6. schema control maps 
- plan map 
- **code map**: [files, classes, métodos] x [funções negócio] = tags [pendencia, maturidade] 
  - pendencia: [novo, refatorar, manter, eliminar] 
  - maturidade: [descrições, code block, quality, test] 
- **data process map**: [files, classes, métodos] x [data blocks] = tags [pendencia, maturidade] 

# 1. Sobre este documento

## 1.1. resumo
{template PRD}

## 1.2. instruções
### 1.2.1. instruções gerais
{template PRD}

### 1.2.2. sobre a seção "contexto do projeto"
{template PRD}

### 1.2.3. sobre a seção "arquitetura do projeto"
{template PRD}

### 1.2.4. sobre a seção "arquitetura de funções"
{template PRD}

### 1.2.5. sobre a seção "arquitetura de dados"
{template PRD}

# 2. arquitetura do projeto
Neste projeto estamos revisando a arquitetura existente para uma organização mais clara de layers.

## 2.1. versão atual ⟶ versão nova
path base: `C:\Users\muril\OneDrive\01 mycloud\01 sistMu\10.01 scripts\01_root\main\260511_meta_api\`
### 2.1.1. camada frontend
| versão atual                       | versão nova                            | cometários |
| ---------------------------------- | -------------------------------------- | ---------- |
| dev\src\painel\painel_controle.ps1 | dev\src\view_shell\painel_controle.ps1 |            |

### 2.1.2. camada backend
| versão atual                             | versão nova                     | cometários                               |
| ---------------------------------------- | ------------------------------- | ---------------------------------------- |
|                                          | dev\src\controllers             | ainda não existe code script             |
| dev\src\painel\config\painel_settings.py | dev\src\services\painel_init.py |                                          |
| dev\src\painel\services                  | dev\src\services                |                                          |
| dev\src\painel\services\logs             | dev\src\services\logs           |                                          |
| dev\src\painel\services\parse            | dev\src\services\parse          |                                          |
|                                          | dev\src\services\sessions       | ainda não existe code script             |
|                                          | dev\src\services\sync           | ainda não existe code script             |
| dev\src\painel\dart_tools                | dev\src\services\dart_tools     |                                          |
| dev\src\painel\services\utils_io         | dev\src\utils_io                |                                          |
| dev\src\sql_sqlite                       | dev\src\sql_sqlite              |                                          |
| dev\src\painel\models                    | dev\src\models                  |                                          |
| dev\src\painel\config                    | dev\src\repositories            | sub-pasta schema → models?               |
| dev\src\utils_auth                       | dev\src\repositories            | renomear arquivos para `auth_data*.json` |
|                                          | dev\src\temp                    | testes                                   |


### 2.1.3. camada dados
| versão atual           | versão nova                   | cometários |
| ---------------------- | ----------------------------- | ---------- |
| dev\dbMu\parse_dart.db | dev\dbMu\sqlite\parse_dart.db |            |
| dev\dbMu\parse_md.db   | dev\dbMu\sqlite\parse_md.db   |            |
| dev\parse_docs         | dev\dbMu\doc_painel           |            |

# 3. arquitetura de funções 

## 3.1. resumo
- pipeline [type, function group]
	- [automatic], criação de markdown, extração de AST markdown
	- [session], edição [markdown, code scripts] em sessões interativas
  - [agent] edição e revisão [markdown, code scripts] com base em instruções padronizadas
- automatic functions 
  - painel controle, section parse 
    - parse md [PRD, SRD, session_code_blocks] ast [text blocks, tables, code blocks] ⟶ [json, sqlite]
  	- parse code_scripts [ps1, python, dart] ast ⟶ [json, sqlite]  
  	- parse code_scripts [ps1, python, dart] raw ⟶ [json, sqlite] 
  - painel controle, section session 
    - update AGENTS.md: [prompt, selected PRD sections, selected templates, selected rules] ⟶ AGENTS.md 
    - create PRD: [template_PRD, rules] ⟶ PRD 
    - create SRD: [template_SRD, rules] ⟶ SRD 
    - lint code_scripts [ps1, python, dart] ⟶ [json, sqlite] 
  - painel controle, section sync 
    - sync json ⟷ sqlite ⟷ csv ⟷ xlsx
  - sql views
    - logic_map_functions
    - logic_map_functions_data
    - control_map_code
    - control_map_data
- session functions: interações [user, agent] via prompt, sem regras 
- agent functions 
	- rule-edit [naming_rules, variables_rules, data_object_rules, orchestrator_rules] 
	- spec-edit [SRD, session_code_blocks] 
	- spec-review [SRD, session_code_blocks] ⟶ [review_srd_{version}.md, review_code_blocks_{version}.md]  
	- code-script-edit [code_scripts] 
	- code-script-edit-comments [comments, tags] 
	- code-script-review [code_scripts] ⟶ review_code_scripts_{version}.md 
	- control-map-edit
	- control-map-review

## 3.2. pipeline [type, function]
- [automatic] update PRD: [PRD_00, template_PRD] ⟶ PRD_01
- [automatic] update AGENTS.md: [AGENTS, PRD_01] ⟶ AGENTS.md
- [session] update PRD 
- [automatic] create SRD: [PRD_02, template_SRD] ⟶ SRD_00
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

## 3.3. automatic functions

### 3.3.1. painel controle, section parse
- 🟤 parse md [PRD, SRD, session_code_blocks] ast [text blocks, tables, code blocks] ⟶ [json, sqlite]
- 🟤 parse code_scripts [ps1, python, dart] ast ⟶ [json, sqlite]  
- 🟤 parse code_scripts [ps1, python, dart] raw ⟶ [json, sqlite] 

### 3.3.2. painel controle, section session 

#### 3.3.2.1. update PRD 
- ⚪️ update PRD
  - input: [PRD_00, template_PRD] 
  - model: 
  - process: 
  - output: PRD_01 

#### 3.3.2.2. update AGENTS.md 
- ⚪️ update AGENTS.md
  - input: [prompt, selected PRD sections, selected templates, selected rules] 
  - model: 
  - process: transclusão dos hipertextos
  - output: AGENTS.md 

#### 3.3.2.3. create SRD 
aplicar hierarquia funcional com base nos modelos de dados
⚪️ [template_SRD, rules] ⟶ SRD 

#### 3.3.2.4. lint tools

- ⚪️ lint code_scripts [ps1, python, dart] ⟶ [json, sqlite] 

| tipo de violação\ tool                 | architecture_enforcer | pylint | import-linter | mypy | radon+xenon |
| -------------------------------------- | :-------------------: | :----: | :-----------: | :--: | :---------: |
| **Nomeacao inadequada**                |                       |   x    |               |      |             |
| **Acoplamento indevido**               |           x           |        |       x       |      |             |
| **Violaçao de SRP — escopo da classe** |           x           |        |               |      |             |
| **Não uso de metodo unificado**        |           x           |        |               |      |             |
| **Duplicacao de codigo**               |                       |   x    |               |      |             |
| **Uso indevido de variaveis**          |           x           |   x    |               |      |             |
| **Uso indevido de objetos de dados**   |           x           |        |               |  x   |             |
| **Import de camada proibida**          |                       |        |       x       |      |             |
| **Complexidade / classe grande**       |                       |   x    |               |      |      x      |

### 3.3.3. painel controle, section sync
Transformações entre os modelos de dados.
- ⚪️ sync json ⟷ sqlite ⟷ csv ⟷ xlsx
- ⚪️ mirroring [md, json, toml, csv, xlsx]  

### 3.3.4. sql views

#### 3.3.4.1. view logic_map_functions 
- ⚪️ [arquitetura funções] x [arquitetura funções] = [descrições]

#### 3.3.4.2. view logic_map_functions_data 
- ⚪️ [arquitetura funções] x [arquitetura dados] = [descrições]

#### 3.3.4.3. view control_map_code 
- ⚪️ **code map**: [files, classes, métodos] x [funções negócio] = tags [pendencia, maturidade] 
  - pendencia: [novo, refatorar, manter, eliminar] 
  - maturidade: [descrições, code block, quality, test] 

#### 3.3.4.4. view control_map_code 
- ⚪️ **data process map**: [files, classes, métodos] x [data blocks] = tags [pendencia, maturidade] 


## 3.4. agent functions
usar project documents rules  
- ⚪️ rule-edit [naming_rules, variables_rules, data_object_rules, orchestrator_rules] 
- ⚪️ spec-edit [SRD, session_code_blocks] 
- ⚪️ spec-review [SRD, session_code_blocks] ⟶ [review_srd_{version}.md, review_code_blocks_{version}.md]  
- ⚪️ code-script-edit [code_scripts] 
- ⚪️ code-script-edit-comments [comments, tags] 
- ⚪️ code-script-review [code_scripts] ⟶ review_code_scripts_{version}.md 
- ⚪️ control-map-edit
- ⚪️ control-map-review

# 4. arquitetura de dados

## 4.1. dados de negocio
### 4.1.1. dados fonte, armazenamento fisico
#### 4.1.1.1. fonte de dados de negocio `project_path\PRD`
**Data source name template**: para o caso de documentos com name template

#### 4.1.1.2. fonte de dados de negocio `project_path\SRD`
**Data source name template**: para o caso de documentos com name template

#### 4.1.1.3. fonte de dados de negocio `project_path\code_blocks`
**Data source name template**: para o caso de documentos com name template


#### 4.1.1.4. fonte de dados de negocio `code_scripts_folder`
documentos code_scripts [ps1, python, dart] 
code doc [md, json, sqlite]
code blocks, control maps

### 4.1.2. demais dados, armazenamento fisico 
#### 4.1.2.1. demais dados `json_docs_folder`
documentos markdown [tables, code blocks]
PRD, SRD, code blocks
#### 4.1.2.2. demais dados `sqlite_folder`
### 4.1.3. demais dados, armazenamento temporario no run time 
### 4.1.4. modelos para code scripts
SRP, responsabilidades de classes, métodos 
classes/methods data flow

## 4.2. dados de controle [auth, config, actions. state]
### 4.2.1. repositorios fonte
### 4.2.2. armazenamento físico 
### 4.2.3. armazenamento temporário no run time 
run time data access

### 4.2.4. modelos para code scripts
SRP, responsabilidades de classes, métodos 
classes/methods data flow

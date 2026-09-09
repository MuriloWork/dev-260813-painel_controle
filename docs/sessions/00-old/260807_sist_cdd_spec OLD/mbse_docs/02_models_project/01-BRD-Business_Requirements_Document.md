# 1. Sobre este documento

## 1.1. resumo

BRD – Business Requirements Document – Defines the general business requirements for the project. Identifies business and end-user requirements, problems or issues, project information, process information, and training and documentation requirements.


- referências: docs 

PRD (Product Requirements Document, ou Documento de Requisitos do Produto), documento nº 1 da familia de documentos de projeto [PRD, SRD, session_code_blocks, code_scripts, plano].
O PRD define as especificações desenvolvimento de alto nível do projeto, sob a ótica do negócio, suas arquiteturas e modelos de funções e de dados. As especificações do PRD sempre serão decrescentes em precisão, ou seja, mais precisas nas primeiras camadas de especificação e menos precisas nas últimas camadas, ficando a cargo do documento SRD (Software Requirements Document) aprofundar o detalhamento das especificações.

Na arquitetura de funções de negócio serão definidos [layers, folders, code scripts].

Na arquitetura de dados serão definidos [layers, folders, armazenamento, modelos]

## 1.2. instruções

### 1.2.1. instruções gerais
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
continuação da arquitetura do projeto para layers [frontend, backend], sob a ótica funcional, podendo atravessar varios code scripts

legenda: status implementação  
- 🟢 finalizado  
- 🔵 funcionando, falta organizar e testar consistencia  
- 🟤 implementação script iniciada  
- 🟡 code blocks definidos e revisados  
- 🟠 descrição funcional definida e revisada  
- ⚪️ descrição funcional não iniciada ou parcial  

### 1.2.5. sobre a seção "arquitetura de dados"
continuação da arquitetura do projeto para layers [data, backend], sob a ótica estrutural, podendo atravessar varios code scripts

Tipos de dados:
- dados de negocio: dados principais, ligados aos objetivos do projeto
- dados de controle 
	- auth: endereços, tokens e senhas de validação de acesso para API e serviços
	- config: configurações estáticas de operação do sistema (projeto)
	- actions: configurações dinâmicas do pipeline do sistema (projeto), definem os tipos de ações que podem ser selecionados no disparo ou durante a operação do sistema
	- state: configurações de estado do sistema ou da interface do usuario

# 2. Contexto Operacional (Black-Box)

## 2.1. Conceitos MBSE Envolvidos

- **Abstração e Limite do Sistema (_System Boundary_):** Tratamento do sistema como uma "Caixa-Preta" (_Black-Box_), onde apenas as interações com o ambiente externo (Atores) são visíveis, ocultando os detalhes de implementação interna.
- **Concept of Operations (ConOps):** Definição das condições operacionais, intenção de uso, gatilhos, pré e pós-condições sem comprometer a arquitetura lógica ou física.

## 2.2. Resumo das Definições das Referências

1. **OMG SysML v1.7 (Capítulo 8 - Black-Box View / IBD):**
    - **Conceito:** A visão _Black-Box_ trata o bloco do sistema como um elemento opaco. Ela esconde a estrutura interna (peças, partes, subsistemas) e expõe exclusivamente sua **fronteira** (_System Boundary_).
    - **Aplicação:** As interações com o ambiente externo ocorrem por meio de **Portas** (_Ports_) e **Fluxos de Itens** (_Item Flows_). Mostra apenas _o que entra_, _o que sai_ e _quem (Atores)_ interage nas fronteiras.
2. **ISO/IEC/IEEE 15288:2015 (Seção 6.4.2 - Business or Mission Analysis & Stakeholder Needs and Requirements Definition):**
    - **Conceito:** Define o **Operational Concept (OpsCon / ConOps)** como a declaração formal do objetivo de negócio, serviços prestados, ambiente operacional e expectativas dos _stakeholders_.
    - **Aplicação:** Estabelece a transição entre o problema de negócio (_por que o sistema deve existir_) e as restrições de alto nível sob as quais o sistema operará, sem ditar como o sistema será construído.
3. **INCOSE Systems Engineering Handbook (sobre ConOps):**
    - **Conceito:** Descreve o "Dia a Dia" do sistema em operação (_User Operational Scenarios_).
    - **Aplicação:** O ConOps segundo o INCOSE responde a: _Quem são os atores? Qual é o contexto de missão? Quais são as pré e pós-condições operacionais globais? Quais são os critérios de sucesso da operação?_

## 2.3. Referências Normativas e Padrões

- **[OMG SysML v1.7](https://www.omg.org/spec/SysML/1.7/PDF) (Capítulo 8 - Internal Block Diagrams / Black-Box view):** Define a modelagem do sistema como um bloco de mais alto nível (_System Under Test / System Under Development_), expondo apenas portas de interação com os atores externos.
- **ISO/IEC/IEEE 15288:2015 (Systems and software engineering — System life cycle processes):** Especifica os processos de definição das necessidades e requisitos dos _stakeholders_ (seção 6.4.2 - _Operational Concept_).
- **INCOSE Systems Engineering Handbook (4ª/5ª ed.):** Guia de elaboração do documento ConOps e ciclo de vida de requisitos operacionais.


# 3. contexto do sistema

Para o **`crm-cdd`** (Gerenciamento de Processos de Marketing em Mídias e Venda de Produtos Digitais), os campos do template do ConOps **permanecem os mesmos**, mas o **escopo da abstração muda de nível (Zoom Out)**:
- **Em vez de detalhar uma função:** O ConOps do `crm-cdd` abordará a **missão global do sistema** (ex: atração de leads, automação de funis, gestão de campanhas e conversão de vendas).

## 3.1. ConOps: Sistema crm-cdd (Visão Global de Sistema)

**Contexto Operacional (Black-Box System Level)**

* **Atores Principais:** Gestor de Tráfego, Estrategista de Conteúdo, Lead/Cliente Final, Copywriter.
* **Objetivo Global:** Automatizar e orquestrar a jornada de atração, engajamento e conversão de produtos digitais em múltiplas mídias.
* **Gatilhos Iniciais do Sistema:** Lançamento de campanha, captura de lead por formulário, evento de webhook de gateway de pagamento.
* **Pré-condições do Ecossistema:** Canais de mídia conectados (APIs externas), produtos digitais e ofertas cadastradas.
* **Pós-condição (Sucesso da Missão):** Leads qualificados, vendas liquidadas e métricas de ROI de campanhas consolidadas.


## 3.2. objetivos e resumo 
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

## 3.3. stack do projeto 
Exemplo:
- ambiente/servidor: local
- UI: flutter windows, flutter web, powershell
- script languages: dart, python, ps1, sqlite
- api: 
- dados: sqlite, json 

## 3.4. caminhos do projeto
Exemplo:

| path type | path name      | path                                                                                                                         |
| --------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| session   | project_path   | `C:\Users\muril\OneDrive\01 mycloud\01 sistMu\10.01 scripts\01_root\main\260511_meta_api`                                    |
| session   | session_folder | `C:\Users\muril\OneDrive\01 mycloud\01 sistMu\10.01 scripts\01_root\main\260511_meta_api\sessions\260623_arquitetura_painel` |
| target    | target_folder  | `C:\Users\muril\OneDrive\01 mycloud\01 sistMu\10.01 scripts\01_root\main\260511_meta_api\dev`                                |
| ignore    | ignore_pattern | `C:\Users\muril\OneDrive\01 mycloud\01 sistMu\10.01 scripts\01_root\main\260511_meta_api\dev\.*`                             |

pastas no `ignore_pattern` não são necessarias para edição de codigo, mas deverão ser movidas conforme a nova arquitetura


## 3.5. templates do projeto
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

# 4. arquitetura do projeto 
## 4.1. camada frontend
### 4.1.1. src/view_shell/
## 4.2. camada backend
### 4.2.1. src/controllers/
### 4.2.2. src/services/
#### 4.2.2.1. src/services/~~painel_settings~~painel_init.py
#### 4.2.2.2. src/services/parse
#### 4.2.2.3. src/services/logs
#### 4.2.2.4. src/services/dart_tools
### 4.2.3. src/utils_io/
### 4.2.4. src/sql_sqlite/
#### 4.2.4.1. src/sql_sqlite/sql_parse_md
#### 4.2.4.2. src/sql_sqlite/sql_tkinter
#### 4.2.4.3. src/sql_sqlite/sql_parse_script
### 4.2.5. src/sql_supabase/
### 4.2.6. src/models/
#### 4.2.6.1. src/models/schemas
### 4.2.7. src/~~config~~ repositories/
#### 4.2.7.1. src/config/schemas
#### 4.2.7.2. src/~~utils_auth~~/auth_data*.json
### 4.2.8. src/temp
## 4.3. camada dados
### 4.3.1. dbMu/
- files
  - parse_dart.db
  - parse_md.db
### 4.3.2. doc_painel/

# 5. arquitetura de funções 

## 5.1. resumo
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

## 5.2. pipeline [type, function]
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

## 5.3. automatic functions

### 5.3.1. painel controle, section parse
Exemplo:
- parse md [PRD, SRD, session_code_blocks] ast [tables, code blocks] ⟶ [json, sqlite]
- parse code_scripts [ps1, python, dart] ast ⟶ [json, sqlite]  
- parse code_scripts [ps1, python, dart] raw ⟶ [json, sqlite] 

### 5.3.2. painel controle, section session 

#### 5.3.2.1. create PRD 

[template_PRD, rules] ⟶ PRD 

#### 5.3.2.2. create SRD 
aplicar hierarquia funcional com base nos modelos de dados
[template_SRD, rules] ⟶ SRD 

#### 5.3.2.3. lint tools

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

### 5.3.3. painel controle, section sync
Transformações entre os modelos de dados.
- sync json ⟷ sqlite ⟷ csv ⟷ xlsx

## 5.4. agent functions
- inteligentes
  - interpretar com base nos conteudos [texto, lista]
    - logica funcional aplicada a [seções do documento, hierarquia funcional]
    - hierarquia funcional  
    - status de implementação
  - resumir conteudos
  - verificar a aderencia dos modelos [md, json]

### 5.4.1. project documents rules  

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


# 6. arquitetura de dados

## 6.1. dados de negocio 

### 6.1.1. dados fonte, armazenamento fisico
{conteudo obrigatorio, conforme o escopo do projeto}

#### 6.1.1.1. fonte de dados de negocio `data_source_path`
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


### 6.1.2. demais dados, armazenamento fisico

#### 6.1.2.1. documentos de dados
{conteudo opcional, conforme o escopo do projeto}
geralmente documentos json

#### 6.1.2.2. banco de dados `database_name`
{conteudo opcional, conforme o escopo do projeto}

##### 6.1.2.2.1. tabela `table_name`
{conteudo opcional, conforme o escopo do projeto}

| campo        | tipo    | descrição                              |
| ------------ | ------- | -------------------------------------- |
| id           | INTEGER | PK autoincrement                       |
| project_name | TEXT    | descrição do que esse campo representa |

##### 6.1.2.2.2. view `view_name`
{conteudo opcional, conforme o escopo do projeto}

| campo saida | tipo | descrição                                             |
| ----------- | ---- | ----------------------------------------------------- |
| field_1     | TEXT | breve descrição da transformação em linguagem natural |

### 6.1.3. demais dados, armazenamento temporario no run time 
{conteudo opcional, conforme o escopo do projeto}

### 6.1.4. dados de negocio, modelos para code scripts
SRP, responsabilidades de classes, métodos 
classes/methods data flow
#### 6.1.4.1. schemas de extração/importação
**Responsabilidade**: Documentar os schemas declarativos usados pelo sistema (ast_model, json_schema_*).

**Instrução de preenchimento**: Explicar o que cada schema faz e qual sua relação com os demais. Incluir code blocks com a definição dos schemas (Python dicts ou JSON). Incluir tabela de template de arquivos gerados (se aplicável).

#### 6.1.4.2. schemas internos para transformações intermediarias

#### 6.1.4.3. schemas de exportação

## 6.2. dados de controle 

### 6.2.1. dados de controle, armazenamento fisico
{conteudo obrigatorio, conforme o escopo do projeto}
tipos de dados: [auth, config, actions, state]

#### 6.2.1.1. fonte de dados de controle `data_source_path`
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

### 6.2.2. dados de controle, armazenamento temporario no run time 
{conteudo opcional, conforme o escopo do projeto}

### 6.2.3. dados de controle, modelos para code scripts

#### 6.2.3.1. schemas de extração/importação

#### 6.2.3.2. schemas internos para transformações intermediarias

#### 6.2.3.3. schemas de exportação


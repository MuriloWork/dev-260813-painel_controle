# 1. Sobre este documento

## 1.1. resumo

[[260617_conceitos_info_se_sdlc#2. modelos Mu|source: modelos Mu]]

| Form or Template               | Description                                                                                                                                                                                                                                                                                                 |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Business Analysis Document     | Define domain, ConOps,  stakeholders, problema/ oportunidade [[260617_conceitos_info_se#1.1.2.1. 2023 incose-systems-engineering-handbook.pdf page=128 Business or Mission Analysis\|source-md]]                                                                                                            |
| Business Requirements Document | Defines the general business requirements for the project. Identifies business and end user requirements, problems or issues, project information, process information, and training and documentation requirements. ([[260617_conceitos_info_se#1.1.2.2. Business (Stakeholder) Requirements\|source-md]]) |



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



# 2. business analysis 

## 2.1. domain
## 2.2. concept of operations

### 2.2.1. Contexto Operacional (Black-Box)

#### 2.2.1.1. Conceitos MBSE Envolvidos

- **Abstração e Limite do Sistema (_System Boundary_):** Tratamento do sistema como uma "Caixa-Preta" (_Black-Box_), onde apenas as interações com o ambiente externo (Atores) são visíveis, ocultando os detalhes de implementação interna.
- **Concept of Operations (ConOps):** Definição das condições operacionais, intenção de uso, gatilhos, pré e pós-condições sem comprometer a arquitetura lógica ou física.

#### 2.2.1.2. Resumo das Definições das Referências

1. **OMG SysML v1.7 (Capítulo 8 - Black-Box View / IBD):**
    - **Conceito:** A visão _Black-Box_ trata o bloco do sistema como um elemento opaco. Ela esconde a estrutura interna (peças, partes, subsistemas) e expõe exclusivamente sua **fronteira** (_System Boundary_).
    - **Aplicação:** As interações com o ambiente externo ocorrem por meio de **Portas** (_Ports_) e **Fluxos de Itens** (_Item Flows_). Mostra apenas _o que entra_, _o que sai_ e _quem (Atores)_ interage nas fronteiras.
2. **ISO/IEC/IEEE 15288:2015 (Seção 6.4.2 - Business or Mission Analysis & Stakeholder Needs and Requirements Definition):**
    - **Conceito:** Define o **Operational Concept (OpsCon / ConOps)** como a declaração formal do objetivo de negócio, serviços prestados, ambiente operacional e expectativas dos _stakeholders_.
    - **Aplicação:** Estabelece a transição entre o problema de negócio (_por que o sistema deve existir_) e as restrições de alto nível sob as quais o sistema operará, sem ditar como o sistema será construído.
3. **INCOSE Systems Engineering Handbook (sobre ConOps):**
    - **Conceito:** Descreve o "Dia a Dia" do sistema em operação (_User Operational Scenarios_).
    - **Aplicação:** O ConOps segundo o INCOSE responde a: _Quem são os atores? Qual é o contexto de missão? Quais são as pré e pós-condições operacionais globais? Quais são os critérios de sucesso da operação?_

#### 2.2.1.3. Referências Normativas e Padrões

- **[OMG SysML v1.7](https://www.omg.org/spec/SysML/1.7/PDF) (Capítulo 8 - Internal Block Diagrams / Black-Box view):** Define a modelagem do sistema como um bloco de mais alto nível (_System Under Test / System Under Development_), expondo apenas portas de interação com os atores externos.
- **ISO/IEC/IEEE 15288:2015 (Systems and software engineering — System life cycle processes):** Especifica os processos de definição das necessidades e requisitos dos _stakeholders_ (seção 6.4.2 - _Operational Concept_).
- **INCOSE Systems Engineering Handbook (4ª/5ª ed.):** Guia de elaboração do documento ConOps e ciclo de vida de requisitos operacionais.



## 2.3. stakeholders
## 2.4. definição do problema ou oportunidade
# 3. business requirements
## 3.1. cenarios operacionais (business use cases)
### 3.1.1. contexto do sistema

O sistema está no contexto de engenharia de software com base em modelagem. Sobre uma base comum de conhecimento desenvolvido durante o projeto os processos técnicos do ciclo de vida de desenvolvimento de software serão usados no desenvolvimento de aplicações particulares. 
- mbcg 
- crm 
- cms 
- planner 

Para o **`crm-cdd`** (Gerenciamento de Processos de Marketing em Mídias e Venda de Produtos Digitais), os campos do template do ConOps **permanecem os mesmos**, mas o **escopo da abstração muda de nível (Zoom Out)**:
- **Em vez de detalhar uma função:** O ConOps do `crm-cdd` abordará a **missão global do sistema** (ex: atração de leads, automação de funis, gestão de campanhas e conversão de vendas).

#### 3.1.1.1. ConOps: Sistema crm-cdd (Visão Global de Sistema)

**Contexto Operacional (Black-Box System Level)**

* **Atores Principais:** Gestor de Tráfego, Estrategista de Conteúdo, Lead/Cliente Final, Copywriter.
* **Objetivo Global:** Automatizar e orquestrar a jornada de atração, engajamento e conversão de produtos digitais em múltiplas mídias.
* **Gatilhos Iniciais do Sistema:** Lançamento de campanha, captura de lead por formulário, evento de webhook de gateway de pagamento.
* **Pré-condições do Ecossistema:** Canais de mídia conectados (APIs externas), produtos digitais e ofertas cadastradas.
* **Pós-condição (Sucesso da Missão):** Leads qualificados, vendas liquidadas e métricas de ROI de campanhas consolidadas.


#### 3.1.1.2. objetivos e resumo 
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

#### 3.1.1.3. stack do projeto 
Exemplo:
- ambiente/servidor: local
- UI: flutter windows, flutter web, powershell
- script languages: dart, python, ps1, sqlite
- api: 
- dados: sqlite, json 

#### 3.1.1.4. caminhos do projeto
Exemplo:

| path type | path name      | path                                                                                                                         |
| --------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| session   | project_path   | `C:\Users\muril\OneDrive\01 mycloud\01 sistMu\10.01 scripts\01_root\main\260511_meta_api`                                    |
| session   | session_folder | `C:\Users\muril\OneDrive\01 mycloud\01 sistMu\10.01 scripts\01_root\main\260511_meta_api\sessions\260623_arquitetura_painel` |
| target    | target_folder  | `C:\Users\muril\OneDrive\01 mycloud\01 sistMu\10.01 scripts\01_root\main\260511_meta_api\dev`                                |
| ignore    | ignore_pattern | `C:\Users\muril\OneDrive\01 mycloud\01 sistMu\10.01 scripts\01_root\main\260511_meta_api\dev\.*`                             |

pastas no `ignore_pattern` não são necessarias para edição de codigo, mas deverão ser movidas conforme a nova arquitetura


#### 3.1.1.5. templates do projeto
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


### 3.1.2. 260813_mbse_docs
#### 3.1.2.1. revisão conceitual 

##### 3.1.2.1.1. MBSE - Model Based Systems Engineering 
[[260617_conceitos_info_se]]
[[260617_conceitos_info_se#2. SDLC - Software Development Life Cicle]]
[[260617_conceitos_info_se_mbse]]

###### 3.1.2.1.1.1. análises de recursos MBSE

| titulo da analise  | hiperlink                                                                                                       | status |
| ------------------ | --------------------------------------------------------------------------------------------------------------- | ------ |
| modelagem          | [[260726_analise_mbse_models_00]]                                                                               |        |
| atributos          | [[260726_analise_mbse_atributos_00]]                                                                            |        |
| tools              | [[260726_analise_mbse_tools_00#1.1. Introdução ao Contexto das Ferramentas MBSE\|260726_analise_mbse_tools_00]] |        |
|                    |                                                                                                                 |        |

legenda:
não iniciado 
iniciado pelo agente 
finalizado pelo agente 
revisado pelo usuário 

#### 3.1.2.2. o sistema mbse_docs 
##### 3.1.2.2.1. Sistema MB-SDD

MB-SDD - Model Based Spec Driven Development - será um sistema de gerenciamento de especificações de software baseadas em modelos OMG

Diferente de abordagens tradicionais baseadas em documentos de texto estáticos, o MB-SDD atuará como um editor e gerenciador de especificações executáveis de software. Ele permitirá capturar requisitos, arquitetura de software, componentes, fluxos de dados e regras de negócio diretamente em modelos semânticos estruturados (UML, SysML, RAAML).

Principais Objetivos do Sistema
* **Modelagem Semântica Unificada**: Permitir a criação e edição gráfica e textual de diagramas de estrutura, comportamento e requisitos.
* **Manutenibilidade e Rastreabilidade**: Garantir o rastreamento bidirecional entre requisitos de software, elementos de arquitetura, restrições de negócio e código-fonte.
* **Independência de Plataforma** (MDA): Separar a especificação conceitual do sistema (CIM/PIM) das implementações de tecnologia específicas (PSM).
* **Interoperabilidade**: Consumir e exportar dados nos padrões XMI, JSON Schema e conectores de código-fonte.

##### 3.1.2.2.2. resumo dos documentos gerenciados pelo sistema 
- mbse_docs
	- inteligencia
		- skd - system knowledge documentation
		- instruções (loops), agents, skills
	- regras mbse: modelagem, arquiteturas, qualidade
	- modelos: templates, instruções
- modelos para um sistema alvo
	- sistema
		- dominio
		- software
			- spec current
				- README.md, prd, srd
	- projeto  = gsd-planning 
		- planejamento 
			- conceituação: Business Case Document, Concept of Operations
			- planos: Work Breakdown Structure, Project Plan (planos de execução)
			- controle: Action Item Status, controle de configuração
		- analise 
			- [[260617_conceitos_info_mbse#6.2.2. Requirements Definition Phase|source models]]: Business Requirements Document, Functional Requirements Document, Software Architecture Plan, Use Case Template, Requirements Inspection Checklist, Requirements Traceability Matrix
			- spec new: PRD
		- projeto
			- Systems Requirements Specifications, Database Design Document, User Interface Design Template, Code Review Checklist
			- spec new: SRD
	- sessão 
		- inteligencia
			- AGENTS.md
			- prompts
		- analises

#### 3.1.2.3. documentos mbse

##### 3.1.2.3.1. documentos de inteligencia 
###### 3.1.2.3.1.1. skd - system knowledge documentation
como funciona o sistema, instruções para humanos e agentes
###### 3.1.2.3.1.2. instruções (loops), agents, skills
####### 3.2.3.1.2.1. agent: session-planner 

- session-plan-init-investigate  
- session-plan-init-structure 
- session-plan-init-review 
- session-plan-init-publish 
- session-plan-update 
- session-plan-finish 

####### 3.2.3.1.2.2. agent: project-planner 

- skills 
  - project-prd 
  - project-srd 
  - project-plan-steps  
  - project-plan-map 
  - project-plan-code-map 

####### 3.2.3.1.2.3. agent: code-planner 

####### 3.2.3.1.2.4. agent: code-reviewer 

- input prompt  
  - contexto 
    - project_title: 
    - project_absolute_path: 
    - stack 
    - seção do projeto 
  - caminhos dos documentos, relativos ao {project_absolute_path} 
    - code_folder: 
    - code_target_files 
    - code_map: 
    - srd: seções [descrições, tag system] 
    - session_code_blocks: 
    - session_code_blocks_sections: [] 
    - requested_report: 
  - instruções 
- agent rules 
  - permissions: ~~skills~~, tools 
  - var paths map `{placeholders}` 
  - fix paths map 
    - output template 
    - skills 
    - aux files: json 
    - regras para chamar skills 
  - workflow 
    - ler 
    - executar 
    - salvar requested report, versionamento 
- skills 
  - code-spec-compliance 
    - paths map: srd [descrições, tag system] 
    - rules: conformidade com descrições, checklist 
  - code-quality 
    - paths map: code control map, code files, srd [tag system] 
    - rules: hierarquia, nomenclatura, complexidade 




##### 3.1.2.3.2. documentos de regras mbse
regras aplicáveis de:
- modelagem 
- arquitetura, design patterns
- rastreabilidade, gerenciamento
- qualidade

###### 3.1.2.3.2.1. regras gerais

####### 3.2.3.2.1.1. formatação 
####### 3.2.3.2.1.2. Legenda de Tags

######## 3.5.2.1.2.1. versao atual

| Tag   | Significado                                                     | Regra de consistência                                                                                           |
| ----- | --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `[1]` | **Novo** — classe/método que será criado                        | Deve existir em `classe nova` com `metodo novo` preenchido                                                      |
| `[2]` | **Refatorar** — método existente que muda de script/classe/nome | `script novo` e `classe nova` devem refletir o destino final. `metodo novo` opcional se só mudar de classe      |
| `[3]` | **Manter** — fica como está, sem alteração                      | `script novo` = `script atual`. `classe nova` = `subsection atual` (se aplicável). `metodo novo` = `item atual` |
| `[4]` | **Descartar** — será removido                                   | `script novo` e `classe nova` vazios. Nenhuma referência no novo código                                         |

######## 3.5.2.1.2.2. versao nova

| Tag     | Significado base                                                | Significado complementar (com base no status da especificação tecnica)                      |
| ------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `[1.0]` | **Novo** — classe/método que será criado                        | testado                                                                                     |
| `[1.1]` | **Novo** — classe/método que será criado                        | implementado                                                                                |
| `[1.2]` | **Novo** — classe/método que será criado                        | code block (dart ou markdown) validado pelo usuario                                         |
| `[1.3]` | **Novo** — classe/método que será criado                        | code block (dart ou markdown) criado                                                        |
| `[1.4]` | **Novo** — classe/método que será criado                        | descrição inicial (csv ou markdown) alinhada com "logica de responsabilidades e requisitos" |
| `[2.0]` | **Refatorar** — método existente que muda de script/classe/nome | testado                                                                                     |
| `[2.1]` | **Refatorar** — método existente que muda de script/classe/nome | implementado                                                                                |
| `[2.2]` | **Refatorar** — método existente que muda de script/classe/nome | code block (dart ou markdown) validado pelo usuario                                         |
| `[2.3]` | **Refatorar** — método existente que muda de script/classe/nome | code block (dart ou markdown) criado                                                        |
| `[2.4]` | **Refatorar** — método existente que muda de script/classe/nome | descrição inicial (csv ou markdown) alinhada com "logica de responsabilidades e requisitos" |
| `[3.0]` | **Manter** — fica como está, sem alteração                      | —                                                                                           |
| `[4.0]` | **Descartar** — será removido                                   | —                                                                                           |

observações: 
- será necessario atualizar as atuais classificações da tabela csv (versao nova)
- itens classificados como [3.0] onde seja indentificada pendencia devem ser reclassificados para [2.2]
- descrição inicial (csv ou markdown) = nome do metodos + [descrição no csv OU descrição complementar no md (se necessario)]

####### 3.2.3.2.1.3. instruções de Consistência

######## 3.5.2.1.3.1. Verificação Cruzada

Para verificar a tabela CSV, aplicar estas instruções:

| #   | Regra                                                                                                                    | Como verificar                                          |
| --- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------- |
| 1   | Todo `[1]` novo deve ter `classe nova` e `metodo novo` preenchidos                                                       | Filtrar tag=`[1]`, checar se campos não vazios          |
| 2   | Todo `[2]` refatorar deve ter `script novo` diferente do `script atual` OU `classe nova` diferente de `subsection atual` | Filtrar tag=`[2]`, checar se pelo menos um campo difere |
| 3   | Todo `[3]` manter deve ter `script novo` = `script atual`                                                                | Filtrar tag=`[3]`, checar igualdade                     |
| 4   | Todo `[4]` descartar deve ter `script novo` e `classe nova` vazios                                                       | Filtrar tag=`[4]`, checar campos vazios                 |
| 5   | `metodo novo` deve ser único dentro de cada `classe nova`                                                                | Agrupar por classe nova, checar duplicatas              |
| 6   | Nenhum `metodo novo` deve ter nome de classe reservada (`class`)                                                         | Checar se "class" aparece como nome de método           |

######## 3.5.2.1.3.2. Verificação de Pipeline

| Etapa | Entrada               | Classe             | Saída                   |
| ----- | --------------------- | ------------------ | ----------------------- |
| 1     | Diretório de assets   | `BuildAssets`      | `List<AssetsContent>`   |
| 2     | `List<AssetsContent>` | `BuildPostConfig`  | `List<Map post_config>` |
| 3     | `Map post_config`     | `BuildPostContent` | `Map post_content`      |
| 4     | `Map post_content`    | `BuildPayload`     | `PostContent` (Dart)    |

Cada classe recebe o que a anterior produziu — sem saltos, sem dependências circulares.

######## 3.5.2.1.3.3. O que será eliminado

| Arquivo                                           | Destino                                                                                                   |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `src/scripts/post_builder.dart`                   | Eliminado (imports migrados)                                                                              |
| `src/scripts/publish/post_builder_facebook.dart`  | Métodos `resolveContent` e `_textFrom` movidos; `fillPostContentTextFields` e `_textFieldFor` descartados |
| `src/scripts/publish/post_builder_instagram.dart` | `resolveContent` movido; `fillPostContentFields` descartado                                               |

####### 3.2.3.2.1.4. regras de arquitetura, design patterns, qualidade de codigo

###### 3.1.2.3.2.2. project documents rules  
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


##### 3.1.2.3.3. formas de aplicação 
###### 3.1.2.3.3.1. aplicação manual
###### 3.1.2.3.3.2. aplicação automatica

####### 3.2.3.3.2.1. PRD

| doc\ modelos             | template | herança | instruções gerais | instruções especificas |
| ------------------------ | :------: | :-----: | :---------------: | :--------------------: |
| PRD                      |          |         |                   |                        |
| PRD sobre este documento |          |    x    |                   |                        |
| PRD contexto do projeto  |    x     |         |                   |                        |
| PRD logica funcional     |    x     |         |                   |                        |
| PRD funções de negócio   |    x     |         |                   |                        |
| PRD modelos de dados     |    x     |         |                   |                        |

####### 3.2.3.3.2.2. SRD

| documento, seção \ modelos                                                        | template | herança | instruções gerais | instruções especificas |
| --------------------------------------------------------------------------------- | :------: | :-----: | :---------------: | :--------------------: |
| SRD                                                                               |          |         |                   |                        |
| SRD sobre este documento                                                          |          |    x    |                   |                        |
| SRD arquitetura de funções                                                        |          |         |                   |                        |
| SRD arquitetura de funções, instruções e resumo                                   |          |         |                   |                        |
| SRD arquitetura de funções, instruções e resumo, instruções                       |          |    x    |                   |                        |
| SRD arquitetura de funções, instruções e resumo, resumo                           |    x     |         |                   |                        |
| SRD arquitetura de funções, funções de negócio                                    |          |    x    |                   |                        |
| SRD arquitetura de funções, funções de automação                                  |          |    x    |                   |                        |
| SRD arquitetura de funções, funções de automação, instruções e resumo             |          |         |                   |                        |
| SRD arquitetura de funções, funções de automação, instruções e resumo, instruções |          |    x    |                   |                        |
| SRD arquitetura de funções, funções de automação, instruções e resumo, resumo     |    x     |         |                   |                        |
| SRD arquitetura de funções, funções de automação, script `script_name`            |    x     |         |                   |                        |
| SRD arquitetura de funções, funções de automação, script, classe `class_name`     |    x     |         |                   |                        |
| SRD arquitetura de dados                                                          |    x     |         |                   |                        |
| SRD arquitetura de dados, instruções e resumo                                     |          |         |                   |                        |
| SRD arquitetura de dados, instruções e resumo, instruções                         |          |    x    |                   |                        |
| SRD arquitetura de dados, instruções e resumo, resumo                             |    x     |         |                   |                        |
| SRD descrições funcionais                                                         |    x     |         |                   |                        |

como os modelos são aplicados nos documentos:
- templates: formatos fixos, conteudo editável com base nas instruções gerais ou especificas
- herança: conteúdo não editáve, herdado de outro documento
- instruções*: conteúdo não editável# 5. documentos de sistema
###### 3.1.2.3.3.3. aplicação agêntica

#### 3.1.2.4. documentos de sistema 
#### 3.1.2.5. documentos de projeto 

##### 3.1.2.5.1. documentos de planejamento 
###### 3.1.2.5.1.1. planos de execução 

- plano integral: etapas 
- plano etapa, todo 
- control maps 
  - plan map 
  - **code map**: [files, classes, métodos] x [funções negócio] = tags [pendencia, maturidade] 
    - pendencia: [novo, refatorar, manter, eliminar] 
    - maturidade: [descrições, code block, quality, test] 
  - **data process map**: [files, classes, métodos] x [data blocks] = tags [pendencia, maturidade] 

##### 3.1.2.5.2. documentos de analise 
###### 3.1.2.5.2.1. alguns conceitos

####### 3.2.5.2.1.1. Matriz de Amarrações Operacionais (Sem Tecnologia/Classes)
######## 3.7.2.1.1.1. É um Diagrama de Definição de Blocos (BDD)?

A Matriz de Amarrações Operacionais em formato visual/conceitual aproxima-se de uma junção de:

1. **Internal Block Diagram (IBD) / Allocation Matrix:** Mostra os fluxos de informação passando entre subsistemas/camadas.
2. **Tabular Allocation View:** A OMG/SysML prevê matrizes de alocação (_Allocation Tables_) para mapear atividades para blocos lógicos ou para mapear funções entre camadas.

######## 3.7.2.1.1.2. Reformulação da Matriz no Formato Tabela por Camadas (Sua Sugestão)

Formatá-la em tabela com **referência ao pipeline** e **uma coluna por camada** deixa a rastreabilidade direta e clara:

  

######## 3.7.2.1.1.3. Exemplo de Matriz Tabular Operacional do `crm-cdd`:

| **Ref. Pipeline** | **Ref. Funcionalidade** | **Camada Operacional (Entrada / Interface)** | **Camada de Transformação (Regras de Negócio / Processamento)** | **Camada de Saída (Persistência / Notificação / Entrega)** |
| ----------------- | ----------------------- | -------------------------------------------- | --------------------------------------------------------------- | ---------------------------------------------------------- |
| **Passo 01**      | `[FN-2.1]`              | Captura dados do formulário de opt-in        | Valida duplicação de lead e calcula score inicial               | Registra novo lead no repositório de contatos              |
| **Passo 02**      | `[FN-2.3]`              | Recebe confirmação de abertura de e-mail     | Aplica regra de automação de fluxo de nutrição                  | Agenda próximo envio no canal do usuário                   |
| **Passo 03**      | `[FN-3.1]`              | Recebe webhook de checkout aprovado          | Transfere status do cliente e libera licença                    | Emite comprovante e envia acesso ao produto                |


####### 3.2.5.2.1.2. Requisitos de Regra e Exceções do Pipeline
######## 3.7.2.1.2.1. Referenciando cada Funcionalidade do Pipeline nos Requisitos

Na especificação formal do SysML (`Requirements Diagram` / `ISO 29148`), cada requisito deve ter uma relação explícita de rastreabilidade (estereótipos `«trace»` ou `«satisfy»`) apontando para a funcionalidade correspondente.

  

######## 3.7.2.1.2.2. Ajuste no Template de Requisitos para o `crm-cdd`:

Markdown

```
####### 4. Requisitos de Regra e Exceções do Pipeline

######## Regras de Negócio (RN)
* **[RN-01] [Ref: FN-2.1]:** O e-mail do lead deve ser validado via sintaxe e verificação de domínio antes do cadastro.
* **[RN-02] [Ref: FN-2.2]:** A pontuação de lead (*Lead Scoring*) deve ser recalculada a cada ação de clique em links monitorados.
* **[RN-03] [Ref: FN-3.1]:** A liberação de acesso ao produto digital deve ocorrer em no máximo 30 segundos após a confirmação do webhook de pagamento.

######## Tratameno de Exceções (EX)
* **[EX-01] [Ref: FN-2.1] Lead Duplicado:** Caso o e-mail já exista na base, o sistema deve fundir (*merge*) os dados e atualizar o histórico de interações sem criar um novo registro.
* **[EX-02] [Ref: FN-3.1] Falha no Webhook:** Se o gateway de pagamento não responder em 3 tentativas, o pipeline deve mover a transação para a fila de reconciliação manual e alertar o administrador.
```





###### 3.1.2.5.2.2. [[01-BRD-Business_Requirements_Document|BRD - Business_Requirements_Document]]
from ex-PRD

###### 3.1.2.5.2.3. [[02-FRD-Functional_Requirements_Document|FRD - Functional Requirements Document]] 
from ex-PRD
###### 3.1.2.5.2.4. Use Case Template

####### 3.2.5.2.4.1. Matriz de Amarrações Operacionais (Sem Tecnologia/Classes)

######## 3.7.2.4.1.1. Conceitos MBSE Envolvidos

- **Decomposição Funcional e Camadas (_Functional Layering / Abstraction Layers_):** Organização das responsabilidades operacionais em camadas (Interface, Transformação e Saída) sem associação com arquitetura de software (ex: MVC, Microserviços).
- **Alocação de Responsabilidade Operacional (_Operational Allocation_):** Estabelecimento das dependências e do fluxo de informações (_Data/Control Flows_) entre as camadas lógicas operacionais.

######## 3.7.2.4.1.2. Referências Normativas e Padrões

- **OMG SysML v1.7 (Capítulo 7 - Block Definition Diagrams & Structuring):** Definição da hierarquia lógica do sistema e decomposição do bloco do sistema em subsistemas funcionais abstratos.
- **OMG SysML v1.7 (Capítulo 15 - Allocation):** Conceito da relação `«allocate»`, usada para rastrear como capacidades/atividades de alto nível se conectam com as camadas lógicas de processamento antes de atingirem componentes físicos.


###### 3.1.2.5.2.5. Software Architecture Plan (from ex-PRD)
- stack 
	- scripts: dart, python, ps1, sqlite, api  
	- UI: flutter, web, shell 

###### 3.1.2.5.2.6. Requirements Traceability Matrix
###### 3.1.2.5.2.7. Requirements Inspection Checklist

##### 3.1.2.5.3. documentos de design
###### 3.1.2.5.3.1. srd 
  
- arquitetura de funções 
  - tipo: [negócio, automação] 
  - funções de automação (implementação)
   - arquitetura, folders, files 
     - classes, métodos, objetos 
- arquitetura de dados 
  - tipo: [ambiente, config, auth, state, script flow, negócio]
  - dados de negócio 
  - documentos, schemas, tabelas 
    - objetos, campos 
- blocos do modelo de dados  
	- post type: [platform, content_type, media_type]
	- texto: campos detalhados abaixo
	- media: [image_path, video_path]
	- schedule: [published, scheduled_publish_time]
- descrições funcionais (responsabilidades, lógicas, requisitos, restrições) 
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
- logic maps 
	- [arquitetura funções] x [arquitetura funções] = [descrições]
	- [arquitetura funções] x [arquitetura dados] = [descrições]

###### 3.1.2.5.3.2. srd session code blocks 

- resumo do srd: selected logic map maps review rules   
- resumo do control map + tag system 
- selected code blocks 

###### 3.1.2.5.3.3. code, code-review, test 

#### 3.1.2.6. documentos de sessão 

##### 3.1.2.6.1. inteligencia 
###### 3.1.2.6.1.1. session: AGENTS.md 

- objetivo, contexto [prd], entregas 
- referencias: agents 
##### 3.1.2.6.2. analises 

#### 3.1.2.7. casos de uso 

[[260807_sist_crm_00]]



## 3.2. limitações: fronteiras, interfaces, riscos, restrições
## 3.3. business needs
## 3.4. business requirements

**business requirements** —  descrever de forma a indicar caminho para system requirements (stack, arquitetura)







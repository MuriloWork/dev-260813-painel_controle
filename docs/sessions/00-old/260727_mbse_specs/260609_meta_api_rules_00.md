# 1. sobre este documento

# 2. documentos de projeto 

## 2.1. instruções e resumo

### 2.1.1. instruções
instruções

### 2.1.2. resumo
- general rules: naming, versioning  
- spec docs  
- plan docs  
	- plan & control rules: tag system  
- script docs  
	- review rules: spec, quality  

## 2.2. docs planejamento 

### 2.2.1. prd 

- funções de negócio 
- stack 
	- scripts: dart, python, ps1, sqlite, api  
	- UI: flutter, web, shell 
- referências: docs 

### 2.2.2. srd 
  
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

### 2.2.3. srd session code blocks 

- resumo do srd: selected logic map maps review rules   
- resumo do control map + tag system 
- selected code blocks 

### 2.2.4. plano 

- plano integral: etapas 
- plano etapa, todo 
- control maps 
  - plan map 
  - **code map**: [files, classes, métodos] x [funções negócio] = tags [pendencia, maturidade] 
    - pendencia: [novo, refatorar, manter, eliminar] 
    - maturidade: [descrições, code block, quality, test] 
  - **data process map**: [files, classes, métodos] x [data blocks] = tags [pendencia, maturidade] 

### 2.2.5. code, code-review, test 

## 2.3. docs inteligência 

### 2.3.1. regras e templates  

#### 2.3.1.1. project documents rules  
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

# 3. documentos de sessão 

## 3.1. session: AGENTS.md 

- objetivo, contexto [prd], entregas 
- referencias: agents 
## 3.2. agent: session-planner 

- session-plan-init-investigate  
- session-plan-init-structure 
- session-plan-init-review 
- session-plan-init-publish 
- session-plan-update 
- session-plan-finish 

## 3.3. agent: project-planner 

- skills 
  - project-prd 
  - project-srd 
  - project-plan-steps  
  - project-plan-map 
  - project-plan-code-map 

## 3.4. agent: code-planner 

## 3.5. agent: code-reviewer 

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




# 4. instruções gerais

## 4.1. formatação 
## 4.2. Legenda de Tags

### 4.2.1. versao atual

| Tag   | Significado                                                     | Regra de consistência                                                                                           |
| ----- | --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `[1]` | **Novo** — classe/método que será criado                        | Deve existir em `classe nova` com `metodo novo` preenchido                                                      |
| `[2]` | **Refatorar** — método existente que muda de script/classe/nome | `script novo` e `classe nova` devem refletir o destino final. `metodo novo` opcional se só mudar de classe      |
| `[3]` | **Manter** — fica como está, sem alteração                      | `script novo` = `script atual`. `classe nova` = `subsection atual` (se aplicável). `metodo novo` = `item atual` |
| `[4]` | **Descartar** — será removido                                   | `script novo` e `classe nova` vazios. Nenhuma referência no novo código                                         |

### 4.2.2. versao nova

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

## 4.3. instruções de Consistência

### 4.3.1. Verificação Cruzada

Para verificar a tabela CSV, aplicar estas instruções:

| #   | Regra                                                                                                                    | Como verificar                                          |
| --- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------- |
| 1   | Todo `[1]` novo deve ter `classe nova` e `metodo novo` preenchidos                                                       | Filtrar tag=`[1]`, checar se campos não vazios          |
| 2   | Todo `[2]` refatorar deve ter `script novo` diferente do `script atual` OU `classe nova` diferente de `subsection atual` | Filtrar tag=`[2]`, checar se pelo menos um campo difere |
| 3   | Todo `[3]` manter deve ter `script novo` = `script atual`                                                                | Filtrar tag=`[3]`, checar igualdade                     |
| 4   | Todo `[4]` descartar deve ter `script novo` e `classe nova` vazios                                                       | Filtrar tag=`[4]`, checar campos vazios                 |
| 5   | `metodo novo` deve ser único dentro de cada `classe nova`                                                                | Agrupar por classe nova, checar duplicatas              |
| 6   | Nenhum `metodo novo` deve ter nome de classe reservada (`class`)                                                         | Checar se "class" aparece como nome de método           |

### 4.3.2. Verificação de Pipeline

| Etapa | Entrada               | Classe             | Saída                   |
| ----- | --------------------- | ------------------ | ----------------------- |
| 1     | Diretório de assets   | `BuildAssets`      | `List<AssetsContent>`   |
| 2     | `List<AssetsContent>` | `BuildPostConfig`  | `List<Map post_config>` |
| 3     | `Map post_config`     | `BuildPostContent` | `Map post_content`      |
| 4     | `Map post_content`    | `BuildPayload`     | `PostContent` (Dart)    |

Cada classe recebe o que a anterior produziu — sem saltos, sem dependências circulares.

### 4.3.3. O que será eliminado

| Arquivo                                           | Destino                                                                                                   |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `src/scripts/post_builder.dart`                   | Eliminado (imports migrados)                                                                              |
| `src/scripts/publish/post_builder_facebook.dart`  | Métodos `resolveContent` e `_textFrom` movidos; `fillPostContentTextFields` e `_textFieldFor` descartados |
| `src/scripts/publish/post_builder_instagram.dart` | `resolveContent` movido; `fillPostContentFields` descartado                                               |

# 5. instruções especificas por documento

## 5.1. instruções documento PRD
prd

## 5.2. instruções documento SRD

### 5.2.1. Sobre este documento

### 5.2.2. arquitetura de funções

#### 5.2.2.1. funções de negócio
sem instruções

#### 5.2.2.2. funções de automação

### 5.2.3. arquitetura de dados

### 5.2.4. descrições funcionais

## 5.3. instruções documento session plan
session plan

# 6. aplicação

## 6.1. PRD

| doc\ modelos                                                | template | herança | instruções gerais | instruções especificas |
| ----------------------------------------------------------- | :------: | :-----: | :---------------: | :--------------------: |
| PRD                                                         |          |         |                   |                        |
| PRD sobre este documento                                    |          |    x    |                   |                        |
| PRD contexto do projeto                                     |    x     |         |                   |                        |
| PRD logica funcional                                        |    x     |         |                   |                        |
| PRD funções de negócio                                      |    x     |         |                   |                        |
| PRD modelos de dados                                        |    x     |         |                   |                        |

## 6.2. SRD

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
| SRD arquitetura de dados, instruções e resumo                                   |          |         |                   |                        |
| SRD arquitetura de dados, instruções e resumo, instruções                       |          |    x    |                   |                        |
| SRD arquitetura de dados, instruções e resumo, resumo                           |    x     |         |                   |                        |
| SRD descrições funcionais                                                         |    x     |         |                   |                        |

como os modelos são aplicados nos documentos:
- templates: formatos fixos, conteudo editável com base nas instruções gerais ou especificas
- herança: conteúdo não editáve, herdado de outro documento
- instruções*: conteúdo não editável
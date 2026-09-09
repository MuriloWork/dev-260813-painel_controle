**260613_painel_controle_prd_00**

# 1. Sobre este documento 

## 1.1. resumo
Este documento analisa o **modelo SRD** (Especificação de Requisitos de Desenvolvimento), documento nº 2 da tríade PRD → SRD → Plano de Execução.

## 1.2. instruções

### 1.2.1. instruções gerais
Cada seção abaixo corresponde a uma seção do SRD e contém:
- **Propósito**: o que a seção representa no modelo
- **Instrução de preenchimento**: o que o autor deve descrever em cada parte

### 1.2.2. instruções especificas
- conteudo não editável
  - todas as seções de instruções
  - estrutura (seções, subseções, titulos) das seções [arquitetura de funções,arquitetura de dados]
    - formato
- seções editáveis

# 2. contexto do projeto 

## 2.1. resumo e objetivos 

- crm para venda de produtos afiliados 
- gerenciamento de redes sociais 
- produção de [pesquisas, postagens, mensagens]

## 2.2. arquitetura (caminhos relativos a project_path) 

- stack
  - scripts: dart, python, ps1, sqlite, api
  - UI: flutter windows, flutter web, powershell
- project_path: `C:\Users\muril\OneDrive\01 mycloud\01 sistMu\10.01 scripts\01_root\main\260511_meta_api`
- aplicativo
  - scripts
    - configurações
    - models 
  - data (dados de negocio): 
  - assets (conteudos das publicações): 

## 2.3. documentos de referência (caminhos relativos a project_path) 

- plano: `sessions\260512_meta_api`
  - PRD (este documento): `sessions\260530_meta_api_organize\260606_meta_api_prd_00.md`
  - doc rules (procedimentos de gestão de documentos): `sessions\260530_meta_api_organize\260606_meta_api_rules_00.md`
  - SRD (documento base das especificações detalhadas): `sessions\260530_meta_api_organize\260606_meta_api_srd_00.md`
  - plano de execução: `sessions\260530_meta_api_organize\260606_meta_api_plan_00.md` 
- documentos tecnicos  
  - meta api: `sessions\260512_meta_api\meta_api_docs`

# 3. logica funcional 
Explica como funciona a hierarquia das seções e listas nas proximas seções.
- funções
- modelos de dados  
- legenda: status implementação  
	- 🟢 finalizado  
	- 🔵 funcionando, falta organizar e testar consistencia  
	- 🟤 implementação script iniciada  
	- 🟡 code blocks definidos e revisados  
	- 🟠 descrição funcional definida e revisada  
	- ⚪️ descrição funcional não iniciada ou parcial  

# 4. analise arquitetura atual

## 4.1. root/
- .env.base
### 4.1.1. main/
- files
  - requirements-base.txt
  - requirements-projeto.txt
  - painel_controle_config.json
  - painel_controle.ps1

#### 4.1.1.1. projeto/dev/
- .env.projeto
- client_secret.json

##### 4.1.1.1.1. config/
- files
  - 260417_google_api_people_get.ps1
  - 260417_google_api_people_get.py
  - client_secret.json
  - google_oauth_tokens.json
  - service_account.json

##### 4.1.1.1.2. painel/
- files
  - requirements-projeto.txt
  - painel_controle.bat
  - painel_controle.ps1
  - painel_tkinter.py

###### 4.1.1.1.2.1. config
- ast_func_1d.json
- ast_func_2d.json
- logs_string.json
- logs_tag_map_modelo.json
- set_process_targets.json
- set_shell_targets.json

###### 4.1.1.1.2.2. logs
- logs_dart.py
- analyze_logs.py

####### 1.1.2.2.1. logs.json

###### 4.1.1.1.2.3. parse
- convert_pdf_to_md.py
- list_exposed_schemas.dart
- normalize_md.ts
- painel_sqlite_export.py
- painel_sqlite_import.py
- parse_dart_ast.dart
- parse_dart_ast.py
- parse_dart_raw.py
- parse_model_pydantic.py
- parse_xls.py
- pubspec.yaml
- test_parse_md_ast.py
- validate_schema.dart

###### 4.1.1.1.2.4. utils
- parse_utils.py
- heaper.ps1
- painel_files.py
- painel_settings.py
##### 4.1.1.1.3. parse/ (json)
##### 4.1.1.1.4. sqlite/ (sql)
##### 4.1.1.1.5. supabase/ (sql)

#### 4.1.1.2. dbMu/
- files
  - eventos.db
  - financeiro.db

##### 4.1.1.2.1. bases sistMuFileHandling
##### 4.1.1.2.2. bases_cadastros
##### 4.1.1.2.3. bases_eventos
##### 4.1.1.2.4. bases_sistMuFin
##### 4.1.1.2.5. supabase_251113_sistMuFin

#### 4.1.1.3. src/
##### 4.1.1.3.1. joplin_plugin/
###### 4.1.1.3.1.1. joplin_plugin_muSync
###### 4.1.1.3.1.2. joplin_plugin_muToc
##### 4.1.1.3.2. py_geral/
- z02_funcPy04trsf_json.py
- z02_funcPy01api_handling.py
- z02_funcPy02doc_handling.py

##### 4.1.1.3.3. py_nicegui/
##### 4.1.1.3.4. py_sync/
###### 4.1.1.3.4.1. syncSqliteTrello
###### 4.1.1.3.4.2. syncSqliteExcel
##### 4.1.1.3.5. pydantic_models/
- pydanticEventos.py

##### 4.1.1.3.6. sql_supabase/
- sync_excel_financeiro.py
- eventos_financeiro_attach.sql
- eventos_financeiro_categorias.sql
- run_sql_supabase.py

# 5. arquitetura nova

## 5.1. main/projeto/dev (= main para `painel` em desenvolvimento)
### 5.1.1. camada dados
#### 5.1.1.1. dbMu/
- files
  - parse_dart.db
  - parse_md.db
#### 5.1.1.2. doc_painel/
### 5.1.2. camada frontend
#### 5.1.2.1. src/view_shell/
### 5.1.3. camada backend
#### 5.1.3.1. src/controllers/
#### 5.1.3.2. src/services/
##### 5.1.3.2.1. src/services/~~painel_settings~~painel_init.py
##### 5.1.3.2.2. src/services/parse
##### 5.1.3.2.3. src/services/logs
##### 5.1.3.2.4. src/services/dart_tools
#### 5.1.3.3. src/utils_io/
#### 5.1.3.4. src/sql_sqlite/
##### 5.1.3.4.1. src/sql_sqlite/sql_parse_md
##### 5.1.3.4.2. src/sql_sqlite/sql_tkinter
##### 5.1.3.4.3. src/sql_sqlite/sql_parse_script
#### 5.1.3.5. src/sql_supabase/
#### 5.1.3.6. src/models/
##### 5.1.3.6.1. src/models/schemas
#### 5.1.3.7. src/~~config~~ repositories/
##### 5.1.3.7.1. src/config/schemas
##### 5.1.3.7.2. src/~~utils_auth~~/auth_data*.json
#### 5.1.3.8. src/temp
## 5.2. main/
### 5.2.1. dbMu/
- files
  - eventos.db
  - financeiro.db
  - parse_dart.db
  - parse_md.db
### 5.2.2. doc_eventos/
### 5.2.3. doc_painel/
### 5.2.4. src/ 
#### 5.2.4.1. eventos/
##### 5.2.4.1.1. config/
##### 5.2.4.1.2. models/
##### 5.2.4.1.3. services/
#### 5.2.4.2. painel/
##### 5.2.4.2.1. config/
##### 5.2.4.2.2. models/
##### 5.2.4.2.3. services/
#### 5.2.4.3. utils_auth/
#### 5.2.4.4. sql_sqlite/
#### 5.2.4.5. sql_supabase/
#### 5.2.4.6. joplin_plugins/
##### 5.2.4.6.1. joplin_plugin_muSync/
##### 5.2.4.6.2. joplin_plugin_muToc/
#### 5.2.4.7. vscode_plugins/



# 6. funções de negócio

## 6.1. resumo

- agents prompts
  - init [project, session] 
  - edit [srd, session plan, code block] 
  - review [code doc]
- agents scripts
  - parse + sync: md doc
    - md  → json →  sqlite
    - md  ↔  json
    - md  ↔  joplin  
  - parse + sync: code doc
    - [dart, python] ast  →  json  →  sqlite  
    - [dart, python] raw  →  json  →  sqlite  
    - sqlite  ↔  csv  ↔  xlsx
  - project planner:
    - md doc: [ruĺes, prd, template_srd]  →  srd 
    - fluxos: criação, controle, revisão
- sync 
- logs 
- shell 

## 6.2. ⚪️ funções comuns 
- inteligentes
  - interpretar com base nos conteudos [texto, lista]
    - logica funcional aplicada a [seções do documento, hierarquia funcional]
    - hierarquia funcional  
    - status de implementação
  - resumir conteudos
  - verificar a aderencia dos modelos [md, json]
- automaticas
  - aplicar hierarquia funcional com base nos modelos de dados

## 6.3. ⚪️ md doc 
### 6.3.1. prd 

- funções de negócio 
- stack 
	- scripts: dart, python, ps1, sqlite, api  
	- UI: flutter, web, shell 
- referências: docs 

### 6.3.2. project documents rules  

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

### 6.3.3. srd 
  
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
	- [arquitetura funções invocação] x [arquitetura funções implementação] = [descrições]
	- [arquitetura funções] x [arquitetura dados] = [descrições]

### 6.3.4. plano 
- plano integral: etapas 
- plano etapa, todo 
- control maps 
  - plan map 
  - **code map**: [files, classes, métodos] x [funções negócio] = tags [pendencia, maturidade] 
    - pendencia: [novo, refatorar, manter, eliminar] 
    - maturidade: [descrições, code block, quality, test] 
  - **data process map**: [files, classes, métodos] x [data blocks] = tags [pendencia, maturidade] 

## 6.4. ⚪️ code doc 

### 6.4.1. srd code blocks  
- resumo do srd: selected logic map maps review rules   
- resumo do control map + tag system 
- code blocks  

### 6.4.2. srd session code blocks   
- resumo do srd: selected logic map maps review rules   
- resumo do control map + tag system 
- selected code blocks 

### 6.4.3. code, code-review, test

## 6.5. ⚪️ sync doc 
Transformações entre os modelos de dados.

# 7. modelos de dados 
## 7.1. resumo
## 7.2. md doc [md, json, joplin]
### 7.2.1. PRD, SRD, plano
## 7.3. code doc [md, json, sqlite]
### 7.3.1. code blocks, control maps

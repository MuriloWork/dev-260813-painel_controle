# 1. contexto do projeto

## 1.1. resumo e objetivos

- crm para venda de produtos afiliados 
- gerenciamento de redes sociais 
- produção de [pesquisas, postagens, mensagens]

## 1.2. arquitetura (caminhos relativos a project_path)

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

## 1.3. documentos de referência (caminhos relativos a project_path)

- plano: `sessions\260512_meta_api`
  - PRD (este documento): `sessions\260530_meta_api_organize\260606_meta_api_prd_00.md`
  - doc rules (procedimentos de gestão de documentos): `sessions\260530_meta_api_organize\260606_meta_api_rules_00.md`
  - SRD (documento base das especificações detalhadas): `sessions\260530_meta_api_organize\260606_meta_api_srd_00.md`
  - plano de execução: `sessions\260530_meta_api_organize\260606_meta_api_plan_00.md` 
- documentos tecnicos  
  - meta api: `sessions\260512_meta_api\meta_api_docs`

# 2. funções de negócio

## 2.1. resumo 

- funções  
	- 🔷 adm postagens: [build, schedule, publish]
	- 🔷 adm assets: [site, docs, midia] 
	- 🔷 adm comércio: [research, qualificação, cadastro] 
	  - produtos
	- adm mensagens 
		- ❎ summary view 
		- 🔷 msg (diretas, respostas) build 
	- adm contatos 
		- ❎ full view 
		- 🌈 leads edit 
		- 🔷 master edit 
	- ❎ performance view 
	- adm de dados 
- legenda 
  - UI
  	- 🔷 crm_cdd: win → web → mobile
  	- 🌈 google 
  	- ❎ excel 
  - status implementação  
  	- 🟢 finalizado  
  	- 🔵 funcionando, falta organizar e testar consistencia  
  	- 🟤 implementação script iniciada  
  	- 🟡 code blocks definidos e revisados  
  	- 🟠 descrição funcional definida e revisada  
  	- ⚪️ descrição funcional não iniciada ou parcial  

## 2.2. 🟠 adm postagens: [build, schedule, publish] 

- build 
	- models 
		- markdown, json 
		- FB, IG, TT [story, reel, feed] 
		- YT 
	- prompts 
- schedule 
	- basic 
		- folders [FB stories, FB reels, FB feed, IG stories, IG reels, IG feed]
		- files: timestamp-titulo.md 
		- post model builder v1 
	- planner 
		- asset tree 
		- post schedule  
			- schedule pattern, intervalo 
			- metadata: tema, canal, funil  
			- post model builder v2 
		- calendar view  
	- tracker 
- publish 
	- ✅ post model 
	- blog, TT, YT
	- ✅ FB, IG 
- post service post 
	- `[02 ConfigService]` env, auth, config 
	- post builder 
		- assets --> post config 
		- post config --> post content 
		- post content --> payload 
- post service post OLD 
	- `[01]` main 
	- `[02 ConfigService]` env, auth, config 
	- `[03]` get model 
	- `[04 PostModelService]` process data to model 
	- `[05 PublishService]` publish prepare 
	- `[09 TunnelService]` _startLocalServerAndTunnel 
	- `[06 ApiClient]` publish request 
	- `[07 ValidationService]` confirm, validate, error treatment 
	- `[08 ResponseHelper]` process response
	- `[10]` interno 
- draft  
	- main
		- runJsonModelTest
			- loadEnv
			- loadConfig
			- getPageAccessToken
			- loadJsonModel
			- getInstagramUserId
			- processIgPostModel
				- _fillPostContentIgFields
				- _startLocalServerAndTunnel
	      - post_builder.resolveIgPostType
				- processIgPost
			- processPostModel
				- updatePostModelWithFilledFields
				- processPost
					- apiPost  [interno]
			- updatePostModelWithResult
			- validateIgPost
			- validatePost
			- updatePostModelWithError
	- internos 
		- igPublish [interno]
			- igApiPost
		- _processThreeStep
	  	- _logPayload
	  	- _uploadFileToUrl
	  	- _apiPostQuery
		- _buildIgPermalink
		- _buildPermalink
		- _fillPostContentTextFields
		- _generateNotes
		- _getBodyFromSource
		- _getTitleFromSource
		- _igUploadToRuplad
		- _processIgContainer
		- _processIgResumable
		- _processResumable
		- _processTwoStep
		- _trunc
		- _validateSchedule
	- post_builder
	  - _buildFinishParams
	  - _resolveText
	  - _toUnix
	  - FeedPostType
	  - IgImagePostType
	  - IgReelsPostType
	  - IgStoryPostType
	  - ImageContent
	  - PostContent
	  - PostType
	  - ReelsPostType
	  - resolveContent
	  - resolvePostType
	  - StoryPostType
	  - TextContent
	  - VideoContent
- adm assets: [site, docs, midia] 
  - mapeamento background
    - `scripts\contents_service.dart`  --> assets_service
- adm comércio: [research, qualificação, cadastro] 
- performance view 
- adm mensagens 
- adm contatos 



## 2.3. ⚪️ adm assets 

- asset tree 
	- list view, draggable 
	- card view 
	- metadata edit 
		- tipo [texto, imagem, video]
			- readiness [raw, draft, ready, published]
				- tema.(win prop "titulo"): [[260507 funnel web#2.2. temas|lista]] 
					- canal (win prop "marcas/tags"): [blog, fb_feed, fb_reel, fb_stories, ig_feed, ig_reel, ig_stories, youtube] 
						- funil (win prop "marcas/tags"): [prospecção , atração , oferta, compra] 
- sync  

## 2.4. ⚪️ performance view 

- postagens 
- conversão 
- vendas 

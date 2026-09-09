**DEV WORKFLOW**  

# 1. sessions 

## 1.1. AGENTS.md 

- objetivo, contexto [prd], entregas 
- referencias: agents 

# 2. projects 

## 2.1. prd 

- funções de negócio 
- stack 
	- scripts: dart, python, ps1, sqlite, api  
	- UI: flutter, web, shell 
- referências: docs 

## 2.2. project documents rules  

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

## 2.3. srd 
  
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

## 2.4. srd session code blocks 

- resumo do srd: selected logic map maps review rules   
- resumo do control map + tag system 
- selected code blocks 

## 2.5. plano 

- plano integral: etapas 
- plano etapa, todo 
- control maps 
  - plan map 
  - **code map**: [files, classes, métodos] x [funções negócio] = tags [pendencia, maturidade] 
    - pendencia: [novo, refatorar, manter, eliminar] 
    - maturidade: [descrições, code block, quality, test] 
  - **data process map**: [files, classes, métodos] x [data blocks] = tags [pendencia, maturidade] 

## 2.6. code, code-review, test 

# 3. agents 

## 3.1. session-planner 

- session-plan-init-investigate  
- session-plan-init-structure 
- session-plan-init-review 
- session-plan-init-publish 
- session-plan-update 
- session-plan-finish 

## 3.2. project-planner 

- skills 
  - project-prd 
  - project-srd 
  - project-plan-steps  
  - project-plan-map 
  - project-plan-code-map 

## 3.3. code-planner 

## 3.4. code-reviewer 

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


```toml
[tab]
abc = 1
dgh = "cvbnk"
```  

# 4. harness + skills

Exatamente! Você pegou o conceito central. A persistência (ou não) dos dados no contexto é uma decisão puramente do **harness** (a infraestrutura de código que envelopa o LLM).

No caso do **OpenCode**, o ecossistema lida com isso de forma muito inteligente e estruturada através de ferramentas nativas e plugins de compactação/memória.

O ecossistema do OpenCode gerencia o ciclo de vida das skills e o contexto da seguinte forma:

---

## 4.1. O Carregamento NATIVO de Skills no OpenCode

O OpenCode possui uma ferramenta nativa chamada explicitamente **`skill`**.
As suas habilidades personalizadas ficam salvas em arquivos `SKILL.md` (dentro de diretórios como `.opencode/skills/nome-da-skill/`).

O fluxo de contexto que ele faz segue esta lógica:

* **No início da sessão:** O OpenCode injeta no System Prompt apenas a tag `<available_skills>` contendo o `name` e a `description` de cada skill cadastrada. O conteúdo interno do markdown **não** entra no contexto ainda.
* **A Invocação:** Quando o agente precisa daquela habilidade, ele executa a ferramenta: `skill(name="minha-skill")`.
* **O Impacto no Contexto:** O OpenCode lê o arquivo `SKILL.md` e joga o texto completo dele **para dentro da janela de conversa** como o retorno da ferramenta.

---

## 4.2. Como o OpenCode evita o estouro do contexto após usar a Skill?

Se o agente ler três ou quatro arquivos `SKILL.md` densos, a janela de contexto começaria a pesar. Para mitigar isso, o OpenCode utiliza duas frentes (nativas e via plugins):

### 4.2.1. A. Isolamento via Sub-agentes (Nativo)

O OpenCode frequentemente delega tarefas pesadas que exigem habilidades específicas para **Sub-agentes** (como os sub-agentes embutidos *General*, *Explore* ou *Scout*).

* Quando o agente principal spawna um sub-agente para aplicar uma skill, esse sub-agente roda em uma **chamada de API paralela e isolada**, com sua própria janela de contexto.
* Quando o sub-agente termina de processar a skill, ele devolve apenas um resumo ou o resultado final para o agente principal através de troca de mensagens. As instruções brutas da skill morrem junto com o contexto descartado do sub-agente.

### 4.2.2. B. O Mecanismo de Compactação (Context Window Compaction)

Para sessões longas no terminal, o OpenCode possui uma rotina de **Compaction** (Compactação). Quando a conversa fica ociosa (*idle*) ou atinge um limite crítico de tokens, o harness do OpenCode passa uma "poda" no histórico:

* Ele remove os retornos brutos e gigantescos de ferramentas (como o conteúdo completo de um arquivo lido ou de uma skill carregada passos atrás).
* Ele mantém apenas os turnos essenciais da conversa (as instruções finais e o estado atual do código).

### 4.2.3. C. Integração com Plugins de Memória Longa (ex: Hindsight / Agent-Memory)

Em implementações mais robustas do OpenCode, utilizam-se plugins como o `hindsight` ou `opencode-agent-memory` (baseado no padrão do Letta).

Esses componentes alteram drasticamente o jogo:

1. O plugin intercepta a conversa a cada $N$ turnos (`retainEveryNTurns`).
2. Ele extrai os aprendizados e o resultado do uso daquela skill.
3. Ele joga fora o log pesado da execução da ferramenta do contexto atual e salva o aprendizado em um banco SQLite local (Durable Objects) ou arquivos markdown de memória (`.opencode/memory/`).
4. Se o agente precisar daquele conhecimento de novo, ele usa ferramentas de recordação (`hindsight_recall`) para trazer apenas o pedaço estritamente necessário de volta.

---

### 4.2.4. Resumo

No **OpenCode**, o conteúdo de um `SKILL.md` entra por completo no contexto do chat no momento em que a ferramenta `skill` é chamada. Porém, ele não fica lá para sempre gerando "gordura": o OpenCode limpa essa janela através de **sub-agentes isolados** (para a skill não poluir o fluxo principal) ou através de rotinas automáticas de **compactação de contexto** quando o terminal fica ocioso.


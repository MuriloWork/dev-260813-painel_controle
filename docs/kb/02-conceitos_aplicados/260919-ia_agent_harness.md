[[260909-ia_handbook]]

# 1. memory 

- **memoria prospectiva** = controle de execução de tarefas futuras
- **working memory**
	- **memoria semantica** = AGENTS.md, verdade, fatos úteis 
	- **memoria episodica** = o que aconteceu, historico, cross-task transfer 
	- **memoria procedimental** = `agent/<agent_name>` + SKILL.md, regras 
	- **retrieval - memoria de longo prazo** = memory governance (long-term retrieval planning and memory control)
	- **memoria parametrica** = original do model LLM 
- ++ Multi-Agent Memory 
- ++ Context Compaction and State Offloading

# 2. context 
- context architecture (hierarchy,  layers) 
	- harness context (global)
		- project context 
			- project [front, block, subject, subdomain] context 
				- session context 
					- prompt cache 
					- working memory
		- ~~assets~~ 

## 2.1. context layer: harness
### 2.1.1. opencode.json 
### 2.1.2. AGENTS.md 
## 2.2. context layer: project
opencodeignore 
### 2.2.1. opencode.json 
instructions, references, worktrees 
### 2.2.2. AGENTS.md 
## 2.3. context layer: project [front, block, subject, subdomain]
## 2.4. context layer: session 

### 2.4.1. prompt cache
por model provider: 
- mecanismo de disparo [manual, automatico]
- persistencia (no intervalo entre requests) = [5 min, 1 hora]

# 3. agents + skills

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

## 3.3. code-reviewer 

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


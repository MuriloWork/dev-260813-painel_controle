---
name: session-plan-finish
description: Encerra a sessão gerando resumo de entregas e, se necessário, o briefing da próxima sessão
license: MIT
compatibility: opencode
metadata:
  audience: session-planner
  workflow: session-end
---

## Propósito
Consolidar o que foi produzido na sessão e preparar o terreno para a continuidade do trabalho.

## Fluxo

### 1. Levantar Entregas da Sessão
Percorrer os arquivos modificados/criados, comparar com a versão inicial {base_scripts_dir} e organizar em categorias:

- **Scripts criados/alterados:**
	- Caminho completo
	- Breve descrição do propósito
- **Classes criadas/alteradas:**
	- Nome da classe
	- Caminho do arquivo
	- Responsabilidade principal
- **Métodos/funções criados/alterados:**
	- Nome do método/função
	- Classe/arquivo
	- O que faz (1 linha)
- **Lógicas/Regras de negócio implementadas:**
	- Descrição da regra
	- Onde foi aplicada
- **Documentos atualizados:**
	- AGENTS.md (briefing)
	- Planos (novas versões)
	- Outros (README, docs, etc.)

### 2. Documento A — ultima versao do plano
Criar `{plan_dir}/{data}_plan_{session_name}_{last_version_number+1}.md` com:

- confirmar finalização da sessao com o usuario 
- ler conteúdo integral da última versão 
- criar nova versao do plano, usando `plan_dir` e `plan_pattern`(incrementar o número de versão) apenas com a seção "projeto" e as suas subseções retratando o estado final do projeto, suas funções de negocio, scripts, classes e métodos. 

### 3. Documento B — Briefing da Próxima Sessão (se aplicável)
Criar `{plan_dir}/{data}_{plan_name}_00.md` com:
```
# Preparação para Próxima Sessão

## Pendências
- {itens não concluídos}

## Próximo Passo Lógico
- {o que fazer a seguir}

## Recomendação de Foco
- {qual parte do projeto abordar}

## Arquivos Relevantes
- {caminhos para consultar}
```

Se o próximo passo for óbvio e imediato, pode apenas registrar como seção no próprio resumo ao invés de criar arquivo separado.

### 4. Limpeza do Briefing
- Remover a seção `## Briefing da Sessão Atual` no `{briefing_file}`
- Se houver próxima sessão agendada, deixar apenas nota `## Briefing da Sessão Atual\n<!-- Próxima sessão preparada em {data}_{plan_name}_00.md -->`

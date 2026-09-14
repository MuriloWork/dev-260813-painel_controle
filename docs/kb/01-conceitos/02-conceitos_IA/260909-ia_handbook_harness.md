**IA HARNESS**  

# 1. harness + agents

## 1.1. caso de uso: Code Review Agent Harness

Um **code review agent harness** (infraestrutura/suporte de agente para revisão de código) é o andaime técnico construído ao redor de um modelo de Inteligência Artificial. Ele gerencia suas ferramentas, memória, restrições e o ciclo de execução. Essa estrutura transforma um modelo de linguagem isolado em um sistema autônomo capaz de analisar e revisar Pull Requests (PRs) de forma inteligente.

Uma arquitetura padrão de harness divide o fluxo de trabalho do agente em três fases essenciais:

- **Loop** do Agente e Ferramentas baseado no padrão ReAct (Reasoning and Acting). O harness entrega as alterações de código para a IA e disponibiliza interfaces de ferramentas específicas:
	* **Gerenciamento de Contexto:** O harness filtra rigorosamente o que entra na janela de contexto do modelo para evitar a degradação do raciocínio.
	* **Determinismo vs. Flexibilidade:** Garante que a IA siga caminhos estritos. O modelo tem liberdade para julgar o código, mas os limites do que ele pode aprovar ou alterar são rigidamente codificados.
- **Sensores e Verificação** para avaliar as alterações, capturar erros de lógica e validar o comportamento do agente antes que qualquer humano veja a revisão:
	* **Sensores Determinísticos:** Ferramentas de análise estática (linters), checklists de segurança (como OWASP Top 10) e scanners de vulnerabilidades rodam de forma independente da IA.
	* **Sensores Inferenciais:** Um segundo LLM pode atuar como "supervisor" para checar a lógica do agente revisor principal, ou um agente adversário pode ser usado para encontrar falhas nas sugestões.
	* **Validação por Testes:** O harness força o agente a escrever e executar testes unitários para provar que suas sugestões de refatoração realmente funcionam.
- Mecanismos de Controle e Pós-Processamento
O harness governa as permissões do agente, define orçamentos de consumo de tokens (evitando loops infinitos de alucinação) e formata a saída em comentários estruturados:
	* **Automação de CI/CD:** Gatilhos disparam a revisão assim que um PR é aberto ou atualizado, publicando os comentários da IA diretamente na plataforma de Git (GitHub, GitLab, Harness Code).
	* **Iteração Contínua:** Se um erro é detectado no próprio raciocínio da IA, o harness descarta a saída, ajusta o prompt e força o agente a reiniciar a análise por outro ângulo.


## 1.2. design patterns

Se o objetivo é criar um harness reutilizável para vários projetos, a combinação **Facade + Factory + Builder + Strategy + Dependency Injection** costuma ser a mais comum e escalável. Os demais padrões entram para funcionalidades específicas, como observabilidade, gerenciamento de estado e integração com ferramentas. 
Na prática, uma arquitetura típica fica assim:

```mermaid
AgentHarness (Facade)
│
├── AgentFactory
│
├── AgentBuilder
│      ├── LLM (Strategy)
│      ├── Prompt (Strategy)
│      ├── Tools (Command)
│      ├── Memory (State)
│      └── Callbacks (Observer)
│
└── AgentExecutor
```
Patterns mais usados em projetos com LangChain:

| Pattern                        | Uso no LangChain                                   | Frequência |
| ------------------------------ | -------------------------------------------------- | ---------- |
| ==Strategy==                   | Trocar LLM, prompts, ferramentas e políticas       | Muito alta |
| ==Factory== / Abstract Factory | Criar agentes, modelos e ferramentas               | Muito alta |
| Builder                        | Construir pipelines e agentes complexos            | Muito alta |
| Dependency Injection           | Injetar LLM, memória, tools, callbacks             | Muito alta |
| Chain of Responsibility        | Encadear etapas de processamento                   | Muito alta |
| ==Command==                    | Representar chamadas de ferramentas (Tool Calling) | Alta       |
| Template Method                | Fluxo fixo com etapas customizáveis                | Alta       |
| Adapter                        | Integrar APIs e bibliotecas externas               | Alta       |
| Facade                         | Esconder a complexidade do LangChain               | Alta       |
| ==Observer==                   | Logging, tracing, callbacks, streaming             | Alta       |
| ==State==                      | Conversação e estado do agente                     | Média      |
| Composite                      | Agrupar tools e chains                             | Média      |
| Decorator                      | Retry, cache, métricas, logging                    | Média      |

Para um Agent Harness moderno (especialmente com LangGraph/LangChain), a arquitetura costuma combinar:
- Factory → cria agentes.
- Builder → monta o agente.
- Strategy → escolhe modelo, prompt e ferramentas.
- Dependency Injection → fornece dependências.
- Facade → expõe uma API simples (`AgentHarness.run()`).
- Observer → callbacks, tracing e logs.
- State → controla contexto e memória.
- Command → execução das ferramentas.

## 1.3. Harness Interface: Code for Reasoning, Acting, and Environment Modeling

**Executability** means the harness can verify what the model intended. 
**Inspectability** means failures can be diagnosed and fed back. 
**Statefulness** means the agent’s interaction history is not lost between steps.

## 1.4. Harness Mechanisms: Planning, Memory, Tool Use, Control, and Optimization

**Planning** organizes long-horizon task execution by externalizing goals into decompositions, structural constraints, search trajectories, or workflow-level orchestration. 
**Memory** and context engineering manage mutable state across long interactions by preserving working context, retrieving repository evidence, storing reusable experience, supporting shared histories, and offloading state beyond the active context window. 
**Tool usage** connects the agent to governed executable interfaces, including APIs, repositories, terminals, sandboxes, verification tools, and workflow orchestrators. 
Harness **control** through the Plan-Execute-Verify loop reframes feedback-guided debugging as a broader control process: plans form contracts over intended changes, execution applies them inside sandboxed and permissioned environments, and verification uses deterministic sensors and human-review gates to decide whether the state should be accepted, revised, escalated, or rolled back. 
**Optimization**. Agentic harness engineering studies how the harness itself can be measured and improved through deep telemetry, evolution agents, replay-based evaluation, and governed harness mutation.

### 1.4.1. [[260629 Code as Agent Harness Toward Executable, Verifiable, and Stateful Agent Systems#3.2. Memory and Context Engineering for Agent Harness|Memory and Context Engineering for Agent Harness]]
#### 1.4.1.1. resumo
[YT - jamwithai](https://youtu.be/bK1clrG-boc?is=M_MtSUgc3cYXQGQ4)
![[260909-ia_handbook_harness_memory-03.jpg]]

- **working memory**
- **memoria semantica** = AGENTS.md, verdade, fatos úteis 
- **memoria procedimental** = SKILL.md, regras 
- **memoria episodica** = o que aconteceu, historico, cross-task transfer 
- **retrieval - memoria de longo prazo** = memory governance (long-term retrieval planning and memory control)
- **memoria parametrica** = original do model LLM 
- ++ Multi-Agent Memory 
- ++ Context Compaction and State Offloading

#### 1.4.1.2. working memory

![[260909-ia_handbook_harness_memory-04.jpg]]



#### 1.4.1.3. prompt/memory cache

[YT - prompt caching explained](https://youtu.be/SkM4k4SKvCM?is=sw2KgQAox8BSB0bG)


#### 1.4.1.4. generalidades
[caso de uso - YT AlmaBrain - acionabilidade](https://youtu.be/vF8YZiLsl2Q?is=d8_Nrlo78vr4cSx5)
- projetos
- memori[IA]
	- governantes 
	- cronos 
	- estado da mente 
- áreas = rotinas
- recursos 
- inbox 
- arquivado 

![[260909-ia_handbook_harness_memory-02.jpg]]

[YT - mem0](https://youtu.be/aYfZN8t6AQs?is=ISEaROfbpn7tZLzI)
- Ingestão 

![[260909-ia_handbook_harness_memory-01.jpg]]



## 1.5. Scaling the Harness: Multi-Agent Orchestration over Code

**Limitations for single-agent** emerge: (1) context window constraints prevent a single agent from holding an entire codebase, long interaction history, and execution trace in working memory; (2) specialization requirements make it inefficient to use one generalist agent for planning, synthesis, testing, review, and debugging simultaneously; and (3) the absence of independent coordination and verification channels prevents the agent from reliably detecting and correcting its own errors during long-horizon execution. 
Multi-agent systems introduce a powerful **principle**: once these responsibilities are distributed across specialized roles, the agent harness itself becomes more **modular, inspectable, and adaptable**. Early systems such as ChatDev \[Qian2023ChatDev\], MetaGPT \[Hong2023MetaGPT\], and AgentCoder \[huang2023agentcoder\] demonstrate this shift by dividing software-development responsibilities among distinct agents such as architect, programmer, tester, reviewer, and executor. Coordinated through **structured communication protocols** and **shared code artifacts**, these role-specialized agents turn code from a mere output target into the shared substrate through which the overall harness plans, acts, verifies, and improves itself.

# 2. harness + skills
## 2.1. resumo 

Exatamente! Você pegou o conceito central. A persistência (ou não) dos dados no contexto é uma decisão puramente do **harness** (a infraestrutura de código que envelopa o LLM).

No caso do **OpenCode**, o ecossistema lida com isso de forma muito inteligente e estruturada através de ferramentas nativas e plugins de compactação/memória.

O ecossistema do OpenCode gerencia o ciclo de vida das skills e o contexto da seguinte forma:

---

## 2.2. O Carregamento NATIVO de Skills no OpenCode

O OpenCode possui uma ferramenta nativa chamada explicitamente **`skill`**.
As suas habilidades personalizadas ficam salvas em arquivos `SKILL.md` (dentro de diretórios como `.opencode/skills/nome-da-skill/`).

O fluxo de contexto que ele faz segue esta lógica:

* **No início da sessão:** O OpenCode injeta no System Prompt apenas a tag `<available_skills>` contendo o `name` e a `description` de cada skill cadastrada. O conteúdo interno do markdown **não** entra no contexto ainda.
* **A Invocação:** Quando o agente precisa daquela habilidade, ele executa a ferramenta: `skill(name="minha-skill")`.
* **O Impacto no Contexto:** O OpenCode lê o arquivo `SKILL.md` e joga o texto completo dele **para dentro da janela de conversa** como o retorno da ferramenta.

---

## 2.3. Como o OpenCode evita o estouro do contexto após usar a Skill?

Se o agente ler três ou quatro arquivos `SKILL.md` densos, a janela de contexto começaria a pesar. Para mitigar isso, o OpenCode utiliza duas frentes (nativas e via plugins):

### 2.3.1. A. Isolamento via Sub-agentes (Nativo)

O OpenCode frequentemente delega tarefas pesadas que exigem habilidades específicas para **Sub-agentes** (como os sub-agentes embutidos *General*, *Explore* ou *Scout*).

* Quando o agente principal spawna um sub-agente para aplicar uma skill, esse sub-agente roda em uma **chamada de API paralela e isolada**, com sua própria janela de contexto.
* Quando o sub-agente termina de processar a skill, ele devolve apenas um resumo ou o resultado final para o agente principal através de troca de mensagens. As instruções brutas da skill morrem junto com o contexto descartado do sub-agente.

### 2.3.2. B. O Mecanismo de Compactação (Context Window Compaction)

Para sessões longas no terminal, o OpenCode possui uma rotina de **Compaction** (Compactação). Quando a conversa fica ociosa (*idle*) ou atinge um limite crítico de tokens, o harness do OpenCode passa uma "poda" no histórico:

* Ele remove os retornos brutos e gigantescos de ferramentas (como o conteúdo completo de um arquivo lido ou de uma skill carregada passos atrás).
* Ele mantém apenas os turnos essenciais da conversa (as instruções finais e o estado atual do código).

### 2.3.3. C. Integração com Plugins de Memória Longa (ex: Hindsight / Agent-Memory)

Em implementações mais robustas do OpenCode, utilizam-se plugins como o `hindsight` ou `opencode-agent-memory` (baseado no padrão do Letta).

Esses componentes alteram drasticamente o jogo:

1. O plugin intercepta a conversa a cada $N$ turnos (`retainEveryNTurns`).
2. Ele extrai os aprendizados e o resultado do uso daquela skill.
3. Ele joga fora o log pesado da execução da ferramenta do contexto atual e salva o aprendizado em um banco SQLite local (Durable Objects) ou arquivos markdown de memória (`.opencode/memory/`).
4. Se o agente precisar daquele conhecimento de novo, ele usa ferramentas de recordação (`hindsight_recall`) para trazer apenas o pedaço estritamente necessário de volta.

---

### 2.3.4. Resumo

No **OpenCode**, o conteúdo de um `SKILL.md` entra por completo no contexto do chat no momento em que a ferramenta `skill` é chamada. Porém, ele não fica lá para sempre gerando "gordura": o OpenCode limpa essa janela através de **sub-agentes isolados** (para a skill não poluir o fluxo principal) ou através de rotinas automáticas de **compactação de contexto** quando o terminal fica ocioso.

# 3. harness hooks

## 3.1. opencode hooks plugin

[Does OpenCode Support Hooks? A Complete Guide to Extensibility](https://dev.to/einarcesar/does-opencode-support-hooks-a-complete-guide-to-extensibility-k3p)


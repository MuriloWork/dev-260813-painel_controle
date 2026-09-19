**IA**  

# 1. [[260909-ia_handbook_harness|agent harness]]  
## 1.1. [[260919-ia_agent_harness|caso de uso: agent_harness, versao atual]]

# 2. agents + skills 
## 2.1. resumo 
Existe uma relação estreita entre [janela de contexto, memoria] do agente interagindo com o modelo LLM e os mecanismos de cada aplicação de agent harness, na forma e dinamica de gerenciamento de que o harness consegue realizar.

Os aspectos conceituais sobre [[260909-ia_handbook_harness#1.4.1. Memory and Context Engineering for Agent Harness|Memory and Context Engineering for Agent Harness]] são abordados em seção dedicada ao tema.
A persistência (ou não) dos dados no contexto é uma decisão puramente do **harness** (a infraestrutura de código que envelopa o LLM).

Aqui nessa seção serão tratados os aspectos operacionais de gerenciamento de memoria e contexto, com base em casos de uso.

## 2.2. [[260919-ia_agent_harness|caso de uso: opencode]] 
No caso do **OpenCode**, o ecossistema lida com isso de forma muito inteligente e estruturada através de ferramentas nativas e plugins de compactação/memória.

O ecossistema do OpenCode gerencia o ciclo de vida das skills e o contexto da seguinte forma:

### 2.2.1. agentes opencode |[web](https://opencode.ai/docs/pt-br/agents/)|

Agentes são assistentes de IA especializados que podem ser configurados para tarefas e fluxos de trabalho específicos. Eles permitem que você crie ferramentas focadas com prompts, modelos e acesso a ferramentas personalizados.

Você pode alternar entre agentes durante uma sessão ou invocá-los com a menção `@`.



#### 2.2.1.1. Tipos

Existem dois tipos de agentes no opencode; agentes primários e subagentes.



##### 2.2.1.1.1. Agentes primários

Agentes primários são os principais assistentes com os quais você interage diretamente. Você pode alternar entre eles usando a tecla **Tab** ou sua tecla de atalho configurada `switch_agent`. Esses agentes lidam com sua conversa principal. O acesso às ferramentas é configurado por meio de permissões — por exemplo, Build tem todas as ferramentas habilitadas, enquanto Plan é restrito.

opencode vem com dois agentes primários integrados, **Build** e **Plan**. Vamos ver isso abaixo.



##### 2.2.1.1.2. Subagentes

Subagentes são assistentes especializados que agentes primários podem invocar para tarefas específicas. Você também pode invocá-los manualmente mencionando-os com **@** em suas mensagens.

OpenCode vem com três subagentes integrados, **General**, **Explore** e **Scout**. Vamos ver isso abaixo.



#### 2.2.1.2. Integrados

OpenCode vem com dois agentes primários integrados e três subagentes integrados.



##### 2.2.1.2.1. build

*Modo*: `primary`

Build é o agente primário **padrão** com todas as ferramentas habilitadas. Este é o agente padrão para trabalho de desenvolvimento onde você precisa de acesso total a operações de arquivo e comandos do sistema.



##### 2.2.1.2.2. plan

*Modo*: `primary`

Um agente restrito projetado para planejamento e análise. Usamos um sistema de permissões para lhe dar mais controle e evitar alterações não intencionais. Por padrão, todos os seguintes estão configurados para `ask`:

- `file edits`: Todas as gravações, patches e edições
- `bash`: Todos os comandos bash

Este agente é útil quando você deseja que o LLM analise código, sugira alterações ou crie planos sem fazer modificações reais em seu código.



##### 2.2.1.2.3. general

*Modo*: `subagent`

Um agente de propósito geral para pesquisar questões complexas e executar tarefas em múltiplas etapas. Tem acesso total às ferramentas (exceto todo), portanto, pode fazer alterações em arquivos quando necessário. Use isso para executar várias unidades de trabalho em paralelo.



##### 2.2.1.2.4. explore

*Modo*: `subagent`

Um agente rápido e somente leitura para explorar bases de código. Não pode modificar arquivos. Use isso quando você precisar encontrar rapidamente arquivos por padrões, pesquisar código por palavras-chave ou responder perguntas sobre a base de código.



##### 2.2.1.2.5. Scout

*Modo*: `subagent`

Um agente somente leitura para pesquisa em documentação externa e dependências. Use-o quando você precisar clonar o repositório de uma dependência para o cache gerenciado do OpenCode, inspecionar o código-fonte de uma biblioteca ou cruzar o código local com implementações upstream sem modificar seu workspace.



##### 2.2.1.2.6. compaction

*Modo*: `primary`

Agente de sistema oculto que compacta longos contextos em um resumo menor. Ele é executado automaticamente quando necessário e não é selecionável na interface.



*Modo*: `primary`

Agente de sistema oculto que gera títulos curtos para sessões. Ele é executado automaticamente e não é selecionável na interface.



##### 2.2.1.2.7. summary

*Modo*: `primary`

Agente de sistema oculto que cria resumos de sessões. Ele é executado automaticamente e não é selecionável na interface.



#### 2.2.1.3. Uso

1. Para agentes primários, use a tecla **Tab** para alternar entre eles durante uma sessão. Você também pode usar sua tecla de atalho configurada `switch_agent`.
2. Subagentes podem ser invocados:
	- **Automaticamente** por agentes primários para tarefas especializadas com base em suas descrições.
		- Manualmente mencionando um subagente em sua mensagem. Por exemplo.
		```txt
		@general help me search for this function
		```
3. **Navegação entre sessões**: Quando subagentes criam suas próprias sessões filhas, você pode navegar entre a sessão pai e todas as sessões filhas usando:
	- **\<Leader>+Right** (ou sua tecla de atalho configurada `session_child_cycle`) para alternar para frente através de pai → child1 → child2 → … → pai
		- **\<Leader>+Left** (ou sua tecla de atalho configurada `session_child_cycle_reverse`) para alternar para trás através de pai ← child1 ← child2 ← … ← pai
	Isso permite que você mude perfeitamente entre a conversa principal e o trabalho especializado do subagente.



#### 2.2.1.4. Configuração

Você pode personalizar os agentes integrados ou criar os seus próprios através da configuração. Os agentes podem ser configurados de duas maneiras:



##### 2.2.1.4.1. JSON

Configure os agentes em seu arquivo de configuração `opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "agent": {
    "build": {
      "mode": "primary",
      "model": "anthropic/claude-sonnet-4-20250514",
      "prompt": "{file:./prompts/build.txt}",
      "tools": {
        "write": true,
        "edit": true,
        "bash": true
      }
    },
    "plan": {
      "mode": "primary",
      "model": "anthropic/claude-haiku-4-20250514",
      "tools": {
        "write": false,
        "edit": false,
        "bash": false
      }
    },
    "code-reviewer": {
      "description": "Revisa código para melhores práticas e potenciais problemas",
      "mode": "subagent",
      "model": "anthropic/claude-sonnet-4-20250514",
      "prompt": "Você é um revisor de código. Foque em segurança, performance e manutenibilidade.",
      "tools": {
        "write": false,
        "edit": false
      }
    }
  }
}
```



##### 2.2.1.4.2. Markdown

Você também pode definir agentes usando arquivos markdown. Coloque-os em:

- Global: `~/.config/opencode/agents/`
- Por projeto: `.opencode/agents/`

```markdown
---
description: Revisa código para qualidade e melhores práticas
mode: subagent
model: anthropic/claude-sonnet-4-20250514
temperature: 0.1
tools:
  write: false
  edit: false
  bash: false
---

Você está no modo de revisão de código. Foque em:

- Qualidade do código e melhores práticas
- Bugs potenciais e casos de borda
- Implicações de desempenho
- Considerações de segurança

Forneça feedback construtivo sem fazer alterações diretas.
```

O nome do arquivo markdown se torna o nome do agente. Por exemplo, `review.md` cria um agente `review`.



#### 2.2.1.5. Opções

Vamos analisar essas opções de configuração em detalhes.



##### 2.2.1.5.1. Descrição

Use a opção `description` para fornecer uma breve descrição do que o agente faz e quando usá-lo.

```json
{
  "agent": {
    "review": {
      "description": "Revisa código para melhores práticas e potenciais problemas"
    }
  }
}
```

Esta é uma opção de configuração **obrigatória**.



##### 2.2.1.5.2. Temperatura

Controle a aleatoriedade e criatividade das respostas do LLM com a configuração `temperature`.

Valores mais baixos tornam as respostas mais focadas e determinísticas, enquanto valores mais altos aumentam a criatividade e variabilidade.

```json
{
  "agent": {
    "plan": {
      "temperature": 0.1
    },
    "creative": {
      "temperature": 0.8
    }
  }
}
```

Os valores de temperatura geralmente variam de 0.0 a 1.0:

- **0.0-0.2**: Respostas muito focadas e determinísticas, ideais para análise de código e planejamento
- **0.3-0.5**: Respostas equilibradas com alguma criatividade, boas para tarefas de desenvolvimento gerais
- **0.6-1.0**: Respostas mais criativas e variadas, úteis para brainstorming e exploração

```json
{
  "agent": {
    "analyze": {
      "temperature": 0.1,
      "prompt": "{file:./prompts/analysis.txt}"
    },
    "build": {
      "temperature": 0.3
    },
    "brainstorm": {
      "temperature": 0.7,
      "prompt": "{file:./prompts/creative.txt}"
    }
  }
}
```

Se nenhuma temperatura for especificada, o opencode usa padrões específicos do modelo; tipicamente 0 para a maioria dos modelos, 0.55 para modelos Qwen.



##### 2.2.1.5.3. Máximo de etapas

Controle o número máximo de iterações que um agente pode realizar antes de ser forçado a responder apenas com texto. Isso permite que usuários que desejam controlar custos definam um limite nas ações do agente.

Se isso não for definido, o agente continuará a iterar até que o modelo decida parar ou o usuário interrompa a sessão.

```json
{
  "agent": {
    "quick-thinker": {
      "description": "Raciocínio rápido com iterações limitadas",
      "prompt": "Você é um pensador rápido. Resolva problemas com etapas mínimas.",
      "steps": 5
    }
  }
}
```

Quando o limite é alcançado, o agente recebe um prompt especial do sistema instruindo-o a responder com um resumo de seu trabalho e tarefas recomendadas restantes.



##### 2.2.1.5.4. Desativar

Defina como `true` para desativar o agente.

```json
{
  "agent": {
    "review": {
      "disable": true
    }
  }
}
```



##### 2.2.1.5.5. Prompt

Especifique um arquivo de prompt do sistema personalizado para este agente com a configuração `prompt`. O arquivo de prompt deve conter instruções específicas para o propósito do agente.

```json
{
  "agent": {
    "review": {
      "prompt": "{file:./prompts/code-review.txt}"
    }
  }
}
```

Este caminho é relativo ao local onde o arquivo de configuração está localizado. Portanto, isso funciona tanto para a configuração global do opencode quanto para a configuração específica do projeto.



##### 2.2.1.5.6. Modelo

Use a configuração `model` para substituir o modelo para este agente. Útil para usar diferentes modelos otimizados para diferentes tarefas. Por exemplo, um modelo mais rápido para planejamento, um modelo mais capaz para implementação.

```json
{
  "agent": {
    "plan": {
      "model": "anthropic/claude-haiku-4-20250514"
    }
  }
}
```

O ID do modelo em sua configuração do opencode usa o formato `provider/model-id`. Por exemplo, se você estiver usando [OpenCode Zen](https://opencode.ai/docs/zen), você usaria `opencode/gpt-5.1-codex` para GPT 5.1 Codex.



##### 2.2.1.5.7. Ferramentas

Controle quais ferramentas estão disponíveis neste agente com a configuração `tools`. Você pode habilitar ou desabilitar ferramentas específicas definindo-as como `true` ou `false`.

```json
{
  "$schema": "https://opencode.ai/config.json",
  "tools": {
    "write": true,
    "bash": true
  },
  "agent": {
    "plan": {
      "tools": {
        "write": false,
        "bash": false
      }
    }
  }
}
```

Você também pode usar curingas para controlar várias ferramentas ao mesmo tempo. Por exemplo, para desativar todas as ferramentas de um servidor MCP:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "agent": {
    "readonly": {
      "tools": {
        "mymcp_*": false,
        "write": false,
        "edit": false
      }
    }
  }
}
```

[Saiba mais sobre ferramentas](https://opencode.ai/docs/tools).



##### 2.2.1.5.8. Permissões

Você pode configurar permissões para gerenciar quais ações um agente pode realizar. Atualmente, as permissões para as ferramentas `edit`, `bash` e `webfetch` podem ser configuradas para:

- `"ask"` — Solicitar aprovação antes de executar a ferramenta
- `"allow"` — Permitir todas as operações sem aprovação
- `"deny"` — Desativar a ferramenta

```json
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "edit": "deny"
  }
}
```

Você pode substituir essas permissões por agente.

```json
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "edit": "deny"
  },
  "agent": {
    "build": {
      "permission": {
        "edit": "ask"
      }
    }
  }
}
```

Você também pode definir permissões em agentes Markdown.

```markdown
---
description: Revisão de código sem edições
mode: subagent
permission:
  edit: deny
  bash:
    "*": ask
    "git diff": allow
    "git log*": allow
    "grep *": allow
  webfetch: deny
---

Apenas analise o código e sugira alterações.
```

Você pode definir permissões para comandos bash específicos.

```json
{
  "$schema": "https://opencode.ai/config.json",
  "agent": {
    "build": {
      "permission": {
        "bash": {
          "git push": "ask",
          "grep *": "allow"
        }
      }
    }
  }
}
```

Isso pode aceitar um padrão glob.

```json
{
  "$schema": "https://opencode.ai/config.json",
  "agent": {
    "build": {
      "permission": {
        "bash": {
          "git *": "ask"
        }
      }
    }
  }
}
```

E você também pode usar o curinga `*` para gerenciar permissões para todos os comandos. Como a última regra correspondente tem precedência, coloque o curinga `*` primeiro e regras específicas depois.

```json
{
  "$schema": "https://opencode.ai/config.json",
  "agent": {
    "build": {
      "permission": {
        "bash": {
          "*": "ask",
          "git status *": "allow"
        }
      }
    }
  }
}
```

[Saiba mais sobre permissões](https://opencode.ai/docs/permissions).


##### 2.2.1.5.9. Modo

Controle o modo do agente com a configuração `mode`. A opção `mode` é usada para determinar como o agente pode ser usado.

```json
{
  "agent": {
    "review": {
      "mode": "subagent"
    }
  }
}
```

A opção `mode` pode ser definida como `primary`, `subagent` ou `all`. Se nenhum `mode` for especificado, o padrão é `all`.

---

##### 2.2.1.5.10. Oculto

Oculte um subagente do menu de autocompletar `@` com `hidden: true`. Útil para subagentes internos que devem ser invocados apenas programaticamente por outros agentes através da ferramenta Task.

```json
{
  "agent": {
    "internal-helper": {
      "mode": "subagent",
      "hidden": true
    }
  }
}
```

Isso afeta apenas a visibilidade do usuário no menu de autocompletar. Agentes ocultos ainda podem ser invocados pelo modelo através da ferramenta Task, se as permissões permitirem.

---

##### 2.2.1.5.11. Permissões de tarefa

Controle quais subagentes um agente pode invocar através da ferramenta Task com `permission.task`. Usa padrões globais para correspondência flexível.

```json
{
  "agent": {
    "orchestrator": {
      "mode": "primary",
      "permission": {
        "task": {
          "*": "deny",
          "orchestrator-*": "allow",
          "code-reviewer": "ask"
        }
      }
    }
  }
}
```

Quando definido como `deny`, o subagente é removido da descrição da ferramenta Task completamente, então o modelo não tentará invocá-lo.

---

##### 2.2.1.5.12. Cor

Personalize a aparência visual do agente na interface com a opção `color`. Isso afeta como o agente aparece na interface.

Use uma cor hex válida (por exemplo, `#FF5733`) ou cor de tema: `primary`, `secondary`, `accent`, `success`, `warning`, `error`, `info`.

```json
{
  "agent": {
    "creative": {
      "color": "#ff6b6b"
    },
    "code-reviewer": {
      "color": "accent"
    }
  }
}
```

---

##### 2.2.1.5.13. Top P

Controle a diversidade das respostas com a opção `top_p`. Alternativa à temperatura para controlar a aleatoriedade.

```json
{
  "agent": {
    "brainstorm": {
      "top_p": 0.9
    }
  }
}
```

Os valores variam de 0.0 a 1.0. Valores mais baixos são mais focados, valores mais altos são mais diversos.

---

##### 2.2.1.5.14. Adicional

Quaisquer outras opções que você especificar em sua configuração de agente serão **passadas diretamente** para o provedor como opções de modelo. Isso permite que você use recursos e parâmetros específicos do provedor.

Por exemplo, com os modelos de raciocínio da OpenAI, você pode controlar o esforço de raciocínio:

```json
{
  "agent": {
    "deep-thinker": {
      "description": "Agente que usa alto esforço de raciocínio para problemas complexos",
      "model": "openai/gpt-5",
      "reasoningEffort": "high",
      "textVerbosity": "low"
    }
  }
}
```

Essas opções adicionais são específicas do modelo e do provedor. Verifique a documentação do seu provedor para parâmetros disponíveis.

---

#### 2.2.1.6. Criando agentes

Você pode criar novos agentes usando o seguinte comando:

```bash
opencode agent create
```

Este comando interativo irá:

1. Perguntar onde salvar o agente; global ou específico do projeto.
2. Descrição do que o agente deve fazer.
3. Gerar um prompt de sistema apropriado e identificador.
4. Permitir que você selecione quais ferramentas o agente pode acessar.
5. Finalmente, criar um arquivo markdown com a configuração do agente.

#### 2.2.1.7. Casos de uso

Aqui estão alguns casos de uso comuns para diferentes agentes.

- **Agente Build**: Trabalho de desenvolvimento completo com todas as ferramentas habilitadas
- **Agente Plan**: Análise e planejamento sem fazer alterações
- **Agente Review**: Revisão de código com acesso somente leitura e ferramentas de documentação
- **Agente Debug**: Focado em investigação com ferramentas bash e de leitura habilitadas
- **Agente Docs**: Redação de documentação com operações de arquivo, mas sem comandos do sistema

#### 2.2.1.8. Exemplos

Aqui estão alguns agentes de exemplo que você pode achar úteis.

##### 2.2.1.8.1. Agente de documentação

```markdown
---
description: Escreve e mantém a documentação do projeto
mode: subagent
tools:
  bash: false
---

Você é um escritor técnico. Crie documentação clara e abrangente.

Foque em:

- Explicações claras
- Estrutura adequada
- Exemplos de código
- Linguagem amigável ao usuário
```


##### 2.2.1.8.2. Auditor de segurança

```markdown
---
description: Realiza auditorias de segurança e identifica vulnerabilidades
mode: subagent
tools:
  write: false
  edit: false
---

Você é um especialista em segurança. Foque em identificar potenciais problemas de segurança.

Procure por:

- Vulnerabilidades de validação de entrada
- Falhas de autenticação e autorização
- Riscos de exposição de dados
- Vulnerabilidades de dependência
- Problemas de segurança de configuração
```


### 2.2.2. O Carregamento NATIVO de Skills no OpenCode

O OpenCode possui uma ferramenta nativa chamada explicitamente **`skill`**.
As suas habilidades personalizadas ficam salvas em arquivos `SKILL.md` (dentro de diretórios como `.opencode/skills/nome-da-skill/`).

O fluxo de contexto que ele faz segue esta lógica:

* **No início da sessão:** O OpenCode injeta no System Prompt apenas a tag `<available_skills>` contendo o `name` e a `description` de cada skill cadastrada. O conteúdo interno do markdown **não** entra no contexto ainda.
* **A Invocação:** Quando o agente precisa daquela habilidade, ele executa a ferramenta: `skill(name="minha-skill")`.
* **O Impacto no Contexto:** O OpenCode lê o arquivo `SKILL.md` e joga o texto completo dele **para dentro da janela de conversa** como o retorno da ferramenta.

---

### 2.2.3. Como o OpenCode evita o estouro do contexto após usar a Skill?

Se o agente ler três ou quatro arquivos `SKILL.md` densos, a janela de contexto começaria a pesar. Para mitigar isso, o OpenCode utiliza duas frentes (nativas e via plugins):

#### 2.2.3.1. A. Isolamento via Sub-agentes (Nativo)

O OpenCode frequentemente delega tarefas pesadas que exigem habilidades específicas para **Sub-agentes** (como os sub-agentes embutidos *General*, *Explore* ou *Scout*).

* Quando o agente principal spawna um sub-agente para aplicar uma skill, esse sub-agente roda em uma **chamada de API paralela e isolada**, com sua própria janela de contexto.
* Quando o sub-agente termina de processar a skill, ele devolve apenas um resumo ou o resultado final para o agente principal através de troca de mensagens. As instruções brutas da skill morrem junto com o contexto descartado do sub-agente.

#### 2.2.3.2. B. O Mecanismo de Compactação (Context Window Compaction)

Para sessões longas no terminal, o OpenCode possui uma rotina de **Compaction** (Compactação). Quando a conversa fica ociosa (*idle*) ou atinge um limite crítico de tokens, o harness do OpenCode passa uma "poda" no histórico:

* Ele remove os retornos brutos e gigantescos de ferramentas (como o conteúdo completo de um arquivo lido ou de uma skill carregada passos atrás).
* Ele mantém apenas os turnos essenciais da conversa (as instruções finais e o estado atual do código).

#### 2.2.3.3. C. Integração com Plugins de Memória Longa (ex: Hindsight / Agent-Memory)

Em implementações mais robustas do OpenCode, utilizam-se plugins como o `hindsight` ou `opencode-agent-memory` (baseado no padrão do Letta).

Esses componentes alteram drasticamente o jogo:

1. O plugin intercepta a conversa a cada $N$ turnos (`retainEveryNTurns`).
2. Ele extrai os aprendizados e o resultado do uso daquela skill.
3. Ele joga fora o log pesado da execução da ferramenta do contexto atual e salva o aprendizado em um banco SQLite local (Durable Objects) ou arquivos markdown de memória (`.opencode/memory/`).
4. Se o agente precisar daquele conhecimento de novo, ele usa ferramentas de recordação (`hindsight_recall`) para trazer apenas o pedaço estritamente necessário de volta.

---

#### 2.2.3.4. Resumo

No **OpenCode**, o conteúdo de um `SKILL.md` entra por completo no contexto do chat no momento em que a ferramenta `skill` é chamada. Porém, ele não fica lá para sempre gerando "gordura": o OpenCode limpa essa janela através de **sub-agentes isolados** (para a skill não poluir o fluxo principal) ou através de rotinas automáticas de **compactação de contexto** quando o terminal fica ocioso.


# 3. Knowledge base

## 3.1. project docs OLD 

### 3.1.1. prd 

- funções de negócio 
- stack 
	- scripts: dart, python, ps1, sqlite, api  
	- UI: flutter, web, shell 
- referências: docs 

### 3.1.2. project documents rules  

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

### 3.1.3. srd 
  
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

### 3.1.4. srd session code blocks 

- resumo do srd: selected logic map maps review rules   
- resumo do control map + tag system 
- selected code blocks 

### 3.1.5. plano 

- plano integral: etapas 
- plano etapa, todo 
- control maps 
  - plan map 
  - **code map**: [files, classes, métodos] x [funções negócio] = tags [pendencia, maturidade] 
    - pendencia: [novo, refatorar, manter, eliminar] 
    - maturidade: [descrições, code block, quality, test] 
  - **data process map**: [files, classes, métodos] x [data blocks] = tags [pendencia, maturidade] 

### 3.1.6. code, code-review, test 

## 3.2. okf - open knowledge format

### 3.2.1. esclarecimentos
[[260810_okf_spec|GitHub OKF spec original (local)]]

#### 3.2.1.1. OKF versus md + links + frontmatter

##### 3.2.1.1.1. recursos básicos do OKF já existiam
O diferencial está na **combinação de pequenas convenções**.

A especificação define explicitamente:
- conceito = um arquivo Markdown;
- `type` obrigatório;
- `title`, `description`, `tags`, etc.;
- links entre conceitos;
- `index.md` para _progressive disclosure_;
- hierarquia de diretórios;
- `sources` para proveniência;
- `generated` e `verified`;
- `status`;
- `stale_after`;
- IDs implícitos baseados no caminho;
- convenções para atores/agentes;
- possibilidade de gerar índices automaticamente. ([GitHub](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md?utm_source=chatgpt.com "knowledge-catalog/okf/SPEC.md at main · GoogleCloudPlatform/knowledge-catalog · GitHub"))

Então eu dividiria o ganho em **três níveis**.

##### 3.2.1.1.2. Nível 1 — organização

Um Markdown convencional:

```text
docs/
    foo.md
    bar.md
    bla.md
```

não diz muita coisa para um agente.

OKF acrescenta:

```text
knowledge/
├── index.md
├── requirements/
│   ├── index.md
│   ├── REQ-001.md
│   └── REQ-002.md
├── architecture/
│   ├── index.md
│   └── ARCH-001.md
└── classes/
    ├── index.md
    └── CLASS-001.md
```

Agora a própria estrutura já é uma **forma de navegação**.

---

##### 3.2.1.1.3. Nível 2 — progressive disclosure

Esse é, para mim, um dos recursos mais interessantes para o seu problema.

Imagine:

```text
knowledge/index.md
```

contendo:

```
## Knowledge Base

### Requirements

- [Functional requirements](requirements/index.md)
  - User and authentication requirements

### Architecture

- [System architecture](architecture/index.md)
  - Components and architectural decisions

### Domain model

- [Classes](classes/index.md)
  - Domain classes and relationships
```

O agente pode fazer:

```text
index
  ↓
requirements/index
  ↓
REQ-001
```

em vez de:

```text
carregar 2.000 arquivos
        ↓
      LLM
```

A própria especificação chama isso explicitamente de **progressive disclosure**: o `index.md` permite descobrir o que existe antes de abrir os documentos individuais. ([GitHub](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md?utm_source=chatgpt.com "knowledge-catalog/okf/SPEC.md at main · GoogleCloudPlatform/knowledge-catalog · GitHub"))

Isso responde parcialmente à sua pergunta 2.

---

##### 3.2.1.1.4. Nível 3 — conhecimento passa a ter metadados sobre o próprio conhecimento

Aqui está uma diferença mais substancial.

Imagine:

```yaml
---
type: Architecture Decision
title: Use PostgreSQL
status: stable

generated:
  by: human:murilo
  at: 2026-08-10T10:00:00Z

verified:
  by: human:murilo
  at: 2026-08-10T11:00:00Z

stale_after: 2027-01-01

sources:
  - id: architecture-analysis
    resource: /references/architecture-analysis.md
---
```

Agora um agente consegue distinguir:

```text
documento
   │
   ├── o que é?
   ├── de onde veio?
   ├── quem produziu?
   ├── foi verificado?
   ├── quando?
   ├── ainda está vigente?
   └── quais fontes o sustentam?
```

Isso é uma das principais novidades do **OKF v0.2**: provenance, trust e lifecycle viraram conceitos de primeira classe. ([GitHub](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md?utm_source=chatgpt.com "knowledge-catalog/okf/SPEC.md at main · GoogleCloudPlatform/knowledge-catalog · GitHub"))

Para uma KB mantida parcialmente por agentes, isso é muito mais importante do que simplesmente ter YAML frontmatter.

---

#### 3.2.1.2. recursos necessarios

A estrutura básica é extremamente simples:

```text
knowledge/
├── index.md
├── requirements/
│   ├── index.md
│   ├── REQ-001.md
│   └── REQ-002.md
├── architecture/
│   ├── index.md
│   └── ARCH-001.md
├── components/
│   ├── index.md
│   └── COMPONENT-001.md
└── decisions/
    └── ADR-001.md
```

Cada conceito é essencialmente um Markdown com YAML frontmatter:

```
---
type: requirement
title: Autenticação do usuário
id: REQ-001
status: approved
---

#### Autenticação do usuário

O sistema deve permitir que o usuário...
```

A especificação atual é **OKF v0.2**. Ela continua deliberadamente mínima: uma coleção de Markdown + YAML frontmatter, sem schema registry, autoridade central ou ferramenta obrigatória. ([GitHub](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md?utm_source=chatgpt.com "knowledge-catalog/okf/SPEC.md at main · GoogleCloudPlatform/knowledge-catalog · GitHub"))

**Portanto**:

| Componente          | Precisa? | Para quê?                                |
| ------------------- | -------: | ---------------------------------------- |
| Google Cloud        |        ❌ | Não                                      |
| Conta Google        |        ❌ | Não                                      |
| API Key             |        ❌ | Não                                      |
| OAuth               |        ❌ | Não                                      |
| Banco de dados      |        ❌ | Não                                      |
| Vector DB           |        ❌ | Não                                      |
| SDK do Google       |        ❌ | Não                                      |
| Python/Node/etc.    |        ❌ | Não                                      |
| Markdown            |        ✅ | Conteúdo                                 |
| YAML                |        ✅ | Metadados                                |
| Sistema de arquivos |        ✅ | Armazenamento                            |
| Git                 | opcional | Versionamento                            |
| LLM                 | opcional | Agentes consultarem/gerarem conhecimento |

Isso é uma das características mais interessantes do OKF para o seu projeto.

---

### 3.2.2. instruções, como produzir
#### 3.2.2.1. O mais interessante para sua aplicação: links entre conceitos

O OKF é especialmente interessante para o seu caso porque os documentos podem representar **conceitos relacionados**, e os relacionamentos podem ser expressos por links Markdown.

Por exemplo:

```
---
type: requirement
title: Autenticação
id: REQ-001
---

#### Autenticação

O sistema deve autenticar usuários.

Relacionado:

- [Caso de uso Login](../use-cases/UC-001.md)
- [Componente AuthenticationService](../components/COMP-012.md)
- [Decisão ADR-004](../decisions/ADR-004.md)
```

Então você pode ter:

```text
REQ-001
   │
   ├────────► UC-001
   │
   ├────────► COMP-012
   │
   └────────► ADR-004
                  │
                  ▼
             PATTERN-003
```

Isso começa a ficar **muito próximo da base de conhecimento que você vinha investigando para requisitos + arquitetura + objetos + UML**.

A própria especificação trabalha com a ideia de _concepts_ e relações entre eles, mantendo a representação em formatos simples. ([GitHub](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md?utm_source=chatgpt.com "knowledge-catalog/okf/SPEC.md at main · GoogleCloudPlatform/knowledge-catalog · GitHub"))

---

#### 3.2.2.2. Minha recomendação para seu projeto

Eu **não começaria usando nenhum produto Google**.

Eu faria inicialmente:

```text
my-model-based-generator/
│
├── knowledge/
│   ├── index.md
│   │
│   ├── requirements/
│   ├── use-cases/
│   ├── architecture/
│   ├── components/
│   ├── classes/
│   ├── interfaces/
│   ├── design-patterns/
│   ├── decisions/
│   ├── constraints/
│   └── generation-rules/
│
├── models/
│   ├── uml/
│   └── ...
│
├── generators/
│
└── agents/
```

E trataria:

> **OKF como o formato persistente da Knowledge Base.**

Seu aplicativo seria responsável por:

```text
                  Application
                       │
       ┌───────────────┼────────────────┐
       │               │                │
    Editor          Agents          Generator
       │               │                │
       └───────────────┼────────────────┘
                       │
                 Knowledge API
                       │
                       ▼
                  OKF Repository
```

Depois você pode decidir se precisa de:

- SQLite;
- PostgreSQL;
- Git;
- SQLite + Git;
- índice FTS;
- vector database;
- knowledge graph;
- MCP;
- LangChain/LangGraph;
- Gemini/OpenAI/Claude;
- etc.
    

**sem alterar o formato fundamental da sua base.**

---

##### 3.2.2.2.1. E há uma questão arquitetural ainda mais interessante

Para o seu caso, eu separaria **"modelo do sistema"** de **"conhecimento sobre o modelo"**.

Por exemplo:

```text
              MODEL
                │
       ┌────────┼─────────┐
       │        │         │
   Requirement Class   Component
       │        │         │
       └────────┼─────────┘
                │
                ▼
          Knowledge about
             the model
                │
       ┌────────┼──────────┐
       │        │          │
   decisions patterns  generation rules
```

E o OKF pode funcionar muito bem como essa segunda camada.

Isso permitiria que sua aplicação tenha **um modelo formal (UML/estrutura própria)** e, ao redor dele, uma **base de conhecimento textual, versionável e navegável pelos agentes**.

Para uma aplicação de _model-based code generation_, eu acho essa separação particularmente promissora.

Se quiser, posso avançar um passo e **propor uma estrutura OKF completa para sua aplicação**, incluindo `requirements`, `architecture`, `UML classes`, `design patterns`, `ADRs`, `code-generation rules`, relacionamentos e como um agente deveria consultar essa base.

### 3.2.3. instruções, como consumir, grafos

A especificação diz explicitamente que os links entre conceitos formam relações e que consumidores podem construir uma visão de grafo; o visualizador de referência do próprio projeto faz exatamente isso. Ele fornece:

`estrutura + metadados + links + índices`

A estratégia de recuperação fica para o consumidor.

### 3.2.4. outras referencias
[Google Cloud - apresentando o okf](https://cloud-google-com.translate.goog/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc)
[Atteniv OKF Editor](https://github.com/atteniv/okf-editor/blob/main/README.md#where-this-editor-fits)

# 4. Knowledge Graph
- understand anything 
- [Graphify + code-review-graph](https://dev.to/mir_mursalin_ankur/graphify-code-review-graph-build-a-self-updating-knowledge-graph-for-claude-code-and-other-ai-j1m)

# 5. drafts

## 5.1. perguntas e respostas

### 5.1.1. perguntas 01
- links entre arquivos markdown, e outros, e tambem frontmatters, são recursos comuns, o que há no okf que aprimora o uso desses recursos?
- uma leitura eficiente da base de conhecimento é ler o conteudo certo no momento certo, para um agente fazer uma leitura eficiente precisa de algum recurso, tipo um grafo?
- ainda sobre como o agente lê o conteúdo, 
	- faz diferença onde os links são posicinados no conteudo markdown? se o link estiver no meio de um paragrafo, existe o risco do agente navegar para um proximo arquivo sem ter lido o conteudo necessario no arquivo de origem?
	- cada interação sobre a base de conhecimento podem ter objetivos ligeiramente distintos, cabendo ao agente decidir se deve ler (trazer para o contexto) todo o conteudo de um determinado markdown ou apenas uma parte, o que funciona melhor? conhecimento quebrado em um numero maior de arquivos ou em arquivos maiores e deixar o agente selecionar?

### 5.1.2. respostas 01

#### 5.1.2.1. Eu faria uma arquitetura híbrida

Para sua aplicação eu não escolheria:

> Markdown **OU** grafo.

Eu faria:

```text
                    Knowledge Base
                          │
                ┌─────────┴─────────┐
                │                   │
           Filesystem             Graph
                │                   │
             *.md               nodes/edges
                │                   │
                └─────────┬─────────┘
                          │
                    Knowledge API
                          │
                         Agent
```

O Markdown é a **fonte de verdade**.

O grafo é um **índice derivado**.

Por exemplo:

```text
REQ-001.md
    │
    ├── link → UC-001.md
    ├── link → ARCH-002.md
    └── link → ADR-003.md
```

se transforma em:

```text
REQ-001
   │
   ├── UC-001
   ├── ARCH-002
   └── ADR-003
```

Você pode reconstruir esse grafo a qualquer momento.

Isso evita ficar preso a um banco de grafos.

---

#### 5.1.2.2. Sobre sua pergunta mais interessante: posição do link

> Se o link estiver no meio de um parágrafo, existe risco de o agente navegar para o próximo arquivo sem ter lido o conteúdo necessário?

**Sim, conceitualmente existe esse risco — mas ele não é específico do OKF.**

Por exemplo:

```
A arquitetura utiliza o padrão
[Repository](../patterns/repository.md)
para separar persistência da lógica de domínio.
```

Um agente pode interpretar isso como:

```text
"Repository é relevante"
       ↓
abre Repository.md
```

sem necessariamente terminar de interpretar:

```text
"para separar persistência da lógica de domínio"
```

Mas isso não significa que você precise evitar links inline.

O significado semântico do link está no **contexto textual que o rodeia**.

A própria especificação do OKF considera a relação como sendo determinada pelo texto ao redor do link; o link em si não possui um tipo formal como `depends-on`, `implements`, `references`, etc. ([GitHub](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md?utm_source=chatgpt.com "knowledge-catalog/okf/SPEC.md at main · GoogleCloudPlatform/knowledge-catalog · GitHub"))

Isso é uma limitação importante para o seu caso.

---

#### 5.1.2.3. Para Model-Based Code Generation eu faria diferente

Eu provavelmente adotaria uma convenção mais estruturada.

Em vez de:

```
A classe utiliza o padrão
[Repository](../patterns/repository.md)
para persistência.
```

poderia ter:

```
## Persistence

A classe utiliza Repository para separar persistência da lógica
de domínio.

Related concepts:

- Repository Pattern: [PAT-003](../patterns/PAT-003.md)
- Persistence component: [COMP-012](../components/COMP-012.md)
```

Ou até:

```
## Relationships

- implements: [INTERFACE-003](../interfaces/INTERFACE-003.md)
- uses: [PAT-003](../patterns/PAT-003.md)
- depends-on: [COMP-012](../components/COMP-012.md)
- satisfies: [REQ-034](../requirements/REQ-034.md)
```

A diferença é enorme para um agente.

Você está dando:

```text
texto humano
       +
estrutura semântica
```

em vez de somente:

```text
texto humano
       +
link
```

---

#### 5.1.2.4. Eu iria ainda mais longe

Para seu projeto, eu consideraria uma convenção própria sobre o OKF:

```yaml
---
type: Class
id: CLASS-001
title: OrderService
---
```

e:

```
## Responsibilities

...

## Relationships

- satisfies: [REQ-021](../requirements/REQ-021.md)
- implements: [INTERFACE-003](../interfaces/INTERFACE-003.md)
- depends-on: [CLASS-007](../classes/CLASS-007.md)
- uses-pattern: [PATTERN-004](../patterns/PATTERN-004.md)
```

Seu parser poderia transformar isso em:

```text
CLASS-001
  │
  ├── satisfies ───────> REQ-021
  ├── implements ──────> INTERFACE-003
  ├── depends-on ──────> CLASS-007
  └── uses-pattern ────> PATTERN-004
```

O OKF continua válido porque permite extensões e não fixa uma taxonomia de tipos ou relações. ([GitHub](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md?utm_source=chatgpt.com "knowledge-catalog/okf/SPEC.md at main · GoogleCloudPlatform/knowledge-catalog · GitHub"))

---

#### 5.1.2.5. Agora sua terceira pergunta: arquivos pequenos ou arquivos grandes?

Aqui eu acho que existe uma resposta bastante clara para **agentes**:

> **Não otimize o número de arquivos. Otimize a unidade semântica de recuperação.**

Isso é muito importante.

Não faça:

```text
CLASS-001-name.md
CLASS-001-purpose.md
CLASS-001-method1.md
CLASS-001-method2.md
CLASS-001-method3.md
CLASS-001-dependencies.md
```

só porque agentes conseguem navegar entre arquivos.

Isso cria um grafo extremamente fragmentado:

```text
          CLASS-001
          /   |   \
         /    |    \
      name purpose methods
                   / | \
```

O agente terá que fazer muitas operações de navegação.

---

Por outro lado, também não faria:

```text
entire-system.md
```

com 50.000 linhas.

A unidade que eu buscaria é:

> **um arquivo = um conceito que pode ser compreendido relativamente sozinho.**

Isso coincide bastante com a definição de _concept_ no OKF: cada conceito é representado como um documento Markdown. ([GitHub](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md?utm_source=chatgpt.com "knowledge-catalog/okf/SPEC.md at main · GoogleCloudPlatform/knowledge-catalog · GitHub"))

---

#### 5.1.2.6. Um exemplo para seu domínio

Eu consideraria:

```text
requirements/
    REQ-001-authentication.md

use-cases/
    UC-001-login.md

architecture/
    ARCH-001-layered-architecture.md

components/
    COMP-001-authentication-service.md

classes/
    CLASS-001-user.md
    CLASS-002-user-service.md

interfaces/
    IF-001-user-repository.md

patterns/
    PAT-001-repository.md

decisions/
    ADR-001-database.md
```

Cada arquivo suficientemente completo.

Por exemplo:

```text
CLASS-002-user-service.md
```

contém:

```text
metadata
+
responsabilidade
+
atributos
+
métodos
+
regras
+
relationships
+
constraints
+
examples
```

Não dividiria cada método em outro arquivo.

---

#### 5.1.2.7. Mas existe uma segunda dimensão: dentro do arquivo

Aqui está uma solução muito interessante para sua situação.

Você pode ter:

```
---
type: Class
title: UserService
---

## Summary

...

## Responsibilities

...

## Attributes

...

## Methods

...

## Relationships

...

## Constraints

...

## Examples

...
```

O agente não precisa necessariamente colocar tudo no contexto.

Ele pode pedir:

```text
CLASS-002
  └── # Methods
```

ou:

```text
CLASS-002
  └── # Relationships
```

Portanto você tem **duas granularidades**:

```text
                    Knowledge
                       │
                 ┌─────┴─────┐
                 │           │
              Concept       Concept
               file          file
                 │
          ┌──────┼──────┐
          │      │      │
        Summary Methods Relationships
```

Isso é muito melhor do que transformar cada seção em um arquivo.

---

#### 5.1.2.8. Isso permite uma estratégia de recuperação em camadas

Eu projetaria seu agente mais ou menos assim:

```text
                 User request
                      │
                      ▼
              ┌───────────────┐
              │ Determine task│
              └───────┬───────┘
                      │
                      ▼
              Read root index
                      │
                      ▼
             Select concept type
                      │
                      ▼
              Read concept metadata
                      │
                      ▼
             Read relevant sections
                      │
                      ▼
             Follow relationships
                      │
                      ▼
              Read related concepts
                      │
                      ▼
               Build context
                      │
                      ▼
                   Answer
```

Isso é essencialmente:

> **progressive disclosure + graph traversal + selective section retrieval.**

E acho que essa combinação é muito mais importante para seu projeto do que simplesmente "usar RAG".

---

#### 5.1.2.9. Um detalhe do OKF que acho especialmente importante para isso

O `description` do frontmatter não é apenas documentação bonita.

A especificação recomenda que ele seja usado para:

- gerar `index.md`;
    
- snippets de busca;
    
- previews. ([GitHub](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md?utm_source=chatgpt.com "knowledge-catalog/okf/SPEC.md at main · GoogleCloudPlatform/knowledge-catalog · GitHub"))
    

Então você poderia ter:

```yaml
---
type: Class
title: UserService
description: Coordinates user creation, authentication and persistence.
tags:
  - domain
  - authentication
  - service
---
```

O agente pode inicialmente receber somente:

```text
CLASS-001
User — Domain entity representing an authenticated user.

CLASS-002
UserService — Coordinates user creation, authentication and persistence.

CLASS-003
UserRepository — Provides persistence abstraction for User.
```

E só depois abrir o documento escolhido.

Isso é uma forma **muito barata de reduzir contexto**.

---

#### 5.1.2.10. E o `index.md` pode funcionar como um "mapa cognitivo"

Eu gosto bastante dessa possibilidade para o seu projeto.

Por exemplo:

```
## Domain Model

### Authentication

- [User](../classes/CLASS-001.md)
  Represents the authenticated user.

- [UserService](../classes/CLASS-002.md)
  Coordinates authentication operations.

- [AuthenticationRepository](../interfaces/IF-003.md)
  Persistence abstraction.

### Relationships

User
→ UserService
→ AuthenticationRepository
```

O agente primeiro lê:

```text
Domain Model index
```

e decide:

> "Para responder a essa pergunta preciso de UserService + AuthenticationRepository."

Em vez de receber:

```text
todos os 300 conceitos do domínio.
```

---

#### 5.1.2.11. Então eu faria uma distinção entre três coisas

Isso pode ser muito útil para a arquitetura que você está desenhando:

###### 5.1.2.11.1.1. Storage

```text
Markdown + YAML
```

###### 5.1.2.11.1.2. Knowledge structure

```text
hierarchy + links + relationships
```

###### 5.1.2.11.1.3. Retrieval

```text
agent
+
search
+
graph traversal
+
section extraction
```

São problemas diferentes.

```text
                 KNOWLEDGE
                     │
          ┌──────────┴──────────┐
          │                     │
       Storage              Structure
          │                     │
    Markdown/YAML          Graph/links
                                │
                                ▼
                           Retrieval
                                │
                    ┌───────────┼───────────┐
                    │           │           │
                  index       search      graph
                    │           │           │
                    └───────────┼───────────┘
                                ▼
                              Agent
```

**OKF resolve muito bem Storage + parte de Structure.**

Não resolve Retrieval.

---

#### 5.1.2.12. Minha recomendação concreta para sua KB

Para a sua aplicação, eu começaria com:

##### 5.1.2.12.1. Unidade

**1 arquivo = 1 conceito**

##### 5.1.2.12.2. Granularidade

Conceitos relativamente independentes, mas não microssegmentados.

##### 5.1.2.12.3. Estrutura

```text
knowledge/
├── index.md
├── requirements/
│   └── index.md
├── use-cases/
│   └── index.md
├── architecture/
│   └── index.md
├── components/
│   └── index.md
├── classes/
│   └── index.md
├── interfaces/
│   └── index.md
├── patterns/
│   └── index.md
├── decisions/
│   └── index.md
└── generation/
    └── index.md
```

##### 5.1.2.12.4. Cada conceito

```yaml
---
type:
title:
description:
tags:
status:
generated:
verified:
sources:
stale_after:
---
```

##### 5.1.2.12.5. Corpo

```
## Summary

## Responsibilities

## Relationships

## Constraints

## Examples
```

##### 5.1.2.12.6. Relationships

Eu adicionaria uma **convenção própria**, como:

```
## Relationships

- satisfies: [REQ-001](...)
- depends-on: [CLASS-002](...)
- implements: [IF-001](...)
- extends: [CLASS-003](...)
- uses-pattern: [PAT-001](...)
```

Isso permite seu parser construir um grafo tipado:

```text
                REQ-001
                   ▲
                satisfies
                   │
              CLASS-001
             /    |    \
      extends   uses    depends
          │       │        │
          ▼       ▼        ▼
      CLASS-002 PAT-001 CLASS-003
```

E, finalmente:

> **não obrigaria o LLM a decidir sozinho como navegar pelo filesystem.**

Criaria uma camada de conhecimento para o agente:

```text
Knowledge API

get_concept(id)
get_metadata(id)
get_section(id, section)
get_related(id, relation)
find(type, tags, query)
get_dependencies(id)
get_dependents(id)
get_requirements(id)
get_implementation(id)
```

Aí o agente trabalha em cima de **operações semânticas**, e não:

```text
"vou abrir ../foo/../bar.md e ver o que tem lá..."
```

Isso, na minha opinião, é onde a sua ideia começa a ficar realmente interessante: **OKF pode ser o formato persistente e interoperável, enquanto a sua aplicação constrói uma camada de navegação/retrieval específica para Model-Based Code Generation.**

E o mais importante: **essa camada pode ser derivada dos Markdown, sem transformar o grafo em sua fonte de verdade.** O próprio OKF segue essa filosofia — o visualizador oficial, por exemplo, deriva o grafo dos cross-links dos documentos. ([GitHub](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/README.md?utm_source=chatgpt.com "knowledge-catalog/okf/README.md at main · GoogleCloudPlatform/knowledge-catalog · GitHub"))

### 5.1.3. perguntas 02
- quero entender um pouco mais do que o modelo OKF em si já contém em termos de facilidades, disponibilizadas no github oficial:
	- do que se trata esse recurso instalável? ```python3.13 -m venv .venv  \n  .venv/bin/pip install --index-url https://pypi.org/simple/ -e .[dev]```
	- produtor okf: existe um agente de referencia mas, pelo que entendi, ele só gera os modelos de exemplo, mas não funcionaria para o meu caso, certo?
	- consumidor okf: como faço para usar o visualizador original?
- sobre a distinção dos tipos de knowledge base, entendo que existirão pelo menos 3 bases
	- sobre o sistema que estiver sendo construido pelo "model-based code generator"
	- sobre o proprio sistema "model-based code generator", que tambem será objeto de especificações e desenvolvimento
	- sobre a inteligencia (regras, skills, templates, etc) utilizada para interações usuario-agente, com ou sem harness ou loops automaticos, para especificação e desenvolvimento de sistemas via "model-based code generator"
- dessa forma pretendo adotar como modelos predominantes
	- para o sistema "model-based code generator" e seus "filhos" (sistemas criados com ele): adotar sua recomendação de "md (com convenção propria para o okf) + grafo" e adicionar (considero fundamental) o padrão UML, com arquivos tipo gaphor (gerado pelo aplicativo gaphor conforme o padrão XMI da OMG), o que acha? funciona bem? quais seriam os principais pontos de atenção?
	- para a inteligencia em si (item 3 acima): predominante md + grafo automatico (se possivel usando o consumidor original disponibilizado no github)

### 5.1.4. respostas 02

Sim — e, depois de olhar o repositório oficial atual, eu faria **uma pequena correção de rumo** em relação ao que discutimos antes: o OKF está mais interessante do que apenas “Markdown + YAML + links”. O **v0.2 adicionou provenance, trust, lifecycle e attestation**, além do visualizador de referência. ([GitHub][1])

#### 5.1.4.1. O que existe efetivamente no repositório oficial

##### 5.1.4.1.1. 1 O comando de instalação

Este trecho:

```bash
python3.13 -m venv .venv
.venv/bin/pip install --index-url https://pypi.org/simple/ -e .[dev]
```

não instala um “servidor OKF” nem uma infraestrutura de Knowledge Base.

Ele faz duas coisas:

1. cria um ambiente virtual Python;
2. instala **o próprio código desse repositório**, em modo `editable`, incluindo as dependências de desenvolvimento.

O `-e .[dev]` significa aproximadamente:

```text
.       → instale o projeto que está neste diretório
[dev]   → instale também as dependências opcionais de desenvolvimento
-e      → editable install
```

Ou seja, você clona:

```text
knowledge-catalog/
```

e dentro dele executa a instalação.

Isso disponibiliza, entre outras coisas, o `reference_agent` e o comando `visualize`. O README deixa explícito que esse agente é **proof of concept**, enquanto o formato OKF é a contribuição principal. ([GitHub][2])

##### 5.1.4.1.2. E aqui está uma distinção importante

**Para simplesmente criar seus próprios arquivos OKF, você não precisa instalar isso.**

Você pode fazer:

```text
my-kb/
├── index.md
├── requirements/
│   └── REQ-001.md
└── architecture/
    └── ARCH-001.md
```

e isso já é OKF.

O repositório oficial é útil para obter:

```text
reference producer
        +
reference consumer/visualizer
        +
exemplos
```

---

##### 5.1.4.1.3. 2 O Reference Producer

Sua interpretação está essencialmente correta.

O `reference_agent` não é:

> “um agente genérico para pegar qualquer projeto meu e transformá-lo em OKF”.

Ele demonstra uma **forma possível de produzir OKF automaticamente**.

O fluxo implementado atualmente é bastante específico:

```text
BigQuery metadata
       │
       ▼
concepts OKF
       │
       ▼
web crawler + LLM
       │
       ├── enrich existing concept
       ├── create reference concept
       └── skip
```

O README descreve duas passagens: uma sobre metadados do BigQuery e outra em que o LLM percorre URLs fornecidas como seeds e decide quais páginas são relevantes. ([GitHub][2])

Portanto, para o seu projeto:

**eu não usaria o `reference_agent` como produtor.**

Eu faria seu próprio produtor:

```text
Gaphor/XMI
      │
      ▼
XMI parser
      │
      ▼
Model
      │
      ├──────────────┐
      ▼              ▼
 UML concepts     Graph
      │
      ▼
   OKF .md
```

e:

```text
Requirements
Architecture
ADRs
Generation rules
etc.
      │
      ▼
   OKF writer
```

Você estaria usando **o padrão OKF**, mas implementando um producer adequado ao seu domínio.

---

##### 5.1.4.1.4. 3 O Visualizador oficial

Esse sim é particularmente interessante para você.

O comando documentado é:

```bash
.venv/bin/python -m reference_agent visualize \
    --bundle ./bundles/<name>
```

Ele gera:

```text
bundles/<name>/viz.html
```

O HTML é **self-contained**: depois de gerado, você abre no navegador e não precisa executar um servidor backend. ([GitHub][2])

Ele oferece:

* grafo force-directed;
* nós coloridos por `type`;
* arestas direcionadas pelos links Markdown;
* painel com frontmatter;
* Markdown renderizado;
* navegação pelos links internos;
* backlinks `"Cited by"`;
* busca;
* filtro por tipo;
* diferentes layouts do grafo. ([GitHub][2])

Portanto, para experimentar sua futura KB:

```text
knowledge/
   ↓
reference_agent visualize
   ↓
viz.html
   ↓
browser
```

é uma solução muito boa.

E tem uma característica importante para sua arquitetura:

> **o visualizador não possui um banco de grafos separado.**

Ele lê os arquivos, constrói o grafo a partir dos cross-links e embute o resultado no HTML. ([GitHub][2])

Isso reforça bastante a arquitetura que sugeri anteriormente:

```text
             Markdown = source of truth
                       │
                       ▼
                  parser/indexer
                       │
              ┌────────┴────────┐
              ▼                 ▼
          graph index       search index
```

---

#### 5.1.4.2. Suas três Knowledge Bases

Aqui concordo **fortemente** com sua separação.

Eu inclusive daria nomes diferentes para evitar que no futuro elas sejam confundidas.

##### 5.1.4.2.1. KB-1 — Product/System Knowledge

Conhecimento **do sistema que está sendo construído**.

```text
System KB
│
├── requirements
├── use-cases
├── architecture
├── components
├── classes
├── interfaces
├── data-model
├── decisions
├── constraints
└── generation specifications
```

Exemplo:

```text
Sistema: ERP
REQ-001
ARCH-003
CLASS-021
ADR-008
```

---

##### 5.1.4.2.2. KB-2 — Generator Knowledge

Conhecimento **sobre o próprio Model-Based Code Generator**.

```text
Generator KB
│
├── requirements
├── architecture
├── components
├── classes
├── UML model
├── generators
├── parsers
├── templates
├── supported languages
└── limitations
```

E isso é particularmente interessante porque o seu próprio generator passa a ser um **produto model-based**.

Você poderia inclusive ter:

```text
Generator
    │
    ├── próprio modelo UML
    ├── própria especificação OKF
    ├── próprio código
    └── própria documentação
```

---

##### 5.1.4.2.3. KB-3 — Agent Intelligence

Essa é diferente das duas anteriores.

Ela não descreve necessariamente um sistema.

Ela descreve **como a inteligência deve trabalhar**:

```text
Agent Intelligence KB
│
├── skills
├── workflows
├── rules
├── policies
├── prompts
├── templates
├── coding standards
├── modeling standards
├── retrieval strategies
├── validation rules
└── generation strategies
```

Por exemplo:

```text
skill:
  "derive classes from requirements"

rule:
  "every persistent entity must have repository abstraction"

template:
  "Flutter repository"

workflow:
  "requirement → architecture → UML → code"
```

Eu manteria essa separação.

---

##### 5.1.4.2.4. E aqui surge uma arquitetura que acho muito boa

Você acaba tendo:

```text
                 MODEL-BASED CODE GENERATOR
                            │
             ┌──────────────┼──────────────┐
             │              │              │
             ▼              ▼              ▼
          System KB     Generator KB   Intelligence KB
             │              │              │
             ▼              ▼              ▼
          "produto"      "ferramenta"    "como pensar"
```

Ou:

```text
         WHAT
          │
       System KB
          │
          ▼
         MODEL
          │
          ▼
         CODE

         HOW
          │
   Intelligence KB
          │
          ▼
       AGENTS

         TOOL
          │
     Generator KB
          │
          ▼
      Generator
```

Essa separação vai ser muito útil para evitar que regras do agente sejam confundidas com especificações do produto.

---

#### 5.1.4.3. Sua proposta de UML + OKF

Aqui eu concordo **quase integralmente**.

##### 5.1.4.3.1. Eu faria:

```text
System KB
│
├── Markdown + YAML
├── links / graph
└── UML model
      │
      └── Gaphor/XMI
```

E trataria os dois como representações complementares.

Não faria:

```text
Markdown → UML
```

como se um fosse simplesmente uma visualização do outro.

Eu faria:

```text
                  SYSTEM MODEL
                       │
          ┌────────────┴────────────┐
          │                         │
      Knowledge                  Formal Model
          │                         │
    OKF Markdown                  UML
          │                         │
       graph                     XMI
          │                         │
          └──────────┬──────────────┘
                     │
               Code Generator
```

---

##### 5.1.4.3.2. Por que isso é particularmente bom?

Porque Markdown e UML resolvem problemas diferentes.

###### 5.1.4.3.2.1. Markdown/OKF

Excelente para:

* requisitos;
* decisões;
* explicações;
* regras;
* constraints;
* rationale;
* exemplos;
* documentação;
* contexto;
* conhecimento gerado por agentes;
* provenance;
* instruções.

###### 5.1.4.3.2.2. UML/XMI

Excelente para:

* classes;
* interfaces;
* generalização;
* associação;
* composição;
* multiplicidade;
* atributos;
* operações;
* tipos;
* relacionamentos formais;
* diagramas;
* modelo estrutural.

Então:

```text
REQ-001.md

"Usuário deve poder autenticar..."
```

e:

```text
CLASS-001
CLASS-002
INTERFACE-003
```

no UML podem representar aspectos diferentes da mesma realidade.

---

##### 5.1.4.3.3. Mas eu colocaria uma regra fundamental

**Não deixe Markdown e XMI se tornarem duas fontes independentes da verdade.**

Esse é provavelmente o maior risco da arquitetura.

Imagine:

```text
REQ-001.md
```

diz:

```text
UserService autentica usuário.
```

Enquanto XMI diz:

```text
AuthenticationService
```

e o agente começa a interpretar os dois como autoridades independentes.

Você precisa estabelecer **ownership**.

Por exemplo:

| Informação                 | Fonte primária                |
| -------------------------- | ----------------------------- |
| Requisito                  | OKF/MD                        |
| Rationale                  | OKF/MD                        |
| ADR                        | OKF/MD                        |
| Regra de negócio textual   | OKF/MD                        |
| Classe                     | UML                           |
| Interface                  | UML                           |
| Associação                 | UML                           |
| Multiplicidade             | UML                           |
| Generalização              | UML                           |
| Diagrama                   | UML                           |
| Relação requisito → classe | OKF ou modelo de traceability |
| Código                     | source code                   |

Isso é extremamente importante.

---

##### 5.1.4.3.4. E eu adicionaria Traceability como uma camada explícita

Aqui sua aplicação pode ficar realmente poderosa.

Por exemplo:

```text
REQ-001
   │
   │ satisfies
   ▼
UC-001
   │
   │ realized-by
   ▼
CLASS-001
   │
   │ implements
   ▼
IF-001
   │
   │ generated-to
   ▼
src/user_service.dart
```

O OKF consegue representar muito bem a parte documental dessas relações através dos links. O UML representa a estrutura formal.

Mas eu criaria uma convenção de relações:

```text
satisfies
realizes
implements
depends-on
refines
derived-from
generated-from
verified-by
```

Assim seu grafo passa a ser **um grafo de engenharia de software**, não apenas um grafo de hyperlinks.

---

##### 5.1.4.3.5. Atenção: o XMI não deve virar a interface do agente

Esse seria outro ponto importante.

Eu **não faria**:

```text
Agent
  ↓
lê XMI diretamente
```

como mecanismo primário.

XMI é uma representação de intercâmbio de modelo. É excelente para máquinas e ferramentas UML, mas é muito menos amigável para LLMs.

Eu faria:

```text
                XMI
                 │
              parser
                 │
                 ▼
            UML model
                 │
        ┌────────┴────────┐
        ▼                 ▼
      graph             OKF
        │                 │
        └────────┬────────┘
                 ▼
               Agent
```

Ou seja:

**XMI é uma fonte formal do modelo; OKF é uma representação de conhecimento acessível ao agente.**

---

##### 5.1.4.3.6. Sobre Gaphor especificamente

Sua ideia de utilizar o arquivo de projeto do Gaphor/XMI é viável, mas eu faria uma ressalva importante.

Você precisa separar:

```text
UML interchange format
```

de:

```text
Gaphor project format
```

e verificar exatamente qual deles você pretende considerar como fonte persistente.

A arquitetura ideal seria:

```text
             Gaphor
                │
             XMI/UML
                │
                ▼
          UML importer
                │
                ▼
          Canonical Model
           /           \
          /             \
       XMI               OKF
                         │
                         ▼
                       Agent
```

Assim você não fica conceitualmente preso ao Gaphor.

Se amanhã decidir trocar:

```text
Gaphor
    ↓
Modelio
    ↓
Eclipse Papyrus
    ↓
outro UML tool
```

seu **modelo canônico** continua sendo o mesmo.

---

#### 5.1.4.4. Para a Intelligence KB eu faria ainda mais simples

Aqui sua proposta:

> **MD + grafo automático + visualizador oficial**

me parece excelente.

Algo como:

```text
intelligence/
│
├── index.md
│
├── skills/
│   ├── index.md
│   ├── derive-requirements.md
│   ├── derive-architecture.md
│   └── generate-code.md
│
├── rules/
│   ├── index.md
│   ├── naming.md
│   └── architecture.md
│
├── templates/
│   ├── index.md
│   └── flutter-service.md
│
├── workflows/
│   ├── index.md
│   └── system-development.md
│
└── policies/
    └── validation.md
```

Cada arquivo é um conceito.

E:

```text
generate-code.md
```

poderia referenciar:

```text
skill
   │
   ├── uses → architecture-rule
   ├── uses → flutter-template
   ├── requires → UML-model
   └── produces → source-code
```

O visualizador oficial consegue transformar esses cross-links em grafo automaticamente. ([GitHub][2])

---

#### 5.1.4.5. Uma coisa que eu mudaria na sua ideia

Eu não chamaria simplesmente de:

> `MD + grafo automático`

Eu pensaria em:

> **OKF + semantic graph derived from OKF**

porque o grafo não deve ser uma segunda base independente.

```text
              OKF repository
                   │
                   │ parse
                   ▼
              Graph index
                   │
          ┌────────┼─────────┐
          │        │         │
       viewer    retrieval  analysis
```

Isso deixa a arquitetura muito mais limpa.

O próprio visualizador oficial segue exatamente essa ideia: ele deriva as arestas dos cross-links dos Markdown e calcula backlinks a partir do grafo reverso. ([GitHub][2])

---

#### 5.1.4.6. E existe uma descoberta importante para seu projeto

O OKF **explicitamente permite extensões**.

O `type` não possui um catálogo central obrigatório e produtores podem acrescentar outros campos de frontmatter; consumidores devem tolerar tipos e campos desconhecidos. ([GitHub][1])

Isso significa que você poderia estabelecer algo como:

```yaml
---
type: uml-class
title: UserService
uml:
  xmi_id: "_abc123"
  qualified_name: "domain::UserService"
  source: "../model/model.xmi"
---
```

ou:

```yaml
---
type: requirement
id: REQ-001
uml:
  verified: true
traceability:
  satisfies:
    - UC-001
---
```

**sem deixar de ser OKF**, desde que você mantenha as regras fundamentais.

Eu, porém, evitaria colocar muita coisa no frontmatter. Preferiria:

```yaml
---
type: uml-class
title: UserService
xmi_id: _abc123
---
```

e deixar a maior parte das informações no corpo/links.

---

#### 5.1.4.7. Minha arquitetura recomendada para você

Considerando tudo o que você descreveu, eu chegaria a isto:

```text
                         MB-CODE-GENERATOR
                                  │
            ┌─────────────────────┼─────────────────────┐
            │                     │                     │
            ▼                     ▼                     ▼
       SYSTEM KB            GENERATOR KB         INTELLIGENCE KB
            │                     │                     │
       ┌────┴────┐           ┌────┴────┐           ┌────┴────┐
       │         │           │         │           │         │
      OKF       UML          OKF       UML         OKF      Graph
       │         │           │         │           │
       │        XMI          │        XMI          │
       │         │           │         │           │
       └────┬────┘           └────┬────┘           │
            │                     │                │
            └──────────┬──────────┴────────────────┘
                       │
                       ▼
                KNOWLEDGE ENGINE
                       │
            ┌──────────┼──────────┐
            │          │          │
          Search      Graph     Retrieval
            │          │          │
            └──────────┼──────────┘
                       │
                       ▼
                     Agent
                       │
                       ▼
                 Code Generator
```

E eu definiria uma regra arquitetural:

> **OKF/Markdown = conhecimento discursivo + metadados + traceability.**
>
> **UML/XMI = modelo formal estrutural/comportamental.**
>
> **Graph = índice derivado dos dois.**
>
> **Agent = consumidor, nunca fonte implícita de verdade.**

---

#### 5.1.4.8. Um último ponto que considero muito importante

O OKF v0.2 ainda está **deliberadamente incompleto como protocolo de execução/serving**. A própria especificação diz que não define storage, serving, query infrastructure nem um runtime; e algumas partes, como o protocolo completo de attestation, foram deixadas para versões futuras. ([GitHub][1])

Isso não é necessariamente uma fraqueza para seu projeto. Pelo contrário: **eu evitaria acoplar seu Model-Based Code Generator ao runtime do repositório Google**.

Use o OKF como **formato de interoperabilidade** e o visualizador oficial como uma ferramenta auxiliar. Construa a sua camada de conhecimento/retrieval acima dele.

Isso também deixa aberta a possibilidade de futuramente seu próprio agente expor operações como:

```text
get_requirement()
get_related_concepts()
get_uml_class()
get_traceability()
get_generation_rule()
get_skill()
get_template()
find_by_type()
find_by_tag()
find_path()
```

sem que o agente precise conhecer a estrutura física da KB.

**Essa, para mim, é a evolução natural da arquitetura que você está desenhando.**

[1]: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md?utm_source=chatgpt.com "knowledge-catalog/okf/SPEC.md at main · GoogleCloudPlatform/knowledge-catalog · GitHub"
[2]: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/README.md?utm_source=chatgpt.com "knowledge-catalog/okf/README.md at main · GoogleCloudPlatform/knowledge-catalog · GitHub"



### 5.1.5. perguntas 03
1. sobre "ownership [md, uml] de temas + convenção de relações (traceability)", existe alguma norma ou convenção de modelagem que eu possa seguir para isso?
2. sobre "XMI não deve virar a interface do agente"
   - eu imaginei que o agente teria facilidade com XMI, pois é um XML que segue os padrões UML 
   - existe alguma ferramenta open source, ou biblioteca python, disponível? 
   - em linhas gerais, como seria o parse de XMI para [md, graph]? 


### 5.1.6. respostas 03

Sim. Pesquisei especificamente a parte de **UML/XMI, traceability e ferramentas Python**, e eu faria uma distinção importante entre três níveis: **norma**, **modelo canônico** e **formato de consumo pelo agente**.

#### 5.1.6.1. Existe uma norma para o ownership MD × UML + traceability?

**Não existe uma norma única que diga "este tipo de informação deve ficar em Markdown e aquele em UML".** Essa decisão é arquitetural.

Mas existem padrões OMG que dão uma base muito boa para você não inventar tudo.

##### 5.1.6.1.1. O principal candidato é SysML

Embora seu domínio seja software, eu estudaria **SysML**, especialmente o conceito de *requirements modeling* e relações de rastreabilidade.

O SysML foi justamente criado para especificação, análise, projeto e verificação de sistemas, e inclui mecanismos para relacionar requisitos com outros elementos do modelo. A especificação usa relações como:

* `deriveReqt`
* `satisfy`
* `verify`
* `refine`
* `trace`

e `allocate` para alocação entre elementos. ([OMG][1])

Isso é muito próximo do que você chamou de:

```text
REQ
  │
  ├── satisfies
  ├── derives
  ├── verifies
  ├── refines
  └── traces
```

Por exemplo:

```text
REQ-001
   │
   │ satisfy
   ▼
CLASS-001
```

ou:

```text
REQ-001
   │
   │ verify
   ▼
TEST-001
```

Então, para **traceability**, eu não inventaria uma taxonomia do zero. Eu começaria estudando a terminologia de SysML e adotaria o que fizer sentido.

---

##### 5.1.6.1.2. UML também possui `Trace`

O UML possui o conceito de `Trace`/`Abstraction`, mas ele é deliberadamente genérico.

Por isso, para seu caso, eu vejo:

```text
UML
 └── estrutura do software

SysML
 └── requisitos + rastreabilidade
```

como uma combinação conceitualmente interessante.

A especificação SysML inclusive define `Trace` como uma relação entre requisitos e elementos do modelo, e existem relações especializadas para `satisfy`, `verify`, `deriveReqt` etc. ([OMG Issue Tracker][2])

---

#### 5.1.6.2. Eu faria ownership assim

Em vez de procurar uma norma que diga exatamente onde cada informação deve ficar, estabeleceria uma **Architecture Decision** do seu próprio sistema:

| Informação               | Fonte de verdade |
| ------------------------ | ---------------- |
| Requisito textual        | OKF/Markdown     |
| Rationale                | OKF/Markdown     |
| Critérios de aceitação   | OKF/Markdown     |
| ADR                      | OKF/Markdown     |
| Regra de negócio textual | OKF/Markdown     |
| Skill/regra de agente    | Intelligence KB  |
| Classe                   | UML              |
| Interface                | UML              |
| Atributo                 | UML              |
| Operação                 | UML              |
| Associação               | UML              |
| Generalização            | UML              |
| Multiplicidade           | UML              |
| Composição/agregação     | UML              |
| Diagrama                 | UML              |
| Dependência estrutural   | UML              |
| Requisito → elemento UML | Traceability     |
| Elemento UML → código    | Traceability     |
| Código                   | código-fonte     |

E colocaria uma regra:

> **Se uma informação tem uma representação formal no modelo UML, o UML é a autoridade para aquela informação.**

Por exemplo, não permitiria:

```
CLASS-001.md

Atributos:
- name: String
- age: int
```

e simultaneamente:

```text
CLASS-001 no UML

name: String
birthDate: Date
```

Isso cria duas verdades concorrentes.

Melhor:

```text
CLASS-001.md

## User

Representa o usuário do sistema.

[modelo UML](...)
```

e os atributos ficam exclusivamente no UML.

---

#### 5.1.6.3. Onde eu colocaria a traceability?

Aqui eu faria uma coisa um pouco diferente da minha sugestão anterior.

**Não colocaria necessariamente a relação somente no Markdown.**

Eu permitiria que ela existisse no **modelo formal**, quando a ferramenta/modelo suportar isso.

Por exemplo, conceitualmente:

```text
REQ-001
   │
   │ satisfy
   ▼
CLASS-001
```

poderia estar no modelo UML/SysML.

E o OKF poderia expor a mesma relação para os agentes:

```
## Traceability

- satisfies: [REQ-001](../requirements/REQ-001.md)
```

Mas isso cria duplicação.

Então eu estabeleceria:

> **uma relação possui uma fonte de verdade; as demais representações são projeções.**

Por exemplo:

```text
              Canonical Model
                    │
          ┌─────────┴─────────┐
          │                   │
          ▼                   ▼
        XMI                  OKF
          │                   │
          ▼                   ▼
       Gaphor               Agent
```

Ou, se o requisito nasce no OKF:

```text
       OKF Requirement
              │
              ▼
       Traceability Model
              │
              ▼
          UML/XMI
```

Isso evita inconsistência.

---

#### 5.1.6.4. Sobre sua hipótese: "o agente teria facilidade com XMI"

Aqui eu faria uma correção na minha afirmação anterior:

**Sim, um LLM consegue ler XMI.**

E, para alguns tipos de tarefas, ele pode até fazer isso razoavelmente bem.

O problema não é:

> "LLM não entende XML."

Ele entende.

O problema é:

> **XMI é uma representação de intercâmbio de modelo, não uma representação otimizada para recuperação seletiva de conhecimento.**

---

##### 5.1.6.4.1. Por que XMI pode ser ruim como interface direta?

Imagine algo conceitualmente simples:

```text
User
 ├── name: String
 └── repository: UserRepository
```

No modelo UML isso é relativamente simples.

Em XMI você pode acabar com algo próximo de:

```xml
<packagedElement
    xmi:type="uml:Class"
    xmi:id="_abc"
    name="User">

    <ownedAttribute
        xmi:id="_def"
        name="name"
        type="_string"/>

    <ownedAttribute
        xmi:id="_ghi"
        name="repository"
        type="_xyz"/>
</packagedElement>
```

E depois:

```xml
<xmi:Extension ...>
...
</xmi:Extension>
```

e referências:

```xml
type="_xyz"
```

que apontam para outro lugar.

Então o agente precisa fazer:

```text
XMI
 │
 ├── descobrir namespace
 ├── descobrir metamodel
 ├── resolver IDs
 ├── resolver referências
 ├── entender stereotypes
 ├── interpretar containment
 ├── interpretar multiplicities
 └── reconstruir relações
```

O XML não é o problema.

**O problema é que XMI é serialização, não a estrutura cognitiva mais conveniente para consulta.**

---

#### 5.1.6.5. E há uma questão ainda mais importante: XMI não é "UML XML"

Essa distinção é fundamental.

Você disse:

> "XMI que segue os padrões UML"

Mais precisamente:

```text
UML
  │
  │ define metamodel
  ▼
UML metamodel
  │
  │ serializado usando
  ▼
XMI
```

**XMI é um padrão de intercâmbio/serialização de modelos da OMG.**

A OMG disponibiliza tanto a especificação XMI 2.5.1 quanto os artefatos XMI do metamodelo UML 2.5.1. ([OMG][3])

Portanto:

```text
XMI ≠ UML
```

e:

```text
XMI + UML metamodel = representação de um modelo UML
```

Isso também explica por que dois arquivos XMI de ferramentas diferentes podem ser significativamente diferentes.

---

#### 5.1.6.6. Existem bibliotecas Python?

**Sim — e uma delas é especialmente relevante para seu projeto: PyEcore.**

[PyEcore documentation](https://pyecore.readthedocs.io/en/latest/?utm_source=chatgpt.com)

PyEcore é uma implementação Python do **EMF/Ecore**, com uma API inspirada no EMF Java.

Ele suporta explicitamente:

* carregar modelos;
* salvar modelos;
* metamodelos;
* relacionamentos;
* XMI serialization;
* XMI deserialization;
* navegação reflexiva. ([PyEcore Documentation][4])

Isso é muito mais interessante do que fazer:

```python
ElementTree.parse("model.xmi")
```

e ficar manualmente procurando:

```python
find("packagedElement")
find("ownedAttribute")
...
```

---

#### 5.1.6.7. Por que PyEcore é particularmente interessante?

Porque você quer fazer **Model Driven Engineering**.

E PyEcore é justamente um framework de MDE para Python.

A arquitetura poderia ser:

```text
                 Gaphor
                    │
                    ▼
                   XMI
                    │
                    ▼
                 PyEcore
                    │
                    ▼
              UML Model API
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
       Graph                OKF
          │                   │
          └─────────┬─────────┘
                    ▼
                  Agent
```

Isso é muito melhor do que:

```text
XMI → XML parser → regex → Markdown
```

---

#### 5.1.6.8. Mas existe um ponto de atenção enorme com Gaphor

**Eu não assumiria que "PyEcore consegue ler XMI" significa "PyEcore consegue ler qualquer XMI gerado pelo Gaphor".**

São coisas diferentes.

Você precisa verificar:

```text
Gaphor
  ↓
qual versão UML?
  ↓
qual versão XMI?
  ↓
qual metamodelo?
  ↓
quais namespaces?
  ↓
quais extensões?
  ↓
PyEcore
```

E principalmente:

> **qual é exatamente o formato que o Gaphor exporta?**

Porque uma ferramenta UML pode utilizar XMI como mecanismo de persistência/intercâmbio e ainda introduzir extensões próprias.

Portanto eu faria um pequeno POC antes de decidir a arquitetura.

---

#### 5.1.6.9. Como seria o parse XMI → MD + Graph?

Eu não faria:

```text
XMI
 │
 ├──→ Markdown
 └──→ Graph
```

diretamente.

Faria:

```text
                       XMI
                        │
                        ▼
                 XMI importer
                        │
                        ▼
                 Canonical UML
                    Model API
                        │
              ┌─────────┴─────────┐
              │                   │
              ▼                   ▼
          Graph builder       OKF generator
              │                   │
              ▼                   ▼
         Graph index          Markdown
```

Esse **Canonical UML Model** é uma peça importantíssima.

---

#### 5.1.6.10. Exemplo

Suponha que o XMI represente:

```text
User
 ├── id: UUID
 ├── name: String
 └── authenticate()
```

e:

```text
UserService
 └── userRepository: UserRepository
```

e:

```text
UserService → UserRepository
```

O parser cria internamente:

```python
UMLModel(
    classes=[
        UMLClass(
            id="_abc",
            name="User",
            attributes=[...],
            operations=[...],
        ),
        UMLClass(
            id="_def",
            name="UserService",
            ...
        ),
    ],
    relationships=[
        UMLDependency(
            source="_def",
            target="_ghi",
        )
    ]
)
```

Isso é o seu **modelo intermediário**.

---

#### 5.1.6.11. Depois você produz o grafo

Por exemplo:

```text
Node:
    id = _abc
    type = uml-class
    name = User

Node:
    id = _def
    type = uml-class
    name = UserService

Edge:
    source = _def
    target = _ghi
    type = depends-on
```

O grafo pode ficar:

```text
UserService
     │
     │ depends-on
     ▼
UserRepository
```

E isso pode alimentar:

* visualizador;
* retrieval;
* análise arquitetural;
* validação;
* agente.

---

#### 5.1.6.12. Depois você gera o OKF

Por exemplo:

```text
classes/
    CLASS-001-user.md
```

```yaml
---
type: uml-class
id: CLASS-001
title: User
uml_id: _abc
---
```

E:

```
## User

Representa o usuário autenticado do sistema.

### Attributes

Os atributos estruturais são definidos no modelo UML.

### Operations

As operações são definidas no modelo UML.

### Relationships

- used-by: [UserService](CLASS-002-user-service.md)
```

Mas perceba uma coisa:

**eu não duplicaria todos os atributos UML no Markdown.**

O Markdown poderia ser:

```text
conceitual/documental
```

enquanto o UML permanece:

```text
estrutural/formal
```

---

#### 5.1.6.13. E você pode gerar uma representação "Agent-friendly"

Aqui acho que está a oportunidade mais interessante.

O agente não precisa receber:

```xml
<XMI>
  <uml:Package>
    ...
```

nem necessariamente:

```
## User

...
```

Você pode ter uma API:

```text
get_class("User")
```

retornando algo conceitualmente como:

```json
{
  "type": "uml-class",
  "name": "User",
  "attributes": [
    {"name": "id", "type": "UUID"},
    {"name": "name", "type": "String"}
  ],
  "operations": [
    {"name": "authenticate"}
  ],
  "relationships": [
    {
      "type": "used-by",
      "target": "UserService"
    }
  ]
}
```

Então:

```text
XMI
 ↓
Canonical Model
 ↓
Knowledge API
 ↓
Agent
```

Isso é, na minha opinião, superior a simplesmente jogar o XMI inteiro no contexto.

---

#### 5.1.6.14. E o mais interessante: o agente pode pedir exatamente o que precisa

Por exemplo:

```text
get_class("User")
```

ou:

```text
get_class_attributes("User")
```

ou:

```text
get_class_relationships("User")
```

ou:

```text
get_related_classes("User", depth=2)
```

ou:

```text
get_implementations("UserRepository")
```

ou:

```text
trace("REQ-001")
```

Então você consegue implementar exatamente aquela estratégia que discutimos anteriormente:

> **ler o conhecimento certo no momento certo.**

---

#### 5.1.6.15. Eu adotaria esta arquitetura

Para o seu caso, depois dessas perguntas, eu refinaria minha recomendação para:

```text
                         SOURCE MODELS
                              │
               ┌──────────────┼──────────────┐
               │              │              │
               ▼              ▼              ▼
             Gaphor          OKF          Source Code
               │              │
              XMI            MD
               │              │
               └──────┬───────┘
                      ▼
              Knowledge Compiler
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
     Canonical     Graph       Search
      Model        Index       Index
          │           │           │
          └───────────┼───────────┘
                      ▼
                Knowledge API
                      │
                      ▼
                    Agent
```

Eu chamaria esse componente de algo como:

> **Knowledge Compiler**

porque ele transforma os artefatos de engenharia em uma representação consultável pelos agentes.

---

#### 5.1.6.16. E há uma consequência importante para sua decisão UML

Eu **não usaria apenas UML puro** se o seu objetivo inclui requisitos e rastreabilidade.

Eu avaliaria:

##### 5.1.6.16.1. Opção A — UML + OKF

```text
UML → estrutura
OKF → requisitos/documentação
```

Mais simples.

##### 5.1.6.16.2. Opção B — UML + conceitos de SysML + OKF

```text
UML → estrutura
SysML concepts → requirements/traceability
OKF → documentação/knowledge
```

Mais rico.

##### 5.1.6.16.3. Opção C — SysML como modelo formal principal

```text
SysML → requirements + structure + traceability
OKF → knowledge/documentation
```

É a opção mais "MBSE", mas provavelmente mais pesada para o seu **Model-Based Code Generator**.

**Eu começaria pela A, mas estudaria B seriamente.**

A OMG mantém UML 2.5.1 como especificação formal e disponibiliza o metamodelo UML em XMI; para SysML, a versão 1.7 foi adotada em 2024 e SysML v2 em 2025. ([OMG][5])

---

#### 5.1.6.17. Minha recomendação final neste momento

Eu faria um **POC extremamente pequeno antes de definir tudo**:

```text
Gaphor
  │
  │ export
  ▼
sample.xmi
  │
  ▼
PyEcore
  │
  ▼
UML classes / attributes / associations
  │
  ├──────────────► Graph
  │
  └──────────────► OKF Markdown
```

Com apenas:

```text
User
UserService
UserRepository
```

e:

```text
UserService → UserRepository
UserService → User
```

Se o Gaphor → XMI → PyEcore funcionar bem para esse caso, você terá validado uma parte **muito importante** da arquitetura.

E eu acrescentaria ao POC uma quarta saída:

```text
XMI
 ↓
Canonical Model
 ↓
┌────────────┬────────────┬─────────────┐
│            │            │             │
Graph        OKF          JSON/API      UML
```

Se essas quatro representações conseguirem ser geradas consistentemente a partir do mesmo **Canonical Model**, você terá encontrado uma arquitetura muito sólida para o seu projeto.

**O ponto central passa a ser o `Canonical Model`, não o XMI nem o Markdown.** XMI vira o formato de intercâmbio com a ferramenta UML; OKF vira o formato de conhecimento interoperável; Graph vira índice; e a Knowledge API vira a interface do agente.

[1]: https://www.omg.org/sysml/sysmlv1/?utm_source=chatgpt.com "SysML® v1 Specification | Object Management Group"
[2]: https://issues.omg.org/issues/SYSML17-176?utm_source=chatgpt.com "SysML 1.7 RTF — Open Issues - OMG Issue Tracker"
[3]: https://www.omg.org/spec/XMI?utm_source=chatgpt.com "About the XML Metadata Interchange Specification Version 2.5.1"
[4]: https://pyecore.readthedocs.io/en/latest/?utm_source=chatgpt.com "PyEcore Documentation — PyEcore 0.14.0 documentation"
[5]: https://www.omg.org/spec/UML/2.5.1/About-UML/?utm_source=chatgpt.com "About the Unified Modeling Language Specification Version 2.5.1"


## 5.2. descartavel
### 5.2.1. Então onde entra o Google?

O Google **define/publica a especificação** e também possui ferramentas/ecossistema que podem trabalhar com ela.

Mas existe uma separação importante:

```text
                    Open Knowledge Format
                              │
              ┌───────────────┴───────────────┐
              │                               │
          ESPECIFICAÇÃO                  FERRAMENTAS
              │                               │
       Markdown + YAML                 Google Cloud
              │                       outros projetos
              │                       seus próprios agentes
              │                       scripts Python
              │                       LangChain
              │                       etc.
```

O próprio Google enfatiza que OKF é **"format, not platform"**: ele não é amarrado a cloud, banco, modelo ou framework de agentes. ([Google Cloud](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing?utm_source=chatgpt.com "How the Open Knowledge Format can improve data sharing | Google Cloud Blog"))

Isso é particularmente relevante para a sua aplicação de **model-based code generation**.

---

### 5.2.2. OKF não é uma Knowledge Base pronta

Aqui está provavelmente a distinção mais importante.

Você pode pensar em:

> **OKF = formato da base de conhecimento**

e não:

> **OKF = sistema de banco de conhecimento**

Por exemplo, imagine que sua aplicação tenha:

```text
knowledge/
├── requirements/
├── use-cases/
├── architecture/
├── components/
├── classes/
├── interfaces/
├── design-patterns/
├── decisions/
└── code-generation/
```

Isso pode ser uma base OKF perfeitamente válida.

Mas o OKF **não resolve sozinho**:

- busca semântica;
    
- embeddings;
    
- RAG;
    
- ranking;
    
- autorização;
    
- controle de usuários;
    
- interface gráfica;
    
- sincronização;
    
- banco de dados;
    
- execução de agentes;
    
- geração de código;
    
- validação dos modelos;
    
- consistência entre requisitos e classes.
    

Essas coisas ficam **acima do OKF**.

---

### 5.2.3. E isso combina muito bem com sua ideia

Pelo que você está investigando para sua aplicação de **Model Based Code Generation**, eu vejo uma arquitetura interessante:

```text
                    ┌──────────────────────┐
                    │       Usuário        │
                    └──────────┬───────────┘
                               │
                    ┌──────────▼───────────┐
                    │  Model Based Code    │
                    │      Generator       │
                    └──────────┬───────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │                           │
          ┌──────▼──────┐             ┌──────▼──────┐
          │    Agent     │             │   Designer   │
          │   / LLM      │             │    / User    │
          └──────┬──────┘             └──────┬──────┘
                 │                           │
                 └─────────────┬─────────────┘
                               │
                    ┌──────────▼───────────┐
                    │    Knowledge Layer   │
                    │                      │
                    │       OKF            │
                    └──────────┬───────────┘
                               │
          ┌────────────────────┼────────────────────┐
          │                    │                    │
     Requirements         Architecture         Design Model
          │                    │                    │
          ▼                    ▼                    ▼
       REQ-001              ARCH-001             CLASS-001
       REQ-002              ARCH-002             CLASS-002
```

E aí você pode adicionar posteriormente um mecanismo de busca:

```text
                 OKF files
                    │
        ┌───────────┼───────────┐
        │           │           │
       Git        Parser      Indexer
        │           │           │
        │           │      ┌────▼─────┐
        │           │      │ Full Text│
        │           │      │  Search  │
        │           │      └────┬─────┘
        │           │           │
        │           │      ┌────▼─────┐
        │           └─────►│  Vector  │
        │                  │  Search  │
        │                  └────┬─────┘
        │                       │
        └───────────────────────▼
                              Agent
```

E nada disso precisa fazer parte do OKF.

---

### 5.2.4. Você não precisa de RAG inicialmente

Isso também é importante.

Se sua base tiver, por exemplo:

```text
knowledge/
├── requirements/
│   ├── REQ-001.md
│   ├── REQ-002.md
│   └── REQ-003.md
├── architecture/
│   └── ARCH-001.md
└── classes/
    ├── CLASS-001.md
    └── CLASS-002.md
```

Seu agente pode simplesmente receber:

```text
Leia knowledge/index.md.

Para implementar REQ-001:
1. leia REQ-001
2. siga os links relacionados
3. leia ARCH-001
4. leia CLASS-001
5. proponha a implementação
```

Ou seja:

**OKF permite uma abordagem baseada em navegação de conhecimento**, não necessariamente baseada em embeddings.

Depois, quando a base ficar grande:

```text
                  Knowledge OKF
                       │
             ┌─────────┴─────────┐
             │                   │
        navegação              busca
        estrutural           semântica
             │                   │
          links              embeddings
             │                   │
             └─────────┬─────────┘
                       │
                      Agent
```

---

### 5.2.5. Credenciais só aparecem quando você adicionar serviços

Por exemplo, se você decidir:

#### 5.2.5.1. Armazenamento local

```text
OKF
 ↓
Git
 ↓
filesystem
```

**Zero credenciais.**

---

#### 5.2.5.2. GitHub/GitLab

```text
OKF
 ↓
Git repository
 ↓
GitHub
```

Aí você precisa das credenciais do GitHub/GitLab, mas **isso não tem relação com OKF**.

---

#### 5.2.5.3. Google Cloud

```text
OKF
 ↓
Google Cloud service
```

Aí entram:

- projeto Google Cloud;
    
- autenticação;
    
- IAM;
    
- eventualmente APIs;
    
- eventualmente billing.
    

Novamente, isso é dependência **do serviço que você escolheu**, não do OKF.

---

#### 5.2.5.4. OpenAI / Gemini / Claude

```text
OKF
 ↓
Agent
 ↓
LLM
```

Aí você terá a credencial da API correspondente.

Mas o agente poderia ser:

```text
GPT
Gemini
Claude
Llama
Qwen
modelo local
```

O OKF não se importa.

---

### 5.2.6. Existe uma ferramenta oficial?

O repositório oficial do Google é o **GoogleCloudPlatform/knowledge-catalog**, que contém a especificação e material relacionado ao OKF. ([GitHub](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md?utm_source=chatgpt.com "knowledge-catalog/okf/SPEC.md at main · GoogleCloudPlatform/knowledge-catalog · GitHub"))

[GoogleCloudPlatform/knowledge-catalog — OKF](https://github.com/GoogleCloudPlatform/knowledge-catalog?utm_source=chatgpt.com)

A especificação atual é relativamente pequena e vale mais a pena **ler a especificação do que começar instalando alguma ferramenta**.

---


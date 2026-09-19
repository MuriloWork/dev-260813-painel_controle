# 1. resumo
Pesquisei os principais caminhos atuais, focando em API gratuita + modelos gratuitos + algum mecanismo real de reutilização de contexto/prefixo. O resultado é mais restrito do que parece.

Provedor / runtime	Modelos gratuitos	Cache de contexto/prefixo	Como funciona	Controle	Adequado ao MBCG?

[Groq](https://groq.com/?utm_source=chatgpt.com)	GPT-OSS 20B/120B, entre outros no free tier	Sim — Prefix/Prompt Caching	Cache automático do prefixo idêntico	Automático; TTL ~2h	★★★★★
[Google Gemini API](https://ai.google.dev/?utm_source=chatgpt.com)	Gemini 2.5 Flash/Flash-Lite etc.	Sim, implicit caching, mas context caching explícito não é gratuito	Cache automático de prefixos	Automático	★★★☆☆
[OpenRouter](https://openrouter.ai/?utm_source=chatgpt.com)	25+ modelos gratuitos	Depende do provider/modelo	OpenRouter encaminha para providers que suportam caching	Parcial; sticky routing ajuda a manter cache	★★★★☆
vLLM (self-hosted)	Qualquer modelo open-weight que você hospede	Sim — Automatic Prefix Caching	Reutilização direta do KV cache entre requests	Você controla	★★★★★
NVIDIA NIM (self-hosted)	Modelos open-weight suportados	Sim — KV Cache Reuse / Prefix Caching	Reutilização do KV cache	Você controla	★★★★★


# 2. Groq é atualmente a opção gratuita mais interessante

O Groq implementa prompt caching automático para alguns modelos, atualmente incluindo GPT-OSS 20B e 120B. O cache procura prefixos exatamente iguais entre requests; não exige nenhuma alteração no código. O cache tem expiração automática e os tokens cacheados recebem 50% de desconto quando há cobrança. 

Mais importante para seu caso: o free plan inclui esses modelos, embora com limites de requisições/tokens. 

# 3. Gemini

O Gemini possui implicit caching para modelos recentes: você simplesmente repete o prefixo e o sistema tenta reutilizá-lo. Porém, a tabela atual do Google mostra que o context caching explicitamente cobrado não está disponível no Free Tier. 

Portanto, eu não escolheria Gemini se o objetivo principal do experimento for ter controle explícito sobre uma camada persistente de contexto.

# 4. OpenRouter

É interessante porque você pode acessar gratuitamente vários modelos através de uma API única. 

Mas há uma ressalva: o caching de prompt é delegado ao provider que efetivamente executa o modelo. O OpenRouter usa sticky routing para aumentar a chance de reencontrar o cache. 

Portanto, não é uma camada de KV-cache própria e controlável por você.

# 5. Se você quiser realmente controlar a arquitetura

A opção mais interessante é self-hosted vLLM:
```
MBCG
                   │
              LangGraph
                   │
             Context Builder
                   │
                   ▼
              vLLM Server
                   │
          ┌────────┴────────┐
          │   Prefix Cache   │
          │     KV Cache     │
          └────────┬────────┘
                   │
                   ▼
                  LLM
```

Aqui você realmente controla o mecanismo. O vLLM possui Automatic Prefix Caching, reutilizando o KV cache de partes já processadas do prompt.

# 6. NVIDIA NIM 
oferece essencialmente a mesma ideia sob o nome KV Cache Reuse, também chamado de prefix caching, inclusive com configuração explícita para habilitá-lo. 

# 7. Eu separaria duas coisas:

1. Para prototipar sem custo:
	- Groq + GPT-OSS 20B/120B
2. Para construir a arquitetura definitiva:
	- vLLM + modelo open-weight + Automatic Prefix Caching

Porque no segundo caso você não fica dependente de como cada provedor implementa "prompt caching". Você controla diretamente:
```
Persistent Context
        ↓
Context Builder
        ↓
prefixo estável
        ↓
vLLM Prefix Cache
        ↓
LLM
```

# 8. opencode API

## 8.1. aproveitar o que o OpenCode já resolveu
faz sentido tratá-lo como uma camada de execução do agente, em vez de reproduzir em Python o gerenciamento de contexto/cache.

Um resumo conceitual:

| Recurso do OpenCode                    | Papel                                                          | Persistência      |
| -------------------------------------- | -------------------------------------------------------------- | ----------------- |
| `AGENTS.md`                            | Instruções/contexto persistente do projeto                     | Arquivo           |
| `CLAUDE.md` / outros instruction files | Instruções adicionais compatíveis                              | Arquivo           |
| **Session**                            | Histórico e estado da interação                                | Persistente       |
| **Messages**                           | Conversas, tool calls e resultados                             | Na sessão         |
| **Context / prompt**                   | Conteúdo efetivamente enviado ao LLM                           | Por request       |
| **Prompt caching**                     | Reutilização de prefixos estáveis                              | Provider/runtime  |
| **Compaction**                         | Resume contexto quando a janela fica cheia                     | Atualiza a sessão |
| **Tools**                              | Produzem contexto dinamicamente                                | Por execução      |
| **Subagents**                          | Contextos/sessões separados para tarefas específicas           | Sessão própria    |
| **Skills**                             | Conhecimento/instruções especializadas carregáveis sob demanda | Arquivos          |

A arquitetura fica aproximadamente:

```text
                 OpenCode
                    │
        ┌───────────┴───────────┐
        │                       │
   Persistent              Session
   Instructions            / History
   AGENTS.md                   │
        │                       │
        └───────────┬───────────┘
                    ▼
             Context Builder
                    │
          ┌─────────┴─────────┐
          │                   │
      static prefix       dynamic context
          │                   │
          └─────────┬─────────┘
                    ▼
                   LLM
                    │
              Provider cache
```

### 8.1.1. Para o MBCG

Eu aproveitaria **diretamente esses mecanismos** e faria o MBCG atuar principalmente na camada acima:

```text
MBCG Knowledge / KG / OKF
          ↓
    Context preparation
          ↓
       OpenCode
          ↓
   session + context
          ↓
    provider / LLM
```

A vantagem é grande: **não precisamos implementar nosso próprio mecanismo de sessão, compaction, instruction loading e aproveitamento de prompt cache**.

A ressalva é que **OpenCode não é uma API abstrata de memória/contexto**; é um agente/CLI completo. Portanto, se quisermos usá-lo como _agent runtime_ do MBCG, vale mapear exatamente quais desses mecanismos são acessíveis programaticamente e quais só existem internamente no CLI.


## 8.2. separar o que é API pública do que é mecanismo interno

| Mecanismo                             | Acessível programaticamente? | Como                                                                                                                           |
| ------------------------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Sessions**                          | ✅                            | SDK/API: criar, obter, listar, apagar                                                                                          |
| **Histórico de mensagens**            | ✅                            | `session.messages()`                                                                                                           |
| **Enviar prompt**                     | ✅                            | `session.prompt()`                                                                                                             |
| **Contexto sem gerar resposta**       | ✅                            | `session.prompt(noReply=true)`                                                                                                 |
| **AGENTS.md / instructions**          | ⚠️ Indiretamente             | Arquivos são descobertos pelo OpenCode; não é uma API genérica de `PersistentContext`                                          |
| **Skills / MCP / referências**        | ⚠️                           | Entram no mecanismo interno de construção de contexto                                                                          |
| **Compaction**                        | ✅ Parcialmente               | `session.summarize()`; mecanismo automático é interno                                                                          |
| **Subagents**                         | ✅                            | Sessions filhas / agentes configurados                                                                                         |
| **Prompt caching / KV cache**         | ❌ Controle direto            | Delegado ao provider/runtime                                                                                                   |
| **Construção final do prompt**        | ❌                            | Interna ao OpenCode                                                                                                            |
| **Política de quando/como compactar** | ❌                            | Interna                                                                                                                        |
| **Gerenciamento do KV cache**         | ❌                            | Provider/runtime                                                                                                               |
| **Storage das sessões**               | ⚠️                           | Existe e é persistente, mas o formato/storage interno não é uma abstração pública recomendável para você manipular diretamente |

A API é bastante interessante para o seu caso: o OpenCode pode ser executado como **servidor local** e controlado via SDK/API; a API expõe diretamente operações de sessão, mensagens, prompt, comandos, shell e sumarização. ([OpenCode](https://opencode.ai/docs/pt-br/sdk/?utm_source=chatgpt.com "SDK | OpenCode"))

### 8.2.1. O ponto mais importante

O OpenCode **não possui uma API pública chamada `PersistentContext`**.

O que ele faz é combinar várias fontes:

```text
AGENTS.md
built-in context
skills
MCP
session context
        │
        ▼
Instructions / Context Builder
        │
        ▼
model request
```

Na versão atual, a documentação diz explicitamente que esses valores são armazenados como **durable deltas** e depois renderizados junto com as atualizações cronológicas **a cada model request**. ([OpenCode](https://opencode.ai/v2/docs/instructions?utm_source=chatgpt.com "Instructions | OpenCode"))

E a compactação também é explícita: quando necessário, o OpenCode substitui uma parte antiga da sessão por um checkpoint/resumo e reconstrói as requisições a partir desse checkpoint + mensagens posteriores. ([OpenCode](https://opencode.ai/v2/docs/compaction?utm_source=chatgpt.com "Compaction | OpenCode"))

### 8.2.2. Para o MBCG

Isso sugere uma arquitetura muito simples:

```text
                 MBCG
                   │
        ┌──────────┴──────────┐
        │                     │
   Knowledge Layer       Agent Control
   KG / OKF / XMI              │
        │                       ▼
        └──────────────►    OpenCode
                              │
                    ┌─────────┼─────────┐
                    ▼         ▼         ▼
                 Session   Context   Compaction
                    │         │
                    └────┬────┘
                         ▼
                    Provider/LLM
                         │
                    KV/prompt cache
```

**Minha conclusão:** em vez de implementar `PersistentContext + Session + Compaction + Context Builder` em Python, você pode usar o **OpenCode como runtime do agente** e fazer o MBCG atuar como a camada de conhecimento/orquestração.

Isso reduz bastante o que você precisa implementar. O próximo ponto que eu investigaria é **como o Python pode controlar o OpenCode Server/SDK de forma equivalente ao CLI**, porque aí podemos avaliar se ele serve efetivamente como _agent runtime_ do MBCG.
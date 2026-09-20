**Plan: Migrar OpenCode V1 → V2**

# 1. Resumo do Estado Atual

Seu projeto possui **3 arquivos de configuração V1**, **6 agentes com frontmatter V1**, **13 skills**, **1 plugin V1**, e documentação com comandos V1. Nenhum `tui.json`/`cli.json` encontrado (migração automática).

---

# 2. Fase 1 — Preparação (Sem Alterações de Código)

## 2.1. Backup
- Copiar todo o repositório antes de qualquer mudança
- Manter cópia das 3 configs V1: `opencode.json`, `opencode 260723.json`, `opencode 260521.json`

## 2.2. Instalar V2
- Remover instalação V1 do pacote gerenciado
- Instalar V2 com o instalador curl (substitui o binário V1 automaticamente)
- O V2 auto-migra `tui.json` → `cli.json` se existir

---

# 3. Fase 2 — Migração de Configurações JSON

## 3.1. `opencode.json` (projeto root)

| Campo V1 | V2 equivalente |
|----------|---------------|
| `provider.ollama` (objeto) | `providers.ollama` |
| `provider.ollama.npm: "@ai-sdk/openai-compatible"` | `providers.ollama.package: "aisdk:@ai-sdk/openai-compatible"` |
| `provider.ollama.options: { baseURL: ... }` | `providers.ollama.settings: { baseURL: ... }` |
| `provider.ollama.models.qwen2.5-coder:7b` (aninhado) | `providers.ollama.models` (V2 model schema com `modelID`, etc.) |
| `mcp.code-review-graph.enabled: false` | `mcp.servers.code-review-graph.disabled: false` |
| `mcp.supabase.enabled: false` | `mcp.servers.supabase.disabled: true` |
| `plugin: ["@ramtinj95/opencode-tokenscope@latest"]` | `plugins: ["@ramtinj95/opencode-tokenscope@latest"]` (ver Fase 4) |

## 3.2. `opencode 260723.json`

Além das mesmas transformações de 2.1:

| Campo V1 | V2 equivalente |
|----------|---------------|
| `permission: { edit: "ask", bash: "ask", ... }` | `permissions: [{ action: "shell", resource: "edit", effect: "ask" }, ...]` |
| `permission.bash` → `permission.shell` | `action: "shell"` |
| `permission.task` → `permission.subagent` | `action: "subagent"` |
| `permission.write` / `permission.patch` → `permission.edit` | `action: "edit"` |
| `agent.session-planner` | `agents.session-planner` |
| `agent.session-planner.disable: true` | `agents.session-planner.disabled: true` |
| `agent.session-planner.mode: "subagent"` | Agente entra em `agents` como primary agent (ver nota abaixo) |
| `agent.session-planner.prompt: "{file:...}"` | `agents.session-planner.system: "{file:...}"` |
| `agent.session-planner.tools: {}` | Não tem equivalente direto, remover ou validar |

> **Nota sobre `mode`:** O mapa `agent` (singular) V1 se torna `agents`. O V2 diz que "entries from the old `mode` map become primary agents". Como `session-planner` tem `mode: subagent`, precisa-se decidir: manter como agente normal em `agents` (o `mode` não é campo V2) ou migrar para `.opencode/agents/` com frontmatter `mode: primary`.

## 3.3. `opencode 260521.json`

Mesmas transformações de 2.1 (permission, provider, mcp).

## 3.4. Field mapping completo para permissões (V1 → V2)

```
edit → action: "edit"
bash → action: "shell"
read → action: "read"
webfetch → action: "webfetch"
question → action: "question"
glob → action: "glob"
grep → action: "grep"
task → action: "subagent"
todowrite → action: "todowrite"
websearch → action: "websearch"
codesearch → action: "codesearch"
skill → action: "skill"
```

---

# 4. Fase 3 — Migração de Agentes (Frontmatter V1 → V2)

Arquivos em `.opencode/prompts/agents/`:

## 4.1. Todos os 6 agentes têm V1 frontmatter

Cada arquivo `.md` contém:
- `mode: subagent` (5 dos 6 — verificar `doc-researcher`)
- `permission: { read/Write/edit/bash/... }` (todos)

## 4.2. Transformações por arquivo

Para cada agente em `.opencode/prompts/agents/*.md`:
- Renomear `permission:` → `permissions:` (array V1 → V2 array)
- Converter cada entry de `{tool}: {effect}` para `{action: "tool", effect}` — mas note que o V2 frontmatter para agentes ainda não é detalhado na docs. A migração de agent files em frontmatter é "optional" pois o V2 traduz automaticamente.
- `mode: subagent` → remover (o V2 não usa `mode` em frontmatter de agents em `agents/`; se o agente deve ser primary, adicionar `mode: primary`)
- Renomear `prompt` → `system` (se presente no frontmatter)
- Renomear `disable` → `disabled` (se presente)
- Juntar `model` + `variant` como `model#variant` (se presente)

> **Recomendação:** Como o V2 traduz frontmatter legado automaticamente, estas mudanças são opcionais. Priorizar a migração dos arquivos JSON primeiro.

## 4.3. Consideração sobre diretório

O V2 prefere `.opencode/agents/<name>.md` mas ainda descobre `.opencode/prompts/agents/`. **Nenhuma mudança de diretório obrigatória.**

---

# 5. Fase 4 — Migração de Plugin

## 5.1. Plugin V1: `@ramtinj95/opencode-tokenscope@latest`

O V1 plugin **não roda** no V2. Precisa:
1. Verificar se existe versão V2 do `@ramtinj95/opencode-tokenscope`
2. Se não existir, portar o plugin seguindo a [plugin migration guide](https://opencode.ai/v2/docs/build/plugins/migrate-v1/)
3. Atualizar `opencode.json`/`opencode 260723.json`: `"plugin": [...]` → `"plugins": [...]`
4. Atualizar `.opencode/package.json` de `@opencode-ai/plugin: 1.1.53` (V1) para a versão V2 correspondente
5. Mover arquivos de `.opencode/prompts/plugins/` (se existir) para `.opencode/plugins/`

## 5.2. Dependências npm/bun
- Atualizar `bun.lock` após instalar versão V2 do plugin
- `@opencode-ai/plugin` 1.x é V1 API; V2 usa API diferente

---

# 6. Fase 5 — Migração de Skills

## 6.1. Localização atual vs preferida

| Atual | Preferido V2 |
|-------|-------------|
| `.opencode/prompts/skills/<name>/SKILL.md` | `.opencode/skills/<name>/SKILL.md` |

## 6.2. Ações
- Mover os 13 diretórios de `.opencode/prompts/skills/` para `.opencode/skills/`
- Manter conteúdo intacto (o V2 não requer rewrite de SKILL.md)
- Verificar que `name` no frontmatter corresponde ao nome do diretório
- O V2 descobre ambas localizações, mas a preferida é `.opencode/skills/`

---

# 7. Fase 6 — Documentação e Comandos V1

## 7.1. `docs/sessions/utils.md`
Contém comandos V1:
- `OPENCODE_SERVER_PASSWORD=123 opencode web --port 8888 --hostname 0.0.0.0` → verificar flags V2
- `OPENCODE_SERVER_PASSWORD=123 opencode attach http://localhost:8888` → verificar se `attach` existe no V2
- `opencode export ses_...` → verificar sintaxe V2

## 7.2. Outros arquivos de docs
- `docs/kb/...` — referências a `opencode.json` config, geralmente informativas, não precisam de mudança funcional

---

# 8. Ordem de Execução Recomendada

1. **Backup completo** do repositório
2. Remover instalação V1 do pacote gerenciado
3. **Instalar V2** (substitui binário V1)
4. listar demais pendencias para finalizar atualização
5. **Migrar configs JSON** (Fase 2) — começar com `opencode.json`
6. **Migrar plugins** (Fase 4) — instalar versão V2 do tokenScope
7. **Migrar skills** (Fase 5) — mover diretórios
8. **Migrar agent frontmatter** (Fase 3) — opcional, V2 traduz automaticamente
9. **Atualizar docs** (Fase 6)
10. **Testar**: modelos, credenciais, agentes, permissões, MCP servers, plugins
11. **Migrar configs nativos V2** (opcional, último passo) — usar comando "Migrate my OpenCode configuration"

---

# 9. Riscos e Considerações

| Risco                                                                  | Mitigação                                             |
| ---------------------------------------------------------------------- | ----------------------------------------------------- |
| Plugin V1 não funciona em V2                                           | Manter V1 setup em paralelo até plugin V2 funcionar   |
| `permission` V1 pode ter comportamento diferente em V2 (ordered array) | Testar permissões cuidadosamente após migração        |
| `mode: subagent` em agents — comportamento V2 pode diferir             | Validar se agents continuam funcionando como esperado |
| MCP `enabled` invertido para `disabled` — risco de inverter sentido    | Revisar cada MCP server após migração                 |
| `@ai-sdk/openai-compatible` pode ter API diferente no V2               | Verificar compatibilidade do provider                 |
| 3 configs JSON podem conflitar (V1 + V2 mixed)                         | O V2 suporta mixed fields, mas validar warnings       |

---

# 10. Perguntas para o Usuário

1. **Plugin tokenscope**: Existe uma versão V2 do `@ramtinj95/opencode-tokenscope`? Ou precisa portar o plugin manualmente?
2. **Agentes `mode: subagent`**: Os agents que usam `mode: subagent` no frontmatter devem permanecer como subagents, ou devem ser convertidos para primary agents?
3. **3 arquivos JSON**: Os 3 arquivos (`opencode.json`, `opencode 260723.json`, `opencode 260521.json`) são usados para cenários diferentes? Devem ser fundidos em um, ou mantidos separados?
4. **MCP code-review-graph**: O `code-review-graph` MCP está atualmente desabilitado (`enabled: false`). A intenção é mantê-lo desabilitado também no V2?
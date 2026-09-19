**Guia de Execução por Rodada — Instruções Detalhadas**

# Propósito

Este documento contém instruções passo a passo para executar cada etapa do teste, salvar arquivos e decidir quando criar nova versão. Complementa o plano de validação (`260913-analise_termboard_model_validation_plan-04.md`).

---

# 1. Preparação da Rodada

## 1.1. Abrir o Ambiente

1. Abra o workspace no editor de código
2. Navegue até `docs/sessions/260918-repository_model_dev/`
3. Localize a pasta da rodada atual (ex: `rodada-01/`)
4. Identifique a fase atual:
   - Se existe `dev-rN-model-v01.owl` sem `corr-rN-*` → fase DESENVOLVE
   - Se existe `dev-rN-model-v01.*` e CSVs de VALIDA parcialmente preenchidos → fase VALIDA
   - Se existe `corr-rN-model-v01.*` → fase CORRIGE concluída, pronto para próxima rodada

## 1.2. Abrir o Modelo no Termboard

1. Abra o Termboard no navegador
2. Carregue o modelo OWL da rodada atual:
   - Importe `rodada-N/dev-rN-model-v01.owl` ou `corr-rN-model-v01.owl`
3. Verifique se o modelo carrega sem erros
4. Confirme a contagem de conceitos (deve ser 21 na v04)
5. Confirme os 5 ConceptSchemes (facets: Content, Structure, Process, Tool, Scope)

---

# 2. Execução da Fase DESENVOLVE

## 2.1. Editar o Modelo

1. No Termboard, adicione/modifique conceitos conforme necessário
2. Para cada conceito, verifique:
   - Tem rótulo preferencial (prefLabel)?
   - Tem definição?
   - Relacionou com conceito pai (broader)?
   - Relacionou com conceitos filhos (narrower)?
   - Relacionou com conceitos relacionados (related)?
3. Salve no Termboard

## 2.2. Exportar Após Edição

Após salvar, exporte o modelo atualizado para a pasta da rodada:

```
Caminho: rodada-N/dev-rN-model-vM.ext
```

**Passos:**
1. Exporte OWL: `dev-rN-model-vM.owl`
2. Exporte JSON: `dev-rN-model-vM.json`
3. Atualize contexto: `dev-rN-model-vM-context.md`

**Regra de versão:**
- Se foi uma edição pequena (consistência): mantenha vM, sobrescreva
- Se foi uma edição significativa (novos conceitos/relações): incremente para v(M+1)

**Exemplo:**
- Editou apenas definições de 3 conceitos → `dev-r01-model-v01.owl` (sobrescrever)
- Adicionou 5 novos conceitos e 3 novas relações → `dev-r01-model-v02.owl` (novo número)

## 2.3. Quando Avançar para VALIDA

Avanse para VALIDA quando:
- ✅ Todas as edições planejadas foram aplicadas
- ✅ O modelo carrega no Termboard sem erros
- ✅ O JSON reflete o estado atual do OWL
- ✅ O contexto foi atualizado

---

# 3. Execução da Fase VALIDA

## 3.1. Executar OrionBelt

### 3.1.1. Carregar Modelo

1. Abra OrionBelt
2. Vá em Source → Load
3. Selecione `rodada-N/dev-rN-model-v01.owl`
4. Aguarde carregamento
5. Confirme que o modelo está carregado (verifique contagem de conceitos)

### 3.1.2. Executar Validações SKOS

1. Selecione validações SKOS
2. Execute
3. Para cada resultado:
   - Se OK (✓): registre no CSV de resultados
   - Se Erro (✗): registre no CSV com detalhes
   - Se Warning (!): registre no CSV como warning

### 3.1.3. Executar Validações OWL-RL

1. Selecione validações OWL-RL
2. Execute
3. Registre resultados no CSV

### 3.1.4. Registrar no CSV de Resultados

Arquivo: `rodada-N/val-rN-resultados-vM.csv`

**Formato:**
| Rodada | Versão Modelo | Ferramenta | Verificação | Resultado | Detalhes |
|--------|--------------|------------|-------------|-----------|----------|
| R1 | v01 | OrionBelt | Missing prefLabels | ✓ | OK |
| R1 | v01 | OrionBelt | Orphan concepts | ✗ | 3 conceitos sem scheme |

## 3.2. Executar Termboard Semantic Checks

### 3.2.1. Verificações

1. No Termboard, acesse a barra lateral direita → Semantic Checks
2. Execute cada uma das 14 verificações:
   - Missing prefLabels
   - Missing definitions
   - Missing broader
   - Missing narrower
   - Missing related
   - No parent in description
   - No relations
   - Duplicate labels
   - Ambiguous labels
   - Unused concepts
   - Missing concept schemes
   - Circular hierarchies
   - Missing top concept
   - Orphan concepts

### 3.2.2. Registrar no Checklist

Arquivo: `rodada-N/val-rN-checklist-vM.csv`

**Para cada item:**
1. Execute a verificação no Termboard
2. Registre o resultado (✓ / ✗ / !)
3. Adicione observações se necessário
4. Identifique a fase (DESENVOLVE / VALIDA / CORRIGE)

## 3.3. Documentar Procedimentos

Arquivo: `rodada-N/val-rN-procedures-vM.csv`

Para cada verificação (31 itens), registre:
1. Passo a passo executado
2. Ferramenta utilizada
3. Tempo gasto (opcional)
4. Dificuldade (fácil / médio / difícil)
5. Resultado esperado vs. obtido

## 3.4. Gerar Análise

Arquivo: `rodada-N/val-rN-analysis-vM.md`

Estrutura sugerida:
```markdown
# Análise da Rodada N — Fase VALIDA

## Resumo Geral
- Total de verificações: 31
- OK: X
- Erros: Y
- Warnings: Z

## Problemas Encontrados
### [Nome do problema]
- Descrição
- Impacto
- Sugestão de correção

## Pontos Positivos
- [Listar aspectos que funcionaram bem]

## Recomendações
- [Listar recomendações para próxima rodada]
```

Arquivo visual: `rodada-N/val-rN-analysis-vM.jpg`
- Mapeamento visual das relações do modelo
- Gere via Termboard ou ferramenta de diagramação

## 3.5. Quando Avançar para CORRIGE ou Nova Rodada

Avanze para CORRIGE quando:
- ❌ Existem erros (✗) nos CSVs

Avanze para nova rodada quando:
- ✅ Todas verificações ✓ ou ! (sem erros pendentes)
- ✅ Modelo carrega sem inconsistências
- ✅ CSVs preenchidos integralmente
- ✅ Análise documentada

---

# 4. Execução da Fase CORRIGE

## 4.1. Analisar Resultados

1. Abra `rodada-N/val-rN-resultados-vM.csv`
2. Identifique todos os erros (✗) e warnings (!)
3. Crie uma lista de correções necessárias

## 4.2. Aplicar Correções no Termboard

Para cada erro, aplique a correção correspondente:

### Erros comuns e correções:

| Erro | Correção no Termboard |
|------|----------------------|
| Missing prefLabels | Adicionar rótulo preferencial em todos os idiomas |
| Orphan concepts | Associar conceito a um ConceptScheme |
| Duplicate labels | Renomear ou desambiguar rótulos |
| Cycles in broader | Reorganizar hierarquia para eliminar ciclos |
| Missing ConceptScheme | Adicionar conceito ao scheme apropriado |
| Missing domains/ranges | Definir domínio e alcance de propriedades |
| Inconsistencies | Corrigir contradições lógicas |
| Circular hierarchies | Reordenar relações broader |
| Missing broader | Adicionar relação com conceito pai |
| No relations | Adicionar relações relevantes |

## 4.3. Exportar Modelo Corrigido

Após aplicar TODAS as correções:

```
Caminho: rodada-N/corr-rN-model-v01.ext
```

**Passos:**
1. Exporte OWL corrigido: `corr-rN-model-v01.owl`
2. Exporte JSON corrigido: `corr-rN-model-v01.json`
3. Atualize contexto corrigido: `corr-rN-model-v01-context.md`

**Regra de versão:**
- Sempre v01 para o modelo corrigido (dentro da mesma rodada)
- Se houver re-correções na mesma rodada: `corr-rN-model-v02.owl`

## 4.4. Re-Validar (Opcional)

Para confirmar correções:
1. Execute OrionBelt sobre `corr-rN-model-v01.owl`
2. Execute Termboard Semantic Checks
3. Se OK: avance para próxima rodada
4. Se ainda com erros:
   - Aplique novas correções → `corr-rN-model-v02.*`
   - Re-execute validações → `val-rN-checklist-v02.csv`
   - Repita até OK

---

# 5. Quando Criar Nova Versão

## 5.1. Regras Gerais

Crie nova versão (incremente o número) quando:

| Situação | Exemplo |
|----------|---------|
| Edição significativa no modelo | Novos conceitos, novas relações |
| Re-execução de validações | Após correções, re-executar OrionBelt |
| Modelo corrigido exportado | corr-rN-model-v01 → corr-rN-model-v02 |
| Plano atualizado com novas verificações | val-rN-plan-v01 → val-rN-plan-v02 |

Não crie nova versão quando:
- Apenas explorando sem alterar modelo
- Salvamentos temporários
- Re-executando a mesma verificação sem mudanças no modelo
- Edições cosméticas (typos em anotações não estruturais)

## 5.2. Resumo Visual

```
DESENVOLVE: v01 → editar → v01 (pequeno) ou v02 (significativo) → ...
     ↓
VALIDA:    v01 → validar → v01 (continuar) ou v02 (re-validar) → ...
     ↓
CORRIGE:   v01 → corrigir → v01 (normal) ou v02 (re-corrigir) → ...
     ↓
PRÓXIMA RODADA: v01 (reiniciado)
```

---

# 6. Como Salvar Arquivos

## 6.1. Modelo OWL

1. No Termboard, após editar: File → Export → OWL
2. Salve na pasta da rodada: `rodada-N/dev-rN-model-vM.owl`
3. Confirme que o arquivo não está corrompido (abra para verificar)

## 6.2. Modelo JSON

1. No Termboard, exporte em formato JSON
2. Salve como `rodada-N/dev-rN-model-vM.json`
3. Confirme que reflete o estado atual do OWL

## 6.3. Contexto

1. Atualize o documento de contexto manualmente
2. Salve como `rodada-N/dev-rN-model-vM-context.md`
3. Inclua: descrição do modelo, decisões tomadas, alterações recentes

## 6.4. CSVs

1. Abra o CSV correspondente (checklist, resultados, procedures)
2. Preencha/atualize os campos
3. Salve na mesma pasta
4. Confirme que o formato CSV está correto (delimitadores, codificação)

## 6.5. Análise

1. Escreva em markdown
2. Salve como `rodada-N/val-rN-analysis-vM.md`
3. Salve imagem como `rodada-N/val-rN-analysis-vM.jpg`

## 6.6. Plano

1. Atualize o documento de plano se necessário
2. Salve como `rodada-N/val-rN-plan-vM.md`

---

# 7. Fluxo Completo — Resumo Visual

```
┌─────────────────────────────────────────────────────────────────┐
│                         RODADA N                                │
│                                                                 │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐                  │
│  │DESENVOLVE│───→│ VALIDA   │───→│ CORRIGE  │                  │
│  │          │    │          │    │          │                  │
│  │dev-rN-   │    │val-rN-   │    │corr-rN-  │                  │
│  │model-vM  │    │checklist │    │model-vM  │                  │
│  │          │    │resultados│    │          │                  │
│  │          │    │procedures│    │          │                  │
│  │          │    │analysis  │    │          │                  │
│  │          │    │plan      │    │          │                  │
│  └──────────┘    └──────────┘    └──────────┘                  │
│       ↓               ↓                ↓                       │
│  [editar no]    [orionbelt +     [aplicar       │            │
│   Termboard]    termboard]       correções]     │            │
│                                                   │            │
│                          ┌────────────────────────┘            │
│                          ↓                                     │
│                   [exportar modelo]                            │
│                                                                   │
│               ┌─────────────────────────────────┐               │
│               │ Erros? → Voltar para DESENVOLVE │               │
│               │ OK?   → Próxima Rodada (N+1)    │               │
│               └─────────────────────────────────┘               │
└─────────────────────────────────────────────────────────────────┘
```

---

# 8. Verificação Rápida — Checklist de Conformidade

Antes de avançar de fase ou rodada, verifique:

- [ ] Modelo OWL carrega sem erros
- [ ] JSON reflete o OWL
- [ ] Todos os arquivos seguem o template `[fase]-r[N]-[entrega]-v[M].ext`
- [ ] Versão é v01 (ou a correta se houver iterações)
- [ ] CSVs preenchidos (se fase VALIDA ou CORRIGE)
- [ ] Análise documentada (se fase VALIDA)
- [ ] Nenhuma mensagem de erro no terminal (se OrionBelt)
- [ ] Contexto atualizado

---

# 9. Solução de Problemas

## Modelo não carrega no OrionBelt
- Verifique se o OWL é válido (abra no Protégé Desktop → HermiT)
- Verifique namespaces
- Verifique caracteres especiais

## Termboard Semantic Checks falha
- Limpe cache do navegador
- Recarregue a página
- Verifique se o modelo está salvo no formato correto

## CSVs com formato incorreto
- Confirme delimitador (vírgula)
- Confirme codificação (UTF-8)
- Confirme que não há caracteres especiais sem escape

## Versão confusa
- Consulte o plano: `260913-analise_termboard_model_validation_plan-04.md`
- Verifique a seção "Convenção de Nomenclatura"
- Verifique a seção "Etapas de Implantação da Estrutura"

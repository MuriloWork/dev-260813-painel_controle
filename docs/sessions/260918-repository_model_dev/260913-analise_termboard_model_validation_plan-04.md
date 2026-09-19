**Plano de Validação do Modelo Semântico (OWL/SKOS) — v04**

# 1. Contexto

- **Modelo atual (rodada 01):**
  - OWL: `rodada-01/dev-r01-model-v01.owl`
  - JSON: `rodada-01/dev-r01-model-v01.json`
  - Contexto: `rodada-01/dev-r01-model-v01-context.md`
  - 21 conceitos, 5 ConceptSchemes (facets), padrões SKOS/RDFS/OWL
- **Ferramentas:** Termboard (GUI) + OrionBelt (CLI/GUI)
- **Objetivo:** desenvolver, validar e corrigir o modelo via ciclo iterativo DESENVOLVE → VALIDA → CORRIGE

## 1.1. Referências

- W3C SKOS Reference: https://www.w3.org/TR/skos-reference/
- OrionBelt: https://github.com/ralforion/orionbelt-ontology-builder
- Termboard: https://termboard.com
- Termboard Semantic Checks: https://termboard.com/manual/page/right-sidebar/semantic-checks.html

## 1.2. Notas

- Fluxo: USER edita no Termboard, AGENT valida com OrionBelt
- Estrutura: uma pasta por rodada, sem subpastas internas
- Name template: `[fase]-r[rodada]-[entrega]-v[versão].[ext]`
- Versões reiniciam a cada rodada
- Protégé Desktop é opcional (instalação Windows, apenas para validação avançada via HermiT)

---

# 2. Estrutura de Organização

## 2.1. Layout

```
260918-repository_model_dev/
├── 260913-analise_termboard_model_validation_plan-04.md
├── plan-estrutura.md
├── rodada-01/
│   ├── dev-r01-model-v01.owl
│   ├── dev-r01-model-v01.json
│   ├── dev-r01-model-v01-context.md
│   ├── val-r01-plan-v01.md
│   ├── val-r01-checklist-v01.csv
│   ├── val-r01-resultados-v01.csv
│   ├── val-r01-procedures-v01.csv
│   ├── val-r01-analysis-v01.md
│   ├── val-r01-analysis-v01.jpg
│   ├── corr-r01-model-v01.owl
│   ├── corr-r01-model-v01.json
│   └── corr-r01-model-v01-context.md
├── rodada-02/
├── rodada-03/
└── ...
```

## 2.2. Convenção de Nomenclatura

**Template:** `[fase]-r[rodada]-[entrega]-v[versão].[ext]`

| Campo | Valores |
|-------|---------|
| fase | `dev` (DESENVOLVE), `val` (VALIDA), `corr` (CORRIGE) |
| rodada | `01`, `02`, `03` (zero-padded) |
| entrega | `model`, `plan`, `checklist`, `resultados`, `procedures`, `analysis` |
| versão | `01`, `02`, `03` (zero-padded, reseta por rodada) |
| extensão | `.owl`, `.json`, `.md`, `.csv`, `.jpg` |

## 2.3. Conjunto de Arquivos por Rodada

### Fase DESENVOLVE

| Arquivo | Extensão |
|---------|----------|
| `dev-rN-model-vM` | .owl |
| `dev-rN-model-vM` | .json |
| `dev-rN-model-vM-context` | .md |

### Fase VALIDA

| Arquivo | Extensão |
|---------|----------|
| `val-rN-plan-vM` | .md |
| `val-rN-checklist-vM` | .csv |
| `val-rN-resultados-vM` | .csv |
| `val-rN-procedures-vM` | .csv |
| `val-rN-analysis-vM` | .md |
| `val-rN-analysis-vM` | .jpg |

### Fase CORRIGE

| Arquivo | Extensão |
|---------|----------|
| `corr-rN-model-vM` | .owl |
| `corr-rN-model-vM` | .json |
| `corr-rN-model-vM-context` | .md |

---

# 3. Ferramentas e Fluxo

## 3.1. Ferramentas

- **Termboard** (GUI): edição do modelo, 14 verificações semânticas integradas
- **OrionBelt** (CLI/GUI): validação técnica SKOS e OWL-RL
- **Protégé Desktop** (opcional): reasoners (HermiT, Pellet), plugins (OWL Lint, OntoCheck, OntoDebug, SKOS Editor)

## 3.2. Fluxo de Agente

1. USER edita modelo no Termboard → gera `dev-rN-model-vM`
2. AGENT executa OrionBelt + Termboard Semantic Checks → preenche CSVs `val-rN-*`
3. USER analisa resultados e decide: continuar rodada (CORRIGE) ou nova rodada
4. Se CORRIGE: USER aplica correções → gera `corr-rN-model-vM`
5. Se nova rodada: inicia `rodada-N+1` com `dev-r(N+1)-model-v01`

---

# 4. Ciclo de Desenvolvimento

## 4.1. Fases

| Fase | Ação | Gera | Ferramenta Principal |
|------|------|------|----------------------|
| DESENVOLVE | Editar/expandir modelo no Termboard | `dev-rN-model-vM.*` | Termboard |
| VALIDA | Executar verificações e preencher CSVs | `val-rN-*` | OrionBelt + Termboard |
| CORRIGE | Aplicar correções baseadas nos resultados | `corr-rN-model-vM.*` | Termboard |

## 4.2. Transição entre Rodadas

1. Após CORRIGE (rodada N): modelo corrigido = `corr-rN-model-v01`
2. Rodada N+1: copiar modelo corrigido como base → `dev-r(N+1)-model-v01`
3. Versões reiniciam: v01 em todas as entregas de rodada N+1
4. CSVs de rodada N+1 são gerados do zero

---

# 5. Detalhamento das Verificações

## 5.1. Termboard — Verificações Semânticas (14 itens)

| # | Verificação | Fase |
|---|------------|------|
| 1 | Missing prefLabels | DESENVOLVE |
| 2 | Missing definitions | DESENVOLVE |
| 3 | Missing broader | DESENVOLVE |
| 4 | Missing narrower | DESENVOLVE |
| 5 | Missing related | DESENVOLVE |
| 6 | No parent in description | DESENVOLVE |
| 7 | No relations | DESENVOLVE |
| 8 | Duplicate labels | DESENVOLVE |
| 9 | Ambiguous labels | DESENVOLVE |
| 10 | Unused concepts | DESENVOLVE |
| 11 | Missing concept schemes | DESENVOLVE |
| 12 | Circular hierarchies | DESENVOLVE |
| 13 | Missing top concept | DESENVOLVE |
| 14 | Orphan concepts | DESENVOLVE |

## 5.2. OrionBelt — Validação Técnica (18 itens)

| # | Verificação | Fase |
|---|------------|------|
| 1 | Missing prefLabels | VALIDA |
| 2 | Orphan concepts | VALIDA |
| 3 | Duplicate labels | VALIDA |
| 4 | Cycles in broader | VALIDA |
| 5 | Missing ConceptScheme | VALIDA |
| 6 | Missing domains/ranges | VALIDA |
| 7 | Inconsistencies | VALIDA |
| ... | (demais verificações OWL-RL) | VALIDA |

## 5.3. Checklist Unificado (31 itens)

Combina Termboard (14) + OrionBelt (18), com 1 overlap (Missing prefLabels):

- **Categorias:** Conteúdo, Estrutura, Processo, Ferramenta, Escopo
- **Colunas:** Item, Descrição, Categoria, Ferramenta, Fase, Observações
- **Preenchimento:** Durante VALIDA e CORRIGE

---

# 6. Convenção de Nomenclatura — Detalhamento

## 6.1. Template

```
[fase]-r[rodada]-[entrega]-v[versão].[ext]
```

## 6.2. Exemplos Completos — Rodada 01

**DESENVOLVE:**
- `dev-r01-model-v01.owl` — modelo OWL
- `dev-r01-model-v01.json` — modelo JSON
- `dev-r01-model-v01-context.md` — contexto

**VALIDA:**
- `val-r01-plan-v01.md` — plano de validação
- `val-r01-checklist-v01.csv` — checklist (31 itens)
- `val-r01-resultados-v01.csv` — resultados
- `val-r01-procedures-v01.csv` — procedimentos
- `val-r01-analysis-v01.md` — análise
- `val-r01-analysis-v01.jpg` — mapeamento visual

**CORRIGE:**
- `corr-r01-model-v01.owl` — modelo corrigido
- `corr-r01-model-v01.json` — modelo corrigido (JSON)
- `corr-r01-model-v01-context.md` — contexto corrigido

**Rodada 02 (baseado na correção):**
- `dev-r02-model-v01.owl` — modelo v01, mas baseado em corr-r01-model-v01

---

# 7. Etapas de Implantação da Estrutura

## 7.1. Criação de Rodada

### Rodada 01 (inicial)

1. Crie `rodada-01/`
2. Copie modelo atual para `dev-r01-model-v01.owl`, `.json`, `-context.md`
3. Copie plano para `val-r01-plan-v01.md`
4. Copie CSVs para `val-r01-checklist-v01.csv`, `val-r01-resultados-v01.csv`, `val-r01-procedures-v01.csv`
5. Copie análise para `val-r01-analysis-v01.md`, `.jpg`

### Rodada N (subsequentes)

1. Crie `rodada-N/`
2. Copie modelo corrigido da rodada anterior: `corr-r(N-1)-model-v01.*` → `dev-rN-model-v01.*`
3. Adapte plano → `val-rN-plan-v01.md`
4. Reinicie CSVs (limpando resultados) → `val-rN-*.csv`
5. Gere nova análise → `val-rN-analysis-v01.md`, `.jpg`

## 7.2. Execução da Fase DESENVOLVE

1. Abra modelo OWL no Termboard (`dev-rN-model-v01.owl`)
2. Edite/adicione conceitos conforme necessário
3. Exporte: sobrescreva `dev-rN-model-v01.*`
4. Se salvamento parcial, incremente versão: `dev-rN-model-v02.*`
5. Quando satisfeito, avance para VALIDA

## 7.3. Execução da Fase VALIDA

1. Execute OrionBelt sobre `dev-rN-model-v01.owl`:
   - Source → Load
   - Executar validações SKOS + OWL-RL
   - Registrar em `val-rN-resultados-v01.csv`
2. Execute Termboard Semantic Checks:
   - Verifique 14 verificações
   - Preencha `val-rN-checklist-v01.csv`
3. Documente procedimentos em `val-rN-procedures-v01.csv`
4. Gere análise em `val-rN-analysis-v01.md`
5. Gere mapeamento visual em `val-rN-analysis-v01.jpg`
6. Se erros encontrados → CORRIGE
7. Se sem erros → nova rodada (pule CORRIGE)

## 7.4. Execução da Fase CORRIGE

1. Analise `val-rN-resultados-v01.csv` (procure ✗ e !)
2. Aplique correções no Termboard:
   - Rótulos faltantes
   - Relações (broader, narrower, related)
   - Ciclos em hierarchies
   - ConceptSchemes faltantes
   - Inconsistências lógicas
3. Exporte modelo corrigido: `corr-rN-model-v01.*`
4. Opcional: re-execute VALIDA sobre modelo corrigido
   - Se re-executar: `val-rN-checklist-v02.csv`, etc.
5. Avance para próxima rodada

## 7.5. Quando Criar Nova Versão

Crie nova versão (v01 → v02) quando:
- **DESENVOLVE:** Edição significativa (novos conceitos/relações)
- **VALIDA:** Re-executação após correções intermediárias
- **CORRIGE:** Aplicação de correções pendentes

Não crie nova versão quando:
- Apenas explorando sem alterar modelo
- Salvamentos temporários (use rascunho externo)
- Re-executando mesma verificação sem mudanças

## 7.6. Fim de Rodada

Critérios:
1. Todas verificações do checklist: ✓ ou ! (sem erros pendentes)
2. Modelo OWL carrega sem inconsistências
3. CSVs preenchidos
4. Análise documentada

Se NÃO atingidos → CORRIGE → re-VALIDA → repita na mesma rodada (incremente versão)
Se muitas iterações → dividir em duas rodadas

## 7.7. Migração entre Rodadas

1. Confirme critérios de fim de rodada (§7.6)
2. Crie `rodada-N+1/`
3. Base do modelo: `corr-rN-model-v01.*` (ou `dev-rN-model-v01.*` se sem CORRIGE)
4. CSVs começam zerados (v01)
5. Arquivos de rodadas anteriores mantidos (histórico completo)

---

# 8. Versionamento

| Rodada | DESENVOLVE | VALIDA | CORRIGE |
|--------|-----------|--------|---------|
| R1 | dev-r1-model-v01 | val-r1-* | corr-r1-model-v01 |
| R2 | dev-r2-model-v01 | val-r2-* | corr-r2-model-v01 |
| R3 | dev-r3-model-v01 | val-r3-* | — |

---

# 9. Referências

- W3C SKOS Reference: https://www.w3.org/TR/skos-reference/
- OrionBelt: https://github.com/ralforion/orionbelt-ontology-builder
- Termboard: https://termboard.com
- Termboard Semantic Checks: https://termboard.com/manual/page/right-sidebar/semantic-checks.html

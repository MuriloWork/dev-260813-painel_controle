**Plano de Validação do Modelo Semântico (OWL/SKOS) — v03**

# 1. Contexto

- **Modelo atual:**
  - OWL: `00-model/260913-termboard_model_repository_v04.owl`
  - JSON: `00-model/260913-termboard_model_repository-04.json`
  - 21 conceitos, 5 ConceptSchemes (facets), padrões SKOS/RDFS/OWL
- **Ferramentas:** Termboard (GUI) + OrionBelt (CLI/GUI)
- **Arquivos de validação:**
  - `260913-analise_termboard_model_validation_plan_checklist-00.csv`
  - `260913-analise_termboard_model_validation_plan_resultados-00.csv`
  - `260913-analise_termboard_model_validation_plan_procedures-00.csv`
- **Objetivo:** desenvolver, validar e corrigir o modelo via ciclo iterativo

## 1.1. Referências

- W3C SKOS Reference: https://www.w3.org/TR/skos-reference/
- OrionBelt: https://github.com/ralforion/orionbelt-ontology-builder
- Termboard: https://termboard.com
- Termboard Semantic Checks: https://termboard.com/manual/page/right-sidebar/semantic-checks.html

## 1.2. Notas

- Fluxo: USER edita no Termboard, AGENT valida com OrionBelt
- CSVs são o registro principal da validação
- Protégé Desktop é opcional (instalação Windows, apenas para validação avançada via HermiT)
- Versões anteriores do plano: `v02` na raiz, `v03` nesta pasta

---

# 2. Estrutura de Subpastas

```
260918-repository_model_dev/
├── 00-model/              Modelos fonte (JSON, OWL, contexto)
│   ├── 260913-termboard_model_repository-04.json
│   ├── 260913-termboard_model_repository_v04.owl
│   └── 260913-termboard_model_repository_v04-context.md
├── 01-validation/         Planos e resultados de validação
│   ├── 260913-analise_termboard_model_validation_plan-03.md   ← este arquivo
│   ├── 260913-analise_termboard_model_validation_plan_checklist-00.csv
│   ├── 260913-analise_termboard_model_validation_plan_resultados-00.csv
│   └── 260913-analise_termboard_model_validation_plan_procedures-00.csv
├── 02-analysis/           Documentação e análise
│   ├── 260913-analise_termboard_model.md
│   └── 260914-termboard_relations_mapping_view.jpg
└── 03-history/            Versões históricas
    ├── 260913-termboard_model_repository_v02.owl
    ├── 260913-termboard_model_repository_v02-context.md
    ├── 260913-termboard_model_repository_v03.owl
    └── 260913-termboard_model_repository_v03-context.md
```

---

# 3. Ciclo de Desenvolvimento

## 3.1. Visão Geral

```
┌─────────────┐      export OWL       ┌──────────────┐
│ DESENVOLVE  │ ─────────────────────►│   VALIDA     │
│ (Termboard) │                       │ (OrionBelt + │
│             │ ◄─────────────────────│  Termboard)  │
└──────┬──────┘   corrigir + re-export│              │
       │                              └──────┬───────┘
       │                                     │
       │          resultado: CSVs preenchidos │
       │                                     │
       ▼                                     ▼
┌─────────────┐                      ┌──────────────┐
│  CORRIGE    │ ────────────────────►│ DESENVOLVE   │
│ (Termboard) │    se necessário     │ (volta ao 2) │
└─────────────┘                      └──────────────┘
```

## 3.2. Fase 1: DESENVOLVE

**Objetivo:** Editar e evoluir o modelo semântico

| Item | Descrição |
|------|-----------|
| **Ferramenta** | Termboard (GUI) |
| **Entrada** | Modelo atual em `00-model/` |
| **Ação** | Editar conceitos, relações, descrições no JSON |
| **Saída** | JSON atualizado + OWL exportado → `00-model/` |
| **Versionamento** | v04 → v04.1, v05, etc. |

Procedimento:
1. Abrir Termboard → Load/Save → Importar JSON de `00-model/`
2. Editar conceitos conforme necessário
3. Ferramentas → Semantic Checks → verificar qualidade
4. Exportar OWL → salvar em `00-model/`
5. Atualizar contexto se houver mudanças estruturais

## 3.3. Fase 2: VALIDA

**Objetivo:** Validar o modelo exportado usando múltiplas camadas

| Item | Descrição |
|------|-----------|
| **Ferramentas** | OrionBelt (CLI) + Termboard (Semantic Checks) |
| **Entrada** | OWL em `00-model/` |
| **Ação** | Executar validações (veja seção 4) |
| **Saída** | CSVs preenchidos em `01-validation/` |

Procedimento:
1. Carregar OWL no OrionBelt (Source → Load)
2. Executar SKOS Validation (aba Validation)
3. Executar OWL-RL Reasoning (aba Validation)
4. Executar 12 Semantic Checks no Termboard
5. Preencher `checklist-00.csv` (colunas Termboard, OrionBelt)
6. Revisar resultados
7. Preencher `resultados-00.csv` (colunas Termboard, OrionBelt, status_final)

## 3.4. Fase 3: CORRIGE

**Objetivo:** Corrigir erros encontrados na validação

| Item | Descrição |
|------|-----------|
| **Ferramenta** | Termboard (GUI) |
| **Entrada** | `resultados-00.csv` com erros (✗ ou !) |
| **Ação** | Corrigir itens com erro no Termboard |
| **Saída** | JSON e OWL atualizados em `00-model/` |
| **Fluxo** | Volta à Fase 2 (VALIDA) |

Procedimento:
1. Abrir `resultados-00.csv` → identificar itens com ✗ ou !
2. Consultar `procedures-00.csv` → encontrar procedimento do item
3. Abrir Termboard → localizar e corrigir termo/relação
4. Re-exportar OWL → `00-model/`
5. Voltar à Fase 2 (VALIDA) → re-validar
6. Se todos ✓ → ir para Fase 4 (FINALIZAR)

## 3.5. Fase 4: FINALIZAR

**Objetivo:** Registrar estado final do modelo validado

Procedimento:
1. Confirmar todos os itens ✓ no `resultados-00.csv`
2. Confirmar todos os itens ✓ no `checklist-00.csv` (cobertura)
3. Documentar versão final no versionamento
4. Modelo pronto para uso

---

# 4. Detalhamento das Validações

Os procedimentos para cada um dos 31 itens de validação estão no CSV:

**`01-validation/260913-analise_termboard_model_validation_plan_procedures-00.csv`**

Estrutura do CSV:
- `num`: número do item (1-31) — referencia o checklist
- `item`: descrição da validação
- `category`: categoria (Sintaxe, SKOS, OWL, Qualidade Conceitos, Metadados, Visualização)
- `tool`: ferramenta principal (termboard, orionbelt, both)
- `procedure`: instruções passo a passo para executar o teste

### 4.1.1. Termboard — Semantic Checks (12 verificações)

| Check | O que verifica | Fase |
|-------|---------------|------|
| Plurals in name | Nomes no plural devem ser singulares | DESENVOLVE |
| Similar Term Names | Termos com nomes parecidos (Levenshtein < 3) | DESENVOLVE |
| Synonym conflicts | Sinônimos duplicados entre termos | DESENVOLVE |
| Poor Description Quality | Descrições fracas (score 0-100) | DESENVOLVE |
| No parent in description | Descrição não menciona termo pai | DESENVOLVE |
| No relations | Termos sem relações (órfãos) | DESENVOLVE |
| Duplicating parent relations | Relações duplicadas com pai | CORRIGE |
| Multi parent | Herança múltipla | CORRIGE |
| Circular hierarchies | Ciclos em relações is-a | CORRIGE |
| Bidirectional Relations | Relações bidirecionais | CORRIGE |
| Potential Properties | Termos que deveriam ser propriedades | CORRIGE |
| Properties Without Attributive Relations | Propriedades órfãs | CORRIGE |

### 4.1.2. OrionBelt — Validação Técnica

| Verificação | O que verifica | Fase |
|-------------|---------------|------|
| Missing prefLabels | Termos sem rótulos preferenciais | VALIDA |
| Orphan concepts | Conceitos sem ConceptScheme | VALIDA |
| Duplicate labels | Rótulos duplicados por idioma | VALIDA |
| Cycles in broader | Ciclos em skos:broader | VALIDA |
| Missing ConceptScheme | Esquemas sem top concepts | VALIDA |
| Missing domains/ranges | Propriedades sem domínio/alcance | VALIDA |
| Inconsistencies | Contradições lógicas (OWL-RL) | VALIDA |

---

# 5. Checklist de Validação

```csvtable
source: 260913-analise_termboard_model_validation_plan_checklist-00.csv
```

- **Estrutura:** 31 itens de validação organizados por categoria
- **Cobertura:** Termboard (14/31) + OrionBelt (18/31) = 29/31 combinados
- Itens que dependem do USER (não automatizáveis):
  - Qualidade das descrições (requer julgamento humano)
  - Descrição menciona termo pai (requer contexto)
  - Metadados (título, versão, autor)

# 6. Procedimentos

```csvtable
source: 260913-analise_termboard_model_validation_plan_procedures-00.csv
```

- **Estrutura:** 31 itens com instruções passo a passo para cada verificação
- **Uso:** Referência durante Fase 2 (VALIDA) e Fase 3 (CORRIGE)

---

# 7. Resultados

```csvtable
source: 260913-analise_termboard_model_validation_plan_resultados-00.csv
```

- **Estrutura:** 31 itens com colunas para resultado de cada ferramenta
- **Preenchimento:** Durante Fase 2 (VALIDA) e Fase 3 (CORRIGE)
- **Legenda:** ✓ = OK, ✗ = Erro, ! = Warning, — = Não aplicável

---

# 8. Versionamento

| Versão | Fase | Data | Mudanças |
|--------|------|------|----------|
| v04 | DESENVOLVE | 2026-09-16 | Facetas, 21 conceitos |
| v04.1 | CORRIGE | -- | Correções pós-validação |
| v05 | DESENVOLVE | -- | Novos conceitos/relações |

---

# 9. Referências

- W3C SKOS Reference: https://www.w3.org/TR/skos-reference/
- OrionBelt: https://github.com/ralforion/orionbelt-ontology-builder
- Termboard: https://termboard.com
- Termboard Semantic Checks: https://termboard.com/manual/page/right-sidebar/semantic-checks.html

# 10. chat para revisar o plano
## 10.1. user
não
e tambem quero avaliar melhor a estrutura proposta
algumas questoes
1. ficou claro, em minha solicitação, que a estrutura deve estar preparada para um desenvolvimento em ciclos/rodadas?
2. não ficou clara a relação entre as etapas do "ciclo de desenvolvimento" e a "estrutura de subpastas"
3. como identificar os arquivos de uma mesma rodada?
4. o name template de versionamento proposto (v04.1, ...) me parece fragil
5. como os resultados registrados no csv identificarão as [rodadas, versoes]?

## 10.2. agent

### 10.2.1. Ficou claro que a estrutura deve suportar ciclos/rodadas?

**Não.** O v03 menciona o ciclo DESENVOLVE→VALIDA→CORRIGE no texto, mas a estrutura de pastas é estática — não acomoda múltiplas rodadas. Cada rodada precisa de um identificador próprio.

### 10.2.2. Relação entre etapas do ciclo e estrutura de subpastas?

**Não está clara.** As subpastas organizam por tipo de arquivo (modelo, validação, análise, histórico), mas não mapeiam para as fases do ciclo. Deveria haver uma forma de saber quais arquivos pertencem a qual fase/rodada.

### 10.2.3. Como identificar arquivos de uma mesma rodada?

**Não há convenção atual.** Modelo é v04, plano é v03, CSVs são -00 — sem identificador de rodada em comum.

### 10.2.4. Versionamento v04.1, v05 é frágil?

**Sim.** Mistura versão do modelo com iteração do ciclo, sem distinguir o quê mudou (modelo vs. plano vs. resultado).

### 10.2.5. Como resultados no CSV identificarão rodadas e versões?

**Não identificam.** Faltam colunas de `Rodada` e `Versão`.

---

### 10.2.6. Proposta revisada

Três opções de estrutura para aprovação:

#### 10.2.6.1. Opção A — Flat com prefixo de rodada

```
260918-repository_model_dev/
├── 00-model/
│   ├── r1-model-v04.owl
│   ├── r1-model-v04.json
│   └── r1-model-v04-context.md
│   ├── r2-model-v04.owl
│   └── ...
├── 01-validation/
│   ├── r1-plan.md
│   ├── r1-checklist.csv
│   ├── r1-resultados.csv       ← coluna "Rodada" + "Versão"
│   ├── r1-procedures.csv
│   ├── r2-plan.md
│   └── ...
├── 02-analysis/
└── 03-history/
```
- ✅ Simples, rastreável, fácil de comparar rodadas
- ❌ Cresce linearmente com número de rodadas

#### 10.2.6.2. Opção B — Rodada como pasta principal

```
260918-repository_model_dev/
├── rodada-01/
│   ├── 00-model/
│   │   ├── model-v04.owl
│   │   ├── model-v04.json
│   │   └── context.md
│   ├── 01-validation/
│   │   ├── plan.md
│   │   ├── checklist.csv       ← colunas: Rodada=R1, Versão=v04
│   │   ├── resultados.csv
│   │   └── procedures.csv
│   └── 02-analysis/
├── rodada-02/
│   ├── 00-model/
│   ├── 01-validation/
│   └── 02-analysis/
└── 03-history/
```
- ✅ Isolamento completo por rodada
- ❌ Duplica pastas tipo a cada rodada

#### 10.2.6.3. Opção C — Híbrida (rodada nos nomes + tipo em subpastas)

```
260918-repository_model_dev/
├── 00-model/
│   └── v04-r1/        ← modelo v04, rodada 1
│       ├── model.owl
│       ├── model.json
│       └── context.md
│   └── v04-r2/        ← modelo v04, rodada 2 (após correções)
│   └── v05-r3/        ← modelo v05, rodada 3 (novos conceitos)
├── 01-validation/
│   └── r1/
│       ├── plan.md
│       ├── checklist.csv
│       ├── resultados.csv
│       └── procedures.csv
│   └── r2/
├── 02-analysis/
└── 03-history/
```
- ✅ Modelos versionados por rodada, validação isolada por rodada, nomes curtos
- ✅ Versionamento `v05-r3` = modelo v05 na rodada 3 (sem .1 frágil)
- ❌ Pastas intermediárias

---

#### 10.2.6.4. Sobre os CSVs

Todas as opções incluem colunas obrigatórias nos CSVs de resultado:

| Rodada | Versão Modelo | Ferramenta | Item | Resultado |
|--------|--------------|------------|------|-----------|
| R1 | v04 | OrionBelt | Missing prefLabels | ✓ |

#### 10.2.6.5. Sobre o ciclo DESENVOLVE→VALIDA→CORRIGE

Cada rodada pode ter até 3 sub-fases internas:
1. **DESENVOLVE** → edita modelo no Termboard → gera `vNN-rM`
2. **VALIDA** → executa OrionBelt + Termboard checks → preenche CSVs
3. **CORRIGE** → aplica correções → gera `vNN+1-rM` ou `vNN-rM+1`

---

**Qual opção prefere?** E há ajustes nas regras de versionamento ou no fluxo que quer discutir antes de prosseguir?

## 10.3. user
que fiasco, com tantas incoerencias
acho que agora entendeu porque não aprovei a exclusão dos arquivos

sugiro algo mais simples, com base na sua opçao B
1. uma pasta para cada rodada, sem subpastas
2. um conjunto de arquivos em cada rodada, todos com name template definidos e identificando [rodada, entrega, versão]
3. em cada subpasta (rodada) as versoes dos arquivos são reiniciadas
4. os name templates dos arquivos devem estar diretamente relacionados ao ciclo "DESENVOLVE→VALIDA→CORRIGE"
5. os csv não precisam de coluna adicional [rodada, versao] pois o name template cobre essa necessidade
6. na pasta raiz devemos ter outro documento com as instruções detalhadas sobre como executar cada etapa do teste, salvar arquivos, decidir quando criar nova versao

crie a v04 do plano, a ultima seção com as etapas de implantação da estrutura [subpastas, arquivos] revisada


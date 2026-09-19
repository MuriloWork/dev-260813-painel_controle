**Plano de Validação do Modelo Semântico (OWL/SKOS) — v02**

# 1. Contexto

- **Modelo atual:**
  - OWL: `260913-termboard_model_repository_v04.owl`
  - JSON: `260913-termboard_model_repository-04.json`
  - 21 conceitos, 5 ConceptSchemes (facets), padrões SKOS/RDFS/OWL
- **Ferramentas:** Termboard (GUI) + OrionBelt (CLI/GUI)
- **Arquivos de validação:**
  - `260913-analise_termboard_model_validation_plan_checklist-00.csv` — empilhamento das tabelas da seção 4
  - `260913-analise_termboard_model_validation_plan_resultados-00.csv` — matriz de resultados
  - `260913-analise_termboard_model_validation_plan_procedures-00.csv` — procedimentos para cada teste
- **Objetivo:** validação completa via fluxo interativo user ↔ agent

## 1.1. Referências

- W3C SKOS Reference: https://www.w3.org/TR/skos-reference/
- OrionBelt: https://github.com/ralforion/orionbelt-ontology-builder
- Termboard: https://termboard.com
- Termboard Semantic Checks: https://termboard.com/manual/page/right-sidebar/semantic-checks.html

## 1.2. Notas

- Fluxo: USER edita no Termboard, AGENT valida com OrionBelt
- Termboard é para edição e qualidade dos conceitos (GUI)
- OrionBelt é para validação técnica (CLI/GUI, Python)
- Protégé Desktop é opcional (instalação Windows, apenas para validação avançada via HermiT)
- CSVs são o registro principal da validação (checklist + resultados + procedimentos)

# 2. Fluxo Interativo de Validação

## 2.1. Diagrama

```
┌─────────┐    termboard      ┌──────────┐    export OWL    ┌───────────┐
│  USER   │ ────────────────► │ TERMBOARD│ ────────────────► │  ORIONBELT│
│ (inicia)│ ◄──────────────── │ (GUI)    │ ◄──────────────── │ (CLI/GUI) │
└────┬────┘   edita JSON      └──────────┘   importa OWL     └─────┬─────┘
     │                                                             │
     │              resultado: checklist.csv preenchido              │
     │                                                             │
     │                   ◄──────────────────────                    │
     │              resultado: resultados.csv preenchido             │
     │                                                             │
     ▼                                                             ▼
     └────────────── CORREÇÕES ◄─────────────────────────────────┘
                               │
                               ▼
                         RE-EXPORTAR
                               │
                               ▼
                    v04.1, v05, etc.
```

## 2.2. Interação User ↔ Agent

| Etapa | Quem | Ferramenta | Ação |
|-------|------|------------|------|
| 1 | USER | Termboard | Importar JSON, editar conceitos |
| 2 | AGENT | OrionBelt | Executar validação SKOS + OWL-RL |
| 3 | AGENT | OrionBelt | Gerar relatório de resultados |
| 4 | USER | Termboard | Revisar relatório, corrigir conceitos |
| 5 | AGENT | OrionBelt | Re-validar (checklist.csv atualizado) |
| 6 | USER | — | Decidir: OK ou iterar |
| 7 | AGENT | OrionBelt | Finalizar resultados (resultados.csv completo) |

## 2.3. Fluxo Detalhado

```
USER → Termboard: importar/editar JSON
    ↓
AGENT → OrionBelt: importar OWL + rodar validação
    ↓
AGENT → OrionBelt: preencher check-list-00.csv
    ↓
USER: revisar resultados no check-list-00.csv
    ↓
┌─────┴─────┐
│  OK?      │
│  NÃO → USER: corrigir no Termboard → re-exportar → voltar ao passo 2
│  SIM → continue ↓
└───────────┘
    ↓
AGENT → OrionBelt: preencher resultados-00.csv
    ↓
FIM
```

# 3. Procedimentos

## 3.1. Visão Geral

Os procedimentos para cada um dos 31 testes do checklist estão detalhados no CSV:

```csvtable
source: 11-systems^dev/260813-painel_controle^docs/sessions/260913-termboad_model/260913-analise_termboard_model_validation_plan_procedures-00.csv
```

Estrutura:
- `num`: número do item (1-31) — referencia o checklist
- `item`: descrição da validação
- `category`: categoria (Sintaxe, SKOS, OWL, Qualidade Conceitos, Metadados, Visualização)
- `tool`: ferramenta principal (termboard, orionbelt, both)
- `procedure`: instruções passo a passo para executar o teste

## 3.2. Termboard — Instruções Gerais

1. Abrir Termboard (browser)
2. Load/Save → Importar `260913-termboard_model_repository-04.json`
3. Editar conceitos conforme necessário
4. Exportar OWL (para importar no OrionBelt)
5. Ferramentas → Semantic Checks → executar verificações

### 3.2.1. Semantic Checks (12 verificações)

| Check | O que verifica |
|-------|---------------|
| Plurals in name | Nomes no plural devem ser singulares |
| Similar Term Names | Termos com nomes parecidos (Levenshtein < 3) |
| Synonym conflicts | Sinônimos duplicados entre termos |
| Poor Description Quality | Descrições fracas (score 0-100) |
| No parent in description | Descrição não menciona termo pai |
| No relations | Termos sem relações (órfãos) |
| Duplicating parent relations | Relações duplicadas com pai |
| Multi parent | Herança múltipla |
| Circular hierarchies | Ciclos em relações is-a |
| Bidirectional Relations | Relações bidirecionais |
| Potential Properties | Termos que deveriam ser propriedades |
| Properties Without Attributive Relations | Propriedades órfãs |

## 3.3. OrionBelt — Instruções Gerais

### 3.3.1. Instalação
```bash
pip install orionbelt-ontology-builder
# ou
uv tool install orionbelt-ontology-builder
```

### 3.3.2. Execução
```bash
orionbelt-ontology-builder
# Abre no browser (http://localhost:8501)
```

### 3.3.3. Validação
1. Carregar arquivo OWL (Source → Load)
2. SKOS Validation (aba Validation) → verificar missing prefLabels, orphans, duplicate labels, cycles
3. OWL-RL Reasoning (aba Validation) → verificar missing domains/ranges, inconsistencies
4. Visualização (aba Visualization) → confirmar estrutura

# 4. Checklist de Validação

```csvtable
source: 11-systems^dev/260813-painel_controle^docs/sessions/260913-termboad_model/260913-analise_termboard_model_validation_plan_checklist-00.csv
```

- observações
	- Estrutura:
		- `num`: número do item (1-31)
		- `item`: descrição da validação
		- `category`: categoria (Sintaxe, SKOS, OWL, Qualidade Conceitos, Metadados, Visualização)
		- `termboard`: cobertura (✅/⚠️/❌)
		- `orionbelt`: cobertura (✅/⚠️/❌)
	- Resumo de cobertura:
		- **Termboard:** 14/31 itens (45%)
		- **OrionBelt:** 18/31 itens (58%)
		- **Combinando ambos:** 29/31 itens (94%)
	- Itens que dependem do USER (não automatizáveis):
		- Qualidade das descrições (requer julgamento humano)
		- Descrição menciona termo pai (requer contexto)
		- Metadados (título, versão, autor)

# 5. Resultados

```csvtable
source: 11-systems^dev^260813-painel_controle^docs^sessions^260913-termboad_model^260913-analise_termboard_model_validation_plan_resultados-00.csv
```

- Estrutura:
	- `num`: número do item (1-31)
	- `item`: descrição da validação
	- `termboard`: ✓/✗/!/— (resultado da validação via termboard)
	- `orionbelt`: ✓/✗/!/— (resultado da validação via orionbelt)
	- `status_final`: ✓/✗/! (status final após validação)

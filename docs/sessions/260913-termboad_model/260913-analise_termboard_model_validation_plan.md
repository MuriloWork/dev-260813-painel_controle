# 1. Plano de Validação do Modelo Semântico (OWL/SKOS)

## 1.1. Contexto

- **Modelo atual:**
  - OWL: `docs/sessions/260913-termboad_model/260913-termboard_model_repository_v04.owl`
  - JSON: `docs/sessions/260913-termboad_model/260913-termboard_model_repository-04.json`
  - 21 conceitos, 5 ConceptSchemes (facets), padrões SKOS/RDFS/OWL
  - Facetas: Content, Structure, Process, Tool, Scope
  - Conceito hub: `repository` (topConceptOf todas as facets)
- **Ferramentas:** Termboard + Protégé Desktop + OrionBelt
- **Objetivo:** validação completa (consistência lógica, conformidade OWL DL, SKOS, visualização)

---

## 1.2. Fluxo de Trabalho

```
Termboard JSON (edição)
    ↓ export
OWL file
    ↓ validação
Termboard (12 checks) + Protégé Desktop (HermiT + plugins) + OrionBelt (SKOS)
    ↓ correções
Termboard JSON (corrigido)
    ↓ re-export
OWL file (v04.1, v05, etc.)
```

## 1.3. Checklist Consolidado de Validação

### 1.3.1. Sintaxe

| # | Item de Validação | Termboard | Protégé Desktop | OrionBelt |
|---|-------------------|-----------|-----------------|-----------|
| 1 | Arquivo OWL/XML válido | ❌ | ⚠️ Erros de parsing | ✅ Load validation |
| 2 | Namespace RDF correto | ❌ | ⚠️ Erros de parsing | ✅ Load validation |
| 3 | Namespace OWL correto | ❌ | ⚠️ Erros de parsing | ✅ Load validation |
| 4 | Namespace SKOS correto | ❌ | ⚠️ Erros de parsing | ✅ Load validation |

### 1.3.2. SKOS

| # | Item de Validação | Termboard | Protégé Desktop | OrionBelt |
|---|-------------------|-----------|-----------------|-----------|
| 5 | Hierarquia `skos:broader` sem ciclos | ✅ Circular hierarchies | ⚠️ HermiT | ✅ Cycles check |
| 6 | Todo `skos:Concept` em `skos:ConceptScheme` | ❌ | ⚠️ Visual check | ✅ Orphans check |
| 7 | Todo `skos:ConceptScheme` tem `skos:hasTopConcept` | ❌ | ⚠️ Visual check | ✅ SKOS validation |
| 8 | `skos:prefLabel` único por idioma | ✅ Synonym conflicts | ⚠️ Visual check | ✅ Duplicate labels |
| 9 | `skos:altLabel` único por conceito | ✅ Synonym conflicts | ⚠️ Visual check | ✅ Duplicate labels |

### 1.3.3. OWL

| # | Item de Validação | Termboard | Protégé Desktop | OrionBelt |
|---|-------------------|-----------|-----------------|-----------|
| 10 | Reasoner sem inconsistências | ❌ | ✅ HermiT reasoner | ✅ OWL-RL reasoning |
| 11 | Conformidade OWL DL | ❌ | ✅ OWL Lint plugin | ⚠️ OWL-RL only |
| 12 | Propriedades com domínio/alcance definidos | ❌ | ✅ OntoCheck plugin | ✅ Missing domain/range |
| 13 | Restrições lógicas corretas | ❌ | ✅ HermiT reasoner | ✅ OWL-RL reasoning |

### 1.3.4. Termboard: Qualidade dos Conceitos

| # | Item de Validação | Termboard | Protégé Desktop | OrionBelt |
|---|-------------------|-----------|-----------------|-----------|
| 14 | Nomes no plural (devem ser singulares) | ✅ Plurals in name | ❌ | ❌ |
| 15 | Termos com nomes similares (typos) | ✅ Similar Term Names | ❌ | ❌ |
| 16 | Conflitos de sinônimos | ✅ Synonym conflicts | ❌ | ❌ |
| 17 | Qualidade das descrições (score 0-100) | ✅ Poor Description Quality | ❌ | ❌ |
| 18 | Descrição menciona termo pai | ✅ No parent in description | ❌ | ❌ |
| 19 | Termos sem relações (órfãos) | ✅ No relations | ❌ | ✅ Orphans |
| 20 | Relações duplicadas com pai | ✅ Duplicating parent relations | ❌ | ❌ |
| 21 | Herança múltipla | ✅ Multi parent | ❌ | ❌ |
| 22 | Relações bidirecionais | ✅ Bidirectional Relations | ❌ | ❌ |
| 23 | Propriedades identificadas corretamente | ✅ Potential Properties | ❌ | ❌ |
| 24 | Propriedades sem relação atributiva | ✅ Properties Without Attributive Relations | ❌ | ❌ |
| 25 | Conceitos sem hierarquia | ✅ Concepts Without Hierarchical Relations | ❌ | ❌ |

### 1.3.5. Metadados

| # | Item de Validação | Termboard | Protégé Desktop | OrionBelt |
|---|-------------------|-----------|-----------------|-----------|
| 26 | Título da ontologia preenchido | ❌ | ✅ OntoCheck plugin | ⚠️ Manual check |
| 27 | Versão informada | ❌ | ✅ OntoCheck plugin | ⚠️ Manual check |
| 28 | Data de modificação atualizada | ❌ | ⚠️ Manual check | ❌ |
| 29 | Descrição da ontologia presente | ❌ | ✅ OntoCheck plugin | ⚠️ Manual check |
| 30 | Autor/criador documentado | ❌ | ✅ OntoCheck plugin | ⚠️ Manual check |

### 1.3.6. Visualização

| # | Item de Validação | Termboard | Protégé Desktop | OrionBelt |
|---|-------------------|-----------|-----------------|-----------|
| 31 | Visualização gráfica da hierarquia | ✅ Interactive Graph | ✅ OWLViz / Jambalaya | ✅ Graph view |

---

### 1.3.7. Legenda

- ✅ = Ferramenta cobre o item
- ⚠️ = Cobertura parcial (detecta mas não detalha)
- ❌ = Ferramenta não cobre o item

### 1.3.8. Resumo por Ferramenta

| Ferramenta | Itens cobertos | Custo | Instalação |
|------------|---------------|-------|------------|
| **Termboard** | 14/31 (45%) | Grátis | Web app |
| **Protégé Desktop** (com plugins) | 14/31 (45%) | Grátis | Java |
| **OrionBelt** | 18/31 (58%) | Grátis | Python (pip) |

### 1.3.9. Recomendação

**Combinar Termboard + Protégé Desktop** = **22/31 itens (71%)** sem sobreposição significativa.

**Adicionar OrionBelt** = **29/31 itens (94%)** com cobertura quase total.

---

## 1.4. Arquivos para Validação

| Arquivo | Caminho | Uso |
|---------|---------|-----|
| OWL | `docs/sessions/260913-termboad_model/260913-termboard_model_repository_v04.owl` | Protégé, OrionBelt |
| JSON | `docs/sessions/260913-termboad_model/260913-termboard_model_repository-04.json` | Termboard |

---

## 1.5. Teste 1: Termboard (12 Semantic Checks)

### 1.5.1. Pré-requisitos
- Conta no Termboard (https://termboard.com)
- Arquivo JSON: `260913-termboard_model_repository-04.json`

### 1.5.2. Procedimento
1. Abrir Termboard → Load/Save → Import JSON
2. Selecionar arquivo `260913-termboard_model_repository-04.json`
3. Tools → Semantic Checks
4. Executar **cada uma** das 12 verificações:

| # | Check | Ação esperada | Resultado |
|---|-------|---------------|-----------|
| 1 | Plurals in name | Nenhum termo no plural | ☐ |
| 2 | Similar Term Names | Nenhum par similar | ☐ |
| 3 | Synonym conflicts | Nenhum conflito | ☐ |
| 4 | Poor Description Quality | Score > 60 em todos | ☐ |
| 5 | No parent in description | Todos mencionam pai | ☐ |
| 6 | No relations | Todos têm relações | ☐ |
| 7 | Duplicating parent relations | Nenhuma duplicata | ☐ |
| 8 | Multi parent | Nenhum com 2+ pais | ☐ |
| 9 | Circular hierarchies | Nenhum ciclo | ☐ |
| 10 | Bidirectional Relations | Nenhum par bidirecional | ☐ |
| 11 | Potential Properties | Todos classificados corretamente | ☐ |
| 12 | Concepts Without Hierarchical Relations | Todos na hierarquia | ☐ |

5. **Anotar resultados** na coluna "Resultado" (✓ = OK, ✗ = erro, ! = warning)
6. **Corrigir** erros no Termboard
7. **Re-exportar** JSON (se houve correções)

### 1.5.3. Resultado Esperado
- ✅ Todos os 12 checks passando sem erros
- ⚠️ Warnings aceitáveis (ex: qualidade de descrição pode variar)

---

## 1.6. Teste 2: Protégé Desktop (HermiT + Plugins)

### 1.6.1. Pré-requisitos
- Java instalado (`java -version`)
- Protégé Desktop 5.6.9+ (https://protege.stanford.edu/software/)
- Arquivo OWL: `260913-termboard_model_repository_v04.owl`

### 1.6.2. Instalação
```bash
java -version  # verificar Java
# Se não instalado: https://adoptium.net/
# Baixar Protégé: https://protege.stanford.edu/software/
```

### 1.6.3. Procedimento

#### 1.6.3.1. Passo 1: Abrir a Ontologia
1. File → Open
2. Navegar até `docs/sessions/260913-termboad_model/`
3. Selecionar `260913-termboard_model_repository_v04.owl`
4. Aguardar carregamento completo

#### 1.6.3.2. Passo 2: Verificar Metadados
1. Tab "Active Ontology"
2. Verificar:

| Campo        | Esperado                                                              | Atual | Status |
| ------------ | --------------------------------------------------------------------- | ----- | ------ |
| Ontology IRI | `https://termboard.com/ontology/f1a2b3c4-d5e6-7890-abcd-ef1234567890` |       | ☐      |
| Title        | Preenchido                                                            |       | ☐      |
| Version      | `4.1`                                                                 |       | ☐      |
| Label        | Preenchido                                                            |       | ☐      |
| Comment      | Preenchido                                                            |       | ☐      |

#### 1.6.3.3. Passo 3: Executar Reasoner (HermiT)
1. Tools → Reasoner → **HermiT**
2. Reason → **Start Reasoner**
3. Aguardar resultado:

| Resultado        | Significado                  | Ação                  |
| ---------------- | ---------------------------- | --------------------- |
| **Consistent**   | Ontologia logicamente válida | Continuar             |
| **Inconsistent** | Contradições lógicas         | Investigar e corrigir |

4. Se **Consistent**: verificar class hierarchy (taxonomy)
5. Se **Inconsistent**: anotar axiomas conflitantes

#### 1.6.3.4. Passo 4: OWL Lint
1. Tools → OWL Lint (se disponível)
2. Revisar issues reportados:

| Issue Type          | Severidade | Descrição                | Status |
| ------------------- | ---------- | ------------------------ | ------ |
| Missing labels      | Warning    | Conceitos sem rdfs:label | ☐      |
| Missing annotations | Warning    | Conceitos sem anotações  | ☐      |
| Deprecated entities | Info       | Entidades obsoletas      | ☐      |

#### 1.6.3.5. Passo 5: Visualização
1. Window → Tabs → OWLViz
2. Verificar hierarquia gráfica
3. Confirmar que todos os conceitos estão conectados

#### 1.6.3.6. Passo 6: Plugins Instalados

| Plugin          | Função                     | Como usar                          | Status              |
| --------------- | -------------------------- | ---------------------------------- | ------------------- |
| ~~HermiT~~      | Reasoner OWL DL            | Tools → Reasoner → HermiT → Reason | Incluído no Protégé |
| **OWL Lint**    | Quality control, debugging | Tools → OWL Lint                   | Plugin adicional    |
| ~~OntoCheck~~   | Metadata completeness      | Tools → OntoCheck                  | Plugin adicional    |
| ~~OntoDebug~~   | Inconsistency debugger     | Tools → OntoDebug                  | Plugin adicional    |
| ~~OWLViz~~      | Visualização hierárquica   | Window → Tabs → OWLViz             | Incluído no Protégé |
| **SKOS Editor** | Edição/visualização SKOS   | View → SKOS Editor                 | Plugin adicional    |
| ~~Pellet~~      | Reasoner alternativo       | Tools → Reasoner → Pellet          | Plugin adicional    |

> **Nota:** Para instalar plugins adicionais: File → Check for Plugins. Nem todos os plugins estão disponíveis no repositório oficial do Protégé. SKOS Editor requer download manual: https://github.com/simonjupp/skoseditor

### 1.6.4. Resultado Esperado
- ✅ Reasoner: **Consistent**
- ✅ Metadados completos
- ✅ Sem erros críticos no OWL Lint
- ✅ Visualização mostra hierarquia coesa

---

## 1.7. Teste 3: OrionBelt (SKOS Validation + OWL-RL)

### 1.7.1. Pré-requisitos
- Python 3.8+ instalado
- pip instalado
- Arquivo OWL: `260913-termboard_model_repository_v04.owl`

### 1.7.2. Instalação
```bash
# Instalar OrionBelt
pip install orionbelt-ontology-builder

# Ou usar uv (mais rápido)
uv tool install orionbelt-ontology-builder
```

### 1.7.3. Procedimento

#### 1.7.3.1. Passo 1: Iniciar OrionBelt
```bash
orionbelt-ontology-builder
# Abre automaticamente no browser (http://localhost:8501)
```

#### 1.7.3.2. Passo 2: Carregar Ontologia
1. Na aba **Source** ou **Load**
2. Upload do arquivo `260913-termboard_model_repository_v04.owl`
3. Aguardar processamento

#### 1.7.3.3. Passo 3: SKOS Validation
1. Ir para aba **Validation**
2. Executar checks SKOS:

| Check | Esperado | Resultado |
|-------|----------|-----------|
| Missing prefLabels | Nenhum | ☐ |
| Orphan concepts | Nenhum | ☐ |
| Duplicate labels | Nenhum | ☐ |
| Cycles in broader | Nenhum | ☐ |
| Missing ConceptScheme | Nenhum | ☐ |

#### 1.7.3.4. Passo 4: OWL-RL Reasoning
1. Na aba **Validation**
2. Executar OWL-RL reasoning:

| Check | Esperado | Resultado |
|-------|----------|-----------|
| Missing domains/ranges | Nenhum | ☐ |
| Untyped individuals | Nenhum | ☐ |
| Inconsistencies | Nenhum | ☐ |

#### 1.7.3.5. Passo 5: Visualização
1. Aba **Visualization**
2. Verificar graph view
3. Confirmar hierarquia

### 1.7.4. Resultado Esperado
- ✅ Sem erros SKOS
- ✅ Sem erros OWL-RL
- ✅ Visualização confirma estrutura

---

## 1.8. Matriz de Resultados

Após executar os 3 testes, preencher:

| # | Item de Validação | Termboard | Protégé | OrionBelt | Status Final |
|---|-------------------|-----------|---------|-----------|--------------|
| 1 | Arquivo OWL/XML válido | — | | | |
| 2 | Namespace RDF correto | — | | | |
| 3 | Namespace OWL correto | — | | | |
| 4 | Namespace SKOS correto | — | | | |
| 5 | Hierarquia skos:broader sem ciclos | | | | |
| 6 | Todo skos:Concept em ConceptScheme | — | | | |
| 7 | Todo ConceptScheme tem hasTopConcept | — | | | |
| 8 | skos:prefLabel único por idioma | | | | |
| 9 | skos:altLabel único por conceito | | | | |
| 10 | Reasoner sem inconsistências | — | | | |
| 11 | Conformidade OWL DL | — | | | |
| 12 | Propriedades com domínio/alcance | — | | | |
| 13 | Restrições lógicas corretas | — | | | |
| 14 | Nomes no plural | | — | — | |
| 15 | Termos com nomes similares | | — | — | |
| 16 | Conflitos de sinônimos | | — | — | |
| 17 | Qualidade das descrições | | — | — | |
| 18 | Descrição menciona termo pai | | — | — | |
| 19 | Termos sem relações | | — | | |
| 20 | Relações duplicadas com pai | | — | — | |
| 21 | Herança múltipla | | — | — | |
| 22 | Relações bidirecionais | | — | — | |
| 23 | Propriedades identificadas corretamente | | — | — | |
| 24 | Propriedades sem relação atributiva | | — | — | |
| 25 | Conceitos sem hierarquia | | — | — | |
| 26 | Título da ontologia | — | | — | |
| 27 | Versão informada | — | | — | |
| 28 | Data de modificação | — | | — | |
| 29 | Descrição da ontologia | — | | — | |
| 30 | Autor/criador documentado | — | | — | |
| 31 | Visualização gráfica | | | | |

**Legenda:** ✓ = OK, ✗ = Erro, ! = Warning, — = Não aplicável

---

## 1.9. Iteração e Correções

### 1.9.1. Ordem Recomendada

1. **Termboard** (12 checks) → corrigir qualidade dos conceitos
2. **Re-exportar** JSON e OWL
3. **Protégé Desktop** (HermiT + plugins) → corrigir OWL/SKOS
4. **OrionBelt** → validar SKOS e OWL-RL
5. **Preencher** Matriz de Resultados (Seção 1.8)

### 1.9.2. Versionamento

| Versão | Data | Mudanças |
|--------|------|----------|
| v04 | 2026-09-16 | Facetas, 21 conceitos |
| v04.1 | -- | Correções pós-validação |
| v05 | -- | Novos conceitos/relações |

---

## 1.10. Referências

- W3C SKOS Reference: https://www.w3.org/TR/skos-reference/
- W3C RDF Validation: https://validator.w3.org/
- Protégé Documentation: https://protege.stanford.edu/documentation.php
- OrionBelt: https://github.com/ralforion/orionbelt-ontology-builder
- Termboard Semantic Checks: https://termboard.com/manual/page/right-sidebar/semantic-checks.html

---

## 1.11. Notas

- **Termboard** é a ferramenta primária de edição e qualidade dos conceitos
- **Protégé Desktop** é um aplicativo gráfico (GUI), não requer código Java
- **HermiT** é o reasoner padrão para OWL DL (incluído no Protégé)
- **OrionBelt** é browser-based, sem Java (Python), melhor para SKOS validation
- Após validação, documentar resultados na Matriz (Seção 1.8)


```csvtable
source: 11-systems^dev/260813-painel_controle^docs/sessions/260913-termboad_model/260912-termboard_model_repository.csv
```

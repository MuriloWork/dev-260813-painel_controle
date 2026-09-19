# 1. Plano de Validação do Modelo Semântico (OWL/SKOS)

## 1.1. Contexto

- **Modelo atual:** `260913-termboard_model_repository_v04.owl`
  - 21 conceitos, 5 ConceptSchemes (facets), padrões SKOS/RDFS/OWL
  - Facetas: Content, Structure, Process, Tool, Scope
  - Conceito hub: `repository` (topConceptOf todas as facets)
- **Objetivo:** validação completa (consistência lógica, conformidade OWL DL, SKOS, visualização)

---

## 1.2. Fluxo de Trabalho

```
Termboard JSON (edição)
    ↓ export
OWL file
    ↓ validação
Termboard (12 checks) + Protégé Desktop (HermiT + plugins)
    ↓ correções
Termboard JSON (corrigido)
    ↓ re-export
OWL file (v04.1, v05, etc.)
```

---

## 1.3. Checklist Consolidado de Validação

### 1.3.1. Sintaxe

| # | Item de Validação | Termboard | Protégé Desktop | Outros (OrionBelt/ROBOT) |
|---|-------------------|-----------|-----------------|--------------------------|
| 1 | Arquivo OWL/XML válido (W3C validator) | ❌ | ⚠️ Erros de parsing | ⚠️ ROBOT: `robot validate` |
| 2 | Namespace RDF correto | ❌ | ⚠️ Erros de parsing | ⚠️ ROBOT: `robot diff` |
| 3 | Namespace OWL correto | ❌ | ⚠️ Erros de parsing | ⚠️ ROBOT: `robot diff` |
| 4 | Namespace SKOS correto | ❌ | ⚠️ Erros de parsing | ⚠️ ROBOT: `robot diff` |

### 1.3.2. SKOS

| # | Item de Validação | Termboard | Protégé Desktop | Outros (OrionBelt/ROBOT) |
|---|-------------------|-----------|-----------------|--------------------------|
| 5 | Hierarquia `skos:broader` sem ciclos | ✅ Circular hierarchies | ⚠️ HermiT: ontologia inconsistente | ✅ OrionBelt: cycles check |
| 6 | Todo `skos:Concept` em `skos:ConceptScheme` | ❌ | ⚠️ SKOS Editor plugin: visual check | ✅ OrionBelt: orphans check |
| 7 | Todo `skos:ConceptScheme` tem `skos:hasTopConcept` | ❌ | ⚠️ SKOS Editor plugin: visual check | ✅ OrionBelt: SKOS validation |
| 8 | `skos:prefLabel` único por idioma | ✅ Synonym conflicts | ⚠️ SKOS Editor plugin: visual check | ✅ OrionBelt: duplicate labels |
| 9 | `skos:altLabel` único por conceito | ✅ Synonym conflicts | ⚠️ SKOS Editor plugin: visual check | ✅ OrionBelt: duplicate labels |

> **Nota:** Protégé com plugin **SKOS Editor** (https://github.com/simonjupp/skoseditor) permite visualizar e navegar em ontologias SKOS, mas não tem validação automática. Cobertura é parcial (visual/manual).

### 1.3.3. OWL

| # | Item de Validação | Termboard | Protégé Desktop | Outros (OrionBelt/ROBOT) |
|---|-------------------|-----------|-----------------|--------------------------|
| 10 | Reasoner HermiT sem inconsistências | ❌ | ✅ HermiT reasoner | ⚠️ ROBOT: `robot verify` |
| 11 | Conformidade OWL DL | ❌ | ✅ OWL Lint plugin | ⚠️ ROBOT: `robot verify` |
| 12 | Propriedades com domínio/alcance definidos | ❌ | ✅ OntoCheck plugin | ✅ OrionBelt: missing domain/range |
| 13 | Restrições lógicas corretas | ❌ | ✅ HermiT reasoner | ⚠️ ROBOT: `robot verify` |

### 1.3.4. Termboard: Qualidade dos Conceitos

| # | Item de Validação | Termboard | Protégé Desktop | Outros (OrionBelt/ROBOT) |
|---|-------------------|-----------|-----------------|--------------------------|
| 14 | Nomes no plural (devem ser singulares) | ✅ Plurals in name | ❌ | ❌ |
| 15 | Termos com nomes similares (typos) | ✅ Similar Term Names | ❌ | ❌ |
| 16 | Conflitos de sinônimos | ✅ Synonym conflicts | ❌ | ❌ |
| 17 | Qualidade das descrições (score 0-100) | ✅ Poor Description Quality | ❌ | ❌ |
| 18 | Descrição menciona termo pai | ✅ No parent in description | ❌ | ❌ |
| 19 | Termos sem relações (órfãos) | ✅ No relations | ❌ | ✅ OrionBelt: orphans |
| 20 | Relações duplicadas com pai | ✅ Duplicating parent relations | ❌ | ❌ |
| 21 | Herança múltipla | ✅ Multi parent | ❌ | ❌ |
| 22 | Relações bidirecionais | ✅ Bidirectional Relations | ❌ | ❌ |
| 23 | Propriedades identificadas corretamente | ✅ Potential Properties | ❌ | ❌ |
| 24 | Propriedades sem relação atributiva | ✅ Properties Without Attributive Relations | ❌ | ❌ |
| 25 | Conceitos sem hierarquia | ✅ Concepts Without Hierarchical Relations | ❌ | ❌ |

### 1.3.5. Metadados

| # | Item de Validação | Termboard | Protégé Desktop | Outros (OrionBelt/ROBOT) |
|---|-------------------|-----------|-----------------|--------------------------|
| 26 | Título da ontologia preenchido | ❌ | ✅ OntoCheck plugin | ✅ ROBOT: `robot verify` |
| 27 | Versão informada | ❌ | ✅ OntoCheck plugin | ✅ ROBOT: `robot verify` |
| 28 | Data de modificação atualizada | ❌ | ⚠️ Manual check | ❌ |
| 29 | Descrição da ontologia presente | ❌ | ✅ OntoCheck plugin | ✅ ROBOT: `robot verify` |
| 30 | Autor/criador documentado | ❌ | ✅ OntoCheck plugin | ✅ ROBOT: `robot verify` |

### 1.3.6. Visualização

| # | Item de Validação | Termboard | Protégé Desktop | Outros (OrionBelt/ROBOT) |
|---|-------------------|-----------|-----------------|--------------------------|
| 31 | Visualização gráfica da hierarquia | ✅ Interactive Graph | ✅ OWLViz / Jambalaya | ✅ OrionBelt: graph view |

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
| **OrionBelt** | 12/31 (39%) | Grátis | Python (pip) |
| **ROBOT** | 10/31 (32%) | Grátis | Java |

### 1.3.9. Recomendação

**Combinar Termboard + Protégé Desktop** = **22/31 itens (71%)** sem sobreposição significativa.

Se quiser cobertura quase total (29/31 = 94%), adicionar **OrionBelt** (sem Java).

---

## 1.4. Procedimento por Ferramenta

### 1.4.1. Termboard (validações built-in)

1. Abrir modelo no Termboard
2. Tools > Semantic Checks
3. Executar cada uma das 12 verificações
4. Corrigir itens flagados
5. Re-exportar OWL

### 1.4.2. Protégé Desktop

#### 1.4.2.1. Instalação
```bash
java -version  # verificar Java
```
- Baixar: https://protege.stanford.edu/software/
- Versão: 5.6.9+
- Instalar e abrir

#### 1.4.2.2. Validação OWL
1. File → Open → selecionar `.owl`
2. **Reasoner:** Tools → Reasoner → HermiT → Reason → Start Reasoner
3. **Plugins:** File → Check for installed plugins → instalar OWL Lint e OntoCheck
4. **Visualização:** Window → Tabs → OWLViz

#### 1.4.2.3. Plugins de Validação

| Plugin | Função | Como usar | Status |
|--------|--------|-----------|--------|
| **OWL Lint** | Quality control, debugging | Tools → OWL Lint | Incluído no Protégé |
| **OntoCheck** | Metadata completeness | Tools → OntoCheck | Incluído no Protégé |
| **OntoDebug** | Inconsistency debugger | Tools → OntoDebug | Incluído no Protégé |
| **OWLViz** | Visualização hierárquica | Window → Tabs → OWLViz | Incluído no Protégé |
| **SKOS Editor** | Edição/visualização SKOS | https://github.com/simonjupp/skoseditor | Plugin adicional (download manual) |

### 1.4.3. OrionBelt (alternativa sem Java)

```bash
pip install orionbelt-ontology-builder
orionbelt-ontology-builder  # abre no browser
```

- SKOS validation: missing prefLabels, orphans, duplicate labels, cycles
- OWL-RL reasoning
- Visualização interativa

---

## 1.5. Iteração e Correções

### 1.5.1. Ordem Recomendada

1. **Termboard** (12 checks) → corrigir qualidade dos conceitos
2. **Re-exportar** OWL
3. **Protégé Desktop** (HermiT + plugins) → corrigir OWL/SKOS
4. **OrionBelt** (opcional) → validar SKOS specific

### 1.5.2. Versionamento

| Versão | Data | Mudanças |
|--------|------|----------|
| v04 | 2026-09-16 | Facetas, 21 conceitos |
| v04.1 | -- | Correções pós-validação |
| v05 | -- | Novos conceitos/relações |

---

## 1.6. Referências

- W3C SKOS Reference: https://www.w3.org/TR/skos-reference/
- W3C RDF Validation: https://validator.w3.org/
- Protégé Documentation: https://protege.stanford.edu/documentation.php
- WebProtégé: https://webprotege.stanford.edu/
- SKOS Editor Plugin: https://github.com/simonjupp/skoseditor
- OrionBelt: https://github.com/ralforion/orionbelt-ontology-builder
- ROBOT: https://github.com/oborel/robot
- Termboard Semantic Checks: https://termboard.com/manual/page/right-sidebar/semantic-checks.html

---

## 1.7. Notas

- **Termboard** é a ferramenta primária de edição e qualidade dos conceitos
- **Protégé Desktop** é um aplicativo gráfico (GUI), não requer código Java
- **HermiT** é o reasoner padrão para OWL DL
- **SKOS Editor** é plugin adicional para Protégé (download manual: https://github.com/simonjupp/skoseditor)
- **OrionBelt** é browser-based, sem Java (Python)
- Após validação, documentar resultados no checklist (Seção 3)

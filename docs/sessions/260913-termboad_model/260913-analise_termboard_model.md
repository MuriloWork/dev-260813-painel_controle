# 1. question 01
Sobre o modelo @docs/sessions/260913-termboad_model/260912-termboard_model_repository.json

As entidades atuais foram geradas por IA, sem um propósito definido, portanto com ênfase na semântica dos conceitos. Quero praticar e aprender a respeito das lógicas de configuração de conceitos e relacionamentos, alinhados ao modelo SKOS.

sobre os termos/conceitos atuais 
1. recomendaria alguma revisão? novos nomes? 

sobre as relations atuais. 
1. os nomes são recomendados por algum modelo normativo? 
2. existe fonte de consulta para os nomes mais usados? 
3. não entendi muito bem as relations onde source=repository. Pode criar frases lógicas para cada uma dessas relations? 
4. considerando um contexto de gerenciamento de repositórios e seus artefatos, como seriam utilizadas as relations is-a? 
# 2. resposta 
## 2.1. Análise do Modelo: 260912-termboard_model_repository

Li o modelo JSON e o OWL exportado. Aqui vai a análise:

---

### 2.1.1. Revisão dos Termos/Conceitos

**Termos atuais (10):**
- `repository` (concept), `code repository`, `artifact repository`, `data repository`, `documentation repository`, `version control system`, `commit`, `branch`, `merge`, `pull request`

**Problemas identificados:**

| Problema | Exemplo | Sugestão |
|---------|---------|----------|
| Mistura de níveis conceituais | `repository` (conceito abstrato) vs `commit` (evento/processo) | Separar em schemes distintos ou usar tipos mais claros |
| `version control system` como termo solto | É uma *ferramenta*, não um tipo de repo | Renomear para `version control tool` ou mover para conceito separado |
| `merge` é um *processo*, não uma entidade | Deveria ser `merge operation` ou `merge event` | Usar `skos:Concept` para o evento |
| Falta `tag` / `release` | Conceitos essenciais em repos | Adicionar |

**Proposta de renomeação (alinhada SKOS):**

| Atual | Proposta | Justificativa |
|-------|----------|---------------|
| `repository` | `Repository` (ConceptScheme) | Usar como esquema conceitual, não como conceito solto |
| `commit` | `Commit` (event) | Evento pontual, não entidade persistente |
| `merge` | `Merge Operation` | Processo, não coisa |
| `pull request` | `Pull Request` (proposal) | Já ok, mas formalizar como `MergeRequest` (GitLab) |
| `version control system` | `Version Control Tool` | Ferramenta, não conceito de repo |

---

### 2.1.2. Nomes das Relations

**Não, os nomes atuais NÃO seguem modelo normativo SKOS.** O SKOS define relações padrão:

| SKOS Standard | Função | Uso no modelo atual |
|---------------|--------|---------------------|
| `skos:broader` / `skos:narrower` | Hierarquia taxonômica | `is-a` (correto, mas nome diferente) |
| `skos:related` | Associativa (não-hierárquica) | Não usado |
| `skos:semanticRelation` | Superpropriedade | Não usado |

As relations customizadas (`supports`, `proposes changes to`, `is managed by`, `undergoes`, `contains`) são **propriedades de domínio específico**, não SKOS padrão. São válidas em OWL/RDFS, mas não em puro SKOS.

---

### 2.1.3. Relations onde source=repository

Identifiquei 3 relações onde `source = repository`:

| Relation | Target | Frase lógica |
|----------|--------|--------------|
| `repository → supports → branch` | branch | **"Um repositório suporta branches"** — O repo permite a existência de linhas paralelas de desenvolvimento |
| `repository → is managed by → version control system` | version control system | **"Um repositório é gerenciado por um sistema de controle de versão"** — O VCS é a ferramenta que opera sobre o repo |
| `repository → contains → commit` | commit | **"Um repositório contém commits"** — O repo armazena o histórico de snapshots |

**Observação:** A relation `repository → contains → commit` está modelada com `relationType: Aggregation` (seta diamond), o que é semanticamente correto — commits são *partes* do repositório.

---

### 2.1.4. Relations `is-a` no contexto de repositórios

As 4 relações `is-a` atuais são **corretas** e mapeiam para `skos:broader`/`skos:narrower`:

```
code repository       is-a → repository
artifact repository   is-a → repository  
data repository       is-a → repository
documentation repository is-a → repository
```

**Equivalentes SKOS:**
```turtle
code_repository skos:broader repository .
repository skos:narrower code_repository .
```

**Como seriam usadas em contexto:**
- **Navegação hierárquica:** "Mostre todos os tipos de repositório"
- **Inferência:** "code repository herda todas as propriedades de repository"
- **Validação:** "Todo repo deve ter um VCS associado" (via restrição OWL)

**Problema atual:** A relation `is-a` está definida como `relationType: Generalization`, mas no OWL exportado aparece como `c:is-a` (propriedade customizada) **e também** como `rdfs:subClassOf` / `skos:broader`. Isso é redundante — no SKOS puro, `is-a` deveria ser substituído por `skos:broader`.

---

### 2.1.5. Resumo de Recomendações

1. **Usar SKOS como vocabulário base** — `skos:broader` em vez de `is-a`, `skos:related` em vez de `supports` etc.
2. **Separar entidades de processos** — `commit` e `merge` são eventos, não tipos de repo
3. **Adicionar conceitos faltantes** — `tag`, `release`, `remote`, `clone`
4. **Definir um ConceptScheme** — `Repository` como esquema, com conceitos narrower

Quer que eu proponha uma revisão estruturada do modelo JSON?

# 3. question 02

agora temos apenas relations [narrower, related]
como especificar as diferenças entre as diversas "related"?


# 1. user
ontology pipeline
contexto: temos sessoes em andamento, sobre construção de modelos semanticos e ontologia

quero seguir o pipeline recomendado em https://www.ontologypipeline.com/, operacionalizado pelo webapp https://termboard.com/manual/

no momento preciso esclarecer alguns pontos conceituais/estruturais sobre os modelos semanticos/ontologicos
1. um modelo [semantico, ontologico] precisa partir de um conceito central unico, tal qual um mapa mental, ou permite diversos conceitos de primeiro nivel sem nenhum relacionamento entre si?
2. que relacionamento é recomendavel entre os conceitos de primeio nivel e dominios de conhecimento?
2.1. qual a pratica recomendada, considerando uma premissa de boa conformidade com [dicionarios, modelos] ontologicos publicos e disponiveis na web?

# 2. agent

## 2.1. Conceito Central Único vs. Múltiplos Conceitos de Primeiro Nível

**Resposta curta:** Um modelo semântico **não exige** um único conceito central como um mapa mental. Pode ter múltiplos conceitos de primeiro nível **sem relação direta entre si**, desde que estejam unidos por um **escopo de domínio comum**.

**Detalhamento:**

O workflow do Termboard (Step 5 do Semantic Data Model Workshop) produz exatamente isso: *"a canvas with 10-20 core concepts representing key business entities, events, or attributes."* Esses conceitos não precisam estar todos conectados diretamente entre si no início.

Porém, há uma distinção importante entre os **componentes** do modelo:

| Componente                 | Estrutura                                                                                              | Exemplo                                                        |
| -------------------------- | ------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------- |
| **Modelo Semântico (SDM)** | Múltiplos conceitos de 1º nível, conectados por relações semânticas (não necessariamente hierárquicas) | `Cliente` — `Pedido` — `Produto` (sem relação is-a entre eles) |
| **Taxonomia**              | Hierarquia com **um único root** (conceito raiz), usando relações `is-a`/`Generalization`              | `Veículo` → `Carro` → `Sedan`                                  |

A **taxonomia** (passo 6 do workshop) sim recomenda uma estrutura com raiz única — mas isso é um *componente* do modelo, não o modelo inteiro.

**Recomendação prática:** Comece com os conceitos de negócio extraídos do domínio (Step 5), depois construa taxonomias parciais para cada ramo conceitual relevante, e finalmente conecte tudo com relações semânticas (Step 8).



## 2.2. Relacionamento entre Conceitos de Primeiro Nível e Domínios de Conhecimento

O Ontology Pipeline define uma **camada de domínio** que engloba os conceitos:

- **Controlled Vocabulary** → define os termos do domínio
- **Taxonomy** → estrutura hierárquica dentro do domínio
- **Thesaurus** → reconcilia sinônimos e termos relacionados
- **Ontology** → adiciona lógica e regras ao domínio

A relação recomendada é:

```
Domínio de Conhecimento
├── Conceitos de 1º nível (entidades/entidades de negócio)
│   ├── Conceitos filhos (subtipos via is-a)
│   └── Propriedades (atributos)
├── Relações semânticas (entre conceitos do mesmo domínio)
└── Regras de inferência (regras do domínio)
```

**Conceitos de primeiro nível são parte constituinte de um domínio**, não entidades soltas. O domínio fornece o **escopo** e o **contexto** que dão significado aos conceitos.



## 2.3. Prática Recomendada para Conformidade com Ontologias Públicas

O Termboard documenta explicitamente ontologias públicas que podem ser importadas e usadas como base:

| Ontologia | Domínio | Formato |
|---|---|---|
| **Schema.org** | Geral (Web) | JSON-LD, RDFa |
| **FIBO** | Financeiro | OWL |
| **Dublin Core** | Metadados | RDF |
| **FOAF** | Redes Sociais | RDF |
| **SKOS** | Thesauri/Taxonomias | RDF |

**Prática recomendada (conforme documentação do Termboard):**

1. **Importe ontologias públicas existentes** (`File > Import > OWL`) — não reinvente a roda
2. **Mapeie seus termos** para termos já definidos em ontologias públicas usando o **Mapping Studio** do Termboard
3. **Siga o padrão SKOS** para taxonomias e thesauri (formato padrão para interoperabilidade web)
4. **Use `rdfs:subClassOf`** para hierarquias (é o que o Termboard exporta automaticamente como Generalization)
5. **Prefira conceitos já definidos** em ontologias públicas quando disponíveis — por exemplo, se modelando uma empresa, use `schema:Organization` em vez de criar um termo próprio

**Fluxo prático no Termboard:**
```
1. Importar ontologia pública relevante (ex: Schema.org)
2. Identificar conceitos mapeáveis
3. Criar seus conceitos de domínio
4. Usar Mapping Studio para conectar seus conceitos aos da ontologia pública
5. Estender com conceitos específicos do seu negócio
```



## 2.4. Resumo Prático para seu Pipeline

Para operacionalizar no Termboard:

1. **Defina o escopo do domínio** (Step 1 do workshop)
2. **Extraia conceitos centrais** do domínio (Step 5) — podem ser múltiplos, sem relação direta entre si
3. **Construa taxonomias** para cada ramo (Step 6) — aqui sim, raiz única por taxonomia
4. **Importe ontologia pública** relacionada ao domínio (ex: Schema.org, FIBO)
5. **Mapeie** seus conceitos para a ontologia pública (Mapping Studio)
6. **Defina relações semânticas** entre conceitos (Step 8)
7. **Exporte** em OWL/SKOS para interoperabilidade

Deseja que eu busque mais detalhes sobre algum componente específico, ou que elabore o plano de implementação no Termboard?

# 3. user
suas respostas não agregaram muito conhecimento além do que já estava disponivel nos endereços que adicionei no contexto, preciso de algo mais, **com base em boas praticas disponiveis na web**

vou tentar perguntar de outra forma, aproveitando suas respostas
1. sobre Um modelo semântico não exigir um único conceito central
1.1. sua resposta foi clara e diz que pelas regras normativas "Pode ter múltiplos conceitos de primeiro nível sem relação direta entre si, desde que estejam unidos por um escopo de domínio comum.", mas tenho duvidas
1.1.1. se essa é uma boa pratica
1.1.2. se, com base nas boas praticas, seria recomendavel definir relacionamentos, mesmo que fracos, entre os múltiplos conceitos de primeiro nível
1.1.3. se sim, com base nas boas praticas, que tipos de relacionamentos seriam recomendaveis em um dominio voltado para repositorios de artefatos digitais
1.1.4. onde no [OWL/RDF model, termboard] deve ser definido o "escopo de domínio comum"
2. sobre o workflow do Termboard
2.1. voce citou até step 8, mas eu só identifiquei (https://termboard.com/manual/termstorm/workshop-stages.html) até step 4, onde posso consultar os demais steps?
3. sobre a Conformidade com Ontologias Públicas
3.1. indo um além do obvio [import, mapping, SKOS/RDFS models]
3.2. como identificar na nova ontologia os conceitos originados de importação ou os especificos adicionados?
3.3. ao adicionar novos conceitos especificos, naturalmente está sendo definido um sub-dominio de conhecimento, é possivel definir essa relação [dominio, sub-dominio] de forma explicita? 
3.4. se sim, como fazer?

# 4. agent

## 4.1. É boa prática ter múltiplos conceitos de primeiro nível sem relação?

**Sim, é prática aceita — MAS com ressalvas importantes.**

A referência W3C (Achieving Semantic Interoperability Using RDF and OWL) estabelece que o objetivo é **reduzir ambiguidade expressando mais significado**. Conceitos de primeiro nível sem *nenhum* relação entre si violam parcialmente esse princípio, pois criam "ilhas semânticas" difíceis de integrar.

A prática recomendada (metaphacts Semantic Modeling Guidelines, W3C SKOS) é:

- Ter múltiplos conceitos de 1º nível é **aceitável** quando eles representam **entidades de negócio distintas** (ex: `Cliente`, `Produto`, `Pedido`)
- Porém, **mesmo sem relação `is-a`**, eles devem ter **pelo menos relações associativas** que os conectem ao domínio

A abordagem top-down do metaphacts recomenda: *"Start big, by designing high-level domain concepts, then working your way down to specialized sub-ontologies for specific subdomains."* Mas sempre com o modelo respondendo a **competency questions** — perguntas que o modelo deve ser capaz de responder.



## 4.2. Deve-se definir relacionamentos fracos entre conceitos de primeiro nível?

**Sim, é fortemente recomendado.** O W3C SKOS define exatamente isso com `skos:related`:

> *"skos:related enables the representation of associative (non-hierarchical) links, such as the relationship between one type of event and a class of entities which typically participate in it."*

**Tipos de relacionamentos recomendados** (conforme W3C SKOS e metaphacts):

| Tipo de Relação | Construção OWL/SKOS | Quando usar |
|---|---|---|
| **Associativa** | `skos:related` | Conexão semântica onde nenhum é mais geral que o outro |
| **Mapeamento** | `skos:closeMatch`, `skos:exactMatch` | Quando conceitos de esquemas diferentes são equivalentes |
| **Parte-todo** | `skos:broader` (não-hierárquico) | Relação de composição sem ser `is-a` |
| **Dependência** | `owl:ObjectProperty` customizado | Quando um conceito depende do outro para existir |



## 4.3. Tipos de relacionamentos para repositórios de artefatos digitais

Para seu domínio específico, com base em ontologias públicas (DCAT, ADMS, Dublin Core, Helmholtz Digitisation Ontology):

| Relação | Fonte | Exemplo |
|---|---|---|
| `dcterms:isPartOf` | Dublin Core | Artefato → Coleção |
| `dcterms:hasPart` | Dublin Core | Coleção → Artefato |
| `dcterms:references` / `dcterms:isReferencedBy` | Dublin Core | Artefato A ↔ Artefato B |
| `dcterms:isVersionOf` / `dcterms:hasVersion` | Dublin Core | Versão derivada ↔ Original |
| `dcterms:conformsTo` | Dublin Core | Artefato → Esquema/Metadado |
| `dcterms:source` | Dublin Core | Artefato → Fonte de origem |
| `adms:relatedAsset` | ADMS | Ativo semântico → Ativo semântico |
| `dcat:theme` | DCAT | Artefato → Categoria/Classificação |
| `pav:importedFrom` | PAV | Artefato → Fonte de importação |
| `pav:authoredBy` | PAV | Artefato → Agente/Autor |
| `foaf:primaryTopic` | FOAF | Documento → Tópico principal |

**Padrão recomendado para repositórios:** Use Dublin Core como vocabulário base (é o mais interoperável para artefatos digitais), e estenda com ADMS/PAV quando precisar de proveniência e versionamento.



## 4.4. Onde definir o "escopo de domínio comum" no OWL/RDF/Termboard?

### 4.4.1. No SKOS (recomendado para controlled vocabularies):

```turtle
:MeuDominio rdf:type skos:ConceptScheme ;
    dct:title "Repositório de Artefatos Digitais" ;
    skos:hasTopConcept :Artefato ;
    skos:hasTopConcept :Colecao ;
    skos:hasTopConcept :Repositorio .

:Artefato rdf:type skos:Concept ;
    skos:topConceptOf :MeuDominio .
```

**`skos:ConceptScheme`** é o mecanismo padrão W3C para definir o escopo de domínio. Ele:
- Agrupa conceitos em um esquema coeso
- Permite que conceitos participem de múltiplos esquemas (`skos:inScheme`)
- Define pontos de entrada via `skos:hasTopConcept`

### 4.4.2. No OWL:

```turtle
:MeuDominioOntology rdf:type owl:Ontology ;
    owl:imports <http://purl.org/dc/terms/> ;
    owl:imports <http://www.w3.org/2004/02/skos/core#> ;
    rdfs:label "Ontologia de Repositório de Artefatos Digitais"@pt .
```

Aqui o domínio é definido pela própria ontologia (`owl:Ontology`) e seus imports.

### 4.4.3. No Termboard:

O Termboard não tem um campo explícito "ConceptScheme". A prática é:
1. Usar **Extra Fields** para criar um campo "ConceptScheme" ou "Domain"
2. Atribuir o valor do domíio a cada termo via esse campo
3. Usar o **Domain Profiles** para segmentar visualmente



## 4.5. Onde estão os steps 5-10 do Termboard?

Você está confundindo dois recursos diferentes:

| Ferramenta | Steps | Propósito |
|---|---|---|
| **TermStorm** | 4 stages (Collect → Discuss → Vote → Copy) | Ferramenta de workshop colaborativo para **coletar conceitos** |
| **Semantic Data Model Guide** | 10 steps | Guia completo de modelagem semântica |

Os 10 steps estão em: https://termboard.com/manual/howto/semantic-model.html

| Step | Nome | Descrição |
|---|---|---|
| 1 | Domain Scope | Definir limites do domínio |
| 2 | Workshop Preparation | Preparar materiais |
| 3 | Kick-off & Context | Introdução e contexto |
| 4 | Usecases Identification | Identificar casos de uso de dados |
| 5 | Concept Extraction | Extrair conceitos centrais |
| 6 | Hierarchy Building | Construir hierarquias `is-a` |
| 7 | Concept Definitions | Definir descrições |
| 8 | Relation Identification | Identificar relações semânticas |
| 9 | Review & Validation | Revisão e validação |
| 10 | Documentation & Iteration | Documentação e iteração |

O TermStorm (4 stages) é apenas a **ferramenta** para executar o Step 5 (Concept Extraction) de forma colaborativa. Depois, você exporta para o Termboard e continua com os steps 6-10.



## 4.6. Conformidade com Ontologias Públicas (além do óbvio)

### 4.6.1. Como identificar conceitos importados vs. específicos?

**No OWL/RDF, a distinção é feita via namespace:**

```turtle
# Conceito importado (de ontologia pública)
:Pet rdf:type owl:Class ;
    rdfs:label "Pet"@en .
# O namespace indica: Pet pertence à sua ontologia

# Conceito de Schema.org (reusado)
schema:Person rdf:type owl:Class .
# O prefixo "schema:" indica que vem de schema.org

# Conceito específico do seu domínio
:ArtefatoDigital rdf:type owl:Class ;
    rdfs:label "Artefato Digital"@pt .
# O namespace indica: é seu conceito
```

**Prática recomendada (TDCC Ontology Publishing Guide):**

> *"Every term you use from your own namespace should also be defined there. Don't just use a term; define it."*

Use `owl:imports` no cabeçalho da ontologia para declarar formalmente quais ontologias foram importadas. A ferramenta `askwol` pode verificar se os termos externos realmente existem nas ontologias declaradas.

**No Termboard:** Use o **Mapping Studio** para criar mapeamentos explícitos entre seus conceitos e os da ontologia pública. Isso gera `owl:equivalentClass` ou `skos:closeMatch`.

### 4.6.2. É possível definir a relação domínio/sub-domínio explicitamente?

**Sim, de várias formas:**

**Opção A — SKOS (mais simples e recomendada para vocabulários):**

```turtle
:RepositorioDeArtefatos rdf:type skos:ConceptScheme ;
    dct:title "Repositório de Artefatos Digitais" .

:MetadadosParaArtefatos rdf:type skos:ConceptScheme ;
    dct:title "Metadados para Artefatos" ;
    skos:hasTopConcept :MetadataSchema .

# Um conceito pode pertencer a múltiplos esquemas
:MetadataSchema rdf:type skos:Concept ;
    skos:inScheme :RepositorioDeArtefatos ;
    skos:inScheme :MetadadosParaArtefatos .
```

**Opção B — OWL (mais formal):**

```turtle
:MetadadosSubdominio rdf:type owl:Ontology ;
    owl:imports <http://meudominio/ontologia-repositorio> ;
    rdfs:label "Sub-domínio de Metadados" .
```

**Opção C — Hierarquia de classes (ontologia de upper-level):**

```turtle
:SubdominioMetadados rdf:type owl:Class ;
    rdfs:subClassOf :DominioRepositorio .
```

### 4.6.3. Como fazer na prática?

1. **Defina um `skos:ConceptScheme` para cada sub-domínio**
2. **Atribua conceitos a esquemas** via `skos:inScheme`
3. **Use `skos:hasTopConcept`** para marcar os pontos de entrada de cada sub-domínio
4. **Se precisar de hierarquia entre esquemas**, use `owl:imports` no OWL ou documente a relação em anotações
5. **No Termboard:** crie um Extra Field "ConceptScheme" e atribua valores a cada termo; depois filtre por esquema

**Exemplo concreto para seu caso:**

```
ConceptScheme: Repositório de Artefatos Digitais
├── Top Concepts: Artefato, Repositório, Coleção
├── Sub-domínio: Metadados
│   └── Conceitos: Schema, Campo, Qualificador
├── Sub-domínio: Proveniência
│   └── Conceitos: Autor, Origem, Versão
└── Sub-domínio: Acesso
    └── Conceitos: Permissão, Licença, Visibilidade
```

## 4.7. fontes 

**Referências consultadas:**
- W3C SKOS Reference: https://www.w3.org/TR/skos-reference/
- W3C Semantic Interoperability: https://www.w3.org/2001/sw/BestPractices/OEP/SemInt/
- metaphacts Semantic Modeling Guidelines: https://blog.metaphacts.com/semantic-knowledge-modeling-best-practices
- Dublin Core Terms: https://www.dublincore.org/specifications/dublin-core/dcmi-terms/
- TDCC OWL Publishing Guide: https://lod-4tu.tudelft.nl/askwol/guide
- Helmholtz Digitisation Ontology: https://materials-data-science-and-informatics.github.io/Helmholtz-Digitisation-Ontology-Documentation/index-en.html
- PAV Ontology: https://pmc.ncbi.nlm.nih.gov/articles/PMC4177195/

# 1. O que é um Knowledge Graph?

Uma forma útil de pensar é:

> **Knowledge Graph (KG) é uma representação estruturada de conhecimento em que entidades/conceitos são identificados e conectados por relações semanticamente significativas, permitindo que software navegue, consulte e, dependendo do modelo, faça inferências sobre esse conhecimento.**

No modelo RDF, isso aparece de forma muito explícita:

```text
sujeito ── relação ── objeto
```

Por exemplo:

```text
Requirement:REQ-001
       │
       └── satisfies ──> Functionality:F-001
                              │
                              └── realizedBy ──> Component:C-001
```

O RDF padroniza justamente essa representação por **triplas**, formando um grafo direcionado e rotulado. ([W3C](https://www.w3.org/RDF/?utm_source=chatgpt.com "RDF - Semantic Web Standards"))

Mas existe uma distinção importante:

## 1.1. Knowledge Graph ≠ simplesmente banco de dados em grafo

Existem pelo menos duas famílias que vale você conhecer:

**Property Graph**

```text
[Requirement]
 id = REQ-001
 title = ...

      |
 satisfies
      |

[Functionality]
 id = F-001
```

É o universo de ferramentas como Neo4j, JanusGraph etc.

**Semantic Graph / RDF**

```text
:REQ-001
    :satisfies
        :F-001 .
```

Aqui entram RDF, RDFS, OWL, SHACL, SPARQL etc.

Para **o problema que você está investigando**, eu prestaria atenção especial à segunda família.

O W3C define RDF como modelo para representar recursos e relações entre eles, e OWL acrescenta uma linguagem para representar conhecimento mais rico sobre entidades e relações. ([W3C](https://www.w3.org/RDF/?utm_source=chatgpt.com "RDF - Semantic Web Standards"))

---

# 2. E onde entra o que estamos fazendo no MBCG?

Aqui está, na minha opinião, a parte mais interessante.

Você está tentando descobrir:

> **Quais entidades existem no sistema que estamos modelando?**
> 
> **Quais propriedades essas entidades possuem?**
> 
> **Quais valores essas propriedades podem assumir?**
> 
> **Quais relações existem entre as entidades?**
> 
> **Quais regras determinam a validade dessas informações?**

Isso é muito próximo do processo de construção de uma **ontologia/modelo semântico**.

Por exemplo, estamos começando a pensar:

```text
MBSE
│
├── Requirement
│   ├── id
│   ├── title
│   ├── description
│   └── ...
│
├── Function
│   ├── id
│   ├── ...
│
├── Component
│   ├── id
│   ├── ...
│
└── Decision
    ├── id
    └── ...
```

e depois:

```text
Requirement
    │
    ├── satisfies ───────> Function
    │
    ├── allocatedTo ─────> Component
    │
    └── verifiedBy ──────> Test
```

Isso já começa a ser um **modelo de conhecimento**.

E é justamente por isso que acho que **não devemos voltar agora para a tabela `campo | papel | regras | valores`**.

Primeiro devemos descobrir o modelo.

---

# 3. A descoberta que acho que estamos fazendo

Você começou perguntando:

> “Quais devem ser os campos do Frontmatter?”

Mas a pergunta anterior é:

> **“Que tipo de coisa é um Concept dentro do nosso MBSE?”**

E anterior ainda:

> **“Que conhecimento precisamos representar sobre um sistema?”**

E anterior:

> **“Qual é o modelo conceitual de um sistema desenvolvido por engenharia/modelagem?”**

A sequência poderia ser:

```text
Sistema real
      ↓
Domínio do sistema
      ↓
Modelo conceitual
      ↓
Entidades / conceitos
      ↓
Propriedades
      ↓
Relações
      ↓
Restrições
      ↓
Ontologia / modelo semântico
      ↓
Representação OKF
      ↓
Frontmatter + Body
```

Isso explica perfeitamente por que você estava sentindo que as versões anteriores da seção 3 estavam “conceituais demais”.

Nós estávamos tentando configurar a **representação** antes de terminar de definir o **modelo que está sendo representado**.

---

# 4. Existe exatamente literatura sobre isso em Engenharia de Software

E encontrei algo particularmente relevante para sua pergunta.

Há uma revisão sistemática chamada **“Application of knowledge graph in software engineering field: A systematic literature review”**, que analisou mais de 100 trabalhos e selecionou 55 diretamente relacionados. Ela identifica aplicações de Knowledge Graphs em engenharia de software envolvendo, entre outras coisas, **arquitetura de software, detalhes de código, segurança, desenvolvimento inteligente e testes**. O trabalho também analisa técnicas de construção envolvendo **modelagem ontológica, reconhecimento de entidades e integração/fusão de conhecimento**. ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0950584923001829?utm_source=chatgpt.com "Application of knowledge graph in software engineering field: A systematic literature review - ScienceDirect"))

Isso é muito próximo da direção que estamos tomando.

Mais interessante ainda: existe pesquisa especificamente sobre **requirements engineering + ontologia + rastreabilidade**.

Um trabalho de 2019 propõe uma abordagem baseada em ontologia para rastreabilidade de requisitos e utiliza **OWL + Protégé**, modelando tipos de requisitos, artefatos e relações entre eles. ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1877050919303898?utm_source=chatgpt.com "An Ontology-based Approach to Support for Requirements Traceability in Agile Development - ScienceDirect"))

E há trabalho mais recente, de 2025, sobre rastreabilidade entre **requisitos de software e modelos conceituais**, tratando explicitamente traceability como relações entre artefatos. ([Springer Nature Link](https://link.springer.com/article/10.1007/s00766-025-00447-4?utm_source=chatgpt.com "Ontology-based NLP tool for tracing software requirements and conceptual models: an empirical study | Requirements Engineering | Springer Nature Link"))

Portanto, existe uma linha de pesquisa bastante consolidada:

**Requirements Engineering → Ontology → Knowledge Representation → Traceability → Knowledge Graph**

---

# 5. Ferramentas open source que eu investigaria

Não estou dizendo ainda que devemos adotá-las no MBCG. Eu investigaria cada uma para entender **qual problema ela resolve**.

### 5.1.1. Protégé

[Protégé](https://protege.stanford.edu/?utm_source=chatgpt.com)

É provavelmente a primeira ferramenta que eu colocaria na sua lista de estudos.

Ela permite construir ontologias em OWL e visualizar/modelar classes, propriedades e relações.

O interessante para nós não é necessariamente usar Protégé no produto final.

É usá-lo como **laboratório para descobrir o nosso modelo MBSE**.

---

### 5.1.2. RDF / OWL

Eu estudaria os dois juntos.

**RDF**:

> Como representar entidades e relações.

**OWL**:

> Como representar significado e relações mais complexas entre entidades.

A especificação OWL do W3C explica justamente que OWL permite representar conhecimento sobre coisas, grupos de coisas e relações, e que esse conhecimento pode ser usado computacionalmente para verificar consistência ou explicitar conhecimento implícito. ([W3C](https://www.w3.org/OWL/?utm_source=chatgpt.com "OWL - Semantic Web Standards"))

---

### 5.1.3. SHACL

Esse talvez seja **a descoberta mais importante para o problema que você acabou de apresentar**.

O SHACL é uma linguagem para **validar grafos RDF contra condições definidas por “shapes”**. ([W3C](https://www.w3.org/TR/shacl-core/all/?utm_source=chatgpt.com "Cover page | shacl-core | W3C standards and drafts | W3C"))

E veja como isso se aproxima da nossa tabela:

```text
Concept: Requirement

type:
    obrigatório
    valor = "requirement"

title:
    recomendado
    string

description:
    recomendado
    string

...
```

Isso pode ser pensado como uma **restrição sobre a forma válida de um determinado tipo de entidade**.

Ou seja, em vez de escrever apenas:

> Requirement possui `title`.

podemos chegar a algo formal como:

```text
RequirementShape

    type
        minCount = 1
        maxCount = 1

    title
        minCount = 0
        datatype = string

    description
        ...
```

Isso é **muito mais próximo do que você está buscando como “configuração operacional”**.

E o próprio W3C observa que SHACL pode servir não apenas para validação, mas também para construção de interfaces, geração de código e integração de dados. ([W3C](https://www.w3.org/TR/shacl-core/all/?utm_source=chatgpt.com "Cover page | shacl-core | W3C standards and drafts | W3C"))

---

# 6. RDFLib e Apache Jena / RDF4J

Para experimentar programaticamente:

### 6.1.1. Python

[RDFLib](https://rdflib.readthedocs.io/?utm_source=chatgpt.com)

É especialmente interessante para você porque trabalha com Python.

### 6.1.2. Java

[Apache Jena](https://jena.apache.org/?utm_source=chatgpt.com)

É uma plataforma bastante conhecida para RDF, SPARQL e tecnologias semânticas.

### 6.1.3. Alternativa Java

[Eclipse RDF4J](https://rdf4j.org/?utm_source=chatgpt.com)

O RDF4J oferece criação, processamento, armazenamento e consulta de dados RDF. ([Eclipse RDF4J](https://rdf4j.org/documentation/tutorials/getting-started/?utm_source=chatgpt.com "Getting Started With RDF4J · Eclipse RDF4J™ | The Eclipse Foundation"))

---

# 7. E a sua segunda pergunta: “modelagem de dados em aplicação similar”

Sim. E eu procuraria **não apenas por “knowledge graph”**.

Existem quatro áreas que se sobrepõem e que são muito relevantes para o MBCG:

### 7.1.1. A. Ontology Engineering

Procure por:

> ontology engineering  
> ontology modeling  
> ontology development methodology  
> domain ontology  
> ontology design patterns

Aqui você encontrará métodos para descobrir:

```text
conceitos
atributos
relações
restrições
taxonomias
```

---

### 7.1.2. B. Requirements Engineering + Ontology

Procure por:

> ontology requirements engineering

> ontology-based requirements engineering

> requirements ontology

> requirements traceability ontology

Essa área é particularmente próxima do que você está fazendo. O trabalho que mencionei sobre rastreabilidade de requisitos é um bom exemplo. ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1877050919303898?utm_source=chatgpt.com "An Ontology-based Approach to Support for Requirements Traceability in Agile Development - ScienceDirect"))

---

### 7.1.3. C. Software Engineering Knowledge Graph

Procure por:

> software engineering knowledge graph

> software architecture knowledge graph

> requirements knowledge graph

> software development knowledge graph

A revisão sistemática que encontrei é um excelente ponto de partida justamente porque organiza essa literatura. ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0950584923001829?utm_source=chatgpt.com "Application of knowledge graph in software engineering field: A systematic literature review - ScienceDirect"))

---

### 7.1.4. D. Model-Based Systems Engineering + Ontology

E aqui chegamos provavelmente ao **território mais próximo do MBCG**:

> MBSE ontology

> systems engineering ontology

> SysML ontology

> model-based systems engineering knowledge graph

> systems engineering knowledge graph

Porque aí começamos a juntar:

**MBSE + modelo semântico + rastreabilidade + grafo de conhecimento.**

---

# 8. Uma arquitetura conceitual que eu investigaria para o MBCG

Sem decidir ainda que é isso que devemos fazer, eu colocaria como hipótese de trabalho:

```text
                   MBSE
                    │
             modelo conceitual
                    │
          ┌─────────┴─────────┐
          │                   │
       Classes             Relações
          │                   │
     Requirement          satisfies
     Function             realizes
     Component            dependsOn
     Interface            verifies
     Decision             derivesFrom
     Test                 ...
          │
          └─────────┬─────────┘
                    │
                 Ontologia
                    │
             RDF / OWL / SHACL
                    │
              Knowledge Base
                    │
                   OKF
                    │
             ┌──────┴──────┐
             │             │
        Frontmatter       Body
```

E aqui aparece uma possibilidade **muito interessante**:

## 8.1. O Frontmatter poderia ser a manifestação de um modelo semântico.

Em vez de pensar:

> “Vamos inventar seis campos para o Frontmatter.”

poderíamos pensar:

> “Temos um modelo MBSE. Cada tipo de Concept possui determinadas propriedades. O OKF Frontmatter é uma das formas de serializar essas propriedades.”

Nesse cenário:

```text
MBSE Concept
     ↓
Ontology/Class
     ↓
Properties
     ↓
Constraints (SHACL)
     ↓
OKF Frontmatter
```

Isso poderia nos dar exatamente a **inequivocidade operacional** que você está procurando.

---

## 8.2. Mas eu faria uma ressalva importante

Eu **não adotaria RDF/OWL/SHACL automaticamente no MBCG**.

Primeiro precisamos investigar se o nosso problema realmente precisa da complexidade completa dessas tecnologias.

Talvez o resultado seja:

```text
MBSE metamodel
      +
constraints
      +
typed relations
      +
traceability
      ↓
modelo próprio do MBCG
      ↓
OKF
```

e não necessariamente uma implementação de um Knowledge Graph completo.

Mas aprender **Ontology + RDF + OWL + SHACL** pode nos fornecer uma linguagem conceitual extremamente útil para tomar essa decisão.

E, principalmente, **SHACL merece nossa atenção imediata**, porque a pergunta que você acabou de formular — _“quais campos existem, quais são obrigatórios, quais valores são permitidos e quais regras devem ser obedecidas?”_ — é muito próxima do problema que SHACL foi criado para expressar. ([W3C](https://www.w3.org/TR/shacl-core/all/?utm_source=chatgpt.com "Cover page | shacl-core | W3C standards and drafts | W3C"))

## 8.3. Minha sugestão para nossa próxima etapa

Antes de voltar ao documento 3.1.1, eu faria um pequeno **experimento conceitual**, não de programação:

```text
MBSE genérico
    ↓
10–20 conceitos fundamentais
    ↓
relações entre eles
    ↓
propriedades de cada conceito
    ↓
restrições
```

E então tentaríamos representar **um pequeno subconjunto disso em OWL + SHACL**.

Se conseguirmos fazer isso sem artificialidade, teremos uma excelente indicação de que estamos no caminho certo para definir as configurações do MBCG.
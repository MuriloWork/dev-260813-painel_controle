# 1. Model-Based Code Generator — Knowledge Base

> Documento consolidado das decisões, hipóteses e linhas de investigação discutidas até 2026-08-10.
>
> **Status:** base de conhecimento inicial / arquitetura em investigação.

---

## 1.1. Objetivo

Investigar e definir a arquitetura de um sistema de **Model-Based Code Generation (MBCG)** no qual:

- o usuário especifica sistemas por meio de requisitos, arquitetura, modelos e outras especificações;
- agentes de IA participam da especificação, análise, modelagem, validação e geração de código;
- o conhecimento precisa ser consultável tanto por humanos quanto por agentes;
- modelos formais, especialmente UML, devem coexistir com conhecimento descritivo;
- o conhecimento deve ser versionável, rastreável e, idealmente, independente de fornecedor;
- o sistema gerador também é um sistema que será especificado e desenvolvido pelo próprio processo MBCG.

---

# 2. Conceito geral de arquitetura

A arquitetura investigada separa:

1. **Knowledge Base** — conhecimento persistente;
2. **Formal Models** — modelos estruturados/formais, principalmente UML;
3. **Graph** — representação derivada das relações;
4. **Knowledge/Retrieval Layer** — mecanismos para localizar e recuperar conhecimento;
5. **Agents** — consumidores que raciocinam sobre o conhecimento;
6. **Generator** — transforma modelos/especificações em código.

Uma visão conceitual:

```text
                         MODEL-BASED CODE GENERATOR
                                    |
              +---------------------+---------------------+
              |                     |                     |
              v                     v                     v
          System KB            Generator KB        Intelligence KB
              |                     |                     |
          Product/system        The generator       How agents work
          being built           itself              and generate
              |                     |                     |
              +---------------------+---------------------+
                                    |
                            Knowledge Engine
                                    |
                    +---------------+---------------+
                    |               |               |
                  Search          Graph          Retrieval
                    |               |               |
                    +---------------+---------------+
                                    |
                                  Agent
                                    |
                              Code Generator
```

---

# 3. Três Knowledge Bases

A separação em três bases é considerada importante.

## 3.1. System KB

Conhecimento sobre o sistema que está sendo construído pelo MBCG.

Exemplos:

- requirements;
- use cases;
- architecture;
- components;
- classes;
- interfaces;
- data model;
- business rules;
- constraints;
- architectural decisions;
- traceability;
- generation specifications.

Exemplo:

```text
System KB
├── requirements/
├── use-cases/
├── architecture/
├── components/
├── classes/
├── interfaces/
├── decisions/
└── generation/
```

---

## 3.2. Generator KB

Conhecimento sobre o próprio **Model-Based Code Generator**.

O gerador é tratado como um produto de software que também pode ser especificado e desenvolvido pelo próprio processo.

Inclui:

- requisitos do gerador;
- arquitetura;
- componentes;
- classes;
- UML;
- parsers;
- generators;
- templates;
- linguagens suportadas;
- limitações;
- decisões arquiteturais.

Exemplo:

```text
Generator KB
├── requirements/
├── architecture/
├── components/
├── classes/
├── interfaces/
├── uml/
├── generators/
└── decisions/
```

---

## 3.3. Intelligence KB

Conhecimento sobre a inteligência utilizada na interação usuário-agente e nos processos automáticos.

É conceitualmente diferente das duas anteriores.

Inclui:

- skills;
- rules;
- workflows;
- policies;
- prompts;
- templates;
- modeling standards;
- coding standards;
- retrieval strategies;
- validation rules;
- generation strategies.

Exemplo:

```text
Intelligence KB
├── skills/
├── rules/
├── workflows/
├── policies/
├── templates/
└── validation/
```

Uma distinção útil:

```text
System KB       = WHAT
Generator KB    = TOOL
Intelligence KB = HOW
```

---

# 4. Open Knowledge Format (OKF)

## 4.1. Papel do OKF

O OKF é tratado como **formato de conhecimento**, e não como uma plataforma ou banco de dados.

Ele não exige:

- Google Cloud;
- conta Google;
- API key;
- OAuth;
- banco de dados;
- vector database;
- SDK Google;
- LLM;
- framework de agentes.

Uma base pode ser simplesmente uma coleção de arquivos Markdown com YAML frontmatter, organizada segundo as convenções do OKF.

O repositório oficial é:

https://github.com/GoogleCloudPlatform/knowledge-catalog

A especificação atual investigada é OKF v0.2.

---

## 4.2. O que o OKF acrescenta ao Markdown convencional

Markdown, YAML frontmatter e hyperlinks não são novidades do OKF.

O valor do OKF está na combinação de convenções para:

- conceitos;
- tipos;
- títulos;
- descrições;
- tags;
- índices;
- progressive disclosure;
- links entre conceitos;
- provenance;
- generated;
- verified;
- status;
- stale_after;
- sources;
- attestation/trust;
- organização hierárquica.

Assim, o OKF pode ser visto como:

```text
Markdown + YAML
      +
convenções para Knowledge
      +
links
      +
lifecycle/provenance
      +
progressive disclosure
```

---

# 5. Progressive disclosure

Uma característica particularmente relevante para agentes é o uso de `index.md`.

A ideia:

```text
knowledge/index.md
        |
        +--> requirements/index.md
        |       |
        |       +--> REQ-001.md
        |
        +--> architecture/index.md
        |       |
        |       +--> ARCH-001.md
        |
        +--> classes/index.md
                |
                +--> CLASS-001.md
```

O agente não precisa carregar toda a base de uma vez.

Ele pode:

1. ler o índice;
2. identificar a área relevante;
3. ler o índice daquela área;
4. escolher os conceitos;
5. abrir somente os documentos necessários.

---

# 6. OKF Reference Producer

O repositório oficial contém um `reference_agent`.

A conclusão atual é:

> O `reference_agent` é uma demonstração/reference implementation de produção de OKF, não um produtor genérico para o MBCG.

O exemplo é voltado a um fluxo específico, incluindo metadados de BigQuery e crawling/enriquecimento com LLM.

Para o MBCG, a intenção é implementar um **producer próprio**, especialmente para:

- requirements;
- UML/XMI;
- architecture;
- classes;
- traceability;
- generation rules;
- intelligence knowledge.

---

# 7. OKF Reference Consumer / Visualizer

O repositório oficial possui um visualizador de referência.

O fluxo documentado é aproximadamente:

```bash
.venv/bin/python -m reference_agent visualize \
    --bundle ./bundles/<name>
```

O resultado é um `viz.html` self-contained.

O visualizador oferece:

- grafo force-directed;
- nós por tipo;
- arestas derivadas dos links Markdown;
- painel com frontmatter;
- Markdown renderizado;
- navegação pelos links;
- backlinks;
- busca;
- filtros;
- layouts.

Ponto arquitetural importante:

> O visualizador deriva o grafo dos arquivos/conexões; não exige um banco de grafos como fonte primária.

---

# 8. Instalação do repositório oficial

O comando:

```bash
python3.13 -m venv .venv
.venv/bin/pip install --index-url https://pypi.org/simple/ -e .[dev]
```

significa:

- criar ambiente virtual Python;
- instalar o projeto local em modo editable;
- instalar dependências opcionais de desenvolvimento.

Isso não significa instalar uma plataforma OKF.

Para simplesmente criar arquivos OKF, não é necessário instalar o repositório oficial.

---

# 9. Markdown + Graph

A arquitetura proposta é:

```text
                 Markdown / OKF
                       |
                       | parse
                       v
                    Graph
                       |
          +------------+-------------+
          |            |             |
       viewer       retrieval      analysis
```

O Markdown/OKF permanece como **source of truth**.

O grafo é um índice derivado.

Isso evita que o projeto tenha que manter duas bases independentes.

---

# 10. Grafo e eficiência de leitura por agentes

Uma Knowledge Base eficiente para agentes não precisa necessariamente de um banco de grafos.

Entretanto, a base deve ser pensada como um grafo.

Exemplo:

```text
REQ-001
   |
   +----> UC-001
   |
   +----> ARCH-001
   |
   +----> ADR-004
              |
              +----> PAT-003
```

Cada link pode ser transformado em uma aresta.

O OKF fornece mecanismos de estrutura e links, mas não define sozinho um algoritmo completo de retrieval.

Portanto:

```text
OKF
 |
 +-- storage/structure
 |
 +-- links
 |
 +-- metadata
 |
 +-- progressive disclosure
 |
 +-- provenance
 |
 v
Knowledge/Retrieval Layer
 |
 +-- search
 +-- graph traversal
 +-- section retrieval
 +-- ranking
 |
 v
Agent
```

---

# 11. Link inline e risco de navegação prematura

Links Markdown podem aparecer no meio de um parágrafo:

```
A arquitetura utiliza o padrão
[Repository](../patterns/repository.md)
para separar persistência da lógica de domínio.
```

Um agente pode decidir navegar para o arquivo antes de terminar de interpretar o parágrafo.

Isso não é uma limitação exclusiva do OKF.

Para o MBCG, é recomendável estabelecer uma convenção mais estruturada para relações.

Por exemplo:

```
# Relationships

- satisfies: [REQ-001](...)
- implements: [IF-003](...)
- depends-on: [COMP-012](...)
- uses-pattern: [PAT-003](...)
```

Isso permite transformar hyperlinks em relações semanticamente tipadas.

---

# 12. Granularidade dos arquivos

Princípio adotado:

> **1 arquivo = 1 conceito semanticamente coerente.**

Evitar microfragmentação:

```text
CLASS-001-name.md
CLASS-001-method1.md
CLASS-001-method2.md
CLASS-001-dependencies.md
```

Mas também evitar arquivos gigantes:

```text
entire-system.md
```

A unidade desejável é um conceito que possa ser compreendido relativamente sozinho.

Um conceito pode conter seções:

```
# Summary

# Responsibilities

# Relationships

# Constraints

# Examples
```

Assim existe uma segunda granularidade:

```text
Concept
 |
 +-- Summary
 +-- Responsibilities
 +-- Relationships
 +-- Constraints
 +-- Examples
```

Isso permite recuperação por seção sem fragmentar excessivamente a base.

---

# 13. Estratégia de retrieval desejada

A estratégia ideal para o agente é:

```text
User request
     |
     v
Determine task
     |
     v
Read root index
     |
     v
Select concept type
     |
     v
Read metadata/description
     |
     v
Read relevant sections
     |
     v
Follow relevant relationships
     |
     v
Read related concepts
     |
     v
Build context
     |
     v
Answer / modify model / generate
```

O objetivo é:

> **ler o conhecimento certo no momento certo.**

---

# 14. Descrição e metadados como mecanismo de seleção

O frontmatter pode fornecer um resumo barato para seleção inicial.

Exemplo:

```yaml
---
type: Class
title: UserService
description: Coordinates user creation, authentication and persistence.
tags:
  - domain
  - authentication
  - service
---
```

Um índice pode expor apenas:

```text
CLASS-001
User — Domain entity representing a user.

CLASS-002
UserService — Coordinates user creation, authentication and persistence.

CLASS-003
UserRepository — Persistence abstraction for User.
```

O agente só abre o documento completo depois de selecionar o conceito.

---

# 15. UML + OKF

A proposta considerada adequada é utilizar duas representações complementares:

```text
System Model
 |
 +---------------------+
 |                     |
 v                     v
OKF / Markdown       UML
 |                     |
knowledge            formal model
 |                     |
Graph                XMI
```

### 15.1.1. Markdown/OKF

Preferencialmente para:

- requirements;
- rationale;
- ADR;
- regras;
- constraints textuais;
- exemplos;
- documentação;
- provenance;
- knowledge de agentes;
- traceability exposta ao agente.

### 15.1.2. UML/XMI

Preferencialmente para:

- classes;
- interfaces;
- atributos;
- operações;
- associações;
- composição/agregação;
- generalização;
- multiplicidade;
- dependências;
- diagramas;
- estrutura formal.

---

# 16. Ownership entre Markdown e UML

Não existe uma norma única que determine exatamente qual informação deve ser armazenada em Markdown versus UML.

A decisão deve ser uma **architectural convention** do MBCG.

Convenção proposta:

| Informação | Fonte primária |
|---|---|
| Requisito textual | OKF/MD |
| Rationale | OKF/MD |
| Critério de aceitação | OKF/MD |
| ADR | OKF/MD |
| Regra de negócio textual | OKF/MD |
| Skill/regra do agente | Intelligence KB |
| Classe | UML |
| Interface | UML |
| Atributo | UML |
| Operação | UML |
| Associação | UML |
| Generalização | UML |
| Multiplicidade | UML |
| Composição/agregação | UML |
| Diagrama | UML |
| Estrutura formal | UML |
| Traceability | modelo de relações, com representação derivada em OKF |
| Código | source code |

Regra fundamental:

> **Uma informação deve ter uma fonte de verdade claramente definida.**

Evitar, por exemplo, que atributos de uma classe sejam independentemente mantidos em Markdown e UML.

---

# 17. Normas OMG relevantes

Para traceability e requisitos, **SysML** merece ser estudado além de UML.

SysML possui relações como:

- `deriveReqt`;
- `satisfy`;
- `verify`;
- `refine`;
- `trace`;
- `allocate`.

Isso fornece uma taxonomia conceitualmente útil para rastreabilidade.

UML possui mecanismos mais genéricos de `Trace`/`Abstraction`.

Possível combinação:

```text
UML
 |
 +-- estrutura de software

SysML concepts
 |
 +-- requirements
 +-- traceability
```

Não é necessário adotar SysML inteiro; a terminologia pode ser usada como referência para uma convenção própria.

---

# 18. XMI e UML

Importante distinguir:

```text
UML != XMI
```

UML é o metamodelo/modeling language.

XMI é um padrão OMG para intercâmbio/serialização de modelos.

Conceitualmente:

```text
UML
 |
 v
UML metamodel
 |
 v
XMI serialization
```

A OMG disponibiliza os artefatos UML e XMI correspondentes.

---

# 19. XMI como interface direta do agente

Um LLM consegue ler XML/XMI.

Portanto, não é correto dizer que um agente "não entende XMI".

O problema é outro:

> XMI é otimizado para intercâmbio de modelos entre ferramentas, não para recuperação seletiva de conhecimento por agentes.

O agente pode ter que resolver:

- namespaces;
- metamodelos;
- IDs;
- referências;
- containment;
- stereotypes;
- multiplicidades;
- extensões específicas da ferramenta.

Exemplo:

```xml
<packagedElement
    xmi:type="uml:Class"
    xmi:id="_abc"
    name="User">
```

e referências como:

```xml
type="_xyz"
```

podem exigir reconstrução do modelo para serem semanticamente úteis.

Conclusão:

> XMI deve ser tratado como **formato de intercâmbio**, não como principal API cognitiva do agente.

---

# 20. Ferramenta Python relevante: PyEcore

Uma biblioteca particularmente relevante é **PyEcore**:

https://pyecore.readthedocs.io/en/latest/

Ela implementa conceitos de Ecore/EMF em Python e oferece suporte a:

- metamodelos;
- modelos;
- navegação reflexiva;
- serialização;
- desserialização;
- XMI.

Isso é mais adequado ao problema do que simplesmente fazer parsing XML com `ElementTree`.

---

# 21. Atenção ao XMI do Gaphor

Não assumir:

```text
PyEcore lê XMI
+
Gaphor exporta XMI
=
PyEcore lê perfeitamente o XMI do Gaphor
```

É necessário validar:

```text
Gaphor
 |
 +-- UML version
 +-- XMI version
 +-- namespaces
 +-- metamodel
 +-- tool-specific extensions
 |
 v
PyEcore
```

Um POC deve ser feito antes de definir o pipeline definitivo.

---

# 22. Arquitetura XMI → MD + Graph

Não fazer:

```text
XMI
 +----> MD
 +----> Graph
```

diretamente.

Preferível:

```text
                  XMI
                   |
                   v
             XMI importer
                   |
                   v
            Canonical UML Model
                   |
          +--------+--------+
          |                 |
          v                 v
    Graph builder      OKF generator
          |                 |
          v                 v
      Graph index        Markdown
```

O **Canonical UML Model** é uma peça central.

---

# 23. Exemplo de Canonical Model

Conceitualmente:

```python
UMLModel(
    classes=[
        UMLClass(
            id="_abc",
            name="User",
            attributes=[...],
            operations=[...],
        ),
        UMLClass(
            id="_def",
            name="UserService",
            attributes=[...],
            operations=[...],
        ),
    ],
    relationships=[
        UMLDependency(
            source="_def",
            target="_ghi",
        )
    ]
)
```

A partir dele:

```text
Canonical Model
 |
 +----> Graph
 |
 +----> OKF Markdown
 |
 +----> validation
 |
 +----> code generation
 |
 +----> agent API
```

---

# 24. Graph gerado a partir do modelo

Exemplo:

```text
Node:
    id = _abc
    type = uml-class
    name = User

Node:
    id = _def
    type = uml-class
    name = UserService

Edge:
    source = _def
    target = _ghi
    type = depends-on
```

Visualmente:

```text
UserService
     |
     | depends-on
     v
UserRepository
```

---

# 25. OKF gerado a partir do modelo

Exemplo:

```yaml
---
type: uml-class
id: CLASS-001
title: User
uml_id: _abc
---
```

Corpo:

```
# User

Representa o usuário autenticado do sistema.

## Relationships

- used-by: [UserService](CLASS-002-user-service.md)
```

Evitar duplicar atributos UML detalhados no Markdown se o UML for a fonte de verdade.

---

# 26. Knowledge API

A interface principal do agente deve ser semântica, não baseada em arquivos físicos.

Exemplos:

```text
get_concept(id)
get_metadata(id)
get_section(id, section)
find(type, tags, query)

get_class(id)
get_class_attributes(id)
get_class_relationships(id)

get_related(id, relation)
get_dependencies(id)
get_dependents(id)

trace(id)
get_requirements(id)
get_implementations(id)

get_skill(id)
get_generation_rule(id)
get_template(id)
```

Isso permite ao agente pedir apenas o que precisa.

---

# 27. Knowledge Compiler

Um componente conceitual importante é o **Knowledge Compiler**:

```text
                  Sources
                    |
        +-----------+-----------+
        |           |           |
       XMI         OKF        source code
        |           |
        +-----------+-----------+
                    |
                    v
             Knowledge Compiler
                    |
        +-----------+-----------+-----------+
        |           |           |           |
        v           v           v           v
    Canonical     Graph       Search      Validation
      Model       Index       Index
        |           |           |
        +-----------+-----------+
                    |
                    v
              Knowledge API
                    |
                    v
                  Agent
```

O objetivo é transformar artefatos de engenharia em representações consultáveis por agentes.

---

# 28. Relações / Traceability

Adotar, quando apropriado, uma convenção inspirada em UML/SysML.

Exemplos:

```text
satisfies
realizes
implements
depends-on
refines
derived-from
generated-from
verified-by
uses-pattern
```

Exemplo:

```text
REQ-001
   |
   | satisfies
   v
CLASS-001
   |
   | implements
   v
IF-001
   |
   | generated-to
   v
src/user_service.dart
```

Atenção:

> Relações devem ter uma fonte de verdade. Não manter duas relações independentes e potencialmente conflitantes em UML e Markdown.

---

# 29. Gaphor

A intenção é utilizar Gaphor como uma das ferramentas UML, mantendo o modelo formal em UML/XMI.

Arquitetura desejada:

```text
Gaphor
   |
   v
UML/XMI
   |
   v
UML importer
   |
   v
Canonical Model
   |
   +----> OKF
   +----> Graph
   +----> validation
   +----> agent API
```

O MBCG não deve ficar conceitualmente preso ao Gaphor.

Outras ferramentas UML poderão ser suportadas posteriormente se produzirem modelos compatíveis.

---

# 30. Intelligence KB

Para a base de inteligência, a solução pode ser mais simples:

```text
intelligence/
├── index.md
├── skills/
│   ├── index.md
│   ├── derive-requirements.md
│   ├── derive-architecture.md
│   └── generate-code.md
├── rules/
│   ├── index.md
│   ├── naming.md
│   └── architecture.md
├── templates/
│   ├── index.md
│   └── flutter-service.md
├── workflows/
│   ├── index.md
│   └── system-development.md
└── policies/
    └── validation.md
```

Para essa KB:

```text
OKF/MD
   |
   v
automatic graph
   |
   +----> official OKF visualizer
   |
   +----> retrieval
   |
   +----> agent
```

Não é necessário UML para a maior parte da Intelligence KB.

---

# 31. Princípios arquiteturais consolidados

## 31.1. P1 — Source of truth

Cada informação deve ter uma única fonte de verdade.

## 31.2. P2 — OKF como formato

OKF deve ser tratado como formato interoperável de conhecimento, não como plataforma obrigatória.

## 31.3. P3 — Markdown como conhecimento discursivo

Markdown é apropriado para requisitos, rationale, decisões, regras e documentação.

## 31.4. P4 — UML como modelo formal

UML/XMI é apropriado para estrutura formal do sistema.

## 31.5. P5 — Graph como índice

O grafo deve ser derivado dos modelos/links sempre que possível.

## 31.6. P6 — Agent API semântica

Agentes devem consumir operações semânticas, e não depender diretamente da estrutura física dos arquivos.

## 31.7. P7 — Progressive disclosure

O agente deve começar com índices/metadados e aprofundar somente quando necessário.

## 31.8. P8 — Canonical Model

XMI não deve ser necessariamente a representação interna principal. Um modelo canônico intermediário permite múltiplas projeções.

## 31.9. P9 — Interoperabilidade

Gaphor é uma ferramenta, não deve ser o centro conceitual do MBCG.

## 31.10. P10 — Traceability explícita

Relações entre requisitos, modelos, código, decisões, padrões e testes devem ser representáveis e consultáveis.

---

# 32. POC prioritário

Antes de implementar a arquitetura completa, validar:

```text
Gaphor
   |
   v
sample.xmi
   |
   v
PyEcore
   |
   v
Canonical UML Model
   |
   +----> Graph
   |
   +----> OKF Markdown
   |
   +----> JSON/Knowledge API
```

Modelo mínimo:

```text
User
UserService
UserRepository
```

Relações:

```text
UserService -> User
UserService -> UserRepository
```

Critério de sucesso:

1. importar XMI;
2. recuperar classes;
3. recuperar atributos;
4. recuperar operações;
5. recuperar associações/dependências;
6. gerar nós/arestas;
7. gerar documentos OKF;
8. preservar IDs/referências;
9. conseguir consultar o resultado via API;
10. visualizar a KB com o visualizador OKF.

---

# 33. Estado atual das decisões

### 33.1.1. Decidido / fortemente recomendado

- utilizar três KBs conceitualmente separadas;
- usar OKF/Markdown como base de conhecimento;
- usar grafo derivado;
- usar UML como modelo formal para sistemas;
- estudar SysML para requisitos/traceability;
- usar XMI como intercâmbio;
- não usar XMI como principal interface cognitiva do agente;
- investigar PyEcore;
- introduzir um Canonical Model;
- criar uma Knowledge API semântica;
- considerar o visualizador oficial OKF para a Intelligence KB;
- evitar duplicação de informações entre MD e UML.

### 33.1.2. Ainda em investigação

- formato exato do modelo canônico;
- integração específica Gaphor → XMI → PyEcore;
- ownership detalhado das relações de traceability;
- UML puro versus UML + subconjunto de conceitos SysML;
- mecanismo de busca;
- graph database versus graph index em memória/arquivo;
- vector search;
- integração com MCP;
- estratégia de chunking/section retrieval;
- formato das APIs para agentes;
- como representar geração de código e vínculos com source code.

---

# 34. Arquitetura de referência atual

```text
                         MODEL-BASED CODE GENERATOR
                                      |
          +---------------------------+---------------------------+
          |                           |                           |
          v                           v                           v
      SYSTEM KB                 GENERATOR KB              INTELLIGENCE KB
          |                           |                           |
      OKF + UML                   OKF + UML                  OKF + Graph
          |                           |                           |
         XMI                         XMI                         MD
          |                           |                           |
          +---------------------------+---------------------------+
                                      |
                              Knowledge Compiler
                                      |
                        +-------------+-------------+
                        |             |             |
                        v             v             v
                  Canonical Model   Graph        Search
                        |             |             |
                        +-------------+-------------+
                                      |
                              Knowledge API
                                      |
                                      v
                                    Agent
                                      |
                           +----------+----------+
                           |                     |
                           v                     v
                    Model modification      Code generation
                           |                     |
                           +----------+----------+
                                      |
                                      v
                                  Source Code
```

---

# 35. Principais referências técnicas

- Google Cloud Platform — Knowledge Catalog / OKF:
  https://github.com/GoogleCloudPlatform/knowledge-catalog

- OMG UML:
  https://www.omg.org/spec/UML/

- OMG XMI:
  https://www.omg.org/spec/XMI/

- OMG SysML:
  https://www.omg.org/spec/SysML/

- PyEcore:
  https://pyecore.readthedocs.io/

---

# 36. Próximas investigações sugeridas

1. Validar Gaphor → XMI.
2. Validar XMI → PyEcore.
3. Definir Canonical UML Model mínimo.
4. Definir taxonomia de relações.
5. Definir ownership MD/UML.
6. Definir representação OKF dos elementos UML.
7. Criar gerador Graph + OKF.
8. Testar visualizador oficial.
9. Definir Knowledge API.
10. Criar primeiro agente que navegue pela KB.
11. Medir contexto utilizado com:
    - arquivo inteiro;
    - seção;
    - vizinhança do grafo;
    - busca textual;
    - combinação graph + search.
12. Só depois decidir se um vector database é necessário.

---

# 37. Hipótese arquitetural principal

A hipótese que emerge das discussões é:

> **O MBCG deve tratar conhecimento, modelo formal e código como representações relacionadas, mas não equivalentes.**

```text
Knowledge
    |
    | OKF/MD
    v
Conceptual / descriptive knowledge

Formal Model
    |
    | UML/XMI
    v
Structural / formal model

Graph
    |
    | derived
    v
Relationships / traversal / retrieval

Code
    |
    | generated
    v
Executable implementation
```

O agente deve operar principalmente sobre uma **Knowledge API semântica**, que combina essas representações conforme a tarefa, em vez de receber indiscriminadamente todos os arquivos ou todo o XMI.

Essa arquitetura mantém:

- interoperabilidade;
- versionamento;
- explicabilidade;
- rastreabilidade;
- possibilidade de múltiplos agentes;
- possibilidade de múltiplos LLMs;
- independência relativa de ferramentas;
- evolução futura do mecanismo de retrieval.

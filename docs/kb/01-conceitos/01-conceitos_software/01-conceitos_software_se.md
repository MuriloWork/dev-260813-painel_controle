**Systems Engineering**

# 1. Systems Engineering Handbook
## 1.1. Summary INCOSE: Systems Life Cycle 
- concepts
- models
- processes
- quality characteristics
- analyses and methods

### 1.1.1. Systems Life Cycle processes
![[260617_conceitos_info_se_processes.jpg]]
[[2023 incose-systems-engineering-handbook.pdf#page=66]]

### 1.1.2. [[#2. Systems Engineering - Technical Processes|technical processes]]  
### 1.1.3. analyses and methods
([[2023 incose-systems-engineering-handbook.pdf#page=217|source-pdf]])  

Systems Modeling and Simulation has been defined (NAFEMS and INCOSE, 2019) as the use of interdisciplinary functional, architectural, and behavioral models (with physical, mathematical, and logical representations) for all life stages.

Classifying and Characterizing Models There are many different kinds of models to address different system aspects and different kinds of systems. Generally, a specific type of model focuses on some subset of the system char- acteristics, such as timing, process behavior, measures of performance, interfaces, and connections. It is useful to classify the types of models to assist in selecting the appropriate one. Figure 3.10 shows one possible (non-exhaustive) taxonomy as an example. 

- **Physical model**—A physical model represents (aspects of) a system with real parts. Examples are a physical mockup, a scaled model airplane, a wind tunnel model, and a 3D-printed scale model from a digital model specification (the latter could be considered a physical view of a digital model). If simulation is performed with a physical model, it is typically called a test. 
- **Digital model**—Digital models can have many different expressions to represent (e.g., a system, entity, phenomenon, or process), each of which may vary in degrees of formalism. Therefore, the next level of classification is between informal and formal models. 
- **Formal models**—A formal model is expressed in a machine-readable language with explicitly defined semantics. The language may be textual and/or graphical, but with only one way of interpretation. Formal models can be further classified as logical, quantitative (i.e., mathematical), geometric, or surrogate models. A logical model, also referred to as a descriptive model or a conceptual model, represents logical relationships about the system such as whole–part relationships, interconnection relationships between elements, or precedence relationships between activities, to name  a few. Logical models are often depicted using network graphs (with nodes and edges) or tables. A quantitative model represents quantitative relationships (e.g., mathematical equations) about the system or its elements that yield numerical results. A geometric model represents the geometry, geometric shapes, and spatial relationships of the system or any of its (physical) elements. A surrogate model is a reduced model that is derived from a higher fidelity, more detailed model using a data-driven, typically automated, transformation. The goal (and challenge) is to create a surrogate that adequately represents essential aspects of the modeled system while requiring substantially less compu- tational resources. Surrogate models then enable running large numbers of (parameterized) experiments in order to facilitate design exploration, optimization, or validation. 
- **Informal models**—An informal model is expressed using some convention understood by humans, where the convention is defined casually without formal semantics. The model does not need to be machine-readable. An informal model can be created by hand or with simple tools (e.g., word-processing, spreadsheet, diagramming, mind- mapping). While such informal representations can be useful, they often lack the rigor to be considered a type of model that is truly usable for MA&S for non-trivial systems. Informal model presentations may be used as views that are generated from or ingested into formal models in order to communicate with people not familiar with the notation. 
- **Mixed models**—A mixed model is a combination of physical and digital models. 

In addition to a selected type of model, any model can be further characterized for its intended purpose through the following three characteristics: 
- The model breadth reflects what aspects of the SoI—and possibly its (actual or intended) environment(s)—are represented, and to what extent. 
- The model granularity characterizes the amount of visible detail captured in the model, in terms of the repre- sented depth of system decomposition as well as the represented level of details of individual system elements. 
- The model fidelity indicates how accurately the model represents the real-world system. Where applicable, this includes the computational precision to be achieved and the discretization scheme to be used. The type of model and the model characteristics must be balanced against project needs and resources. Another important aspect of modeling is to explicitly state the assumptions and limitations that almost inevitably apply to any model.

**Model Interoperability** Since the development of complex systems requires collaboration between all project mem- bers and disciplines, it is very important to have the ability to exchange and share models as well as analysis and sim- ulation results across disciplines, projects, organizations, and life cycle stages. This is also referred to as digital interchange. In most projects and (extended) enterprises it is not possible to standardize on a single set of tools. The alternative is to develop and utilize open, tool-independent standards that enable information exchange and sharing. There is an increasing awareness and consensus between user communities and tool developers on the merit of inter- national royalty-free standards. Standards can be categorized in terms of how MA&S is supported. The main cate- gories are: 
- Standardized data exchange file, 
- Application programming interface (API), 
- Modeling language, and 
- Process. 
Data exchange files are used for on-demand transfer of complete models or results. APIs usually support more fine- grained data access and sharing, often implementing a service-oriented software architecture. Modeling languages can be graphical, textual or both, and are used to standardize the way of expressing a model. Process standards specify (aspects of) the MA&S processes. Most modeling languages do not prescribe a particular methodology to be followed. This flexibility is a feature of a general-purpose modeling language that enables economies of scale for implementations which are in the interest of the SE community as a whole. However, in order to align how SE practitioners in a team, organization, or application domain approach MA&S, a methodology is needed. A methodology provides guidance and examples on how to organize MA&S over a typical system life cycle, how to structure model artifacts, as well as what stages and milestones to respect. A methodology can also capture proven modeling patterns and checklists, as well as good practices in general. For further details se Section 4.2.1 or consult the OMG MBSE Wiki (2023).



## 1.2. Summary SEBok Systems Engineering Body of Knowledge 
https://sebokwiki.org/wiki/Guide_to_the_Systems_Engineering_Body_of_Knowledge_(SEBoK)

## 1.3. Normativos Systems Engineering 
[ISO/IEC/IEEE 15288: A Guide to the Systems Lifecycle Processes](https://www.jamasoftware.com/blog/the-complete-guide-to-iso-iec-ieee-152882015-systems-and-software-engineering/)
[ISO-IEC-IEEE-24748-1-2018 Systems Life Cycle management](https://1drv.ms/b/c/68092d0c5dd50638/IQCUyBeKHHgxQq2tl0Q__uUZATnSSd2icwb8mO53gRPcpG0)
[ISO-IEC-IEEE-29148 Requirements Specification Document](https://1drv.ms/b/c/68092d0c5dd50638/IQBoBn4wD1DNTJw9O8JeV1DjAfgGm_SVFEpNyEAK54hKZ1Y)
[Capacities of the ISO/IEC/IEEE 42020 Architecture Elaboration of Software and Systems](https://dl.acm.org/doi/fullHtml/10.1145/3592813.3592932)
[Software, systems and enterprise — Architecture processes](https://1drv.ms/b/c/68092d0c5dd50638/IQAZVOpGx_rMTqODMSklQsxaAfgw_be0gzyNj_PiO8V2oSI)


# 2. Systems Engineering - Technical Processes
## 2.1. diagrama resumo
![[01-conceitos_software_se_technical_processes.jpg]]
|[[2023 incose-systems-engineering-handbook.pdf#page=127|source-pdf]]|

## 2.2. Business or Mission Analysis

- domain
- ConOps
- stakeholders
- definição do problema ou oportunidade

**Concept of operations** (ConOps) — Describes the way the organization will operate to achieve its missions, goals, and objectives. The ConOps captures how the system will potentially impact the acquiring and other organizations. “The ConOps describes the organization’s assumptions or intent in regard to an overall operation or series of operations of the business with using the system to be developed, existing systems and possible future systems. The ConOps serves as a basis for the organization to direct the overall characteristics of the future business and systems, for the project to understand its background, and for [its] users to implement the stakeholder requirements elicitation” (ISO/IEC/IEEE 29148, 2018) Ideally, the enterprise level ConOps should be an input to the Business or Mission Analysis process, but if it does not exist, it may need to be jointly developed and maintained. The ConOps also describes the higher-level system in which the SoI must operate. |[[2023 incose-systems-engineering-handbook.pdf#page=128|source-pdf]]|  

## 2.3. Business (Stakeholder) Requirements

- cenarios operacionais (use cases)
- limitações: fronteiras, interfaces, riscos, restrições
- business needs
- business requirements

**business requirements** —  descrever de forma a indicar caminho para system requirements (stack, arquitetura)  |[[2023 incose-systems-engineering-handbook.pdf#page=132|souce-pdf]]|

## 2.4. System Requirements Definition

From [[2023 incose-systems-engineering-handbook.pdf#page=137|INCOSE SE Handbook]]  
- Define system requirements.
	- Define the functional boundary of the system in terms of the behavior and properties to be provided.
	- Identify the life cycle concepts and stakeholder requirements from which the system requirements will be transformed and then define each function and associated performance.
	- ==Define each expected system function==, including the associated performance. Include both primary functions and enabling functions.
	- Define necessary constraints. These include higher-level requirements allocated to the SoI, operational condi-tions, and interactions with external systems. Define interactions with users, operators, maintainers, and disposers.
	- Identify system requirements that relate to risks, criticality of the system, critical quality characteristics, and compliance with standards and regulations.
	- Define verification success criteria for each system requirement, the verification strategy, verification method, and responsible organization for providing proof the system requirements have been met (see Section 2.3.5.9).
	- Capture the system requirements and their attributes.
- Analyze system requirements.
	- Analyze the system requirements for characteristics of individual requirements and of the set of requirements (can be the set of requirements for the current increment, build, or sprint). Analyze the set of requirements to ensure they are correct, complete, consistent, comprehensible, appropriate to level, and feasible (see the elab-oration below and the INCOSE GtWR [2023] for more details).
	- Enable technical achievement monitoring through the definition of critical performance measures.
	- Review the analyzed requirements with the applicable stakeholders.
	- Perform issue resolution for the system requirements. Negotiate changes, amendments, and modifications to resolve inconsistencies, conflicts, and unrealizable or impractical requirements.
<br>

Mais referencias:
- [article: Digital requirements engineering with an INCOSE-derived SysML meta-model](https://arxiv.org/html/2410.21288v2)

### 2.4.1. From [INCOSE Requirements Guide](file:///C:/Users/muril/OneDrive/01%20mycloud/01-sistMu/20-pkm/10_info/20%20automation/01.01%20systems_engineering/2022%20INCOSE_Guide_to_Writing_Requirements.pdf)
#### 2.4.1.1. [Node] Conceitos Fundamentais de Engenharia de Requisitos
Este nó estabelece a base conceitual sobre a qual as regras e características da especificação de requisitos são construídas [4, 6].

##### 2.4.1.1.1. [Node] Needs (Necessidades)
*   **Definição:** Declarações textuais formais das expectativas dos stakeholders para uma Entidade de Interesse (SOI - System of Interest), expressas em linguagem natural estruturada, sob a perspectiva do que os stakeholders precisam que o sistema faça, no nível adequado de abstração [11].
*   **Origem:** É o resultado de uma transformação formal de um ou mais conceitos de ciclo de vida (como expectativas de stakeholders, objetivos de negócio, drivers e restrições) em expectativas acordadas [11, 12].
*   **Relação de Grafo:** Conecta-se diretamente aos *Concepts* (Conceitos) como entrada, e é transformado em *Design Input Requirements* [13, 18].

##### 2.4.1.1.2. [Node] Requirements (Requisitos)
*   **Definição:** Declarações formais que descrevem o que o sistema deve fazer (insumo de projeto / *design input requirements*), sem impor soluções de implementação (saída de projeto / *design output specifications*) [7, 8, 44].
*   **Propósito:** Fornecer uma especificação clara que direcione a arquitetura e o design do sistema, servindo como base para a verificação do sistema [7, 10, 18].
*   **Linguagem:** Escritos de forma estruturada e imperativa utilizando tradicionalmente o termo obrigatório "**shall**" (deve) em português ou inglês [10, 36].

##### 2.4.1.1.3. [Node] Attributes (Atributos)
*   **Definição:** Informações adicionais associadas a um enunciado de necessidade ou requisito usada para auxiliar na sua definição e gerenciamento ao longo do ciclo de vida [12].
*   **Importância:** Permitem o gerenciamento eficaz do ciclo de vida e ajudam a identificar erros precocemente, evitando retrabalhos caros [12].
*   **Exemplos de Atributos:** Racional (A1), Rastreabilidade para Fonte (A3), Prioridade (A34), Método de Verificação, Critérios de Sucesso, etc [12, 34, 40].
*   **Expressões completas:** Uma "expressão de necessidade" ou "expressão de requisito" é a composição do enunciado textual correspondente somado ao seu conjunto de atributos associados [12].

##### 2.4.1.1.4. [Node] Verification vs Validation (Verificação vs Validação)
*   **Verificação de Requisitos ("Did we write the requirements correctly?" / "Are the requirements written correctly?"):** Avalia se os enunciados individuais e conjuntos de requisitos estão em conformidade com as regras e características de qualidade do próprio guia [15, 16, 18].
*   **Verificação do Sistema ("Did we build it correctly?" / "Did we design it right?"):** Confirma que o design ou o sistema físico atende aos requisitos de entrada estabelecidos [18]. Realizada por inspeção, análise, demonstração ou teste [25].
*   **Validação de Necessidades ("Are we building the right thing?"):** Confirma se as necessidades expressam com precisão as intenções dos conceitos de ciclo de vida de origem [17, 18].
*   **Validação de Requisitos:** Confirma se os requisitos comunicam claramente a intenção das necessidades ou requisitos de nível superior correspondentes [17].
*   **Validação do Sistema ("Did we build the right thing?"):** Confirma se o sistema realizado atende às necessidades dos stakeholders no seu contexto operacional [10, 18].

---

#### 2.4.1.2. [Node] Qualidade de Needs e Requisitos (Characteristics)
Enunciados e conjuntos devem possuir características fundamentais para serem considerados bem-formados, mitigando riscos de falhas no projeto [15].

##### 2.4.1.2.1. [Node] Características de Enunciados Individuais
*   **C1 - Necessário (Necessary):** Cada enunciado deve ser indispensável. Um requisito não é necessário se a intenção puder ser atendida por outro requisito, se não tiver rastreabilidade para uma fonte/necessidade, ou se não houver um racional válido para sua existência. O uso do racional (A1) apoia essa característica [34, 40].
*   **C3 - Desambiguado (Unambiguous):** Deve possuir apenas uma interpretação possível por todos os stakeholders envolvidos. A ambiguidade pode levar a desvios de cronograma, estouros de orçamento ou falhas na validação do sistema [22].
*   **C4 - Completo (Complete):** O enunciado individual deve ser compreensível por si só, contendo todas as informações de comportamento, condições e critérios de sucesso necessários, sem depender de outros requisitos ou títulos para sua explicação [24, 25, 42].
*   **C5 - Singular (Singular):** Deve declarar apenas uma única necessidade ou requisito aplicável a um único comportamento, característica ou condição do sistema [39].
*   **C7 - Verificável (Verifiable):** Um requisito é verificável se for possível determinar de forma precisa, com tolerâncias, se o sistema realizado obedece ao requisito (sucesso ou falha) usando um dos quatro métodos padrão (inspeção, análise, demonstração ou teste) [25].
*   **C8 - Correto (Correct):** Não deve conter erros, omissões ou informações falsas em relação ao conceito original do ciclo de vida [17].

##### 2.4.1.2.2. [Node] Características de Conjuntos (Sets)
*   **C10 - Completo (Complete):** O conjunto de necessidades ou requisitos deve ser autossuficiente para descrever todas as capacidades, restrições, funções e fatores de qualidade exigidos para o sistema no nível correspondente de abstração [31].
*   **C11 - Consistente (Consistent):** Não deve haver conflitos, sobreposições ou contradições entre os requisitos individuais do conjunto, garantindo termos, terminologias, unidades de medida e glossários homogêneos [32].
*   **C12 - Viável (Feasible):** O conjunto deve ser realizável dentro das restrições de custo, prazo, tecnologia e risco aceitáveis do projeto [33].

---

#### 2.4.1.3. [Node] Regras de Escrita (Rules)
As regras fornecem as diretrizes práticas para atingir as características de qualidade especificadas [6, 35].

##### 2.4.1.3.1. [Node] R1 - Estrutura da Sentença
*   **Regra:** Expandir a forma básica `<sujeito> <verbo> <objeto>` para a estrutura formal padrão:
    *   *Estrutura:* `O <sistema> deve <verbo de ação> <objeto> <resultado mensurável> <condições de contorno/qualificação>` [36].
*   **Significado de "deve" (shall):** Utilizado para indicar que o enunciado é formal, obrigatório e contratualmente vinculante [10, 36].

##### 2.4.1.3.2. [Node] R18 - Sentença Única (Singularidade)
*   **Regra:** Escrever cada requisito em uma única frase, evitando múltiplos parágrafos ou agrupamentos de ideias independentes [26, 29].
*   **Justificativa:** Facilita a alocação, rastreamento e verificação individualizada de cada requisito [39].

##### 2.4.1.3.3. [Node] R19 - Evitar Combinadores
*   **Regra:** Evitar palavras de ligação como "e", "ou", "então", "a menos que", "mas", "bem como" no corpo principal da ação [39].
*   **Justificativa:** A presença dessas palavras geralmente sinaliza a oportunidade de decompor em múltiplos requisitos singulares [39].
*   **Exceção:** Uso de operadores lógicos (AND, OR, NOT) em letras maiúsculas para qualificar condições complexas [39].

##### 2.4.1.3.4. [Node] R20 - Evitar Expressões de Propósito
*   **Regra:** Evitar frases que justificam o requisito no próprio texto, como "a fim de", "de modo que", "para permitir que" [40].
*   **Diretriz:** A justificativa e o propósito devem ser delegados para o atributo de **Racional (A1)**, mantendo o enunciado do requisito conciso e focado estritamente na obrigação do sistema [40].

##### 2.4.1.3.5. [Node] R25 - Evitar Dependência de Cabeçalhos
*   **Regra:** O requisito deve ser compreensível independentemente do cabeçalho da seção onde está localizado no documento [42].
*   **Diretriz:** Não use pronomes referindo-se a cabeçalhos. O requisito deve manter sua integridade quando gerenciado em uma ferramenta eletrônica de requisitos baseada em banco de dados (RMT) [24, 42].

##### 2.4.1.3.6. [Node] R30 - Expressar Apenas Uma Vez
*   **Regra:** Cada necessidade ou requisito deve ser expresso uma única vez no conjunto [29, 43].
*   **Justificativa:** Evita inconsistências futuras durante alterações e simplifica as atividades de verificação e contagem [32, 43].

---

#### 2.4.1.4. [Node] Padrões de Requisitos (Patterns)
*   **Definição:** Estruturas gramaticais pré-definidas (ou templates de nível de sentença) que auxiliam os autores a formular requisitos de forma completa e consistente [5, 6, 24].
*   **Blocos de Construção:** Geralmente compostos por condições, gatilhos, entidades executoras, verbos imperativos e resultados mensuráveis [3, 36].
*   **Exemplos de Padrões:** Padrões orientados a eventos, estados, restrições ou capacidades funcionais (ex: EARS - Easy Approach to Requirements Syntax) [52, 53].


# 3. [[01-conceitos_software_se_sdlc|SDLC - Software Development Life Cicle]]  
# 4. qualidade de software 

## 4.1. ISO 25010

[Understanding ISO/IEC 25010: A Comprehensive Framework for Software Quality Evaluation](https://medium.com/@oczz/understanding-iso-iec-25010-a-comprehensive-framework-for-software-quality-evaluation-ae3cc5250057)
[sonar](https://www.sonarsource.com/resources/library/iso-iec-25010-explained/)

- Functional Suitability
	- functional **completeness**: covering all required functionality
	- Functional **correctness**: producing accurate and expected results
	- Functional **appropriateness**: enabling users to accomplish their objectives efficiently
- Maintainability
	- **Modularity**: separating functionality into well-defined components
	- **Testability**: verifying that changes behave as expected
	- **Reusability**: leveraging existing assets across systems and projects
	- **Analyzability**: efficiently diagnosing defects, vulnerabilities, and performance issues
	- Modifiability: implementing changes without introducing unintended side effects
- Interaction capability
	- **Appropriateness recognizability** - Degree to which users can recognize whether a product or system is appropriate for their needs.
	- **Learnability** - Degree to which the functions of a product or system can be learnt to be used by specified users within a specified amount of time.
	- **Operability** - Degree to which a product or system has attributes that make it easy to operate and control.
	- **User error protection**. Degree to which a system prevents users against operation errors.
	- **User engagement** - Degree to which a user interface presents functions and information in an inviting and motivating manner encouraging continued interaction.
	- **Inclusivity** - Degree to which a product or system can be used by people of various backgrounds (such as people of various ages, abilities, cultures, ethnicities, languages, genders, economic situations, etc.).
	- **User assistance** - Degree to which a product can be used by people with the widest range of characteristics and capabilities to achieve specified goals in a specified context of use.
	- **Self-descriptiveness** - Degree to wich a product presents appropriate information, where needed by the user, to make its capabilities and use immediately obvious to the user without excessive interactions with a product or other resources (such as user documentation, help desks or other users).
- Performance Efficiency
	- Sub-characteristics: response time behavior, resource utilization, capacity.
- Compatibility
	- Sub-characteristics: co-existence, interoperability.
- Reliability
	- Sub-characteristics: ~~maturity~~ Faultlessness, availability, fault tolerance, recoverability.
- Security
	- Sub-characteristics: confidentiality, integrity, non-repudiation, accountability, authenticity.
- Portability
	- Sub-characteristics: adaptability, installability, replaceability.

## 4.2. Automated Source Code Quality Measures (ASCQM) - ISO 5055

[omg-ASCQM](https://www.omg.org/spec/ASCQM/1.0/PDF)


A ISO/IEC 5055 complementa a ISO/IEC 25010 focando estritamente na medição automatizada do código-fonte. Enquanto a ISO 25010 define o modelo conceitual de qualidade do produto, a ISO 5055 fornece as regras de engenharia para calcular essa qualidade na prática. ISO/IEC 25000 series of standards that govern software product quality do not provide measures at the source code level.
### 4.2.1. Diferenças e Relação Prática

* Escopo: A ISO 25010 descreve o que avaliar (conceitos amplos), enquanto a ISO 5055 diz como medir via código (regras estritas).
* Abordagem: A ISO 25010 inclui a percepção do usuário e testes de caixa-preta. A ISO 5055 faz análise de caixa-branca (código-fonte).
* Métricas: A ISO 5055 foca em contar violações arquiteturais e estruturais graves no sistema.

### 4.2.2. Alinhamento dos Pilares
A ISO 5055 adota exatamente quatro das características de qualidade definidas na ISO 25010:

* Segurança: Foco em vulnerabilidades de código (ex: validação de dados) que afetam a segurança da ISO 25010.
* Confiabilidade: Mede a estabilidade do código para atingir a maturidade e tolerância a falhas da ISO 25010.
* Eficiência de Desempenho: Avalia o uso de recursos no nível do código para garantir o tempo de resposta da ISO 25010.
* Manutenibilidade: Analisa o acoplamento e complexidade do código para viabilizar a modificabilidade da ISO 25010.

### 4.2.3. SPMS - Structured Patterns Metamodel Standard
[omg-spms](https://www.omg.org/spec/SPMS/1.2/)

### 4.2.4. KDM - Knowledge Discovery Metamodel .
The code-based elements in SPMS patterns

[omg-kdm](https://www.omg.org/spec/KDM/1.4/)


# 5. OOP - Object Oriented Programming 

Superficially the term object-oriented (OO) means that we organize software as a collection of discrete objects that incorporate both data structure and behavior. This contrasts with pre-vious programming approaches in which data structure and behavior are only loosely con-nected. There is some dispute about exactly what characteristics are required by an OO approach, but they generally include.


## 5.1. four aspects: [identity, classification, inheritance, and polymorphism

## 5.2. OO Methodology

**System conception**. Software development begins with business analysts or users con-ceiving an application and formulating tentative requirements.

**Analysis**. The analyst scrutinizes and rigorously restates the requirements from system conception by constructing models. The analyst must work with the requestor to under-stand the problem, because problem statements are rarely complete or correct. The anal-ysis model is a concise, precise abstraction of what the desired system must do, not how it will be done. The analysis model should not contain implementation decisions. For example, a Window class in a workstation windowing system would be described in terms of its visible attributes and operations.
The analysis model has two parts: the **domain model**, a description of the real-world objects reflected within the system; and the **application model**, a description of the parts of the application system itself that are visible to the user. For example, domain objects for a stockbroker application might include stock, bond, trade, and commission. Appli-cation objects might control the execution of trades and present the results. Application experts who are not programmers can understand and criticize a good model.

**System design**. The development team devise a high-level strategy—the system archi-tecture—for solving the application problem. They also establish policies that will serve as a default for the subsequent, more detailed portions of design. The system designer must decide what performance characteristics to optimize, choose a strategy of attacking the problem, and make tentative resource allocations. For example, the system designer might decide that changes to the workstation screen must be fast and smooth, even when windows are moved or erased, and choose an appropriate communications protocol and memory buffering strategy.

**Class design**. The class designer adds details to the analysis model in accordance with the system design strategy. The class designer elaborates both domain and application objects using the same OO concepts and notation, although they exist on different conceptual planes. The focus of class design is the data structures and algorithms needed to implement each class. For example, the class designer now determines data structures and algorithms for each of the operations of the Window class.

**Implementation**. Implementers translate the classes and relationships developed during class design into a particular programming language, database, or hardware. Programming should be straightforward, because all of the hard decisions should have already been made. During implementation, it is important to follow good software engineering practice so that traceability to the design is apparent and so that the system remains flexible and extensible. For example, implementers would code the Window class in a programming language, using calls to the underlying graphics system on the workstation.

## 5.3. Three Models 

We use three kinds of models to describe a system from different viewpoints: the class model for the objects in the system and their relationships; the state model for the life history of objects; and the interaction model for the interactions among objects. Each model applies during all stages of development and acquires detail as development progresses. A complete description of a system requires models from all three viewpoints.

The **class model** describes the static structure of the objects in a system, their relationships to other objects, their attributes, and their operations. The class model provides context for the state and interaction models. Changes and interactions are meaningless unless there is something to be changed or with which to interact. Objects are the units into which we divide the world, the molecules of our models. The class model contains **class diagrams**. A class diagram is a graph whose nodes are classes and whose arcs are relationships among classes.

The **state model** describes the aspects of an object that change over time. The state model specifies and implements control with state diagrams. A state diagram is a graph whose nodes are states and whose arcs are transitions between states caused by events.

The **interaction model** describes how the objects in a system cooperate to achieve broader results. The interaction model starts with use cases that are then elaborated with se-quence and activity diagrams. A use case focuses on the functionality of a system—that is, what a system does for users. A sequence diagram shows the objects that interact and the time sequence of their interactions. An activity diagram elaborates important processing steps.

The three models are separate parts of the description of a complete system but are cross-linked. The class model is most fundamental, because it is necessary to describe what is changing or transforming before describing when or how it changes.

# 6. [[01-conceitos_software_se_mbse|MBSE - Model Based Systems Engineering]]
# 7. Knowledge Graph 
caso de uso: [[260819-modelo_repositorios#4.1. KG - Knowledge Graph|KMS - modelo repositorios]]

- Conceitos basicos para estudo
	- [SYSTEM ENGINEERING MODELS MEET KNOWLEDGE GRAPHS](https://nebula.esa.int/sites/default/files/neb_tec_study/1436/public/C4000133311ExS.pdf)
	- [Knowledge Graph Generation Framework for Systems Engineering](https://semantic-web-journal.net/content/kgg4se-knowledge-graph-generation-framework-systems-engineering)
	- [Applications of Graph Theory for Reuse of MBSE Design Data](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://sercuarc.org/wp-content/uploads/2025/06/1670526932.ARR-22_SDSF_5_Herrington_Applications-of-Graph-Theory-for-Reuse-of-Model-Based-Systems-Engineering-Design-Data.pdf&ved=2ahUKEwjv7tqa0ZuWAxXABLkGHYZXCmgQFnoECG4QAQ&usg=AOvVaw2Sza6FrYECqT2muktYVMwz)
	- [MBSE using ontology-based knowledge graphs](https://arxiv.org/pdf/2512.09596)
	- [Identification of Missing Knowledge in MBSE Using Graph-Based Machine Learning](https://incose.onlinelibrary.wiley.com/doi/epdf/10.1002/sys.70013)
	- [Knowledge graph based System model configuration design](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://iopscience.iop.org/article/10.1088/1742-6596/2029/1/012108/pdf&ved=2ahUKEwip9ZXv4puWAxXcBbkGHRi0NdY4ChAWegQINBAB&usg=AOvVaw3uyukv0nWjoW8VvAPG0tOl)
- Ontologia e KG
	- [Ontologia de Modelo Gráfico](https://graph.build/resources/ontology)
	- [Understanding Ontologies and Knowledge Graphs](https://www.falkordb.com/blog/understanding-ontologies-knowledge-graph-schemas/)
	- [Construction of Knowledge Graphs: State and Challenges](https://ar5iv.labs.arxiv.org/html/2302.11509)
	- [Multiple Roles of Ontologies in Explainable AI](https://ar5iv.labs.arxiv.org/html/2311.04778)
	- [Model management to support systems engineering workflows using ontology-based knowledge graphs](https://arxiv.org/html/2512.09596v1)
- Listas de recursos
	- [From Individual Intelligence to System Intelligence](https://github.com/DEEP-JLU/Awesome-Graph-Engineering) 

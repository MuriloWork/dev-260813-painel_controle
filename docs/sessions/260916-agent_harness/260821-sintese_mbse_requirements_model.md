# 1. request
quero sintese das fontes, se possivel como arquivo markdown para eu baixar
- requisitos
	- maximo 8 paginas
	- formatação markdown
		- heading h1 = [INCOSE Requirements Guide, SysML]
		- demais headings, considerar como nós de um knowledge graph (mindmap)
		- usar
			- para diagramas usar mermaid 
		- usar moderadamente 
			- diagramas 
		- não usar
			- horizontal ruler `---` 
			- formatação adicional nos headings 

# 2. sintese INCOSE + SysML

## 2.1. INCOSE Requirements Guide

### 2.1.1. [Node] Conceitos Fundamentais de Engenharia de Requisitos
Este nó estabelece a base conceitual sobre a qual as regras e características da especificação de requisitos são construídas [4, 6].

#### 2.1.1.1. [Node] Needs (Necessidades)
*   **Definição:** Declarações textuais formais das expectativas dos stakeholders para uma Entidade de Interesse (SOI - System of Interest), expressas em linguagem natural estruturada, sob a perspectiva do que os stakeholders precisam que o sistema faça, no nível adequado de abstração [11].
*   **Origem:** É o resultado de uma transformação formal de um ou mais conceitos de ciclo de vida (como expectativas de stakeholders, objetivos de negócio, drivers e restrições) em expectativas acordadas [11, 12].
*   **Relação de Grafo:** Conecta-se diretamente aos *Concepts* (Conceitos) como entrada, e é transformado em *Design Input Requirements* [13, 18].

#### 2.1.1.2. [Node] Requirements (Requisitos)
*   **Definição:** Declarações formais que descrevem o que o sistema deve fazer (insumo de projeto / *design input requirements*), sem impor soluções de implementação (saída de projeto / *design output specifications*) [7, 8, 44].
*   **Propósito:** Fornecer uma especificação clara que direcione a arquitetura e o design do sistema, servindo como base para a verificação do sistema [7, 10, 18].
*   **Linguagem:** Escritos de forma estruturada e imperativa utilizando tradicionalmente o termo obrigatório "**shall**" (deve) em português ou inglês [10, 36].

#### 2.1.1.3. [Node] Attributes (Atributos)
*   **Definição:** Informações adicionais associadas a um enunciado de necessidade ou requisito usada para auxiliar na sua definição e gerenciamento ao longo do ciclo de vida [12].
*   **Importância:** Permitem o gerenciamento eficaz do ciclo de vida e ajudam a identificar erros precocemente, evitando retrabalhos caros [12].
*   **Exemplos de Atributos:** Racional (A1), Rastreabilidade para Fonte (A3), Prioridade (A34), Método de Verificação, Critérios de Sucesso, etc [12, 34, 40].
*   **Expressões completas:** Uma "expressão de necessidade" ou "expressão de requisito" é a composição do enunciado textual correspondente somado ao seu conjunto de atributos associados [12].

#### 2.1.1.4. [Node] Verification vs Validation (Verificação vs Validação)
*   **Verificação de Requisitos ("Did we write the requirements correctly?" / "Are the requirements written correctly?"):** Avalia se os enunciados individuais e conjuntos de requisitos estão em conformidade com as regras e características de qualidade do próprio guia [15, 16, 18].
*   **Verificação do Sistema ("Did we build it correctly?" / "Did we design it right?"):** Confirma que o design ou o sistema físico atende aos requisitos de entrada estabelecidos [18]. Realizada por inspeção, análise, demonstração ou teste [25].
*   **Validação de Necessidades ("Are we building the right thing?"):** Confirma se as necessidades expressam com precisão as intenções dos conceitos de ciclo de vida de origem [17, 18].
*   **Validação de Requisitos:** Confirma se os requisitos comunicam claramente a intenção das necessidades ou requisitos de nível superior correspondentes [17].
*   **Validação do Sistema ("Did we build the right thing?"):** Confirma se o sistema realizado atende às necessidades dos stakeholders no seu contexto operacional [10, 18].

---

### 2.1.2. [Node] Qualidade de Needs e Requisitos (Characteristics)
Enunciados e conjuntos devem possuir características fundamentais para serem considerados bem-formados, mitigando riscos de falhas no projeto [15].

#### 2.1.2.1. [Node] Características de Enunciados Individuais
*   **C1 - Necessário (Necessary):** Cada enunciado deve ser indispensável. Um requisito não é necessário se a intenção puder ser atendida por outro requisito, se não tiver rastreabilidade para uma fonte/necessidade, ou se não houver um racional válido para sua existência. O uso do racional (A1) apoia essa característica [34, 40].
*   **C3 - Desambiguado (Unambiguous):** Deve possuir apenas uma interpretação possível por todos os stakeholders envolvidos. A ambiguidade pode levar a desvios de cronograma, estouros de orçamento ou falhas na validação do sistema [22].
*   **C4 - Completo (Complete):** O enunciado individual deve ser compreensível por si só, contendo todas as informações de comportamento, condições e critérios de sucesso necessários, sem depender de outros requisitos ou títulos para sua explicação [24, 25, 42].
*   **C5 - Singular (Singular):** Deve declarar apenas uma única necessidade ou requisito aplicável a um único comportamento, característica ou condição do sistema [39].
*   **C7 - Verificável (Verifiable):** Um requisito é verificável se for possível determinar de forma precisa, com tolerâncias, se o sistema realizado obedece ao requisito (sucesso ou falha) usando um dos quatro métodos padrão (inspeção, análise, demonstração ou teste) [25].
*   **C8 - Correto (Correct):** Não deve conter erros, omissões ou informações falsas em relação ao conceito original do ciclo de vida [17].

#### 2.1.2.2. [Node] Características de Conjuntos (Sets)
*   **C10 - Completo (Complete):** O conjunto de necessidades ou requisitos deve ser autossuficiente para descrever todas as capacidades, restrições, funções e fatores de qualidade exigidos para o sistema no nível correspondente de abstração [31].
*   **C11 - Consistente (Consistent):** Não deve haver conflitos, sobreposições ou contradições entre os requisitos individuais do conjunto, garantindo termos, terminologias, unidades de medida e glossários homogêneos [32].
*   **C12 - Viável (Feasible):** O conjunto deve ser realizável dentro das restrições de custo, prazo, tecnologia e risco aceitáveis do projeto [33].

---

### 2.1.3. [Node] Regras de Escrita (Rules)
As regras fornecem as diretrizes práticas para atingir as características de qualidade especificadas [6, 35].

#### 2.1.3.1. [Node] R1 - Estrutura da Sentença
*   **Regra:** Expandir a forma básica `<sujeito> <verbo> <objeto>` para a estrutura formal padrão:
    *   *Estrutura:* `O <sistema> deve <verbo de ação> <objeto> <resultado mensurável> <condições de contorno/qualificação>` [36].
*   **Significado de "deve" (shall):** Utilizado para indicar que o enunciado é formal, obrigatório e contratualmente vinculante [10, 36].

#### 2.1.3.2. [Node] R18 - Sentença Única (Singularidade)
*   **Regra:** Escrever cada requisito em uma única frase, evitando múltiplos parágrafos ou agrupamentos de ideias independentes [26, 29].
*   **Justificativa:** Facilita a alocação, rastreamento e verificação individualizada de cada requisito [39].

#### 2.1.3.3. [Node] R19 - Evitar Combinadores
*   **Regra:** Evitar palavras de ligação como "e", "ou", "então", "a menos que", "mas", "bem como" no corpo principal da ação [39].
*   **Justificativa:** A presença dessas palavras geralmente sinaliza a oportunidade de decompor em múltiplos requisitos singulares [39].
*   **Exceção:** Uso de operadores lógicos (AND, OR, NOT) em letras maiúsculas para qualificar condições complexas [39].

#### 2.1.3.4. [Node] R20 - Evitar Expressões de Propósito
*   **Regra:** Evitar frases que justificam o requisito no próprio texto, como "a fim de", "de modo que", "para permitir que" [40].
*   **Diretriz:** A justificativa e o propósito devem ser delegados para o atributo de **Racional (A1)**, mantendo o enunciado do requisito conciso e focado estritamente na obrigação do sistema [40].

#### 2.1.3.5. [Node] R25 - Evitar Dependência de Cabeçalhos
*   **Regra:** O requisito deve ser compreensível independentemente do cabeçalho da seção onde está localizado no documento [42].
*   **Diretriz:** Não use pronomes referindo-se a cabeçalhos. O requisito deve manter sua integridade quando gerenciado em uma ferramenta eletrônica de requisitos baseada em banco de dados (RMT) [24, 42].

#### 2.1.3.6. [Node] R30 - Expressar Apenas Uma Vez
*   **Regra:** Cada necessidade ou requisito deve ser expresso uma única vez no conjunto [29, 43].
*   **Justificativa:** Evita inconsistências futuras durante alterações e simplifica as atividades de verificação e contagem [32, 43].

---

### 2.1.4. [Node] Padrões de Requisitos (Patterns)
*   **Definição:** Estruturas gramaticais pré-definidas (ou templates de nível de sentença) que auxiliam os autores a formular requisitos de forma completa e consistente [5, 6, 24].
*   **Blocos de Construção:** Geralmente compostos por condições, gatilhos, entidades executoras, verbos imperativos e resultados mensuráveis [3, 36].
*   **Exemplos de Padrões:** Padrões orientados a eventos, estados, restrições ou capacidades funcionais (ex: EARS - Easy Approach to Requirements Syntax) [52, 53].

---
---

## 2.2. SysML (Systems Modeling Language)

### 2.2.1. [Node] Visão Geral e Arquitetura da Linguagem
A Systems Modeling Language (SysML) é uma linguagem de modelagem de propósito geral para engenharia de sistemas [64].

#### 2.2.1.1. [Node] Relacionamento com UML
*   **Fundação:** O SysML é projetado como uma extensão do Unified Modeling Language (UML) 2.5.1 através do mecanismo de profiles [65, 71, 72].
*   **UML4SysML:** O SysML reutiliza um subconjunto de construções do UML 2 (denominado UML4SysML) e define novas construções adicionais para suprir as lacunas da engenharia de sistemas [71, 72].
*   **UML Not Required:** Certas partes complexas do UML que não se aplicam à engenharia de sistemas (como máquinas de estado de protocolo e associações muito especializadas) são deliberadamente excluídas [88, 94].
*   **Interoperabilidade:** Por herdar as construções base do UML, o SysML suporta o intercâmbio de dados via XMI e promove a colaboração contínua entre engenheiros de software (UML) e engenheiros de sistemas (SysML) [65, 72].

#### 2.2.1.2. [Node] Princípios de Design do SysML
*   **Requirements-driven:** Desenvolvido especificamente para atender aos requisitos da RFP (Request for Proposal) de UML para Engenharia de Sistemas do OMG [72].
*   **UML Reuse:** Minimizar modificações na linguagem UML subjacente para facilitar a implementação por fornecedores de ferramentas CASE [72].
*   **Partitioning (Particionamento):** Organização das estruturas da linguagem em pacotes independentes para minimizar dependências circulares [72].
*   **Layering (Camadas):** Especificado como uma camada de extensão sobre o metamodelo do UML [72].

#### 2.2.1.3. [Node] Pacotes Principais (Packages)
O metamodelo do SysML é subdividido em vários pacotes conceituais principais que estendem o UML [74, 75]:
1.  **ModelElements:** Elementos básicos de organização de modelos (pacotes, modelos, visões, pontos de vista, comentários, rationale e problemas) [75, 81, 82, 83].
2.  **Blocks:** Construção estrutural modular primária que representa de maneira unificada o sistema ou seus componentes [75, 86].
3.  **ConstraintBlocks:** Usado para expressar restrições matemáticas e relações não-causais entre parâmetros [75, 87, 93].
4.  **Ports & Flows:** Define as interações físicas ou lógicas nas fronteiras dos blocos e os itens que fluem entre conectores [75, 90].
5.  **Activities:** Elementos para modelagem de fluxos de controle e dados que descrevem comportamento de fluxo funcional [75, 99].
6.  **Allocations:** Mecanismo transversal para relacionar modelos de comportamento (atividades) com modelos de estrutura (blocos) ou outros elementos [75, 99].
7.  **Requirements:** Integração de requisitos textuais e seus relacionamentos no modelo [75, 95].

---

### 2.2.2. [Node] Diagramas do SysML (Taxonomia)
O SysML define uma taxonomia de nove diagramas, que se dividem em três grandes categorias e um grupo transversal de requisitos [77, 98, 99].

```
                ┌─────────────────────────────────────────┐
                │             Diagramas SysML             │
                └────────────────────┬────────────────────┘
       ┌─────────────────────────────┼─────────────────────────────┐
┌──────┴──────────────┐       ┌──────┴──────────────┐       ┌──────┴──────────────┐
│  Diagramas Estrutura│       │Diagramas Comportam. │       │Diagrama Requisitos  │
└──────┬──────────────┘       └──────┬──────────────┘       └─────────────────────┘
       ├─ Package Diagram            ├─ Activity Diagram
       ├─ Block Definition (bdd)     ├─ Sequence Diagram
       ├─ Internal Block (ibd)       ├─ State Machine Diagram
       └─ Parametric Diagram         └─ Use Case Diagram
```

#### 2.2.2.1. [Node] Diagramas de Estrutura
*   **Package Diagram (Diagrama de Pacotes):** Organiza o modelo em namespaces, estabelecendo partições e dependências de importação [81].
*   **Block Definition Diagram (BDD):** Define as características estruturais e comportamentais dos blocos (propriedades, operações) e seus relacionamentos de classificação (generalização) e composição (associações) [87].
*   **Internal Block Diagram (IBD):** Descreve a arquitetura interna e a interconexão das propriedades de um bloco em termos de portas, conectores e fluxos [87, 90].
*   **Parametric Diagram (Diagrama Paramétrico):** Restringe valores de propriedades de blocos usando ConstraintBlocks para apoiar análises de desempenho, dimensionamento e simulações matemáticas [87, 93].

#### 2.2.2.2. [Node] Diagramas de Comportamento
*   **Activity Diagram (Diagrama de Atividades):** Modela o fluxo de controle e dados operacionais baseados em fluxos [99].
*   **Sequence Diagram (Diagrama de Sequência):** Modela a interação baseada em troca de mensagens no tempo entre partes de blocos ou atores [94, 99].
*   **State Machine Diagram (Diagrama de Máquina de Estados):** Descreve o comportamento reativo de um bloco com base em estados discretos e transições disparadas por eventos [94].
*   **Use Case Diagram (Diagrama de Casos de Uso):** Fornece uma visão de alto nível das funcionalidades do sistema conforme percebidas por atores externos [99].

#### 2.2.2.3. [Node] Frames de Diagramas (Mandatory Frame)
*   **Regra:** Diferente do UML (onde é opcional), todos os diagramas SysML requerem obrigatoriamente um frame retangular delimitador contendo um cabeçalho identificador formal [100].
*   **Sintaxe do Cabeçalho:** `[modelElementType] modelElementName [diagramName]` [100].
*   **Função:** O frame atua como um namespace delimitado, facilitando a identificação clara e o intercâmbio de diagramas [100].

---

### 2.2.3. [Node] Elementos de Modelagem Estrutural

#### 2.2.3.1. [Node] Blocks
*   **Definição:** A unidade de descrição modular do SysML. Podem representar sistemas físicos, lógicos, componentes de software, hardware ou até elementos humanos [86].
*   **Decomposição:** Permite representar hierarquias de sistemas de interesse ("part-whole relationships") de forma recursiva (um sistema se decompõe em subsistemas, que são modelados como blocos internos) [86, 91, 92].
*   **Propriedades de Bloco:** Um bloco pode possuir propriedades de valores (valores de engenharia com unidades), propriedades de parte (componentes possuídos por composição), propriedades de referência (referências lógicas de associação) e propriedades de restrição [87, 90].

#### 2.2.3.2. [Node] Ports & Flows
*   **Definição:** Portas representam pontos de interação formal nas fronteiras lógicas ou físicas de um bloco [87, 90].
*   **Fluxos:** Descrevem o tipo de dado, material ou energia que flui através das conexões entre as portas de blocos diferentes [68].

#### 2.2.3.3. [Node] Constraint Blocks
*   **Definição:** Blocos especiais que representam relações matemáticas fundamentais e restrições não causais (sem impor qual variável é dependente ou independente) [93].
*   **Apoio à Análise:** Seus parâmetros são amarrados (ligados) por conexões paramétricas às propriedades de valor de outros blocos dentro de diagramas paramétricos para conduzir análises de engenharia [87, 93].

---

### 2.2.4. [Node] Requisitos no SysML (Crosscutting)
O SysML integra requisitos textuais diretamente no modelo visual de sistemas através do diagrama de requisitos [98].

#### 2.2.4.1. [Node] Requirement Diagram
*   **Definição:** Novo tipo de diagrama introduzido pelo SysML para representar requisitos baseados em texto e amarrar suas dependências com outros elementos de modelo lógicos, físicos ou comportamentais [95, 98].
*   **Estrutura Básica:** Um requisito do SysML contém, no mínimo, propriedades padrão para armazenar um identificador único (`Id`) e o enunciado textual formal (`Text`) [95].

#### 2.2.4.2. [Node] Relacionamentos de Requisitos
Os relacionamentos de requisitos do SysML estendem estereótipos do UML para gerenciar a rastreabilidade complexa ao longo de toda a arquitetura de sistemas [73, 95]:

*   **`«satisfy»` (Satisfazer):**
    *   *Tipo:* Dependência em que o elemento cliente (como um bloco de design estrutural ou elemento de software) atende à exigência estipulada pelo requisito fornecedor [95, 97].
    *   *Relação de Grafo:* `[Elemento de Design] ──> «satisfy» ──> [Requisito]` [97].
*   **`«verify»` (Verificar):**
    *   *Tipo:* Dependência que conecta o requisito com o caso de teste ou atividade de verificação que comprovará sua conformidade [95, 97].
    *   *Relação de Grafo:* `[Caso de Teste / Bloco de Contexto] ──> «verify» ──> [Requisito]` [97].
*   **`«deriveReqt»` (Derivar Requisito):**
    *   *Tipo:* Relacionamento de derivação entre um requisito filho e um requisito pai de nível superior, normalmente estabelecido como resultado de escolhas arquiteturais ou de decomposição [95, 96].
    *   *Relação de Grafo:* `[Requisito Filho] ──> «deriveReqt» ──> [Requisito Pai]` [96].
*   **`«copy»` (Copiar):**
    *   *Tipo:* Relacionamento de dependência que permite reuso seguro de requisitos. O requisito "slave" é uma cópia exata de leitura do requisito "master", impedindo inconsistências em múltiplos pacotes [95, 96].
    *   *Relação de Grafo:* `[Requisito Cópia] ──> «copy» ──> [Requisito Master]` [96].
*   **`«refine»` / `«trace»` (Refinar e Rastrear):**
    *   *Tipo:* Relacionamento conceitual que permite demonstrar como um elemento do modelo (como um caso de uso ou diagrama) adiciona detalhes ou refina o enunciado textual original [73, 95].

# 3. [Node] SysML Requirement Diagram

O **Requirement Diagram** (Diagrama de Requisitos) é um tipo de diagrama estrutural introduzido pelo SysML para preencher a lacuna entre as ferramentas tradicionais de gerenciamento de requisitos baseadas em texto e os modelos de design do sistema [393, 458]. Ele permite a representação gráfica, hierárquica ou tabular de requisitos de texto e seus relacionamentos de rastreabilidade [393, 408].

## 3.1. [Node] Requirement Stereotype
O elemento central do diagrama é o estereótipo `«requirement»`, que estende a metaclasse `Class` do UML [394, 410]. Ele possui propriedades fundamentais obrigatórias para identificar e descrever a especificação [394]:
*   **id : String [1]:** Identificador único e inequívoco do requisito [409, 412].
*   **text : String [1]:** O enunciado textual ou referência ao texto do requisito [412].

### 3.1.1. [Node] Requirement Stereotype Constraints
Para manter a simplicidade e a separação clara entre a especificação de requisitos e o design físico/lógico, o SysML impõe restrições rígidas baseadas em regras de validação (OCL) para qualquer elemento estereotipado como `«requirement»` [422, 424]:
1.  **Constraint 1 (no_operation):** A propriedade `ownedOperation` deve estar vazia (requisitos não possuem operações ou comportamentos internos diretos) [424].
2.  **Constraint 2 (no_attribute):** A propriedade `ownedAttribute` deve estar vazia (requisitos não contêm atributos estruturais padrão de classes) [424].
3.  **Constraint 3 (no_association):** Classes estereotipadas como requisitos não podem participar de associações UML [424].
4.  **Constraint 4 (no_generalization):** Requisitos não podem participar de relacionamentos de generalização padrão UML (exceto subclassificações do estereótipo abstrato `AbstractRequirement`) [425].
5.  **Constraint 5 (nestedclassifiers_are_requirements):** Qualquer classificador aninhado (*nestedClassifier*) dentro de um requisito deve obrigatoriamente ser estereotipado como `Requirement` ou suas especializações [425].
6.  **Constraint 6 (not_a_type):** Elementos estereotipados como requisito não podem ser usados como tipo para qualquer outro elemento do modelo [425].



## 3.2. [Node] Diagram Rules & Allowed Elements
O Diagrama de Requisitos tem um escopo de visualização restrito para garantir a legibilidade e o foco do modelo [406]:
*   **Elementos Permitidos:** O diagrama pode exibir apenas requisitos, pacotes, outros classificadores (como blocos ou atores), casos de teste (*test cases*) e notas de justificativa (*rationale*) [406].
*   **Moldura de Diagrama (Frame):** O uso da moldura retangular contendo cabeçalho com a abreviação **req** (ex: `req [Package] HSUV Requirements [Acceleration Requirement Relationships]`) é obrigatório [402, 462, 466]. A moldura define o namespace padrão dos elementos internos [462].



## 3.3. [Node] Requirement Relationships & Traceability
A rastreabilidade é estabelecida através de relacionamentos específicos dirigidos. A seta sempre aponta do elemento dependente (cliente) para o elemento de origem/requisito (fornecedor), exceto quando especificado o contrário [418, 426, 429].

```
       [Satisfying/Verifying/Deriving Element] 
                       |
                       | (Relationship)
                       v
                 [Requirement]
```

### 3.3.1. [Node] Relationship: Namespace Containment]
*   **Descrição:** Representa a decomposição hierárquica de um requisito complexo em subrequisitos menores (ex: "O sistema deve fazer A, B e C" é decomposto em três requisitos aninhados) [395].
*   **Regra de Notação:** Representado pela linha com um círculo cruzado com uma cruz (+) na extremidade do requisito pai (composição por namespace através da propriedade `nestedClassifier`) [395, 404, 423].
*   **Regra de Exclusão:** A exclusão ou deleção do requisito pai resulta na deleção automática em cascata de todos os subrequisitos aninhados [423].

### 3.3.2. [Node] Relationship: DeriveReqt
*   **Descrição:** Um requisito derivado (`«deriveReqt»`) descreve como um requisito em um nível inferior de abstração ou hierarquia física é gerado a partir de um requisito de nível superior [397, 418].
*   **Direção da Seta:** Aponta do requisito derivado (cliente) para o requisito de origem (fornecedor/source) [418].
*   **Exemplo:** O requisito de aceleração do veículo deriva os requisitos específicos de potência do motor, peso total e arrasto aerodinâmico [397].

### 3.3.3. [Node] Relationship: Satisfy
*   **Descrição:** Mostra como um elemento de design ou implementação de sistema (como um Bloco) atende plenamente ao requisito estabelecido [397, 426].
*   **Direção da Seta:** Aponta do elemento de design (cliente) para o requisito satisfeito (supplier) [426].
*   **Uso em Outros Diagramas:** A relação de satisfação pode ser exibida diretamente em diagramas estruturais (como Internal Block Diagrams) usando a propriedade callout `Satisfies` anexada ao bloco [407, 436].

### 3.3.4. [Node] Relationship: Verify
*   **Descrição:** Conecta um requisito ao elemento encarregado de provar seu cumprimento, normalmente um Caso de Teste (`«testCase»`) [398, 429].
*   **Tipo de Retorno do Caso de Teste:** O caso de teste associado deve obrigatoriamente retornar o tipo de parâmetro `VerdictKind` (cujos literais normativos são: `pass`, `fail`, `inconclusive` e `error`) [398, 420, 431].
*   **Direção da Seta:** Aponta do caso de teste (cliente) para o requisito verificado (supplier) [429].

### 3.3.5. [Node] Relationship: Refine
*   **Descrição:** Descreve como um elemento do modelo (como um Caso de Uso ou Diagrama de Atividades) detalha, contextualiza ou esclarece um requisito textual abstrato [399, 421].
*   **Flexibilidade:** Pode ser bidirecional em termos de semântica conceitual, mas formalmente herda de `DirectedRelationshipPropertyPath` para identificar caminhos de propriedades aninhados [421].

### 3.3.6. [Node] Relationship: Copy
*   **Descrição:** Utilizada para reutilização de requisitos (*Requirements Reuse*) entre diferentes famílias de produtos ou projetos [396, 415].
*   **Regra de Master/Slave:** O requisito copiado (slave) tem sua propriedade `text` restrita como uma cópia de leitura programática (*read-only*) do requisito original (master) [396, 415]. Qualquer alteração no texto do master é propagada automaticamente ao slave [396].
*   **Direção da Seta:** Aponta do requisito slave (cliente) para o requisito master (supplier) [404, 415].

### 3.3.7. [Node] Relationship: Trace
*   **Descrição:** Um relacionamento genérico de rastreamento com semântica fraca e sem restrições formais [399, 427].
*   **Recomendação de Uso:** O SysML recomenda que a relação `«trace»` **não** seja utilizada de forma misturada ou redundante com relacionamentos mais específicos como `deriveReqt`, `satisfy` ou `verify` [399].



## 3.4. [Node] Requirements Table
O SysML recomenda a representação tabular como uma alternativa extremamente compacta e eficiente aos diagramas gráficos de requisitos, contendo as seguintes colunas recomendadas [408]:
1.  **Id e Text:** Propriedades básicas do requisito [408].
2.  **Supplier Column:** Coluna indicando os fornecedores de qualquer dependência direta de rastreabilidade (Derive, Verify, Refine, Trace) [408].
3.  **Satisfying Elements:** Coluna listando os elementos de modelo específicos (como caminhos de propriedades de blocos) que satisfazem o requisito [408].
4.  **Rationale Column:** Justificativa da relação de rastreabilidade, podendo referenciar trade studies, relatórios de análise técnica ou procedimentos formais de teste [408].



## 3.5. [Node] Property-Based Requirements (PBR)
As abordagens puramente textuais de requisitos limitam a capacidade de verificação e simulação automatizada [647]. Para resolver isso, o SysML fornece mecanismos de extensão não-normativos para definir requisitos baseados em propriedades e parâmetros matemáticos vinculáveis [648]:

*   **RequirementConstraintBlock:** Um estereótipo que combina `AbstractRequirement` com um `ConstraintBlock` [652].
*   **Mapeamento de Parâmetros:** Permite definir parâmetros numéricos tipados por `ValueType` (com unidades de medida e dimensões físicas) associados diretamente ao requisito (ex: `actualMass` e `requiredMass` ambos tipados como `kilogram`) [653].
*   **Binding Connectors:** Esses parâmetros podem ser ligados diretamente às propriedades de blocos de design físico em um diagrama paramétrico (`Parametric Diagram`), permitindo que motores de cálculo verifiquem automaticamente se as equações de restrição (ex: `{actualMass <= requiredMass}`) estão sendo violadas [653, 654].
*   **CbRequirement:** Estereótipo que une um requisito diretamente a uma expressão opaca de restrição matemática (computável via linguagens de restrição como OCL) [657].

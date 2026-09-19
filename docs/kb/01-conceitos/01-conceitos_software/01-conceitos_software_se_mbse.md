**MBSE - Model Based Software Engineering**

# 1. fontes
https://modeling-languages.com/
[livro web 2006 uml-guia-do-usuario-grady-booch](https://1drv.ms/b/c/68092d0c5dd50638/IQB2X0_n6TnFSqwv6OHwIei9ARR2AgK9wdwFKebfAX6uAf0?e=YEIghd)

# 2. SysML - Systems Modeling Language
## 2.1. [Node] Visão Geral e Arquitetura da Linguagem
A Systems Modeling Language (SysML) é uma linguagem de modelagem de propósito geral para engenharia de sistemas [64].

### 2.1.1. OMG summary
The SysML v2 specification is available at OMG [SysML specification page](https://www.omg.org/spec/SysML) and the [Systems Modeling API and Services specification is available at Systems Modeling API and Services Specification page](https://www.omg.org/spec/SystemsModelingAPI).

The OMG Systems Modeling Language v1 **(OMG SysML®)** is a general-purpose graphical modeling language for specifying, analyzing, designing, and verifying complex systems that may include hardware, software, information, personnel, procedures, and facilities. In particular, the language provides graphical representations with a semantic foundation for modeling system requirements, behavior, structure, and parametrics, which is used to integrate with other engineering analysis models. It represents a subset of **[UML 2](https://www.omg.org/uml/)** with extensions needed to satisfy the requirements of the UML® for Systems Engineering RFP as indicated in Figure 1. SysML leverages the OMG XML Metadata Interchange (XMI®) to exchange modeling data between tools, and is also intended to be compatible with the evolving [ISO 10303-233](http://www.ap233.org/) systems engineering data interchange standard.

[The UML for Systems Engineering RFP](https://www.omg.org/syseng/) was developed jointly by the [OMG](https://www.omg.org/) and the [International Council on Systems Engineering (INCOSE)](http://www.incose.org/) and issued by the OMG in March 2003. The RFP specified the requirements for extending UML to support the needs of the systems engineering community. The [SysML Specification](https://www.omg.org/spec/SysML) was developed in response to these requirements by the [diverse group of tool vendors, end users, academia, and government representatives](https://www.omg.org/sysml/SysML-Development-Team.htm). The Object Management Group announced the adoption on July 6, 2006 and the availability of OMG SysML™ v1.0 in September 2007.

![Figure 1. Relationship between SysML and UML](https://www.omg.org/sysml/images/SysML-Figure-1-a.jpg)  
  
Figure 1. Relationship between SysML and UML



### 2.1.2. [Node] Relacionamento com UML
*   **Fundação:** O SysML é projetado como uma extensão do Unified Modeling Language (UML) 2.5.1 através do mecanismo de profiles [65, 71, 72].
*   **UML4SysML:** O SysML reutiliza um subconjunto de construções do UML 2 (denominado UML4SysML) e define novas construções adicionais para suprir as lacunas da engenharia de sistemas [71, 72].
*   **UML Not Required:** Certas partes complexas do UML que não se aplicam à engenharia de sistemas (como máquinas de estado de protocolo e associações muito especializadas) são deliberadamente excluídas [88, 94].
*   **Interoperabilidade:** Por herdar as construções base do UML, o SysML suporta o intercâmbio de dados via XMI e promove a colaboração contínua entre engenheiros de software (UML) e engenheiros de sistemas (SysML) [65, 72].

### 2.1.3. [Node] Princípios de Design do SysML
*   **Requirements-driven:** Desenvolvido especificamente para atender aos requisitos da RFP (Request for Proposal) de UML para Engenharia de Sistemas do OMG [72].
*   **UML Reuse:** Minimizar modificações na linguagem UML subjacente para facilitar a implementação por fornecedores de ferramentas CASE [72].
*   **Partitioning (Particionamento):** Organização das estruturas da linguagem em pacotes independentes para minimizar dependências circulares [72].
*   **Layering (Camadas):** Especificado como uma camada de extensão sobre o metamodelo do UML [72].

### 2.1.4. [Node] Pacotes Principais (Packages)
O metamodelo do SysML é subdividido em vários pacotes conceituais principais que estendem o UML [74, 75]:
1.  **ModelElements:** Elementos básicos de organização de modelos (pacotes, modelos, visões, pontos de vista, comentários, rationale e problemas) [75, 81, 82, 83].
2.  **Blocks:** Construção estrutural modular primária que representa de maneira unificada o sistema ou seus componentes [75, 86].
3.  **ConstraintBlocks:** Usado para expressar restrições matemáticas e relações não-causais entre parâmetros [75, 87, 93].
4.  **Ports & Flows:** Define as interações físicas ou lógicas nas fronteiras dos blocos e os itens que fluem entre conectores [75, 90].
5.  **Activities:** Elementos para modelagem de fluxos de controle e dados que descrevem comportamento de fluxo funcional [75, 99].
6.  **Allocations:** Mecanismo transversal para relacionar modelos de comportamento (atividades) com modelos de estrutura (blocos) ou outros elementos [75, 99].
7.  **Requirements:** Integração de requisitos textuais e seus relacionamentos no modelo [75, 95].




### 2.1.5. SysML vs UML (site draw.io)

A linguagem de modelagem de sistemas (SysML) é uma extensão da UML modificada para engenharia de sistemas. Embora ambas possam documentar software, informações e processos, os diagramas SysML também documentam o hardware, os seres humanos, os componentes físicos e as instalações do sistema.  


![venn](https://www.drawio.com/img/blog/sysml-vs-uml.png)

SysML possui menos diagramas que [UML](https://www.drawio.com/docs/diagram-types/uml/) e modifica três dos tipos de diagramas compartilhados: diagramas de atividade, diagramas de definição de blocos (derivados de diagramas de classe) e diagramas de blocos internos (derivados de diagramas de estrutura composta).

Dois novos tipos de diagramas em SysML — diagramas de requisitos e diagramas paramétricos — são usados para documentar especificações e garantir que o sistema funcione corretamente, além de ilustrar como o produto atenderá a critérios mensuráveis de desempenho, segurança ou qualidade.

#### 2.1.5.1. Dica: Use um diagrama com várias páginas.

Como cada sistema ou componente pode conter subsistemas/subcomponentes, [use diagramas com várias páginas](https://www.drawio.com/docs/manual/pages/) e [vincule](https://www.drawio.com/docs/manual/insert/insert-text-link/) a forma principal à sua página de diagrama detalhada. Selecione uma forma e pressione `Alt+Shift+L`, ou clique com o botão direito do mouse em uma forma e selecione *Editar vínculo*.  
![Adicione links para diagramas de subpacotes em outra página para facilitar a navegação no seu diagrama|800x500](https://www.drawio.com/img/blog/sysml-package-diagram-add-link.png)

#### 2.1.5.2. Ative a biblioteca de formas SysML.

Para criar diagramas SysML no draw.io, habilite a biblioteca de formas SysML. As formas estão organizadas em subcategorias de tipos de diagrama.

1. Clique em *Mais Formas* na parte inferior do painel de formas à esquerda.
2. Marque a caixa de seleção ao lado de *SysML* na seção *Negócios*.
3. Clique em *Aplicar*.  
	![Ative a biblioteca de formas SysML.](https://www.drawio.com/img/blog/sysml-shape-library-enable.png)

Embora seja possível criar muitos dos diagramas com as bibliotecas de formas UML, as formas de bloco com portas, restrições e fluxos estão na biblioteca de formas SysML.

**Dica:** [Estilize as formas com cores](https://www.drawio.com/docs/manual/styles/shape-styles/) para diferenciar mais claramente os tipos de elementos, os diferentes agrupamentos ou as regiões.


## 2.2. [Node] Diagramas do SysML (Taxonomia)
O SysML define uma taxonomia de nove diagramas, que se dividem em três grandes categorias e um grupo transversal de requisitos [77, 98, 99].
### 2.2.1. SysML Diagram Summary

The SysML diagram types are identified in Figure 2 and summarized below. *Refer to the [OMG SysML Tutorial](https://www.omg.org/sysml/INCOSE-OMGSysML-Tutorial-Final-090901.pdf) for an overview of the language.* (Note: Because these are large files, it is recommended that you save to your desktop by right clicking and save target)

![Figure 2. SysML Diagram Types](https://www.omg.org/sysml/images/SysML-Figure-2.jpg)  
  
Figure 2. SysML Diagram Types

The block is the basic unit of structure in SysML and can be used to represent hardware, software, facilities, personnel, or any other system element. The system structure is represented by block definition diagrams and internal block diagrams. A block definition diagram describes the system hierarchy and system/component classifications. The internal block diagram describes the internal structure of a system in terms of its parts, ports, and connectors. The package diagram is used to organize the model.

The behavior diagrams include the use case diagram, activity diagram, sequence diagram, and state machine diagram. A use-case diagram provides a high-level description of functionality that is achieved through interaction among systems or system parts. The activity diagram represents the flow of data and control between activities. A sequence diagram represents the interaction between collaborating parts of a system. The state machine diagram describes the state transitions and actions that a system or its parts perform in response to events.

SysML includes a graphical construct to represent text based requirements and relate them to other model elements. The requirements diagram captures requirements hierarchies and requirements derivation, and the satisfy and verify relationships allow a modeler to relate a requirement to a model element that satisfies or verifies the requirements. The requirement diagram provides a bridge between the typical requirements management tools and the system models.

The parametric diagram represents constraints on system property values such as performance, reliability, and mass properties, and serves as a means to integrate the specification and design models with engineering analysis models.

SysML also includes an allocation relationship to represent various types of allocation, including allocation of functions to components, logical to physical components, and software to hardware.

A simple example of some of the key diagram types is highlighted in Figure 3.

![Figure 3. The Four Pillars of SysML](https://www.omg.org/sysml/images/SysML-Figure-3.jpg)  
  
Figure 3. The Four Pillars of SysML

The [OMG SysML Specification](https://www.omg.org/spec/SysML/1.5/) includes diagram element tables in chapters 7-17 that identifies allowable symbols on each of the diagram types, as well as usage examples. Fragments corresponding to the design of a hybrid sports utility vehicle (HSUV) are included in the sample problem in Annex D of the [specification](https://www.omg.org/spec/SysML/1.5/).

The OMG SysML Specification Version 1.4.1 is also published by the International Organization for Standardization (ISO) as a full International Standard (IS), whose short title is “ISO/IEC 19514:2017” and full title is "ISO/IEC 19514:2017, Information technology -- Object management group systems modeling language (OMG SysML)". The direct catalogue reference is [https://www.iso.org/standard/65231.html](https://www.iso.org/standard/65231.html).

To learn about the latest evolution of the language, visit the [SysML v2.0](https://www.omg.org/sysml/sysmlv2) page.



### 2.2.2. [Node] Diagramas de Estrutura
*   **Package Diagram (Diagrama de Pacotes):** Organiza o modelo em namespaces, estabelecendo partições e dependências de importação [81].
*   **Block Definition Diagram (BDD):** Define as características estruturais e comportamentais dos blocos (propriedades, operações) e seus relacionamentos de classificação (generalização) e composição (associações) [87].
*   **Internal Block Diagram (IBD):** Descreve a arquitetura interna e a interconexão das propriedades de um bloco em termos de portas, conectores e fluxos [87, 90].
*   **Parametric Diagram (Diagrama Paramétrico):** Restringe valores de propriedades de blocos usando ConstraintBlocks para apoiar análises de desempenho, dimensionamento e simulações matemáticas [87, 93].

#### 2.2.2.1. Diagrama de package

*Os diagramas de pacotes SysML são ligeiramente diferentes dos [diagramas de pacotes UML](https://www.drawio.com/docs/diagram-types/uml/package-diagrams/).*

Os diagramas de pacotes são usados para documentar, organizar e gerenciar sistemas grandes e complexos. A partir dessa visão geral, você pode acessar diagramas de nível inferior para subpacotes, operações (diagrama de atividades), restrições, blocos e assim por diante.

Utilize formas da categoria *Elementos do Modelo* e organize-as para formar grupos lógicos dentro de cada pacote, incluindo vistas e pontos de vista, modelos e bibliotecas de modelos, restrições e requisitos, quando necessário.  
![Os elementos do modelo SysML contêm vários estilos de pacotes, modelos, visualizações e pontos de vista.](https://www.drawio.com/img/blog/sysml-model-element-shapes.png)

Use o *Diagrama de Pacotes* como forma externa para nomear o diagrama. Formas *de Blocos SysML* também podem ser usadas em diagramas de pacotes.

As relações entre pacotes e elementos são mostradas com diferentes extremidades de conectores e linhas contínuas ou tracejadas: depender, importar, realizar, estar em conformidade, conter, refinar e expor.  
[![Os diagramas de pacotes agrupam elementos de um sistema de diversas maneiras lógicas.](https://www.drawio.com/img/blog/sysml-package-diagram.png)](https://viewer.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&page=0&nav=1&title=#Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fjgraph%2Fdrawio-diagrams%2Fdev%2Fexamples%2Fsysml-package-diagram.drawio)

**Dica:** Identifique quaisquer relações pouco claras clicando duas vezes em um conector, por exemplo `<<conform>>`, ou `<<refine>>`.

Muitas dessas formas podem conter subdiagramas. Como alternativa, crie um [diagrama com várias páginas](https://www.drawio.com/docs/manual/pages/) e [estabeleça links da forma principal](https://www.drawio.com/docs/manual/insert/insert-text-link/) para a página correspondente.

#### 2.2.2.2. Diagrama de definição de blocos

*Os diagramas de definição de blocos SysML são [diagramas de classe UML](https://www.drawio.com/docs/diagram-types/uml/class-diagrams/) bastante modificados.*

Os 'blocos' descrevem a arquitetura de um sistema e contêm **restrições**, **operações**, **partes**, **referências**, **valores** e **propriedades** — tudo o que você precisa para especificar os componentes de hardware, software e humanos de um sistema.

Um ou mais compartimentos - **estereótipo**, **espaço de nomes** e **estrutura** \- podem conter diagramas de definição de blocos de nível inferior, aninhando sistemas mais simples dentro de blocos de nível superior.

Os conectores indicam um comportamento semelhante aos diagramas de classe UML, mas com menos tipos de 'seta':

- **dependência** \- linha tracejada
- **Associação** \- rótulo central com uma seta para indicar a direção da associação.
	- **associação parcial** \- diamante preenchido
		- **associação compartilhada** \- diamante vazio
- **generalização** \- triângulo vazio
- **Contenção de namespace** \- círculo com barras horizontais/verticais

Os conectores podem se dividir para formar associações com várias ramificações. Use o formato de ponto de passagem para unir esses conectores de forma organizada no draw.io.  
[![Desenhe diagramas de definição de blocos SysML no draw.io com a biblioteca de formas SysML.](https://www.drawio.com/img/blog/sysml-block-definition-diagram.png)](https://viewer.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&page=0&nav=1&title=#Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fjgraph%2Fdrawio-diagrams%2Fdev%2Fexamples%2Fsysml-block-definition-diagram.drawio)

**Trabalhar com texto em formas de bloco:**

- Pressione `Enter` para adicionar uma nova linha.
- Clique duas vezes em uma palavra para selecioná-la e formatá-la com a guia *Texto* no painel Formatar.
- Para adicionar um divisor de seção, selecione um divisor existente em qualquer bloco. Clique duas vezes no bloco desejado para que o cursor de texto apareça e pressione `Ctrl+C` Enter `Ctrl+V` para copiar e colar o divisor de seção nesse local.

#### 2.2.2.3. Diagrama de blocos internos

*[Os diagramas de blocos internos do SysML são diagramas de estrutura composta UML](https://www.drawio.com/blog/uml-2-5/) modificados .*

Os diagramas de blocos internos descrevem as conexões entre as portas das instâncias de blocos para mostrar quais dados ou materiais fluem entre esses blocos e suas propriedades.

Existem alguns tipos especiais de propriedades:

- **portas** \- permitem apenas tipos específicos de interações com esse bloco
- **restrições** \- limitar outras propriedades dentro do bloco
- **participantes** \- indicar associações compostas

Os conectores em diagramas de blocos internos podem mostrar o seguinte:

- **dependência** \- linha tracejada
- **Encadernação** \- linha contínua, opcionalmente com indicação do tipo de amarração, por exemplo.`<<equal>>`

Indique a direção do fluxo com setas sólidas - formas triangulares básicas preenchidas - no meio dos conectores.  
[![Desenhe diagramas de blocos internos do SysML no draw.io com a biblioteca de formas do SysML.](https://www.drawio.com/img/blog/sysml-internal-block-diagram.png)](https://viewer.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&page=0&nav=1&title=#Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fjgraph%2Fdrawio-diagrams%2Fdev%2Fexamples%2Fsysml-internal-block-diagram.drawio)

##### 2.2.2.3.1. Diagramas paramétricos

Um modelo paramétrico é uma forma especializada de diagrama de blocos interno usado para analisar métricas de desempenho, segurança, confiabilidade e características físicas mensuráveis. *(Apenas SysML)*

Conecte cada restrição por meio de suas portas a um nó de parâmetro de restrição ou a outra forma de restrição. Use as formas nas categorias *Restrições*, *Portas e Fluxos* e modifique-as, inverta-as e rotule-as conforme necessário para adequá-las ao seu layout.  
[![Desenhe diagramas paramétricos SysML no draw.io com a biblioteca de formas SysML.](https://www.drawio.com/img/blog/sysml-parametric-diagram.png)](https://viewer.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&page=0&nav=1&title=#Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fjgraph%2Fdrawio-diagrams%2Fdev%2Fexamples%2Fsysml-parametric-diagram.drawio)

**Dica:** Sobreponha formas quadradas adicionais para adicionar mais de duas restrições e agrupá-las com a forma da restrição. Mantenha pressionada a tecla Ctrl `Alt` ou `Option` Shift para [sobrepor as formas às formas do contêiner](https://www.drawio.com/docs/manual/shapes/shapes-overlap/).

### 2.2.3. [Node] Diagramas de Comportamento
*   **Activity Diagram (Diagrama de Atividades):** Modela o fluxo de controle e dados operacionais baseados em fluxos [99].
*   **Sequence Diagram (Diagrama de Sequência):** Modela a interação baseada em troca de mensagens no tempo entre partes de blocos ou atores [94, 99].
*   **State Machine Diagram (Diagrama de Máquina de Estados):** Descreve o comportamento reativo de um bloco com base em estados discretos e transições disparadas por eventos [94].
*   **Use Case Diagram (Diagrama de Casos de Uso):** Fornece uma visão de alto nível das funcionalidades do sistema conforme percebidas por atores externos [99].

#### 2.2.3.1. Diagrama de casos de uso

Um [diagrama de casos de uso descreve](https://www.drawio.com/docs/diagram-types/uml/use-case-diagrams/) todas as formas como um usuário final interage com seus sistemas. *(Semelhante ao UML)*  
[![Um exemplo de diagrama de casos de uso](https://www.drawio.com/img/blog/uml-use-case-example.png)](https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=#Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fjgraph%2Fdrawio-diagrams%2Fdev%2Fexamples%2Fuml-use-case-example.drawio)

#### 2.2.3.2. Diagrama de sequência

[Os diagramas de sequência](https://www.drawio.com/docs/diagram-types/uml/sequence-diagrams/) mostram a ordem das mensagens que são transmitidas entre os elementos de um sistema para concluir uma tarefa ou caso de uso específico. *(Semelhante à UML)*  
[![Adicione rótulos de formas e conectores e arraste o texto para as condições para dentro de uma forma de quadro em um diagrama de sequência no draw.io.](https://www.drawio.com/img/blog/uml-sequence-example.png)](https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=#Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fjgraph%2Fdrawio-diagrams%2Fdev%2Fexamples%2Fsequence-diagram-examples.drawio)

#### 2.2.3.3. Diagrama de máquina de estados

[Os diagramas de máquina de estados](https://www.drawio.com/docs/diagram-types/uml/state-diagrams/) documentam os vários estados que um sistema pode atingir. Cada nó representa um estado do sistema, e os conectores mostram os gatilhos que forçam uma mudança para outro estado. *(Semelhante à UML)*  
[![Um exemplo de diagrama de máquina de estados UML de alto nível de uma fechadura inteligente.](https://www.drawio.com/img/blog/uml-state-diagram-smart-lock.png)](https://viewer.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&page=0&nav=1&title=#Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fjgraph%2Fdrawio-diagrams%2Fdev%2Fblog%2Fuml-state-diagram-smart-lock.drawio)

#### 2.2.3.4. Diagrama de atividades

*Os diagramas de atividades em SysML usam formas ligeiramente diferentes das usadas em UML, mas os conceitos são os mesmos.*

Em [diagramas de atividades](https://www.drawio.com/docs/diagram-types/uml/activity-diagrams/) SysML, as etapas que mostram tanto o fluxo de controle (conector sólido) quanto o fluxo de dados (conector tracejado) são organizadas em raias. As regiões podem mostrar eventos, agrupar subatividades ou indicar interrupções.  
[![Os diagramas de atividades são usados ​​para modelar fluxos de trabalho de diversas maneiras.](https://www.drawio.com/img/blog/sysml-activity-diagram.png)](https://viewer.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&page=0&nav=1&title=#Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fjgraph%2Fdrawio-diagrams%2Fdev%2Fexamples%2Fsysml-activity-diagram.drawio)

Use as formas da categoria *Atividades SysML* para construir seu diagrama de atividades. As portas nas formas de atividade — os pequenos quadrados — especificam onde os parâmetros de dados ou objetos são necessários.  
![Os formatos de atividade do SysML são diferentes daqueles usados ​​no UML.](https://www.drawio.com/img/blog/sysml-activity-shapes.png)




### 2.2.4. [Node] Diagrama de requisitos
#### 2.2.4.1. resumo
O **Requirement Diagram** (Diagrama de Requisitos) é um tipo de diagrama estrutural introduzido pelo SysML para preencher a lacuna entre as ferramentas tradicionais de gerenciamento de requisitos baseadas em texto e os modelos de design do sistema [393, 458]. Ele permite a representação gráfica, hierárquica ou tabular de requisitos de texto e seus relacionamentos de rastreabilidade [393, 408].

Também chamados de diagramas de especificação detalhada, os diagramas de requisitos mostram como os diferentes requisitos se relacionam entre si e com os elementos de projeto. Eles incluem casos de teste descritivos para garantir que os requisitos sejam acompanhados e atendidos durante a implementação.

Os requisitos podem ser especificados da seguinte forma:

- **Funcional** \- esses requisitos *devem* ser atendidos.
- **Não funcional** \- um critério de qualidade para testar e avaliar o desempenho de um sistema e tudo o que ele produz.

Os requisitos não funcionais podem ser especializados das seguintes maneiras.

- `<<performanceRequirement>>`
- `<<interfaceRequirement>>`
- `<<designConstraint>>`
- `<<physicalRequirement>>`

Os requisitos contidos são indicados por um círculo com uma cruz vertical no requisito principal. Os casos de teste e os requisitos derivados são vinculados aos requisitos por meio de um conector tracejado e um rótulo apropriado.  
[![Crie diagramas de requisitos SysML no draw.io com a biblioteca de formas SysML.](https://www.drawio.com/img/blog/sysml-requirements-diagram.png)](https://viewer.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&page=0&nav=1&title=#Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fjgraph%2Fdrawio-diagrams%2Fdev%2Fexamples%2Fsysml-requirements-diagram.drawio)

#### 2.2.4.2. [Node] Requirement Stereotype
O elemento central do diagrama é o estereótipo `«requirement»`, que estende a metaclasse `Class` do UML [394, 410]. Ele possui propriedades fundamentais obrigatórias para identificar e descrever a especificação [394]:
*   **id : String [1]:** Identificador único e inequívoco do requisito [409, 412].
*   **text : String [1]:** O enunciado textual ou referência ao texto do requisito [412].

##### 2.2.4.2.1. [Node] Requirement Stereotype Constraints
Para manter a simplicidade e a separação clara entre a especificação de requisitos e o design físico/lógico, o SysML impõe restrições rígidas baseadas em regras de validação (OCL) para qualquer elemento estereotipado como `«requirement»` [422, 424]:
1.  **Constraint 1 (no_operation):** A propriedade `ownedOperation` deve estar vazia (requisitos não possuem operações ou comportamentos internos diretos) [424].
2.  **Constraint 2 (no_attribute):** A propriedade `ownedAttribute` deve estar vazia (requisitos não contêm atributos estruturais padrão de classes) [424].
3.  **Constraint 3 (no_association):** Classes estereotipadas como requisitos não podem participar de associações UML [424].
4.  **Constraint 4 (no_generalization):** Requisitos não podem participar de relacionamentos de generalização padrão UML (exceto subclassificações do estereótipo abstrato `AbstractRequirement`) [425].
5.  **Constraint 5 (nestedclassifiers_are_requirements):** Qualquer classificador aninhado (*nestedClassifier*) dentro de um requisito deve obrigatoriamente ser estereotipado como `Requirement` ou suas especializações [425].
6.  **Constraint 6 (not_a_type):** Elementos estereotipados como requisito não podem ser usados como tipo para qualquer outro elemento do modelo [425].



#### 2.2.4.3. [Node] Diagram Rules & Allowed Elements
O Diagrama de Requisitos tem um escopo de visualização restrito para garantir a legibilidade e o foco do modelo [406]:
*   **Elementos Permitidos:** O diagrama pode exibir apenas requisitos, pacotes, outros classificadores (como blocos ou atores), casos de teste (*test cases*) e notas de justificativa (*rationale*) [406].
*   **Moldura de Diagrama (Frame):** O uso da moldura retangular contendo cabeçalho com a abreviação **req** (ex: `req [Package] HSUV Requirements [Acceleration Requirement Relationships]`) é obrigatório [402, 462, 466]. A moldura define o namespace padrão dos elementos internos [462].



#### 2.2.4.4. [Node] Requirement Relationships & Traceability
A rastreabilidade é estabelecida através de relacionamentos específicos dirigidos. A seta sempre aponta do elemento dependente (cliente) para o elemento de origem/requisito (fornecedor), exceto quando especificado o contrário [418, 426, 429].

```
       [Satisfying/Verifying/Deriving Element] 
                       |
                       | (Relationship)
                       v
                 [Requirement]
```

##### 2.2.4.4.1. [Node] Relationship: Namespace Containment]
*   **Descrição:** Representa a decomposição hierárquica de um requisito complexo em subrequisitos menores (ex: "O sistema deve fazer A, B e C" é decomposto em três requisitos aninhados) [395].
*   **Regra de Notação:** Representado pela linha com um círculo cruzado com uma cruz (+) na extremidade do requisito pai (composição por namespace através da propriedade `nestedClassifier`) [395, 404, 423].
*   **Regra de Exclusão:** A exclusão ou deleção do requisito pai resulta na deleção automática em cascata de todos os subrequisitos aninhados [423].

##### 2.2.4.4.2. [Node] Relationship: DeriveReqt
*   **Descrição:** Um requisito derivado (`«deriveReqt»`) descreve como um requisito em um nível inferior de abstração ou hierarquia física é gerado a partir de um requisito de nível superior [397, 418].
*   **Direção da Seta:** Aponta do requisito derivado (cliente) para o requisito de origem (fornecedor/source) [418].
*   **Exemplo:** O requisito de aceleração do veículo deriva os requisitos específicos de potência do motor, peso total e arrasto aerodinâmico [397].

##### 2.2.4.4.3. [Node] Relationship: Satisfy
*   **Descrição:** Mostra como um elemento de design ou implementação de sistema (como um Bloco) atende plenamente ao requisito estabelecido [397, 426].
*   **Direção da Seta:** Aponta do elemento de design (cliente) para o requisito satisfeito (supplier) [426].
*   **Uso em Outros Diagramas:** A relação de satisfação pode ser exibida diretamente em diagramas estruturais (como Internal Block Diagrams) usando a propriedade callout `Satisfies` anexada ao bloco [407, 436].

##### 2.2.4.4.4. [Node] Relationship: Verify
*   **Descrição:** Conecta um requisito ao elemento encarregado de provar seu cumprimento, normalmente um Caso de Teste (`«testCase»`) [398, 429].
*   **Tipo de Retorno do Caso de Teste:** O caso de teste associado deve obrigatoriamente retornar o tipo de parâmetro `VerdictKind` (cujos literais normativos são: `pass`, `fail`, `inconclusive` e `error`) [398, 420, 431].
*   **Direção da Seta:** Aponta do caso de teste (cliente) para o requisito verificado (supplier) [429].

##### 2.2.4.4.5. [Node] Relationship: Refine
*   **Descrição:** Descreve como um elemento do modelo (como um Caso de Uso ou Diagrama de Atividades) detalha, contextualiza ou esclarece um requisito textual abstrato [399, 421].
*   **Flexibilidade:** Pode ser bidirecional em termos de semântica conceitual, mas formalmente herda de `DirectedRelationshipPropertyPath` para identificar caminhos de propriedades aninhados [421].

##### 2.2.4.4.6. [Node] Relationship: Copy
*   **Descrição:** Utilizada para reutilização de requisitos (*Requirements Reuse*) entre diferentes famílias de produtos ou projetos [396, 415].
*   **Regra de Master/Slave:** O requisito copiado (slave) tem sua propriedade `text` restrita como uma cópia de leitura programática (*read-only*) do requisito original (master) [396, 415]. Qualquer alteração no texto do master é propagada automaticamente ao slave [396].
*   **Direção da Seta:** Aponta do requisito slave (cliente) para o requisito master (supplier) [404, 415].

##### 2.2.4.4.7. [Node] Relationship: Trace
*   **Descrição:** Um relacionamento genérico de rastreamento com semântica fraca e sem restrições formais [399, 427].
*   **Recomendação de Uso:** O SysML recomenda que a relação `«trace»` **não** seja utilizada de forma misturada ou redundante com relacionamentos mais específicos como `deriveReqt`, `satisfy` ou `verify` [399].


#### 2.2.4.5. [Node] Requirements Table
O SysML recomenda a representação tabular como uma alternativa extremamente compacta e eficiente aos diagramas gráficos de requisitos, contendo as seguintes colunas recomendadas [408]:
1.  **Id e Text:** Propriedades básicas do requisito [408].
2.  **Supplier Column:** Coluna indicando os fornecedores de qualquer dependência direta de rastreabilidade (Derive, Verify, Refine, Trace) [408].
3.  **Satisfying Elements:** Coluna listando os elementos de modelo específicos (como caminhos de propriedades de blocos) que satisfazem o requisito [408].
4.  **Rationale Column:** Justificativa da relação de rastreabilidade, podendo referenciar trade studies, relatórios de análise técnica ou procedimentos formais de teste [408].


#### 2.2.4.6. [Node] Property-Based Requirements (PBR)
As abordagens puramente textuais de requisitos limitam a capacidade de verificação e simulação automatizada [647]. Para resolver isso, o SysML fornece mecanismos de extensão não-normativos para definir requisitos baseados em propriedades e parâmetros matemáticos vinculáveis [648]:

*   **RequirementConstraintBlock:** Um estereótipo que combina `AbstractRequirement` com um `ConstraintBlock` [652].
*   **Mapeamento de Parâmetros:** Permite definir parâmetros numéricos tipados por `ValueType` (com unidades de medida e dimensões físicas) associados diretamente ao requisito (ex: `actualMass` e `requiredMass` ambos tipados como `kilogram`) [653].
*   **Binding Connectors:** Esses parâmetros podem ser ligados diretamente às propriedades de blocos de design físico em um diagrama paramétrico (`Parametric Diagram`), permitindo que motores de cálculo verifiquem automaticamente se as equações de restrição (ex: `{actualMass <= requiredMass}`) estão sendo violadas [653, 654].
*   **CbRequirement:** Estereótipo que une um requisito diretamente a uma expressão opaca de restrição matemática (computável via linguagens de restrição como OCL) [657].

### 2.2.5. [Node] Frames de Diagramas (Mandatory Frame)
*   **Regra:** Diferente do UML (onde é opcional), todos os diagramas SysML requerem obrigatoriamente um frame retangular delimitador contendo um cabeçalho identificador formal [100].
*   **Sintaxe do Cabeçalho:** `[modelElementType] modelElementName [diagramName]` [100].
*   **Função:** O frame atua como um namespace delimitado, facilitando a identificação clara e o intercâmbio de diagramas [100].



## 2.3. [Node] Elementos de Modelagem Estrutural

### 2.3.1. [Node] Blocks
*   **Definição:** A unidade de descrição modular do SysML. Podem representar sistemas físicos, lógicos, componentes de software, hardware ou até elementos humanos [86].
*   **Decomposição:** Permite representar hierarquias de sistemas de interesse ("part-whole relationships") de forma recursiva (um sistema se decompõe em subsistemas, que são modelados como blocos internos) [86, 91, 92].
*   **Propriedades de Bloco:** Um bloco pode possuir propriedades de valores (valores de engenharia com unidades), propriedades de parte (componentes possuídos por composição), propriedades de referência (referências lógicas de associação) e propriedades de restrição [87, 90].

### 2.3.2. [Node] Ports & Flows
*   **Definição:** Portas representam pontos de interação formal nas fronteiras lógicas ou físicas de um bloco [87, 90].
*   **Fluxos:** Descrevem o tipo de dado, material ou energia que flui através das conexões entre as portas de blocos diferentes [68].

### 2.3.3. [Node] Constraint Blocks
*   **Definição:** Blocos especiais que representam relações matemáticas fundamentais e restrições não causais (sem impor qual variável é dependente ou independente) [93].
*   **Apoio à Análise:** Seus parâmetros são amarrados (ligados) por conexões paramétricas às propriedades de valor de outros blocos dentro de diagramas paramétricos para conduzir análises de engenharia [87, 93].



## 2.4. [Node] Requisitos no SysML (Crosscutting)
O SysML integra requisitos textuais diretamente no modelo visual de sistemas através do diagrama de requisitos [98].

### 2.4.1. [Node] Requirement Diagram
*   **Definição:** Novo tipo de diagrama introduzido pelo SysML para representar requisitos baseados em texto e amarrar suas dependências com outros elementos de modelo lógicos, físicos ou comportamentais [95, 98].
*   **Estrutura Básica:** Um requisito do SysML contém, no mínimo, propriedades padrão para armazenar um identificador único (`Id`) e o enunciado textual formal (`Text`) [95].

### 2.4.2. [Node] Relacionamentos de Requisitos
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



# 3. MDD - Model Driven Design 

![YT - model driven design](https://youtu.be/0mLJG-4Cj64?is=M3hzyxnWTg2Yi2MT)

# 4. MDA - Model Driven Architecture 

## 4.1. o que é arquitetura

Arquitetura é o conjunto de decisões significativas acerca dos seguintes itens:
 - A **organização** do sistema de software.
 - A seleção dos **elementos estruturais e suas interfaces**, que compõem o sistema.
 - Seu **comportamento**, conforme especificado nas colaborações entre esses elementos.
 - A **composição** desses elementos estruturais e comportamentais em subsistemas progressivamente maiores.
 - O **estilo** de arquitetura que orienta a organização: os elementos estáticos e dinâmicos e as respectivas interfaces, colaborações e composição.


**CINCO VISÕES INTERLIGADAS**
![[260617_conceitos_info_mbse_MDA.gif]]

- **Visão do caso de uso** 
	- abrange os casos de uso que descrevem o comportamento do sistema conforme é visto pelos seus usuários finais, analistas e pessoal de teste. Essa visão não especifica realmente a organização do sistema de um software. Porém, ela existe para especificar as forças que determinam a forma da arquitetura do sistema. Com a UML, os aspectos estáticos dessa visão são capturados em diagramas de caso de uso, enquanto os aspectos dinâmicos são capturados em diagramas de interação, diagramas de estados e diagramas de atividades.
- **Visão de projeto** de um sistema 
	- abrange as classes, interfaces e colaborações que formam o vocabulário do problema e de sua solução. Essa perspectiva proporciona principalmente um suporte para os requisitos funcionais do sistema, ou seja, os serviços que o sistema deverá fornecer a seus usuários finais. Com a UML, os aspectos estáticos dessa visão são captados em diagramas de classes e de objetos; os aspectos dinâmicos são captados em diagramas de interações, diagramas de estados e diagramas de atividades. O diagrama da estrutura interna de uma classe é particularmente útil.
- **Visão de processo** de um sistema 
	- mostra o fluxo de controle entre as várias partes, incluindo mecanismos de concorrência e de sincronização. Essa visão cuida principalmente de questões referentes ao desempenho, à escalabilidade e ao rendimento do sistema. Com a UML, os aspectos estáticos e dinâmicos dessa visão são captados nos mesmos tipos de diagramas da visão de projeto, mas com o foco voltado para as classes ativas que controlam o sistema e as mensagens que passam por elas.
- **Visão de implementação** de um sistema 
	- abrange os **componentes** e os **artefatos** utilizados para a montagem e o fornecimento do sistema físico. Essa visão envolve principalmente o gerenciamento da configuração das versões do sistema, compostas por componentes e arquivos de alguma maneira independentes, que podem ser reunidos de diferentes formas para a produção de um sistema executável. Diz respeito também ao **mapeamento de classes lógicas e componentes** para artefatos físicos. Com a UML, os aspectos estáticos dessa visão são capturados em diagramas de componentes; os aspectos dinâmicos são capturados em diagramas de interações, de estados e de atividades.
- A **visão de implantação** de um sistema 
	- abrange os nós que formam a topologia de hardware em que o sistema é executado. Com a UML, os aspectos estáticos dessa visão são capturados em diagramas de implantação; os aspectos dinâmicos são capturados em diagramas de interações, diagramas de estados e diagramas de atividades.

Cada uma dessas cinco visões pode ser considerada isoladamente, permitindo que diferentes participantes dirijam seu foco para os aspectos da arquitetura do sistema que mais lhes interessam. Essas cinco visões também interagem entre si – os nós na visão de implantação contêm componentes desta visão, que, por sua vez, representa a realização física de classes, interfaces, colaborações e classes ativas provenientes das visões de projeto e de processo. A UML permite expressar cada uma dessas cinco visões.


## 4.2. UAF - Unified Architecture Framework

## 4.3. CIM, PIM, PSM

CIM - Computation Independent Model
PIM - Platform Independent Model
PSM - Platform Specific Model
## 4.4. MOF - Meta Object Facility 

[omg--mof](https://www.omg.org/spec/MOF/2.5.1/PDF)

## 4.5. UML - Unified Modeling Language 

### 4.5.1. Resumos

- Artefatos de documentação:
	-  Requisitos 
	- Arquitetura  
	- Projeto  
	- Código-fonte  
	- Planos do projeto  
	- Testes  
	- Protótipos  
	- Versões
- Elementos principais da UML: 
	- **blocos de construção** básicos da UML
		- itens 
			- Itens estruturais: 
			- Itens comportamentais 
			- Itens de agrupamentos 
			- Itens anotacionais
		- relacionamentos 
			- Dependência 
			- Associação 
			- Generalização 
			- Realização
		- diagramas 
			- diagramas estruturais 
				- Diagrama de classes 
				- Diagrama de componentes 
				- Diagrama de objetos 
				- Diagrama de estruturas compostas 
				- Diagrama de implantação 
				- Diagrama de pacote 
				- Profile diagram
			- diagramas comportamentais 
				- Diagrama de atividades 
				- Diagrama de casos de uso 
				- Diagrama máquina de estados 
				- diagramas de interação 
					- Diagrama de sequências 
					- Diagrama de visão geral da interação
					- Diagrama de comunicações 
					- Diagrama de temporização 
	- as **regras** que determinam **como esses blocos poderão ser combinados** 
	- alguns **mecanismos** comuns aplicados na UML
		- Especificações 
		- Adornos 
		- Divisões comuns 
			- classe/ objeto 
			- interface/ implementação 
		- Mecanismos de extensão 
			- Estereótipos  
			- Valores atribuídos  
			- Restrições


### 4.5.2. Elementos UML

### 4.5.3. Itens estruturais 

Substantivos, partes mais estáticas do modelo, representando elementos conceituais ou físicos, coletivamente são chamados **classificadores**.

**ELEMENTOS BÁSICOS** 

**Classes** são descrições de conjuntos de objetos que compartilham os mesmos atributos, operações, relacionamentos e semântica. Classes implementam uma ou mais interfaces. Graficamente, as classes são representadas por retângulos, geralmente incluindo seu nome, atributos e operações.

[[2006 uml-guia-do-usuario-grady-booch.pdf#page=350|2006 uml-guia-do-usuario-grady-booch]]



Todos os objetos de uma classe têm o mesmo tipo de **estado** e o mesmo tipo de **comportamento**.

**cartões CRC**: Classe, Responsabilidade, Colaboração 

**Interface** é uma coleção de operações que especificam serviços de uma classe ou componente. Portanto, uma interface descreve o comportamento externamente visível desse elemento. Uma interface poderá representar todo o comportamento de uma classe ou componente, como também apenas parte desse comportamento. A interface define um conjunto de especificações de operações (suas assinaturas), mas nunca um conjunto de implementações de operações.

**Colaborações** definem interações e são sociedades de papéis e outros elementos que funcionam em conjunto para proporcionar um comportamento cooperativo superior à soma de todos os elementos. Portanto, as colaborações contêm dimensões estruturais, assim como comportamentais.

**Caso de uso** é a descrição de sequências de ações realizadas pelo sistema que proporciona resultados observáveis de valor para um determinado ator. Um caso de uso é utilizado para estruturar o comportamento de itens em um modelo. Um caso de uso é realizado por uma colaboração.

**Classes ativas** são classes cujos objetos têm um ou mais processos ou threads e, portanto, podem iniciar a atividade de controle. Uma classe ativa é semelhante a uma classe, exceto pelo fato de que seus objetos representam elementos cujo comportamento é concorrente com o de outros elementos.

**Componentes** são partes modulares de um sistema, que ocultam a sua implementação atrás de um conjunto de interfaces externas. Em um sistema, os componentes que compartilham as mesmas interfaces podem ser substituídos ao mesmo tempo em que preservam o mesmo comportamento lógico.

**Artefato** é uma peça física substituível de um sistema que contém informações físicas (“bits”). Em um sistema, você encontrará diferentes tipos de artefatos de implantação, como arquivos de código-fonte, executáveis e scripts. Um artefato normalmente representa a embalagem física da fonte ou as informações de tempo de execução.

**Nó** é um elemento físico existente em tempo de execução que representa um recurso computacional, geralmente com pelo menos alguma memória e, frequentemente, capacidade de processamento. Um conjunto de componentes poderá estar contido em um nó e também poderá migrar de um nó para outro.

Variações dos elementos básicos: atores, sinais e utilitários (tipos de classes);
processos e threads (tipos de classes ativas); e aplicações, documentos, arquivos, bibliotecas, páginas e tabelas (tipos de artefatos).

### 4.5.4. itens comportamentais 

São as partes dinâmicas dos modelos de UML. São os verbos de um modelo, representando comportamentos no tempo e no espaço.

**Interação** é um comportamento que abrange um conjunto de mensagens trocadas entre um conjunto de objetos em determinado contexto para a realização de propósitos específicos. O comportamento de uma sociedade de objetos ou de uma operação individual poderá ser especificado por meio de uma interação. As interações envolvem outros elementos, inclusive mensagens, ações e ligações (as conexões entre os objetos).

**Máquina de estado** é um comportamento que especifica as sequências de estados pelas quais objetos ou interações passam durante sua existência em resposta a eventos, bem como suas respostas a esses eventos. O comportamento de uma classe individual ou de uma colaboração de classes pode ser especificado por meio de uma máquina de estados. Uma máquina de estado abrange outros elementos, incluindo estados, transições (o fluxo de um estado a outro), eventos (itens que disparam uma transição) e atividades (as respostas às transições).

**Atividade** é um comportamento que especifica a sequência de etapas que um processo computacional realiza. Em uma interação, o foco está no conjunto de objetos que interage. Em uma máquina de estado, o foco é no ciclo de vida de um objeto por vez. Em uma atividade, o foco está nos fluxos entre as etapas, independente de qual objeto realiza cada etapa. Uma etapa de uma atividade é chamada de ação.

### 4.5.5. itens de agrupamento

São as partes organizacionais dos modelos de UML. São os blocos em que os modelos podem ser decompostos.

**Pacote** é um mecanismo de propósito geral para a organização do próprio projeto, ao contrário das classes, que organizam os construtos de implementação. Os itens estruturais, os itens comportamentais e até outros itens de grupos podem ser colocados em pacotes. Ao contrário dos componentes (que existem em tempo de execução), um pacote é puramente conceitual (o que significa que existe apenas em tempo de desenvolvimento). Também existem variações, como frameworks, modelos e subsistemas (tipos de pacotes).

### 4.5.6. itens anotacionais 

São as partes explicativas dos modelos de UML. São comentários, incluídos para descrever, esclarecer e fazer alguma observação sobre qualquer elemento do modelo.

**Nota** é apenas um símbolo para representar restrições e comentários anexados a um elemento ou a uma coleção de elementos.

### 4.5.7. relacionamentos 

**Dependência** é um relacionamento semântico entre dois itens, nos quais a alteração de um (o item independente) pode afetar a semântica do outro (o item dependente).

**Associação** é um relacionamento estrutural entre classes que descreve um conjunto de ligações, em que as ligações são conexões entre objetos que são instâncias das classes. A agregação é um tipo especial de associação, representando um relacionamento estrutural entre o todo e suas partes.

**Generalização** é um relacionamento de especialização/generalização, no qual os objetos dos elementos especializados (os filhos) são substituíveis por objetos do elemento generalizado (os pais). Dessa maneira, os filhos compartilham a estrutura e o comportamento dos pais.

**Realização** é um relacionamento semântico entre classificadores, em que um classificador especifica um contrato que outro classificador garante executar. Os relacionamentos de realizações serão encontrados em dois locais: entre interfaces e as classes ou componentes que as realizam; e entre casos de uso e as colaborações que os realizam.

### 4.5.8. diagramas UML

- diagramas estruturais 
	- Profile Diagram - Packages
	- Package Diagram - Packages
	- Class Diagram - Structured Classifiers
	- Composite Structure Diagram - Structured Classifiers
	- Component Diagram - Structured Classifiers
	- Object Diagram - Classification
	- Deployment diagram - Deployments
- diagramas comportamentais 
	- Activity Diagram - Activities ([exemplo1](https://unbarqdsw2021-1.github.io/2021.1_G6_Curumim/modelagem/modelagem-dinamica/diagrama-de-atividades/), [exemplo2](https://www.ibm.com/docs/pt-br/rsas/7.5.0?topic=diagrams-activity))
	- Interaction diagrams 
		- Sequence Diagram - Interactions
		- Communication Diagram - Interactions
		- Interaction Overview Diagram - Interactions
		- Timing Diagram - Interactions
	- Use Case Diagram - Use Cases ([exemplo](https://www-uml--diagrams-org.translate.goog/use-case-diagrams.html?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc))
	- State Machine Diagram - State Machines

### 4.5.9. regras UML

Regras semânticas para [Nomes, Escopo, Visibilidade, Integridade, Execução]

### 4.5.10. mecanismos básicos  

**Especificações** da UML fornecem um repertório semântico, contendo todas as partes de todos os modelos de determinado sistema, cada parte relacionada às demais de uma forma consistente. Assim, os diagramas da UML são apenas projeções visuais a partir desse repertório, cada diagrama revelando um aspecto interessante específico do sistema.

**Adornos**. Em sua maioria, os elementos da UML têm uma notação gráfica única e direta, que proporciona uma representação visual dos aspectos mais importantes do elemento.

**Mecanismos de extensão**:
- **Estereótipo** amplia o vocabulário da UML, permitindo a criação de novos tipos de blocos de construção que são derivados dos já existentes, mas específicos a determinados problemas.
- **Valor atribuído** estende as propriedades dos blocos de construção da UML, permitindo a criação de novas informações na especificação de um elemento.
- **Restrição** amplia as semânticas dos blocos de construção da UML, permitindo acrescentar novas regras ou modificar as já existentes.



### 4.5.11. [especificação UML](https://www.omg.org/spec/UML/2.5.1/PDF)

1. Scope 
2. Conformance 
3. Normative References 
4. Terms and Definitions 
5. Notational Conventions 
6. Additional Information 
7. Common Structure 
8. Values 
9. Classification 
10. Simple Classifiers 
11. Structured Classifiers 
12. Packages 
13. Common Behavior 
14. State Machines 
15. Activities 
16. Actions 
17. Interactions 
18. User Cases 
19. Deployments 
20. Information Flows 
21. Primitive Types 
22. Standard Profile 


## 4.6. OCL - Object Constraint Language

[omg-doc](https://www.omg.org/spec/OCL/2.3.1/PDF)

### 4.6.1. OCL vs UML 

**O que a OCL tem que a UML não tem?**
UML é visual e descritiva — diagramas de classe, sequência, etc. São intrinsecamente ambíguos: um mesmo diagrama pode ser interpretado de formas diferentes.
OCL é uma linguagem formal e textual que adiciona precisão matemática aos modelos UML sem ambiguidade. Ela permite expressar:
- Invariantes: regras que devem ser sempre verdadeiras numa classe
- Pré-condições: o que deve ser verdade antes de uma operação executar
- Pós-condições: o que deve ser verdade depois da operação executar
Exemplo concreto:
-- UML não consegue expressar isso visualmente:
	context Account::withdraw(amount: Integer)
	pre:  amount > 0 and balance >= amount
	post: balance = balance@pre - amount and
	      result = true
A UML diz "existe uma operação withdraw". A OCL diz "só pode sacar se tiver saldo, e o saldo final tem que ser exato". Sem OCL, essas regras ficam soltas na cabeça do desenvolvedor ou em documentação não executável.

**Como usar OCL para testar resultados?**
A OCL define o "expected result" de forma formal. O fluxo é:
1. No modelo PIM, você anota cada operação com pós‑condições OCL que especificam o resultado esperado
2. Após código gerado (PIM→PSM→código), você transforma essas pós‑condições em assertions de teste
3. O teste executa a função gerada e compara o resultado real contra a pós‑condição OCL
Exemplo do withdraw:
context Account::withdraw(amount: Integer) : Boolean
post:
  -- resultado deve ser true se conseguiu sacar
  result = (balance@pre >= amount) and
  -- saldo final = saldo inicial - amount
  balance = balance@pre - amount
Isso vira um teste unitário:
@Test
void withdraw() {
    Account a = new Account(100.0);
    boolean result = a.withdraw(30.0);
    assertEquals(70.0, a.getBalance(), 0.01);  // pós-condição
    assertTrue(result);                          // pós-condição
}
A diferença do meu texto original: eu disse "testes OCL sobre o modelo pós‑transformação" (verificando o modelo). O correto é "testar os resultados da execução do código gerado contra as pós‑condições OCL" (verificando o output das funções).
OCL para verificação de Design Patterns?
Sim, para os aspectos estruturais. Exemplos:
Singleton — garante que só existe uma instância:
context Singleton inv:
  Singleton.allInstances()->size() = 1
Observer — garante que todo observer está registrado no subject:
context Subject inv:
  observers->forAll(o | o.subject = self)
Composite — garante que um nó folha não tem filhos:
context Leaf inv:
  children->isEmpty()
Mas com limitações: OCL só verifica estrutura estática (multiplicidades, tipos, relacionamentos). Comportamento dinâmico (ex: sequência de chamadas no Observer durante uma notificação) requer simulação ou model checking, que a OCL pura não cobre.


### 4.6.2. Conceito e Objetivo

- **O que é?**
    
    - Linguagem formal e declarativa padrão da OMG para expressar restrições e regras de negócio em modelos UML.
        
- **Sem Efeitos Colaterais (_Side-Effect Free_):**
    
    - É estritamente de **apenas leitura** (_read-only_).
        
    - Não altera o estado do sistema, nem modifica valores de atributos ao ser avaliada.
        
- **Propósito Principal:**
    
    - Eliminar ambiguidades que diagramas visuais (como o Diagrama de Classes) não conseguem expressar sozinhos.
        



### 4.6.3. Tipos de Restrições e Contextos

- **`context`**: Define a qual elemento UML a regra pertence (ex: `context Pessoa`).
    
- **`inv` (Invariante):**
    
    - Regra que deve ser **sempre verdadeira** durante todo o ciclo de vida do objeto.
        
    - _Exemplo:_ `context Pessoa inv: self.idade >= 0`
        
- **`pre` (Pré-condição):**
    
    - Condição que deve ser satisfeita **antes** de executar uma operação.
        
- **`post` (Pós-condição):**
    
    - Condição garantida como verdadeira **após** a execução de uma operação.
        
    - Uso do `@pre`: Referencia o valor de um atributo _antes_ da execução (ex: `saldo = saldo@pre + valor`).
        
- **`init` / `derive` / `body`:**
    
    - `init`: Define o valor inicial de um atributo.
        
    - `derive`: Regra de cálculo/derivação de um atributo derivado.
        
    - `body`: Define o resultado de uma operação de consulta (_query_).
        



### 4.6.4. Tipos de Dados

- **Tipos Primitivos (Básicos):**
    
    - `Boolean`: `true`, `false` (operadores: `and`, `or`, `not`, `implies`, `xor`).
        
    - `Integer`: Números inteiros.
        
    - `Real`: Números decimais.
        
    - `String`: Operações em texto (ex: `.concat()`, `.substring()`).
        
- **Tipos de Coleção (_Collections_):**
    
    - `Set`: Coleção não ordenada sem elementos duplicados.
        
    - `Bag`: Coleção não ordenada que permite elementos duplicados.
        
    - `Sequence`: Coleção ordenada que permite elementos duplicados.
        
    - `OrderedSet`: Coleção ordenada sem elementos duplicados.
        
- **Tipos Especiais:**
    
    - `OclAny`: Tipo pai universal de todos os tipos em OCL.
        
    - `OclVoid` / `OclInvalid`: Representam valores nulos ou erros de avaliação.
        



### 4.6.5. Sintaxe e Operadores de Navegação

- **Navegação Básica:**
    
    - **Ponto (`.`):** Acessa atributos, associações simples e métodos de um objeto (ex: `self.nome`).
        
    - **Seta (`->`):** Aplica operações sobre **coleções** (ex: `self.pedidos->size()`).
        
- **Iteradores de Coleção Frequentes:**
    
    - `->select(condicao)`: Retorna uma subcoleção apenas com elementos que satisfazem a condição.
        
    - `->reject(condicao)`: Oposto do `select` (exclui os elementos que atendem à condição).
        
    - `->collect(expressao)`: Mapeia a coleção para uma nova estrutura/atributo.
        
    - `->forAll(condicao)`: Retorna `true` se **todos** os elementos atenderem à regra.
        
    - `->exists(condicao)`: Retorna `true` se **pelo menos um** elemento atender à regra.
        
    - `->isEmpty()` / `->notEmpty()`: Verifica se a coleção está vazia ou possui elementos.
        
    - `->size()`: Quantidade total de elementos.
        


### 4.6.6. Aplicações no Ecossistema de Software

- **Model-Driven Architecture (MDA / MDE):**
    - Utilizada em engenharia movida a modelos para validação e transformação automática de código.
- **Validação de Modelos:**
	- Verificação estática de consistência em ferramentas como Eclipse OCL, USE (_UML Specification Environment_) e Papyrus.


# 5. use cases

[UDA (Unified Data Architecture) at Netflix](https://netflixtechblog.com/uda-unified-data-architecture-6a6aee261d8d)

## 5.1. [[260916-modelos_semanticos#3. OLD mbse_docs|mbse_docs]]
definições:
- documentos de sistema
- documentos de projeto
- documentos de sessão

### 5.1.1. mapa lógico 
- conceito mbse
- diagrama SysML, UML 


### 5.1.2. pesquisa: Template Markdown: Pipeline de Jornada & Mapeamento Funcional

Se o objetivo é agilidade e alinhamento antes de abrir ferramentas de modelagem (como Cameo, Enterprise Architect ou Draw.io), este template em Markdown funciona como uma ponte direta entre a jornada do usuário e os requisitos/funções do MBSE:

[ Usuário / UI ] ---> [ Regra de Negócio / Função ] ---> [ Persistência / Integração ]

| | |

+-- Ex: Preencher Form +-- Ex: Calcular Imposto e Frete +-- Ex: Salvar Pedido

Markdown

```
## [Nome da Funcionalidade / Jornada]

### 1. Visão de Contexto (ConOps)
* **Objetivo do Usuário:** [O que o cliente quer realizar no final do pipeline?]
* **Ator Principal:** [Perfil do cliente/operador]
* **Gatilho Inicial:** [Evento que dispara a jornada]
* **Resultado Esperado (Pós-condição):** [Estado final do sistema/negócio]



### 2. Backbone da Jornada do Usuário (Pipeline Linha do Tempo)

| Estágio da Jornada | Ação / Passo do Usuário | Entrada do Usuário | Resposta / Saída Esperada | Função do Sistema (Black-Box) |
| :--- | :--- | :--- | :--- | :--- |
| **1. Descoberta** | Seleciona o produto no catálogo | Clique/Busca | Exibição de detalhes e estoque | Buscar metadados do item |
| **2. Intenção** | Adiciona ao carrinho | Qtd, Opções | Confirmação visual no carrinho | Validar disponibilidade |
| **3. Checkout** | Insere dados de pagamento | Cartão, Cupom | Token de autorização | Processar transação financeira |
| **4. Conclusão** | Recebe confirmação | E-mail / Tela | Pedido gerado com ID | Emitir comprovante e notificar |



### 3. Matriz de Amarrações por Camada (Sem Definição de Classes)





### 4. Regras de Negócio e Exceções do Pipeline
* **[RN-01]:** O frete só pode ser calculado se o CEP for válido.
* **[EX-01] Falha no Pagamento:** O sistema deve reter os itens no carrinho por 15 minutos e exibir erro amigável ao usuário.
```

### 5.1.3. pesquisa: Como Conectar Esse Mapa ao Ciclo MBSE

1. **Entrada:** A jornada em formato Markdown serve como entrada para os **Requisitos Funcionais** e o **ConOps**.
2. **Derivação UML/SysML:** Cada _Ação do Usuário_ vira um nó em um **Diagrama de Atividades** de alto nível.
3. **Evolução Arquitetural:** Apenas quando as funções do sistema (_Black-Box_) estiverem validadas no pipeline do cliente é que você faz a alocação dessas funções em blocos/componentes no **SysML Block Definition Diagram (BDD)** ou **Internal Block Diagram (IBD)**.



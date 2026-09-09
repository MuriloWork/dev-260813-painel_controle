[guia.dev](https://guia.dev/pt/guide.html)

# 1. Negócio

O pilar inicial aborda uma questão essencial para desenvolver software que entregue valor. A compreensão do negócio e as definições de produto são o primeiro passo para a construção de qualquer software. Aplicar as boas práticas de engenharia só faz sentido quando o software desenvolvido atende de forma satisfatória as definições de produto. O cliente de uma solução espera que seu negócio seja impactado com o uso da solução, por este motivo tal pilar é tão importante. Sendo assim, antes de pensar em quais tecnologias serão utilizadas é necessário haver certeza de que o time de desenvolvimento possui compreensão do negócio e produto.

# 2. Systems Engineering
## 2.1. [[01-conceitos_software_ontologia|Ontologia]]
## 2.2. [[01-conceitos_software_se|Systems Engineering]]
## 2.3. [[01-conceitos_software_se|MBSE - Model Based Systems Engineering]]
## 2.4. [[260810_learning_ia_skills|IA resources]]

# 3. Arquitetura de Software

O segundo pilar contempla a base para o desenvolvimento de um bom software a médio e longo prazo. A arquitetura vai muito além de diagramas e desenhos técnicos e ela está totalmente associada às definições de produto e do negócio. Defini-la bem requer estratégias que resultem em implementações mais simples e eficazes. Decisões sobre linguagens de programação, frameworks, ferramentas, dentre outros, devem ser realizadas conforme a arquitetura definida e não o contrário para que não limitem alternativas e o poder de inovação.

## 3.1. [Camadas](https://guia.dev/pt/pillars/software-architecture/layers.html)

### 3.1.1. frontend
### 3.1.2. backend
### 3.1.3. dados

sql na **Camada de Dados (Data)**.

#### 3.1.3.1. Onde os arquivos ficam? (Aspecto Estrutural)
Se você está falando dos arquivos `.sql` que criam as *Views* e *Triggers* no SQLite, eles pertencem inquestionavelmente à **Camada de Dados**.

*   **Por quê?** Porque eles são objetos do SGBD (Sistema Gerenciador de Banco de Dados). Eles são escritos em SQL, são executados dentro do motor do banco de dados e são versionados junto com o *schema* do banco (via migrations).
*   **Como organizar no projeto:**
    ```text
    /seu_projeto
      /frontend
      /backend
      /data (ou /database)
         /migrations
         /views        <-- Scripts SQL de criação de views
         /triggers     <-- Scripts SQL de criação de triggers
         /seeds
    ```

---

#### 3.1.3.2. Onde a LÓGICA deve ficar? (Aspecto Arquitetural)
Aqui é onde a maioria dos desenvolvedores comete erros. Embora os *arquivos* fiquem na camada de dados, **o que eles fazem** dita se eles deveriam sequer existir.

##### 3.1.3.2.1. Sobre VIEWS (Visões)
*   **Veredito:** **Excelente para a Camada de Dados.**
*   **Motivo:** Views não possuem "lógica de negócio" mutável, elas são apenas *consultas salvas* (atalhos de leitura). Usar Views no SQLite para agregar dados, fazer joins complexos ou mascarar colunas sensíveis é uma ótima prática. O Backend apenas lê a View como se fosse uma tabela simples.

##### 3.1.3.2.2. Sobre TRIGGERS (Gatilhos)
*   **Veredito:** **Cuidado! Geralmente é um "Code Smell" (mau cheiro) se usado para regra de negócio.**
*   **Motivo:** Triggers executam *lógica procedural* (ex: "SE o estoque for menor que 0, ENTÃO atualize a tabela de alertas"). Se você coloca regra de negócio dentro de uma Trigger no SQLite, você está **vazando a responsabilidade do Backend para a Camada de Dados**.
*   **O problema disso:**
    1.  **Invisibilidade:** O desenvolvedor Backend lê o código da API e não entende por que um campo foi alterado, pois a mágica aconteceu "por baixo dos panos" no banco.
    2.  **Acoplamento:** Se um dia você migrar do SQLite para o PostgreSQL, terá que reescrever toda a lógica procedural (PL/pgSQL é diferente de SQL puro).
    3.  **Testabilidade:** É muito difícil testar triggers com testes unitários na camada de Backend.

**Quando usar Triggers na Camada de Dados?**
Apenas para coisas que são **exigência intrínseca do banco de dados**, como:
*   Logs de auditoria (histórico de quem alterou o quê e quando).
*   Atualização de campos de `updated_at` automaticamente.
*   Integridade referencial complexa que o SGBD não resolve com *Foreign Keys* padrão.

---

#### 3.1.3.3. E se os "Scripts" forem códigos Python/Node/Go?
Se por "scripts de única responsabilidade de transformação" você não está falando de SQL, mas sim de arquivos `.py`, `.js` ou `.go` que pegam dados brutos, transformam e salvam (processos de ETL, batch jobs, ou cron jobs):

*   **Se rodam sob demanda via API:** Pertencem ao **Backend** (geralmente em um subdomínio de *Services* ou *UseCases*).
*   **Se rodam em segundo plano/agendados:** Pertencem ao **Backend** (em uma camada de *Workers*, *Background Jobs* ou *Consumers*).

---

#### 3.1.3.4. Resumo da Regra de Ouro (Separação de Responsabilidades)

Para manter sua arquitetura `[Frontend, Backend, Data]` saudável, siga esta filosofia:

1.  **Camada de Dados (Data):** É "burra". Ela apenas **persiste, recupera e garante integridade estrutural**. Ela sabe *como* salvar (SQL, índices, views de leitura), mas não sabe *por que* está salvando.
2.  **Camada de Backend:** É o "cérebro". Ela contém a **Regra de Negócio e a Lógica de Transformação**. Ela decide *o que* fazer com os dados antes de mandar para a camada de Dados.

**Conclusão para o seu caso:**
Mantenha os arquivos de criação de **Views e Triggers dentro da pasta da Camada de Dados** (junto com suas migrations). Porém, **evite ao máximo usar Triggers para transformar dados ou aplicar regras de negócio**; prefira fazer essa transformação no código do Backend antes de enviar o `INSERT/UPDATE` para o SQLite.

### 3.1.4. arquiteturas de dados

[banco de dados de grafos - oracle](https://www.oracle.com/br/autonomous-database/what-is-graph-database/)


## 3.2. [Camadas e Padrões de Arquitetura](https://guia.dev/pt/pillars/software-architecture/layers-and-architecture-patterns.html)



Arquitetura SOLID:  
	- SRP - Single Responsbility Principle (Responsabilidade Única)
		- Uma classe deve ter um, e somente um, motivo para mudar. Ela deve ser especializada em um único assunto e possuir apenas uma única responsabilidade dentro do seu software.
	- OCP - Open Closed Principle (Aberto Fechado)
		- Suas camadas de domínio e casos de uso devem ser abertas para extensão, mas fechadas para modificação. Você adiciona novas regras ou integrações criando novos componentes, sem alterar o código central que já funciona
	- LSP - Liskov Substitution Principle (Substituição de Liskov)
		- Classes derivadas devem poder ser substitutas de suas classes base
	- ISP - Interface Segregation Principle (Segregação de Interfaces)
		- Interfaces específicas são melhores do que uma interface única e genérica. As camadas da Clean Architecture comunicam-se através de contratos enxutos, forçando o baixo acoplamento.
	- DIP - Dependence Inversion Principle (Inversão de Dependências)
		- Módulos de alto nível (regras de negócio) não devem depender de módulos de baixo nível (banco de dados, frameworks); ambos devem depender de abstrações. As dependências sempre apontam para dentro, em direção ao domínio.


### 3.2.1. UML reverse engineering 

Ferramentas open source baseadas nos conceitos da OMG incluem o Pyreverse e [Clang-UML](https://github.com/bkryza/clang-uml) para engenharia reversa, além do Modelio e Eclipse Papyrus, que oferecem simulação e execução de modelos UML. Para geração de código a partir de modelos executáveis ([xtUML](https://xtuml.org/)), a ferramenta de referência é o BridgePoint. Para mais detalhes sobre ferramentas de modelagem, visite [Modeling Languages](https://modeling-languages.com/uml-tools/).

[executable-uml](https://github.com/topics/executable-uml)


## 3.3. [Documentação Técnica](https://guia.dev/pt/pillars/software-architecture/technical-documentation.html)

- Artefatos de documentação:
	-  Requisitos 
	- Arquitetura  
	- Projeto  
	- Código-fonte  
	- Planos do projeto  
	- Testes  
	- Protótipos  
	- Versões


## 3.4. [Desenho Técnico](https://guia.dev/pt/pillars/software-architecture/technical-drawing.html)

# 4. Linguagens e Ferramentas

O terceiro pilar orienta a escolha da linguagem de programação e ferramentas que suportem a arquitetura definida. Essa escolha pode ser difícil, muitas vezes é feita considerando o que o time já conhece e embora esse seja um fator realmente importante ele não deve ser prioritário. A arquitetura deve ser o fator de maior peso, pois as escolhas neste pilar devem viabilizar a implementação da arquitetura proposta.


# 5. Código Fonte

O quarto pilar é o mais relacionado ao dia a dia de desenvolvedores(as), pois todo software resulta de um conjunto de código escrito para atender uma necessidade de negócio. Normalmente o primeiro aspecto de qualidade de um código é atender ao negócio, as definições de produto e de arquitetura. Quando isso não ocorre, há uma grande tendência de que o código seja refeito em curto prazo. Além destas questões um bom código deve ser legível e extensível, qualquer desenvolvedor(a) deve ser capaz de compreendê-lo e mesmo que um código atenda o negócio e siga a arquitetura definida, quando não é compreensível e não respeita boas práticas ele se torna um detrator de performance do time, culminando muitas vezes no principal limitador de evolução do software e da solução de negócio.

## 5.1. [Gerenciamento de Projetos com Código Fonte](https://guia.dev/pt/pillars/source-code/source-code-management.html)

## 5.2. [Organização de Código Fonte](https://guia.dev/pt/pillars/source-code/source-code-organization.html)

### 5.2.1. Diretórios

- Código da aplicação;
- Código de testes da aplicação;
- Artefatos oriundos da construção do projeto;
- Pacotes que serão publicados;
- Arquivos de configuração para construção e execução da aplicação.
- Scripts e/ou Binários executáveis;
- Documentação.

### 5.2.2. Padrões de Projeto

#### 5.2.2.1. As 3 categorias principais

A referência mais famosa e fundamental sobre o tema é o livro de 1994, **"Design Patterns: Elements of Reusable Object-Oriented Software"**.

Por terem sido escritos por quatro autores (Erich Gamma, Richard Helm, Ralph Johnson e John Vlissides), eles ficaram conhecidos como a **Gang of Four (GoF)**.

Por isso, é muito comum ouvir a expressão " **Quais são os padrões GoF?**".

Neste livro, eles catalogaram 23 padrões clássicos, divididos em três categorias principais, de acordo com o tipo de problema que resolvem.

Vamos explorar cada uma delas com exemplos.

#### 5.2.2.2. Padrões criacionais (creational patterns)

Esses padrões lidam com os mecanismos de **criação de objetos**. Eles tentam criar objetos de uma maneira adequada para a situação, tornando o sistema mais flexível e independente de como seus objetos são criados, compostos e representados.
- Prototype
##### 5.2.2.2.1. Singleton Design Pattern

Este é um dos padrões mais conhecidos (e às vezes controverso). O singleton design pattern garante que uma classe tenha **apenas uma instância** e fornece um ponto de acesso global para ela.

- **Problema:** Você precisa ter exatamente um objeto de um tipo em todo o sistema. Por exemplo, uma classe que gerencia a conexão com um banco de dados ou as configurações de uma aplicação.
- **Solução:** A classe se torna responsável por criar sua própria instância e garante que nenhuma outra instância seja criada.

##### 5.2.2.2.2. ==Factory/ Abstract Factory== Method

Define uma interface para criar um objeto, mas deixa as subclasses decidirem qual classe instanciar.

- **Problema:** Você tem uma classe que não pode antecipar o tipo de objetos que precisa criar. Imagine um aplicativo de logística que precisa criar objetos Transporte — pode ser um Caminhao, um Navio ou um Aviao.
- **Solução:** Você cria um método "fábrica" que é implementado pelas subclasses (FabricaDeCaminhoes, FabricaDeNavios), cada uma retornando o objeto de transporte correto.

##### 5.2.2.2.3. Builder

Permite construir objetos complexos passo a passo. O padrão permite que você produza diferentes tipos e representações de um objeto usando o mesmo código de construção.

- **Problema:** Você precisa criar um objeto com muitos campos de configuração (alguns obrigatórios, outros opcionais), e um construtor com uma lista gigante de parâmetros seria impraticável.
- **Solução:** Você cria um objeto Builder que recebe as configurações passo a passo (.comNome("X"),.comEndereco("Y")) e, ao final, chama um método.build() para retornar o objeto final, devidamente configurado.

#### 5.2.2.3. Padrões estruturais (structural patterns)

Esses padrões explicam **como montar objetos e classes** em estruturas maiores, mantendo a flexibilidade e a eficiência da estrutura. Eles se concentram em como as classes e objetos são compostos para formar estruturas maiores e mais complexas.
- Composite
- Bridge
- Flyweight 
- Proxy 
##### 5.2.2.3.1. Adapter

Permite que objetos com interfaces incompatíveis colaborem. É como um adaptador de tomada que permite que um plugue europeu funcione em uma tomada brasileira.

- **Problema:** Você precisa usar uma classe de uma biblioteca externa, mas a interface dela não é compatível com o resto do seu código.
- **Solução:** Você cria uma classe "adaptadora" que "envolve" o objeto incompatível e expõe uma interface que seu sistema entende.

##### 5.2.2.3.2. Decorator

Permite adicionar novos comportamentos a objetos dinamicamente, colocando-os dentro de objetos "envoltórios" especiais que contêm os comportamentos.

- **Problema:** Você quer adicionar responsabilidades extras a um objeto sem alterar sua classe. Imagine uma cafeteria onde você pode ter um café simples, um café com leite, um café com leite e chocolate, etc.
- **Solução:** Você "decora" o objeto Cafe base com um DecoradorDeLeite e, em seguida, com um DecoradorDeChocolate, adicionando funcionalidades e custos em camadas.

##### 5.2.2.3.3. Facade

Fornece uma interface simplificada para uma biblioteca, um framework ou qualquer outro conjunto complexo de classes.

- **Problema:** Você está trabalhando com um subsistema complexo que tem dezenas de classes e objetos que precisam ser inicializados e coordenados para realizar uma tarefa.
- **Solução:** Você cria uma classe Facade (Fachada) que esconde toda essa complexidade interna e oferece alguns métodos simples para o cliente utilizar (ex: iniciarSistema(), desligarSistema()).

#### 5.2.2.4. Padrões comportamentais (behavioral patterns)

Esses padrões se concentram nos algoritmos e na **atribuição de responsabilidades** entre os objetos. Eles descrevem não apenas padrões de objetos ou classes, mas também padrões de comunicação entre eles.
- Template Method
- ==Command== 
- Interpreter
- Iterator
- Mediator
- Memento
- ==State==
- Visitor 

##### 5.2.2.4.1. ==Strategy==

Permite definir uma família de algoritmos, colocar cada um deles em uma classe separada e tornar seus objetos intercambiáveis.

- **Problema:** Você tem uma tarefa que pode ser executada de várias maneiras diferentes. Por exemplo, calcular uma rota em um aplicativo de mapas pode usar a estratégia "caminho mais rápido", "caminho mais curto" ou "caminho sem pedágios".
- **Solução:** Você define uma interface EstrategiaDeRota e cria classes concretas (RotaRapida, RotaCurta). O objeto principal (o Mapa) pode trocar de estratégia dinamicamente, sem alterar seu próprio código.

##### 5.2.2.4.2. ==Observer==

Permite definir um mecanismo de assinatura para notificar múltiplos objetos sobre quaisquer eventos que aconteçam com o objeto que eles estão observando.

- **Problema:** Você tem um objeto (o "sujeito") cujo estado muda, e vários outros objetos (os "observadores") precisam ser notificados sobre essa mudança. Pense em uma planilha: quando você muda o valor de uma célula, todos os gráficos que dependem dela são atualizados automaticamente.
- **Solução:** Os observadores se "inscrevem" no sujeito. Quando o estado do sujeito muda, ele percorre sua lista de observadores e chama um método de notificação em cada um deles.

##### 5.2.2.4.3. Chain of responsibility

Permite passar requisições ao longo de uma cadeia de manipuladores. Ao receber uma requisição, cada manipulador decide se processa a requisição ou se a passa para o próximo manipulador na cadeia.

- **Problema:** Você tem uma série de verificações a serem feitas em uma requisição, como um sistema de aprovação de despesas: um gestor pode aprovar até R500,umdiretorateˊR5.000, e o CEO aprova valores maiores.
- **Solução:** Você cria uma "corrente" de objetos (gestor -> diretor -> CEO). A requisição de despesa é passada ao primeiro elo. Se ele não puder aprová-la, passa para o próximo, e assim por diante.


### 5.2.3. diagramas OMT - Object Modeling Technique
UML - Unified Modeling Language

# 6. Documentos e Dados

## 6.1. [[260819-modelo_repositorios#6. Análise de Formatos de Documentos para Agentes de IA|Análise de Formatos de Documentos para Agentes de IA]]

# 7. Integração Contínua

Integração contínua vai além de utilizar uma ferramenta que automatiza tarefas. Em um processo moderno e eficiente de desenvolvimento, uma das questões mais relevantes é o momento de mesclagem do código. Quanto maior o time, número de alterações e integrações entre sistemas, maior é a chance de haver conflitos e falhas durante essa etapa podendo afetar a cadência de times e baixar a qualidade de entregas. O quinto pilar trata os conceitos e boas práticas relacionadas a integração contínua, considerando ferramentas de CI apenas como um meio de automatizar o processo de integrar código continuamente.


# 8. Entrega Contínua

Um momento muito aguardado no desenvolvimento de um software é a sua entrega e atualmente em um processo moderno e eficiente a forma de organizar tais entregas vem passando por várias mudanças. O sexto pilar aborda as estratégias e boas práticas que viabilizam a entrega contínua de software, o que inclui o processo de implantação contínua do mesmo e como os pilares de negócio, arquitetura e integração contínua influenciam na periodicidade e capacidade de entregar e implantar continuamente softwares.



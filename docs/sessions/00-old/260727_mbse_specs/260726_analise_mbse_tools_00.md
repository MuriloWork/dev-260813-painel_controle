# 1. **Pesquisa Comparativa de Ferramentas MBSE: Eclipse Papyrus, Modelio e Gaphor (V2)**

A Engenharia de Sistemas Baseada em Modelos (*Model-Based Systems Engineering \- MBSE*) é uma abordagem formalizada para apoiar a especificação, design, análise, verificação e validação de sistemas complexos ao longo de todo o seu ciclo de vida. Em vez de documentos textuais isolados, o MBSE utiliza modelos conceituais padronizados — principalmente embasados em notações como **SysML (Systems Modeling Language)** e **UML (Unified Modeling Language)**.

Esta versão (V2) do documento expande a análise comparativa das três ferramentas de código aberto (**Eclipse Papyrus**, **Modelio** e **Gaphor**), introduzindo o mapeamento de persitência/bancos de dados e diretrizes de integração no fluxo de engenharia de software.

## 1.1. Introdução ao Contexto das Ferramentas MBSE

As ferramentas de modelagem desempenham um papel central na transição de processos tradicionais baseados em documentos para ecossistemas orientados a modelos. O objetivo central de uma ferramenta MBSE é fornecer suporte visual e semântico consistente para expressar requisitos, arquitetura estrutural, comportamentos dinâmicos e restrições paramétricas do sistema.

**Principais Aspectos Avaliados em Ferramentas MBSE:**

* **Conformidade com Padrões OMG:** Suporte rigoroso a SysML e UML.  
* **Rastreabilidade de Requisitos:** Capacidade de vincular necessidades a blocos estruturais e testes de verificação.  
* **Modelos de Armazenamento e Persistência:** Como os dados do metamodelo são estruturados no disco/repositório.  
* **Integração ao Fluxo de Software:** Adequação para fluxos de especificação e desenvolvimento ágil ou tradicional.

- lista de ferramentas para pesquisa
	- Eclipse foundation 
		- [Eclipse Papyrus](https://eclipse.dev/papyrus/)
		- [Epsilon Model Connectivity Layer](https://eclipse.dev/epsilon/doc/emc/)
	- [Modelio](https://github.com/ModelioOpenSource/Modelio)
	- [Gaphor](https://github.com/gaphor/gaphor)
	- [UML tools for Python](https://modeling-languages.com/uml-tools/#:~:text=tools%20satisfy%20them.-,UML%20tools%20for%20Python,-Are%20UML%20tools)
	- [BESSER Web Modeling Editor](https://github.com/BESSER-PEARL/BESSER-Web-Modeling-Editor#besser-web-modeling-editor)
	- [Sirius](https://modeling-languages.com/sirius-eclipse-obeo-graphical-modeling-tool/)
	- [mendix](https://www.mendix.com/)
	- [MoTxT](https://marketplace.visualstudio.com/items?itemName=csui-rse-lab.motxt)


## 1.2. Análise Detalhada das Ferramentas

### 1.2.1. **2.1 Eclipse Papyrus**

O **Eclipse Papyrus** é uma das ferramentas de modelagem industrial e acadêmica mais robustas do ecossistema de código aberto. Desenvolvido no âmbito da Eclipse Foundation, o Papyrus fornece um ambiente completo para Engenharia Orientada a Modelos (MDE) e MBSE.

* **Padrões e Notações:** Oferece suporte completo ao UML 2.5 e SysML 1.6, incluindo suporte a perfis customizados (DSMLs) e notações avançadas como MARTE.  
* **Recursos de MBSE:** Matrizes de alocação de requisitos, diagramas paramétricos, execução/simulação comportamental com Moka e customização de telas via Eclipse Sirius.  
* **Pontos Fortes:** Extremamente extensível, rico em recursos, padrões rigorosos e forte integração com o ecossistema Eclipse.  
* **Desafios:** Alta complexidade de configuração e curva de aprendizado íngreme.

### 1.2.2. **2.2 Modelio**

O **Modelio** é uma ferramenta de modelagem flexível desenvolvida com foco no suporte a UML, BPMN e SysML. O projeto oferece edições abertas (open-source) e ecossistema extensível por módulos.

* **Padrões e Notações:** Suporta UML 2, SysML (módulo SysML Architect) e BPMN para processos de negócios.  
* **Recursos de MBSE:** Gerenciamento/rastreabilidade de requisitos, geração automatizada de documentação e suporte a extensões em Jython/Python e Java.  
* **Pontos Fortes:** Interface acessível, integração equilibrada entre UML e BPMN, e boa organização do repositório.  
* **Desafios:** Recursos avançados de simulação e suporte colaborativo de grande porte estão em módulos avançados.

### 1.2.3. **2.3 Gaphor**

O **Gaphor** é uma ferramenta moderna, leve e multiplataforma desenvolvida em Python e GTK. Foi projetado para ser intuitivo e direto, mantendo conformidade semântica com UML 2 e SysML.

* **Padrões e Notações:** Suporta UML 2, SysML, RAAML e o modelo C4 para arquitetura de software.  
* **Recursos de MBSE:** Design focado em diagramas, suporte a BDD, IBD e diagramas de Requisitos do SysML, e integração nativa com ecossistemas Python.  
* **Pontos Fortes:** Início imediato, baixo consumo de recursos, código 100% aberto e excelente usabilidade.  
* **Desafios:** Não possui mecanismos nativos de simulação de modelos complexos (como fUML).

## 1.3. Modelos de Bancos de Dados e Persistência de Dados

Cada ferramenta adota uma estratégia distinta para o armazenamento e gerenciamento do metamodelo, o que afeta diretamente o controle de versão, colaboração e performance em grandes projetos:

| Ferramenta | Modelo de Persistência / Banco de Dados | Formato de Arquivo Principal | Comportamento com Controle de Versão (Git/SVN)   |
| :---- | :---- | :---- | :---- |
| **Eclipse Papyrus** | **EMF (Eclipse Modeling Framework) / XMI** O metamodelo é salvo em arquivos XMI estruturados em nós relacionais XML. Pode utilizar persistência em banco de dados em grafos/relacional via extensões EMF Store ou CDO (Connected Data Objects). | .uml, .notation, .di | Exige ferramentas específicas de merge estrutural (como EMF Compare) devido à verbosidade do XMI em commits paralelos. |
| **Modelio** | **H2 Database / Repositório Orientado a Objetos** Utiliza internamente o banco de dados embutido H2 para o repositório local e gerenciamento de transações de modelo. Projetos complexos sincronizam via servidor de modelos. | .exml / Arquivos de banco local H2 em diretórios de projeto | Bom isolamento de componentes, mas o merge direto em arquivos binários/banco de dados exige exportação/importação no nível de módulo. |
| **Gaphor** | **XML Orientado a Grafos Leves (Data-centric XML)** Armazena o modelo conceitual em um formato XML simples e human-readable, onde os elementos do modelo e itens visuais possuem IDs únicos persistentes. | .gaphor (XML plano) | Altamente amigável ao Git. Conflitos de mesclagem podem ser inspecionados e resolvidos diretamente em editores de texto. |

## 1.4. Recomendações para Uso no Fluxo de Criação de Especificações de Software

A engenharia de software moderna exige um fluxo fluido entre a concepção do sistema, a especificação dos requisitos e a implementação do código. A seguir estão as recomendações de adoção por tipo de fluxo de trabalho:

### 1.4.1. **4.1 Fluxo Ágil / Orientado a microsserviços e APIs (Gaphor)**

* **Aplicação Ideal:** Especificação rápida de arquiteturas de software, mapeamento C4 e diagramas de domínio.  
* **Recomendação de Uso:** Integre o Gaphor no repositório do código fonte (Docs-as-Code). Os arquivos .gaphor e exportações de imagem podem residir na pasta /docs do projeto de software. Testes automatizados via CI/CD podem garantir que os modelos Python não possuem dependências quebradas.

### 1.4.2. **4.2 Fluxo Híbrido / Engenharia de Requisitos com Regras de Negócio (Modelio)**

* **Aplicação Ideal:** Sistemas corporativos, especificações funcionais pesadas e rastreabilidade entre processos de negócio (BPMN) e software (UML).  
* **Recomendação de Uso:** Utilizar o Modelio no início da fase de especificação para capturar requisitos funcionais e mapear processos de negócio. Exporte especificações em PDF/HTML para validação com clientes não técnicos antes do início do desenvolvimento.

### 1.4.3. **4.3 Fluxo Crítico / Engenharia de Sistemas de Alta Complexidade (Eclipse Papyrus)**

* **Aplicação Ideal:** Sistemas embarcados, dispositivos médicos, setor aeroespacial e automotivo (onde o software interage com hardware pesado).  
* **Recomendação de Uso:** Adote o Papyrus em pipelines estritos de engenharia de sistemas. Utilize diagramas SysML para rastrear requisitos de sistema até o software, aplique Moka para simular estados do sistema antes da codificação e use engenharia reversa para manter os modelos UML sincronizados com código Java/C++.

## 1.5. Tabela Comparativa Geral

| Critério | Eclipse Papyrus | Modelio | Gaphor   |
| :---- | :---- | :---- | :---- |
| **Licença** | Eclipse Public License (EPL) | GPL / Apache (Core Open Source) | Apache License 2.0 |
| **Linguagens Suportadas** | UML 2.5, SysML 1.6, MARTE, Perfis customizados | UML 2, SysML, BPMN | UML 2, SysML, RAAML, C4 |
| **Modelo de Banco/Persistência** | EMF / XMI / CDO Repository | H2 Database / EXML | XML Plano orientado a grafos |
| **Compatibilidade com Git** | Requer EMF Compare | Requer gestão por módulos/exportação | Nativa e amigável (Diff textual) |
| **Usabilidade** | Complexa (Exige treinamento) | Moderada (Interface estruturada) | Simples e Intuitiva |
| **Perfil no Fluxo de Software** | Sistemas críticos / Embedded / MBSE completo | Sistemas corporativos e BPMN \+ UML | Arquitetura ágil / Docs-as-Code / C4 |

## 1.6. Conclusão e Recomendações de Adoção

1. **Eclipse Papyrus:** Indicado se o ciclo de vida do software exigir rastreabilidade rigorosa de padrões MBSE industriais, validação paramétrica e execução de modelos.  
2. **Modelio:** Indicado se a especificação do software depender fortemente de processos de negócio preexistentes e alinhamento com stakeholders de análise de negócios.  
3. **Gaphor:** Indicado se o foco for velocidade de documentação, simplicidade na manutenção dentro de repositórios Git de projetos ágeis.

# 2. nova

**Análise de Ferramentas MBSE - Foco Gaphor & Gerenciamento de Mídias Sociais**

**Identificador do Documento:** 260726\_analise\_mbse\_tools\_03  
**Escopo do Projeto:** Sistema de Gerenciamento de Conteúdo de Mídias Sociais (Meta, Google Ads/YouTube, TikTok)  
**Ferramenta Selecionada para Adoção Inicial:** Gaphor

## 2.1. Contexto Geral e Mapeamento do Gaphor

Nas revisões anteriores, analisou-se o panorama de ferramentas de MBSE (Eclipse Papyrus, Modelio e Gaphor). O **Gaphor** destacou-se pela leveza, facilidade de integração em fluxos ágeis de engenharia de software e compatibilidade nativa com controle de versão (Git/Docs-as-Code).

### 2.1.1. Características do Gaphor

* **Notações Suportadas:** UML 2, SysML, RAAML e C4 Model.  
* **Modelo de Persistência:** XML plano orientado a grafos lecionáveis por editores de texto (data-centric XML) armazenado em arquivos com extensão .gaphor.  
* **Controle de Versão:** Excelente integração com Git; permite verificação visual de diffs textuais sem necessidade de engines pesadas de merge de metamodelos.  
* **Usabilidade:** Interface GTK/Python fluida, sem a sobrecarga de ambientes RCP pesados.

## 2.2. Contexto do Sistema: Gerenciamento de Mídias Sociais (Meta, Google, TikTok)

O sistema em desenvolvimento trata da gestão e publicação automatizada de conteúdo em múltiplas redes sociais (Meta/Instagram/Facebook, Google/YouTube, TikTok). Este tipo de sistema possui características específicas:

* **Integração com APIs Heterogêneas:** Cada plataforma (Meta Graph API, Google People/YouTube API, TikTok Business API) exige esquemas de autenticação (OAuth2/Tokens), taxas de limite (rate limits) e estruturas de payloads distintas.  
* **Modelagem de Dados e Arquitetura de Código:** Exige desacoplamento entre os serviços de API, camadas de persistência (armazenamento de agendamentos, tokens, métricas) e interfaces de usuário.

## 2.3. Adequação do Gaphor para Especificação de Arquitetura de Código, Dados e Engenharia Reversa

Para que o Gaphor atenda com precisão a modelagem do sistema de mídias sociais e permita automações como \*\*engenharia reversa\*\* e \*\*geração de código\*\*, é necessário estabelecer estratégias claras de uso:

### 2.3.1. Definição Precisa da Arquitetura de Código e Dados no Gaphor

* **Arquitetura de Dados (Modelagem ER e Entidades):**  
  * Utilize os **Class Diagrams (UML)** no Gaphor com tipos de dados explícitos para definir o modelo de dados (ex: IDs de postagem, tokens de autenticação, timestamps e enums de status).  
  * Aplique o nível de detalhamento de atributos e métodos (com visibilidades \+public, \-private, \#protected e protótipos de retorno) para que os modelos representem com precisão as classes do domínio.  
* **Arquitetura do Sistema e Contratos de API:**  
  * Utilize o **C4 Model (Containers e Components)** nativo do Gaphor para mapear o fluxo de integração entre os conectores das APIs (MetaService, GoogleService, TikTokService) e os controllers do sistema.

### 2.3.2. Recomendações e Estratégia para Engenharia Reversa e Sincronização

O Gaphor não possui um motor de engenharia reversa nativo "out-of-the-box" com botão de um clique para ler bases SQL ou código fonte e regerar diagramas. Contudo, devido à sua arquitetura interna aberta em Python e formato .gaphor limpo, a engenharia reversa é perfeitamente viável através de abordagens automatizadas:

| Desafio no Gaphor | Estratégia Recomendada para o Projeto | Ferramentas e Automações Auxiliares   |
| :---- | :---- | :---- |
| **Engenharia Reversa de Código** | Utilizar a API em Python do Gaphor ou scripts de AST (Abstract Syntax Tree) para ler o código (Python/Dart/TypeScript) e instanciar/atualizar elementos no arquivo .gaphor. | Scripts customizados com gaphor.core / parsers de AST para extrair classes e relacionamentos diretamente para o modelo. |
| **Engenharia Reversa de Dados (SQL/Schema)** | Extrair metamodelos do banco de dados (ex: PostgreSQL/SQLite/Supabase) via inspeção de esquema e mapeá-los para entidades UML no Gaphor. | Utilitários de exportação de DDL/JSON Schema convertidos via CLI Python para a estrutura do Gaphor. |
| **Geração de Código (Code Gen)** | Gerar boilerplate de código (interfaces de conectores de API, models e DTOs) a partir do modelo .gaphor. | Templates Jinja2 / scripts Python lendo o arquivo .gaphor para gerar DTOs e classes de contrato de mídia social. |

## 2.4. Recomendações Práticas para o Fluxo do Projeto

1. **Estrutura de Repositório (Docs-as-Code):** Mantenha o arquivo do modelo na raiz ou em /docs/architecture/260726\_media\_manager.gaphor no controle de versão Git.  
2. **Evolução Progressiva de Modelagem:**  
   * **Fase 1 (C4 System Context):** Visão geral do app conectando-se às plataformas Meta, Google e TikTok.  
   * **Fase 2 (Diagrama de Classes UML de Domínio):** Mapeamento das tabelas/classes de Post, AccountToken, Campaign e AnalyticsMetric.  
   * **Fase 3 (Diagrama de Sequência UML):** Detalhamento do fluxo de publicação e renovação de tokens OAuth.  
1. **Automação de Engenharia Reversa:** Dado a arquitetura baseada em Python, monte um script simples para manter a sincronização caso o código evolua primeiro no repositório.

# 3. ultima

## 3.1. Análise da Ferramenta Core: Gaphor
### 3.1.1. Arquitetura do Gaphor
O Gaphor é uma ferramenta de modelagem UML/SysML open-source desenvolvida em Python e baseada na biblioteca gráfica GTK (via PyGObject) e no motor de renderização cairo.
 * Modelo Interno (Data Model): Mantém uma representação baseada em metamodelo no estilo OMG. Os elementos são instâncias do pacote gaphor.UML ou gaphor.SysML.
 * Separação Modelo-Visão: O Gaphor separa rigorosamente o elemento do modelo (Element) da sua representação gráfica na tela (Presentation).
 * Persistência Padrão: Armazena os dados em arquivo XML customizado (.gaphor), serializando a árvore de objetos internos e suas conexões.
### 3.1.2. Pontos Fortes e Limitações
| Aspecto      | Pontos Fortes                                                 | Limitações                                                                                |
| ------------ | ------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Arquitetura  | Leve, modular, extensível em Python e totalmente open-source. | Interface nativa acoplada ao GTK/PyGObject.                                               |
| Metamodelo   | Suporte sólido a UML 2.x e SysML 1.x.                         | Falta suporte nativo a OCL e regras avançadas de MDA.                                     |
| Persistência | Arquivo XML simples de inspecionar.                           | Falta persistência em banco relacional/documental para consultas complexas em tempo real. |
### 3.1.3. Estrutura de Dados Ampliada
Para evoluir o Gaphor de um editor visual local para um Sistema Completo de Edição de Especificações de Software, é essencial ampliar sua estrutura de dados e camada de persistência.
#### 3.1.3.1. Ampliação para Elementos da MDA (Model Driven Architecture)
A estrutura de dados deve ser expandida para cobrir as três camadas fundamentais da MDA (CIM, PIM, PSM) e incorporar os seguintes pilares:
 * Inclusão de OCL (Object Constraint Language):
   * Expressão de Regras e Invariantes: Associação de invariantes, pré-condições e pós-condições diretamente a Classes, Interfaces e Casos de Uso.
   * Validação Semântica: Motor de execução OCL para validar se a especificação do software é internamente consistente antes da geração de artefatos.
 * Elementos para Geração de Código (Code Generation / PSM):
   * Metadados de mapeamento de tipos (ex: mapeamento do tipo genérico String para VARCHAR em SQL ou String em Dart/Python).
   * Templates de transformação (M2T - Model-to-Text) associados aos elementos de modelo.
   * Anotações de ORM, rotas de API, escopos de segurança e estruturas de dados DTO.
 * Engenharia Reversa e Sincronização (Round-Trip Engineering):
   * Mapeamento de Hashing e AST: Identificadores únicos globais (UUIDs) atrelados a nós da AST (Abstract Syntax Tree) do código gerado para detecção de derivações (drift).
   * Log de Mudanças Granulares: Estrutura de auditoria para rastrear alterações efetuadas diretamente no código ou no modelo, permitindo mesclagem bidirecional (3-way merge).
#### 3.1.3.2. Recomendações para Modelagem da Especificação da Estrutura de Dados
Para modelar a especificação estendida sem quebrar a compatibilidade com o motor base do Gaphor:
* Abordagem Baseada em Perfis e Estreitamento de Metamodelo (Profiles & Stereotypes):
	* Utilizar os mecanismos nativos de Profiles da UML/SysML do Gaphor para definir novos estereótipos (ex: `<OCLConstraint>`, `<RESTEndpoint>`, `<DatabaseEntity>`).
- Estrutura de Metadados JSON/BSON Embutida:
	- Estender a classe Element base do Gaphor com um atributo dinâmico de propriedades adicionais (extra_properties / mda_metadata), permitindo anexar esquemas e payloads sem alterar o core rígido do Gaphor.
* Separador de Camada do Grafo de Exibição vs. Grafo de Domínio:
	* Isolar a representação do modelo abstrato de dados (Domain AST) dos artefatos visuais (Canvas Coordinates, Layout), permitindo processar a especificação do software em pipelines headless (CI/CD) sem carregar bibliotecas gráficas GTK.

#### 3.1.3.3. Stack Recomendada para Ampliação da Base de Dados Integrada com o Gaphor

Dado o requisito de arquitetura para um sistema monousuário e local, toda a persistência central, controle de metadados e suporte aos elementos estendidos da MDA (incluindo expressões OCL e mapeamentos de geração de código) podem ser resolvidos de forma leve, embarcada e eficiente.

```
+-------------------------------------------------------------------+
|                         Gaphor Client                             |
|    (Python / PyGObject / UI de Modelagem / Motor OCL Local)       |
+-------------------------------------------------------------------+
                                  │
                  [Camada de Persistência & Sync Engine]
                                  │
                                  ▼
+-------------------------------------------------------------------+
|                   Armazenamento Local Embarcado                   |
|                                                                   |
|  ┌─────────────────────────────────────────────────────────────┐  |
|  │                       SQLite Local                          │  |
|  │  - Armazenamento Relacional (Tabelas e Unicidade de UUIDs)   │  |
|  │  - Colunas JSON / JSONB (Suporte Nativo a Metadados MDA/OCL) │  |
|  │  - Consultas via SQL / JSON_EXTRACT / FTS5 (Busca Textual)  │  |
|  └─────────────────────────────────────────────────────────────┘  |
|  ┌─────────────────────────────────────────────────────────────┐  |
|  │                Git Local (via pygit2 / GitPython)           │  |
|  │  - Exportação de Snapshots em JSON/YAML Legíveis            │  |
|  │  - Controle de Versão Descentralizado e Historização        │  |
|  └─────────────────────────────────────────────────────────────┘  |
+-------------------------------------------------------------------+
```

 * SQLite com Suporte Nativo a JSON/JSONB:
   * Modelagem Híbrida: Utiliza o SQLite no modo arquivo local (.db ou .sqlite). A estrutura relacional atende aos elementos rígidos do metamodelo (UUIDs, relacionamentos do grafo, tipos de elementos), enquanto os atributos dinâmicos (regras OCL, metadados de geração de código, mapeamentos de tipos) são armazenados em colunas com o tipo JSONB (disponível nativamente a partir do SQLite 3.45+).
   * Vantagens: Alta performance em leitura e escrita local, sem dependência de processos/servidores externos e suporte completo a operadores de consulta JSON (json_extract, json_tree) para filtrar especificações diretamente via SQL.
 * Engine de Versionamento Local (Git via pygit2 / GitPython):
   * Uso: Além do banco SQLite local, a aplicação exporta snapshots das especificações em arquivos estruturados (JSON ou YAML limpos) diretamente dentro do repositório Git do projeto.
   * Vantagens: Permite realizar histórico de alterações, commits, criação de branches e inspeção de diffs visuais legíveis por humanos no código da especificação.
 * Validação de Modelos e Mapeamento (Pydantic em Python):
   * Uso: Utilizado como camada intermediária entre os objetos do Gaphor e a persistência no SQLite. Garante a tipagem forte, serialização/deserialização do payload JSONB e validação de consistência dos dados do modelo antes da gravação no disco.

### 3.1.4. Recomendações Práticas para o Fluxo do Projeto

 * Manter o Gaphor como Motor de Modelagem Visual:
   * Evitar reescrever o motor de renderização visual. Utilizar plugins e extensões do próprio Gaphor para acoplar a nova estrutura de dados.
 * Desenvolver Extensões Desacopladas (Modular Core):
   * Implementar o parser OCL, o mecanismo de validação MDA e os geradores de código como pacotes Python independentes, importáveis pelo Gaphor e executáveis via CLI.
 * Padrão de Serialização Intermediária (JSON Schema MDA):
   * Adotar um formato intermediário aberto e legível em JSON para a especificação do software, facilitando a integração com ferramentas externas (Aider, CLI tools, analisadores estáticos).
 * Estratégia de Integração com Desenvolvimento (CLI & CI/CD):
   * Permitir que o modelo de especificação seja validado e compilado em código-fonte diretamente em pipelines de integração contínua sem depender da interface gráfica.

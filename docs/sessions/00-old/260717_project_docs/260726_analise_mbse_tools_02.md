# **Pesquisa Comparativa de Ferramentas MBSE: Eclipse Papyrus, Modelio e Gaphor (V2)**

A Engenharia de Sistemas Baseada em Modelos (*Model-Based Systems Engineering \- MBSE*) é uma abordagem formalizada para apoiar a especificação, design, análise, verificação e validação de sistemas complexos ao longo de todo o seu ciclo de vida. Em vez de documentos textuais isolados, o MBSE utiliza modelos conceituais padronizados — principalmente embasados em notações como **SysML (Systems Modeling Language)** e **UML (Unified Modeling Language)**.

Esta versão (V2) do documento expande a análise comparativa das três ferramentas de código aberto (**Eclipse Papyrus**, **Modelio** e **Gaphor**), introduzindo o mapeamento de persitência/bancos de dados e diretrizes de integração no fluxo de engenharia de software.

## **1\. Introdução ao Contexto das Ferramentas MBSE**

As ferramentas de modelagem desempenham um papel central na transição de processos tradicionais baseados em documentos para ecossistemas orientados a modelos. O objetivo central de uma ferramenta MBSE é fornecer suporte visual e semântico consistente para expressar requisitos, arquitetura estrutural, comportamentos dinâmicos e restrições paramétricas do sistema.

**Principais Aspectos Avaliados em Ferramentas MBSE:**

* **Conformidade com Padrões OMG:** Suporte rigoroso a SysML e UML.  
* **Rastreabilidade de Requisitos:** Capacidade de vincular necessidades a blocos estruturais e testes de verificação.  
* **Modelos de Armazenamento e Persistência:** Como os dados do metamodelo são estruturados no disco/repositório.  
* **Integração ao Fluxo de Software:** Adequação para fluxos de especificação e desenvolvimento ágil ou tradicional.

## **2\. Análise Detalhada das Ferramentas**

### **2.1 Eclipse Papyrus**

O **Eclipse Papyrus** é uma das ferramentas de modelagem industrial e acadêmica mais robustas do ecossistema de código aberto. Desenvolvido no âmbito da Eclipse Foundation, o Papyrus fornece um ambiente completo para Engenharia Orientada a Modelos (MDE) e MBSE.

* **Padrões e Notações:** Oferece suporte completo ao UML 2.5 e SysML 1.6, incluindo suporte a perfis customizados (DSMLs) e notações avançadas como MARTE.  
* **Recursos de MBSE:** Matrizes de alocação de requisitos, diagramas paramétricos, execução/simulação comportamental com Moka e customização de telas via Eclipse Sirius.  
* **Pontos Fortes:** Extremamente extensível, rico em recursos, padrões rigorosos e forte integração com o ecossistema Eclipse.  
* **Desafios:** Alta complexidade de configuração e curva de aprendizado íngreme.

### **2.2 Modelio**

O **Modelio** é uma ferramenta de modelagem flexível desenvolvida com foco no suporte a UML, BPMN e SysML. O projeto oferece edições abertas (open-source) e ecossistema extensível por módulos.

* **Padrões e Notações:** Suporta UML 2, SysML (módulo SysML Architect) e BPMN para processos de negócios.  
* **Recursos de MBSE:** Gerenciamento/rastreabilidade de requisitos, geração automatizada de documentação e suporte a extensões em Jython/Python e Java.  
* **Pontos Fortes:** Interface acessível, integração equilibrada entre UML e BPMN, e boa organização do repositório.  
* **Desafios:** Recursos avançados de simulação e suporte colaborativo de grande porte estão em módulos avançados.

### **2.3 Gaphor**

O **Gaphor** é uma ferramenta moderna, leve e multiplataforma desenvolvida em Python e GTK. Foi projetado para ser intuitivo e direto, mantendo conformidade semântica com UML 2 e SysML.

* **Padrões e Notações:** Suporta UML 2, SysML, RAAML e o modelo C4 para arquitetura de software.  
* **Recursos de MBSE:** Design focado em diagramas, suporte a BDD, IBD e diagramas de Requisitos do SysML, e integração nativa com ecossistemas Python.  
* **Pontos Fortes:** Início imediato, baixo consumo de recursos, código 100% aberto e excelente usabilidade.  
* **Desafios:** Não possui mecanismos nativos de simulação de modelos complexos (como fUML).

## **3\. Modelos de Bancos de Dados e Persistência de Dados**

Cada ferramenta adota uma estratégia distinta para o armazenamento e gerenciamento do metamodelo, o que afeta diretamente o controle de versão, colaboração e performance em grandes projetos:

| Ferramenta | Modelo de Persistência / Banco de Dados | Formato de Arquivo Principal | Comportamento com Controle de Versão (Git/SVN)   |
| :---- | :---- | :---- | :---- |
| **Eclipse Papyrus** | **EMF (Eclipse Modeling Framework) / XMI** O metamodelo é salvo em arquivos XMI estruturados em nós relacionais XML. Pode utilizar persistência em banco de dados em grafos/relacional via extensões EMF Store ou CDO (Connected Data Objects). | .uml, .notation, .di | Exige ferramentas específicas de merge estrutural (como EMF Compare) devido à verbosidade do XMI em commits paralelos. |
| **Modelio** | **H2 Database / Repositório Orientado a Objetos** Utiliza internamente o banco de dados embutido H2 para o repositório local e gerenciamento de transações de modelo. Projetos complexos sincronizam via servidor de modelos. | .exml / Arquivos de banco local H2 em diretórios de projeto | Bom isolamento de componentes, mas o merge direto em arquivos binários/banco de dados exige exportação/importação no nível de módulo. |
| **Gaphor** | **XML Orientado a Grafos Leves (Data-centric XML)** Armazena o modelo conceitual em um formato XML simples e human-readable, onde os elementos do modelo e itens visuais possuem IDs únicos persistentes. | .gaphor (XML plano) | Altamente amigável ao Git. Conflitos de mesclagem podem ser inspecionados e resolvidos diretamente em editores de texto. |

## **4\. Recomendações para Uso no Fluxo de Criação de Especificações de Software**

A engenharia de software moderna exige um fluxo fluido entre a concepção do sistema, a especificação dos requisitos e a implementação do código. A seguir estão as recomendações de adoção por tipo de fluxo de trabalho:

### **4.1 Fluxo Ágil / Orientado a microsserviços e APIs (Gaphor)**

* **Aplicação Ideal:** Especificação rápida de arquiteturas de software, mapeamento C4 e diagramas de domínio.  
* **Recomendação de Uso:** Integre o Gaphor no repositório do código fonte (Docs-as-Code). Os arquivos .gaphor e exportações de imagem podem residir na pasta /docs do projeto de software. Testes automatizados via CI/CD podem garantir que os modelos Python não possuem dependências quebradas.

### **4.2 Fluxo Híbrido / Engenharia de Requisitos com Regras de Negócio (Modelio)**

* **Aplicação Ideal:** Sistemas corporativos, especificações funcionais pesadas e rastreabilidade entre processos de negócio (BPMN) e software (UML).  
* **Recomendação de Uso:** Utilizar o Modelio no início da fase de especificação para capturar requisitos funcionais e mapear processos de negócio. Exporte especificações em PDF/HTML para validação com clientes não técnicos antes do início do desenvolvimento.

### **4.3 Fluxo Crítico / Engenharia de Sistemas de Alta Complexidade (Eclipse Papyrus)**

* **Aplicação Ideal:** Sistemas embarcados, dispositivos médicos, setor aeroespacial e automotivo (onde o software interage com hardware pesado).  
* **Recomendação de Uso:** Adote o Papyrus em pipelines estritos de engenharia de sistemas. Utilize diagramas SysML para rastrear requisitos de sistema até o software, aplique Moka para simular estados do sistema antes da codificação e use engenharia reversa para manter os modelos UML sincronizados com código Java/C++.

## **5\. Tabela Comparativa Geral**

| Critério | Eclipse Papyrus | Modelio | Gaphor   |
| :---- | :---- | :---- | :---- |
| **Licença** | Eclipse Public License (EPL) | GPL / Apache (Core Open Source) | Apache License 2.0 |
| **Linguagens Suportadas** | UML 2.5, SysML 1.6, MARTE, Perfis customizados | UML 2, SysML, BPMN | UML 2, SysML, RAAML, C4 |
| **Modelo de Banco/Persistência** | EMF / XMI / CDO Repository | H2 Database / EXML | XML Plano orientado a grafos |
| **Compatibilidade com Git** | Requer EMF Compare | Requer gestão por módulos/exportação | Nativa e amigável (Diff textual) |
| **Usabilidade** | Complexa (Exige treinamento) | Moderada (Interface estruturada) | Simples e Intuitiva |
| **Perfil no Fluxo de Software** | Sistemas críticos / Embedded / MBSE completo | Sistemas corporativos e BPMN \+ UML | Arquitetura ágil / Docs-as-Code / C4 |

## **6\. Conclusão e Recomendações de Adoção**

1. **Eclipse Papyrus:** Indicado se o ciclo de vida do software exigir rastreabilidade rigorosa de padrões MBSE industriais, validação paramétrica e execução de modelos.  
2. **Modelio:** Indicado se a especificação do software depender fortemente de processos de negócio preexistentes e alinhamento com stakeholders de análise de negócios.  
3. **Gaphor:** Indicado se o foco for velocidade de documentação, simplicidade na manutenção dentro de repositórios Git de projetos ágeis.
# 1. **Pesquisa Comparativa de Ferramentas MBSE: Eclipse Papyrus, Modelio e Gaphor**

A Engenharia de Sistemas Baseada em Modelos (*Model-Based Systems Engineering \- MBSE*) é uma abordagem formalizada para apoiar a especificação, design, análise, verificação e validação de sistemas complexos ao longo de todo o seu ciclo de vida. Em vez de documentos textuais isolados, o MBSE utiliza modelos conceituais padronizados — principalmente embasados em notações como **SysML (Systems Modeling Language)** e **UML (Unified Modeling Language)**.

Este documento apresenta um estudo detalhado e comparativo sobre três relevantes ferramentas de código aberto para MBSE: **Eclipse Papyrus**, **Modelio** e **Gaphor**.

## 1.1. Introdução ao Contexto das Ferramentas MBSE

As ferramentas de modelagem desempenham um papel central na transição de processos tradicionais baseados em documentos para ecossistemas orientados a modelos. O objetivo central de uma ferramenta MBSE é fornecer suporte visual e semântico consistente para expressar requisitos, arquitetura estrutural, comportamentos dinâmicos e restrições paramétricas do sistema.

**Principais Aspectos Avaliados em Ferramentas MBSE:**

* **Conformidade com Padrões OMG:** Suporte rigoroso a SysML e UML.  
* **Rastreabilidade de Requisitos:** Capacidade de vincular necessidades a blocos estruturais e testes de verificação.  
* **Simulação e Execução:** Capacidade de validar o comportamento do modelo dinamicamente.  
* **Usabilidade e Extensibilidade:** Curva de aprendizado e suporte a personalizações/plugins.

## 1.2. Análise Detalhada das Ferramentas

### 1.2.1. **2.1 Eclipse Papyrus**

O **Eclipse Papyrus** é uma das ferramentas de modelagem industrial e acadêmica mais robustas do ecossistema de código aberto. Desenvolvido no âmbito da Eclipse Foundation, o Papyrus fornece um ambiente completo para Engenharia Orientada a Modelos (MDE) e MBSE.

* **Padrões e Notações:** Oferece suporte completo ao UML 2.5 e SysML 1.6, incluindo suporte a perfis customizados (DSMLs) e notações avançadas como MARTE (para sistemas embarcados de tempo real).  
* **Recursos de MBSE:**  
  * Matrizes de alocação para rastreabilidade precisa de requisitos a componentes do sistema.  
  * Diagramas paramétricos com blocos de restrição para análise matemática de desempenho.  
  * Módulo **Moka** para execução e simulação gráfica de modelos comportamentais (fUML / PSCS).  
  * Personalização gráfica avançada via Eclipse Sirius e mecanismo de *Viewpoints* para adaptar a visualização às necessidades de diferentes stakeholders.  
* **Pontos Fortes:** Extremamente extensível, rico em recursos, padrões rigorosos e forte integração com o ecossistema Eclipse (EGit, EMF Compare, Xtext).  
* **Desafios:** Alta complexidade de configuração e curva de aprendizado íngreme, especialmente para iniciantes.

### 1.2.2. **2.2 Modelio**

O **Modelio** é uma ferramenta de modelagem flexível desenvolvida com foco no suporte a UML, BPMN e SysML. O projeto oferece edições abertas (open-source) e ecossistema extensível por módulos.

* **Padrões e Notações:** Suporta UML 2, SysML (através do módulo SysML Architect) e BPMN para modelagem de processos de negócios.  
* **Recursos de MBSE:**  
  * Gerenciamento e rastreabilidade de requisitos integrados ao ambiente de modelagem.  
  * Geração automatizada de documentação em formatos como HTML e PDF.  
  * Suporte à extensão do metamodelo por meio de módulos em Jython/Python e Java.  
* **Pontos Fortes:** Interface mais acessível do que ambientes Eclipse puros, integração equilibrada entre UML e BPMN, e boa organização do repositório de modelos.  
* **Desafios:** Recursos avançados de simulação e suporte colaborativo de equipe de grande porte estão concentrados em módulos comerciais/avançados.

### 1.2.3. **2.3 Gaphor**

O **Gaphor** é uma ferramenta moderna, leve e multiplataforma desenvolvida inteiramente em Python e GTK. Ele foi projetado para ser intuitivo e direto, mantendo total conformidade semântica com o modelo de dados UML 2 e SysML.

* **Padrões e Notações:** Suporta UML 2, SysML, RAAML (Risk Analysis and Assessment Modeling Language) e o modelo C4 para arquitetura de software.  
* **Recursos de MBSE:**  
  * Design focado em diagramas: sem painéis ocultos ou configurações excessivamente complexas.  
  * Suporte a diagramas de Definição de Bloco (BDD), Uso Interno (IBD) e Requisitos do SysML.  
  * Integração nativa com ecossistemas Python, permitindo uso em scripts e notebooks Jupyter.  
  * Interface moderna com suporte a modo escuro e exportação limpa de diagramas.  
* **Pontos Fortes:** Início imediato, consumo mínimo de recursos do sistema, código 100% aberto (licença Apache 2.0), excelente usabilidade para estudantes e projetos ágeis.  
* **Desafios:** Não possui mecanismos nativos de simulação de modelos complexos (como fUML) ou motores de geração pesada de código.

## 1.3. Tabela Comparativa de Recursos e Capacidades

A tabela a seguir resume as principais características técnicas e operacionais das três ferramentas:

| Critério | Eclipse Papyrus | Modelio | Gaphor   |
| :---- | :---- | :---- | :---- |
| **Licença** | Eclipse Public License (EPL) | GPL / Apache (Core Open Source) | Apache License 2.0 |
| **Linguagens Suportadas** | UML 2.5, SysML 1.6, MARTE, Perfis customizados | UML 2, SysML, BPMN | UML 2, SysML, RAAML, C4 |
| **Linguagem / Base Tecnológica** | Java / Eclipse RCP (EMF, GMF, Sirius) | Java / Jython | Python / GTK / Cairo |
| **Usabilidade / Curva de Aprendizado** | Complexa (Exige treinamento) | Moderada (Interface estruturada) | Simples e Intuitiva (Acesso rápido) |
| **Simulação de Modelos** | Avançada (Módulo Moka fUML/PSCS) | Limitada na versão FOSS | Sem suporte nativo a simulação |
| **Extensibilidade** | Altíssima (Plugins Eclipse e Perfis UML) | Alta (Módulos em Java e Scripts Python) | Média (Plugins Python e API de scripts) |
| **Perfil de Uso Indicado** | Sistemas industriais complexos e pesquisas acadêmicas profundas | Engenharia de sistemas geral e integração com processos de negócio | Projetos ágeis, ensino, documentação rápida e modelagem leve |

## 1.4. Conclusão e Recomendações

A escolha da ferramenta MBSE ideal depende diretamente da complexidade do projeto, do perfil da equipe e das necessidades de validação:

1. **Escolha o Eclipse Papyrus** se você precisa de rigor absoluto com os padrões OMG, exige simulação de modelos (fUML), necessita criar linguagens específicas de domínio (DSML) através de perfis UML complexos ou está inserido em um processo industrial de grande porte.  
2. **Escolha o Modelio** se busca um equilíbrio entre facilidade de uso, rastreabilidade de requisitos e integração com modelagem de processos de negócio (BPMN).  
3. **Escolha o Gaphor** se o seu objetivo é criar diagramas SysML/UML e C4 de forma rápida e visualmente limpa, integrando o modelo a ecossistemas de scripts Python ou projetos sem a sobrecarga de ambientes computacionais pesados.
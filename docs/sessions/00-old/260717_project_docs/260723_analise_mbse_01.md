# 1. objetivos 

analisar as características da MBSE (Model Based Software Engineering) e MDA (Model Driven Architecture) como base para um modelo predominantemente determinístico de SDD (Spec Driven Development)

# 2. metodo de análise 

- definir atributos de avaliação de qualidade de software  
- definir atributos de eficiência de desenvolvimento de software 
- mapear todos os atributos dos modelos definidos pela OMG (Object Management Group) para construção da MDA (Model Driven Architecture)
- analisar a relação entre os modelos da MDA e os atributos de qualidade e eficiência do desenvolvimento de software 

# 3. plano de execução

| Etapa                          | Objetivo                                                                                                       | Ações principais                                                                           | Entregável esperado                    |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | -------------------------------------- |
| 1. Mapeamento de normas OMG    | Identificar todas as especificações relevantes (MOF, QVT, UML, SBVR, SPEM…)                                    | • Listar documentos OMG → PDF/HTML <br>• Compilar glosários de termos                      | *Checklist de normas*                  |
| 2. Definição de atributos      | Estabelecer atributos de qualidade (rastreabilidade, consistência) e de eficiência (tempo de ciclo, automação) | • Criação de catálogo de atributos <br>• Vincular cada atributo a uma norma/metamodelo     | *Catálogo de atributos*                |
| 3. Mapeamento MDA → Atributos  | Construir matriz em que cada norma/modelo (CIM/PIM/PSM) encontra os atributos relevantes                       | • Colunas: normas; linhas: atributos; células: presença/grade<br>• Notação de dependências | *Matriz de mapeamento*                 |
| 4. Análise de adequação ao SDD | Verificar se o modelo determinístico de SDD se sustenta na matriz                                              | • Identificar lacunas <br>• Recomendar práticas de modelagem (ex.: variáveis, refinamento) | *Relatório de adequação*               |
| 5. Documentação                | Produzir a *Matriz de mapeamento atributos* (relatório tsv/markdown)                                           | • Exportar tabela <br>• Incluir notas de insight                                           | `matriz_mda_atributos.md` (ou `.xlsx`) |

# 4. Pesquisa de Especificações OMG

## 4.1. Fonte: https://www.omg.org/spec/ (acessado via webfetch)

## 4.2. Especificações Atualizadas Recentemente (últimos 6 meses)

| Nome                                              | Acrônimo      | Versão     | Status | Data de Publicação |
| ------------------------------------------------- | ------------- | ---------- | ------ | ------------------ |
| Command and Control Message Specification         | C2MS          | 1.2 beta   | beta   | Abril 2026         |
| Commons Ontology Library                          | Commons       | 1.3        | formal | Junho 2026         |
| DDS Security                                      | DDS-SECURITY™ | 1.2        | formal | Fevereiro 2026     |
| Essence Kernel & Language for Engineering Methods | Essence®      | 2.0 beta 2 | beta   | Março 2026         |
| Financial Instrument Global Identifier®           | FIGI®         | 1.2        | formal | Março 2026         |
| Ground Data Delivery Interface                    | GDDI          | 1.0        | formal | Julho 2026         |
| Multiple Vocabulary Facility                      | MVF           | 1.1 beta   | beta   | Abril 2026         |
| Robotic Interaction Service Framework             | RoIS™         | 2.0        | formal | Junho 2026         |
| Robotic Service Ontology                          | ROSO          | 1.1        | formal | Junho 2026         |
| Specification Common Elements                     | SCE           | 1.0        | formal | Junho 2026         |
| Shared Data Model and Notation                    | SDMN          | 1.0        | formal | Junho 2026         |
| Unified Architecture Framework                    | UAF           | 1.3        | formal | Abril 2026         |

## 4.3. Especificações Adotadas pela ISO

| Nome                                               | Versão | Número ISO                                                                            | Status                     |
| -------------------------------------------------- | ------ | ------------------------------------------------------------------------------------- | -------------------------- |
| Automated Function Points (AFP™)                   | 1.0    | 19515:2019                                                                            | formal/19-05-03            |
| Automated Source Code Quality Measures (ASCQM)     | 1.0    | 5055:2023                                                                             | formal/23-12-01            |
| Business Process Model And Notation (BPMN™)        | 2.0.1  | 19510:2013                                                                            | formal/13-11-03            |
| Common Object Request Broker Architecture (CORBA®) | 3.1.1  | 19500-1:2012 (Interfaces), 19500-2:2012 (Interoperability), 19500-3:2012 (Components) | formal/12-05-03 a 12-05-05 |
| Interface Definition Language (IDL)                | 4.2    | 19516:2022                                                                            | formal/22-06-02            |
| Knowledge Discovery Metamodel (KDM)                | 1.3    | 19506:2012                                                                            | formal/12-05-08            |
| Meta Object Facility (MOF™)                        | 1.4    | 19502:2005                                                                            | formal/05-05-05            |
| Meta Object Facility (MOF™)                        | 2.4.2  | 19508:2014                                                                            | formal/14-04-05            |
| Object Constraint Language (OCL™)                  | 2.3.1  | 19507:2012                                                                            | formal/12-05-09            |
| OMG Systems Modeling Language (SysML®)             | 1.4    | 19514:2017                                                                            | formal/17-05-08            |
| Unified Architecture Framework (UAF)               | 1.1    | 19540-1:2022 (DMM), 19540-2:2022 (UAFP)                                               | formal/22-04-03 a 22-04-04 |
| Unified Modeling Language (UML®)                   | 1.4    | 19501:2005                                                                            | formal/05-04-01            |
| Unified Modeling Language (UML®)                   | 2.4.1  | 19505-1:2012 (Infrastructure), 19505-2:2012 (Superstructure)                          | formal/12-05-06 a 12-05-07 |
| Unified Profile for DoDAF and MODAF (UPDM™)        | 2.1.1  | 19513:2019                                                                            | formal/19-05-04            |
| XML Metadata Interchange (XMI®)                    | 2.0    | 19503:2005                                                                            | formal/05-05-06            |
| XML Metadata Interchange (XMI®)                    | 2.4.2  | 19509:2014                                                                            | formal/14-04-06            |

## 4.4. Lista Completa de Especificações (Contagem: 282)

*Devido ao tamanho, a lista completa não foi incluída aqui. Está disponível em: https://www.omg.org/spec/*  
*Principais categorias:* Business Modeling, C4i, Communications, Component Architecture, Enterprise Modeling, Finance, Government, Healthcare, High Performance Computing, Industrial Systems, Information Security, Interoperability, Lifesciences, Manufacturing, Retail, Robotics, Space, Transport, Language Mapping, Middleware, Modeling, OMG Data Distribution Service, Software Modernization, BPM Plus, CISQ, Corba Embedded Intelligence, Corba Facilities, Corba Platform, Corba Real Time, Corba Security, Corba Services, Data Warehousing, Domain, DTC, Interface Definition Language, Platform, Ptc, Real Time, Reference Architecture, Software Engineering, Systems Assurance, Systems Engineering, UML, UML Profile.

## 4.5. Links de Download Diretos para Normas-Chave MDA/MBSE

- **MOF 2.0**: https://www.omg.org/spec/MOF/2.0  
- **MOF 2.4.2**: https://www.omg.org/spec/MOF/2.4.2  
- **UML 2.4.1**: https://www.omg.org/spec/UML/2.4.1  
- **QVT 1.3**: https://www.omg.org/spec/QVT/1.3  
- **XMI 2.4.2**: https://www.omg.org/spec/XMI/2.4.2  
- **OCL 2.3.1**: https://www.omg.org/spec/OCL/2.3.1  
- **SysML 1.4**: https://www.omg.org/spec/SysML/1.4  
- **MDA Guide**: https://www.omg.org/spec/MDA  
- **SBVR 1.1**: https://www.omg.org/spec/SBVR/1.1  
- **SPEM 2.0**: https://www.omg.org/spec/SPEM/2.0  

# 5. Checklist de Normas OMG para MBSE/MDA

## 5.1. Normas Fundamentais

| Norma                                                       | Versão | Descrição                                                            | Status de Acesso | Observações                                         |
| ----------------------------------------------------------- | ------ | -------------------------------------------------------------------- | ---------------- | --------------------------------------------------- |
| MOF (Meta-Object Facility)                                  | 2.0    | Arquitetura de metamodelos para definição de linguagens de modelagem | Público          | Base para UML, SysML, etc.                          |
| UML (Unified Modeling Language)                             | 2.5.1  | Linguagem padrão para modelagem de sistemas de software              | Público          | Principal notação para PIM                          |
| QVT (Query/View/Transformation)                             | 1.3    | Padrão para transformações de modelos                                | Público          | Essencial para MDA (PIM→PSM)                        |
| XMI (XML Metadata Interchange)                              | 2.1.1  | Formato para troca de metadados entre ferramentas                    | Público          | Usado para serialização de modelos                  |
| OCL (Object Constraint Language)                            | 2.4    | Linguagem para expressar restrições e consultas em modelos           | Público          | Complementa UML/QVT                                 |
| SBVR (Semantics of Business Vocabulary and Business Rules)  | 1.1    | Especificação para vocabulário e regras de negócio                   | Público          | Relevante para modelagem de domínio                 |
| SPEM (Software Process Engineering Meta-model)              | 2.0    | Metamodelo para definição de processos de software                   | Público          | Útil para modelagem de processos de desenvolvimento |
| CWM (Common Warehouse Metamodel)                            | 1.1    | Metamodelo para armazenamento de dados e business intelligence       | Público          | Menos relevante para SE pura                        |
| SysML (Systems Modeling Language)                           | 1.7    | Extensão do UML para engenharia de sistemas                          | Público          | Relevante para MBSE em sistemas complexos           |
| MARTE (Modeling and Analysis of Real-Time Embedded systems) | 1.1    | Perfil UML para sistemas em tempo real e embarcados                  | Público          | Especializado para sistemas embutidos               |
| PLCS (Product Life Cycle Support)                           | -      | Específica para dados de ciclo de vida de produtos                   | Público          | Mais para manufatura que SE                         |
| FUML (Foundational UML)                                     | 1.3    | Subconjunto executável do UML                                        | Público          | Base para simulação e execução de modelos           |
| Alfabet (UML Action Language)                               | 1.0    | Linguagem de ações para UML                                          | Público          | Alternativa para especificação de comportamento     |

## 5.2. Normas Adicionais/Especializadas

| Norma                                             | Versão | Descrição                                       | Status de Acesso | Observações                          |
| ------------------------------------------------- | ------ | ----------------------------------------------- | ---------------- | ------------------------------------ |
| DDS (Data Distribution Service)                   | 1.4    | Padrão para middleware de publicação-assinatura | Público          | Relevante para sistemas distribuídos |
| CORBA (Common Object Request Broker Architecture) | 3.0    | Arquitetura para sistemas distribuídos          | Público          | Legado, mas ainda usado              |
| MDA Guide                                         | 1.0    | Guia geral para Model Driven Architecture       | Público          | Documentação orientativa             |
| MOF Query/View/Transformation                     | 1.0    | Especificação inicial do QVT                    | Público          | Histórico                            |

## 5.3. Links de Referência

- Portal OMG: https://www.omg.org/specs/
- Documentos públicos: https://spec.omg.org/
- Repositório GitHub (exemplos): https://github.com/omgdocs

# 6. Atributos de Qualidade e Eficiência para MBSE/MDA → SDD

## 6.1. Atributos de Qualidade de Software (ISO/IEC 25010)

[Understanding ISO/IEC 25010: A Comprehensive Framework for Software Quality Evaluation](https://medium.com/@oczz/understanding-iso-iec-25010-a-comprehensive-framework-for-software-quality-evaluation-ae3cc5250057)
[sonar](https://www.sonarsource.com/resources/library/iso-iec-25010-explained/)

| Categoria              | Sub‑atributo                                                                                                          | Descrição                                                            | Relevância para MBSE/MDA                                                            | revisar tabela                                                                                                                                  |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Functional Suitability | Functional completeness                                                                                               | Cobertura dos requisitos definidos na especificação                  | Essencial para garantir que os modelos MDA capturem todos os requisitos de software |                                                                                                                                                 |
|                        | Functional correctness                                                                                                | Conformidade com a semântica dos modelos                             | Vital para validar que as transformações PIM→PSM preservam significado              |                                                                                                                                                 |
|                        | Functional appropriateness                                                                                            | enabling users to accomplish their objectives efficiently            |                                                                                     |                                                                                                                                                 |
| Maintainability        | Analyzability                                                                                                         | Facilidade de identificar impactos de mudanças nos modelos           | Ajuda a estimar esforço de manutenção pós‑geração                                   |                                                                                                                                                 |
|                        | Conformance                                                                                                           | Cumprimento de normas e Metamodelos OMG                              | Garante que os artefatos sejam reconhecidos por outros sistemas                     | atributo não existente na ISO 25010 mas o requisito é importante, sugiro adotar como criterio para o atributo "Maintainability + Analyzability" |
|                        | Modularity                                                                                                            | Grau de acoplamento entre sub‑modelos                                | Impacta diretamente na reutilização de artefatos MDA                                |                                                                                                                                                 |
|                        | reusability, modifiability, testability                                                                               |                                                                      |                                                                                     | atributos existentes na ISO 25010 e que podem ser uteis                                                                                         |
| Interaction capability | Appropriateness recognizability                                                                                       | Facilidade de interpretação dos artefatos modelo por desenvolvedores | Determina a adoção prática do processo MDA nas equipes                              | na nova versao da norma "usability" foi renomeado para "Interaction capability"                                                                 |
|                        | Learnability, Operability, User error protection, User engagement, Inclusivity, User assistance, Self-descriptiveness |                                                                      |                                                                                     | atributos existentes na ISO 25010 e que podem ser uteis                                                                                         |
| Compatibility          | Interoperability                                                                                                      | Capacidade de troca de modelos entre ferramentas                     | Afeta a flexibilidade na escolha de ambientes de modelagem                          | irrelevante no momento, pode ser eliminado da tabela                                                                                            |
| Reliability            | Maturity                                                                                                              | Estabilidade dos modelos e ferramentas de modelagem                  | Influencia a previsibilidade da geração automática de código                        | irrelevante no momento, pode ser eliminado da tabela                                                                                            |
| Security               | Confidentiality / Integrity                                                                                           | Proteção de modelos sensíveis durante a troca entre ferramentas      | Crucial em ambientes corporativos com dados proprietários                           | irrelevante no momento, pode ser eliminado da tabela                                                                                            |
| Performance Efficiency | Time behavior                                                                                                         | Latência de processos de modelagem e geração de código               | Importante para reduzir o lead‑time de desenvolvimento                              | irrelevante no momento, pode ser eliminado da tabela                                                                                            |


## 6.2. Atributos de Eficiência de Desenvolvimento de Software

| Atributo                               | Métrica                                                            | Como medir                                                  | Impacto esperado                          |
| -------------------------------------- | ------------------------------------------------------------------ | ----------------------------------------------------------- | ----------------------------------------- |
| Lead‑time de desenvolvimento           | Dias/horas da concepção do modelo até entrega de código executável | Cronômetro a partir do início do modelagem até deploy       | Redução de ciclos de release              |
| Taxa de automação                      | % de artefatos gerados automaticamente (código, testes, docs)      | Contagem de artefatos gerados / total de artefatos          | Aumento de produtividade                  |
| Defeito density                        | Nº de defeitos por KLOC gerados a partir de modelos                | Relatórios de qualidade pós‑deploy                          | Qualidade do código gerado                |
| Reutilização                           | % de componentes reutilizados entre projetos                       | Contagem de componentes reutilizados / total de componentes | Redução de esforço em iniciativas futuras |
| Cost of change                         | Custo de alterar requisito após geração do modelo                  | Estimativa baseada em esforço de re‑modelagem e re‑geração  | Determina a "deterministicidade" do SDD   |
| Model‑to‑Model transformation accuracy | % de transformações bem‑sucedidas sem rollback                     | Métricas de sucessos de QVT/Transformações                  | Afetiva confiança no processo MDA         |
| Model drift                            | Tempo para detectar divergência entre modelo e implementação       | Monitoramento contínuo de sincronização                     | Evita retrabalho futuro                   |

## 6.3. Mapeamento Provisório

| Atributo (Qualidade/Eficiência) | Norma OMG relacionada                    | Comentário de vínculo                                                   |
| ------------------------------- | ---------------------------------------- | ----------------------------------------------------------------------- |
| Functional completeness         | UML, SysML, MDA Guide                    | Modelos de caso de uso e funcionalidades capturam requisitos completos  |
| Performance efficiency          | QVT, DDS                                 | Tempos de execução de transformações determinam performance da pipeline |
| Maintainability                 | SPEM, CIM/PIM                            | Estrutura de modelo modular facilita manutenção                         |
| Lead‑time de desenvolvimento    | MDA Guide, MOF Query/View/Transformation | Automação de QVT reduz tempo de geração                                 |
| Taxa de automação               | QVT, DDS                                 | Percentual de geração automática reflete eficiência da pipeline         |
| Defeito density                 | OCL, ATL, Model‑to‑Model transformations | Qualidade de regras de validação impacta defeitos no código             |

# 7. Matriz de Mapeamento MDA → Atributos

| Norma/Modelo                               | Atributo(s) Relacionado(s)                                                 | Comentário                                                                                                                                        |
| ------------------------------------------ | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CIM (Conceptual Information Model)**     | Functional completeness, Analyzability, Conformance                        | Modelos CIM capturam requisitos de alto nível e estruturas de domínio, vinculados à completude funcional e conformância a normas como BPMN e SBVR |
| **PIM (Platform Independent Model)**       | Reliability, Maintainability, Security                                     | PIM define arquiteturas independentes da plataforma, exigindo confiabilidade e segurança em transformações                                        |
| **PSM (Platform Specific Model)**          | Performance efficiency, Performance Effort                                 | PSM está vinculado a implantações específicas, afetando latência e esforço de desenvolvimento                                                     |
| **QVT (Model Transformations)**            | Taxa de automação, Defeito density, Model-to-Model transformation accuracy | QVT é essencial para automação e precisão em transformações, exigindo métricas de eficiência e qualidade                                          |
| **UML 2.4.1**                              | Maintainability, Compatibility                                             | UML é padrão largamente adotado, impactando compatibilidade e facilidade de manutenção                                                            |
| **SysML 1.4**                              | Reliability, Reusability                                                   | SysML suporta sistemas complexos, exigindo análise de confiabilidade e reutilização de componentes                                                |
| **SPEM (Software Process Engineering)**    | Performance Efficiency, Performance Effort                                 | SPEM influencia processos de desenvolvimento, afetando eficiência em atividades de modelagem e geração de código                                  |
| **DDS (Data Distribution Service)**        | Security, Latency (Time behavior)                                          | DDS é crítico para sistemas distribuídos, exigindo segurança e controle de latência                                                               |
| **MDA Guide**                              | Conformance, Interoperability                                              | Guia OMG é referência para conformância e interoperabilidade entre ferramentas                                                                    |
| **SBVR (Semantic of Business Vocabulary)** | Usability, Understandability                                               | SBVR padroniza vocabulário de domínio, impactando compreensão do modelo por desenvolvedores                                                       |
| **XMI 2.4.2**                              | Compatibility, Model Storage                                               | XMI é formato de troca de metadados, influenciando na compatibilidade e integridade do modelo                                                     |
| **Emerging Standards (ex: SAROS)**         | Scalability                                                                | Novas normas em pesquisa podem introduzir novos atributos                                                                                         |

*Nota: Esta matriz será expandida conforme validação de cada norma. Por exemplo, QVT pode ser vinculado indiretamente à Maintainability se melhorar a modularidade dos modelos.*

---

*Documento consolidado em 23/07/2026 a partir de: 260723_omg_research.md, 260723_checklist_normas_omg.md, 260723_atributos.md, 260723_matrix_mda_atributos.md.*
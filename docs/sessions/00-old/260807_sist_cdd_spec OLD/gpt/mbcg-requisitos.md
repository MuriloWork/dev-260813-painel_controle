
ID do Documento: MBCG-REQ-00
Sistema: MB-Code-Generator
Tipo de Documento: Baseline de Requisitos
Metodologia: MBSE
Status: Rascunho
Versão: 0.1
Data: 2026-08-10

---

# 1. BRD — Business Requirements Document

## 1.1. Objetivo

O MB-Code-Generator (MBCG) é um sistema de Geração de Código Baseada em Modelos (Model-Based Code Generation) destinado a apoiar a especificação, modelagem, validação e implementação de sistemas de software por meio da combinação de:

- requisitos estruturados;
- conhecimento descritivo;
- modelos formais de sistemas;
- rastreabilidade;
- grafos de conhecimento;
- agentes de IA;
- inteligência de engenharia reutilizável;
- templates e regras de geração;
- geração automatizada de código.

O próprio MBCG deverá ser desenvolvido utilizando os mesmos princípios de desenvolvimento baseado em modelos que oferece aos sistemas que gera.

---

## 1.2. Contexto de Negócio

O desenvolvimento tradicional de software distribui o conhecimento entre diversos artefatos:

Requisitos
    |
    +-- Documentos
    +-- Diagramas
    +-- Código-fonte
    +-- Testes
    +-- Decisões
    +-- Issues
    +-- Conhecimento informal

Essa fragmentação dificulta a manutenção da consistência e da rastreabilidade entre:

Necessidade de negócio
        ↓
Requisito
        ↓
Função
        ↓
Arquitetura
        ↓
Modelo
        ↓
Implementação
        ↓
Verificação

O MBCG deverá fornecer um ambiente no qual esses artefatos possam ser relacionados e progressivamente transformados.

---

## 1.3. Problemas de Negócio

BR-001 — Fragmentação do Conhecimento de Engenharia

O conhecimento de engenharia de software encontra-se distribuído entre documentos, diagramas, código-fonte e outros artefatos.

Necessidade: estabelecer uma estrutura integrada de conhecimento que conecte esses artefatos.

---

BR-002 — Rastreabilidade Insuficiente

É difícil determinar como um requisito de negócio está representado na arquitetura, nos modelos e na implementação.

Necessidade: estabelecer relações de rastreabilidade explícitas e navegáveis.

---

BR-003 — Perda da Intenção de Projeto

A implementação tende a se tornar a representação dominante do sistema, enquanto as decisões arquiteturais e a intenção de projeto tornam-se difíceis de recuperar.

Necessidade: manter o conhecimento do sistema independentemente da implementação.

---

BR-004 — Trabalho Repetitivo de Desenvolvimento

Muitas estruturas de implementação são repetitivas e podem ser derivadas de modelos, regras e templates.

Necessidade: automatizar a geração de artefatos de implementação quando apropriado.

---

BR-005 — Uso Ineficiente de IA

Agentes de IA precisam acessar o conhecimento correto no momento correto. Fornecer indiscriminadamente todo o projeto é ineficiente e pode reduzir a confiabilidade.

Necessidade: fornecer conhecimento estruturado, navegável e recuperável seletivamente.

---

BR-006 — Divergência entre Modelo e Implementação

A implementação pode divergir do modelo pretendido.

Necessidade: detectar, analisar e gerenciar divergências entre especificações, modelos e implementação.

---

BR-007 — Ausência de Inteligência de Engenharia Reutilizável

Práticas de engenharia, como regras de modelagem, regras arquiteturais, padrões de geração e procedimentos de validação, frequentemente permanecem incorporadas ao conhecimento individual dos profissionais.

Necessidade: capturar explicitamente a inteligência de engenharia reutilizável.

---

## 1.4. Objetivos de Negócio

BO-001 — Desenvolvimento Baseado em Modelos

Estabelecer modelos do sistema como artefatos de engenharia de primeira classe.

BO-002 — Rastreabilidade

Manter rastreabilidade entre requisitos, funções, modelos, implementação e verificação.

BO-003 — Geração de Código Controlada

Gerar artefatos de implementação a partir de especificações e modelos validados.

BO-004 — Engenharia Assistida por IA

Permitir que agentes de IA participem das atividades de engenharia utilizando conhecimento e regras explícitos.

BO-005 — Reutilização de Conhecimento

Permitir a reutilização de skills, regras, templates, modelos e estratégias de geração.

BO-006 — Interoperabilidade

Minimizar a dependência de uma ferramenta específica de modelagem, modelo de IA, framework de agentes ou tecnologia de geração de código.

BO-007 — Usabilidade Humana e Computacional

Manter representações de conhecimento úteis tanto para engenheiros humanos quanto para agentes de IA.

---

# 2. Arquitetura de Conhecimento do Sistema

O MBCG deverá gerenciar três bases de conhecimento logicamente distintas.

## 2.1. KB-01 — Base de Conhecimento do Sistema-Alvo

Contém o conhecimento sobre o sistema de software que está sendo desenvolvido.

KB-01
Sistema-Alvo
    |
    +-- Requisitos de Negócio
    +-- Requisitos Funcionais
    +-- Arquitetura
    +-- UML
    +-- Decisões
    +-- Restrições
    +-- Rastreabilidade
    +-- Especificações de Geração

---

## 2.2. KB-02 — Base de Conhecimento do MB-Code-Generator

Contém o conhecimento sobre o próprio MBCG.

KB-02
MB-Code-Generator
    |
    +-- Requisitos
    +-- Arquitetura
    +-- UML
    +-- Componentes
    +-- Interfaces
    +-- Algoritmos
    +-- Motor de Geração
    +-- Motor de Conhecimento
    +-- Harness de Agentes

---

## 2.3. KB-03 — Base de Conhecimento de Inteligência

Contém o conhecimento que descreve como as atividades de engenharia devem ser realizadas.

KB-03
Inteligência de Engenharia
    |
    +-- Skills
    +-- Regras
    +-- Políticas
    +-- Workflows
    +-- Templates
    +-- Convenções de Modelagem
    +-- Convenções de Geração
    +-- Regras de Validação

A distinção conceitual é:

KB-01 = O QUE está sendo construído
KB-02 = O QUE constrói o sistema
KB-03 = COMO o trabalho deve ser realizado

---

# 3. Requisitos de Negócio dos Usuários

| req                                  | descrição                                                                                                               |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| BR-101 — Conhecimento do Projeto     | O sistema deverá fornecer uma base de conhecimento estruturada para cada sistema-alvo.                                  |
| BR-102 — Gerenciamento de Requisitos | O sistema deverá permitir a definição e o gerenciamento dos requisitos do sistema.                                      |
| BR-103 — Decomposição Funcional      | O sistema deverá permitir a decomposição das capacidades do sistema em funções.                                         |
| BR-104 — Modelagem Formal            | O sistema deverá suportar modelos formais de sistemas, inicialmente baseados em UML.                                    |
| BR-105 — Relações de Conhecimento    | O sistema deverá suportar relações explícitas entre os artefatos de engenharia.                                         |
| BR-106 — Rastreabilidade             | O sistema deverá permitir a navegação pelas cadeias de rastreabilidade.                                                 |
| BR-107 — Recuperação de Conhecimento | O sistema deverá permitir a recuperação somente do conhecimento relevante para uma determinada atividade de engenharia. |
| BR-108 — Agentes de IA               | O sistema deverá fornecer aos agentes acesso controlado ao conhecimento de engenharia.                                  |
| BR-109 — Inteligência de Engenharia  | O sistema deverá suportar skills, regras, workflows e templates reutilizáveis.                                          |
| BR-110 — Validação                   | O sistema deverá validar requisitos, modelos, relações e pré-condições para geração.                                    |
| BR-111 — Geração de Código           | O sistema deverá gerar artefatos de implementação a partir de especificações e modelos.                                 |
| BR-112 — Impacto de Mudanças         | O sistema deverá permitir a análise do impacto potencial de mudanças.                                                   |
| BR-113 — Regeneração                 | O sistema deverá permitir a regeneração dos artefatos de implementação afetados.                                        |



# 4. FBS — Functional Breakdown Structure

A FBS representa o que o sistema deve fazer, independentemente de como será implementado.

MB-CODE-GENERATOR
## 4.1. F1 — Gerenciar Conhecimento de Engenharia
│   │
│   ├── F1.1 Criar conhecimento
│   ├── F1.2 Ler conhecimento
│   ├── F1.3 Atualizar conhecimento
│   ├── F1.4 Versionar conhecimento
│   ├── F1.5 Organizar conhecimento
│   └── F1.6 Recuperar conhecimento
│
## 4.2. F2 — Especificar Sistema
│   │
│   ├── F2.1 Capturar requisitos de negócio
│   ├── F2.2 Definir requisitos do sistema
│   ├── F2.3 Definir restrições
│   ├── F2.4 Definir casos de uso
│   ├── F2.5 Definir critérios de aceitação
│   └── F2.6 Estabelecer baseline de requisitos
│
## 4.3. F3 — Decompor Sistema
│   │
│   ├── F3.1 Decompor capacidades
│   ├── F3.2 Definir funções
│   ├── F3.3 Definir relações funcionais
│   └── F3.4 Alocar requisitos às funções
│
## 4.4. F4 — Modelar Sistema
│   │
│   ├── F4.1 Criar modelo UML
│   ├── F4.2 Importar modelo UML
│   ├── F4.3 Exportar modelo UML
│   ├── F4.4 Gerenciar elementos do modelo
│   ├── F4.5 Gerenciar diagramas
│   └── F4.6 Validar modelo
│
## 4.5. F5 — Gerenciar Arquitetura
│   │
│   ├── F5.1 Definir arquitetura
│   ├── F5.2 Definir componentes
│   ├── F5.3 Definir interfaces
│   ├── F5.4 Definir dependências
│   └── F5.5 Registrar decisões arquiteturais
│
## 4.6. F6 — Gerenciar Rastreabilidade
│   │
│   ├── F6.1 Criar rastreabilidade
│   ├── F6.2 Navegar pela rastreabilidade
│   ├── F6.3 Analisar dependências
│   ├── F6.4 Analisar impacto
│   └── F6.5 Validar rastreabilidade
│
## 4.7. F7 — Gerenciar Grafo de Conhecimento
│   │
│   ├── F7.1 Construir grafo
│   ├── F7.2 Atualizar grafo
│   ├── F7.3 Consultar grafo
│   ├── F7.4 Percorrer grafo
│   └── F7.5 Visualizar grafo
│
## 4.8. F8 — Suportar Agentes de IA
│   │
│   ├── F8.1 Descobrir conhecimento
│   ├── F8.2 Recuperar contexto
│   ├── F8.3 Consultar modelos
│   ├── F8.4 Executar skills
│   ├── F8.5 Aplicar regras
│   ├── F8.6 Executar workflows
│   └── F8.7 Validar ações do agente
│
## 4.9. F9 — Validar Artefatos de Engenharia
│   │
│   ├── F9.1 Validar requisitos
│   ├── F9.2 Validar funções
│   ├── F9.3 Validar modelos
│   ├── F9.4 Validar arquitetura
│   ├── F9.5 Validar rastreabilidade
│   └── F9.6 Validar prontidão para geração
│
## 4.10. F10 — Gerar Software
│   │
│   ├── F10.1 Selecionar alvo de geração
│   ├── F10.2 Selecionar templates
│   ├── F10.3 Aplicar regras de geração
│   ├── F10.4 Gerar código-fonte
│   ├── F10.5 Gerar configuração
│   ├── F10.6 Gerar documentação
│   └── F10.7 Reportar resultados da geração
│
## 4.11. F11 — Gerenciar Evolução do Sistema
    │
    ├── F11.1 Detectar mudanças
    ├── F11.2 Analisar impacto
    ├── F11.3 Identificar artefatos afetados
    ├── F11.4 Regenerar artefatos
    ├── F11.5 Detectar divergências
    └── F11.6 Manter baselines

---

# 5. Princípio de Decomposição da FBS

A FBS deverá permanecer independente das tecnologias de implementação.

Por exemplo:

F10 — Gerar Software

é uma função do sistema.

Ela não deverá ser inicialmente decomposta como:

F10
 ├── Python
 ├── Jinja
 ├── LangChain
 └── OpenAI API

Esses elementos são decisões de implementação ou arquitetura.

A FBS descreve o que deve acontecer, e não como isso será implementado.

---

# 6. Macro Plan

O Macro Plan representa as principais ações necessárias para desenvolver o MBCG.

Ele não constitui, neste momento, um cronograma detalhado do projeto.

---

## 6.1. MP-01 — Estabelecer Fundamentos MBSE

Objetivo

Estabelecer a linguagem, a estrutura e as convenções do MBCG.

Ações

- definir terminologia do sistema;
- definir taxonomia de documentos;
- definir IDs dos artefatos;
- definir convenções de Markdown/frontmatter;
- definir convenções de links;
- definir convenções de status e versão;
- definir os limites das três bases de conhecimento.

Saídas

Terminologia
Taxonomia de Documentos
Convenção de Identificação de Artefatos
Definição dos Limites das KBs

---

## 6.2. MP-02 — Estabelecer Baseline de Requisitos

Objetivo

Criar uma baseline coerente de requisitos.

Ações

- desenvolver BRD;
- desenvolver FBS;
- derivar requisitos do sistema;
- identificar requisitos não funcionais;
- estabelecer rastreabilidade inicial.

Saídas

BRD
FBS
Requisitos do Sistema
Requisitos Não Funcionais
Rastreabilidade Inicial

---

## 6.3. MP-03 — Estabelecer Arquitetura de Conhecimento

Objetivo

Definir como o conhecimento de engenharia será representado e recuperado.

Ações

- definir convenções OKF/Markdown;
- definir metadados;
- definir tipos de conceitos;
- definir tipos de relações;
- definir estrutura de índices;
- definir divulgação progressiva do conhecimento;
- definir projeção em grafo;
- definir estratégia de recuperação.

Saídas

Modelo de Conhecimento
Convenção OKF
Modelo de Grafo
Modelo de Recuperação

---

## 6.4. MP-04 — Estabelecer Modelagem Formal

Objetivo

Definir modelos formais como artefatos de primeira classe do sistema.

Ações

- estabelecer convenções de modelagem UML;
- avaliar Gaphor;
- definir estrutura de pacotes UML;
- definir identificação dos elementos do modelo;
- investigar XMI;
- investigar PyEcore;
- definir representação do modelo canônico.

Saídas

Convenção UML
Estratégia de Intercâmbio XMI
Modelo Canônico

---

## 6.5. MP-05 — Estabelecer Rastreabilidade

Objetivo

Criar uma estratégia formal de rastreabilidade.

Ações

Definir relações como:

derive
decompose
satisfy
refine
realize
implement
verify
trace
depend-on
generate-from

Estabelecer regras de propriedade das relações entre:

Requirement
Function
Architecture
UML
Code
Test

Saídas

Modelo de Rastreabilidade
Taxonomia de Relações
Regras de Rastreabilidade

---

## 6.6. MP-06 — Estabelecer Grafo de Conhecimento

Objetivo

Fornecer navegação baseada em grafo para o conhecimento de engenharia.

Ações

- derivar grafo das relações Markdown;
- derivar grafo das relações UML;
- definir nós do grafo;
- definir arestas do grafo;
- implementar navegação;
- avaliar visualização;
- avaliar persistência do grafo.

Saídas

Grafo de Conhecimento
Construtor do Grafo
Modelo de Consulta do Grafo
Visualização do Grafo

---

## 6.7. MP-07 — Estabelecer Base de Inteligência

Objetivo

Capturar a inteligência de engenharia independentemente do conhecimento específico de cada projeto.

Ações

Definir:

Skills
Regras
Políticas
Workflows
Templates
Regras de Validação
Convenções de Modelagem
Convenções de Geração

Saídas

Base de Inteligência
Catálogo de Skills
Catálogo de Regras
Catálogo de Templates
Catálogo de Workflows

---

## 6.8. MP-08 — Estabelecer Interface para Agentes

Objetivo

Permitir que agentes trabalhem sobre o conhecimento de engenharia.

Ações

- definir Knowledge API;
- implementar recuperação de conceitos;
- implementar recuperação de seções;
- implementar navegação pelo grafo;
- implementar consultas aos modelos;
- implementar consultas de rastreabilidade;
- implementar modificações controladas;
- implementar feedback de validação.

Saídas

Knowledge API
Construtor de Contexto para Agentes
Operações para Agentes
Interface de Validação

---

## 6.9. MP-09 — Estabelecer Geração Baseada em Modelos

Objetivo

Transformar modelos validados em artefatos de implementação.

Ações

- definir alvos de geração;
- definir mapeamentos modelo → código;
- definir templates;
- definir regras de geração;
- implementar geradores;
- validar artefatos gerados;
- estabelecer estratégia de regeneração.

Saídas

Modelo de Geração
Templates
Regras de Geração
Geradores de Código
Artefatos Gerados

---

## 6.10. MP-10 — Estabelecer Verificação e Evolução

Objetivo

Garantir que o sistema permaneça consistente durante sua evolução.

Ações

- validar requisitos;
- validar modelos;
- validar rastreabilidade;
- validar código gerado;
- detectar divergência entre modelo e código;
- realizar análise de impacto;
- regenerar artefatos afetados;
- manter baselines.

Saídas

Modelo de Verificação
Regras de Consistência
Análise de Impacto
Processo de Regeneração
Gerenciamento de Baselines

---

# 7. Cadeia Inicial de Rastreabilidade MBSE

A cadeia inicial de rastreabilidade é:

BRD
 │
 │ motiva
 ▼
Requisito de Negócio
 │
 │ decompõe-se em
 ▼
Função
 │
 │ é realizada por
 ▼
Requisito do Sistema
 │
 │ é alocado a
 ▼
Arquitetura / Modelo
 │
 │ é implementado por
 ▼
Artefato de Código
 │
 │ é verificado por
 ▼
Artefato de Verificação

A cadeia relacionada à inteligência é:

Atividade de Engenharia
        │
        │ utiliza
        ▼
      Skill
        │
        │ governada por
        ▼
       Regra
        │
        │ utiliza
        ▼
     Template
        │
        ▼
Artefato Gerado

---

# 8. Considerações Iniciais de Requisitos Não Funcionais

As seguintes questões deverão ser detalhadas posteriormente em um documento específico de requisitos não funcionais:

- legibilidade humana;
- legibilidade por máquina;
- versionamento;
- reprodutibilidade;
- interoperabilidade;
- geração determinística;
- auditabilidade;
- explicabilidade;
- recuperação incremental;
- escalabilidade;
- segurança;
- extensibilidade.

---

# 9. Questões em Aberto

As seguintes questões permanecem deliberadamente abertas para documentos MBSE posteriores:

1. Qual será o metamodelo exato do MBCG?
2. Quais elementos UML serão obrigatórios?
3. Quais conceitos SysML, se houver, deverão ser adotados?
4. Quais artefatos serão autoritativos em Markdown e quais serão autoritativos em UML?
5. Qual será a taxonomia exata das relações de rastreabilidade?
6. O que constituirá o modelo canônico?
7. Qual será o conjunto mínimo da Knowledge API necessário aos agentes?
8. Quando deverá ser utilizada navegação por grafo em vez de recuperação textual?
9. Quando deverá ser introduzida recuperação vetorial/semântica?
10. Quais partes do MBCG serão geradas a partir de seus próprios modelos?
11. Quais artefatos serão gerados e quais permanecerão como autoria manual?
12. Como os artefatos gerados serão relacionados de volta aos elementos do modelo?

---

# 10. Próximos Documentos MBSE

Os próximos documentos deverão ser derivados desta baseline de requisitos, e não desenvolvidos de forma independente.

Sequência sugerida:

mb-code-generator-requirements_00.md
              │
              ├── mb-code-generator-fbs_00.md
              │
              ├── mb-code-generator-architecture_00.md
              │
              ├── mb-code-generator-knowledge-model_00.md
              │
              ├── mb-code-generator-traceability_00.md
              │
              ├── mb-code-generator-uml-model_00.md
              │
              ├── mb-code-generator-intelligence_00.md
              │
              ├── mb-code-generator-agent_00.md
              │
              ├── mb-code-generator-generation_00.md
              │
              └── mb-code-generator-verification_00.md

Os IDs deste documento ("BR-*", "BO-*", "F*", "MP-*") deverão permanecer estáveis à medida que o projeto evoluir. Os documentos posteriores deverão referenciar esses IDs em vez de duplicar suas definições.A estrutura já começa a formar uma baseline MBSE coerente: BRD → FBS → requisitos → arquitetura/modelos → geração → verificação, enquanto a KB-03 introduz uma segunda dimensão de rastreabilidade: atividade → skill → regra → template → artefato.
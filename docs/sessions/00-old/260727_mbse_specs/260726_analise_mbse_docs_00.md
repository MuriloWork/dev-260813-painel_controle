# 1. mapa mental de atributos

## 1.1. MBSE - Model Based Software Engineering
 

- [[260617_conceitos_info#2.1.3. Three Models|modelos OOP]]
- [[260617_conceitos_info#2.2.1. UML - Unified Modeling Language|UML - Unified Modeling Language]]
## 1.2. MBSE tools 

[Eclipse Papyrus](https://eclipse.dev/papyrus/)
[Modelio](https://github.com/ModelioOpenSource/Modelio)
[Gaphor](https://github.com/gaphor/gaphor)
[UML tools for Python](https://modeling-languages.com/uml-tools/#:~:text=tools%20satisfy%20them.-,UML%20tools%20for%20Python,-Are%20UML%20tools)
[BESSER Web Modeling Editor](https://github.com/BESSER-PEARL/BESSER-Web-Modeling-Editor#besser-web-modeling-editor)
[Sirius](https://modeling-languages.com/sirius-eclipse-obeo-graphical-modeling-tool/)

## 1.3. SSD - Spec Driven Development 

# 2. sistema

- recursos
	- model database
	- code database
	- design rules
- pipeline
	- engenharia reversa codigo ⟶ modelo
	- criar modelo
	- relatórios 
	- criar codigo
	- revisar codigo

# 3. docs tree


| folder            | docs   | descrição |
| ----------------- | ------ | --------- |
|                   | readme |           |
| agents            |        |           |
| spec              |        |           |
| coding rules      |        |           |
| gsd-planning      |        |           |
| code-review-graph |        |           |

# 4. templates
## 4.1. readme
### 4.1.1. versão atual do sistema
#### 4.1.1.1. funcionalidades
#### 4.1.1.2. gsd-codebase
- STACK.md        - Technologies and dependencies
- ARCHITECTURE.md - System design and patterns
- STRUCTURE.md    - Directory layout and organisation
- INTEGRATIONS.md - External services and APIs
### 4.1.2. desenvolvimento do sistema
#### 4.1.2.1. spec + status
#### 4.1.2.2. gsd-planning
### 4.1.3. instruções para desenvolvimento
#### 4.1.3.1. spec-driven
- harness pipeline
### 4.1.4. docs index
#### 4.1.4.1. coding rules
#### 4.1.4.2. spec templates
#### 4.1.4.3. agents

## 4.2. agents

## 4.3. spec + status

### 4.3.1. resumo

No Specification-Driven Development (SDD), o maior desafio não é apenas documentar os requisitos, mas manter a rastreabilidade entre versões de:

> Necessidade de negócio → Comportamento do sistema → Componentes da arquitetura → Código → Testes

| pasta | Documento                                                                          | Objetivo                               | Público                        | Nível      |
| ----- | ---------------------------------------------------------------------------------- | -------------------------------------- | ------------------------------ | ---------- |
|       | **PRD (Product Requirements Document)**                                            | O que será construído                  | Produto + Negócio + Engenharia | Alto       |
|       | **SRD/SRS (Software Requirements Document / Software Requirements Specification)** | Requisitos funcionais e não funcionais | Engenharia                     | Médio      |
|       | **Architecture Document (SAD)**                                                    | Arquitetura do sistema                 | Arquitetura + Desenvolvimento  | Médio      |
|       | **Feature Specifications**                                                         | Cada funcionalidade                    | Desenvolvedores                | Detalhado  |
|       | **Use Cases**                                                                      | Fluxos de execução                     | Desenvolvedores                | Detalhado  |

### 4.3.2. PRD

#### 4.3.2.1. resumo

Visão geral do sistema

Ele responde:
- Qual problema estamos resolvendo?
- Quem é o usuário?
- Quais funcionalidades existirão?
- Quais são as prioridades?
- Como medir sucesso?

Exemplo:

Sistema de Gestão de Eventos

Objetivo
Organizar eventos.

Principais Features

F001 Cadastro

F002 Planejamento

F003 Orçamento

F004 Cronograma

F005 Exportação Excel

F006 Sincronização

Fora do Escopo

Aplicativo iOS

Indicadores

Tempo para criar evento

Quantidade de eventos

O PRD normalmente não entra em detalhes de implementação.


---

### 4.3.3. SRD (ou SRS)

#### 4.3.3.1. instruções 

O SRD é muito mais técnico. Enquanto o PRD diz:

> O sistema deve permitir importar planilhas.

O SRD detalha:

RF-21
- O sistema deverá importar arquivos XLSX.
- Campos obrigatórios [SKU, Quantidade, Preço, Descrição]
- Em caso de erro [Linha, Campo, Mensagem]

#### 4.3.3.2. exemplo

##### 4.3.3.2.1. general requirements 
##### 4.3.3.2.2. specific requirements 
##### 4.3.3.2.3. components architecture 
##### 4.3.3.2.4. data entities 
##### 4.3.3.2.5. data api
##### 4.3.3.2.6. data store
##### 4.3.3.2.7. infinite scroll 
##### 4.3.3.2.8. optimization 
##### 4.3.3.2.9. accessibility 



### 4.3.4. Architecture Document (SAD)

Presentation ⟶ Application ⟶ Domain ⟶ Infrastructure

- Responde se a arquitetura:
  - satisfaz os objetivos de negocio
  - está conforme as constraints
  - atende os atributos de qualidade
  - é a solução de menor risco/custo
- Explica:
  - módulos
  - componentes
  - bancos
  - APIs
  - integrações
  - padrões arquiteturais

### 4.3.5. Feature Specification

Cada Feature ganha um documento próprio.

Feature

Importar Excel

Objetivo

Regras

Entradas

Saídas

Erros

Critérios de Aceitação


---

Use Case

Mostra o fluxo.

Seleciona arquivo

↓

Valida

↓

Importa

↓

Atualiza Grid

↓

Salva


---



É o documento central.

Define:

objetivo da funcionalidade

regras de negócio

fluxos

entradas

saídas

exceções


Exemplo:

Feature: Emitir Nota Fiscal

Regras:
- Somente pedidos pagos
- Validar estoque
- Gerar XML
- Enviar para SEFAZ

Cada feature recebe um identificador.

F-001 Emitir Nota
F-002 Cancelar Nota
F-003 Reemitir DANFE

Esses IDs serão usados em toda a arquitetura.


---

### 4.3.6. Use Cases / User Stories

Descrevem o comportamento esperado.

Exemplo

UC-15 Emitir Nota

Ator:
Operador

Fluxo Principal

1 Seleciona pedido
2 Sistema valida estoque
3 Sistema gera XML
4 Sistema envia para SEFAZ

Cada passo pode ser implementado por vários componentes.


---

### 4.3.7. Architecture Decision Records (ADR)

Não relacionam diretamente funções ao código.

Relacionam:

Por que escolhemos
Clean Architecture

Por que usamos
CQRS

Por que existe um Aggregate

Por que existe um Event

São documentos importantes para explicar a arquitetura.


---

### 4.3.8. Component Mapping 

É provavelmente o documento que você procura.

Ele faz a ligação entre funcionalidades e componentes.

Exemplo

| Feature | Use Case | Camada         | Classe       | Método         |
| ------- | -------- | -------------- | ------------ | -------------- |
| F001    | UC15     | Application    | OrderService | issueInvoice() |
| F001    | UC15     | Domain         | Invoice      | validate()     |
| F001    | UC15     | Infrastructure | SefazGateway | sendXml()      |


Esse tipo de matriz é muito usado em sistemas grandes.


---

### 4.3.9. Traceability Matrix 

É o documento clássico de engenharia de software.

Relaciona tudo.

| Requirement | Feature | Classe         | Teste |
| ----------- | ------- | -------------- | ----- |
| R001        | F001    | InvoiceService | T45   |
| R002        | F001    | XmlGenerator   | T46   |


Em projetos regulados (aviação, medicina, automotivo) isso é praticamente obrigatório.


---

### 4.3.10. Sequence Diagrams

Mostram quem chama quem.

UI

↓

Controller

↓

Application Service

↓

Domain

↓

Repository

↓

Database

São excelentes para visualizar uma funcionalidade.


---

### 4.3.11. Domain Model

Mostra:

Pedido

↓

Itens

↓

Pagamento

↓

Nota Fiscal

Relaciona entidades e regras.


---

### 4.3.12. Package Diagram

Relaciona módulos.

Orders

↓

Payments

↓

Invoices

↓

Notifications


---

### 4.3.13. C4 Model

Muito usado atualmente.

Níveis:

Context

↓

Containers

↓

Components

↓

Code

É excelente para localizar onde cada funcionalidade vive.


---

### 4.3.14. Código anotado

Em muitos projetos modernos, a especificação fica próxima do código.

Exemplo

// Feature F-015
// UC-22
// Requirement R-45

class InvoiceService {

    issueInvoice() {

    }

}

Ferramentas conseguem gerar rastreabilidade automaticamente a partir dessas anotações.


---

Em projetos modernos (SDD + IA)

Hoje muitas equipes mantêm uma estrutura como esta:

spec/

    features/

        F001.md

        F002.md

    use_cases/

        UC15.md

        UC16.md

    architecture/

        containers.md

        components.md

        sequence/

    traceability/

        matrix.csv

Depois, uma IA ou uma ferramenta consegue responder perguntas como:

Feature F001

↓

Use Case UC15

↓

Application

InvoiceService.issueInvoice()

↓

Domain

Invoice.validate()

↓

Infrastructure

XmlGenerator

↓

Repository

InvoiceRepository

Ou o caminho inverso:

Método

↓

Classe

↓

Componente

↓

Feature

↓

Regra de negócio


### 4.3.15. Qual a diferença entre Feature Specification e Use Case?

A principal diferença é o nível de abstração.

Feature Specification = "O que o sistema deve fazer"

A Feature Specification descreve uma capacidade do sistema do ponto de vista do negócio.

Ela responde perguntas como:

Qual problema resolve?

Quais regras de negócio existem?

Quais são os dados envolvidos?

Quais restrições existem?

Como sabemos que a feature está pronta?


Exemplo:

Feature: Emitir Nota Fiscal

Objetivo
Emitir nota fiscal para pedidos aprovados.

Entradas
- Pedido
- Cliente
- Itens

Saída
- XML
- DANFE

Regras

RN01
Somente pedidos pagos.

RN02
Cliente deve possuir CPF/CNPJ válido.

RN03
Todos os itens precisam possuir NCM.

RN04
Caso a SEFAZ esteja indisponível,
o pedido permanece pendente.

Perceba que aqui não existe passo a passo da interface.

Existe apenas a especificação do comportamento esperado.


---

Use Case = "Como essa feature acontece"

O Use Case descreve uma execução específica da feature.

Mesmo uma única Feature pode possuir vários Use Cases.

Por exemplo:

Feature

Emitir Nota Fiscal

Pode possuir:

UC01
Emitir nota normalmente

UC02
Emitir nota em contingência

UC03
Reemitir DANFE

UC04
Cancelar nota

UC05
Consultar status da nota

Cada Use Case possui o fluxo.

UC01

Ator
Operador

Fluxo principal

1 Seleciona pedido

2 Clica em Emitir

3 Sistema valida estoque

4 Sistema gera XML

5 Sistema envia à SEFAZ

6 Sistema salva protocolo

7 Sistema informa sucesso

Agora aparecem os passos.


---

Uma analogia

Imagine um carro.

A Feature seria:

Frear o veículo.

Já os Use Cases seriam:

Frear normalmente.

Frear em piso molhado.

Frear em descida.

Frear com ABS.

Frear com reboque.

A Feature define a capacidade.

Os Use Cases mostram as formas pelas quais essa capacidade é utilizada.


---

### 4.3.16. Em qual documento ficam os testes?

Essa é uma dúvida muito comum. A resposta é: depende do nível do teste.

Nível 1 — Critérios de Aceitação (na Feature Specification)

Na própria Feature você normalmente escreve:

Critérios de Aceitação

CA01

Dado um pedido pago

Quando emitir nota

Então deve gerar XML.

----------------

CA02

Dado um pedido não pago

Quando emitir nota

Então deve apresentar erro.

Esses critérios dizem quando a Feature está correta.

Eles não são casos de teste completos.


---

Nível 2 — Casos de Teste (Test Specification)

Em projetos maiores existe um documento separado.

Feature

F001 Emitir Nota

↓

Test Specification

TS001

TS002

TS003

TS004

Por exemplo:

TS001

Objetivo

Emitir nota normalmente

Pré-condição

Pedido pago

Entrada

Pedido 123

Resultado esperado

XML gerado
Protocolo salvo
Status Emitido

Outro teste:

TS007

Objetivo

Cliente sem CPF

Resultado esperado

Erro RN02
Nenhum XML criado


---

Nível 3 — Testes automatizados

Depois os testes automatizados referenciam o mesmo identificador.

Feature

F001

↓

Rule

RN03

↓

Acceptance

CA05

↓

Test

test_invoice_missing_ncm()

Assim fica fácil localizar o motivo da existência de um teste.


---

Uma estrutura que funciona muito bem

Em projetos modernos, gosto de separar assim:

spec/

    features/

        F001_emitir_nota.md
            Objetivo
            Regras
            Critérios de Aceitação

    use_cases/

        UC001_emitir.md

        UC002_cancelar.md

    tests/

        TS001_emitir_normal.md

        TS002_cliente_sem_cpf.md

        TS003_sefaz_indisponivel.md

Depois existe uma matriz de rastreabilidade:

Feature	Regra	Use Case	Teste

F001	RN01	UC01	TS001
F001	RN02	UC01	TS002
F001	RN03	UC01	TS003
F001	RN04	UC02	TS010


Essa organização tem uma vantagem importante: se a regra RN03 mudar, você consegue identificar imediatamente quais Use Cases e quais testes precisam ser atualizados.


---

Pelo tipo de sistema que você vem descrevendo nas conversas anteriores (com camadas bem definidas e interesse em agentes de IA), eu iria um passo além: faria cada Feature referenciar explicitamente as classes da arquitetura que a implementam (Application Service, Domain Service, Repository, etc.). Isso cria uma ligação direta entre especificação → arquitetura → código → testes, permitindo que uma IA navegue em qualquer direção com muito mais precisão.





## 4.4. coding rules

## 4.5. gsd-planning

- .planning/
	- PROJECT.md          ← descrição do projeto; capacidades existentes em "Validated"
	- REQUIREMENTS.md     ← HLT-01, HLT-02
	- ROADMAP.md          ← Fase 1, status: pending
	- STATE.md            ← memória de sessão
	- config.json         ← configurações do fluxo de trabalho
	- onboarding/SUMMARY.md ← status do onboarding e próximo comando
	- codebase/ 
		- STACK.md        (47 lines) - Technologies and dependencies
		- ARCHITECTURE.md (62 lines) - System design and patterns
		- STRUCTURE.md    (38 lines) - Directory layout and organisation
		- CONVENTIONS.md  (55 lines) - Code style and patterns
		- TESTING.md      (41 lines) - Test structure and practices
		- INTEGRATIONS.md (29 lines) - External services and APIs
		- CONCERNS.md     (33 lines) - Technical debt and issues

## 4.6. code-review-graph




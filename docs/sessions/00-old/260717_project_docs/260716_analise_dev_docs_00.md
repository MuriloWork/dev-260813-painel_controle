# 1. readme
## 1.1. versão atual do sistema
### 1.1.1. funcionalidades
### 1.1.2. gsd-codebase
- STACK.md        - Technologies and dependencies
- ARCHITECTURE.md - System design and patterns
- STRUCTURE.md    - Directory layout and organisation
- INTEGRATIONS.md - External services and APIs
## 1.2. desenvolvimento do sistema
### 1.2.1. spec + status
### 1.2.2. gsd-planning
## 1.3. instruções para desenvolvimento
### 1.3.1. spec-driven
- harness pipeline
## 1.4. docs index
### 1.4.1. coding rules
### 1.4.2. spec templates
### 1.4.3. agents

# 2. agents

# 3. spec + status

## 3.1. resumo

No Specification-Driven Development (SDD), o maior desafio não é apenas documentar os requisitos, mas manter a rastreabilidade entre versões de:

> Necessidade de negócio → Comportamento do sistema → Componentes da arquitetura → Código → Testes

| pasta | Documento                                                                          | Objetivo                               | Público                        | Nível      |
| ----- | ---------------------------------------------------------------------------------- | -------------------------------------- | ------------------------------ | ---------- |
|       | **PRD (Product Requirements Document)**                                            | O que será construído                  | Produto + Negócio + Engenharia | Alto       |
|       | **SRD/SRS (Software Requirements Document / Software Requirements Specification)** | Requisitos funcionais e não funcionais | Engenharia                     | Médio      |
|       | **Architecture Document (SAD)**                                                    | Arquitetura do sistema                 | Arquitetura + Desenvolvimento  | Médio      |
|       | **Feature Specifications**                                                         | Cada funcionalidade                    | Desenvolvedores                | Detalhado  |
|       | **Use Cases**                                                                      | Fluxos de execução                     | Desenvolvedores                | Detalhado  |

## 3.2. PRD

### 3.2.1. resumo

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

## 3.3. SRD (ou SRS)

### 3.3.1. instruções 

O SRD é muito mais técnico. Enquanto o PRD diz:

> O sistema deve permitir importar planilhas.

O SRD detalha:

RF-21
- O sistema deverá importar arquivos XLSX.
- Campos obrigatórios [SKU, Quantidade, Preço, Descrição]
- Em caso de erro [Linha, Campo, Mensagem]

### 3.3.2. exemplo

#### 3.3.2.1. general requirements 
#### 3.3.2.2. specific requirements 
#### 3.3.2.3. components architecture 
#### 3.3.2.4. data entities 
#### 3.3.2.5. data api
#### 3.3.2.6. data store
#### 3.3.2.7. infinite scroll 
#### 3.3.2.8. optimization 
#### 3.3.2.9. accessibility 



## 3.4. Architecture Document (SAD)

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

## 3.5. Feature Specification

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

## 3.6. Use Cases / User Stories

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

## 3.7. Architecture Decision Records (ADR)

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

## 3.8. Component Mapping 

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

## 3.9. Traceability Matrix 

É o documento clássico de engenharia de software.

Relaciona tudo.

| Requirement | Feature | Classe         | Teste |
| ----------- | ------- | -------------- | ----- |
| R001        | F001    | InvoiceService | T45   |
| R002        | F001    | XmlGenerator   | T46   |


Em projetos regulados (aviação, medicina, automotivo) isso é praticamente obrigatório.


---

## 3.10. Sequence Diagrams

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

## 3.11. Domain Model

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

## 3.12. Package Diagram

Relaciona módulos.

Orders

↓

Payments

↓

Invoices

↓

Notifications


---

## 3.13. C4 Model

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

## 3.14. Código anotado

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


## 3.15. Qual a diferença entre Feature Specification e Use Case?

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

## 3.16. Em qual documento ficam os testes?

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





# 4. coding rules

# 5. gsd-planning

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

# 6. code-review-graph

```excalidraw
{
	"type": "excalidraw",
	"version": 2,
	"source": "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag2.24.2",
	"elements": [
		{
			"id": "session-start",
			"type": "rectangle",
			"x": 400,
			"y": 20,
			"width": 200,
			"height": 50,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#c5f5b8",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roundness": {
				"type": 3
			},
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"seed": 1001,
			"version": 25,
			"versionNonce": 1002557287,
			"index": "a1",
			"isDeleted": false,
			"groupIds": [],
			"frameId": null,
			"boundElements": [
				{
					"type": "text",
					"id": "LjZAqlcV"
				},
				{
					"id": "ITjfOuS7",
					"type": "arrow"
				}
			],
			"updated": 1782487348136,
			"link": null,
			"locked": false,
			"hasTextLink": false,
			"customData": {
				"legacyTextWrap": true
			}
		}
	],
	"appState": {
		"theme": "light",
		"viewBackgroundColor": "#ffffff",
		"currentItemStrokeColor": "#1e1e1e",
		"currentItemBackgroundColor": "#e0e0e0",
		"currentItemFillStyle": "solid",
		"currentItemStrokeWidth": 2,
		"currentItemStrokeStyle": "solid",
		"currentItemRoughness": 1,
		"currentItemOpacity": 100,
		"currentItemFontFamily": 5,
		"currentItemFontSize": 16,
		"currentItemTextAlign": "left",
		"currentItemStartArrowhead": null,
		"currentItemEndArrowhead": "arrow",
		"currentItemArrowType": "elbow",
		"currentItemFrameRole": null,
		"scrollX": 167.4978299591274,
		"scrollY": 116.92897260930717,
		"zoom": {
			"value": 0.672266
		},
		"currentItemRoundness": "round",
		"gridSize": 20,
		"gridStep": 5,
		"gridModeEnabled": false,
		"gridColor": {
			"Bold": "rgba(217, 217, 217, 0.5)",
			"Regular": "rgba(230, 230, 230, 0.5)"
		},
		"currentStrokeOptions": null,
		"frameRendering": {
			"enabled": true,
			"clip": true,
			"name": true,
			"outline": true,
			"markerName": true,
			"markerEnabled": true
		},
		"objectsSnapModeEnabled": false,
		"activeTool": {
			"type": "hand",
			"customType": null,
			"locked": false,
			"fromSelection": false,
			"lastActiveTool": null
		},
		"disableContextMenu": false,
		"bindingPreference": "enabled",
		"isBindingEnabled": true,
		"isMidpointSnappingEnabled": true,
		"boxSelectionMode": "contain"
	},
	"prevTextMode": "parsed",
	"files": {}
}
```



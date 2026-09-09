MBCG — Model-Based-Code-Generator

# 1. conceitos MBCG
## 1.1. Sobre os conceitos MBSE adotados pelo MB-Code-Generator.

- Declaração. Qual conceito normalizado será utilizado em cada camada da especificação?
- Referência. De qual normativo, ou literatura de referência, vem o conceito? Resumir o conceito existente e instruir como deve ser utilizado no MBCG
- Estabelecimento de encadeamento lógico. As camadas e blocos das especificações de sistema são encadeados e inter-relacionados, gerando complexidade para suas definições, implementações e gerenciamento. Definir clara e detalhadamente quais serão as lógicas de relacionamento é fundamental para consistência das especificações. 

## 1.2. mapa mental 
- modelagem knowledge graph 
	- owl 
		- RFD - Resource Description Framework
			- sujeito ── relação ── objeto
	- gpt 
		- Sistema real
		- Domínio do sistema
		- Modelo conceitual
		- Entidades / conceitos
		- Propriedades
		- Relações
		- Restrições
		- Ontologia / modelo semântico
		- Representação OKF
		- Frontmatter + Body
- inteligência
	- domain independent model 
		- memória: sistemas de persistência de dados [repositorios, documentos, bancos de dados]
		- rede de assuntos: qualquer domínio pode ser estruturado em hierarquias ou em redes de assuntos relacionados 
		- trilhas de raciocínio: pesquisas sobre os dados, ou outros repositorios, podem identificar novos novos nós ou arestas na base
		- regras de julgamento, decisão: mapa de conhecimento secundário sobre como criticar o mapa de conhecimento principal 
		- aprendizado: mecanismo de melhoria do próprio modelo em si 
	- domain specific model = MBSE 
		- determinismo
		- system specific model = MBCG 
			- recursos combinados orquestração
- KB - Knowledge Bundle 
	- domain independent model 
	- domain specific model = MBSE 
		- software particular
		- qualidade
		- system specific model = MBCG 
- okf 
	- type
	- title
	- description
	- resource
	- tags
	- source
- Propósito
	- Transformar conhecimento formalizado em artefatos de software
	- Reduzir a distância entre intenção humana e implementação
	- Produzir software a partir de modelos, requisitos e regras
- Domínio do problema
	- Negócio
	- Usuário
	- Necessidade
	- Problema
	- Objetivo
	- Resultado esperado
	- Restrição
	- Premissa
- Conhecimento
	- Conceito
	- Definição
	- Termo
	- Regra
	- Princípio
	- Fato
	- Relação
	- Contexto
	- Decisão
- Requisitos
	- Requisito de negócio
		- Necessidade de negócio
		- Objetivo de negócio
		- Resultado de negócio
		- Regra de negócio
	- Requisito de usuário
		- Ator
		- Necessidade do usuário
		- Expectativa
	- Requisito funcional
		- Função
		- Serviço
		- Comportamento
	- Requisito não funcional
		- Qualidade
		- Desempenho
		- Segurança
		- Confiabilidade
		- Usabilidade
		- Restrição técnica
	- Critério de aceitação
	- Prioridade
	- Dependência
	- Rastreabilidade
- Estrutura funcional
	- Sistema
	- Subsistema
	- Capacidade
	- Função
	- Subfunção
	- Processo
	- Atividade
	- Tarefa
	- Operação
	- Hierarquia funcional
	- Fluxo funcional
	- Entrada
	- Saída
- Modelo
	- Modelo conceitual
	- Modelo lógico
	- Modelo físico
	- Modelo comportamental
	- Modelo estrutural
	- Modelo funcional
	- Modelo de dados
	- Modelo de domínio
	- Metamodelo
- Arquitetura
	- Sistema
	- Componente
	- Subcomponente
	- Interface
	- Serviço
	- Responsabilidade
	- Dependência
	- Composição
	- Conector
	- Camada
- Artefatos
	- Especificação
	- Documento
	- Modelo
	- Diagrama
	- Código-fonte
	- Configuração
	- Teste
	- Documentação
- Transformação
	- Origem
	- Destino
	- Regra de transformação
	- Mapeamento
	- Geração
	- Derivação
	- Validação
	- Refinamento
- Rastreabilidade
	- Origem
	- Derivação
	- Realização
	- Implementação
	- Verificação
	- Validação
	- Impacto
- Knowledge Bases
	- Knowledge Base
	- Domínio
	- Vocabulário
	- Ontologia
	- Modelo
	- Requisitos
	- Regras
- Templates
	- Metadados
	- Índices
	- Referências
	- Templates
	- Template de requisito de negócio
	- Template de requisito funcional
	- Template de requisito não funcional
	- Template de hierarquia funcional
	- Template de arquitetura
	- Template de componente
	- Template de interface
	- Template de caso de uso
	- Template de modelo
	- Template de rastreabilidade
- MBCG como sistema recursivo
	- O MBCG é definido por conhecimento
	- O conhecimento é estruturado segundo modelos
	- Os modelos são descritos por especificações
	- As especificações podem ser produzidas pelo próprio MBCG
	- Os templates definem como novos elementos são especificados
	- Os templates são derivados dos conceitos do próprio MBCG
	- O sistema pode utilizar seus próprios conceitos para descrever sua própria definição
	- Autodefinição recursiva
		- Conceito → especificação
		- Especificação → modelo
		- Modelo → template
		- Template → nova especificação
		- Nova especificação → evolução do conceito

## 1.3. camadas da especificação MBSE

### 1.3.1. resumo 
Sim. Agora ficou claro o papel de conceitos_mbcg: ele não é um glossário genérico do MBCG. Ele deve estabelecer a linguagem conceitual e as regras de encadeamento que posteriormente serão materializadas nos templates.

Para isso, eu separaria duas dimensões:

Camadas → níveis de abstração/especificação, do problema à implementação.

Blocos → tipos de informação/modelos que existem dentro de cada camada.


A referência mais sólida para a espinha dorsal é ISO/IEC/IEEE 15288:2023, complementada por ISO/IEC/IEEE 29148:2018 para engenharia de requisitos e pelo INCOSE Systems Engineering Handbook. A 15288 é especialmente adequada porque permite aplicar os processos em diferentes níveis da hierarquia do sistema; a 29148 trata explicitamente da produção e gerenciamento dos artefatos de requisitos. 

### 1.3.2. Proposta de camadas do MBCG

Eu recomendaria inicialmente 8 camadas, evitando colocar arquitetura, implementação e requisitos todos no mesmo nível:

- L0 — Contexto e Necessidade
	- Contexto
	- Stakeholders
	- Problema
	- Necessidade
	- Oportunidade
	- Objetivos
	- Resultados esperados
	- Restrições
	- Premissas
- L1 — Requisitos de Negócio e Stakeholders
	- Requisitos de negócio
	- Requisitos dos stakeholders
	- Capacidades requeridas
	- Benefícios
	- Critérios de sucesso
	- Regras de negócio
	- Critérios de aceitação
- L2 — Requisitos do Sistema
	- Requisitos funcionais
	- Requisitos de desempenho
	- Requisitos de qualidade
	- Requisitos de interface
	- Requisitos de dados
	- Requisitos de segurança
	- Restrições de design
	- Outros requisitos não funcionais
- L3 — Análise Funcional
	- Função
	- Subfunção
	- Hierarquia funcional
	- Fluxo funcional
	- Entrada
	- Saída
	- Controle
	- Mecanismo
	- Cenário
	- Comportamento
- L4 — Arquitetura Lógica
	- Elemento lógico
	- Responsabilidade
	- Serviço
	- Interface lógica
	- Fluxo lógico
	- Alocação de funções
	- Dependências
	- Colaboração
	- Estrutura lógica
- L5 — Arquitetura Física
	- Elemento físico
	- Componente
	- Subcomponente
	- Interface física
	- Conector
	- Tecnologia
	- Alocação lógica → física
	- Dependências físicas
	- Decisões arquiteturais
- L6 — Projeto e Implementação
	- Componente de software
	- Classe
	- Objeto
	- Módulo
	- Serviço
	- API
	- Banco de dados
	- Configuração
	- Código
	- Build
	- Deploy
- L7 — Verificação, Validação e Evidências
	- Verificação
	- Validação
	- Caso de teste
	- Procedimento de teste
	- Resultado
	- Evidência
	- Critério de verificação
	- Critério de validação
	- Conformidade
	- Não conformidade


Essa separação também preserva uma distinção importante da engenhae sria diste a mas:artetquiura funcional/lógica não deve ser confundida com a arquitetura física. A arquitetura lógica descreve o que o sistema precisa realizar de maneira independente da solução tecnológica; a física trata dos elementos que efetivamente realizam essa solução. Essa distinção é explicitamente utilizada em práticas de MBSE/INCOSE. 

### 1.3.3. blocos transversais:

Há um problema se tratarmos somente essas oito camadas: rastreabilidade, decisões, versões e critérios não pertencem a uma única camada.

Portanto, além das camadas L0–L7, eu criaria blocos transversais:

- Identidade
	- ID
	- Nome
	- Tipo
	- Versão
	- Status
- Semântica
	- Definição
	- Tipo conceitual
	- Vocabulário
	- Unidade
	- Domínio
- Relacionamentos
	- Deriva de
	- Satisfaz
	- Realiza
	- Contém
	- Decompõe
	- Aloca
	- Depende de
	- Interfaceia com
	- Verifica
	- Valida
- Rastreabilidade
	- Origem
	- Destino
	- Justificativa
	- Cobertura
	- Impacto
- Decisão
	- Problema
	- Alternativas
	- Critérios
	- Decisão
	- Justificativa
	- Consequência
- Gestão
	- Prioridade
	- Risco
	- Mudança
	- Baseline
	- Status
	- Responsável
- Evidência
	- Critério
	- Método
	- Resultado
	- Evidência
	- Conformidade

O ponto mais importante para o MBCG

Eu não faria o encadeamento simplesmente:
Negócio → Requisitos → Funções → Arquitetura → Código

Isso ainda é superficial para o sistema que estamos projetando.
O que precisamos definir em conceitos_mbcg é uma rede de relações tipadas:

### 1.3.4. relacionamentos 

**Necessidade**: é formalizada por → Requisito de negócio
**Requisito de negócio**: é refinado em → Requisito de stakeholder
**Requisito de stakeholder**: é refinado em → Requisito de sistema
**Requisito de sistema**: é realizado por → Função
**Função**: é decomposta em → Subfunções, é alocada a → Elemento lógico
**Elemento lógico**: é realizado por → Elemento físico
**Elemento físico**: é implementado por → Componente
**Componente**: é implementado por → Código
**Requisito**: é verificado por → Caso de teste, é validado por → Evidência
Cada elemento: pode derivar de → Elemento de nível superior, pode decompor-se em → Elementos de nível inferior

E existe uma relação transversal fundamental:

qualquer elemento de especificação pode ter identidade, definição, relações, justificativa, estado, versão e rastreabilidade.

É justamente aqui que o conceitos_mbcg começa a ficar interessante: ele não vai apenas declarar "o que é um requisito". Ele vai estabelecer quais conceitos podem existir em cada camada e quais relações podem ligar conceitos de uma camada a outra.

A 29148 é particularmente útil para essa parte porque não trata apenas da frase do requisito: ela define processos, características, atributos e itens de informação relacionados à engenharia e gestão de requisitos. 

### 1.3.5. resumo
Eu congelaria, por enquanto, esta estrutura

- Camadas
	- L0 — Contexto e Necessidade
	- L1 — Requisitos de Negócio e Stakeholders
	- L2 — Requisitos do Sistema
	- L3 — Análise Funcional
	- L4 — Arquitetura Lógica
	- L5 — Arquitetura Física
	- L6 — Projeto e Implementação
	- L7 — Verificação, Validação e Evidências
- Blocos transversais
	- Identidade
	- Semântica
	- Relacionamentos
	- Rastreabilidade
	- Decisão
	- Gestão
	- Evidência

A partir disso, o próximo passo natural é não criar ainda os templates. Primeiro precisamos montar uma matriz:

Camada × Bloco × Conceito × Relações permitidas × Referência normativa

Essa matriz será, na minha opinião, o verdadeiro núcleo de conceitos_mbcg; dela poderemos derivar de forma consistente o template de Requisitos de Negócio, depois o de Hierarquia Funcional, e assim por diante.

# 2. conceitos MBCG KB

## 2.1. Sobre este documento

Conceitos e Definições OKF adotados pelo MB-Code-Generator

Objetivo: Descrever o propósito deste documento e delimitar quais conceitos do Open Knowledge Format (OKF) serão adotados e normalizados para a estruturação e consumo das Knowledge Bases do MB-Code-Generator.

## 2.2. Especificações originais para produção dos documentos OKF

Listar os conceitos, elementos e termos originais do OKF utilizados pelo MB-Code-Generator, apresentando para cada um sua definição e seu papel na estrutura das KBs.

Identificar, para cada conceito adotado, o trecho correspondente da especificação OKF utilizada como base para sua definição.

O MB-Code-Generator adota como referência conceitual o modelo definido pelo OKF para representação de conhecimento em **Knowledge Bundles**, constituídos por documentos Markdown organizados hierarquicamente e complementados por YAML frontmatter. O OKF estabelece um conjunto mínimo de conceitos estruturais, semânticos e operacionais que permitem que o conhecimento seja produzido por pessoas, agentes ou processos e consumido por pessoas, agentes, interfaces, índices de busca e código determinístico. 

A produção das KBs do MBCG utiliza os seguintes conceitos originais do OKF.

### 2.2.1. Arquitetura fisica: Knowledge Bundle

**Definição:** Um _Knowledge Bundle_ é uma coleção autocontida e hierárquica de documentos de conhecimento. Constitui a unidade de distribuição do conhecimento no OKF. 

**Papel nas KBs:** O Knowledge Bundle representa a própria unidade de organização e distribuição de uma KB do MBCG, fisicamente representada pela pasta raiz. Sua estrutura é formada por uma árvore de diretórios e arquivos Markdown, permitindo organizar os conceitos em grupos e subgrupos de forma independente do domínio do conhecimento. ([GitHub](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md?utm_source=chatgpt.com "knowledge-catalog/okf/SPEC.md at main · GoogleCloudPlatform/knowledge-catalog · GitHub"))
#### 2.2.1.1. Documento: Index

**Definição:** `index.md` é um arquivo de nome reservado do OKF, opcional que enumera o conteúdo de um diretório e permite exposição progressiva do conhecimento antes da abertura dos documentos individuais.

**Papel nas KBs:** O Index fornece uma visão navegável da estrutura de uma KB, permitindo que pessoas e agentes descubram quais Concepts e subdiretórios estão disponíveis sem precisar carregar previamente todos os documentos. `index.md` possui semântica própria e, por isso, não é um Concept document. ([GitHub](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md?utm_source=chatgpt.com "knowledge-catalog/okf/SPEC.md at main · GoogleCloudPlatform/knowledge-catalog · GitHub"))

#### 2.2.1.2. Documento: Log

**Definição:** `log.md` é um arquivo opcional de nome reservado do OKF, utilizado para registrar o histórico de alterações de um determinado escopo da hierarquia.

**Papel nas KBs:** O Log registra cronologicamente alterações realizadas em uma parte da KB, fornecendo contexto histórico sobre sua evolução. Assim como `index.md`, possui significado estrutural próprio e não é um Concept document. ([GitHub](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md?utm_source=chatgpt.com "knowledge-catalog/okf/SPEC.md at main · GoogleCloudPlatform/knowledge-catalog · GitHub"))

#### 2.2.1.3. Documento: Concept

**Definição:** Um _Concept_ é uma unidade individual de conhecimento dentro de um bundle, representada por um documento Markdown. Pode representar um ativo concreto, como uma tabela ou API, uma ideia abstrata, como uma métrica ou processo de negócio, ou qualquer outro elemento que constitua conhecimento. O _Concept ID_ é o caminho do arquivo que representa o conceito dentro do bundle, com o sufixo `.md` removido.

**Papel nas KBs:** O Concept ID fornece a identidade do conceito a partir de sua localização no bundle, estabelecendo uma correspondência direta entre a identidade lógica do conhecimento e o caminho do documento que o representa. ([GitHub](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md?utm_source=chatgpt.com "knowledge-catalog/okf/SPEC.md at main · GoogleCloudPlatform/knowledge-catalog · GitHub"))


##### 2.2.1.3.1. Frontmatter

**Definição:** O _Frontmatter_ é o bloco de metadados YAML delimitado por `---` localizado no início de um documento Markdown.

**Papel nas KBs:** O Frontmatter contém os metadados estruturais e semânticos que permitem identificar, classificar e interpretar um Concept. No OKF v0.2, o campo `type` é obrigatório; outros campos, como `title`, `description`, `resource`, `tags`, proveniência, confiança e ciclo de vida, são opcionais conforme suas respectivas regras. ([GitHub](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md?utm_source=chatgpt.com "knowledge-catalog/okf/SPEC.md at main · GoogleCloudPlatform/knowledge-catalog · GitHub"))

###### 2.2.1.3.1.1. Type

**Definição:** `type` é uma string curta que identifica o tipo de um Concept. É o único campo de Frontmatter sempre obrigatório no OKF.

**Papel nas KBs:** O `type` permite que consumidores façam roteamento, filtragem e apresentação dos conceitos. Os valores de tipo não possuem registro centralizado; os produtores devem utilizar valores descritivos e autoexplicativos, enquanto os consumidores devem tolerar tipos desconhecidos. ([GitHub](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md?utm_source=chatgpt.com "knowledge-catalog/okf/SPEC.md at main · GoogleCloudPlatform/knowledge-catalog · GitHub"))

###### 2.2.1.3.1.2. Title

**Definição:** `title` é o nome legível por humanos utilizado para apresentação de um Concept.

**Papel nas KBs:** O `title` fornece uma identificação de apresentação do conceito, podendo ser utilizado em índices, interfaces e resultados de consulta. Quando ausente, o consumidor pode derivar um título a partir do nome do arquivo. ([GitHub](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md?utm_source=chatgpt.com "knowledge-catalog/okf/SPEC.md at main · GoogleCloudPlatform/knowledge-catalog · GitHub"))

###### 2.2.1.3.1.3. Description

**Definição:** `description` é um resumo de uma única frase que descreve o Concept.

**Papel nas KBs:** A descrição fornece uma representação concisa do conhecimento para utilização em índices, resultados de busca e visualizações preliminares do conteúdo. ([GitHub](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md?utm_source=chatgpt.com "knowledge-catalog/okf/SPEC.md at main · GoogleCloudPlatform/knowledge-catalog · GitHub"))

###### 2.2.1.3.1.4. Resource

**Definição:** `resource` é uma URI canônica que identifica o recurso subjacente ao Concept.

**Papel nas KBs:** O campo relaciona um Concept ao ativo que ele descreve quando esse ativo possui uma identidade ou localização própria. Para conceitos abstratos, o campo pode não estar presente. ([GitHub](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md?utm_source=chatgpt.com "knowledge-catalog/okf/SPEC.md at main · GoogleCloudPlatform/knowledge-catalog · GitHub"))

###### 2.2.1.3.1.5. Tags

**Definição:** `tags` é uma lista YAML de strings curtas utilizadas para categorização transversal dos conceitos.

**Papel nas KBs:** As tags permitem classificar Concepts independentemente da hierarquia de diretórios em que estão organizados. O OKF não define um formato específico de arquivos para agregação por tags; essa visão pode ser sintetizada pelo consumidor. ([GitHub](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md?utm_source=chatgpt.com "knowledge-catalog/okf/SPEC.md at main · GoogleCloudPlatform/knowledge-catalog · GitHub"))

###### 2.2.1.3.1.6. Source

**Definição:** Um _Source_ é um material do qual um Concept deriva, podendo ser externo ou interno ao bundle, registrado no campo `sources`.

**Papel nas KBs:** Source permite registrar as fontes utilizadas na produção de um conceito e estabelecer a base documental de suas afirmações. ([GitHub](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md?utm_source=chatgpt.com "knowledge-catalog/okf/SPEC.md at main · GoogleCloudPlatform/knowledge-catalog · GitHub"))


##### 2.2.1.3.2. Body

**Definição:** O _Body_ corresponde a todo o conteúdo do documento que aparece após o Frontmatter e utiliza Markdown padrão.

**Papel nas KBs:** O Body contém o conteúdo principal do conhecimento representado pelo Concept. O OKF recomenda o uso de Markdown estrutural — títulos, listas, tabelas e blocos de código — para favorecer a leitura humana e a recuperação por agentes. ([GitHub](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md?utm_source=chatgpt.com "knowledge-catalog/okf/SPEC.md at main · GoogleCloudPlatform/knowledge-catalog · GitHub"))

###### 2.2.1.3.2.1. Link

**Definição:** Um _Link_ é um link Markdown padrão entre um Concept e outro Concept, utilizado para expressar relacionamentos além da hierarquia implícita de pai e filho.

**Papel nas KBs:** Links estabelecem relações explícitas entre unidades de conhecimento e permitem que a coleção de documentos seja interpretada como uma estrutura de conhecimento interconectada. O tipo específico da relação não é codificado pelo link; seu significado é determinado pelo contexto textual em que o link aparece. ([GitHub](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md?utm_source=chatgpt.com "knowledge-catalog/okf/SPEC.md at main · GoogleCloudPlatform/knowledge-catalog · GitHub"))


### 2.2.2. Lógica semântica e operacional

Um corpus de conhecimento não é necessariamente criado uma única vez para depois ser apenas consultado: ele pode ser **continuamente produzido e mantido por agentes**. Quando a maior parte dos conceitos é gerada por máquinas, o consumidor precisa obter respostas que uma convenção simples de Markdown com frontmatter não torna explícitas:

- **Conformidade**: documento em conformidade com a especificação OKF?
- **Proveniência:** a partir de que fontes este conhecimento foi criado e como foi verificado?
- **Confiança:** quanto se deve confiar neste conhecimento?
- **Ciclo de vida:** ele representa a versão atualmente vigente?

O OKF v0.2 torna proveniência (provenance), confiança (trust), ciclo de vida (lifecycle), conformidade (conformance) e atestação (futuramente) conceitos de primeira classe, mantendo o formato deliberadamente pouco opinativo. Esses conceitos complementam a estrutura física do bundle e dos documentos de conceito, fornecendo as informações necessárias para que os consumidores avaliem a origem, a confiabilidade, a atualidade, o estado do ciclo de vida e a validade computacional do conhecimento.

#### 2.2.2.1. Provenance

**Definição:** *Provenance* é o conjunto de fontes das quais um Concept deriva. No OKF, a proveniência é registrada pelo campo `sources` do frontmatter.

**Papel nas KBs:** A Provenance permite registrar a origem do conhecimento e possibilita ao consumidor identificar os materiais a partir dos quais um Concept foi produzido. As fontes podem ser externas ou internas ao bundle e podem conter sinais objetivos de credibilidade que auxiliam o consumidor na avaliação da confiança do conhecimento.

##### 2.2.2.1.1. Credibility Signal

**Definição:** Um _Credibility Signal_ é um fato objetivo associado individualmente a uma Source — como `author`, `usage_count` ou `last_modified` — utilizado para inferir confiança. O OKF registra os sinais, mas não estabelece um veredito de credibilidade.

**Papel nas KBs:** Os sinais fornecem informações objetivas que podem ser utilizadas pelo consumidor para avaliar a confiança associada às fontes de um Concept, sem que o próprio OKF imponha uma pontuação ou julgamento único. ([GitHub](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md?utm_source=chatgpt.com "knowledge-catalog/okf/SPEC.md at main · GoogleCloudPlatform/knowledge-catalog · GitHub"))

#### 2.2.2.2. Trust

O OKF representa a confiança de forma distinta da autoria ou geração do conhecimento. O campo `generated` registra como o conteúdo atual foi produzido, enquanto `verified` registra quem ou o que confirmou o conteúdo em relação às suas fontes ou ao recurso descrito. A partir de `verified`, o consumidor pode derivar um *Trust Tier*. :contentReference[oaicite:5]{index=5}
##### 2.2.2.2.1. Trust Tier

**Definição:** _Trust Tier_ é um nível derivado do campo `verified` de um Concept, podendo representar os estados _unverified_, _machine-confirmed_ ou _human-reviewed_.

**Papel nas KBs:** O Trust Tier permite ao consumidor interpretar o estado de confiança de um Concept a partir das informações de verificação registradas no documento. ([GitHub](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md?utm_source=chatgpt.com "knowledge-catalog/okf/SPEC.md at main · GoogleCloudPlatform/knowledge-catalog · GitHub"))

##### 2.2.2.2.2. Actor

**Definição:** Um _Actor_ é uma string que identifica quem ou o que executou uma ação. O OKF define as convenções `<producer>/<version>` para agentes e ferramentas, `human:<id>` para pessoas e `process:<id>` para processos automatizados.

**Papel nas KBs:** Actor identifica a autoria ou confirmação associada a operações como geração e verificação do conhecimento, permitindo ao consumidor distinguir agentes, pessoas e processos responsáveis por essas ações. ([GitHub](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md?utm_source=chatgpt.com "knowledge-catalog/okf/SPEC.md at main · GoogleCloudPlatform/knowledge-catalog · GitHub"))

#### 2.2.2.3. Lifecycle

O *Lifecycle* representa o estado e a atualidade de um Concept ao longo do tempo. No OKF, essa dimensão é expressa pelos campos `status` e `stale_after`, permitindo distinguir o estado de ciclo de vida de um conceito de sua atualidade temporal. Ambos são opcionais. Na ausência de `status`, o conceito é considerado `stable`. :contentReference[oaicite:8]{index=8}

##### 2.2.2.3.1. Status

**Definição:** `status` identifica o estado de ciclo de vida de um Concept. O OKF define os valores `draft`, `stable` e `deprecated`.

**Papel nas KBs:** O `status` permite ao consumidor distinguir conceitos ainda em elaboração, conceitos vigentes e conceitos mantidos apenas para preservar links e histórico. Na ausência do campo, o estado padrão é `stable`. :contentReference[oaicite:9]{index=9}

##### 2.2.2.3.2. Stale After

**Definição:** `stale_after` é uma data absoluta (`YYYY-MM-DD`) a partir da qual o Concept é considerado desatualizado.

**Papel nas KBs:** O `stale_after` permite ao consumidor determinar de forma objetiva se um Concept ainda deve ser considerado atual. Um Concept é considerado stale quando a data corrente é igual ou posterior à data definida nesse campo. :contentReference[oaicite:10]{index=10}

#### 2.2.2.4. Conformance

A conformidade define as condições mínimas para que um documento seja considerado um documento OKF válido. O OKF adota uma abordagem deliberadamente mínima: um Concept é um arquivo Markdown UTF-8 composto por um bloco YAML frontmatter e um body Markdown, sendo `type` o único campo de frontmatter obrigatório. Os demais campos e famílias de metadados são opcionais, e produtores podem acrescentar campos adicionais. Consumidores devem tolerar tipos e campos desconhecidos e não devem rejeitar documentos por sua ausência. :contentReference[oaicite:11]{index=11}



## 2.3. Configurações para produção dos documentos OKF do MB-Code-Generator
### 2.3.1. resumo
A produção dos documentos OKF do MB-Code-Generator é orientada por configurações que estabelecem a forma pela qual o conhecimento do sistema será representado nas Knowledge Bases. As configurações definem características dos Concepts, de sua organização e de suas relações, preservando os conceitos originais do OKF apresentados na seção 2.

As configurações são divididas em **configurações para os conceitos originais**, que estabelecem como os conceitos OKF serão utilizados para representar o conhecimento do MBCG, e **configurações complementares**, que estabelecem propriedades adicionais necessárias para otimizar a organização, descoberta e consumo desse conhecimento.

Sim. Você tem razão — eu me adiantei para a seção 4. O que precisamos fazer agora é **revisar exclusivamente a seção 3**, aplicando a definição de “Configuração” que acabamos de estabelecer.

O principal ajuste, na minha leitura, é este: os itens atuais estão bons como conteúdo, mas precisam ficar mais claramente formulados como **configurações**, com **contexto, decisão/configuração e regras aplicáveis**, sem transformar a seção em uma lista de princípios genéricos.

Eu preservaria a divisão entre **conceitos originais** e **configurações complementares**, porque ela faz sentido no modelo que você está construindo.

### 2.3.2. Configurações para os conceitos originais

#### 2.3.2.1. mindmap
- type
- title
- description
- resource
- tags
- source




#### 2.3.2.2. Frontmatter

O Frontmatter constitui a parte estruturada do documento OKF destinada à identificação e à descrição das características do Concept. No MB-Code-Generator, seu preenchimento deve seguir as configurações definidas para os campos reconhecidos pelo modelo adotado.

As configurações para os campos do Frontmatter são:

| campo         | papel                                                          | regras                                                                                                                                                                                     | valores                                                            |
| ------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `type`        | Identifica a natureza ou categoria semântica do Concept.       | **Obrigatório.** Deve ser informado em todo Concept. O valor deve corresponder a um tipo reconhecido pelo modelo de Concepts do MBCG.                                                      | Nome do tipo de Concept definido pelo MBCG.                        |
| `title`       | Fornece um título legível para identificação do Concept.       | **Recomendado.** Deve representar de forma concisa o Concept ao qual o documento se refere.                                                                                                | Texto.                                                             |
| `description` | Fornece uma descrição resumida do Concept.                     | **Recomendado.** Deve apresentar o significado do Concept de forma suficiente para permitir sua identificação e compreensão sem a necessidade de interpretar todo o conteúdo do documento. | Texto descritivo.                                                  |
| `resource`    | Identifica um recurso associado ao Concept.                    | **Recomendado.** Quando utilizado, deve identificar o recurso de acordo com a convenção adotada pelo MBCG para esse tipo de referência.                                                    | Identificador ou referência de recurso, conforme o modelo adotado. |
| `tags`        | Associa termos de classificação ou indexação ao Concept.       | **Recomendado.** Os valores devem ser utilizados de maneira consistente para Concepts que compartilham a mesma classificação.                                                              | Um ou mais termos de classificação.                                |
| `source`      | Identifica a origem do conhecimento representado pelo Concept. | **Recomendado.** Quando o conhecimento for derivado de uma fonte identificável, a fonte deve ser indicada de acordo com o mecanismo de origem definido pelo OKF.                           | Referência a uma fonte, conforme o modelo adotado.                 |

**Informações adicionais:**
- `type` é o único campo obrigatório entre os campos definidos nesta configuração. A ausência de um campo recomendado não deve, por si só, impedir a produção do documento.
- O valor de `type` deve permitir que o Concept seja distinguido dos demais tipos de Concepts produzidos pelo MBCG.
- `title` e `description` possuem funções distintas: `title` identifica o Concept de forma concisa, enquanto `description` fornece uma caracterização textual de seu significado.
- `tags` deve ser utilizado para classificação ou indexação complementar e não deve substituir `type` quando a distinção representar a natureza semântica do Concept.
- `source` identifica a origem do conhecimento. Quando for necessário registrar informações mais detalhadas sobre como o conhecimento foi produzido, transformado ou verificado, devem ser utilizados os mecanismos de `Provenance` definidos pelo OKF.
- Os valores dos campos devem ser definidos de acordo com o domínio estabelecido para cada campo. Exemplos de valores não constituem, por si mesmos, novos valores admissíveis quando não estiverem incluídos no domínio definido para o campo.

### 2.3.3. OLD Configurações para os conceitos originais

#### 2.3.3.1. Natureza do Concept
- **Contexto da configuração**: Concept do MBCG.
- **Título da configuração**: unidade de conhecimento representada por um Concept.
- **Definição**: cada Concept deve representar uma unidade identificável de conhecimento sobre o sistema, seus requisitos, sua arquitetura, seus elementos, seus comportamentos, suas decisões ou outros aspectos necessários à sua definição.
- **Regras**:
    - o Concept deve possuir identidade própria;
    - o significado representado pelo Concept deve ser identificável;
    - o Concept deve possuir utilidade independente quando sua separação for necessária para identificação, relacionamento, evolução ou consumo;
    - conceitos independentes não devem ser agregados em um mesmo Concept apenas para reduzir a quantidade de documentos.

#### 2.3.3.2. Identidade do Concept

- **Contexto da configuração**: identificação de Concepts na Knowledge Base.
    
- **Título da configuração**: identidade do Concept.
    
- **Definição**: todo Concept deve possuir uma identidade única e estável dentro da Knowledge Base, expressa pelo seu Concept ID.
    
- **Regras**:
    
    - o Concept ID deve identificar o conceito representado;
        
    - a identidade não deve representar uma instância transitória do conteúdo do documento;
        
    - alterações no conteúdo não devem produzir uma nova identidade quando o conceito representado permanecer semanticamente o mesmo;
        
    - Concepts semanticamente distintos devem possuir identidades distintas.
        

#### 2.3.3.3. Classificação do Concept

- **Contexto da configuração**: classificação dos Concepts do MBCG.
    
- **Título da configuração**: classificação por `type`.
    
- **Definição**: todo Concept deve possuir uma classificação por `type`, utilizada para determinar sua natureza dentro do conhecimento do MBCG.
    
- **Regras**:
    
    - os valores de `type` devem representar categorias semânticas de Concepts;
        
    - os tipos não devem representar características incidentais da implementação ou da forma de armazenamento do documento;
        
    - um tipo deve permitir identificar Concepts que compartilham uma mesma natureza;
        
    - consumidores podem utilizar o tipo para aplicar comportamentos específicos aos Concepts classificados.
        

#### 2.3.3.4. Contexto do Concept

- **Contexto da configuração**: interpretação de Concepts na Knowledge Base.
    
- **Título da configuração**: contexto do Concept.
    
- **Definição**: todo Concept deve possuir um contexto determinável a partir de sua posição na estrutura da Knowledge Base e de suas relações com outros Concepts.
    
- **Regras**:
    
    - o contexto deve estabelecer o domínio de conhecimento ao qual o Concept pertence;
        
    - o contexto não deve depender exclusivamente de informações externas ao Concept ou à Knowledge Base;
        
    - a estrutura física dos documentos pode contribuir para o contexto, mas não deve substituir relações semânticas quando estas forem necessárias para sua interpretação.
        

#### 2.3.3.5. Conteúdo do Concept

- **Contexto da configuração**: conteúdo dos Concepts do MBCG.
    
- **Título da configuração**: conteúdo representado pelo Concept.
    
- **Definição**: o conteúdo de um Concept deve representar o conhecimento associado à unidade conceitual identificada por seu Concept ID e classificada por seu `type`.
    
- **Regras**:
    
    - o conteúdo deve ser suficiente para expressar o significado do conceito;
        
    - devem ser representadas as características relevantes para sua interpretação;
        
    - informações necessárias para utilização do Concept por outros Concepts ou consumidores devem ser expressas de forma determinável;
        
    - informações que constituam conhecimento independente não devem ser incorporadas ao conteúdo apenas por conveniência de documentação.
        

#### 2.3.3.6. Propriedades do Concept

- **Contexto da configuração**: propriedades dos Concepts do MBCG.
    
- **Título da configuração**: representação estruturada das propriedades.
    
- **Definição**: as propriedades de um Concept devem representar características que qualificam o conceito e que sejam relevantes para sua interpretação ou utilização.
    
- **Regras**:
    
    - propriedades cujo significado precise ser identificado, comparado ou processado por consumidores devem ser representadas de forma estruturada;
        
    - propriedades não devem depender exclusivamente de interpretação textual quando puderem ser representadas pelo modelo adotado;
        
    - propriedades devem possuir significado definido no contexto do tipo de Concept ao qual pertencem.
        

#### 2.3.3.7. Relações entre Concepts

- **Contexto da configuração**: relações semânticas entre Concepts do MBCG.
    
- **Título da configuração**: representação das relações entre Concepts.
    
- **Definição**: relações entre Concepts devem ser representadas explicitamente sempre que sua existência ou natureza for relevante para a interpretação do conhecimento.
    
- **Regras**:
    
    - a relação deve identificar os Concepts participantes;
        
    - quando aplicável, a natureza da relação deve ser identificável;
        
    - relações semânticas não devem depender exclusivamente da proximidade ou localização física dos documentos;
        
    - o mecanismo `Link` do OKF deve ser utilizado para representar as relações entre Concepts quando aplicável.
        

#### 2.3.3.8. Hierarquia de Concepts

- **Contexto da configuração**: organização estrutural e semântica dos Concepts.
    
- **Título da configuração**: hierarquia e organização dos Concepts.
    
- **Definição**: a organização dos Concepts deve permitir representar relações de especialização, decomposição, composição ou pertencimento quando essas relações forem aplicáveis ao conhecimento representado.
    
- **Regras**:
    
    - uma hierarquia deve possuir significado semântico identificável;
        
    - a hierarquia física de diretórios pode fornecer contexto estrutural;
        
    - uma estrutura física não deve ser utilizada como substituto de uma relação semântica explícita quando esta precisar ser interpretada independentemente da localização do documento.
        

#### 2.3.3.9. Fontes do Concept

- **Contexto da configuração**: origem do conhecimento representado pelos Concepts.
    
- **Título da configuração**: fontes e proveniência.
    
- **Definição**: quando o conhecimento de um Concept for derivado de material identificável, sua origem deve ser representada pelos mecanismos de `Source` e `Provenance` definidos pelo OKF.
    
- **Regras**:
    
    - `Source` deve identificar ou referenciar o material de origem;
        
    - `Provenance` deve representar a relação entre a fonte e o conhecimento produzido no Concept;
        
    - a ausência de uma fonte conhecida não deve resultar na criação de uma fonte fictícia;
        
    - informações de proveniência devem ser preservadas quando forem relevantes para a interpretação ou confiabilidade do conhecimento.
        

### 2.3.4. Configurações complementares

As configurações complementares estabelecem características adicionais do conhecimento do MBCG que não são determinadas diretamente pelos conceitos originais do OKF, mas que são necessárias para que as Knowledge Bases mantenham organização, coerência, independência entre elementos e condições adequadas de utilização.

#### 2.3.4.1. Granularidade semântica

- **Contexto da configuração**: definição da unidade de conhecimento representada por um Concept.
    
- **Título da configuração**: granularidade dos Concepts.
    
- **Definição**: um Concept deve possuir granularidade suficiente para que o conhecimento nele representado possa ser identificado, recuperado, relacionado, validado e utilizado independentemente quando necessário.
    
- **Regras**:
    
    - a granularidade deve ser determinada pela unidade semântica do conhecimento, e não pelo tamanho do documento;
        
    - um Concept deve ser dividido quando diferentes partes do conteúdo puderem possuir identidade, relações, ciclo de vida ou utilização independente;
        
    - Concepts não devem ser artificialmente fragmentados quando a separação prejudicar a compreensão de uma unidade conceitual.
        

#### 2.3.4.2. Atomicidade

- **Contexto da configuração**: composição do conteúdo de um Concept.
    
- **Título da configuração**: unidade semântica dominante.
    
- **Definição**: cada Concept deve possuir uma unidade semântica dominante que determine o conceito representado.
    
- **Regras**:
    
    - um Concept pode possuir múltiplas propriedades e características relacionadas à sua unidade semântica;
        
    - conceitos independentes não devem ser combinados apenas para reduzir a quantidade de documentos;
        
    - informações que possuam identidade própria devem ser representadas por Concepts próprios quando sua separação for necessária.
        

#### 2.3.4.3. Componibilidade

- **Contexto da configuração**: composição de conhecimento a partir de Concepts relacionados.
    
- **Título da configuração**: composição entre Concepts.
    
- **Definição**: Concepts devem poder ser relacionados para formar conhecimento de maior nível de abstração.
    
- **Regras**:
    
    - um Concept complexo deve poder utilizar outros Concepts como elementos constituintes;
        
    - a composição deve ser representada por relações explícitas;
        
    - o conhecimento já representado por outro Concept não deve ser duplicado apenas para compor um conceito de nível superior.
        

#### 2.3.4.4. Rastreabilidade

- **Contexto da configuração**: origem, dependências e relações do conhecimento do MBCG.
    
- **Título da configuração**: rastreabilidade do conhecimento.
    
- **Definição**: conhecimento relevante para a definição do MBCG deve poder ser relacionado aos elementos que determinam sua origem, justificativa, dependências ou derivação.
    
- **Regras**:
    
    - quando houver elementos identificáveis de origem ou justificativa, sua relação com o Concept deve ser representada explicitamente;
        
    - a rastreabilidade pode envolver Concepts, requisitos, decisões, fontes, funcionalidades ou outros elementos da especificação;
        
    - a relação deve permitir identificar o encadeamento do conhecimento sem exigir reconstrução baseada exclusivamente em interpretação textual.
        

#### 2.3.4.5. Não redundância

- **Contexto da configuração**: representação de conhecimento compartilhado por diferentes partes do sistema.
    
- **Título da configuração**: referência canônica do conhecimento.
    
- **Definição**: o mesmo conhecimento semântico não deve ser definido independentemente em múltiplos Concepts.
    
- **Regras**:
    
    - quando um conhecimento for compartilhado por diferentes partes do sistema, deve existir um Concept que constitua sua referência canônica;
        
    - outros Concepts devem relacionar-se ao Concept canônico quando necessitarem utilizar esse conhecimento;
        
    - diferenças legítimas de contexto devem ser representadas como conceitos distintos quando produzirem significados semanticamente distintos.
        

#### 2.3.4.6. Consistência terminológica

- **Contexto da configuração**: terminologia utilizada nos Concepts do MBCG.
    
- **Título da configuração**: terminologia dos Concepts.
    
- **Definição**: um mesmo termo deve representar o mesmo conceito em toda a Knowledge Base, salvo quando diferenças de contexto forem explicitamente estabelecidas.
    
- **Regras**:
    
    - termos utilizados para identificar Concepts devem possuir significado estável;
        
    - sinônimos ou variações de nomenclatura não devem ser utilizados de forma que produzam ambiguidade;
        
    - diferenças terminológicas necessárias entre contextos devem ser explicitamente relacionadas quando representarem conceitos equivalentes ou relacionados.
        

#### 2.3.4.7. Separação entre conceito e representação

- **Contexto da configuração**: relação entre o conhecimento representado e sua forma de utilização.
    
- **Título da configuração**: independência entre conceito e representação.
    
- **Definição**: o Concept deve representar o conhecimento, e não uma forma específica de visualização, consumo ou implementação desse conhecimento.
    
- **Regras**:
    
    - detalhes de apresentação ou processamento não devem definir a identidade do conceito;
        
    - quando uma característica de apresentação, implementação ou processamento constituir conhecimento relevante, ela pode ser representada como propriedade ou Concept próprio;
        
    - a representação operacional não deve ser confundida com o significado do conhecimento representado.
        

#### 2.3.4.8. Evolução independente

- **Contexto da configuração**: evolução dos Concepts ao longo do ciclo de vida do conhecimento.
    
- **Título da configuração**: independência de evolução dos Concepts.
    
- **Definição**: Concepts devem poder evoluir individualmente sempre que sua identidade semântica permanecer preservada.
    
- **Regras**:
    
    - alterações localizadas devem permanecer localizadas sempre que possível;
        
    - uma alteração em um Concept não deve exigir a reescrita de Concepts não afetados;
        
    - alterações que modifiquem a identidade ou o significado do conceito devem ser tratadas de acordo com as regras de evolução de identidade adotadas pelo MBCG.
        

#### 2.3.4.9. Recuperabilidade

- **Contexto da configuração**: organização dos Concepts para localização do conhecimento.
    
- **Título da configuração**: recuperação do conhecimento.
    
- **Definição**: a organização dos Concepts deve permitir que um consumidor encontre conhecimento relevante a partir de diferentes pontos de entrada.
    
- **Regras**:
    
    - Concepts devem poder ser encontrados por sua identidade, classificação, contexto, relações ou conteúdo descritivo, conforme aplicável;
        
    - a organização deve permitir recuperação progressiva do conhecimento;
        
    - o consumidor deve poder partir de uma visão estrutural e aprofundar-se apenas nos Concepts necessários.
        

#### 2.3.4.10. Interpretabilidade

- **Contexto da configuração**: interpretação dos Concepts por consumidores da Knowledge Base.
    
- **Título da configuração**: interpretabilidade do Concept.
    
- **Definição**: um Concept deve conter informações suficientes para que um consumidor determine o que ele representa e como se relaciona com o restante do conhecimento.
    
- **Regras**:
    
    - o significado do Concept deve ser determinável a partir de seu conteúdo e das relações relevantes;
        
    - relações necessárias para a interpretação devem ser representadas explicitamente;
        
    - convenções implícitas não devem ser utilizadas quando impedirem a interpretação independente do Concept;
        
    - a interpretação não deve depender de conhecimento externo que não esteja relacionado ou referenciado pela Knowledge Base.
        

#### 2.3.4.11. O que mudou conceitualmente

A mudança principal não foi simplesmente colocar “Contexto / Título / Definição / Regras” em cada item. O mais importante foi separar **o que está sendo configurado** de **como essa configuração deve ser obedecida**.

Por exemplo:

> **Granularidade semântica** não é simplesmente uma recomendação de “fazer Concepts pequenos”. Ela configura **qual unidade semântica deve resultar em um Concept independente** e estabelece as regras para decidir quando dividir ou não.

E o mesmo vale para rastreabilidade, identidade, `type`, relações etc.

Há ainda **um ponto que eu deixaria em aberto por enquanto**: se “Natureza do Concept”, “Granularidade semântica” e “Atomicidade” estão suficientemente distintos. Eles são próximos e existe risco de três configurações acabarem regulando a mesma decisão com palavras diferentes. Eu não eliminaria nenhuma ainda, mas esse é provavelmente o primeiro conjunto que merece uma revisão de sobreposição antes de consolidarmos a seção 3.

## 2.4. Relacionamentos entre conceitos
Estabelecer o encadeamento lógico entre os conceitos OKF adotados, mostrando como eles se combinam para formar uma KB navegável e consumível por seus consumers.

## 2.5. Convenções específicas do MBCG
Registrar somente as decisões, restrições ou convenções que complementam ou especializam o OKF para atender às necessidades do MB-Code-Generator.

## 2.6. Glossário

**Configuração**. No contexto da especificação de Software, é uma informação explicitamente definida que estabelece ou influencia o comportamento, a estrutura, a operação ou as características de um software, sem constituir, por si mesma, a implementação do comportamento configurado. A configuração representa uma decisão ou parâmetro que pode ser definido, alterado ou selecionado para determinar como o software deve operar em determinado contexto. A descrição de uma configuração deve informar a qual contexto do software se aplica, sendo este contexto geralmente relacionado a: (a) funcionalidades do software, (b) suas regras de processamento, (c) seus resultados ou (d) seus argumentos de entrada. Define-se também o domínio de valores admissíveis e regras que determinem como seu valor influencia o contexto aplicável. Conforme o tipo de configuração, pode ser necessário definir, ou exemplificar, o conjunto de valores admissíveis e condições de exceção. 

Exemplo de configuração: 
- **Contexto da configuração**: OKF Knowledge Bundle do sistema MBCG.
- **Título da configuração**: modelo de OKF concept document, propriedades do frontmatter. 
- observação: neste exemplo optou-se pela formatação de tabela, mas poderia ser outro formato, conforme o conjunto de informações da configuração. 
- **Definições** (campos da tabela):
	- campo: nome do campo no frontmatter 
	- papel: qual o papel ou contribuição do campo no contexto aplicável da configuração 
	- regras: o que deve ser respeitado, observado ou evitado 
	- valores: lista ou exemplos de valores admissíveis 

| campo | papel | regras | valores |
| ----- | ----- | ------ | ------- |
|       |       |        |         |



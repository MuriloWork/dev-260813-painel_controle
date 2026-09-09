MBCG — Model-Based-Code-Generator

# 1. Sobre os conceitos MBSE adotados pelo MB-Code-Generator.

- Declaração. Qual conceito normalizado será utilizado em cada camada da especificação?
- Referência. De qual normativo, ou literatura de referência, vem o conceito? Resumir o conceito existente e instruir como deve ser utilizado no MBCG
- Estabelecimento de encadeamento lógico. As camadas e blocos das especificações de sistema são encadeados e inter-relacionados, gerando complexidade para suas definições, implementações e gerenciamento. Definir clara e detalhadamente quais serão as lógicas de relacionamento é fundamental para consistência das especificações. 

# 2. mapa mental 
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

# 3. camadas da especificação MBSE

## 3.1. resumo 
Sim. Agora ficou claro o papel de conceitos_mbcg: ele não é um glossário genérico do MBCG. Ele deve estabelecer a linguagem conceitual e as regras de encadeamento que posteriormente serão materializadas nos templates.

Para isso, eu separaria duas dimensões:

Camadas → níveis de abstração/especificação, do problema à implementação.

Blocos → tipos de informação/modelos que existem dentro de cada camada.


A referência mais sólida para a espinha dorsal é ISO/IEC/IEEE 15288:2023, complementada por ISO/IEC/IEEE 29148:2018 para engenharia de requisitos e pelo INCOSE Systems Engineering Handbook. A 15288 é especialmente adequada porque permite aplicar os processos em diferentes níveis da hierarquia do sistema; a 29148 trata explicitamente da produção e gerenciamento dos artefatos de requisitos. 

## 3.2. Proposta de camadas do MBCG

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


Essa separação também preserva uma distinção importante da engenharia de sistemas: a arquitetura funcional/lógica não deve ser confundida com a arquitetura física. A arquitetura lógica descreve o que o sistema precisa realizar de maneira independente da solução tecnológica; a física trata dos elementos que efetivamente realizam essa solução. Essa distinção é explicitamente utilizada em práticas de MBSE/INCOSE. 

## 3.3. blocos transversais:

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

## 3.4. relacionamentos 

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

## 3.5. resumo
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

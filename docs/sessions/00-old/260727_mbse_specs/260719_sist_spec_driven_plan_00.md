
Abaixo estão detalhadas as etapas do plano de trabalho para o desenvolvimento e evolução do **Sistema de Edição de Especificações de Software com Base em Modelos** utilizando o ecossistema Gaphor:

# 1. Fase 1: Mapeamento do Metamodelo do Gaphor e Análise de Extensibilidade  

## 1.1. Objetivos Específicos
- Investigação aprofundada das estruturas internas das classes Element e Presentation do Gaphor.  
- Mapeamento do ciclo de vida dos conectores, diagramas e elementos de metamodelo nativos.  
- Identificação de pontos de acoplamento e injeção de extensões de metadados MDA/OCL.  
- Analisar a biblioteca gaphor.core.modeling para compreender o funcionamento do repositório de elementos (ElementFactory) e do sistema de eventos/sinais.  
- Diferenciar e mapear a separação entre a camada de modelo semântico (Element) e a camada de representação gráfica no canvas (Presentation / Item).  
- Avaliar a estrutura dos pacotes gaphor.UML e gaphor.SysML para determinar como introduzir novos estereótipos, perfis e propriedades dinâmicas sem violar as restrições da OMG implementadas no motor.  
- Identificar os mecanismos de extensão de interface (Gtk.Widget) e criação de abas/painéis na barra lateral (Property Page Provider).

## 1.2. Atividades e Entregáveis da Etapa 1

| Código | Atividade                                                                                                                                                                       | Entregável Técnico                                                                                            |
| :----: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------ |
|  1.1   | **Inspeção da AST Interna e Repositório do Gaphor** Auditoria do código-fonte do Gaphor focado em ElementFactory, Element e serialização XML.                                   | Documento de mapeamento das rotas de ciclo de vida de objetos e eventos do repositório.                       |
|  1.2   | **Análise do Mecanismo de Extensão de Telas (Property Pages)** Mapeamento das interfaces PropertyPageProvider para inclusão de campos e formatações personalizadas.             | Protótipo funcional em Python injetando uma nova propriedade customizada em uma classe UML base.              |
|  1.3   | **Definição da Estratégia de Injeção de Metadados MDA** Validação técnica de acoplamento de dicionários/payloads JSON no nível da classe Element.                               | Prova de Conceito (PoC) de anexação e persistência de metadados JSON sem corromper o leitor nativo do Gaphor. |
|  1.4   | **Mapeamento de Diagramas e Conectores Elegíveis** Identificação de quais diagramas UML/SysML do Gaphor serão utilizados como base para os modelos de especificação do sistema. | Matriz de mapeamento entre tipos de diagramas do Gaphor e representações da especificação de software.        |

# 2. Fase 2: Especificação da Estrutura Ampliada (JSON Schema / Pydantic)  
- Definição do esquema de dados estendido utilizando Pydantic para validação em Python.  
- Modelagem de estruturas para suporte a expressões OCL (Object Constraint Language).  
- Especificação do envelope JSON/JSONB para persistência de metadados de geração de código e rastreabilidade de engenharia reversa.  

## 2.1. Especificações a Serem Criadas no Gaphor

Para suportar a edição completa de especificações executáveis de software com base em modelos, serão estruturadas e modeladas no Gaphor as seguintes especificações de domínio:

### 2.1.1. Especificação de Requisitos e Regras de Negócio (CIM / PIM)
- **Modelo de Casos de Uso e Histórias de Usuário:** Mapeamento de atores, fronteiras do sistema, precondições e fluxos principais/alternativos.  
- **Catálogo de Requisitos SysML/UML:** Requisitos funcionais e não-funcionais categorizados com identificadores únicos, prioridade, rastreabilidade de origem e critérios de aceite.  
- **Regras de Negócio e Expressões OCL:** Especificação declarativa de invariantes do sistema, validações de atributos e restrições de transição de estado expressas em OCL.

### 2.1.2. Especificação da Arquitetura e Modelagem Estática (PIM)
- **Modelo de Domínio e Entidades (Class Diagram):** Mapeamento de objetos de domínio, agregados, entidades, objetos de valor (Value Objects), enumerações e seus relacionamentos (associação, composição, agregação).  
- **Especificação de Contratos de API e DTOs:** Definição de rotas HTTP/REST, parâmetros de entrada/saída, tipos de payload e schemas JSON modelados via estereótipos UML.  
- **Modelo de Persistência de Dados:** Mapeamento relacional de tabelas, chaves primárias/estrangeiras, índices, restrições de unicidade e colunas dinâmicas (JSONB) direcionadas ao SQLite local.

### 2.1.3. Especificação Dinâmica e Comportamental (PIM / PSM)
- **Diagramas de Sequência e Integração:** Mapeamento de trocas de mensagens síncronas/assíncronas entre componentes, controllers, serviços e banco de dados.  
- **Diagramas de Máquina de Estados (State Machines):** Especificação do ciclo de vida de entidades complexas do sistema, definindo estados validos, eventos de gatilho e transições condicionadas por regras OCL.  
- **Diagramas de Atividades e Processamento de Dados:** Fluxos de trabalho detalhados de validação, transformação de dados e geração de artefatos.

### 2.1.4. Especificação para Mapeamento de Código e Engenharia Reversa (PSM)
- **Mapeamento de AST e Tipagem Alvo:** Especificação de regras de conversão de tipos abstratos da UML para linguagens de programação alvo (Python, Dart, SQL).  
- **Dicionário de Tags e Anotações de Código:** Configuração de metadados para controle de geração de código (ex: decorators, orm mappings, exportações de módulos).  
- **Matriz de Rastreabilidade Bidirecional (Model-to-Code Mapping):** Vínculo explícito entre UUIDs dos elementos no modelo Gaphor, tabelas no SQLite local e nós da AST dos arquivos de código-fonte.

# 3. Fase 3: Desenvolvimento de Plugin / Extensão do Gaphor  
- Criação de painéis e componentes visuais laterais na interface gráfica do Gaphor (GTK/PyGObject).  
- Habilitação da edição interativa de propriedades estendidas (regras OCL, metadados de API, configurações de banco de dados).  
- Implementação de manipuladores de eventos (\*event handlers\*) para sincronização em tempo real entre UI e modelo subjacente.  

# 4. Fase 4: Motor de Validação Semântica e Execução OCL  
- Integração de parser/interpretador OCL em Python para avaliação de restrições, invariantes, pré e pós-condições.  
- Implementação de rotinas de validação de consistência estática e integridade do modelo.  
- Geração de relatórios de erros e alertas de inconformidade diretamente na interface de edição.  

# 5. Fase 5: Camada de Persistência Local e Sincronização (SQLite \+ JSONB \+ Git)  
- Desenvolvimento do repositório de persistência baseado em SQLite local embarcado utilizando suporte nativo a JSONB.  
- Implementação de mecanismos de serialização e exportação de *snapshots* em JSON/YAML para historização e versionamento em repositórios Git via pygit2 / GitPython.  
- Gestão de unicidade de elementos baseada em UUIDs globais.  

# 6. Fase 6: Pipeline de Geração de Código e Engenharia Reversa (Round-Trip)  
- Desenvolvimento de geradores de código baseados em templates M2T (Model-to-Text via Jinja2/Mako).  
- Implementação de rotinas de extração e análise de AST (Abstract Syntax Tree) para linguagens alvo (ex: Dart, Python, SQL).  
- Mecanismo de reconciliação e detecção de diferenças (*diffing/drift detection*) entre o código-fonte alterado e o modelo de especificação.



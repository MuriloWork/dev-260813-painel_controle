# 1. Modelo Comparativo de Entidades, Expressões e Axiomas em Engenharia de Software

## 1.1. Entidades

### 1.1.1. Indivíduos e Recursos

| Título Genérico | OWL | RDFS | SKOS | Comumente Aplicado em |
| --- | --- | --- | --- | --- |
| Instâncias de Commits e Revisões | `owl:NamedIndividual` (ex: `commit_a1b2c3d`) | `rdfs:Resource` / `rdf:Description` (ex: `http://git.org/commit/a1b2c3d`) | `skos:Concept` (conceito representando o evento do commit) | Rastreabilidade de versionamento e auditoria de código-fonte |
| Servidores e Nós de Infraestrutura | `owl:NamedIndividual` (ex: `node_aws_prod_01`) | `rdfs:Resource` (ex: `http://infra.org/node/01`) | `skos:Concept` (nó de inventário de infraestrutura) | Gerenciamento de configuração, DevOps e mapas de topologia |
| Desenvolvedores e Atores | `owl:NamedIndividual` (ex: `user_alice_dev`) | `rdfs:Resource` / `foaf:Person` (ex: `http://team.org/user/alice`) | `skos:Concept` (conceito do ator/papel do especialista) | Atribuição de responsabilidade, revisão de código e gestão de times |
| Artefatos Compilados e Builds | `owl:NamedIndividual` (ex: `build_1042_jar`) | `rdfs:Resource` (ex: `http://ci.org/build/1042`) | `skos:Concept` (item no catálogo de produtos gerados) | Gestão de release, esteiras de CI/CD e repositórios de binários |
| Pacotes e Bibliotecas Externas | `owl:NamedIndividual` (ex: `npm_express_4_18`) | `rdfs:Resource` (ex: `http://registry.org/npm/express`) | `skos:Concept` (termo de biblioteca em catálogo) | Análise de dependências de software e gestão de licenças |
| Registros de Tarefas e Bugs | `owl:NamedIndividual` (ex: `issue_bug_1420`) | `rdfs:Resource` (ex: `http://tracker.org/issue/1420`) | `skos:Concept` (item de trabalho no vocabulário) | Gestão de chamados, rastreamento de defeitos e listas de backlog |

### 1.1.2. Classes e Categorias

| Título Genérico | OWL | RDFS | SKOS | Comumente Aplicado em |
| --- | --- | --- | --- | --- |
| Componentes e Módulos | `owl:Class` (ex: `swo:SoftwareComponent`) | `rdfs:Class` (ex: `seon:SoftwareModule`) | `skos:ConceptScheme` / `skos:Concept` (categoria no vocabulário) | Arquitetura de software e catalogação de componentes reutilizáveis |
| Requisitos e Histórias de Usuário | `owl:Class` (ex: `seon:FunctionalRequirement`) | `rdfs:Class` (ex: `req:UserStory`) | `skos:Concept` (conceito taxonômico de requisito) | Engenharia de requisitos e rastreabilidade de escopo |
| Tipos de Defeito e Erros | `owl:Class` (ex: `seon:BugReport`) | `rdfs:Class` (ex: `tracker:Defect`) | `skos:Concept` (categoria de falha no KOS) | Análise de qualidade de software e classificação de incidentes |
| Ambientes de Execução | `owl:Class` (ex: `devops:DeploymentEnvironment`) | `rdfs:Class` (ex: `infra:Environment`) | `skos:Concept` (classificação de ambiente) | Automação de deploy e gerenciamento de infraestrutura como código |
| Serviços e Endpoints REST | `owl:Class` (ex: `arch:Microservice`) | `rdfs:Class` (ex: `api:RESTEndpoint`) | `skos:Concept` (termo de serviço em catálogo) | Governança de APIs, service mesh e arquiteturas orientadas a serviços |
| Tipos de Teste de Software | `owl:Class` (ex: `seon:UnitTest`) | `rdfs:Class` (ex: `test:IntegrationTest`) | `skos:Concept` (categoria de teste) | Estratégia de garantia de qualidade e automação de testes |

### 1.1.3. Propriedades de Objeto

| Título Genérico | OWL | RDFS | SKOS | Comumente Aplicado em |
| --- | --- | --- | --- | --- |
| Relação de Dependência de Código | `owl:ObjectProperty` (ex: `dependsOnLibrary`) | `rdf:Property` (ex: `importsModule`) | `skos:related` / `skos:semanticRelation` | Análise de impacto de mudanças e compilação de projetos |
| Rastreabilidade de Requisitos | `owl:ObjectProperty` (ex: `implementsRequirement`) | `rdf:Property` (ex: `satisfiesReq`) | `skos:relatedMatch` / `skos:broadMatch` | Matriz de rastreabilidade entre código e requisitos de negócio |
| Deploy em Infraestrutura | `owl:ObjectProperty` (ex: `deployedToEnvironment`) | `rdf:Property` (ex: `runsOnHost`) | `skos:related` | Orquestração de contêiners e controle de topologia de implantação |
| Autoria e Revisão de Código | `owl:ObjectProperty` (ex: `authoredBy`) | `rdf:Property` (ex: `reviewedBy`) | `skos:related` | Governança de repositórios e auditoria de commits |
| Composição Arquitetural | `owl:ObjectProperty` (ex: `containsSubmodule`) | `rdf:Property` (ex: `hasPart`) | `skos:narrower` / `skos:broader` | Decomposição de sistemas e modelagem de diagramas UML |
| Associação de Release e Branch | `owl:ObjectProperty` (ex: `mergedIntoBranch`) | `rdf:Property` (ex: `partOfRelease`) | `skos:related` | Gerenciamento de fluxo de trabalho Git (GitFlow) e entregas |

### 1.1.4. Propriedades de Dados e Atributos

| Título Genérico | OWL | RDFS | SKOS | Comumente Aplicado em |
| --- | --- | --- | --- | --- |
| Métricas de Qualidade e Complexidade | `owl:DatatypeProperty` (ex: `cyclomaticComplexity` `xsd:integer`) | `rdf:Property` com `rdfs:range rdfs:Literal` | `skos:notation` / literais em propriedades personalizadas | Auditoria de código, análise estática e dívida técnica |
| Identificadores Únicos e Hashes | `owl:DatatypeProperty` (ex: `commitHash` `xsd:string`) | `rdf:Property` (ex: `buildNumber`) | `skos:notation` (ex: código alfanumérico UDC/notação) | Integridade de artefatos e identificação de commits em VCS |
| Marcas Temporais e Cronologia | `owl:DatatypeProperty` (ex: `executionTimeMs` `xsd:decimal`) | `rdf:Property` (ex: `createdAtTimestamp`) | Literais associados a notas de histórico (`skos:historyNote`) | Monitoramento de performance e SLA de pipelines |
| Indicadores de Status e Severidade | `owl:DatatypeProperty` (ex: `vulnerabilityCVSS` `xsd:float`) | `rdf:Property` (ex: `buildStatus`) | `skos:prefLabel` / `skos:notation` de gravidade | Gestão de vulnerabilidades (DevSecOps) e triagem de bugs |
| Mensagens e Logs de Execução | `owl:DatatypeProperty` (ex: `commitMessage` `xsd:string`) | `rdf:Property` (ex: `logOutputText`) | `skos:definition` / `skos:scopeNote` | Diagnóstico de falhas, registros de auditoria e changelogs |
| Parâmetros de Configuração | `owl:DatatypeProperty` (ex: `allocatedMemoryMB` `xsd:integer`) | `rdf:Property` (ex: `portNumber`) | `skos:notation` sintática de parâmetro | Provisionamento de ambientes e parametrização de microsserviços |

### 1.1.5. Propriedades de Anotação

| Título Genérico | OWL | RDFS | SKOS | Comumente Aplicado em |
| --- | --- | --- | --- | --- |
| Nomes Legíveis e Títulos | `owl:AnnotationProperty` (ex: `rdfs:label`) | `rdfs:label` | `skos:prefLabel` (rótulo preferencial por idioma) | Interface de usuário em ferramentas de modelagem e catálogos |
| Descrições Técnicas e Documentação | `owl:AnnotationProperty` (ex: `rdfs:comment`) | `rdfs:comment` | `skos:definition` / `skos:scopeNote` | Documentação de APIs, dicionário de dados e glossários |
| Depreciação e Versionamento de API | `owl:AnnotationProperty` (ex: `owl:deprecated` `xsd:boolean`) | `rdfs:seeAlso` | `skos:changeNote` / `skos:historyNote` | Mapeamento de ciclo de vida de software e APIs legadas |
| Notas Editoriais e Pendências | `owl:AnnotationProperty` (ex: `rdfs:comment`) | `rdfs:comment` | `skos:editorialNote` | Gestão interna de ontologias de engenharia e notas de revisão |
| Referência a Especificações Externas | `owl:AnnotationProperty` (ex: `rdfs:isDefinedBy`) | `rdfs:isDefinedBy` / `rdfs:seeAlso` | `skos:exactMatch` / notas documentárias | Vinculação com documentação OpenAPI/Swagger ou RFCs |
| Sinônimos e Termos Alternativos | `owl:AnnotationProperty` (ex: `rdfs:label`) | `rdfs:label` | `skos:altLabel` / `skos:hiddenLabel` | Mecanismos de busca técnica e tolerância a erros de digitação |

## 1.2. Expressões

### 1.2.1. Conjunção e Interseção

| Título Genérico | OWL | RDFS | SKOS | Comumente Aplicado em |
| --- | --- | --- | --- | --- |
| Microserviço Crítico de Segurança | `owl:intersectionOf` (`Microservice AND SecurityCritical`) | Herança múltipla via `rdfs:subClassOf` em ambas | Pós-coordenação de conceitos `skos:Concept` | Classificação automatizada para auditoria estrita de DevSecOps |
| Defeito de Alta Prioridade Aberto | `owl:intersectionOf` (`BugReport AND OpenStatus AND HighPriority`) | Múltiplas superclasses implícitas | Combinação de coleções de conceitos | Filtragem dinâmica de backlog em ferramentas de gestão de tarefas |
| Teste de Integração Automatizado | `owl:intersectionOf` (`TestCase AND IntegrationTest AND AutomatedTest`) | Superclasses concorrentes em RDFS | Agrupamento pós-coordenado de termos | Seleção automatizada de suítes de teste na esteira de CI/CD |
| Desenvolvedor e Revisor Principal | `owl:intersectionOf` (`Developer AND RepoMaintainer AND CodeReviewer`) | Declarações múltiplas de classe | Associação de múltiplos conceitos ao ator | Validação de regras de aprovação de Pull Requests |
| Componente Depreciado Vulnerável | `owl:intersectionOf` (`SoftwareComponent AND DeprecatedModule AND VulnerableArtifact`) | Atribuição simultânea de tipos | Combinação de rótulos em catálogos | Alertas automáticos de substituição de dependências de software |

### 1.2.2. Disjunção e União

| Título Genérico | OWL | RDFS | SKOS | Comumente Aplicado em |
| --- | --- | --- | --- | --- |
| Artefato Compilável Genérico | `owl:unionOf` (`SourceFile OR BinaryPackage OR ContainerImage`) | Sem suporte nativo direto a união | `skos:Collection` (agrupamento de conceitos) | Regras de empacotamento e artefatos elegíveis para deploy |
| Ator de Execução de Pipeline | `owl:unionOf` (`HumanDeveloper OR BotAccount OR CIProcess`) | Sem suporte nativo a união lógica | `skos:Collection` de atores de sistema | Controle de acesso unificado e auditoria de ações no repositório |
| Evento de Gatilho de CI | `owl:unionOf` (`CodePushEvent OR PullRequestEvent OR ScheduledTrigger`) | Sem suporte nativo | `skos:Collection` de eventos de gatilho | Mapeamento de webhooks e gatilhos de automação de testes |
| Ambiente de Não-Produção | `owl:unionOf` (`DevelopmentEnv OR StagingEnv OR TestingEnv`) | Sem suporte nativo | `skos:Collection` de ambientes secundários | Políticas de permissão e limpeza de recursos de infraestrutura |
| Item de Trabalho do Backlog | `owl:unionOf` (`BugReport OR FeatureRequest OR RefactoringTask`) | Sem suporte nativo | `skos:Collection` de tipos de tarefas | Unificação de visualizações em quadros Kanban/Scrum |

### 1.2.3. Negação e Complemento

| Título Genérico | OWL | RDFS | SKOS | Comumente Aplicado em |
| --- | --- | --- | --- | --- |
| Teste Manual (Não Automatizado) | `owl:complementOf` (`TestCase AND NOT AutomatedTest`) | Sem suporte a complemento | Sem suporte a negação | Identificação de gargalos de testes manuais que exigem ação humana |
| Commit Não Implantado | `owl:complementOf` (`Commit AND NOT DeployedCommit`) | Sem suporte a complemento | Sem suporte a negação | Cálculo de pendências de implantação (Deployment Lead Time) |
| Componente Sem Vulnerabilidades | `owl:complementOf` (`SoftwareModule AND NOT VulnerableComponent`) | Sem suporte a complemento | Sem suporte a negação | Certificação de segurança para liberação em ambiente de produção |
| Repositório Privado (Não Público) | `owl:complementOf` (`Repository AND NOT PublicRepository`) | Sem suporte a complemento | Sem suporte a negação | Imposição de restrições de visibilidade e vazamento de código |
| Código Não Coberto por Testes | `owl:complementOf` (`SourceCodeModule AND NOT TestedModule`) | Sem suporte a complemento | Sem suporte a negação | Geração de relatórios de cobertura de código (Code Coverage) |

### 1.2.4. Restrição Existencial

| Título Genérico | OWL | RDFS | SKOS | Comumente Aplicado em |
| --- | --- | --- | --- | --- |
| Componente com Dependência Vulnerável | `owl:someValuesFrom` (`SoftwareModule AND dependsOn SOME VulnerableLibrary`) | Sem restrição de escopo local (apenas `rdfs:range` global) | Conexões diretas entre instâncias de conceitos | Detecção automática de riscos de segurança em árvores de dependências |
| Release com Correção de Segurança | `owl:someValuesFrom` (`Release AND containsCommit SOME SecurityFixCommit`) | Sem suporte a restrições de classe anônimas | Estrutura de relacionamentos conceituais | Marcação de releases de emergência (Hotfix/Security Patch) |
| Pull Request Aprovação Pendente | `owl:someValuesFrom` (`PullRequest AND hasApproval SOME CodeReviewer`) | Sem suporte local | Sem suporte formal | Validação de portão de qualidade (Quality Gate) em Pull Requests |
| Serviço com Endpoint REST Exposto | `owl:someValuesFrom` (`Service AND exposesEndpoint SOME RESTEndpoint`) | Sem suporte local | Sem suporte formal | Catalogação e descoberta automática de APIs em malhas de serviços |
| Build com Imagem de Contêiner | `owl:someValuesFrom` (`BuildJob AND producesArtifact SOME ContainerImage`) | Sem suporte local | Sem suporte formal | Rastreamento de linhagem de artefatos (Artifact Lineage) em CI/CD |

### 1.2.5. Restrição Universal

| Título Genérico | OWL | RDFS | SKOS | Comumente Aplicado em |
| --- | --- | --- | --- | --- |
| Release Totalmente Homologada | `owl:allValuesFrom` (`SecureRelease AND hasComponent ONLY TestedComponent`) | `rdfs:range` (restrição global para a propriedade) | Sem suporte a quantificação universal | Garantia de conformidade regulatória e validação estrita de releases |
| Pipeline de Execução Segura | `owl:allValuesFrom` (`StrictPipeline AND runsJob ONLY CertifiedContainerJob`) | Restrição global via `rdfs:range` | Sem suporte | Imposição de execução de pipelines exclusivamente em nós homologados |
| Módulo Isolado de Comunicação | `owl:allValuesFrom` (`IsolatedModule AND communicatesWith ONLY InternalService`) | Restrição global via `rdfs:range` | Sem suporte | Arquiteturas de Zero-Trust e isolamento de redes de microsserviços |
| Repositório com Contribuição Assinada | `owl:allValuesFrom` (`OpenRepo AND hasContributor ONLY SignedCLAContributor`) | Restrição global via `rdfs:range` | Sem suporte | Conformidade de propriedade intelectual e licenças open-source |

### 1.2.6. Restrição de Cardinalidade

| Título Genérico | OWL | RDFS | SKOS | Comumente Aplicado em |
| --- | --- | --- | --- | --- |
| Pull Request com Dupla Reversão | `owl:qualifiedCardinality` / `owl:cardinality` (`PullRequest AND hasReview EXACTLY 2`) | Sem suporte a cardinalidade | Convenção estrutural (ex: único `prefLabel` por idioma) | Verificação de política de Code Review obrigatória por dois pares |
| Banco de Dados com Nó Primário Único | `owl:maxCardinality` (`DatabaseCluster AND hasPrimaryNode MAX 1`) | Sem suporte a cardinalidade | Convenção semântica | Validação de arquiteturas de alta disponibilidade e evita Split-Brain |
| Componente HA com Réplicas Mínimas | `owl:minCardinality` (`HAComponent AND hasReplica MIN 3`) | Sem suporte a cardinalidade | Convenção semântica | Dimensionamento de infraestrutura e tolerância a falhas em Kubernetes |
| Limite de Métodos em Classe Limpa | `owl:maxCardinality` (`ClassModule AND hasMethod MAX 50`) | Sem suporte a cardinalidade | Sem suporte | Análise de refatoração de código (evitar instâncias de God Class) |

### 1.2.7. Enumeração de Indivíduos

| Título Genérico | OWL | RDFS | SKOS | Comumente Aplicado em |
| --- | --- | --- | --- | --- |
| Ambientes Oficiais Homologados | `owl:oneOf` (`{env_dev, env_staging, env_prod}`) | Sem suporte nativo a enumeração fechada | `skos:OrderedCollection` com `skos:memberList` | Restrição de destinos válidos para scripts de implantação |
| Mantenedores do Core da Aplicação | `owl:oneOf` (`{dev_alice, dev_bob, dev_charlie}`) | Sem suporte nativo | `skos:Collection` de membros chave | Permissões de escrita direta no branch principal do repositório |
| Repositórios Oficiais do ecossistema | `owl:oneOf` (`{repo_core, repo_api, repo_ui}`) | Sem suporte nativo | `skos:Collection` de repositórios | Escopo de varredura automatizada de ferramentas de SAST/DAST |
| Suíte de Testes de Regressão Crítica | `owl:oneOf` (`{test_auth, test_payment, test_billing}`) | Sem suporte nativo | `skos:OrderedCollection` de testes | Validação de sanidade do sistema antes do deploy em produção |

## 1.3. Axiomas

### 1.3.1. Hierarquia e Subsumção de Classes

| Título Genérico | OWL | RDFS | SKOS | Comumente Aplicado em |
| --- | --- | --- | --- | --- |
| Classificação de Artefatos | `owl:subClassOf` (`SourceCode subClassOf Artifact`) | `rdfs:subClassOf` | `skos:broader` / `skos:narrower` | Organização de elementos do ciclo de vida de desenvolvimento |
| Taxonomia de Falhas e Defeitos | `owl:subClassOf` (`SecurityVulnerability subClassOf SoftwareDefect`) | `rdfs:subClassOf` | `skos:broader` / `skos:narrower` | Categorização e priorização de chamados de manutenção |
| Tipologia de Itens de Trabalho | `owl:subClassOf` (`BugReport subClassOf WorkItem`) | `rdfs:subClassOf` | `skos:broader` / `skos:narrower` | Estruturação de ferramentas de gerenciamento de projetos agile |
| Especialização de Testes | `owl:subClassOf` (`UnitTest subClassOf TestCase`) | `rdfs:subClassOf` | `skos:broader` / `skos:narrower` | Organização de planos e planos de testes automatizados |
| Arquitetura de Serviços | `owl:subClassOf` (`Microservice subClassOf DistributedService`) | `rdfs:subClassOf` | `skos:broader` / `skos:narrower` | Mapeamento de padrões arquiteturais em ecossistemas de software |

### 1.3.2. Equivalência de Classes e Mapeamentos

| Título Genérico | OWL | RDFS | SKOS | Comumente Aplicado em |
| --- | --- | --- | --- | --- |
| Definição Formal de Módulo Vulnerável | `owl:equivalentClass` (`VulnerableModule EquivalentTo Module AND (dependsOn SOME VulnerableLibrary)`) | Declarações recíprocas `rdfs:subClassOf` | `skos:exactMatch` | Inferência automatizada de componentes afetados por CVEs |
| Alinhamento de Vocabulários SEON/SWO | `owl:equivalentClass` (`seon:SoftwareComponent EquivalentTo swo:SoftwareComponent`) | `rdfs:subClassOf` mútuo | `skos:exactMatch` / `skos:closeMatch` | Interoperabilidade entre ontologias distintas de engenharia de software |
| Critério de Release Pronta | `owl:equivalentClass` (`ProductionReadyRelease EquivalentTo Release AND (hasStatus VALUE "PassedAllTests")`) | Declarações recíprocas `rdfs:subClassOf` | `skos:exactMatch` | Automação de portões de qualidade para liberação de software |
| Mapeamento de Ferramentas de Issue | `owl:equivalentClass` (`jira:Issue EquivalentTo github:Issue`) | Declarações recíprocas `rdfs:subClassOf` | `skos:exactMatch` | Integração heterogênea entre sistemas de acompanhamento de tarefas |

### 1.3.3. Disjunção de Classes

| Título Genérico | OWL | RDFS | SKOS | Comumente Aplicado em |
| --- | --- | --- | --- | --- |
| Isolamento de Ambientes | `owl:disjointWith` (`DevelopmentEnv DisjointWith ProductionEnv`) | Sem suporte a disjunção | Disjunção implícita por modelo | Validação de consistência lógica (impedir servidor em dois ambientes) |
| Níveis de Visibilidade do Código | `owl:disjointWith` (`PublicRepo DisjointWith PrivateRepo`) | Sem suporte a disjunção | Disjunção implícita | Prevenção de exposição acidental de código confidencial |
| Níveis Extremos de Severidade | `owl:disjointWith` (`CriticalSeverity DisjointWith LowSeverity`) | Sem suporte a disjunção | Disjunção implícita | Garantia de categorização unívoca em triagem de incidentes |
| Modos de Comunicação de Tarefas | `owl:disjointWith` (`SynchronousTask DisjointWith AsynchronousTask`) | Sem suporte a disjunção | Disjunção implícita | Modelagem precisa de concorrência e arquitetura de mensageria |

### 1.3.4. Domínio e Alcance de Propriedades

| Título Genérico | OWL | RDFS | SKOS | Comumente Aplicado em |
| --- | --- | --- | --- | --- |
| Associação de Correção de Bug | `rdfs:domain Commit`, `rdfs:range BugReport` | `rdfs:domain`, `rdfs:range` | `rdfs:domain skos:Concept`, `rdfs:range skos:Concept` | Validação de referências em mensagens de commit Git |
| Vínculo de Deploy de Pacotes | `rdfs:domain SoftwarePackage`, `rdfs:range Environment` | `rdfs:domain`, `rdfs:range` | `rdfs:domain skos:Concept`, `rdfs:range skos:Concept` | Verificação de conformidade em scripts de implantação |
| Métrica Numérica de Código | `rdfs:domain CodeFunction`, `rdfs:range xsd:integer` | `rdfs:domain`, `rdfs:range` | `rdfs:domain skos:Concept`, `rdfs:range xsd:integer` | Verificação do tipo de dados retornado em ferramentas de análise estática |
| Conexão de Conceitos SKOS | `rdfs:domain skos:Concept`, `rdfs:range skos:Concept` | `rdfs:domain`, `rdfs:range` | `rdfs:domain skos:Concept`, `rdfs:range skos:Concept` | Garantia de integridade do modelo conceitual SKOS |

### 1.3.5. Identidade e Equivalência de Indivíduos

| Título Genérico | OWL | RDFS | SKOS | Comumente Aplicado em |
| --- | --- | --- | --- | --- |
| Aliasing de Usuários em Plataformas | `owl:sameAs` (`user_alice_github sameAs user_alice_ldap`) | Sem suporte nativo | `skos:exactMatch` (evita fusão indesejada de rótulos) | Unificação de métricas de contribuição em ferramentas distintas |
| Redirecionamento de Repositório | `owl:sameAs` (`repo_old_name sameAs repo_new_name`) | Sem suporte nativo | `skos:exactMatch` | Manutenção de links em migrações de infraestrutura de código |
| Mapeamento de Conceitos de Vocabulários | `owl:sameAs` (fundição total de propriedades) | Sem suporte nativo | `skos:exactMatch` (preferido em SKOS para preservar descritores) | Integração de taxonomias técnicas de fornecedores diferentes |
| Aliasing de Nós de Infraestrutura | `owl:sameAs` (`server_ip_10_0_0_1 sameAs server_hostname_prod1`) | Sem suporte nativo | `skos:exactMatch` | Mapeamento de ativos de rede em inventários dinâmicos de nuvem |

### 1.3.6. Diferenciação de Indivíduos

| Título Genérico | OWL | RDFS | SKOS | Comumente Aplicado em |
| --- | --- | --- | --- | --- |
| Distinção de Ambientes de Destino | `owl:differentFrom` (`env_staging differentFrom env_production`) | Sem suporte nativo | Sem suporte nativo | Prevenção de execução acidental de comandos de teste em produção |
| Separação de Branches do Git | `owl:differentFrom` (`branch_main differentFrom branch_feature`) | Sem suporte nativo | Sem suporte nativo | Garantia de integridade em fluxos de mesclagem (merge) de código |
| Distinção de Versões de Release | `owl:differentFrom` (`release_v1_0_0 differentFrom release_v2_0_0`) | Sem suporte nativo | Sem suporte nativo | Rastreamento estrito de incompatibilidades e atualizações breaking |
| Unicidade de Instâncias de Cluster | `owl:AllDifferent` (`AllDifferent(node_1, node_2, node_3)`) | Sem suporte nativo | Sem suporte nativo | Garantia de identidade única para membros de um cluster distribuído |

### 1.3.7. Características Lógicas de Propriedades

| Título Genérico | OWL | RDFS | SKOS | Comumente Aplicado em |
| --- | --- | --- | --- | --- |
| Dependência Transitiva de Módulos | `owl:TransitiveProperty` (`dependsOn`) | Sem suporte nativo | `skos:broaderTransitive` / `skos:narrowerTransitive` | Cálculo da árvore completa de dependências diretas e indiretas |
| Comunicação Bidirecional de Serviços | `owl:SymmetricProperty` (`communicatesWith`) | Sem suporte nativo | `skos:related` | Mapeamento de conexões de rede em arquiteturas distribuídas |
| Linhagem Unidirecional de Commits | `owl:AsymmetricProperty` (`childCommitOf`) | Sem suporte nativo | Sem suporte nativo | Prevenção de ciclos inválidos em grafos direcionados acíclicos (DAG) de commits |
| Atribuição Unívoca de Mantenedor | `owl:FunctionalProperty` (`hasPrimaryMaintainer`) | Sem suporte nativo | Convenção estrutural | Garantia de um único responsável primário por projeto de software |
| Relação Inversa de Componente/Requisito | `owl:inverseOf` (`implementsRequirement inverseOf requiredByComponent`) | Sem suporte nativo | `skos:broader` inverseOf `skos:narrower` | Navegação bidirecional em relatórios de cobertura de requisitos |


# 2. conceitos gerais

| conceito        | definição | valores |     |
| --------------- | --------- | ------- | --- |
| dominio         |           |         |     |
| repositorio     |           |         |     |
| artefato        |           |         |     |
| arquitetura     |           |         |     |
| modelo          |           |         |     |
| system          |           |         |     |
| bloco funcional |           |         |     |

- **conceito**: repositorio 
	- **definição**: 
- **conceito**: arquitetura de repositorio 
	- **definição**: pasta agrupadora, por assuntos, por tipos de artefatos, por camada do acervo 
	- **camadas/zonas do acervo**: 
		- frequência de consulta [do, system, km, mem]
		- agrupamento de assuntos 
	- **componentes**: folder 
		- **finalidade**:  [do, system, km, mem] 
		- **componentes**: artefato 
- **conceito**: dominio 
	- **definição**: área de conhecimento, assunto, ~~camada/zona cognitiva~~, abrangência ~~de aplicação~~ 
		- abrangência no projeto [acima, ...]
	- **valores**: 
		- conceitos 
			- **definição**: 
			- **valores**:
				- software engineering 
					- ontologia 
					- mbse 
		- conceitos aplicados 
		- regras [kb, software, agents, system models]
- modelo 
- projeto, sessão 
- system 
- bloco functional 

# 3. arquitetura modelo dos repositorios 
- repos [repo_type, repo_URI, root, folder_type, rel_folder_path, file_name] 
- repo_type [local/web, public/private, direct/api] 
- artifact type [doc, data, code, midia] 
- artifact purpose [business,  system] 
- ciclo de vida [permanente, temporário, por projeto] 
- destino após desativação 
- `systems^root` ~~scripts^root~~ 
	- `main^system_name` 
	- `dev^proj_name`  
		- system_name_version ⟶ `main^system_name`
			- src 
			- data
			- .docs 
				- spec_version (current) 
		- docs ⟷ `obsidian^systems^dev^proj_name^docs`
			- sessions 
				- session data 
			- gsd-planning 
			- `spec^system_name` 
				- spec_version (current copy) 
				- spec_version (next) 
				- spec_version (updated) ⟶ `main^system_name^docs` 
			- kb ⟶ `obsidian^km^systems_kb`
				- domain- [conceitos, conceitos aplicados, regras sobre kb, regras sobre software, regras sobre agents, regras sobre system models] version 
			- agents_version ⟶ `obsidian^km^systems_agents`
				- agents data
- pkm 
- obsidian
	- `systems^dev^proj_name^docs` 
	- `km^systems_kb`
	- `km^systems_agents`
- repo name = URI 
- [required] README.md
- frontmatter 
	- OKF-title = repository-description 
	- (+) frontmatter especifico conforme title 
- body 

# 4. ontologia para repositorios 
|[[01-conceitos_software_ontologia|conceitos ontologia]]|
|[[01-conceitos_software_ontologia#5.1. pipeline|ontology pipeline]]|

## 4.1. Template Unificado (Modelo Mestre)

| Nome da Coluna                   | Descrição Técnica (Mapeamento JSON-LD)                          | Exemplo de Preenchimento                  |
| -------------------------------- | --------------------------------------------------------------- | ----------------------------------------- |
| ID do Conceito                   | O identificador único local do termo/classe.                    | `TAX_030`                                 |
| Prefixo / Namespace              | Onde o termo reside (geralmente mapeado no `@context`).         | `ex:`                                     |
| Tipo Semântico                   | Se o termo comporta-se como Conceito, Classe ou ambos.          | `["skos:Concept", "owl:Class"]`           |
| Termo Preferido (prefLabel)      | Nome oficial do conceito/classe.                                | `Cachorro`                                |
| Idioma                           | Código ISO do idioma da string.                                 | `pt`                                      |
| Sinônimos (altLabel)             | Termos alternativos separados por vírgula (vira Array no JSON). | `Cão, Canino`                             |
| Definição (definition)           | Significado exato para humanos e sistemas.                      | `Mamífero doméstico da família canídeos.` |
| Termo Pai (broader / subClassOf) | ID do conceito mais amplo ou classe pai.                        | `TAX_020`                                 |
| Propriedade Associada            | Propriedade OWL vinculada a esta classe (se houver).            | `ex:temDono`                              |
| Tipo de Propriedade              | Tipo da relação OWL (`ObjectProperty` ou `DatatypeProperty`).   | `owl:ObjectProperty`                      |
| Domínio (Domain)                 | Quem possui a propriedade (geralmente o próprio ID).            | `TAX_030`                                 |
| Contradomínio (Range)            | O tipo de dado ou classe que responde à propriedade.            | `ex:Pessoa`                               |
| Restrição / Cardinalidade        | Regra lógica de negócio aplicada à propriedade.                 | `owl:maxCardinality 1`                    |

## 4.2. vocabulario


| ID do Conceito | Prefixo / Namespace | Tipo Semântico | ==prefLabel== | Idioma | altLabel | definition | subClassOf | Propriedade Associada | Tipo de Propriedade | Domain | Range | Cardinalidade |
| -------------- | ------------------- | -------------- | ------------- | ------ | -------- | ---------- | ---------- | --------------------- | ------------------- | ------ | ----- | ------------- |
|                |                     |                |               |        |          |            |            |                       |                     |        |       |               |


- repositorio
	- identificação [tipo, URI] 
- pasta 
	- dominio 
	- identificação [path]
- arquivo 
	- path, tipo
	- metadados 

## 4.3. taxonomia para repositorios 

- identificação
- proveniencia
- relacionamento
- persistência [documentos, seções/endereços/labels, relacionamentos, dados]
- versionamento + historico [decisão, alternativas consideradas, justificativa, consequência, elementos afetados]
- validação
- classification scheme 
- subject heading 

### 4.3.1. conforme o objetivo da análise 

#### 4.3.1.1. Taxonomia por Escopo e Tipo de Conteúdo
Classifica o repositório pelo tipo de artefato ou nível de abstração que ele gerencia:
- **Repositório de Código-Fonte (VCS)**: Armazena o código bruto, histórico de commits e ramificações (branches). Exemplos: repositórios Git/GitHub e GitLab.
- **Repositório de Artefatos / Binários (Package Registry)**: Armazena pacotes compilados prontos para distribuição ou deploy. Exemplos: npm (JavaScript), Maven (Java), PyPI (Python) e Docker registries (como o Docker Hub).
- **Repositório de Modelos e Conhecimento**: Armazena documentação, diagramas de arquitetura, requisitos e ontologias do projeto.

#### 4.3.1.2. Taxonomia por Arquitetura de Distribuição
Define como os dados do repositório são armazenados e sincronizados entre os desenvolvedores:
- **Centralizado (CVCS)**: Existe apenas uma cópia mestre do repositório em um servidor central. Os desenvolvedores fazem o checkout de arquivos isolados. Exemplos: Subversion (SVN), Perforce.
- **Distribuído (DVCS)**: Cada desenvolvedor possui um clone completo do repositório em sua máquina local, incluindo todo o histórico de alterações. Exemplos: Git, Mercurial.

#### 4.3.1.3. Facetas de Classificação (Mineração de Repositórios de Software - MSR)
Em pesquisas acadêmicas e análises de ecossistemas (como o mapeamento automatizado de repositórios), adota-se uma taxonomia baseada em facetas:

| Faceta                           | Conceito / Atributos Classificados                                                                                                                        |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Domínio da Aplicação**         | Identifica a finalidade do software armazenado (ex: utilitários, frameworks, ferramentas de desenvolvimento, aplicações de pesquisa).                     |
| **Atividade de Desenvolvimento** | Categoriza o repositório pelo seu status de manutenção (ex: ativo, inativo/arquivado, incubação, espelho/mirror).                                         |
| **Modelo de Licenciamento**      | Classifica de acordo com as permissões legais do repositório (ex: Open Source - MIT, GPL, Apache; Propriatário; InnerSource).                             |
| **Estilo Arquitetural**          | Agrupa os repositórios pelo formato do código (ex: Monorepo — múltiplas aplicações em um único repositório; Polyrepo — um repositório por microsserviço). |

#### 4.3.1.4. Abordagens de Classificação Automatizada
Para lidar com a escala de milhões de repositórios públicos, a engenharia de software moderna utiliza técnicas automatizadas para derivar taxonomias e tags dinâmicas:
- **Topic Modeling (LDA)**: Agrupamento baseado nas palavras-chave encontradas nos arquivos README.md ou descrições dos projetos.
- **Taxonomia baseada em Tags**: Uso de estruturas hierárquicas extraídas de plataformas comunitárias como o Stack Overflow ou metadados de pacotes (como CodeMeta) para taguear automaticamente os repositórios


### 4.3.2. conforme a camada de abstração 
considerada (arquitetura de código, controle de versão, distribuição de pacotes ou ecossistema de dados).

#### 4.3.2.1. Visão de Controle de Versão e Estrutura de Código (VCS / SCM)

Refere-se à forma como o código-fonte e o histórico do projeto são organizados no sistema de controle de versão (como Git).
- **Monorepo (Monolithic Repository):** Um único repositório contém o código-fonte de múltiplos projetos, serviços ou bibliotecas interdependentes. Facilita o refatoramento atômico e o compartilhamento de código.
- **Polyrepo / Multirepo:** Cada serviço, aplicação ou biblioteca possui seu próprio repositório isolado. Promove forte autonomia entre equipes e deploys independentes.
- **Meta-repository (Monorepo Virtual):** Uso de ferramentas (como Git Submodules ou Google repo) para agrupar múltiplos repositórios distintos em um repositório central unificado.

#### 4.3.2.2. Visão do Padrão de Projeto de Software (Design Patterns & DDD)

Refere-se à camada de persistência e acesso a dados dentro da arquitetura do software (ex.: Clean Architecture, DDD).
- **Repository Pattern (Martin Fowler / DDD):** Uma abstração que simula uma coleção em memória para gerenciar entidades de domínio, isolando a regra de negócio da lógica de banco de dados (SQL, NoSQL, ORM).
    - **Read/Write Repository (CQRS):** Separação clara entre repositórios focados em consulta (_Query_) e repositórios focados em mutação (_Command_).
    - **Generic Repository:** Implementação com métodos reutilizáveis de CRUD para qualquer entidade.

#### 4.3.2.3. Visão do Estilo Arquitetural de Sistemas (Architectural Styles)

A classificação abaixo destaca como componentes do sistema interagem com uma fonte centralizada de dados mantida na memória ou em disco.

![[260819-modelo_repositorios-01.webp]]

- **Blackboard Architecture:** Vários subsistemas especializados (especialistas) trabalham de forma independente e assíncrona sobre um repositório comum (_blackboard_) para resolver um problema complexo gradualmente.
- **Database-Centric / Data-Driven Architecture:** A aplicação é construída em torno de um repositório central de dados permanente, acessado por múltiplos componentes independentes.

#### 4.3.2.4. Visão de Ecossistema e Gestão de Artefatos

Classificação dos repositórios utilizados no ciclo de integração e implantação (CI/CD):
- **Source Code Repository:** GitHub, GitLab, Bitbucket.
- **Artifact / Binary Repository:** Nexus, JFrog Artifactory, Docker Hub. Armazenam artefatos compilados, imagens de contêineres e pacotes prontos para execução.
- **Package Repository:** npm, PyPI, Pub.dev, NuGet. Repositórios públicos ou privados voltados à distribuição de dependências e bibliotecas reutilizáveis.
- **MSR (Mining Software Repositories):** Área da engenharia de software voltada para análise estatística e extração de dados sobre o histórico de comits, _pull requests_ e problemas (_issues_).


# 5. modelo para repositorios de documentos `kb` tipo OKF
- onde é encontrado: repositorios com tipo conteudo [documentos] e tipo dominio: [conhecimento conceitual, conhecimento aplicado, regras sobre kb concepts, regras sobre codificação, regras sobre agent pipelines, system models]
## 5.1. modelo geral
-  frontmatter 
	- [required] OKF 
		- **type** = tipo de dominio
		- **title** = lista de strings de outros repositorios relacionados, com ou sem hierarquia, sendo a última string da lista o título do concept propriamente dito
		- **description**: A single sentence summarizing the concept. Used by `index.md` generators, search snippets, and previews.
		- **resource**: A URI that uniquely identifies the underlying asset the concept describes. Absent for concepts that describe abstract ideas rather than physical resources.
		- **tags**: A YAML list of short strings for cross-cutting categorization.
	- [optional] especifico, conforme o titulo 
		- para título padronizado "**repository-description**"
			- valor inferido do `resource`
				- tipo URI: [local file system,  local server, cloud storage (onedrive, gdrive), cloud server, cloud host, github] 
				- persistência: [sistema, permanente, projeto, temporario] 
			- valor conforme regras: 
				- tipo conteudo: [documentos, dados, codigos, hibrido]
				- repository version
- body 
	- headings 
	- links externos 
	- links internos obsidian 
	- taxonomia relacionamentos/ edges 

## 5.2. modelo especifico para INDEX.md
### 5.2.1. modelo especifico para INDEX.md na pasta raiz `docs^kb`
## 5.3. modelo especifico para README.md
### 5.3.1. modelo especifico para README.md na pasta raiz `docs^kb`

# 6. demais modelos
## 6.1. modelo para repositorios de documentos `agents`
## 6.2. modelo para repositorios de documentos `spec`
## 6.3. modelo para repositorios de documentos `gsd-planning`
## 6.4. modelo para repositorios de documentos `sessions`
## 6.5. modelo para repositorios de dados
### 6.5.1. KG - Knowledge Graph
[[01-conceitos_software_se#7. Knowledge Graph|conceitos KG]]

## 6.6. modelo para repositorios de codigos

# 7. Análise de Formatos de Documentos para Agentes de IA

## 7.1. Introdução e Contexto (A Interseção entre OWS e Agentes de IA)
A construção de um **Sistema de Gestão de Conhecimento (KMS)** para agentes de IA de codificação (como *coding assistants*, *autonomous dev agents*) exige a transição de dados não estruturados para representações semânticas. É aqui que os **OWS (Web Ontology Systems / Sistemas de Ontologia Web)** e os **Knowledge Graphs (Grafos de Conhecimento)** entram em cena.

Agentes de IA "leem" documentos de duas formas distintas:
1. **Leitura Estocástica (LLM/Attention):** O modelo processa o texto como tokens, inferindo significado baseado em padrões (usado em Markdown).
2. **Leitura Determinística (Parser/AST):** O agente usa ferramentas para extrair dados exatos de estruturas rígidas (usado em JSON, XML).

Para modelar um KMS robusto, precisamos entender como os formatos de serialização (`.md`, `.xml`, `.json`, `.yaml`, `.toml`) se comportam sob a ótica da IA e como eles podem ser mapeados para ontologias (padrões OWS como RDF, OWL, JSON-LD).



## 7.2. Análise dos Formatos sob os Critérios Definidos

### 7.2.1. Markdown (`.md`)
O Markdown é a linguagem franca da documentação e do *prompt engineering*.
*   **1. Facilidade/Aptidão para leitura:** **Excepcional**. LLMs são massivamente treinados em Markdown. A IA compreende intuitivamente a hierarquia (headers), listas e blocos de código.
*   **2. Acuracidade/Precisão:** **Baixa a Média**. A leitura é semântica, não estrutural. A IA pode "alucinar" a relação entre dois tópicos se o texto for ambíguo. Não há garantia de integridade de dados.
*   **3. Características de sintaxe:** Baseada em texto puro com marcações leves (`#`, `*`, ```). A falta de fechamento rígido (como tags) torna a tokenização muito eficiente (baixo custo de contexto).
*   **4. Recursos para Knowledge Graphs (OWS):** **Fraco nativamente, mas excelente para metadados**. Não suporta grafos nativamente, mas é o melhor formato para embutir grafos visuais (via *Mermaid.js*) ou criar "Wikilinks" (`[[Entidade]]`) que agentes podem usar para indexar conexões conceituais.

### 7.2.2. YAML (`.yaml`)
Muito comum em configuração (Kubernetes, CI/CD) e documentação estruturada (OpenAPI/Swagger).
*   **1. Facilidade/Aptidão para leitura:** **Alta**. Mais legível para humanos e IAs do que JSON, pois remove a "poluição" visual de chaves e aspas.
*   **2. Acuracidade/Precisão:** **Média/Alta**. A precisão é alta, mas a **sensibilidade a espaços em branco (indentação)** é uma armadilha. Um erro de indentação gerado pela IA quebra o parser, causando falhas silenciosas ou erros de compilação no agente.
*   **3. Características de sintaxe:** Baseada em indentação e hífens. Permite anotações e referências (âncoras), o que economiza tokens.
*   **4. Recursos para Knowledge Graphs (OWS):** **Muito Bom**. YAML é frequentemente usado como uma sintaxe alternativa para RDF (RDF/YAML). É ideal para definir *schemas* de ontologias (classes e propriedades) de forma hierárquica.

ver tambem [YAML-LD specifications](https://w3c.github.io/yaml-ld/), [YAML-LD github](https://github.com/w3c/yaml-ld/)

### 7.2.3. TOML (`.toml`)
Formato de configuração focado em ser minimalista e mapear diretamente para dicionários/hash maps.
*   **1. Facilidade/Aptidão para leitura:** **Média/Alta**. Muito limpo, mas a IA o lê mais como um arquivo de configuração de estado do que como um documento de conhecimento.
*   **2. Acuracidade/Precisão:** **Alta**. Estrutura rígida, tipagem forte (datas, inteiros, strings).
*   **3. Características de sintaxe:** Baseado em seções `[secao]` e pares `chave = valor`. Não lida bem com hierarquias profundas ou listas complexas de objetos.
*   **4. Recursos para Knowledge Graphs (OWS):** **Fraco**. A falta de suporte nativo a hierarquias profundas e aninhamentos complexos o torna inadequado para modelagem de grafos de conhecimento ou ontologias.

### 7.2.4. XML (`.xml`)
O formato clássico de documentos estruturados e base de sistemas OWS tradicionais.
*   **1. Facilidade/Aptidão para leitura:** **Média**. IAs entendem XML perfeitamente, mas a leitura é "cansativa" em termos de janela de contexto devido à verbosidade das tags de fechamento.
*   **2. Acuracidade/Precisão:** **Extrema**. Com validação via XSD (XML Schema Definition), a precisão é absoluta. A IA sabe exatamente o que é um atributo e o que é um nó.
*   **3. Características de sintaxe:** Tags aninhadas. Extremamente rígido. Gera um *overhead* de tokens muito alto (ex: `<relation>...</relation>` gasta muitos tokens apenas para dizer "relação").
*   **4. Recursos para Knowledge Graphs (OWS):** **O Padrão Ouro (RDF/XML, OWL/XML)**. A Web Semântica (OWS) foi construída sobre XML. É o melhor formato para definir ontologias complexas, restrições de classes e inferências lógicas.

### 7.2.5. JSON (`.json`)
O formato nativo da web e das APIs, base fundamental para a serialização de ontologias modernas.
*   **1. Facilidade/Aptidão para leitura:** **Alta**. Agentes de IA possuem *function calling* e *tool use* nativos baseados em JSON. A IA lê JSON como uma árvore lógica de objetos.
*   **2. Acuracidade/Precisão:** **Muito Alta**. A sintaxe é determinística. Um parser de JSON não falha se o schema for respeitado. A IA não "inventa" chaves ou tipos de dados.
*   **3. Características de sintaxe:** Uso intensivo de aspas, chaves e colchetes. **Ponto negativo:** É verboso e consome muitos tokens (ruído sintático), o que pode saturar a janela de contexto do agente.
*   **4. Recursos para Knowledge Graphs (OWS):** **Excelente**. O **JSON-LD** é o padrão W3C para vincular dados na web como grafos. Pares de chave-valor mapeiam perfeitamente para triplas RDF (Sujeito-Predicado-Objeto).
### 7.2.6. JSON-LD (diferencas para JSON)

#### 7.2.6.1. Conceito e Proposito
O JSON convencional e projetado prioritariamente como um formato leve de intercambio de dados e mensagens entre sistemas, focado na simplicidade e na facilidade de leitura humana [1, 22]. No entanto, ao integrar dados provenientes de fontes distintas, chaves identicas em documentos JSON diferentes podem entrar em conflito e gerar ambiguidades de interpretacao [22]. Alem disso, o JSON tradicional carece de suporte nativo para hiperlinks ou identificadores globais, dificultando a interconexao de recursos distribuídos na Web [22].

O JSON-LD (JSON-based Linked Data) foi desenvolvido como um formato semantico totalmente compatível com o JSON convencional [1, 3]. Ele funciona como uma extensao que permite que sistemas e interpretadores JSON ja existentes compreendam dados estructurados como Linked Data (Dados Conectados) com o minimo de alteracoes, oferecendo um caminho suave de atualizacao de infraestrutura [1, 3, 9].

#### 7.2.6.2. Modelo de Dados e Topologia
O JSON tradicional organiza os dados em uma estrutura de arvore hierarquica puramente local, composta por elementos sintaticos especificos: objetos (mapas relacionando chaves a valores), arrays (colecoes ordenadas), strings, numeros, valores booleanos e nulos [12, 40].

O JSON-LD estende essa base sintatica de forma a representar o ==modelo de dados RDF== (Resource Description Framework), que descreve grafos direcionados rotulados [12, 213, 214]:
* Nos do Grafo: Sao recursos (que podem ser identificados globalmente por IRIs ou de forma local por identificadores de nos em branco/blank nodes) ou valores literais [10, 11, 214].
* Arestas Direcionadas: Sao as conexoes ou propriedades do grafo, sempre representadas por chaves que se expandem para IRIs globais [10, 214].
* Grafos Nomeados e Default Graph: Permite empacotar multiplos grafos (rotulados com um nome/IRI especifico) juntamente com um grafo padrao desprovido de nome em um único documento ou conjunto de dados [165, 214].

#### 7.2.6.3. padrão IRI
Com base na especificação da [RFC 3987](https://www.rfc-editor.org/info/rfc3987/), o funcionamento estrutural dos **IRIs (Internationalized Resource Identifiers)**, juntamente com as regras normativas e exemplos práticos para converter URIs legados em IRIs, está detalhado a seguir:

##### 7.2.6.3.1. A Sintaxe Geral do IRI

- **Extensão de Caracteres**: A sintaxe do IRI estende diretamente a definição de URI estabelecida na RFC 3986, expandindo a classe de caracteres **não reservados (unreserved)** para incluir os caracteres do **UCS (Universal Character Set)** acima de `U+007F`.
- **Uso de Delimitadores**: Caracteres fora do repertório US-ASCII pertencem à categoria `iunreserved` e **não são reservados**. Portanto, eles **não podem** ser adotados para fins sintáticos de delimitação de componentes em novos esquemas (por exemplo, o caractere `U+00A2` não pode delimitar componentes).
- **Estrutura de Componentes**: O formato aceita esquemas idênticos aos de URIs, mas introduz equivalentes internacionalizados para as subpartes (como `iauthority`, `iuserinfo`, `ihost`, `ireg-name`, `ipath`, `iquery` e `ifragment`).



##### 7.2.6.3.2. Regras de Conversão de URIs Legados para IRIs

A conversão de um URI convencional para um IRI visa remover as codificações percentuais (_percent-encodings_) sempre que possível, transformando-as nos caracteres nativos legíveis. O processo normativo exige a execução estrita dos seguintes passos:

1. **Representação**: Representar o URI original como uma sequência de octetos em US-ASCII.
2. **Decodificação de Percent-Encoding**: Converter todas as sequências `%HH` (onde HH são dois dígitos hexadecimais) para os seus respectivos octetos, **exceto** aquelas correspondentes ao próprio caractere `%`, a caracteres na categoria de reservados (`reserved`) ou a caracteres US-ASCII que não são permitidos em URIs.
3. **Validação de UTF-8**: Analisar os octetos resultantes do passo 2. Qualquer octeto ou sequência de octetos que **não represente** uma sequência de codificação UTF-8 estritamente válida deve ser **re-percent-encodada**.
4. **Filtro de Caracteres Proibidos**: Analisar os caracteres gerados em UTF-8. Se algum caractere resultante for inadequado para exibição direta em um IRI (como caracteres de controle bidirecional invisíveis ou caracteres excluídos por segurança), ele deve ser **re-percent-encodado**.
5. **Interpretação**: Interpretar a sequência de octetos final resultante como uma string de caracteres codificada em **UTF-8**.

**Regra de Ouro**: As conversões de URIs para IRIs **nunca devem utilizar qualquer outra codificação de caracteres que não seja o UTF-8** nos passos 3 e 4. Mesmo que o contexto permita deduzir que o URI original usava outra codificação (como ISO-8859-1), a conversão direta para caracteres é proibida para evitar que o IRI resultante seja mapeado de volta para um URI diferente do original.



##### 7.2.6.3.3. Exemplos Práticos de Conversão (URI \(\rightarrow\) IRI)

###### 7.2.6.3.3.1. Exemplo 1: Conversão Bem-Sucedida de Caractere Internacional

- **URI Original**: `http://www.example.org/D%C3%BCrst`
- **Processamento**: A sequência `%C3%BC` é convertida para os octetos `<c3><bc>`. Como essa sequência é um UTF-8 válido e seguro, ela é mantida e interpretada como o caractere `U+00FC` (letra minúscula `ü` com trema).
- **IRI Resultante**: `http://www.example.org/Dürst` (representado em XML como `http://www.example.org/D&#xFC;rst`).

###### 7.2.6.3.3.2. Exemplo 2: Bloqueio de Codificação Não-UTF-8

- **URI Original**: `http://www.example.org/D%FCrst`
- **Processamento**: O termo `%FC` é convertido para o octeto `<fc>`. Embora o octeto `<fc>` represente a letra `ü` na codificação legada ISO-8859-1, ele **não é** um padrão UTF-8 válido. Por segurança e para evitar incompatibilidades futuras de mapeamento, o octeto é re-percent-encodado de volta ao formato original.
- **IRI Resultante**: `http://www.example.org/D%FCrst` (permanece inalterado).

###### 7.2.6.3.3.3. Exemplo 3: Tratamento de Caractere de Controle Proibido e Domínio Punycode

- **URI Original**: `http://xn--99zt52a.example.org/%e2%80%ae`
- **Processamento**: A sequência `%e2%80%ae` representa o caractere de controle de texto bidirecional `U+202E` (_Right-to-Left Override_). Por regras de segurança que proíbem o uso direto desse caractere em IRIs, ele é re-percent-encodado (preferencialmente em letras maiúsculas). O domínio em Punycode `xn--99zt52a` pode opcionalmente ser convertido para caracteres normativos por sistemas com conhecimento de esquema.
- **IRI Resultante**: `http://納豆.example.org/%E2%80%AE` (onde `xn--99zt52a` é convertido para os caracteres japoneses de "Natto": `U+7D0D` e `U+8C46`).



##### 7.2.6.3.4. Mapeamento Inverso (IRI \(\rightarrow\) URI)

Para que os sistemas legados de recuperação de dados funcionem, os IRIs são mapeados de volta para URIs aplicando a operação inversa:

1. Os caracteres lógicos do IRI são representados e normalizados em formato **NFC** (Normalization Form C), a menos que já estejam em uma codificação baseada em Unicode.
2. Cada caractere estendido (`ucschar` ou `iprivate`) é convertido em octetos usando **UTF-8**.
3. Cada octeto resultante é codificado usando o padrão de escape percentual **`%HH`** (usando preferencialmente letras maiúsculas para reduzir a variabilidade).

Se o esquema utilizar nomes de domínio, o componente `ireg-name` pode ser opcionalmente convertido usando a operação **ToASCII** (IDNA), substituindo rótulos internacionalizados por sequências compatíveis iniciadas com `xn--` para maximizar a interoperabilidade.


#### 7.2.6.4. Sintaxe e Restricoes de Chaves
Enquanto o JSON convencional e muito flexivel quanto a duplicidade de chaves (variando o comportamento conforme a biblioteca ou linguagem que o processa), o JSON-LD aplica regras gramaticais estritas:
* Unicidade Absoluta: Em contraste com o JSON comum, as chaves em objetos JSON-LD devem ser estritamente unicas [219].
* Sensibilidade a Letras: Todas as chaves, palavras-chave e valores em JSON-LD sao estritamente sensiveis a maiusculas e minúsculas [20].
* ==Chaves sem Significado Semantico==: Qualquer chave JSON que nao possa ser mapeada para uma IRI valida através do contexto ativo, ou que nao seja uma palavra-chave reservada, e ==completamente desconsiderada no processamento semantico do grafo==, embora permaneca intacta na sintaxe do arquivo [36, 216].

#### 7.2.6.5. Palavras-Chave Reservadas
O JSON-LD introduz um conjunto de ==chaves sintaticas especiais== denominadas keywords, obrigatoriamente precedidas pelo caractere `@` [13, 221]. O JSON tradicional nao possui chaves reservadas com esta notacao ou significado especial. As principais keywords que diferenciam o processamento do JSON-LD sao:
* `@context`: Define os termos locais e atalhos utilizados no documento, mapeando-os para IRIs de vocabularios compartilhados [13, 26, 27].
* `@id`: Define de forma exclusiva o identificador global (IRI ou blank node) do no que esta sendo descrito [14, 38].
* `@type`: Define a classificacao semantica de um no ou o tipo de dado de um valor literal [15, 96, 99].
* `@value`: Especifica o dado bruto associado a um determinado literal do grafo [14].
* `@language` e `@direction`: Permitem a internacionalizacao de strings, associando tags de idioma (BCP47) e direcao de leitura ("ltr" ou "rtl") [14, 15, 112, 115].
* `@container`, `@list` e `@set`: Controlam como colecoes de dados devem ser estruturadas e interpretadas [15, 16, 121, 126].
* `@nest`: Agrupa chaves relacionadas sob um objeto intermediario por conveniencia de APIs comuns, instruindo o processador semantico a ignorar esse aninhamento e ler as chaves como propriedades diretas do no [17, 129, 130].
* `@json`: Declara que o valor de uma propriedade e um literal JSON puro, contendo dados que nao devem ser interpretados como grafos ou triplas semanticas [19, 101, 102].

##### 7.2.6.5.1. lista completa

Com base na especificação **JSON-LD 1.1**, a lista completa de **palavras-chave reservadas** (tokens de sintaxe que iniciam com `@`) encontradas na fonte para complementar a sua síntese é detalhada a seguir:

###### 7.2.6.5.1.1. Palavras-Chave de Uso Geral e Contexto
*   **`@base`**: Define o **IRI base** para a resolução de referências de IRI relativo no documento [1, 2].
*   **`@container`**: Define o **tipo de contêiner padrão** para um termo, permitindo organizar valores como `@list`, `@set`, `@language`, `@index`, `@id`, `@graph` ou `@type` [3, 4].
*   **`@context`**: Define o **contexto local** que mapeia nomes curtos (termos) para IRIs e define regras de processamento [5, 6].
*   **`@direction`**: Define a **direção base** para strings ou strings marcadas por idioma (ex: "ltr" ou "rtl") [5, 7, 8].
*   **`@graph`**: Utilizado para expressar um **grafo ou conjunto de grafos nomeados** [6, 9, 10].
*   **`@id`**: Identifica exclusivamente um nó no grafo por meio de um **IRI ou identificador de nó em branco** [11, 12].
*   **`@import`**: Permite carregar e mesclar uma **definição de contexto externa** dentro de outro contexto [13-15].
*   **`@included`**: Define um bloco para incluir **objetos de nó secundários** que podem ser referenciados pelo nó principal [13, 16, 17].
*   **`@index`**: Especifica uma chave usada para **indexar informações** semanticamente neutras em um mapa de índices [1, 18, 19].
*   **`@json`**: Indica que o valor associado deve ser tratado estritamente como um **literal JSON** e não interpretado como JSON-LD [17, 20, 21].
*   **`@language`**: Especifica a **tag de idioma** (conforme BCP47) para uma string ou define o idioma padrão do contexto [11, 19, 22].
*   **`@list`**: Expressa um **conjunto ordenado** de dados (equivalente a uma lista RDF) [1, 8, 23].
*   **`@nest`**: Agrupa propriedades relacionadas em um objeto intermediário que é **semanticamente transparente** para o grafo [9, 24, 25].
*   **`@none`**: Atua como uma **chave de índice especial** para representar a ausência de um valor (ex: em mapas de idioma ou de tipo) [9, 25, 26].
*   **`@prefix`**: Determina se um termo pode ser utilizado como prefixo para construir um **IRI compacto** [9, 27, 28].
*   **`@propagate`**: Controla se as definições de um contexto se **propagam para objetos de nó** subsequentes ou se expiram ao entrar em um novo nó [20, 28, 29].
*   **`@protected`**: Impede que definições de termos em um contexto sejam **substituídas ou removidas** por contextos subsequentes [13, 28, 30].
*   **`@reverse`**: Utilizado para declarar **propriedades inversas** (apontando do objeto para o sujeito) [1, 28, 31].
*   **`@set`**: Expressa um **conjunto não ordenado** e garante que o valor seja sempre representado como um array [1, 32, 33].
*   **`@type`**: Define o **tipo de um nó** (classe) ou o **tipo de dado** de um valor literal [3, 15, 34].
*   **`@value`**: Especifica o **valor bruto** de um objeto de valor (como uma string ou número) no grafo [11, 35].
*   **`@version`**: Define o **modo de processamento** do JSON-LD (ex: 1.1) para habilitar novos recursos [35-37].
*   **`@vocab`**: Estabelece um **prefixo de vocabulário comum** para expandir propriedades e tipos que não possuem mapeamento explícito [9, 17, 38].

###### 7.2.6.5.1.2. Palavras-Chave Específicas de Framing (Enquadramento)
Estas palavras-chave são utilizadas em **objetos de enquadramento** para moldar a saída dos dados [39]:
*   **`@default`**: Fornece um valor padrão caso a propriedade esteja ausente [39].
*   **`@embed`**: Controla como os objetos são incorporados (valores: `@always`, `@once`, `@never`) [39].
*   **`@explicit`**: Determina se apenas as propriedades explicitamente presentes no quadro devem ser incluídas [39].
*   **`@omitDefault`**: Instrui o processador a omitir propriedades que usam valores padrão [39].
*   **`@requireAll`**: Indica que todas as propriedades especificadas no quadro devem estar presentes para que um nó seja selecionado [39].
*   **`@null`**: Usado em padrões de enquadramento para representar valores nulos [39].

**Nota importante**: Todas as chaves, palavras-chave e valores em JSON-LD são **sensíveis a maiúsculas e minúsculas** [13].

#### 7.2.6.6. Comportamento de Arrays e Ordenacao
A nocao de ordenacao de dados e interpretada de formas diametralmente opostas entre os dois formatos:
* Ordenacao Inerente no JSON: No JSON convencional, arrays sao sempre estruturas ordenadas por definicao [118].
* Desordenacao no Grafo JSON-LD: Como os grafos semanticos nao possuem ordem nativa para as ligacoes entre seus nos, os arrays comuns em JSON-LD nao transmitem nenhuma ordenacao por padrao [49, 118].
* Listas Ordenadas Semanticas: Para manter a ordenacao estrita de colecoes no JSON-LD, e obrigatorio utilizar a keyword `@list` ou definir `@container: @list` no contexto [121, 122, 231].
* Forca de Representacao com @set: A definicao `@container: @set` instrui o processador a sempre serializar determinados termos locais na forma de arrays sintaticos (mesmo se contiverem um único elemento), normalizando o processamento por parte de softwares clientes [126, 231].

#### 7.2.6.7. Tratamento de Valores Nulos
O comportamento ao encontrar o token `null` difere drasticamente:
* Significado no JSON: No JSON comum, `null` representa a existencia de uma propriedade cujo valor e nulo ou ausente [40].
* Eliminacao Semantica: No JSON-LD, a presenca de um valor `null` instrui o processador semantico a descartar e remover inteiramente a propriedade ou entrada correspondente do grafo resultante durante a expansao do documento [104, 216].
* Preservacao em Literais: O token `null` so e preservado formalmente na arvore de dados quando a propriedade associada e estritamente tipada com `@type: @json`, caso em que o bloco e considerado um literal estruturado opaco [104].

#### 7.2.6.8. Mapeamento Contextual Transparente
O grande diferencial do JSON-LD e a capacidade de desacoplar os dados brutos de sua interpretacao semantica por meio do `@context` [25].
* O Contexto Semantico: O `@context` permite mapear termos simples (como "name") para URIs robustas (como "http://schema.org/name"), fornecendo desambiguacao sem forcar o desenvolvedor a escrever codigos verbosos [23, 24, 26].
* Coercao Semantica: Strings simples no JSON-LD podem ser coagidas automaticamente pelo contexto para assumirem comportamentos semanticos avancados, como interpretacao direta de tipos de dados ou conversao automatica de chaves para identificadores de recursos (`@id`) [37, 105].
* Integracao com JSON Legado: Sistemas podem passar a consumir documentos JSON comuns ja publicados como se fossem JSON-LD. Isso e alcancado sem editar o arquivo de dados original, simplesmente enviando o cabecalho HTTP Link Header (`rel="http://www.w3.org/ns/json-ld#context"`, `type="application/ld+json"`) apontando para um arquivo de contexto externo [9, 31, 202, 203].

#### 7.2.6.9. Diagrama de Diferencas Sintaticas e Semanticas
```mermaid
graph TD
    JSON[JSON Convencional] -->|Diferencas| JLD[JSON-LD 1.1]
    
    JLD --> NodeModel[Modelo: Grafo Semantico RDF]
    JSON --> TreeModel[Modelo: Arvore Hierarquica Local]
    
    JLD --> Identifiers[Identificadores Globais via @id e IRIs]
    JSON --> KeysOnly[Chaves Locais Arbitrarias]
    
    JLD --> SemanticCtx[Definicao de Contexto via @context]
    JSON --> AppSchema[Validacao/Schema Externo a Sintaxe]
    
    JLD --> ArrayUnordered[Arrays: Desordenados por padrao]
    JSON --> ArrayOrdered[Arrays: Ordenados por padrao]
    
    JLD --> SpecialStrings[Strings com Idioma e Direcao]
    JSON --> SimpleStrings[Strings Literais Puras]
```

## 7.3. Modelagem da Arquitetura para o KMS de Agentes de IA

Para um Sistema de Gestão de Conhecimento voltado para agentes de codificação, **nenhum formato deve ser usado isoladamente**. A arquitetura ideal deve adotar uma abordagem em camadas, inspirada nos princípios de OWS (Separação entre *Schema/Ontologia*, *Dados/Grafo* e *Apresentação/Contexto*).

### 7.3.1. Camada 1: A Ontologia e o Grafo (O "Cérebro" Semântico)
*   **Formato Principal:** **JSON-LD** ou **YAML**.
*   **Função:** Definir as regras do ecossistema de software. Ex: O que é um `Microservico`, como ele se `ComunicaCom` um `BancoDeDados`.
*   **Por que:** Permite que o agente de IA faça *inferência*. Se o agente sabe que `ServicoA` depende de `ServicoB` (via JSON-LD), ele pode deduzir que um *deploy* de A exige validação em B.

### 7.3.2. Camada 2: O Contexto e a Documentação (A "Memória" Narrativa)
*   **Formato Principal:** **Markdown (`.md`)**.
*   **Função:** Manter o *RAG* (Retrieval-Augmented Generation). Decisões de arquitetura (ADRs), comentários de código, e manuais de uso.
*   **Por que:** A IA raciocina melhor em linguagem natural. O Markdown permite que o agente leia a *intenção* por trás do código, não apenas a estrutura.

### 7.3.3. Camada 3: O Estado e a Configuração (A "Execução")
*   **Formato Principal:** **TOML** ou **YAML**.
*   **Função:** Configuração de ambientes, *pipelines* de CI/CD, e metadados de pacotes.
*   **Por que:** Precisão determinística para que o agente de IA possa gerar ou modificar arquivos de infraestrutura sem quebrar a sintaxe.

## 7.4. Tabela Comparativa

| Formato              | 1. Facilidade de Leitura (IA)            | 2. Acuracidade / Precisão                           | 3. Características de Sintaxe (Impacto na IA)                   | 4. Recursos para Knowledge Graphs / OWS                                           | Uso Ideal no KMS para Agentes                                   |
| :------------------- | :--------------------------------------- | :-------------------------------------------------- | :-------------------------------------------------------------- | :-------------------------------------------------------------------------------- | :-------------------------------------------------------------- |
| **Markdown (`.md`)** | 🟢 **Excepcional** (Nativo para LLMs)    | 🔴 **Baixa** (Sujeito a alucinações e ambiguidades) | Leve, tokenização eficiente. Falta de rigidez estrutural.       | 🟡 **Fraco** (Usado apenas para grafos visuais via Mermaid ou links conceituais). | Documentação, ADRs, Prompts de contexto, Comentários.           |
| **JSON (`.json`)**   | 🟢 **Alta** (Nativo para *Tool Use*)     | 🟢 **Muito Alta** (Parsing determinístico)          | Verboso. Alto consumo de tokens devido a aspas e chaves.        | 🟢 **Excelente** (Base do **JSON-LD** e grafos aninhados).                        | Respostas de API, Extração de dados, Definição de nós do Grafo. |
| **YAML (`.yaml`)**   | 🟢 **Alta** (Limpo e hierárquico)        | 🟡 **Média/Alta** (Risco de falha por indentação)   | Sensível a espaços em branco. Excelente para anotações.         | 🟢 **Muito Bom** (Serialização RDF, definição de *Schemas*).                      | Definição de Ontologias, Configuração de Agentes, OpenAPI.      |
| **XML (`.xml`)**     | 🟡 **Média** (Entendível, mas verboso)   | 🟢 **Extrema** (Validação via XSD)                  | Altamente verboso. "Ruído" de tags satura a janela de contexto. | 🟢 **O Padrão** (RDF/XML, OWL - Base da Web Semântica).                           | Intercâmbio de Ontologias complexas, Sistemas Legados.          |
| **TOML (`.toml`)**   | 🟡 **Média** (Foco em config, não texto) | 🟢 **Alta** (Tipagem forte e rígida)                | Minimalista, plano. Ruim para hierarquias profundas.            | 🔴 **Fraco** (Inadequado para modelagem de triplas/grafos).                       | Metadados de pacotes, Configuração de ambiente do Agente.       |



## 7.5. Conclusão e Recomendação Arquitetural

Para modelar um **Sistema de Gestão de Conhecimento (KMS)** que alimente agentes de IA de codificação com base em princípios de **OWS (Ontologias)**:

1.  **Não use XML para o dia a dia do agente:** Embora seja o padrão histórico de OWS (RDF/XML), o custo de tokens e a verbosidade atrapalham a janela de contexto dos LLMs atuais.
2.  **Adote JSON-LD como espinha dorsal do Grafo:** Use JSON (especificamente com anotações `@context` do JSON-LD) para mapear a arquitetura do software (ex: mapear repositórios, dependências, APIs). Isso transforma o código em um Grafo de Conhecimento consultável.
3.  **Use YAML para a "Cola" Semântica:** Utilize YAML para definir os *schemas* das ontologias (as regras do que pode ser conectado ao que) devido à sua legibilidade e suporte a hierarquias.
4.  **Mantenha Markdown como a "Interface Humano-IA":** O agente deve usar Markdown para explicar suas descobertas no grafo, gerar documentação e raciocinar passo-a-passo (Chain-of-Thought).

A combinação **JSON-LD (Grafo/Dados) + YAML (Schema/Regras) + Markdown (Contexto/Raciocínio)** formará a arquitetura mais resiliente, precisa e econômica em termos de tokens para agentes de IA de software.



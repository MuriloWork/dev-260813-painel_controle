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

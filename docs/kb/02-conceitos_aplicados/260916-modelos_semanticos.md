[[01-conceitos_software_ontologia#3. configuração ponderada entre modelos]]

# 1. rascunhos de modelos

## 1.1. arquitetura modelo dos repositorios 
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

## 1.2. modelo para repositorios de documentos `kb` tipo OKF
- onde é encontrado: repositorios com tipo conteudo [documentos] e tipo dominio: [conhecimento conceitual, conhecimento aplicado, regras sobre kb concepts, regras sobre codificação, regras sobre agent pipelines, system models]
### 1.2.1. modelo geral
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

### 1.2.2. modelo especifico para INDEX.md
#### 1.2.2.1. modelo especifico para INDEX.md na pasta raiz `docs^kb`
### 1.2.3. modelo especifico para README.md
#### 1.2.3.1. modelo especifico para README.md na pasta raiz `docs^kb`

## 1.3. demais modelos
### 1.3.1. modelo para repositorios de documentos `agents`
### 1.3.2. modelo para repositorios de documentos `spec`
### 1.3.3. modelo para repositorios de documentos `gsd-planning`
### 1.3.4. modelo para repositorios de documentos `sessions`
### 1.3.5. modelo para repositorios de dados
#### 1.3.5.1. KG - Knowledge Graph
[[01-conceitos_software_se#7. Knowledge Graph|conceitos KG]]

### 1.3.6. modelo para repositorios de codigos

## 1.4. Análise de Formatos de Documentos para Agentes de IA

### 1.4.1. Introdução e Contexto (A Interseção entre OWS e Agentes de IA)
A construção de um **Sistema de Gestão de Conhecimento (KMS)** para agentes de IA de codificação (como *coding assistants*, *autonomous dev agents*) exige a transição de dados não estruturados para representações semânticas. É aqui que os **OWS (Web Ontology Systems / Sistemas de Ontologia Web)** e os **Knowledge Graphs (Grafos de Conhecimento)** entram em cena.

Agentes de IA "leem" documentos de duas formas distintas:
1. **Leitura Estocástica (LLM/Attention):** O modelo processa o texto como tokens, inferindo significado baseado em padrões (usado em Markdown).
2. **Leitura Determinística (Parser/AST):** O agente usa ferramentas para extrair dados exatos de estruturas rígidas (usado em JSON, XML).

Para modelar um KMS robusto, precisamos entender como os formatos de serialização (`.md`, `.xml`, `.json`, `.yaml`, `.toml`) se comportam sob a ótica da IA e como eles podem ser mapeados para ontologias (padrões OWS como RDF, OWL, JSON-LD).



### 1.4.2. Análise dos Formatos sob os Critérios Definidos

#### 1.4.2.1. Markdown (`.md`)
O Markdown é a linguagem franca da documentação e do *prompt engineering*.
*   **1. Facilidade/Aptidão para leitura:** **Excepcional**. LLMs são massivamente treinados em Markdown. A IA compreende intuitivamente a hierarquia (headers), listas e blocos de código.
*   **2. Acuracidade/Precisão:** **Baixa a Média**. A leitura é semântica, não estrutural. A IA pode "alucinar" a relação entre dois tópicos se o texto for ambíguo. Não há garantia de integridade de dados.
*   **3. Características de sintaxe:** Baseada em texto puro com marcações leves (`#`, `*`, ```). A falta de fechamento rígido (como tags) torna a tokenização muito eficiente (baixo custo de contexto).
*   **4. Recursos para Knowledge Graphs (OWS):** **Fraco nativamente, mas excelente para metadados**. Não suporta grafos nativamente, mas é o melhor formato para embutir grafos visuais (via *Mermaid.js*) ou criar "Wikilinks" (`[[Entidade]]`) que agentes podem usar para indexar conexões conceituais.

#### 1.4.2.2. YAML (`.yaml`)
Muito comum em configuração (Kubernetes, CI/CD) e documentação estruturada (OpenAPI/Swagger).
*   **1. Facilidade/Aptidão para leitura:** **Alta**. Mais legível para humanos e IAs do que JSON, pois remove a "poluição" visual de chaves e aspas.
*   **2. Acuracidade/Precisão:** **Média/Alta**. A precisão é alta, mas a **sensibilidade a espaços em branco (indentação)** é uma armadilha. Um erro de indentação gerado pela IA quebra o parser, causando falhas silenciosas ou erros de compilação no agente.
*   **3. Características de sintaxe:** Baseada em indentação e hífens. Permite anotações e referências (âncoras), o que economiza tokens.
*   **4. Recursos para Knowledge Graphs (OWS):** **Muito Bom**. YAML é frequentemente usado como uma sintaxe alternativa para RDF (RDF/YAML). É ideal para definir *schemas* de ontologias (classes e propriedades) de forma hierárquica.

ver tambem [YAML-LD specifications](https://w3c.github.io/yaml-ld/), [YAML-LD github](https://github.com/w3c/yaml-ld/)

#### 1.4.2.3. TOML (`.toml`)
Formato de configuração focado em ser minimalista e mapear diretamente para dicionários/hash maps.
*   **1. Facilidade/Aptidão para leitura:** **Média/Alta**. Muito limpo, mas a IA o lê mais como um arquivo de configuração de estado do que como um documento de conhecimento.
*   **2. Acuracidade/Precisão:** **Alta**. Estrutura rígida, tipagem forte (datas, inteiros, strings).
*   **3. Características de sintaxe:** Baseado em seções `[secao]` e pares `chave = valor`. Não lida bem com hierarquias profundas ou listas complexas de objetos.
*   **4. Recursos para Knowledge Graphs (OWS):** **Fraco**. A falta de suporte nativo a hierarquias profundas e aninhamentos complexos o torna inadequado para modelagem de grafos de conhecimento ou ontologias.

#### 1.4.2.4. XML (`.xml`)
O formato clássico de documentos estruturados e base de sistemas OWS tradicionais.
*   **1. Facilidade/Aptidão para leitura:** **Média**. IAs entendem XML perfeitamente, mas a leitura é "cansativa" em termos de janela de contexto devido à verbosidade das tags de fechamento.
*   **2. Acuracidade/Precisão:** **Extrema**. Com validação via XSD (XML Schema Definition), a precisão é absoluta. A IA sabe exatamente o que é um atributo e o que é um nó.
*   **3. Características de sintaxe:** Tags aninhadas. Extremamente rígido. Gera um *overhead* de tokens muito alto (ex: `<relation>...</relation>` gasta muitos tokens apenas para dizer "relação").
*   **4. Recursos para Knowledge Graphs (OWS):** **O Padrão Ouro (RDF/XML, OWL/XML)**. A Web Semântica (OWS) foi construída sobre XML. É o melhor formato para definir ontologias complexas, restrições de classes e inferências lógicas.

#### 1.4.2.5. JSON (`.json`)
O formato nativo da web e das APIs, base fundamental para a serialização de ontologias modernas.
*   **1. Facilidade/Aptidão para leitura:** **Alta**. Agentes de IA possuem *function calling* e *tool use* nativos baseados em JSON. A IA lê JSON como uma árvore lógica de objetos.
*   **2. Acuracidade/Precisão:** **Muito Alta**. A sintaxe é determinística. Um parser de JSON não falha se o schema for respeitado. A IA não "inventa" chaves ou tipos de dados.
*   **3. Características de sintaxe:** Uso intensivo de aspas, chaves e colchetes. **Ponto negativo:** É verboso e consome muitos tokens (ruído sintático), o que pode saturar a janela de contexto do agente.
*   **4. Recursos para Knowledge Graphs (OWS):** **Excelente**. O **JSON-LD** é o padrão W3C para vincular dados na web como grafos. Pares de chave-valor mapeiam perfeitamente para triplas RDF (Sujeito-Predicado-Objeto).
#### 1.4.2.6. JSON-LD (diferencas para JSON)

##### 1.4.2.6.1. Conceito e Proposito
O JSON convencional e projetado prioritariamente como um formato leve de intercambio de dados e mensagens entre sistemas, focado na simplicidade e na facilidade de leitura humana [1, 22]. No entanto, ao integrar dados provenientes de fontes distintas, chaves identicas em documentos JSON diferentes podem entrar em conflito e gerar ambiguidades de interpretacao [22]. Alem disso, o JSON tradicional carece de suporte nativo para hiperlinks ou identificadores globais, dificultando a interconexao de recursos distribuídos na Web [22].

O JSON-LD (JSON-based Linked Data) foi desenvolvido como um formato semantico totalmente compatível com o JSON convencional [1, 3]. Ele funciona como uma extensao que permite que sistemas e interpretadores JSON ja existentes compreendam dados estructurados como Linked Data (Dados Conectados) com o minimo de alteracoes, oferecendo um caminho suave de atualizacao de infraestrutura [1, 3, 9].

##### 1.4.2.6.2. Modelo de Dados e Topologia
O JSON tradicional organiza os dados em uma estrutura de arvore hierarquica puramente local, composta por elementos sintaticos especificos: objetos (mapas relacionando chaves a valores), arrays (colecoes ordenadas), strings, numeros, valores booleanos e nulos [12, 40].

O JSON-LD estende essa base sintatica de forma a representar o ==modelo de dados RDF== (Resource Description Framework), que descreve grafos direcionados rotulados [12, 213, 214]:
* Nos do Grafo: Sao recursos (que podem ser identificados globalmente por IRIs ou de forma local por identificadores de nos em branco/blank nodes) ou valores literais [10, 11, 214].
* Arestas Direcionadas: Sao as conexoes ou propriedades do grafo, sempre representadas por chaves que se expandem para IRIs globais [10, 214].
* Grafos Nomeados e Default Graph: Permite empacotar multiplos grafos (rotulados com um nome/IRI especifico) juntamente com um grafo padrao desprovido de nome em um único documento ou conjunto de dados [165, 214].

##### 1.4.2.6.3. padrão IRI
Com base na especificação da [RFC 3987](https://www.rfc-editor.org/info/rfc3987/), o funcionamento estrutural dos **IRIs (Internationalized Resource Identifiers)**, juntamente com as regras normativas e exemplos práticos para converter URIs legados em IRIs, está detalhado a seguir:

###### 1.4.2.6.3.1. A Sintaxe Geral do IRI

- **Extensão de Caracteres**: A sintaxe do IRI estende diretamente a definição de URI estabelecida na RFC 3986, expandindo a classe de caracteres **não reservados (unreserved)** para incluir os caracteres do **UCS (Universal Character Set)** acima de `U+007F`.
- **Uso de Delimitadores**: Caracteres fora do repertório US-ASCII pertencem à categoria `iunreserved` e **não são reservados**. Portanto, eles **não podem** ser adotados para fins sintáticos de delimitação de componentes em novos esquemas (por exemplo, o caractere `U+00A2` não pode delimitar componentes).
- **Estrutura de Componentes**: O formato aceita esquemas idênticos aos de URIs, mas introduz equivalentes internacionalizados para as subpartes (como `iauthority`, `iuserinfo`, `ihost`, `ireg-name`, `ipath`, `iquery` e `ifragment`).



###### 1.4.2.6.3.2. Regras de Conversão de URIs Legados para IRIs

A conversão de um URI convencional para um IRI visa remover as codificações percentuais (_percent-encodings_) sempre que possível, transformando-as nos caracteres nativos legíveis. O processo normativo exige a execução estrita dos seguintes passos:

1. **Representação**: Representar o URI original como uma sequência de octetos em US-ASCII.
2. **Decodificação de Percent-Encoding**: Converter todas as sequências `%HH` (onde HH são dois dígitos hexadecimais) para os seus respectivos octetos, **exceto** aquelas correspondentes ao próprio caractere `%`, a caracteres na categoria de reservados (`reserved`) ou a caracteres US-ASCII que não são permitidos em URIs.
3. **Validação de UTF-8**: Analisar os octetos resultantes do passo 2. Qualquer octeto ou sequência de octetos que **não represente** uma sequência de codificação UTF-8 estritamente válida deve ser **re-percent-encodada**.
4. **Filtro de Caracteres Proibidos**: Analisar os caracteres gerados em UTF-8. Se algum caractere resultante for inadequado para exibição direta em um IRI (como caracteres de controle bidirecional invisíveis ou caracteres excluídos por segurança), ele deve ser **re-percent-encodado**.
5. **Interpretação**: Interpretar a sequência de octetos final resultante como uma string de caracteres codificada em **UTF-8**.

**Regra de Ouro**: As conversões de URIs para IRIs **nunca devem utilizar qualquer outra codificação de caracteres que não seja o UTF-8** nos passos 3 e 4. Mesmo que o contexto permita deduzir que o URI original usava outra codificação (como ISO-8859-1), a conversão direta para caracteres é proibida para evitar que o IRI resultante seja mapeado de volta para um URI diferente do original.



###### 1.4.2.6.3.3. Exemplos Práticos de Conversão (URI \(\rightarrow\) IRI)

####### 5.2.6.3.3.1. Exemplo 1: Conversão Bem-Sucedida de Caractere Internacional

- **URI Original**: `http://www.example.org/D%C3%BCrst`
- **Processamento**: A sequência `%C3%BC` é convertida para os octetos `<c3><bc>`. Como essa sequência é um UTF-8 válido e seguro, ela é mantida e interpretada como o caractere `U+00FC` (letra minúscula `ü` com trema).
- **IRI Resultante**: `http://www.example.org/Dürst` (representado em XML como `http://www.example.org/D&#xFC;rst`).

####### 5.2.6.3.3.2. Exemplo 2: Bloqueio de Codificação Não-UTF-8

- **URI Original**: `http://www.example.org/D%FCrst`
- **Processamento**: O termo `%FC` é convertido para o octeto `<fc>`. Embora o octeto `<fc>` represente a letra `ü` na codificação legada ISO-8859-1, ele **não é** um padrão UTF-8 válido. Por segurança e para evitar incompatibilidades futuras de mapeamento, o octeto é re-percent-encodado de volta ao formato original.
- **IRI Resultante**: `http://www.example.org/D%FCrst` (permanece inalterado).

####### 5.2.6.3.3.3. Exemplo 3: Tratamento de Caractere de Controle Proibido e Domínio Punycode

- **URI Original**: `http://xn--99zt52a.example.org/%e2%80%ae`
- **Processamento**: A sequência `%e2%80%ae` representa o caractere de controle de texto bidirecional `U+202E` (_Right-to-Left Override_). Por regras de segurança que proíbem o uso direto desse caractere em IRIs, ele é re-percent-encodado (preferencialmente em letras maiúsculas). O domínio em Punycode `xn--99zt52a` pode opcionalmente ser convertido para caracteres normativos por sistemas com conhecimento de esquema.
- **IRI Resultante**: `http://納豆.example.org/%E2%80%AE` (onde `xn--99zt52a` é convertido para os caracteres japoneses de "Natto": `U+7D0D` e `U+8C46`).



###### 1.4.2.6.3.4. Mapeamento Inverso (IRI \(\rightarrow\) URI)

Para que os sistemas legados de recuperação de dados funcionem, os IRIs são mapeados de volta para URIs aplicando a operação inversa:

1. Os caracteres lógicos do IRI são representados e normalizados em formato **NFC** (Normalization Form C), a menos que já estejam em uma codificação baseada em Unicode.
2. Cada caractere estendido (`ucschar` ou `iprivate`) é convertido em octetos usando **UTF-8**.
3. Cada octeto resultante é codificado usando o padrão de escape percentual **`%HH`** (usando preferencialmente letras maiúsculas para reduzir a variabilidade).

Se o esquema utilizar nomes de domínio, o componente `ireg-name` pode ser opcionalmente convertido usando a operação **ToASCII** (IDNA), substituindo rótulos internacionalizados por sequências compatíveis iniciadas com `xn--` para maximizar a interoperabilidade.


##### 1.4.2.6.4. Sintaxe e Restricoes de Chaves
Enquanto o JSON convencional e muito flexivel quanto a duplicidade de chaves (variando o comportamento conforme a biblioteca ou linguagem que o processa), o JSON-LD aplica regras gramaticais estritas:
* Unicidade Absoluta: Em contraste com o JSON comum, as chaves em objetos JSON-LD devem ser estritamente unicas [219].
* Sensibilidade a Letras: Todas as chaves, palavras-chave e valores em JSON-LD sao estritamente sensiveis a maiusculas e minúsculas [20].
* ==Chaves sem Significado Semantico==: Qualquer chave JSON que nao possa ser mapeada para uma IRI valida através do contexto ativo, ou que nao seja uma palavra-chave reservada, e ==completamente desconsiderada no processamento semantico do grafo==, embora permaneca intacta na sintaxe do arquivo [36, 216].

##### 1.4.2.6.5. Palavras-Chave Reservadas
O JSON-LD introduz um conjunto de ==chaves sintaticas especiais== denominadas keywords, obrigatoriamente precedidas pelo caractere `@` [13, 221]. O JSON tradicional nao possui chaves reservadas com esta notacao ou significado especial. As principais keywords que diferenciam o processamento do JSON-LD sao:
* `@context`: Define os termos locais e atalhos utilizados no documento, mapeando-os para IRIs de vocabularios compartilhados [13, 26, 27].
* `@id`: Define de forma exclusiva o identificador global (IRI ou blank node) do no que esta sendo descrito [14, 38].
* `@type`: Define a classificacao semantica de um no ou o tipo de dado de um valor literal [15, 96, 99].
* `@value`: Especifica o dado bruto associado a um determinado literal do grafo [14].
* `@language` e `@direction`: Permitem a internacionalizacao de strings, associando tags de idioma (BCP47) e direcao de leitura ("ltr" ou "rtl") [14, 15, 112, 115].
* `@container`, `@list` e `@set`: Controlam como colecoes de dados devem ser estruturadas e interpretadas [15, 16, 121, 126].
* `@nest`: Agrupa chaves relacionadas sob um objeto intermediario por conveniencia de APIs comuns, instruindo o processador semantico a ignorar esse aninhamento e ler as chaves como propriedades diretas do no [17, 129, 130].
* `@json`: Declara que o valor de uma propriedade e um literal JSON puro, contendo dados que nao devem ser interpretados como grafos ou triplas semanticas [19, 101, 102].

###### 1.4.2.6.5.1. lista completa

Com base na especificação **JSON-LD 1.1**, a lista completa de **palavras-chave reservadas** (tokens de sintaxe que iniciam com `@`) encontradas na fonte para complementar a sua síntese é detalhada a seguir:

####### 5.2.6.5.1.1. Palavras-Chave de Uso Geral e Contexto
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

####### 5.2.6.5.1.2. Palavras-Chave Específicas de Framing (Enquadramento)
Estas palavras-chave são utilizadas em **objetos de enquadramento** para moldar a saída dos dados [39]:
*   **`@default`**: Fornece um valor padrão caso a propriedade esteja ausente [39].
*   **`@embed`**: Controla como os objetos são incorporados (valores: `@always`, `@once`, `@never`) [39].
*   **`@explicit`**: Determina se apenas as propriedades explicitamente presentes no quadro devem ser incluídas [39].
*   **`@omitDefault`**: Instrui o processador a omitir propriedades que usam valores padrão [39].
*   **`@requireAll`**: Indica que todas as propriedades especificadas no quadro devem estar presentes para que um nó seja selecionado [39].
*   **`@null`**: Usado em padrões de enquadramento para representar valores nulos [39].

**Nota importante**: Todas as chaves, palavras-chave e valores em JSON-LD são **sensíveis a maiúsculas e minúsculas** [13].

##### 1.4.2.6.6. Comportamento de Arrays e Ordenacao
A nocao de ordenacao de dados e interpretada de formas diametralmente opostas entre os dois formatos:
* Ordenacao Inerente no JSON: No JSON convencional, arrays sao sempre estruturas ordenadas por definicao [118].
* Desordenacao no Grafo JSON-LD: Como os grafos semanticos nao possuem ordem nativa para as ligacoes entre seus nos, os arrays comuns em JSON-LD nao transmitem nenhuma ordenacao por padrao [49, 118].
* Listas Ordenadas Semanticas: Para manter a ordenacao estrita de colecoes no JSON-LD, e obrigatorio utilizar a keyword `@list` ou definir `@container: @list` no contexto [121, 122, 231].
* Forca de Representacao com @set: A definicao `@container: @set` instrui o processador a sempre serializar determinados termos locais na forma de arrays sintaticos (mesmo se contiverem um único elemento), normalizando o processamento por parte de softwares clientes [126, 231].

##### 1.4.2.6.7. Tratamento de Valores Nulos
O comportamento ao encontrar o token `null` difere drasticamente:
* Significado no JSON: No JSON comum, `null` representa a existencia de uma propriedade cujo valor e nulo ou ausente [40].
* Eliminacao Semantica: No JSON-LD, a presenca de um valor `null` instrui o processador semantico a descartar e remover inteiramente a propriedade ou entrada correspondente do grafo resultante durante a expansao do documento [104, 216].
* Preservacao em Literais: O token `null` so e preservado formalmente na arvore de dados quando a propriedade associada e estritamente tipada com `@type: @json`, caso em que o bloco e considerado um literal estruturado opaco [104].

##### 1.4.2.6.8. Mapeamento Contextual Transparente
O grande diferencial do JSON-LD e a capacidade de desacoplar os dados brutos de sua interpretacao semantica por meio do `@context` [25].
* O Contexto Semantico: O `@context` permite mapear termos simples (como "name") para URIs robustas (como "http://schema.org/name"), fornecendo desambiguacao sem forcar o desenvolvedor a escrever codigos verbosos [23, 24, 26].
* Coercao Semantica: Strings simples no JSON-LD podem ser coagidas automaticamente pelo contexto para assumirem comportamentos semanticos avancados, como interpretacao direta de tipos de dados ou conversao automatica de chaves para identificadores de recursos (`@id`) [37, 105].
* Integracao com JSON Legado: Sistemas podem passar a consumir documentos JSON comuns ja publicados como se fossem JSON-LD. Isso e alcancado sem editar o arquivo de dados original, simplesmente enviando o cabecalho HTTP Link Header (`rel="http://www.w3.org/ns/json-ld#context"`, `type="application/ld+json"`) apontando para um arquivo de contexto externo [9, 31, 202, 203].

##### 1.4.2.6.9. Diagrama de Diferencas Sintaticas e Semanticas
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

### 1.4.3. Modelagem da Arquitetura para o KMS de Agentes de IA

Para um Sistema de Gestão de Conhecimento voltado para agentes de codificação, **nenhum formato deve ser usado isoladamente**. A arquitetura ideal deve adotar uma abordagem em camadas, inspirada nos princípios de OWS (Separação entre *Schema/Ontologia*, *Dados/Grafo* e *Apresentação/Contexto*).

#### 1.4.3.1. Camada 1: A Ontologia e o Grafo (O "Cérebro" Semântico)
*   **Formato Principal:** **JSON-LD** ou **YAML**.
*   **Função:** Definir as regras do ecossistema de software. Ex: O que é um `Microservico`, como ele se `ComunicaCom` um `BancoDeDados`.
*   **Por que:** Permite que o agente de IA faça *inferência*. Se o agente sabe que `ServicoA` depende de `ServicoB` (via JSON-LD), ele pode deduzir que um *deploy* de A exige validação em B.

#### 1.4.3.2. Camada 2: O Contexto e a Documentação (A "Memória" Narrativa)
*   **Formato Principal:** **Markdown (`.md`)**.
*   **Função:** Manter o *RAG* (Retrieval-Augmented Generation). Decisões de arquitetura (ADRs), comentários de código, e manuais de uso.
*   **Por que:** A IA raciocina melhor em linguagem natural. O Markdown permite que o agente leia a *intenção* por trás do código, não apenas a estrutura.

#### 1.4.3.3. Camada 3: O Estado e a Configuração (A "Execução")
*   **Formato Principal:** **TOML** ou **YAML**.
*   **Função:** Configuração de ambientes, *pipelines* de CI/CD, e metadados de pacotes.
*   **Por que:** Precisão determinística para que o agente de IA possa gerar ou modificar arquivos de infraestrutura sem quebrar a sintaxe.

### 1.4.4. Tabela Comparativa

| Formato              | 1. Facilidade de Leitura (IA)            | 2. Acuracidade / Precisão                           | 3. Características de Sintaxe (Impacto na IA)                   | 4. Recursos para Knowledge Graphs / OWS                                           | Uso Ideal no KMS para Agentes                                   |
| :------------------- | :--------------------------------------- | :-------------------------------------------------- | :-------------------------------------------------------------- | :-------------------------------------------------------------------------------- | :-------------------------------------------------------------- |
| **Markdown (`.md`)** | 🟢 **Excepcional** (Nativo para LLMs)    | 🔴 **Baixa** (Sujeito a alucinações e ambiguidades) | Leve, tokenização eficiente. Falta de rigidez estrutural.       | 🟡 **Fraco** (Usado apenas para grafos visuais via Mermaid ou links conceituais). | Documentação, ADRs, Prompts de contexto, Comentários.           |
| **JSON (`.json`)**   | 🟢 **Alta** (Nativo para *Tool Use*)     | 🟢 **Muito Alta** (Parsing determinístico)          | Verboso. Alto consumo de tokens devido a aspas e chaves.        | 🟢 **Excelente** (Base do **JSON-LD** e grafos aninhados).                        | Respostas de API, Extração de dados, Definição de nós do Grafo. |
| **YAML (`.yaml`)**   | 🟢 **Alta** (Limpo e hierárquico)        | 🟡 **Média/Alta** (Risco de falha por indentação)   | Sensível a espaços em branco. Excelente para anotações.         | 🟢 **Muito Bom** (Serialização RDF, definição de *Schemas*).                      | Definição de Ontologias, Configuração de Agentes, OpenAPI.      |
| **XML (`.xml`)**     | 🟡 **Média** (Entendível, mas verboso)   | 🟢 **Extrema** (Validação via XSD)                  | Altamente verboso. "Ruído" de tags satura a janela de contexto. | 🟢 **O Padrão** (RDF/XML, OWL - Base da Web Semântica).                           | Intercâmbio de Ontologias complexas, Sistemas Legados.          |
| **TOML (`.toml`)**   | 🟡 **Média** (Foco em config, não texto) | 🟢 **Alta** (Tipagem forte e rígida)                | Minimalista, plano. Ruim para hierarquias profundas.            | 🔴 **Fraco** (Inadequado para modelagem de triplas/grafos).                       | Metadados de pacotes, Configuração de ambiente do Agente.       |



### 1.4.5. Conclusão e Recomendação Arquitetural

Para modelar um **Sistema de Gestão de Conhecimento (KMS)** que alimente agentes de IA de codificação com base em princípios de **OWS (Ontologias)**:

1.  **Não use XML para o dia a dia do agente:** Embora seja o padrão histórico de OWS (RDF/XML), o custo de tokens e a verbosidade atrapalham a janela de contexto dos LLMs atuais.
2.  **Adote JSON-LD como espinha dorsal do Grafo:** Use JSON (especificamente com anotações `@context` do JSON-LD) para mapear a arquitetura do software (ex: mapear repositórios, dependências, APIs). Isso transforma o código em um Grafo de Conhecimento consultável.
3.  **Use YAML para a "Cola" Semântica:** Utilize YAML para definir os *schemas* das ontologias (as regras do que pode ser conectado ao que) devido à sua legibilidade e suporte a hierarquias.
4.  **Mantenha Markdown como a "Interface Humano-IA":** O agente deve usar Markdown para explicar suas descobertas no grafo, gerar documentação e raciocinar passo-a-passo (Chain-of-Thought).

A combinação **JSON-LD (Grafo/Dados) + YAML (Schema/Regras) + Markdown (Contexto/Raciocínio)** formará a arquitetura mais resiliente, precisa e econômica em termos de tokens para agentes de IA de software.


# 2. ontologia para dominio mbse 
|[[01-conceitos_software_ontologia|conceitos ontologia]]|
|[[01-conceitos_software_ontologia#4. ontology development framework|ontology pipeline]]|

## 2.1. taxonomia (vocabulario + hierarquia) 

domínio: 
### 2.1.1. vocabulario 
Lista de skos:Concept (OWL entidades RDF sujeito, objeto) Predicado default = skos:narrower. Demais predicados  indicados entre colchetes, ex.: [skos:inScheme].

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
- **conceito**: repositorio 
	- **definição**: 
	- identificação [tipo, URI] 
- **conceito**: arquitetura de repositorio 
	- **definição**: pasta agrupadora, por assuntos, por tipos de artefatos, por camada do acervo 
	- **camadas/zonas do acervo**: 
		- frequência de consulta [do, system, km, mem]
		- agrupamento de assuntos 
	- **componentes**: folder 
		- **finalidade**:  [do, system, km, mem] 
		- **componentes**: artefato, arquivo
			- path, tipo 
			- metadados 
		- identificação [path]
- modelo 
- projeto, sessão 
- system 
- bloco functional 
- outros conceitos okf???
	- identificação
	- proveniencia
	- relacionamento
	- persistência [documentos, seções/endereços/labels, relacionamentos, dados]
	- versionamento + historico [decisão, alternativas consideradas, justificativa, consequência, elementos afetados]
	- validação
	- classification scheme 
	- subject heading 


### 2.1.2. conforme o objetivo da análise 

#### 2.1.2.1. Taxonomia por Escopo e Tipo de Conteúdo
Classifica o repositório pelo tipo de artefato ou nível de abstração que ele gerencia:
- **Repositório de Código-Fonte (VCS)**: Armazena o código bruto, histórico de commits e ramificações (branches). Exemplos: repositórios Git/GitHub e GitLab.
- **Repositório de Artefatos / Binários (Package Registry)**: Armazena pacotes compilados prontos para distribuição ou deploy. Exemplos: npm (JavaScript), Maven (Java), PyPI (Python) e Docker registries (como o Docker Hub).
- **Repositório de Modelos e Conhecimento**: Armazena documentação, diagramas de arquitetura, requisitos e ontologias do projeto.

#### 2.1.2.2. Taxonomia por Arquitetura de Distribuição
Define como os dados do repositório são armazenados e sincronizados entre os desenvolvedores:
- **Centralizado (CVCS)**: Existe apenas uma cópia mestre do repositório em um servidor central. Os desenvolvedores fazem o checkout de arquivos isolados. Exemplos: Subversion (SVN), Perforce.
- **Distribuído (DVCS)**: Cada desenvolvedor possui um clone completo do repositório em sua máquina local, incluindo todo o histórico de alterações. Exemplos: Git, Mercurial.

#### 2.1.2.3. Facetas de Classificação (Mineração de Repositórios de Software - MSR)
Em pesquisas acadêmicas e análises de ecossistemas (como o mapeamento automatizado de repositórios), adota-se uma taxonomia baseada em facetas:

| Faceta                           | Conceito / Atributos Classificados                                                                                                                        |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Domínio da Aplicação**         | Identifica a finalidade do software armazenado (ex: utilitários, frameworks, ferramentas de desenvolvimento, aplicações de pesquisa).                     |
| **Atividade de Desenvolvimento** | Categoriza o repositório pelo seu status de manutenção (ex: ativo, inativo/arquivado, incubação, espelho/mirror).                                         |
| **Modelo de Licenciamento**      | Classifica de acordo com as permissões legais do repositório (ex: Open Source - MIT, GPL, Apache; Propriatário; InnerSource).                             |
| **Estilo Arquitetural**          | Agrupa os repositórios pelo formato do código (ex: Monorepo — múltiplas aplicações em um único repositório; Polyrepo — um repositório por microsserviço). |

#### 2.1.2.4. Abordagens de Classificação Automatizada
Para lidar com a escala de milhões de repositórios públicos, a engenharia de software moderna utiliza técnicas automatizadas para derivar taxonomias e tags dinâmicas:
- **Topic Modeling (LDA)**: Agrupamento baseado nas palavras-chave encontradas nos arquivos README.md ou descrições dos projetos.
- **Taxonomia baseada em Tags**: Uso de estruturas hierárquicas extraídas de plataformas comunitárias como o Stack Overflow ou metadados de pacotes (como CodeMeta) para taguear automaticamente os repositórios


### 2.1.3. conforme a camada de abstração 
considerada (arquitetura de código, controle de versão, distribuição de pacotes ou ecossistema de dados).

#### 2.1.3.1. Visão de Controle de Versão e Estrutura de Código (VCS / SCM)

Refere-se à forma como o código-fonte e o histórico do projeto são organizados no sistema de controle de versão (como Git).
- **Monorepo (Monolithic Repository):** Um único repositório contém o código-fonte de múltiplos projetos, serviços ou bibliotecas interdependentes. Facilita o refatoramento atômico e o compartilhamento de código.
- **Polyrepo / Multirepo:** Cada serviço, aplicação ou biblioteca possui seu próprio repositório isolado. Promove forte autonomia entre equipes e deploys independentes.
- **Meta-repository (Monorepo Virtual):** Uso de ferramentas (como Git Submodules ou Google repo) para agrupar múltiplos repositórios distintos em um repositório central unificado.

#### 2.1.3.2. Visão do Padrão de Projeto de Software (Design Patterns & DDD)

Refere-se à camada de persistência e acesso a dados dentro da arquitetura do software (ex.: Clean Architecture, DDD).
- **Repository Pattern (Martin Fowler / DDD):** Uma abstração que simula uma coleção em memória para gerenciar entidades de domínio, isolando a regra de negócio da lógica de banco de dados (SQL, NoSQL, ORM).
    - **Read/Write Repository (CQRS):** Separação clara entre repositórios focados em consulta (_Query_) e repositórios focados em mutação (_Command_).
    - **Generic Repository:** Implementação com métodos reutilizáveis de CRUD para qualquer entidade.

#### 2.1.3.3. Visão do Estilo Arquitetural de Sistemas (Architectural Styles)

A classificação abaixo destaca como componentes do sistema interagem com uma fonte centralizada de dados mantida na memória ou em disco.

![[260916-modelos_semanticos-01.webp]]

- **Blackboard Architecture:** Vários subsistemas especializados (especialistas) trabalham de forma independente e assíncrona sobre um repositório comum (_blackboard_) para resolver um problema complexo gradualmente.
- **Database-Centric / Data-Driven Architecture:** A aplicação é construída em torno de um repositório central de dados permanente, acessado por múltiplos componentes independentes.

#### 2.1.3.4. Visão de Ecossistema e Gestão de Artefatos

Classificação dos repositórios utilizados no ciclo de integração e implantação (CI/CD):
- **Source Code Repository:** GitHub, GitLab, Bitbucket.
- **Artifact / Binary Repository:** Nexus, JFrog Artifactory, Docker Hub. Armazenam artefatos compilados, imagens de contêineres e pacotes prontos para execução.
- **Package Repository:** npm, PyPI, Pub.dev, NuGet. Repositórios públicos ou privados voltados à distribuição de dependências e bibliotecas reutilizáveis.
- **MSR (Mining Software Repositories):** Área da engenharia de software voltada para análise estatística e extração de dados sobre o histórico de comits, _pull requests_ e problemas (_issues_).


## 2.2. Template Unificado (Modelo Mestre)

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


| ID do Conceito | Prefixo / Namespace | Tipo Semântico | ==prefLabel== | Idioma | altLabel | definition | subClassOf | Propriedade Associada | Tipo de Propriedade | Domain | Range | Cardinalidade |
| -------------- | ------------------- | -------------- | ------------- | ------ | -------- | ---------- | ---------- | --------------------- | ------------------- | ------ | ----- | ------------- |
|                |                     |                |               |        |          |            |            |                       |                     |        |       |               |



# 3. OLD mbse_docs

## 3.1. sobre este documento
sistema de documentação para desenvolvimento de software

## 3.2. revisão conceitual 

### 3.2.1. MBSE - Model Based Systems Engineering 
[[260617_conceitos_info_se]]
[[260617_conceitos_info_se#2. SDLC - Software Development Life Cicle]]
[[260617_conceitos_info_se_mbse]]

#### 3.2.1.1. análises de recursos MBSE

| titulo da analise  | hiperlink                                                                                                       | status |
| ------------------ | --------------------------------------------------------------------------------------------------------------- | ------ |
| modelagem          | [[260726_analise_mbse_models_00]]                                                                               |        |
| atributos          | [[260726_analise_mbse_atributos_00]]                                                                            |        |
| tools              | [[260726_analise_mbse_tools_00#1.1. Introdução ao Contexto das Ferramentas MBSE\|260726_analise_mbse_tools_00]] |        |
|                    |                                                                                                                 |        |

legenda:
não iniciado 
iniciado pelo agente 
finalizado pelo agente 
revisado pelo usuário 

## 3.3. o sistema mbse_docs 
##### 3.3.1.1.1. resumo do sistema 

##### 3.3.1.1.2. resumo dos documentos gerenciados pelo sistema 
- mbse_docs
	- inteligencia
		- skd - system knowledge documentation
		- instruções (loops), agents, skills
	- regras mbse: modelagem, arquiteturas, qualidade
	- modelos: templates, instruções
- modelos para um sistema alvo
	- sistema
		- dominio
		- software
			- spec current
				- README.md, prd, srd
	- projeto  = gsd-planning 
		- planejamento 
			- conceituação: Business Case Document, Concept of Operations
			- planos: Work Breakdown Structure, Project Plan (planos de execução)
			- controle: Action Item Status, controle de configuração
		- analise 
			- [[260617_conceitos_info_mbse#6.2.2. Requirements Definition Phase|source models]]: Business Requirements Document, Functional Requirements Document, Software Architecture Plan, Use Case Template, Requirements Inspection Checklist, Requirements Traceability Matrix
			- spec new: PRD
		- projeto
			- Systems Requirements Specifications, Database Design Document, User Interface Design Template, Code Review Checklist
			- spec new: SRD
	- sessão 
		- inteligencia
			- AGENTS.md
			- prompts
		- analises

## 3.4. documentos mbse

### 3.4.1. documentos de inteligencia 
#### 3.4.1.1. skd - system knowledge documentation
como funciona o sistema, instruções para humanos e agentes
#### 3.4.1.2. instruções (loops), agents, skills
##### 3.4.1.2.1. agent: session-planner 

- session-plan-init-investigate  
- session-plan-init-structure 
- session-plan-init-review 
- session-plan-init-publish 
- session-plan-update 
- session-plan-finish 

##### 3.4.1.2.2. agent: project-planner 

- skills 
  - project-prd 
  - project-srd 
  - project-plan-steps  
  - project-plan-map 
  - project-plan-code-map 

##### 3.4.1.2.3. agent: code-planner 

##### 3.4.1.2.4. agent: code-reviewer 

- input prompt  
  - contexto 
    - project_title: 
    - project_absolute_path: 
    - stack 
    - seção do projeto 
  - caminhos dos documentos, relativos ao {project_absolute_path} 
    - code_folder: 
    - code_target_files 
    - code_map: 
    - srd: seções [descrições, tag system] 
    - session_code_blocks: 
    - session_code_blocks_sections: [] 
    - requested_report: 
  - instruções 
- agent rules 
  - permissions: ~~skills~~, tools 
  - var paths map `{placeholders}` 
  - fix paths map 
    - output template 
    - skills 
    - aux files: json 
    - regras para chamar skills 
  - workflow 
    - ler 
    - executar 
    - salvar requested report, versionamento 
- skills 
  - code-spec-compliance 
    - paths map: srd [descrições, tag system] 
    - rules: conformidade com descrições, checklist 
  - code-quality 
    - paths map: code control map, code files, srd [tag system] 
    - rules: hierarquia, nomenclatura, complexidade 




### 3.4.2. documentos de regras mbse
regras aplicáveis de:
- modelagem 
- arquitetura, design patterns
- rastreabilidade, gerenciamento
- qualidade

#### 3.4.2.1. regras gerais

##### 3.4.2.1.1. formatação 
##### 3.4.2.1.2. Legenda de Tags

###### 3.4.2.1.2.1. versao atual

| Tag   | Significado                                                     | Regra de consistência                                                                                           |
| ----- | --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `[1]` | **Novo** — classe/método que será criado                        | Deve existir em `classe nova` com `metodo novo` preenchido                                                      |
| `[2]` | **Refatorar** — método existente que muda de script/classe/nome | `script novo` e `classe nova` devem refletir o destino final. `metodo novo` opcional se só mudar de classe      |
| `[3]` | **Manter** — fica como está, sem alteração                      | `script novo` = `script atual`. `classe nova` = `subsection atual` (se aplicável). `metodo novo` = `item atual` |
| `[4]` | **Descartar** — será removido                                   | `script novo` e `classe nova` vazios. Nenhuma referência no novo código                                         |

###### 3.4.2.1.2.2. versao nova

| Tag     | Significado base                                                | Significado complementar (com base no status da especificação tecnica)                      |
| ------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `[1.0]` | **Novo** — classe/método que será criado                        | testado                                                                                     |
| `[1.1]` | **Novo** — classe/método que será criado                        | implementado                                                                                |
| `[1.2]` | **Novo** — classe/método que será criado                        | code block (dart ou markdown) validado pelo usuario                                         |
| `[1.3]` | **Novo** — classe/método que será criado                        | code block (dart ou markdown) criado                                                        |
| `[1.4]` | **Novo** — classe/método que será criado                        | descrição inicial (csv ou markdown) alinhada com "logica de responsabilidades e requisitos" |
| `[2.0]` | **Refatorar** — método existente que muda de script/classe/nome | testado                                                                                     |
| `[2.1]` | **Refatorar** — método existente que muda de script/classe/nome | implementado                                                                                |
| `[2.2]` | **Refatorar** — método existente que muda de script/classe/nome | code block (dart ou markdown) validado pelo usuario                                         |
| `[2.3]` | **Refatorar** — método existente que muda de script/classe/nome | code block (dart ou markdown) criado                                                        |
| `[2.4]` | **Refatorar** — método existente que muda de script/classe/nome | descrição inicial (csv ou markdown) alinhada com "logica de responsabilidades e requisitos" |
| `[3.0]` | **Manter** — fica como está, sem alteração                      | —                                                                                           |
| `[4.0]` | **Descartar** — será removido                                   | —                                                                                           |

observações: 
- será necessario atualizar as atuais classificações da tabela csv (versao nova)
- itens classificados como [3.0] onde seja indentificada pendencia devem ser reclassificados para [2.2]
- descrição inicial (csv ou markdown) = nome do metodos + [descrição no csv OU descrição complementar no md (se necessario)]

##### 3.4.2.1.3. instruções de Consistência

###### 3.4.2.1.3.1. Verificação Cruzada

Para verificar a tabela CSV, aplicar estas instruções:

| #   | Regra                                                                                                                    | Como verificar                                          |
| --- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------- |
| 1   | Todo `[1]` novo deve ter `classe nova` e `metodo novo` preenchidos                                                       | Filtrar tag=`[1]`, checar se campos não vazios          |
| 2   | Todo `[2]` refatorar deve ter `script novo` diferente do `script atual` OU `classe nova` diferente de `subsection atual` | Filtrar tag=`[2]`, checar se pelo menos um campo difere |
| 3   | Todo `[3]` manter deve ter `script novo` = `script atual`                                                                | Filtrar tag=`[3]`, checar igualdade                     |
| 4   | Todo `[4]` descartar deve ter `script novo` e `classe nova` vazios                                                       | Filtrar tag=`[4]`, checar campos vazios                 |
| 5   | `metodo novo` deve ser único dentro de cada `classe nova`                                                                | Agrupar por classe nova, checar duplicatas              |
| 6   | Nenhum `metodo novo` deve ter nome de classe reservada (`class`)                                                         | Checar se "class" aparece como nome de método           |

###### 3.4.2.1.3.2. Verificação de Pipeline

| Etapa | Entrada               | Classe             | Saída                   |
| ----- | --------------------- | ------------------ | ----------------------- |
| 1     | Diretório de assets   | `BuildAssets`      | `List<AssetsContent>`   |
| 2     | `List<AssetsContent>` | `BuildPostConfig`  | `List<Map post_config>` |
| 3     | `Map post_config`     | `BuildPostContent` | `Map post_content`      |
| 4     | `Map post_content`    | `BuildPayload`     | `PostContent` (Dart)    |

Cada classe recebe o que a anterior produziu — sem saltos, sem dependências circulares.

###### 3.4.2.1.3.3. O que será eliminado

| Arquivo                                           | Destino                                                                                                   |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `src/scripts/post_builder.dart`                   | Eliminado (imports migrados)                                                                              |
| `src/scripts/publish/post_builder_facebook.dart`  | Métodos `resolveContent` e `_textFrom` movidos; `fillPostContentTextFields` e `_textFieldFor` descartados |
| `src/scripts/publish/post_builder_instagram.dart` | `resolveContent` movido; `fillPostContentFields` descartado                                               |

##### 3.4.2.1.4. regras de arquitetura, design patterns, qualidade de codigo

#### 3.4.2.2. project documents rules  
- general rules: 
	- naming 
	- versioning 
	- mirroring [md, json, toml, csv, xlsx]  
- spec docs  
- plan docs  
	- plan & control rules: tag system    
- script docs  
	- build rules
		- metodos
			- factory para boco de dados 
				- Factory: recebe parâmetros tipados nomeados e cria um Map novo — assetsEntry(fileName: x, timestamp: y) => {'fileName': x, 'timestamp': y}.
			- transformador para alimentar o bloco 
				- Transformador: recebe um Map pronto, extrai com casts, transforma em outro Map — _toConfigMap(entry) { final x = entry['fileName'] as String; ... return {...} }.
	- review rules: spec, quality  


### 3.4.3. formas de aplicação 
#### 3.4.3.1. aplicação manual
#### 3.4.3.2. aplicação automatica

##### 3.4.3.2.1. PRD

| doc\ modelos             | template | herança | instruções gerais | instruções especificas |
| ------------------------ | :------: | :-----: | :---------------: | :--------------------: |
| PRD                      |          |         |                   |                        |
| PRD sobre este documento |          |    x    |                   |                        |
| PRD contexto do projeto  |    x     |         |                   |                        |
| PRD logica funcional     |    x     |         |                   |                        |
| PRD funções de negócio   |    x     |         |                   |                        |
| PRD modelos de dados     |    x     |         |                   |                        |

##### 3.4.3.2.2. SRD

| documento, seção \ modelos                                                        | template | herança | instruções gerais | instruções especificas |
| --------------------------------------------------------------------------------- | :------: | :-----: | :---------------: | :--------------------: |
| SRD                                                                               |          |         |                   |                        |
| SRD sobre este documento                                                          |          |    x    |                   |                        |
| SRD arquitetura de funções                                                        |          |         |                   |                        |
| SRD arquitetura de funções, instruções e resumo                                   |          |         |                   |                        |
| SRD arquitetura de funções, instruções e resumo, instruções                       |          |    x    |                   |                        |
| SRD arquitetura de funções, instruções e resumo, resumo                           |    x     |         |                   |                        |
| SRD arquitetura de funções, funções de negócio                                    |          |    x    |                   |                        |
| SRD arquitetura de funções, funções de automação                                  |          |    x    |                   |                        |
| SRD arquitetura de funções, funções de automação, instruções e resumo             |          |         |                   |                        |
| SRD arquitetura de funções, funções de automação, instruções e resumo, instruções |          |    x    |                   |                        |
| SRD arquitetura de funções, funções de automação, instruções e resumo, resumo     |    x     |         |                   |                        |
| SRD arquitetura de funções, funções de automação, script `script_name`            |    x     |         |                   |                        |
| SRD arquitetura de funções, funções de automação, script, classe `class_name`     |    x     |         |                   |                        |
| SRD arquitetura de dados                                                          |    x     |         |                   |                        |
| SRD arquitetura de dados, instruções e resumo                                     |          |         |                   |                        |
| SRD arquitetura de dados, instruções e resumo, instruções                         |          |    x    |                   |                        |
| SRD arquitetura de dados, instruções e resumo, resumo                             |    x     |         |                   |                        |
| SRD descrições funcionais                                                         |    x     |         |                   |                        |

como os modelos são aplicados nos documentos:
- templates: formatos fixos, conteudo editável com base nas instruções gerais ou especificas
- herança: conteúdo não editáve, herdado de outro documento
- instruções*: conteúdo não editável# 5. documentos de sistema
#### 3.4.3.3. aplicação agêntica

## 3.5. documentos de sistema 
## 3.6. documentos de projeto 

### 3.6.1. documentos de planejamento 
#### 3.6.1.1. planos de execução 

- plano integral: etapas 
- plano etapa, todo 
- control maps 
  - plan map 
  - **code map**: [files, classes, métodos] x [funções negócio] = tags [pendencia, maturidade] 
    - pendencia: [novo, refatorar, manter, eliminar] 
    - maturidade: [descrições, code block, quality, test] 
  - **data process map**: [files, classes, métodos] x [data blocks] = tags [pendencia, maturidade] 

### 3.6.2. documentos de analise 
#### 3.6.2.1. alguns conceitos

##### 3.6.2.1.1. Matriz de Amarrações Operacionais (Sem Tecnologia/Classes)
###### 3.6.2.1.1.1. É um Diagrama de Definição de Blocos (BDD)?

A Matriz de Amarrações Operacionais em formato visual/conceitual aproxima-se de uma junção de:

1. **Internal Block Diagram (IBD) / Allocation Matrix:** Mostra os fluxos de informação passando entre subsistemas/camadas.
2. **Tabular Allocation View:** A OMG/SysML prevê matrizes de alocação (_Allocation Tables_) para mapear atividades para blocos lógicos ou para mapear funções entre camadas.

###### 3.6.2.1.1.2. Reformulação da Matriz no Formato Tabela por Camadas (Sua Sugestão)

Formatá-la em tabela com **referência ao pipeline** e **uma coluna por camada** deixa a rastreabilidade direta e clara:

  

###### 3.6.2.1.1.3. Exemplo de Matriz Tabular Operacional do `crm-cdd`:

| **Ref. Pipeline** | **Ref. Funcionalidade** | **Camada Operacional (Entrada / Interface)** | **Camada de Transformação (Regras de Negócio / Processamento)** | **Camada de Saída (Persistência / Notificação / Entrega)** |
| ----------------- | ----------------------- | -------------------------------------------- | --------------------------------------------------------------- | ---------------------------------------------------------- |
| **Passo 01**      | `[FN-2.1]`              | Captura dados do formulário de opt-in        | Valida duplicação de lead e calcula score inicial               | Registra novo lead no repositório de contatos              |
| **Passo 02**      | `[FN-2.3]`              | Recebe confirmação de abertura de e-mail     | Aplica regra de automação de fluxo de nutrição                  | Agenda próximo envio no canal do usuário                   |
| **Passo 03**      | `[FN-3.1]`              | Recebe webhook de checkout aprovado          | Transfere status do cliente e libera licença                    | Emite comprovante e envia acesso ao produto                |


##### 3.6.2.1.2. Requisitos de Regra e Exceções do Pipeline
###### 3.6.2.1.2.1. Referenciando cada Funcionalidade do Pipeline nos Requisitos

Na especificação formal do SysML (`Requirements Diagram` / `ISO 29148`), cada requisito deve ter uma relação explícita de rastreabilidade (estereótipos `«trace»` ou `«satisfy»`) apontando para a funcionalidade correspondente.

  

###### 3.6.2.1.2.2. Ajuste no Template de Requisitos para o `crm-cdd`:

Markdown

```
##### 4. Requisitos de Regra e Exceções do Pipeline

###### Regras de Negócio (RN)
* **[RN-01] [Ref: FN-2.1]:** O e-mail do lead deve ser validado via sintaxe e verificação de domínio antes do cadastro.
* **[RN-02] [Ref: FN-2.2]:** A pontuação de lead (*Lead Scoring*) deve ser recalculada a cada ação de clique em links monitorados.
* **[RN-03] [Ref: FN-3.1]:** A liberação de acesso ao produto digital deve ocorrer em no máximo 30 segundos após a confirmação do webhook de pagamento.

###### Tratameno de Exceções (EX)
* **[EX-01] [Ref: FN-2.1] Lead Duplicado:** Caso o e-mail já exista na base, o sistema deve fundir (*merge*) os dados e atualizar o histórico de interações sem criar um novo registro.
* **[EX-02] [Ref: FN-3.1] Falha no Webhook:** Se o gateway de pagamento não responder em 3 tentativas, o pipeline deve mover a transação para a fila de reconciliação manual e alertar o administrador.
```





#### 3.6.2.2. [[01-BRD-Business_Requirements_Document|BRD - Business_Requirements_Document]]
from ex-PRD

#### 3.6.2.3. [[02-FRD-Functional_Requirements_Document|FRD - Functional Requirements Document]] 
from ex-PRD
#### 3.6.2.4. Use Case Template

##### 3.6.2.4.1. Matriz de Amarrações Operacionais (Sem Tecnologia/Classes)

###### 3.6.2.4.1.1. Conceitos MBSE Envolvidos

- **Decomposição Funcional e Camadas (_Functional Layering / Abstraction Layers_):** Organização das responsabilidades operacionais em camadas (Interface, Transformação e Saída) sem associação com arquitetura de software (ex: MVC, Microserviços).
- **Alocação de Responsabilidade Operacional (_Operational Allocation_):** Estabelecimento das dependências e do fluxo de informações (_Data/Control Flows_) entre as camadas lógicas operacionais.

###### 3.6.2.4.1.2. Referências Normativas e Padrões

- **OMG SysML v1.7 (Capítulo 7 - Block Definition Diagrams & Structuring):** Definição da hierarquia lógica do sistema e decomposição do bloco do sistema em subsistemas funcionais abstratos.
- **OMG SysML v1.7 (Capítulo 15 - Allocation):** Conceito da relação `«allocate»`, usada para rastrear como capacidades/atividades de alto nível se conectam com as camadas lógicas de processamento antes de atingirem componentes físicos.


#### 3.6.2.5. Software Architecture Plan (from ex-PRD)
- stack 
	- scripts: dart, python, ps1, sqlite, api  
	- UI: flutter, web, shell 

#### 3.6.2.6. Requirements Traceability Matrix
#### 3.6.2.7. Requirements Inspection Checklist

### 3.6.3. documentos de design
#### 3.6.3.1. srd 
  
- arquitetura de funções 
  - tipo: [negócio, automação] 
  - funções de automação (implementação)
   - arquitetura, folders, files 
     - classes, métodos, objetos 
- arquitetura de dados 
  - tipo: [ambiente, config, auth, state, script flow, negócio]
  - dados de negócio 
  - documentos, schemas, tabelas 
    - objetos, campos 
- blocos do modelo de dados  
	- post type: [platform, content_type, media_type]
	- texto: campos detalhados abaixo
	- media: [image_path, video_path]
	- schedule: [published, scheduled_publish_time]
- descrições funcionais (responsabilidades, lógicas, requisitos, restrições) 
	- tipo [coordenação de processo, execução de processo, processamento de dados]
	- descrições interfuncionais (coordenação, invocação)
	- descrições intrafuncionais (execução, implementação)
		- responsabilidades comuns 
			- etapas em serie, onde cada etapa
			- busca os dados na fonte (input)
			- executa as tranformações necessarias
			- constroi o mapa de dados para a proxima etapa (output)
	- processamento de dados (data block, input, transformação, output)
      - BuildAssets 
        - input: diretório de assets no disco 
        - transformações: scan pastas `{platform}.{content_type}`, parse timestamp + frontmatter + body, classificar por tipo (textOnly/textWithMedia/mediaOnly) 
        - output: `List<AssetsContent>` (AssetsContent = agrupamento por pasta + List.AssetsEntry) 
        - data blocks processados: 
          - post type: platform, content_type inferidos da pasta; media_type inferido da extensão 
          - texto: frontmatter.title + .md body 
          - media: image_path / video_path resolvidos via media_file do frontmatter 
          - schedule: timestamp extraído do nome do arquivo 
      - BuildPostConfig 
        - input: `List<AssetsContent>`
        - transformações: mapear AssetsContent.Content → Map post_config (fromAssetsContent), resolver campos de texto (titleFrom + bodyFrom + defaultTextForType), formatar schedule
        - output: `List<Map post_config>` no schema definido
        - data blocks processados:
          - post type: platform, content_type, media_type (copia direta)
          - texto: text_values.title + text_values.body (de AssetsContent ou fallback defaultTextForType)
          - media: image_path, video_path (resolvidos do AssetsContent)
          - schedule: published (bool), scheduled_publish_time (ISO8601 ou null)
      - BuildPostContent 
        - input: `Map post_config` (um post)
        - transformações: copiar fields fixos (platform, content_type, media_type, published, scheduled_publish_time, retry_config), copiar paths (image_path, video_path), resolver texto no field correto (postType.textField = message / caption / description)
        - output: `Map post_content`
        - data blocks processados:
          - post type: platform, content_type, media_type (copia direta)
          - texto: title (de text_values.title) + body no textField correto (de text_values.body)
          - media: image_path, video_path (copia direta)
          - schedule: published, scheduled_publish_time (copia direta)
      - BuildPayload 
        - input: `Map post_content`
        - transformações: construir objeto PostContent Dart (TextContent / ImageContent / VideoContent) com base em media_type + campos preenchidos, validar existência dos paths
        - output: `PostContent`
        - data blocks processados:
          - post type: endpoint, uploadFlow (via PostType)
          - texto: extrair do textField correto (caption / description / message)
          - media: validar image_path / video_path no disco 
          - schedule: passed through via PostType.decorate 
- logic maps 
	- [arquitetura funções] x [arquitetura funções] = [descrições]
	- [arquitetura funções] x [arquitetura dados] = [descrições]

#### 3.6.3.2. srd session code blocks 

- resumo do srd: selected logic map maps review rules   
- resumo do control map + tag system 
- selected code blocks 

#### 3.6.3.3. code, code-review, test 

## 3.7. documentos de sessão 

### 3.7.1. inteligencia 
#### 3.7.1.1. session: AGENTS.md 

- objetivo, contexto [prd], entregas 
- referencias: agents 
### 3.7.2. analises 

## 3.8. casos de uso 

[[260807_sist_crm_00]]

# 4. ontologia para dominio harness engineering

- memoria
- janela de contexto
- 
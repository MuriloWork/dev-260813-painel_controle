# 1. Escopo do MBSE
1. **O que exatamente o sistema MBSE deve modelar?** USUARIO: apenas software
2. Qual é o **objeto central** que está sendo desenvolvido/especificado?
	- USUARIO 
		- Genericamente pode ser entendido como `Sistema → Subsistemas → Componentes → Elementos` mas é fundamental o entendimento de que o KB - knowledge bundle - do MBSE deve ser configurado para viabilizar o desenvolvimento de softwares particulares de alta qualidade e alto determinismo, usando orquestração de recursos combinados de códigos de programação, sistemas harness, agentes de IA e coordenação humana.
		- software particular 
		- qualidade 
		- determinismo 
		- recursos combinados orquestração 
3. O MBSE deve representar apenas o **produto/sistema**, ou também o **processo de desenvolvimento** desse produto? USUARIO: aqui temos uma situação um pouco mais complexa, pois o KB do MBSE deve conter a inteligência para todo o SDLC - Software Development Life Cicle - de qualquer software, inclusive dele próprio 
	- inteligência, memória, trilhas de raciocínio, regras de decisão, aprendizado 
4. O modelo deve representar somente o **estado desejado/final** do sistema ou também decisões, alternativas, versões, estados de evolução etc.? USUARIO: no momento vamos nos concentrar apenas no conhecimento necessário para criação, manutenção e aplicação das modelagens necessárias para criação de softwares particulares 

# 2. O que constitui conhecimento no sistema
Imagine que alguém pergunte:
> “Quais são as coisas que eu preciso registrar para especificar completamente este sistema?”
Quais categorias você imagina?
Por exemplo, sem assumir que sejam as suas:
- requisitos;
- funcionalidades;
- atores;
- casos de uso;
- componentes;
- interfaces;
- dados;
- comportamentos;
- estados;
- restrições;
- decisões;
- parâmetros;
- ambientes;
- riscos;
- testes;
- documentos;
- fontes.
**Quais dessas pertencem ao seu MBSE? Quais você acrescentaria?**

# 3. Requisitos
5. Um **requisito** no seu MBSE é uma coisa diferente de uma funcionalidade?
Por exemplo:
> Requisito: “O sistema deve permitir autenticação.”
> Funcionalidade: “Autenticar usuário.”
Ou você pretende que funcionalidade seja apenas uma forma de requisito?
6. Um requisito pode estar relacionado a:
- outro requisito;
- funcionalidade;
- componente;
- interface;
- teste;
- decisão?
7. Você pretende rastrear a cadeia:
> **Necessidade → Requisito → Solução → Implementação → Verificação**
ou uma cadeia diferente?

# 4. Estrutura e arquitetura
8. Quais elementos estruturais você considera fundamentais?
Por exemplo:
> Sistema  
> → subsistema  
> → componente  
> → módulo  
> → classe
Mas talvez, no seu modelo:
> Sistema → domínio → contexto → componente → objeto
Qual seria a estrutura que você imagina?
9. **Componente** e **classe** são conceitos diferentes no MBSE?
10. **Interface** é uma entidade independente do componente ou apenas uma propriedade/relação entre componentes?
11. O modelo precisa representar explicitamente:
> “A depende de B”
> “A contém B”
> “A implementa B”
> “A especializa B”
> “A fornece serviço para B”
?

# 5. Comportamento
12. Como você pretende representar comportamento?
Por exemplo:
- caso de uso;
- atividade;
- processo;
- operação;
- estado;
- transição;
- evento;
- regra de negócio.
13. Existe uma distinção importante entre:
> **o que o sistema faz**
e
> **como o sistema faz**?
Se sim, onde você colocaria essa fronteira?

# 6. Domínio e significado
14. O MBSE precisa possuir um **modelo de domínio** independente da arquitetura?
Por exemplo:
> Cliente  
> Pedido  
> Produto  
> Contrato
seriam conceitos do domínio, enquanto:
> CustomerRepository  
> OrderService  
> PostgreSQL
seriam elementos da solução.
15. Essa distinção entre **domínio do problema** e **solução** é importante para o sistema que você está imaginando?
Essa pergunta é particularmente importante para o nosso futuro `type`.

# 7. Decisões e justificativas
16. O sistema deve registrar **decisões de engenharia**?
Por exemplo:
> Decisão: utilizar PostgreSQL.
17. Se sim, uma decisão deveria poder registrar:
> decisão → alternativas consideradas → justificativa → consequência → elementos afetados
?
18. Uma decisão é conhecimento do mesmo nível que um requisito/componente, ou pertence a uma camada diferente da especificação?

# 8. Relações
Aqui eu gostaria que você pensasse menos em UML e mais no **grafo de conhecimento**.
19. Quais relações você considera fundamentais?
Por exemplo:
- `contains`
- `part_of`
- `depends_on`
- `implements`
- `satisfies`
- `refines`
- `specializes`
- `uses`
- `realizes`
- `verifies`
- `derived_from`
- `constrains`
- `related_to`
Não precisamos escolher os nomes ainda. O importante é descobrir **quais relações existem semanticamente**.
20. Você imagina que praticamente tudo no MBSE possa ser representado como:
> **Elemento + propriedades + relações**
?
Se a resposta for sim, isso será uma decisão arquitetural/conceitual muito importante para o nosso modelo.

# 9. Ciclo de vida
21. Os elementos do MBSE precisam possuir estado?
Por exemplo:
> proposed → draft → approved → implemented → verified → deprecated
Ou o ciclo de vida pertence apenas a determinados elementos?
22. Uma alteração em um elemento deve permitir descobrir **quais outros elementos podem ter sido afetados**?

# 10. A pergunta mais importante
Por fim, eu faria esta pergunta antes de qualquer configuração:
> **Se amanhã tivéssemos que construir um MBSE genérico do zero, quais seriam as 10–20 entidades que você consideraria indispensáveis para representar um sistema de forma suficientemente completa?**
Não precisa pensar em OKF, Frontmatter, `type`, Markdown ou MBCG agora.
Quero que primeiro construamos algo como:
```text
                    SISTEMA
                       │
       ┌───────────────┼───────────────┐
       │               │               │
   Requisitos      Estrutura      Comportamento
       │               │               │
       │               │               │
   ...             ...             ...
```
Depois fazemos a segunda camada:
```text
MBSE
 ├── entidades
 ├── propriedades
 ├── relações
 ├── estados
 ├── fontes
 └── rastreabilidade
```
E **só depois** fazemos a transformação:
```text
MBSE genérico
      ↓
Concepts
      ↓
type
      ↓
Frontmatter
      ↓
regras
      ↓
valores admissíveis
```
Essa sequência evita exatamente o problema que encontramos agora: tentar definir a configuração do documento **antes de termos definido o domínio que o documento precisa representar**.
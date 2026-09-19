# 1. O Sistema MB-SDD

MB-SDD - Model Based Spec Driven Development - será um sistema de gerenciamento de especificações de software baseadas em modelos OMG

Diferente de abordagens tradicionais baseadas em documentos de texto estáticos, o MB-SDD atuará como um editor e gerenciador de especificações executáveis de software. Ele permitirá capturar requisitos, arquitetura de software, componentes, fluxos de dados e regras de negócio diretamente em modelos semânticos estruturados (UML, SysML, RAAML).

Principais Objetivos do Sistema
* **Modelagem Semântica Unificada**: Permitir a criação e edição gráfica e textual de diagramas de estrutura, comportamento e requisitos.
* **Manutenibilidade e Rastreabilidade**: Garantir o rastreamento bidirecional entre requisitos de software, elementos de arquitetura, restrições de negócio e código-fonte.
* **Independência de Plataforma** (MDA): Separar a especificação conceitual do sistema (CIM/PIM) das implementações de tecnologia específicas (PSM).
* **Interoperabilidade**: Consumir e exportar dados nos padrões XMI, JSON Schema e conectores de código-fonte.

# 2. pipeline 
- seleção de documentos 
	- janela windows multi arquivos 
	- painel de arquivos selecionados 
- gestao de documentos 
	- schemas dinâmicos 
		- documentos selecionados md ⟶ json schema 
	- versionamento sob demanda 
		- yyyy 
	- merge 
		- status
		- blocks 
	- mindmap multi docs 
		- hierarquia: headings, listas 
# 3. arquiteturas 

## 3.1. arquitetura de dados 

### 3.1.1. documentos 

- modelo geral  
	- TOC + status
	- conteúdo: headings, blocks (lista, tabela, outros)
- modelos específicos por tipo
	- agents 
	- spec 
	- gsd-planning 
	- sessions 
		- okf docs
			- master doc
				- indice children docs
			- child doc 
				- status 
				- indice children docs


# 1. sobre este documento

## 1.1. resumo e objetivos 

Este documento coordena um processo de pesquisa, estudo e análise de temas ligados abrangente título **MBSE** (Model Based Software Engineering). 

O estudo da MBSE tem por objetivo construir um amplo mapa mental sobre o tema, composto por arquivos markdown, suas seções e conteúdos, bem como links e outros conteúdos complementares. O **mapa mental**, dinamicamente construído durante as análises, deverá guiar o aprendizado e desenvolvimento profissional do usuário nos temas, e também no mapeamento, entendimento e priorização de todos os componentes e atributos necessários para suportar o desenvolvimento de **melhorias na sistematização do ciclo de desenvolvimento de software** (SDLC - Software Development Life Cicle) feito pelo usuário em projetos pessoais. Por melhorias de sistematização entende-se quaisquer dos seguintes tipos de iniciativa:
- padronização de procedimentos e/ou templates
- uso de ferramentas e/ou métodos existentes 
- pequenas aplicações que facilitem qualquer etapa do SDLC, principalmente as etapas de análise e projeto
- integrações com ferramentas de modelagem existentes

O espírito desta análise sobre a MBSE é buscar os objetivos de forma prática, sem inventar a roda, aproveitando ao máximo o vasto conhecimento disponível em normas, literatura e ferramentas existentes, tendo como principais conceitos adotados:
- DDD - Domain Driven Design de Eric Evans
- MDA - Model Driven Architecture da OMG

## 1.2. instruções
- o título de cada subseção do plano de execução segue o template {analise: titulo da analise} 
- a análise dos assuntos de cada subseção deve ser executada conforme a seguinte sequência: 
	- buscar a versão mais recente do documento <file_name_template>
	- se existir, ler a versão mais recente do documento 
	- senão 
- abaixo corresponde a uma etapa de execução unitária, que deve ser validada pelo usuário antes da etapa seguinte, e tem um documento para edição de seus resultados 
- em cada subseção existe uma lista de assuntos para pesquisa e analise  
- para cada assunto_da_lista
	- buscar na web as fontes e conteúdos mais relevantes 
	- no documento <file_name_template>, abaixo da seção "pesquisas" adicionar/revisar subseção <assunto_da_lista> com as subseções [resumo da pesquisa, fontes pesquisadas, atributos recomendados,  melhorias de sistematização recomendadas]
	- solicitar validação do usuário 

## 1.3. plano de execução

- definir atributos de avaliação de qualidade de software  
- definir atributos de eficiência de desenvolvimento de software 
- mapear todos os atributos dos modelos definidos pela OMG (Object Management Group) para construção da MDA (Model Driven Architecture)
- analisar a relação entre os modelos da MDA e os atributos de qualidade e eficiência do desenvolvimento de software 

### 1.3.1. revisao conceitual

file_name_template: 260617_conceitos_info_mbse
lista de assuntos para pesquisa:

### 1.3.2. modelagem 
- normas e modelos existentes no mercado
- modelagem de arquitetura e de dados 
- mapear modelos utilizados em geração e inspeção de código fonte de software 
- mapear todos os atributos dos modelos definidos pela OMG (Object Management Group) para construção da MDA (Model Driven Architecture)
- analisar a relação entre os modelos da MDA e os atributos de qualidade e eficiência do desenvolvimento de software 

### 1.3.3. Atributos de Qualidade e Eficiência

- definir atributos de avaliação de qualidade de software  
- definir atributos de eficiência de desenvolvimento de software 

| Etapa                          | Objetivo                                                                                                       | Ações principais                                                                           | Entregável esperado                    |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | -------------------------------------- |
| 1. Mapeamento de normas OMG    | Identificar todas as especificações relevantes (MOF, QVT, UML, SBVR, SPEM…)                                    | • Listar documentos OMG → PDF/HTML <br>• Compilar glosários de termos                      | *Checklist de normas*                  |
| 2. Definição de atributos      | Estabelecer atributos de qualidade (rastreabilidade, consistência) e de eficiência (tempo de ciclo, automação) | • Criação de catálogo de atributos <br>• Vincular cada atributo a uma norma/metamodelo     | *Catálogo de atributos*                |
| 3. Mapeamento MDA → Atributos  | Construir matriz em que cada norma/modelo (CIM/PIM/PSM) encontra os atributos relevantes                       | • Colunas: normas; linhas: atributos; células: presença/grade<br>• Notação de dependências | *Matriz de mapeamento*                 |
| 4. Análise de adequação ao SDD | Verificar se o modelo determinístico de SDD se sustenta na matriz                                              | • Identificar lacunas <br>• Recomendar práticas de modelagem (ex.: variáveis, refinamento) | *Relatório de adequação*               |
| 5. Documentação                | Produzir a *Matriz de mapeamento atributos* (relatório tsv/markdown)                                           | • Exportar tabela <br>• Incluir notas de insight                                           | `matriz_mda_atributos.md` (ou `.xlsx`) |

# 2. mapa de análises 

[[260726_analise_mbse_tools_00#1.1. Introdução ao Contexto das Ferramentas MBSE]] 

| titulo da analise  | hiperlink                            | status |
| ------------------ | ------------------------------------ | ------ |
| revisão conceitual | [[260617_conceitos_info_mbse]]       |        |
| modelagem          | [[260726_analise_mbse_models_00]]    |        |
| atributos          | [[260726_analise_mbse_atributos_00]] |        |
| tools              | [[260726_analise_mbse_tools_00]]     |        |
|                    |                                      |        |

legenda:
não iniciado 
iniciado pelo agente 
finalizado pelo agente 
revisado pelo usuário 
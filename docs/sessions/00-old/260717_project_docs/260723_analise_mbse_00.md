# 1. objetivos 

analisar as características da MBSE (Model Based Software Engineering) e MDA (Model Driven Architecture) como base para um modelo predominantemente determinístico de SDD (Spec Driven Development)

# 2. metodo de análise 

- definir atributos de avaliação de qualidade de software  
- definir atributos de eficiência de desenvolvimento de software 
- mapear todos os atributos dos modelos definidos pela OMG (Object Management Group) para construção da MDA (Model Driven Architecture)
- analisar a relação entre os modelos da MDA e os atributos de qualidade e eficiência do desenvolvimento de software 

# 3. plano de execução

| Etapa | Objetivo | Ações principais | Entregável esperado |
|-------|----------|------------------|----------------------|
| 1. Mapeamento de normas OMG | Identificar todas as especificações relevantes (MOF, QVT, UML, SBVR, SPEM…) | • Listar documentos OMG → PDF/HTML <br>• Compilar glosários de termos | *Checklist de normas* |
| 2. Definição de atributos | Estabelecer atributos de qualidade (rastreabilidade, consistência) e de eficiência (tempo de ciclo, automação) | • Criação de catálogo de atributos <br>• Vincular cada atributo a uma norma/metamodelo | *Catálogo de atributos* |
| 3. Mapeamento MDA → Atributos | Construir matriz em que cada norma/modelo (CIM/PIM/PSM) encontra os atributos relevantes | • Colunas: normas; linhas: atributos; células: presença/grade<br>• Notação de dependências | *Matriz de mapeamento* |
| 4. Análise de adequação ao SDD | Verificar se o modelo determinístico de SDD se sustenta na matriz | • Identificar lacunas <br>• Recomendar práticas de modelagem (ex.: variáveis, refinamento) | *Relatório de adequação* |
| 5. Documentação | Produzir a *Matriz de mapeamento atributos* (relatório tsv/markdown) | • Exportar tabela <br>• Incluir notas de insight | `matriz_mda_atributos.md` (ou `.xlsx`) |


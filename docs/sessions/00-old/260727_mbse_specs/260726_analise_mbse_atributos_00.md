**Atributos de Qualidade e Eficiência para MBSE/MDA → SDD**

# 1. Atributos de Qualidade de Software (ISO/IEC 25010)

- definir atributos de avaliação de qualidade de software  
- definir atributos de eficiência de desenvolvimento de software 

Referências:
- [Understanding ISO/IEC 25010](https://medium.com/@oczz/understanding-iso-iec-25010-a-comprehensive-framework-for-software-quality-evaluation-ae3cc5250057)
- [Sonar - ISO/IEC 25010 explained](https://www.sonarsource.com/resources/library/iso-iec-25010-explained/)
atributos faltantes: 
- [architecture, data] model completeness
- model quality cfe normas OMG
- aderência aos modelos [arquitetura, dados] 
 
| Atributo,  sub‑atributo                                 | Descrição e Relevância para MBSE/MDA                                                                                                                                           | Procedimento determinístico de avaliação                                                                                          |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| Functional Suitability, Functional completeness         | [25010] Cobertura dos requisitos definidos na especificação.                                                                                                                   | Contar requisitos especificados vs. elementos de modelo correspondentes. Aprova se cobertura ≥ 95%.                               |
| Functional Suitability, Functional correctness          | [original] Conformidade com a semântica dos modelos. Vital para validar que as transformações PIM→PSM preservam significado [25010] producing accurate and expected results    | [original] Executar bateria de testes OCL sobre o modelo pós‑transformação. Aprova se 100% das restrições forem satisfeitas.      |
| Functional Suitability, Functional appropriateness      | [25010] Grau com que os modelos permitem que usuários atinjam seus objetivos de forma eficiente. Garante que os modelos MDA reflitam corretamente as necessidades dos usuários | Simular cenários de uso com o modelo e verificar se cada objetivo funcional pode ser concluído sem desvios.                       |
| Maintainability, Modularity                             | [25010] Grau de acoplamento entre sub‑modelos. Impacta diretamente na reutilização de artefatos MDA                                                                            | Medir acoplamento (fan‑in/fan‑out) entre pacotes do modelo. Aprova se acoplamento médio ≤ 0,5.                                    |
| Maintainability, Analyzability                          | [25010] Facilidade de identificar impactos de mudanças nos modelos. Ajuda a estimar esforço de manutenção pós‑geração                                                          | Executar análise de dependência entre elementos do modelo. Aprova se o grafo de dependências tiver profundidade ≤ 3 níveis.       |
| Maintainability, Reusability                            | [25010] Capacidade de reutilizar componentes de modelo em diferentes contextos. Reduz esforço de modelagem em novos projetos                                                   | Contar componentes marcados como reutilizáveis vs. total. Aprova se taxa ≥ 20%.                                                   |
| Maintainability, Modifiability                          | [25010] Facilidade de alterar modelos sem impactar outras partes. Essencial para evolução iterativa dos modelos                                                                | Medir tempo médio para incorporar uma alteração de requisito. Aprova se ≤ 2h para alterações locais.                              |
| Maintainability, Testability                            | [25010] Facilidade de validar a corretude dos modelos e suas transformações. Permite verificação automatizada da conformidade dos modelos                                      | Executar suite de validação (OCL + simulação) em cada commit do modelo. Aprova se taxa de sucesso ≥ 90%.                          |
| Interaction capability, Appropriateness recognizability | [25010] Facilidade de interpretação dos artefatos modelo por desenvolvedores. Determina a adoção prática do processo MDA nas equipes                                           | Aplicar questionário SUS (System Usability Scale) com 5 desenvolvedores. Aprova se pontuação ≥ 68.                                |
| Interaction capability, Learnability                    | [25010] Curva de aprendizado necessária para utilizar as ferramentas de modelagem. Impacta no tempo de onboarding da equipe                                                    | Medir tempo até um novo desenvolvedor criar um modelo funcional completo. Aprova se ≤ 40h.                                        |
| Interaction capability, Operability                     | [25010] Facilidade de operação das ferramentas e processos de modelagem. Afeta produtividade diária da equipe                                                                  | Cronometrar tarefas de modelagem padrão (criar classe, associar, transformar). Aprova se ≤ 5min/tarefa.                           |
| Interaction capability, User error protection           | [25010] Mecanismos para evitar erros durante a criação/edição de modelos. Reduz retrabalho causado por erros de modelagem                                                      | Contar alertas de validação emitidos vs. erros que chegam ao repositório. Aprova se bloqueio ≥ 80% antes do commit.               |
| Interaction capability, User engagement                 | [25010] Estímulo ao uso contínuo das práticas de modelagem. Influencia a adoção a longo prazo do MDA                                                                           | Medir frequência de commits de modelo por desenvolvedor/semana. Aprova se ≥ 1 commit/semana para 80% da equipe.                   |
| Interaction capability, Inclusivity                     | [25010] Acessibilidade das ferramentas de modelagem para diferentes perfis. Amplia o alcance da equipe que pode contribuir                                                     | Testar com 3 perfis distintos (junior, pleno, senior). Aprova se todos completam a mesma tarefa sem ajuda externa.                |
| Interaction capability, User assistance                 | [25010] Disponibilidade de ajuda e documentação integrada às ferramentas. Acelera resolução de dúvidas durante modelagem                                                       | Medir tempo médio entre dúvida e solução usando o recurso de ajuda integrado. Aprova se ≤ 15min.                                  |
| Interaction capability, Self-descriptiveness            | [25010] Clareza com que os modelos se explicam sem documentação externa. Reduz dependência de documentação separada                                                            | Auditoria: novo desenvolvedor deve explicar o propósito de 5 modelos sem consultar documentação externa. Aprova se acertar ≥ 4/5. |

Observações:
- A categoria *Usability* foi renomeada para *Interaction capability* conforme a versão mais recente da ISO/IEC 25010.
- O atributo *Conformance* (cumprimento de normas OMG) não existe como sub‑atributo independente na ISO/IEC 25010, mas é um requisito importante para MBSE/MDA. Recomenda-se adotá-lo como critério adicional vinculado a *Maintainability + Analyzability*.
- As linhas de *Compatibility/Interoperability*, *Reliability/Maturity*, *Security/Confidentiality‑Integrity* e *Performance Efficiency/Time behavior* foram removidas por serem consideradas irrelevantes para o escopo atual da análise, conforme revisão.

# 2. Atributos de Eficiência de Desenvolvimento de Software

| Atributo                               | Métrica                                                            | Como medir                                                  | Impacto esperado                          |
| -------------------------------------- | ------------------------------------------------------------------ | ----------------------------------------------------------- | ----------------------------------------- |
| Lead‑time de desenvolvimento           | Dias/horas da concepção do modelo até entrega de código executável | Cronômetro a partir do início do modelagem até deploy       | Redução de ciclos de release              |
| Taxa de automação                      | % de artefatos gerados automaticamente (código, testes, docs)      | Contagem de artefatos gerados / total de artefatos          | Aumento de produtividade                  |
| Defeito density                        | Nº de defeitos por KLOC gerados a partir de modelos                | Relatórios de qualidade pós‑deploy                          | Qualidade do código gerado                |
| Reutilização                           | % de componentes reutilizados entre projetos                       | Contagem de componentes reutilizados / total de componentes | Redução de esforço em iniciativas futuras |
| Cost of change                         | Custo de alterar requisito após geração do modelo                  | Estimativa baseada em esforço de re‑modelagem e re‑geração  | Determina a "deterministicidade" do SDD   |
| Model‑to‑Model transformation accuracy | % de transformações bem‑sucedidas sem rollback                     | Métricas de sucessos de QVT/Transformações                  | Afetiva confiança no processo MDA         |
| Model drift                            | Tempo para detectar divergência entre modelo e implementação       | Monitoramento contínuo de sincronização                     | Evita retrabalho futuro                   |

# 3. Mapeamento Provisório

| Atributo (Qualidade/Eficiência) | Norma OMG relacionada                    | Comentário de vínculo                                                   |
| ------------------------------- | ---------------------------------------- | ----------------------------------------------------------------------- |
| Functional completeness         | UML, SysML, MDA Guide                    | Modelos de caso de uso e funcionalidades capturam requisitos completos  |
| Performance efficiency          | QVT, DDS                                 | Tempos de execução de transformações determinam performance da pipeline |
| Maintainability                 | SPEM, CIM/PIM                            | Estrutura de modelo modular facilita manutenção                         |
| Lead‑time de desenvolvimento    | MDA Guide, MOF Query/View/Transformation | Automação de QVT reduz tempo de geração                                 |
| Taxa de automação               | QVT, DDS                                 | Percentual de geração automática reflete eficiência da pipeline         |
| Defeito density                 | OCL, ATL, Model‑to‑Model transformations | Qualidade de regras de validação impacta defeitos no código             |



# 4. Matriz de Mapeamento MDA → Atributos

| Norma/Modelo                               | Atributo(s) Relacionado(s)                                                 | Comentário                                                                                                                                        |
| ------------------------------------------ | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CIM (Conceptual Information Model)**     | Functional completeness, Analyzability, Conformance                        | Modelos CIM capturam requisitos de alto nível e estruturas de domínio, vinculados à completude funcional e conformância a normas como BPMN e SBVR |
| **PIM (Platform Independent Model)**       | Reliability, Maintainability, Security                                     | PIM define arquiteturas independentes da plataforma, exigindo confiabilidade e segurança em transformações                                        |
| **PSM (Platform Specific Model)**          | Performance efficiency, Performance Effort                                 | PSM está vinculado a implantações específicas, afetando latência e esforço de desenvolvimento                                                     |
| **QVT (Model Transformations)**            | Taxa de automação, Defeito density, Model-to-Model transformation accuracy | QVT é essencial para automação e precisão em transformações, exigindo métricas de eficiência e qualidade                                          |
| **UML 2.4.1**                              | Maintainability, Compatibility                                             | UML é padrão largamente adotado, impactando compatibilidade e facilidade de manutenção                                                            |
| **SysML 1.4**                              | Reliability, Reusability                                                   | SysML suporta sistemas complexos, exigindo análise de confiabilidade e reutilização de componentes                                                |
| **SPEM (Software Process Engineering)**    | Performance Efficiency, Performance Effort                                 | SPEM influencia processos de desenvolvimento, afetando eficiência em atividades de modelagem e geração de código                                  |
| **DDS (Data Distribution Service)**        | Security, Latency (Time behavior)                                          | DDS é crítico para sistemas distribuídos, exigindo segurança e controle de latência                                                               |
| **MDA Guide**                              | Conformance, Interoperability                                              | Guia OMG é referência para conformância e interoperabilidade entre ferramentas                                                                    |
| **SBVR (Semantic of Business Vocabulary)** | Usability, Understandability                                               | SBVR padroniza vocabulário de domínio, impactando compreensão do modelo por desenvolvedores                                                       |
| **XMI 2.4.2**                              | Compatibility, Model Storage                                               | XMI é formato de troca de metadados, influenciando na compatibilidade e integridade do modelo                                                     |
| **Emerging Standards (ex: SAROS)**         | Scalability                                                                | Novas normas em pesquisa podem introduzir novos atributos                                                                                         |

*Nota: Esta matriz será expandida conforme validação de cada norma. Por exemplo, QVT pode ser vinculado indiretamente à Maintainability se melhorar a modularidade dos modelos.*

---

*Documento consolidado em 23/07/2026 a partir de: 260723_omg_research.md, 260723_checklist_normas_omg.md, 260723_atributos.md, 260723_matrix_mda_atributos.md.*



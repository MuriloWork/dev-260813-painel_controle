---
name: meta-api-code-block-reviewer
description: Valida code blocks (dart e markdown) gerados nos planos de implementacao contra as regras de consistencia da arquitetura
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: planning
---

## Revisao de Code Blocks em Planos de Implementacao

Usado pelo agente `meta-api-code-block-reviewer` para validar code blocks
em planos de implementacao antes da codificacao real, conferindo se respeitam
as regras de consistencia da arquitetura.

### Regras de validacao

**IMPORTANTE — Rigor:** Seja rigoroso. False negative (✅ onde deveria ser ❌) NAO e aceitavel. False positive (❌ onde deveria ser ✅) e aceitavel. Nao use "e refatoracao de codigo existente" como desculpa para ignorar violacoes — as regras se aplicam a todo code block, independente da tag.

#### 1. Hierarquia
- Metodos devem estar encapsulados nas classes, nao soltos como funcoes livres
- Cada classe deve ter responsabilidade unica definida

#### 2. Nomenclatura
- Classes: seguir a arquitetura ja definida. Qualquer nova classe deve ser alinhada com o usuario
- verificar atentamente o nome de cada metodo no code block e se atendem fortemente as seguintes regas
  - Metodos principais: **devem citar explicitamente o data block que processam no nome**
    - exemplo correto ✅ `resolvePostType()`, `buildTextContent()`, `processMedia()`, `formatSchedule()`
    - exemplo errado ❌ `processData()`, `handleContent()`, `run()`, `execute()`
    - exemplo errado ❌ `toPostConfig()` — processa 4 data blocks (type, texto, media, schedule), nome generico que nao cita nenhum
  - Metodos secundarios internos: se especificos de um metodo principal, referenciar o metodo principal; se genericos, referenciar a finalidade
- Metodos que nao citam o data block no nome devem ser reportados como ❌ Nomenclatura

#### 3. Complexidade
- Metodos especificos com menos de 20 linhas: ❌ Complexidade (sem excecao para refatoracao)
- Metodos muito longos (>150 linhas):
  - Se a logica estiver bem organizada e encapsulada (metodos internos, coesao), reportar como ⚠️ atencao
  - Se a logica for amontoada sem encapsulamento, reportar como ❌ Complexidade

#### 4. Pipeline de responsabilidades
Cada etapa do pipeline segue o padrao:
- Busca input -> transformacoes -> output para proxima etapa
- Data blocks separados por etapa:
  - post type: [platform, content_type, media_type]
  - texto: campos especificos
  - media: [image_path, video_path]
  - schedule: [published, scheduled_publish_time]
- Nenhuma etapa deve pular blocos ou acessar dados que nao foram produzidos pela etapa anterior
- Um metodo que produz output de uma etapa diferente da sua propria classe e ❌ Pipeline fit (ex: AssetsEntry.toPostConfig produz post_config que e output de BuildPostConfig)
- Um metodo que chama funcao livre nao declarada no bloco e ❌ Pipeline fit (dependencia externa nao encapsulada)

#### 5. Tag system
- `[1.x]` Novo — code block deve conter classe + metodo novo
- `[2.x]` Refatorar — code block deve mostrar origem -> destino
- `[3.0]` Manter — code block nao deve alterar
- `[4.0]` Descartar — code block deve remover referencias
- Nenhum item `[3.0]` pode ter pendencia
- A tag NAO isenta o code block de nenhuma regra de validacao

### Formato de saida do validador

O relatorio deve conter:
- Cabecalho: nome do bloco revisado, data
- Para cada code block:
  - Descricao do code block
  - Issues encontradas (lista numerada, cada issue com categoria)
  - Recomendacoes/Sugestoes (lista numerada)
- **Resumo geral**: tabela unica consolidando todos os code blocks (uma linha por par code block + regra)
- **NÃO** incluir secao separada de recomendacoes no final do relatorio

| Code Block | Regra | Resultado | Motivo |
|---|---|---|---|
| 1 | Hierarquia | ✅/❌/⚠️ | ... |
| 1 | Nomenclatura | ✅/❌/⚠️ | ... |
| 1 | Complexidade | ✅/❌/⚠️ | ... |
| 1 | Pipeline fit | ✅/❌/⚠️ | ... |
| 1 | Data blocks | ✅/❌/⚠️ | ... |
| 2 | Hierarquia | ✅/❌/⚠️ | ... |
| 2 | Nomenclatura | ✅/❌/⚠️ | ... |
| 2 | Complexidade | ✅/❌/⚠️ | ... |
| 2 | Pipeline fit | ✅/❌/⚠️ | ... |
| 2 | Data blocks | ✅/❌/⚠️ | ... |
| ... | ... | ... | ... |

### Fluxo de revisao

**Regra:** NÃO crie sub-agentes (tool Task). Use bash tool e read diretamente.

1. Validar que todos os parametros de entrada foram fornecidos (senao, retornar ao agente principal)
2. Ler `plan_file` na secao `plan_section` indicada
3. Para cada code block, aplicar as regras 1-5 acima
4. Consultar os `ref_files` para verificar consistencia com a arquitetura real
5. Produzir relatorio completo no formato especificado

### Salvamento obrigatorio do relatorio

Salvar o relatorio em `report_path` **antes** de retornar. Use **bash tool** diretamente:

- Se `report_path` != "no_save":
  ```powershell
  $reportContent | Out-File -LiteralPath "{report_path}" -Encoding utf8
  ```
- Se `report_path` == "no_save", pular.

### Retorno ao agente principal

Apos salvar (ou pular), retornar ao agente principal:
- O resumo geral (tabela unica)
- Nao incluir o relatorio completo na resposta

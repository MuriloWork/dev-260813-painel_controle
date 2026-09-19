---
name: session-plan-update
description: Registra progresso da sessão criando novas versões do plano (v1, v2, v3...) sem sobrescrever documentos anteriores
license: MIT
compatibility: opencode
metadata:
  audience: session-planner
  workflow: session-update
---

## Propósitos

1. monitorar alinhamento entre o plano do projeto e suas entregas 
2. manter versao atualizada com as informações essenciais sobre cada etapa do projeto, otimizando a janela de contexto

Registrar resultados parciais, descobertas e decisões da sessão em andamento, preservando o histórico através de versionamento incremental.

## Regra Fundamental
**Nunca sobrescrever** o documento anterior. Sempre criar uma nova versão.

## Fluxo

### 1. Localizar o Plano
- Usar `plan_dir` e `plan_pattern` declarados na abertura da sessão
- Listar arquivos correspondentes em `{plan_dir}/`
- Identificar a última versão: se `{data}_plan_{session-name}_00.md` é o original, versões seguintes são `{data}_plan_{session-name}_01.md`, `{data}_plan_{session-name}_02.md`, etc.
- Se não houver versão anterior, perguntar ao usuario

### 2. Criar Nova Versão
- premissa: existe uma versao anterior
- ler conteúdo integral da última versão
- criar nova versao do plano, usando `plan_dir` e `plan_pattern`(incrementar o número de versão) com: 
  - "projeto"
    - estrutura do projeto permanece a mesma?
    - se sim, apenas copiar o conteudo da seção da versao anterior
    - senão, atualizar as sub-seções necessarias
  - seção "plano de implantação" com as etapas de implantação
    - qual é a proxima etapa das entregas?
    - subtituir sub-seção "etapa NN - entregas XXXXX" pela proxima etapa das entregas planejadas 

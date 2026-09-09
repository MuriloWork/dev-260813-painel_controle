 **Análise Comparativa: Projeto Meta API vs code-review-graph**

**Data:** 2026-06-28  
**Objetivo:** Identificar funções do projeto que podem ser substituídas pelo code-review-graph

---

# 1. O que o projeto faz

| Módulo                         | Função                                                   | Linguagens          |
| ------------------------------ | -------------------------------------------------------- | ------------------- |
| `parse-ast`                    | Parse de Markdown → AST → JSON/SQLite                    | Python (MarkdownIt) |
| `dart-tools-visit`             | Visitor AST Dart → JSON (611 linhas, 50+ métodos visit*) | Dart                |
| `dart-tools-fetch`             | Download/recolhimento de arquivos Dart                   | Python              |
| `dart-tools-astcountervisitor` | Contagem de nós AST Dart                                 | Dart                |
| `controllers-session`          | Gerenciamento de sessões de pipeline                     | Python              |
| `io-utils-*`                   | Save JSON, SQLite, resolve paths, match                  | Python              |

## 1.1. Comunidades detectadas (20 total)

| Comunidade          | Nós | Coesão | Linguagem |
| ------------------- | --- | ------ | --------- |
| dart-tools-visit    | 70  | 0.333  | Dart      |
| parse-ast           | 14  | 0.191  | Python    |
| logs-log            | 14  | 0.120  | Python    |
| logs-logs           | 11  | 0.135  | Python    |
| io-utils-sqlite     | 9   | 0.063  | Python    |
| controllers-session | 5   | 0.267  | Python    |

---

# 2. O que o code-review-graph faz

| Capacidade      | Descrição                                                         |
| --------------- | ----------------------------------------------------------------- |
| Parse de código | 30+ linguagens via Tree-sitter (Python, Dart, JS, Go, Rust, etc.) |
| Armazenamento   | SQLite (graph.db) com nós, arestas, comunidades, fluxos           |
| Relações        | CALLS, IMPORTS, INHERITS, CONTAINS, REFERENCES                    |
| Comunidades     | Algoritmo Leiden com detecção automática                          |
| Fluxos          | BFS/DFS com score de criticalidade                                |
| Impacto         | Blast radius de mudanças                                          |
| Wiki            | Geração automática de documentação                                |
| Busca           | Embeddings semânticos + FTS5                                      |

---

# 3. Comparação lado a lado

| Capacidade            | Projeto Meta API              | code-review-graph         |
| --------------------- | ----------------------------- | ------------------------- |
| Parse Dart            | AstToJsonVisitor (50+ visit*) | Tree-sitter Dart (nativo) |
| Extração de variáveis | ✅ Visit* (field, variable, param) | ❌ Só Class/Function/File |
| Parse Markdown        | GenerateAst (MarkdownIt)      | ❌ Não suporta             |
| Armazenamento         | SQLite + JSON                 | SQLite (graph.db)         |
| Relações entre código | ❌                             | CALLS, IMPORTS, INHERITS  |
| Comunidades           | ❌                             | Leiden algorithm          |
| Fluxos de execução    | ❌                             | BFS/DFS + criticalidade   |
| Impacto de mudanças   | ❌                             | Blast radius              |
| Wiki automática       | ❌                             | Community → Markdown      |
| Busca semântica       | ❌                             | Embeddings + FTS5         |

## 3.1. Detalhe: extração de variáveis

O graph.db persiste apenas 3 tipos de nós: **Class**, **Function**, **File**.

O `AstToJsonVisitor` do seu projeto extrai granularidade muito maior:

| Método visit*           | O que extrai                          |
| ----------------------- | ------------------------------------- |
| `visitVariableDeclaration` | Variáveis locais                   |
| `visitFieldDeclaration`     | Campos de classe                  |
| `visitSimpleFormalParameter`| Parâmetros de função              |
| `visitFormalParameterList`  | Lista de parâmetros               |
| `visitConstructorFieldInitializer` | Inicializadores de construtor |

O Tree-sitter do CRG **reconhece** esses nós (visível nos `params` das funções), mas **não os persiste** no graph.db. Se o JSON de saída do pipeline precisa desses dados, o CRG sozinho não substitui.

---

# 4. Funções substituíveis

## 4.1. ✅ SUBSTITUÍVEL: `dart-tools-visit` (AstToJsonVisitor)

- **70 nós**, maior comunidade do projeto
- 611 linhas, 50+ métodos `visit*` (visitClassDeclaration, visitMethodDeclaration, etc.)
- O Tree-sitter do CRG já extrai classes, métodos, imports e chamadas de Dart
- **Ganho:** eliminar ~600 linhas de código Dart

## 4.2. ✅ SUBSTITUÍVEL: `dart-tools-astcountervisitor`

- Contagem de nós AST Dart
- Trivial com o grafo do CRG (query sobre nós com kind=Class/Function)

## 4.3. ❌ NÃO SUBSTITUÍVEL: `parse-ast` (GenerateAst)

- Parse de **Markdown** (não é código)
- CRG não faz parse de conteúdo Markdown
- Mantém necessidade de MarkdownIt

## 4.4. ❌ NÃO SUBSTITUÍVEL: `io-utils/save_json`

- Exporta JSON estruturado do jeito que o projeto precisa
- CRG não gera esse tipo de saída

## 4.5. ❌ NÃO SUBSTITUÍVEL: `controllers-session`

- Gerenciamento de sessões de pipeline
- CRG não tem conceito de sessão

---

# 5. Opções para extração de variáveis e parâmetros

Três caminhos possíveis para resolver a lacuna de extração de variáveis/parâmetros:

## 5.1. Opção A: Estender o code-review-graph

**O que:** Modificar o código-fonte do CRG para persistir variáveis, campos e parâmetros como nós adicionais no graph.db.

| Aspecto | Avaliação |
|---------|-----------|
| Esforço | Médio — o Tree-sitter já reconhece os nós, falta só persistir |
| Dependência | Fork do CRG ou PR para o repositório upstream |
| Manutenção | Precisa sincronizar com versões futuras do CRG |
| Saída | Nó extra por variável/parâmetro com edges CONTAINS do pai |
| Compatibilidade | 100% — usa o mesmo parser Tree-sitter já integrado |

**Prós:** usa infraestrutura existente, parser único, dados já estruturados  
**Contras:** depende de manter fork ou PR aceito, acoplamento ao CRG

## 5.2. Opção B: Criar novo parser Tree-sitter independente

**O que:** Criar um parser separado em Python usando `tree-sitter` + grammar Dart, que gera o JSON de saída diretamente.

| Aspecto | Avaliação |
|---------|-----------|
| Esforço | Alto — implementar visitor completo em Python |
| Dependência | Só `tree-sitter` + `tree-sitter-dart` |
| Manutenção | Independente, controle total |
| Saída | JSON estruturado no formato que o pipeline precisa |
| Compatibilidade | Precisa mapear os tipos do Tree-sitter para o modelo JSON atual |

**Prós:** controle total, sem dependência externa, formato de saída customizável  
**Contras:** duplica lógica de parsing, manutenção independente

## 5.3. Opção C: Ajustar o parser atual (AstToJsonVisitor)

**O que:** Manter o `AstToJsonVisitor` Dart, mas refatorar para simplificar (reduzir de 50+ métodos visit* para apenas os necessários).

| Aspecto | Avaliação |
|---------|-----------|
| Esforço | Baixo/Médio — já funciona, só otimizar |
| Dependência | Dart SDK (já instalado) |
| Manutenção | Baixa — código maduro e testado |
| Saída | JSON no formato exato que o pipeline precisa |
| Compatibilidade | 100% — já é o parser atual |

**Prós:** já funciona, formato de saída garantido, sem dependências novas  
**Contras:** mantém 600+ linhas Dart, não integra com análise do CRG

## 5.4. Comparativo geral

| Critério | A: Estender CRG | B: Novo parser TS | C: Ajustar atual |
|----------|-----------------|-------------------|-------------------|
| Esforço inicial | Médio | Alto | Baixo |
| Controle de saída | Limitado pelo CRG | Total | Total |
| Integração com CRG | Nativa | Precisa exportar | Precisa exportar |
| Manutenção | Fork/PR | Independente | Dart SDK |
| Elimina código Dart | Sim | Sim | Não |
| Dados variáveis | Sim (se estender) | Sim | Sim |

## 5.5. Recomendação

- **Se o objetivo é eliminar código Dart:** Opção A (estender CRG)
- **Se o objetivo é controle total:** Opção B (novo parser)
- **Se o objetivo é minimizar risco:** Opção C (manter e ajustar)
- **Se o objetivo é análise + exportação:** Opção A + C (CRG para análise, Dart para exportação)

---

# 6. Próximos passos

O **`dart-tools-visit`** é o candidato principal para substituição **parcial**. O Tree-sitter já faz nativamente a extração de classes, métodos e imports, mas **não extrai variáveis e parâmetros**.

**Cenários possíveis:**

| Cenário | O que fazer |
|---------|-------------|
| JSON de saída **precisa** de variáveis | Manter AstToJsonVisitor ou estender o CRG para persistir variáveis |
| JSON de saída **não precisa** de variáveis | Substituir pelo CRG, eliminar ~600 linhas Dart |
| Quer **análise** + **exportação** | Usar CRG para análise (comunidades, fluxos, impacto) + manter AstToJsonVisitor para exportação JSON |

1. Definir se o JSON de saída do pipeline precisa de variáveis/parâmetros
2. Escolher opção (A, B ou C) conforme o objetivo
3. Implementar e validar contra os dados atuais do AstToJsonVisitor

---
name: dart-conventions
description: Convenções de código Dart e estilo do projeto Meta API
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: coding
---

## Formatação
- Seguir dartfmt/dart format (2 espaços indentação)
- Limite de linha: 80-100 caracteres
- Aspas simples para strings, duplas apenas quando necessário
- Vírgula final em listas/mapas multilinha

## Importações
- Ordem: dart → pacotes externos → arquivos locais
- Importações relativas para arquivos no mesmo pacote
- Evitar imports não utilizados

## Tipos
- Especificar tipos em parâmetros e retornos
- var apenas quando tipo é óbvio
- Evitar dynamic; preferir Map<String, dynamic> com validação
- Tipos genéricos especificados: List<String>, Map<String, dynamic>

## Nomenclatura
- Classes: PascalCase
- Funções/variáveis: camelCase
- Arquivos: snake_case
- Enums: PascalCase, valores camelCase
- Acronismos maiúsculos: Url, Id, API

## Estrutura
- Funções pequenas (max 20-30 linhas)
- Comentários só para o "porquê", não o "o quê"
- Early returns para evitar aninhamento
- try/catch para I/O, rede, parsing

## JSON
- Validar chaves antes de acessar
- is/as com cautela
- Map<String, dynamic>? para opcionais
- Nunca confiar cegamente em dados externos

## Arquivos
- Verificar existência antes de ler
- Caminhos absolutos ou relativos bem definidos
- Tratar exceções de I/O

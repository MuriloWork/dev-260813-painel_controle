# 1. contexto do projeto 

## 1.1. resumo
project_name: "painel controle"
- ferramentas de apoio para vibe coding 
- UI: terminal powershell com abas (paineis): [shell, session, parse, logs, sync]
- painel shell: dispara comandos shell genéricos
- painel session: dispara code scripts para [edição de markdown, lint tools]
- painel parse: dispara parsers de [markdown, code scripts]
- painel logs: deprecated
- painel sync: dispara code scripts para sincronização de dados [json, sqlite, csv, xlsx]

## 1.2. stack do projeto 
- ambiente/servidor: local
- UI: powershell
- script languages: ps1, python, sql
- dados: sqlite, json 

## 1.3. caminhos do projeto 
| path type | path name      | path                                                                                                                         |
| --------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| session   | project_path   | `C:\Users\muril\OneDrive\01 mycloud\01 sistMu\10.01 scripts\01_root\main\260511_meta_api`                                    |
| session   | session_folder | `C:\Users\muril\OneDrive\01 mycloud\01 sistMu\10.01 scripts\01_root\main\260511_meta_api\sessions\260623_arquitetura_painel` |
| target    | target_folder  | `C:\Users\muril\OneDrive\01 mycloud\01 sistMu\10.01 scripts\01_root\main\260511_meta_api\dev`                                |
| ignore    | ignore_pattern  | `C:\Users\muril\OneDrive\01 mycloud\01 sistMu\10.01 scripts\01_root\main\260511_meta_api\dev\.*`                                |

pastas no `ignore_pattern` não são necessarias para edição de codigo, mas deverão ser movidas conforme a nova arquitetura

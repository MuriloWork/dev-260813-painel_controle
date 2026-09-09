# 2. arquitetura do projeto
Neste projeto estamos revisando a arquitetura existente para uma organização mais clara de layers.

## 2.1. versão atual ⟶ versão nova
path base: `C:\Users\muril\OneDrive\01 mycloud\01 sistMu\10.01 scripts\01_root\main\260511_meta_api\`
### 2.1.1. camada frontend
| versão atual                       | versão nova                            | comentários |
| ---------------------------------- | -------------------------------------- | ----------- |
| dev\src\painel\painel_controle.ps1 | dev\src\view_shell\painel_controle.ps1 |             |

### 2.1.2. camada backend
| versão atual                             | versão nova                     | comentários                              |
| ---------------------------------------- | ------------------------------- | ---------------------------------------- |
|                                          | dev\src\controllers             | ainda não existe code script             |
| dev\src\painel\config\painel_settings.py | dev\src\services\painel_init.py |                                          |
| dev\src\painel\services                  | dev\src\services                |                                          |
| dev\src\painel\services\logs             | dev\src\services\logs           |                                          |
| dev\src\painel\services\parse            | dev\src\services\parse          |                                          |
|                                          | dev\src\services\sessions       | ainda não existe code script             |
|                                          | dev\src\services\sync           | ainda não existe code script             |
| dev\src\painel\dart_tools                | dev\src\services\dart_tools     |                                          |
| dev\src\painel\services\utils_io         | dev\src\utils_io                |                                          |
| dev\src\sql_sqlite                       | dev\src\sql_sqlite              |                                          |
| dev\src\painel\models                    | dev\src\models                  |                                          |
| dev\src\painel\config                    | dev\src\repositories            | sub-pasta schema → models?               |
| dev\src\utils_auth                       | dev\src\repositories            | renomear arquivos para `auth_data*.json` |
|                                          | dev\src\temp                    | testes                                   |


### 2.1.3. camada dados
| versão atual           | versão nova                   | comentários |
| ---------------------- | ----------------------------- | ----------- |
| dev\dbMu\parse_dart.db | dev\dbMu\sqlite\parse_dart.db |             |
| dev\dbMu\parse_md.db   | dev\dbMu\sqlite\parse_md.db   |             |
| dev\parse_docs         | dev\dbMu\doc_painel           |             |


# Plano: Criar views de auditoria (log_*) no banco erp.db

## Referencias
- pastas e arquivos de planejamento
  - plan_dir: sprints\260526_sqlite_ast_views
  - plan_file_pattern: 260526_plan_sqlite_views_{version_number}.md
  - briefing_file: AGENTS.md
  - plan_dir: sprints\260526_sqlite_ast_views
  - investigate_file: 260526_plan_sqlite_views_01_investigate.md
  - plan_file: 260526_plan_sqlite_views_01.md
  - review_file: 260526_plan_sqlite_views_01_review.md
- pastas e arquivos de trabalho
  - session_base_dir: dev\sqlite\
    - oop_script: src\scripts\
    - banco: dev\sqlite\parse_dart.db
    - sql_script_dir: dev\sqlite\sqlite_sql_parse\
  - session_inicial_version_dir: dev\sqlite\sqlite_sql_parse\version 260526\

## Esquemas e Estruturas Encontradas

### Tabelas
- `log_access`
  - colunas: id, user_id, action, timestamp, ip
  - pk: id
  - fk: user_id -> users.id
- `log_changes`
  - colunas: id, table_name, record_id, old_value, new_value, changed_by
  - pk: id

### Views
- `vw_access_summary`
  - base: log_access
  - definicao: GROUP BY user_id, COUNT(*)
- `vw_change_log`
  - base: log_changes
  - definicao: SELECT * FROM log_changes ORDER BY id DESC

### Triggers
- `trg_log_access_insert`
  - tabela: log_access
  - evento: AFTER INSERT
  - acao: atualiza contador em access_stats
- `trg_log_changes_audit`
  - tabela: log_changes
  - evento: AFTER INSERT
  - acao: notifica admin se changed_by for NULL

### Funcoes
- (nenhuma funcao encontrada)

### Relacionamentos
- `log_access.user_id -> users.id`

### Dependencias
- `log_access -> vw_access_summary -> dashboard_api`
- `log_changes -> vw_change_log -> audit_report`

## Modificacoes propostas
- **vw_log_access**
  - referencia: `tb_ast.sql` — CTE recursiva que extrai nos de flutter_app_ast
  - logica: SELECT * FROM log_access com filtro por usuario ativo e periodo
  - metodos principais: getUserAccess(user_id), getAccessByDate(start, end), getRecentActivity(limit)
- **vw_log_changes**
  - referencia: `tb_ast_func.sql` — hierarquia por parent_node_id com mapeamento de niveis
  - logica: SELECT * FROM log_changes JOIN users ON changed_by = users.id, ordenado por timestamp DESC
  - metodos principais: getChangesByTable(table_name), getChangesByUser(user_id), getChangesSince(timestamp)

## Plano de Acao
> Aguardando aprovacao do usuario.
### Etapa 01 -- Criar vw_log_access.sql
### Etapa 02 -- Criar vw_log_changes.sql

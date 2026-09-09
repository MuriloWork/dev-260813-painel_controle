-- DDL da tabela tb_ast
-- line declarado como INTEGER (explicit type)
CREATE TABLE IF NOT EXISTS tb_ast (
  project_name TEXT,
  version TEXT,
  file_path TEXT,
  "column",
  parent_node_id,
  line INTEGER,
  source_text,
  return_type,
  name,
  value,
  type
);

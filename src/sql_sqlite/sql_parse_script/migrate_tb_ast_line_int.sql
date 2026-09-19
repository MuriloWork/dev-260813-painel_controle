-- Recriar tb_ast com line INTEGER
CREATE TABLE tb_ast (
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

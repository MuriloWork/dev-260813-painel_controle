-- Atualizar a tabela tb_ast_func com os dados calculados
-- Primeiro, limpar a tabela existente
DELETE FROM tb_ast_func;

-- Depois, inserir os novos dados
INSERT INTO tb_ast_func
SELECT
  project_name
  ,version
  ,file_path
  ,column
  ,parent_node_id
  ,line
  ,source_text
  ,return_type_name_value
  ,type
  ,COALESCE(
    (CASE WHEN type = 'ClassDeclarationImpl' THEN return_type_name_value END),
    ClassDeclarationImpl
  ) AS ClassDeclarationImpl
  ,COALESCE(
    (CASE WHEN type = 'MethodDeclarationImpl' THEN return_type_name_value END),
    MethodDeclarationImpl
  ) AS MethodDeclarationImpl
  ,COALESCE(
    (CASE WHEN type IN ('VariableDeclarationImpl', 'MethodInvocationImpl') THEN return_type_name_value END),
    VariableDeclarationImpl
  ) AS VariableDeclarationImpl
FROM (
  WITH level_identification AS (
    -- Identificar o nível hierárquico com base na quantidade de números em parent_node_id
    SELECT
      project_name,
      version,
      file_path,
      "column",
      parent_node_id,
      line,
      source_text,
      type,
      CASE
          WHEN type IN ('ClassDeclarationImpl', 'MethodDeclarationImpl') THEN
              COALESCE(name, return_type, value)
          WHEN type = 'MethodInvocationImpl' THEN
              source_text
          ELSE
              COALESCE(name, value, return_type)
      END AS return_type_name_value,
      -- Contar o número de elementos no parent_node_id (número de vírgulas + 1)
      (LENGTH(parent_node_id) - LENGTH(REPLACE(parent_node_id, ',', '')) + 1) AS level_count,
      -- Identificar se é classe/função (2 números), método (3 números) ou variável (mais de 3)
      CASE
        WHEN (LENGTH(parent_node_id) - LENGTH(REPLACE(parent_node_id, ',', '')) + 1) = 2
        THEN COALESCE(name, return_type, value)
      END AS class_name,
      CASE
        WHEN (LENGTH(parent_node_id) - LENGTH(REPLACE(parent_node_id, ',', '')) + 1) = 3
        THEN COALESCE(name, return_type, value)
      END AS method_name,
      CASE
        WHEN (LENGTH(parent_node_id) - LENGTH(REPLACE(parent_node_id, ',', '')) + 1) > 3
        THEN COALESCE(name, return_type, value)
      END AS variable_name
    FROM tb_ast
    WHERE type IN ('ClassDeclarationImpl', 'FunctionDeclarationImpl', 'MethodDeclarationImpl', 'MethodInvocationImpl', 'VariableDeclarationImpl')
	  	AND file_path NOT LIKE '%test%'
  ),
  hierarchy_mapping AS (
    -- Mapear a hierarquia: associar métodos e variáveis às suas classes e métodos pais
    SELECT
      li.project_name,
      li.version,
      li.file_path,
      li."column",
      li.parent_node_id,
      li.line,
      li.source_text,
      li.type,
      li.return_type_name_value,
      li.level_count,
      -- Identificar a classe pai mais próxima
      (SELECT class_name
       FROM level_identification li2
       WHERE li2.file_path = li.file_path
         AND li2.level_count = 2
         AND li.parent_node_id LIKE li2.parent_node_id || '%'
       LIMIT 1) AS ClassDeclarationImpl,
      -- Identificar o método pai mais próximo (se aplicável)
      (SELECT method_name
       FROM level_identification li3
       WHERE li3.file_path = li.file_path
         AND li3.level_count = 3
         AND li.parent_node_id LIKE li3.parent_node_id || '%'
         AND LENGTH(li3.parent_node_id) > (
           SELECT MIN(LENGTH(parent_node_id))
           FROM level_identification
           WHERE file_path = li.file_path AND level_count = 2
         )
       LIMIT 1) AS MethodDeclarationImpl,
      -- Identificar a variável (se aplicável)
      (SELECT variable_name
       FROM level_identification li4
       WHERE li4.file_path = li.file_path
         AND li4.level_count > 3
         AND li.parent_node_id LIKE li4.parent_node_id || '%'
         AND LENGTH(li4.parent_node_id) > (
           SELECT MAX(LENGTH(parent_node_id))
           FROM level_identification
           WHERE file_path = li.file_path AND level_count <= 3
         )
       LIMIT 1) AS VariableDeclarationImpl
    FROM level_identification li
  ),
  ranked_rows AS (
    SELECT *,
      ROW_NUMBER() OVER (
        PARTITION BY file_path, line
        ORDER BY
          CASE type
            WHEN 'ClassDeclarationImpl' THEN 1
            WHEN 'FunctionDeclarationImpl' THEN 2
            WHEN 'MethodDeclarationImpl' THEN 3
            WHEN 'MethodInvocationImpl' THEN 4
            WHEN 'VariableDeclarationImpl' THEN 5
          END
      ) AS rn
    FROM hierarchy_mapping
  )
  SELECT
    project_name
    ,version
    ,file_path
    ,column
    ,parent_node_id
    ,line
    ,source_text
    ,return_type_name_value
    ,type
    ,COALESCE(
      (CASE WHEN type = 'ClassDeclarationImpl' THEN return_type_name_value END),
      ClassDeclarationImpl
    ) AS ClassDeclarationImpl
    ,COALESCE(
      (CASE WHEN type = 'MethodDeclarationImpl' THEN return_type_name_value END),
      MethodDeclarationImpl
    ) AS MethodDeclarationImpl
    ,COALESCE(
      (CASE WHEN type IN ('VariableDeclarationImpl', 'MethodInvocationImpl') THEN return_type_name_value END),
      VariableDeclarationImpl
    ) AS VariableDeclarationImpl
  FROM ranked_rows
  WHERE rn = 1
  ORDER BY file_path, line, parent_node_id
);

-- Atualizar a tabela tb_ast_func_map_2d com os dados calculados
-- Primeiro, limpar a tabela existente
DELETE FROM tb_ast_func_map_2d;

-- Depois, inserir os novos dados
INSERT INTO tb_ast_func_map_2d
SELECT
  file_path
  ,ClassDeclarationImpl
  ,MethodDeclarationImpl
  ,VariableDeclarationImpl
  ,max_count   -- numero de ocorrencias da variavel em cada linha
FROM (
  WITH class_method AS (      -- lista de classes/metodos selecionados agrupados
    SELECT
      file_path
      ,ClassDeclarationImpl
      ,MethodDeclarationImpl
      ,cm_filter
    FROM tb_ast_func_map_1d
--     WHERE cm_filter = 'sim'
    GROUP BY file_path, ClassDeclarationImpl, MethodDeclarationImpl
  ),
  var AS (                -- lista de variaveis selecionadas (após atualização da tb_dim_variables)
    SELECT DISTINCT
      VariableDeclarationImpl
    FROM tb_dim_variables
    WHERE filtro = 'sim'
  ),
  source_var AS (           -- todas as variaveis selecionadas em todos arquivos/classes/metodos
    SELECT
      tf.file_path
      ,tf.line
      ,tf.parent_node_id
      ,tf.source_text
      ,tf.ClassDeclarationImpl
      ,tf.MethodDeclarationImpl
      ,var.VariableDeclarationImpl
    FROM tb_ast_func tf
      CROSS JOIN var
    ORDER BY tf.file_path, tf.line, tf.parent_node_id, var.VariableDeclarationImpl
  ),
  count_var AS (            -- contagem de variaveis no source_text
    SELECT
      file_path
      ,ClassDeclarationImpl
      ,MethodDeclarationImpl
      ,VariableDeclarationImpl
      ,MAX(( LENGTH(source_text) - LENGTH(REPLACE(source_text,
          CASE
            WHEN SUBSTR(VariableDeclarationImpl, 1, 1) = '_'
            THEN SUBSTR(VariableDeclarationImpl, 2)
            ELSE VariableDeclarationImpl
          END, '')))
                / LENGTH(
          CASE
            WHEN SUBSTR(VariableDeclarationImpl, 1, 1) = '_'
            THEN SUBSTR(VariableDeclarationImpl, 2)
            ELSE VariableDeclarationImpl
          END)
      ) AS max_count   -- numero de ocorrencias da variavel em cada linha
    FROM source_var
    GROUP BY file_path, ClassDeclarationImpl, MethodDeclarationImpl, VariableDeclarationImpl
  )
  SELECT                    -- JOIN aplica filtro de classes/metodos
    cv.file_path
    ,cv.ClassDeclarationImpl
    ,cv.MethodDeclarationImpl
    ,cv.VariableDeclarationImpl
    ,cv.max_count
  FROM (SELECT * FROM count_var WHERE max_count > 0) cv    -- filtrando contagens > 0
    JOIN class_method cm 
      ON cv.file_path = cm.file_path
      AND cv.ClassDeclarationImpl = cm.ClassDeclarationImpl
      AND (
        (cv.MethodDeclarationImpl = cm.MethodDeclarationImpl)
        OR (cv.MethodDeclarationImpl IS NULL AND cm.MethodDeclarationImpl IS NULL)
      )
);

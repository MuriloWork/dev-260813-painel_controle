
-- Atualizar a tabela tb_dim_variables antes de executar a view
-- Inserir apenas novas variáveis que não estão na tabela, preservando valores existentes
INSERT INTO tb_dim_variables (VariableDeclarationImpl, filtro)
SELECT DISTINCT v.return_type_name_value, 'sim'  -- Novas variáveis recebem 'sim' como padrão
FROM (
  SELECT DISTINCT
    return_type_name_value
  FROM tb_ast_func
  WHERE type = 'VariableDeclarationImpl'
) v
LEFT JOIN tb_dim_variables d ON v.return_type_name_value = d.VariableDeclarationImpl
WHERE d.VariableDeclarationImpl IS NULL;

-- Remover apenas variáveis que não existem mais em tb_ast_func
DELETE FROM tb_dim_variables
WHERE VariableDeclarationImpl NOT IN (
  SELECT DISTINCT return_type_name_value
  FROM tb_ast_func
  WHERE type = 'VariableDeclarationImpl'
);

-- Atualizar a tabela tb_ast_func_map_1d com os dados calculados
-- Primeiro, limpar a tabela existente
DELETE FROM tb_ast_func_map_1d;

-- Depois, inserir os novos dados
INSERT INTO tb_ast_func_map_1d
SELECT DISTINCT
  file_path,
  ClassDeclarationImpl,
  MethodDeclarationImpl,
  VariableDeclarationImpl,
  'sim' AS cm_filter
FROM tb_ast_func
WHERE ClassDeclarationImpl IS NOT NULL
  -- AND type IN ('ClassDeclarationImpl', 'MethodDeclarationImpl', 'VariableDeclarationImpl');
ORDER BY file_path, line, parent_node_id

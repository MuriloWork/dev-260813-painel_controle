DROP TRIGGER IF EXISTS trg_vw_ast_func_map_1d_update;

-- Trigger para atualizar imediatamente temp_vw_ast_func_map_1d quando a coluna trg_vw_ast_func_map_1d_enabled é atualizada na tabela de controle
-- Somente quando o valor muda de 0 para 1
CREATE TRIGGER trg_vw_ast_func_map_1d_update
AFTER UPDATE OF trg_vw_ast_func_map_1d_enabled ON tb_controle_ast
FOR EACH ROW
WHEN OLD.trg_vw_ast_func_map_1d_enabled = 0 AND NEW.trg_vw_ast_func_map_1d_enabled = 1
BEGIN
  UPDATE tb_controle_ast SET trg_vw_ast_enabled = 0, trg_vw_ast_func_enabled = 0, trg_vw_ast_func_map_1d_enabled = 0, trg_vw_ast_func_map_2d_enabled = 0 WHERE id = 1;
  DELETE FROM temp_vw_ast_func_map_1d;
  INSERT INTO temp_vw_ast_func_map_1d SELECT * FROM vw_ast_func_map_1d;

  -- Atualizar a tabela tb_dim_variables antes de executar a view
  -- Inserir novas variáveis que não estão na tabela
  INSERT INTO tb_dim_variables (VariableDeclarationImpl, filtro)
  SELECT DISTINCT v.return_type_name_value, 'não'  -- Valor padrão 'nao' para novo filtro
  FROM (
    SELECT DISTINCT
      return_type_name_value
    FROM temp_vw_ast_func
    WHERE type = 'VariableDeclarationImpl'
  ) v
  LEFT JOIN tb_dim_variables d ON v.return_type_name_value = d.VariableDeclarationImpl
  WHERE d.VariableDeclarationImpl IS NULL;

  -- Remover variáveis que não existem mais
  DELETE FROM tb_dim_variables
  WHERE VariableDeclarationImpl NOT IN (
    SELECT DISTINCT return_type_name_value
    FROM temp_vw_ast_func
    WHERE type = 'VariableDeclarationImpl'
  );

  -- Atualizar a tabela de controle para continuar a cadeia de atualizações
  UPDATE tb_controle_ast SET trg_vw_ast_func_map_2d_enabled = 1 WHERE id = 1;
END;
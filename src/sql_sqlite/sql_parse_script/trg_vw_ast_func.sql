DROP TRIGGER IF EXISTS trg_vw_ast_func_update;

-- Trigger para atualizar imediatamente temp_vw_ast_func quando a coluna trg_vw_ast_func_enabled é atualizada na tabela de controle
-- Somente quando o valor muda de 0 para 1
CREATE TRIGGER trg_vw_ast_func_update
AFTER UPDATE OF trg_vw_ast_func_enabled ON tb_controle_ast
FOR EACH ROW
WHEN OLD.trg_vw_ast_func_enabled = 0 AND NEW.trg_vw_ast_func_enabled = 1
BEGIN
  UPDATE tb_controle_ast SET trg_vw_ast_enabled = 0, trg_vw_ast_func_enabled = 0, trg_vw_ast_func_map_1d_enabled = 0 WHERE id = 1;
  DELETE FROM temp_vw_ast_func;
  INSERT INTO temp_vw_ast_func SELECT * FROM vw_ast_func;

  -- Atualizar a tabela de controle para continuar a cadeia de atualizações
  UPDATE tb_controle_ast SET trg_vw_ast_func_map_1d_enabled = 1 WHERE id = 1;
END;
-- Tabela de controle para habilitar/desabilitar os triggers individualmente
-- Cada coluna representa o estado de um trigger específico
DROP TABLE IF EXISTS tb_controle_ast;
CREATE TABLE tb_controle_ast (
    id INTEGER PRIMARY KEY CHECK (id = 1),  -- Apenas uma linha é permitida
    trg_vw_ast_enabled INTEGER DEFAULT 0,  -- 0 = desabilitado, 1 = habilitado
    trg_vw_ast_func_enabled INTEGER DEFAULT 0,  -- 0 = desabilitado, 1 = habilitado
    trg_vw_ast_func_map_1d_enabled INTEGER DEFAULT 0,  -- 0 = desabilitado, 1 = habilitado
    trg_vw_ast_func_map_2d_enabled INTEGER DEFAULT 0   -- 0 = desabilitado, 1 = habilitado
);

-- Inserir o valor padrão (todos os triggers desabilitados)
INSERT OR REPLACE INTO tb_controle_ast (id, trg_vw_ast_enabled, trg_vw_ast_func_enabled, trg_vw_ast_func_map_1d_enabled, trg_vw_ast_func_map_2d_enabled) 
VALUES (1, 0, 0, 0, 0);
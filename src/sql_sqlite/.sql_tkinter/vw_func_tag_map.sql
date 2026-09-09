-- View: tb_ast_func_map_2d left join vw_tag_map
-- Combina func_map com tag_map para mapear variáveis de log

DROP VIEW IF EXISTS vw_func_tag_map;
CREATE VIEW vw_func_tag_map AS
SELECT 
    COALESCE(fm.file_path, tm.file_path) AS file_pathl,
    COALESCE(fm.ClassDeclarationImpl, tm.class_name) AS ClassDeclarationImpl,
    COALESCE(fm.MethodDeclarationImpl, tm.method_name) AS MethodDeclarationImpl,
    COALESCE(fm.VariableDeclarationImpl, tm.log_var) AS VariableDeclarationImpl,
    COALESCE(fm.selected, 0) AS selected,
    fm.max_count AS split_count,
    tm.tag_count
FROM tb_ast_func_map_2d fm
FULL OUTER JOIN vw_tag_map tm 
    ON fm.file_path = tm.file_path 
    AND fm.ClassDeclarationImpl = tm.class_name 
    AND fm.MethodDeclarationImpl = tm.method_name
    AND fm.VariableDeclarationImpl = tm.log_var
ORDER BY fm.file_path, fm.ClassDeclarationImpl, fm.MethodDeclarationImpl, fm.VariableDeclarationImpl;

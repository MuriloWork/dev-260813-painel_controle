-- View: tag_map left join logs_string on log_name
-- join em log_name para encontrar as variaveis que devem ser removidas em cada log
-- elimina linhas onde tag_var_remove = log_var
-- agrupa por file_path, class_name, method_name, log_var

CREATE VIEW IF NOT EXISTS vw_tag_map AS
SELECT 
    tm.file_path,
    tm.class_name,
    tm.method_name,
    ls.VariableDeclarationImpl AS log_var,
    COUNT(tm.tag_name) AS tag_count
FROM tag_map tm
LEFT JOIN logs_string ls ON tm.log_name = ls.log_name
WHERE tm.VariableDeclarationImpl != ls.VariableDeclarationImpl 
   OR tm.VariableDeclarationImpl IS NULL
GROUP BY tm.file_path, tm.class_name, tm.method_name, ls.VariableDeclarationImpl
ORDER BY tm.file_path, tm.class_name, tm.method_name, ls.VariableDeclarationImpl;

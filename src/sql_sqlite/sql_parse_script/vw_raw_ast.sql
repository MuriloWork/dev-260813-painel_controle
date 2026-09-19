DROP VIEW IF EXISTS vw_raw_ast;
CREATE VIEW vw_raw_ast AS

SELECT 
	raw.*,
	ast.source_text,
	ast.return_type_name_value,
	ast.type,
	ast.ClassDeclarationImpl,
	ast.MethodDeclarationImpl,
	ast.VariableDeclarationImpl
FROM vw_raw_flat_01 raw
	JOIN tb_ast_func ast 
		ON raw.file_path =ast.file_path  
		AND raw.line=ast.line 

--WHERE 
--    version = (SELECT max(version) FROM raw_script)
--ORDER BY
--    file_path
--    ,line
;

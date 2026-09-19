-- Atualizar a tabela tb_ast com os dados calculados
-- Primeiro, limpar a tabela existente
DELETE FROM tb_ast;

-- Depois, inserir os novos dados
INSERT INTO tb_ast
SELECT
    project_name
    ,version
    ,file_path
    ,column
    ,parent_node_id
    ,line
    ,source_text
    ,return_type
    ,name
    ,value
    ,type
FROM (
    WITH RECURSIVE ast_tree(
        project_name
        ,version
        ,file_path
        ,json_data
        ,column
        ,parent_node_id
        ,line
        ,source_text
        ,return_type
        ,name
        ,value
        ,type
    ) AS (
        SELECT
            project_name
            ,version
            ,file_path
            ,json_data
            ,json_extract(json_data, '$.column')
            ,json_extract(json_data, '$.offset') AS parent_node_id
            ,json_extract(json_data, '$.line')
            ,json_extract(json_data, '$.source_text')
            ,NULL
            ,json_extract(json_data, '$.name') AS name
            ,json_extract(json_data, '$.value') AS value
            ,json_extract(json_data, '$.type') AS type
        FROM flutter_app_ast

        UNION ALL
        SELECT
            ast_tree.project_name
            ,ast_tree.version
            ,ast_tree.file_path
            ,json_each.value
            ,json_extract(json_each.value, '$.column')
            ,ast_tree.parent_node_id || ', ' || json_extract(json_each.value, '$.offset')
            ,json_extract(json_each.value, '$.line')
            ,json_extract(json_each.value, '$.source_text')
            ,COALESCE(json_extract(json_each.value, '$.returnType'), json_extract(json_each.value, '$.staticType')) as return_type
            ,json_extract(json_each.value, '$.name') AS name
            ,json_extract(json_each.value, '$.value') AS value
            ,json_extract(json_each.value, '$.type') AS type
        FROM
            ast_tree
            ,json_each(ast_tree.json_data, '$.children') AS json_each
    )
    SELECT
        project_name
        ,version
        ,file_path
--        ,CASE
--            WHEN instr(file_path, '.dart') > 0 THEN file_path
--            ELSE REPLACE(file_path, '_', '/') || '.dart'
--        END AS file_path
        ,"column"
        ,parent_node_id
        ,CAST(line AS INTEGER) AS line
        ,source_text
        ,return_type
        ,name
        ,value
        ,type
    FROM ast_tree
    WHERE
    	-- version = (SELECT max(version) FROM ast_tree)
    	-- AND type NOT IN ('CompilationUnitImpl')
    	type NOT IN ('CompilationUnitImpl')
    	-- AND return_type IS NOT NULL
    ORDER BY
        CASE
            WHEN instr(file_path, '.dart') > 0 THEN file_path
            ELSE REPLACE(file_path, '_', '/') || '.dart'
        END
        ,CAST(line AS INTEGER)
        ,parent_node_id
);

DROP VIEW IF EXISTS vw_ast_group;
CREATE VIEW vw_ast_group AS

WITH RECURSIVE ast_tree(
    project_name
    ,version
    ,file_path
    ,json_node
    ,parent_id
    ,node_id
    ,line
    ,column
    ,source_text
    ,type
) AS (
    SELECT
        project_name
        ,version
        ,file_path
        ,json_data
        ,NULL
        ,json_extract(json_data, '$.offset')
        ,json_extract(json_data, '$.line')
        ,json_extract(json_data, '$.column')
        ,json_extract(json_data, '$.source_text')
        ,json_extract(json_data, '$.type') AS type
    FROM flutter_app_ast

    UNION ALL
    SELECT
        ast_tree.project_name
        ,ast_tree.version
        ,ast_tree.file_path
        ,json_each.value
        ,ast_tree.node_id
        ,json_extract(json_each.value, '$.offset')
        ,json_extract(json_each.value, '$.line')
        ,json_extract(json_each.value, '$.column')
        ,json_extract(json_each.value, '$.source_text')
        ,json_extract(json_each.value, '$.type') AS type
    FROM
        ast_tree
        ,json_each(ast_tree.json_node, '$.children') AS json_each
)
-- SELECT COUNT(*) FROM ast_tree
SELECT
    project_name
    ,version
    ,file_path
    ,parent_id
    ,node_id
    ,line
    ,column
    ,source_text
    ,group_concat(type, ', ') AS type_list
FROM ast_tree
WHERE 
	version = (SELECT max(version) FROM ast_tree)
	AND type NOT IN ('CompilationUnitImpl')
GROUP BY file_path, line
ORDER BY file_path, line, parent_id, node_id
;

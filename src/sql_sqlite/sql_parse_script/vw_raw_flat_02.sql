DROP VIEW IF EXISTS vw_raw_flat_02;

CREATE VIEW vw_raw_flat_02 AS
WITH RECURSIVE parse_tree(
    project_name,
    version,
    file_path,
    json_node_content,
    node_id,
    node_linha,
    node_linha_pai,
    node_string,
    node_tipo_string,
    node_string_lenght,
    node_coluna
) AS (
    -- Base case: Iterate over the top-level array in json_data
    SELECT
        fs.project_name,
        fs.version,
        fs.file_path,
        json_each.value, -- Each element of the top-level array
        NULL, -- node_id, not present in the current schema
        json_extract(json_each.value, '$.linha'),
        json_extract(json_each.value, '$.linhaPai'),
        json_extract(json_each.value, '$.string'),
        json_extract(json_each.value, '$.tipoString'),
        json_extract(json_each.value, '$.stringLenght'),
        json_extract(json_each.value, '$.coluna')
    FROM flutter_script AS fs, json_each(fs.json_data)
    WHERE
        -- For testing, using a specific file path
        fs.file_path = 'lib\supabase_service.dart'
    UNION ALL
    -- Recursive step: Iterate over the 'strings' array within each json_node_content
    SELECT
        pt.project_name,
        pt.version,
        pt.file_path,
        json_each_strings.value, -- Each element of the 'strings' array
        NULL, -- node_id
        json_extract(json_each_strings.value, '$.linha'),
        json_extract(json_each_strings.value, '$.linhaPai'),
        json_extract(json_each_strings.value, '$.string'),
        json_extract(json_each_strings.value, '$.tipoString'),
        json_extract(json_each_strings.value, '$.stringLenght'),
        json_extract(json_each_strings.value, '$.coluna')
    FROM
        parse_tree AS pt,
        json_each(pt.json_node_content, '$.strings') AS json_each_strings
)
SELECT
    project_name,
    version,
    file_path,
    node_id,
    node_linha,
    node_linha_pai,
    node_string,
    node_tipo_string,
    node_string_lenght,
    node_coluna
FROM
    parse_tree
ORDER BY
    node_linha;

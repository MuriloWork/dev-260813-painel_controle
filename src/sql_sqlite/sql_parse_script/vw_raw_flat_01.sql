DROP VIEW IF EXISTS vw_raw_flat_01;
CREATE VIEW vw_raw_flat_01 AS

SELECT *
-- SELECT count(*)

FROM (
    SELECT 
        project_name
        ,version
        ,folder_path
        ,file_path
        ,json_extract(json_each_00.value, '$.length') AS length
        ,CAST(json_extract(json_each_00.value, '$.line') AS INTEGER) AS line
        ,json_extract(json_each_00.value, '$.column') AS column
        ,json_extract(json_each_00.value, '$.script_string') AS string
        ,json_extract(json_each_00.value, '$.comment') AS comment
        ,json_extract(json_each_00.value, '$.tag') AS tag
    FROM 
        raw_script
        ,json_each(raw_script.json_data) AS json_each_00
) AS r
-- SELECT 
    -- 	count(*),
WHERE 
    version = (SELECT max(version) FROM raw_script)
--    AND r.file_path = 'posts_service_post.dart'
ORDER BY
    file_path
    ,line
;

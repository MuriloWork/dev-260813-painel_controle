DROP VIEW IF EXISTS vw_md_ast_code;
CREATE VIEW IF NOT EXISTS vw_md_ast_code AS
WITH extracted AS (
    SELECT
        c.file_path,
        CAST(json_extract(value, '$.start_line') AS INTEGER) AS start_line,
        json_extract(value, '$.type') AS type,
        CAST(NULLIF(json_extract(value, '$.depth'), 0) AS INTEGER) AS depth,
        json_extract(value, '$.h1') AS section_01,
        json_extract(value, '$.h2') AS section_02,
        json_extract(value, '$.h3') AS section_03,
        json_extract(value, '$.h4') AS section_04,
        json_extract(value, '$.h5') AS section_05,
        json_extract(value, '$.h6') AS section_06,
        COALESCE(NULLIF(json_extract(value, '$.lang'), ''), '(sem tag)') AS lang,
        json_extract(value, '$.value') AS value
    FROM tb_json_md_ast_code c,
         json_each(c.json_data) AS j
),
hierarquia AS (
    SELECT
        *,
        CASE WHEN INSTR(section_03, 'script ') > 0 THEN SUBSTR(section_03, INSTR(section_03, 'script ') + 7)
             WHEN INSTR(section_02, 'script ') > 0 THEN SUBSTR(section_02, INSTR(section_02, 'script ') + 7)
             WHEN INSTR(section_04, 'script ') > 0 THEN SUBSTR(section_04, INSTR(section_04, 'script ') + 7)
             WHEN INSTR(section_01, 'script ') > 0 THEN SUBSTR(section_01, INSTR(section_01, 'script ') + 7)
             WHEN INSTR(section_05, 'script ') > 0 THEN SUBSTR(section_05, INSTR(section_05, 'script ') + 7)
             WHEN INSTR(section_06, 'script ') > 0 THEN SUBSTR(section_06, INSTR(section_06, 'script ') + 7)
             ELSE ''
        END AS script,
        CASE WHEN INSTR(section_04, 'classe ') > 0 AND INSTR(section_04, '[') > 0
             THEN TRIM(SUBSTR(section_04, INSTR(section_04, 'classe ') + 7, INSTR(section_04, '[') - INSTR(section_04, 'classe ') - 7))
             WHEN INSTR(section_03, 'classe ') > 0 AND INSTR(section_03, '[') > 0
             THEN TRIM(SUBSTR(section_03, INSTR(section_03, 'classe ') + 7, INSTR(section_03, '[') - INSTR(section_03, 'classe ') - 7))
             WHEN INSTR(section_05, 'classe ') > 0 AND INSTR(section_05, '[') > 0
             THEN TRIM(SUBSTR(section_05, INSTR(section_05, 'classe ') + 7, INSTR(section_05, '[') - INSTR(section_05, 'classe ') - 7))
             WHEN INSTR(section_02, 'classe ') > 0 AND INSTR(section_02, '[') > 0
             THEN TRIM(SUBSTR(section_02, INSTR(section_02, 'classe ') + 7, INSTR(section_02, '[') - INSTR(section_02, 'classe ') - 7))
             WHEN INSTR(section_06, 'classe ') > 0 AND INSTR(section_06, '[') > 0
             THEN TRIM(SUBSTR(section_06, INSTR(section_06, 'classe ') + 7, INSTR(section_06, '[') - INSTR(section_06, 'classe ') - 7))
             WHEN INSTR(section_01, 'classe ') > 0 AND INSTR(section_01, '[') > 0
             THEN TRIM(SUBSTR(section_01, INSTR(section_01, 'classe ') + 7, INSTR(section_01, '[') - INSTR(section_01, 'classe ') - 7))
             ELSE ''
        END AS classe,
        CASE WHEN INSTR(section_04, 'classe ') > 0 AND INSTR(section_04, '[') > 0 AND INSTR(section_04, ']') > 0
             THEN SUBSTR(section_04, INSTR(section_04, '[') + 1, INSTR(section_04, ']') - INSTR(section_04, '[') - 1)
             WHEN INSTR(section_03, 'classe ') > 0 AND INSTR(section_03, '[') > 0 AND INSTR(section_03, ']') > 0
             THEN SUBSTR(section_03, INSTR(section_03, '[') + 1, INSTR(section_03, ']') - INSTR(section_03, '[') - 1)
             WHEN INSTR(section_05, 'classe ') > 0 AND INSTR(section_05, '[') > 0 AND INSTR(section_05, ']') > 0
             THEN SUBSTR(section_05, INSTR(section_05, '[') + 1, INSTR(section_05, ']') - INSTR(section_05, '[') - 1)
             WHEN INSTR(section_02, 'classe ') > 0 AND INSTR(section_02, '[') > 0 AND INSTR(section_02, ']') > 0
             THEN SUBSTR(section_02, INSTR(section_02, '[') + 1, INSTR(section_02, ']') - INSTR(section_02, '[') - 1)
             WHEN INSTR(section_06, 'classe ') > 0 AND INSTR(section_06, '[') > 0 AND INSTR(section_06, ']') > 0
             THEN SUBSTR(section_06, INSTR(section_06, '[') + 1, INSTR(section_06, ']') - INSTR(section_06, '[') - 1)
             WHEN INSTR(section_01, 'classe ') > 0 AND INSTR(section_01, '[') > 0 AND INSTR(section_01, ']') > 0
             THEN SUBSTR(section_01, INSTR(section_01, '[') + 1, INSTR(section_01, ']') - INSTR(section_01, '[') - 1)
             ELSE ''
        END AS tag_classe
    FROM extracted
)
SELECT * FROM hierarquia
ORDER BY file_path, section_01, section_02, section_03, section_04, section_05, section_06, start_line;

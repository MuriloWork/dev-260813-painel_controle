DROP VIEW IF EXISTS vw_widget;
CREATE VIEW vw_widget AS

SELECT *
-- SELECT count(*), *

FROM (

    SELECT 
        project_name
        ,version
        ,file_path
        ,json_extract(json_each_00.value, '$.description') AS description_00
        ,json_extract(json_each_00.value, '$.widgetRuntimeType') AS type_00
        ,NULL AS description_01
        ,NULL AS type_01
        ,NULL AS description_02
        ,NULL AS type_02
        ,NULL AS description_03
        ,NULL AS type_03
        ,NULL AS description_04
        ,NULL AS type_04
        ,NULL AS description_05
        ,NULL AS type_05
        ,NULL AS description_06
        ,NULL AS type_06
        ,NULL AS description_07
        ,NULL AS type_07
        ,NULL AS description_08
        ,NULL AS type_08
        ,NULL AS description_09
        ,NULL AS type_09
        ,NULL AS description_10
        ,NULL AS type_10
        ,NULL AS description_11
        ,NULL AS type_11
        ,NULL AS description_12
        ,NULL AS type_12
        ,NULL AS description_13
        ,NULL AS type_13
        ,NULL AS description_14
        ,NULL AS type_14
    FROM 
        widget
        ,json_each(widget.json_data, '$.children') AS json_each_00
        -- ,json_each(json_tree_00.value, '$.children') AS json_each_00
    UNION
    SELECT 
        project_name
        ,version
        ,file_path
        ,json_extract(json_each_00.value, '$.description') AS description_00
        ,json_extract(json_each_00.value, '$.widgetRuntimeType') AS type_00
        ,json_extract(json_each_01.value, '$.description') AS description_01
        ,json_extract(json_each_01.value, '$.widgetRuntimeType') AS type_01
        ,NULL AS description_02
        ,NULL AS type_02
        ,NULL AS description_03
        ,NULL AS type_03
        ,NULL AS description_04
        ,NULL AS type_04
        ,NULL AS description_05
        ,NULL AS type_05
        ,NULL AS description_06
        ,NULL AS type_06
        ,NULL AS description_07
        ,NULL AS type_07
        ,NULL AS description_08
        ,NULL AS type_08
        ,NULL AS description_09
        ,NULL AS type_09
        ,NULL AS description_10
        ,NULL AS type_10
        ,NULL AS description_11
        ,NULL AS type_11
        ,NULL AS description_12
        ,NULL AS type_12
        ,NULL AS description_13
        ,NULL AS type_13
        ,NULL AS description_14
        ,NULL AS type_14
    FROM 
        widget
        ,json_each(widget.json_data, '$.children') AS json_each_00
    LEFT JOIN
        json_each(json_each_00.value, '$.children') AS json_each_01
    UNION
    SELECT 
        project_name
        ,version
        ,file_path
        ,json_extract(json_each_00.value, '$.description') AS description_00
        ,json_extract(json_each_00.value, '$.widgetRuntimeType') AS type_00
        ,json_extract(json_each_01.value, '$.description') AS description_01
        ,json_extract(json_each_01.value, '$.widgetRuntimeType') AS type_01
        ,json_extract(json_each_02.value, '$.description') AS description_02
        ,json_extract(json_each_02.value, '$.widgetRuntimeType') AS type_02
        ,NULL AS description_03
        ,NULL AS type_03
        ,NULL AS description_04
        ,NULL AS type_04
        ,NULL AS description_05
        ,NULL AS type_05
        ,NULL AS description_06
        ,NULL AS type_06
        ,NULL AS description_07
        ,NULL AS type_07
        ,NULL AS description_08
        ,NULL AS type_08
        ,NULL AS description_09
        ,NULL AS type_09
        ,NULL AS description_10
        ,NULL AS type_10
        ,NULL AS description_11
        ,NULL AS type_11
        ,NULL AS description_12
        ,NULL AS type_12
        ,NULL AS description_13
        ,NULL AS type_13
        ,NULL AS description_14
        ,NULL AS type_14
    FROM 
        widget
        ,json_each(widget.json_data, '$.children') AS json_each_00
    LEFT JOIN
        json_each(json_each_00.value, '$.children') AS json_each_01
    LEFT JOIN
        json_each(json_each_01.value, '$.children') AS json_each_02
    UNION
    SELECT 
        project_name
        ,version
        ,file_path
        ,json_extract(json_each_00.value, '$.description') AS description_00
        ,json_extract(json_each_00.value, '$.widgetRuntimeType') AS type_00
        ,json_extract(json_each_01.value, '$.description') AS description_01
        ,json_extract(json_each_01.value, '$.widgetRuntimeType') AS type_01
        ,json_extract(json_each_02.value, '$.description') AS description_02
        ,json_extract(json_each_02.value, '$.widgetRuntimeType') AS type_02
        ,json_extract(json_each_03.value, '$.description') AS description_03
        ,json_extract(json_each_03.value, '$.widgetRuntimeType') AS type_03
        ,NULL AS description_04
        ,NULL AS type_04
        ,NULL AS description_05
        ,NULL AS type_05
        ,NULL AS description_06
        ,NULL AS type_06
        ,NULL AS description_07
        ,NULL AS type_07
        ,NULL AS description_08
        ,NULL AS type_08
        ,NULL AS description_09
        ,NULL AS type_09
        ,NULL AS description_10
        ,NULL AS type_10
        ,NULL AS description_11
        ,NULL AS type_11
        ,NULL AS description_12
        ,NULL AS type_12
        ,NULL AS description_13
        ,NULL AS type_13
        ,NULL AS description_14
        ,NULL AS type_14
    FROM 
        widget
        ,json_each(widget.json_data, '$.children') AS json_each_00
    LEFT JOIN
        json_each(json_each_00.value, '$.children') AS json_each_01
    LEFT JOIN
        json_each(json_each_01.value, '$.children') AS json_each_02
    LEFT JOIN
        json_each(json_each_02.value, '$.children') AS json_each_03
    UNION
    SELECT 
        project_name
        ,version
        ,file_path
        ,json_extract(json_each_00.value, '$.description') AS description_00
        ,json_extract(json_each_00.value, '$.widgetRuntimeType') AS type_00
        ,json_extract(json_each_01.value, '$.description') AS description_01
        ,json_extract(json_each_01.value, '$.widgetRuntimeType') AS type_01
        ,json_extract(json_each_02.value, '$.description') AS description_02
        ,json_extract(json_each_02.value, '$.widgetRuntimeType') AS type_02
        ,json_extract(json_each_03.value, '$.description') AS description_03
        ,json_extract(json_each_03.value, '$.widgetRuntimeType') AS type_03
        ,json_extract(json_each_04.value, '$.description') AS description_04
        ,json_extract(json_each_04.value, '$.widgetRuntimeType') AS type_04
        ,NULL AS description_05
        ,NULL AS type_05
        ,NULL AS description_06
        ,NULL AS type_06
        ,NULL AS description_07
        ,NULL AS type_07
        ,NULL AS description_08
        ,NULL AS type_08
        ,NULL AS description_09
        ,NULL AS type_09
        ,NULL AS description_10
        ,NULL AS type_10
        ,NULL AS description_11
        ,NULL AS type_11
        ,NULL AS description_12
        ,NULL AS type_12
        ,NULL AS description_13
        ,NULL AS type_13
        ,NULL AS description_14
        ,NULL AS type_14
    FROM 
        widget
        ,json_each(widget.json_data, '$.children') AS json_each_00
    LEFT JOIN
        json_each(json_each_00.value, '$.children') AS json_each_01
    LEFT JOIN
        json_each(json_each_01.value, '$.children') AS json_each_02
    LEFT JOIN
        json_each(json_each_02.value, '$.children') AS json_each_03
    LEFT JOIN
        json_each(json_each_03.value, '$.children') AS json_each_04
    UNION
    SELECT 
        project_name
        ,version
        ,file_path
        ,json_extract(json_each_00.value, '$.description') AS description_00
        ,json_extract(json_each_00.value, '$.widgetRuntimeType') AS type_00
        ,json_extract(json_each_01.value, '$.description') AS description_01
        ,json_extract(json_each_01.value, '$.widgetRuntimeType') AS type_01
        ,json_extract(json_each_02.value, '$.description') AS description_02
        ,json_extract(json_each_02.value, '$.widgetRuntimeType') AS type_02
        ,json_extract(json_each_03.value, '$.description') AS description_03
        ,json_extract(json_each_03.value, '$.widgetRuntimeType') AS type_03
        ,json_extract(json_each_04.value, '$.description') AS description_04
        ,json_extract(json_each_04.value, '$.widgetRuntimeType') AS type_04
        ,json_extract(json_each_05.value, '$.description') AS description_05
        ,json_extract(json_each_05.value, '$.widgetRuntimeType') AS type_05
        ,NULL AS description_06
        ,NULL AS type_06
        ,NULL AS description_07
        ,NULL AS type_07
        ,NULL AS description_08
        ,NULL AS type_08
        ,NULL AS description_09
        ,NULL AS type_09
        ,NULL AS description_10
        ,NULL AS type_10
        ,NULL AS description_11
        ,NULL AS type_11
        ,NULL AS description_12
        ,NULL AS type_12
        ,NULL AS description_13
        ,NULL AS type_13
        ,NULL AS description_14
        ,NULL AS type_14
    FROM 
        widget
        ,json_each(widget.json_data, '$.children') AS json_each_00
    LEFT JOIN
        json_each(json_each_00.value, '$.children') AS json_each_01
    LEFT JOIN
        json_each(json_each_01.value, '$.children') AS json_each_02
    LEFT JOIN
        json_each(json_each_02.value, '$.children') AS json_each_03
    LEFT JOIN
        json_each(json_each_03.value, '$.children') AS json_each_04
    LEFT JOIN
        json_each(json_each_04.value, '$.children') AS json_each_05
    UNION
    SELECT 
        project_name
        ,version
        ,file_path
        ,json_extract(json_each_00.value, '$.description') AS description_00
        ,json_extract(json_each_00.value, '$.widgetRuntimeType') AS type_00
        ,json_extract(json_each_01.value, '$.description') AS description_01
        ,json_extract(json_each_01.value, '$.widgetRuntimeType') AS type_01
        ,json_extract(json_each_02.value, '$.description') AS description_02
        ,json_extract(json_each_02.value, '$.widgetRuntimeType') AS type_02
        ,json_extract(json_each_03.value, '$.description') AS description_03
        ,json_extract(json_each_03.value, '$.widgetRuntimeType') AS type_03
        ,json_extract(json_each_04.value, '$.description') AS description_04
        ,json_extract(json_each_04.value, '$.widgetRuntimeType') AS type_04
        ,json_extract(json_each_05.value, '$.description') AS description_05
        ,json_extract(json_each_05.value, '$.widgetRuntimeType') AS type_05
        ,json_extract(json_each_06.value, '$.description') AS description_06
        ,json_extract(json_each_06.value, '$.widgetRuntimeType') AS type_06
        ,NULL AS description_07
        ,NULL AS type_07
        ,NULL AS description_08
        ,NULL AS type_08
        ,NULL AS description_09
        ,NULL AS type_09
        ,NULL AS description_10
        ,NULL AS type_10
        ,NULL AS description_11
        ,NULL AS type_11
        ,NULL AS description_12
        ,NULL AS type_12
        ,NULL AS description_13
        ,NULL AS type_13
        ,NULL AS description_14
        ,NULL AS type_14
    FROM 
        widget
        ,json_each(widget.json_data, '$.children') AS json_each_00
    LEFT JOIN
        json_each(json_each_00.value, '$.children') AS json_each_01
    LEFT JOIN
        json_each(json_each_01.value, '$.children') AS json_each_02
    LEFT JOIN
        json_each(json_each_02.value, '$.children') AS json_each_03
    LEFT JOIN
        json_each(json_each_03.value, '$.children') AS json_each_04
    LEFT JOIN
        json_each(json_each_04.value, '$.children') AS json_each_05
    LEFT JOIN
        json_each(json_each_05.value, '$.children') AS json_each_06
    UNION
    SELECT 
        project_name
        ,version
        ,file_path
        ,json_extract(json_each_00.value, '$.description') AS description_00
        ,json_extract(json_each_00.value, '$.widgetRuntimeType') AS type_00
        ,json_extract(json_each_01.value, '$.description') AS description_01
        ,json_extract(json_each_01.value, '$.widgetRuntimeType') AS type_01
        ,json_extract(json_each_02.value, '$.description') AS description_02
        ,json_extract(json_each_02.value, '$.widgetRuntimeType') AS type_02
        ,json_extract(json_each_03.value, '$.description') AS description_03
        ,json_extract(json_each_03.value, '$.widgetRuntimeType') AS type_03
        ,json_extract(json_each_04.value, '$.description') AS description_04
        ,json_extract(json_each_04.value, '$.widgetRuntimeType') AS type_04
        ,json_extract(json_each_05.value, '$.description') AS description_05
        ,json_extract(json_each_05.value, '$.widgetRuntimeType') AS type_05
        ,json_extract(json_each_06.value, '$.description') AS description_06
        ,json_extract(json_each_06.value, '$.widgetRuntimeType') AS type_06
        ,json_extract(json_each_07.value, '$.description') AS description_07
        ,json_extract(json_each_07.value, '$.widgetRuntimeType') AS type_07
        ,NULL AS description_08
        ,NULL AS type_08
        ,NULL AS description_09
        ,NULL AS type_09
        ,NULL AS description_10
        ,NULL AS type_10
        ,NULL AS description_11
        ,NULL AS type_11
        ,NULL AS description_12
        ,NULL AS type_12
        ,NULL AS description_13
        ,NULL AS type_13
        ,NULL AS description_14
        ,NULL AS type_14
    FROM 
        widget
        ,json_each(widget.json_data, '$.children') AS json_each_00
    LEFT JOIN
        json_each(json_each_00.value, '$.children') AS json_each_01
    LEFT JOIN
        json_each(json_each_01.value, '$.children') AS json_each_02
    LEFT JOIN
        json_each(json_each_02.value, '$.children') AS json_each_03
    LEFT JOIN
        json_each(json_each_03.value, '$.children') AS json_each_04
    LEFT JOIN
        json_each(json_each_04.value, '$.children') AS json_each_05
    LEFT JOIN
        json_each(json_each_05.value, '$.children') AS json_each_06
    LEFT JOIN
        json_each(json_each_06.value, '$.children') AS json_each_07
    UNION
    SELECT 
        project_name
        ,version
        ,file_path
        ,json_extract(json_each_00.value, '$.description') AS description_00
        ,json_extract(json_each_00.value, '$.widgetRuntimeType') AS type_00
        ,json_extract(json_each_01.value, '$.description') AS description_01
        ,json_extract(json_each_01.value, '$.widgetRuntimeType') AS type_01
        ,json_extract(json_each_02.value, '$.description') AS description_02
        ,json_extract(json_each_02.value, '$.widgetRuntimeType') AS type_02
        ,json_extract(json_each_03.value, '$.description') AS description_03
        ,json_extract(json_each_03.value, '$.widgetRuntimeType') AS type_03
        ,json_extract(json_each_04.value, '$.description') AS description_04
        ,json_extract(json_each_04.value, '$.widgetRuntimeType') AS type_04
        ,json_extract(json_each_05.value, '$.description') AS description_05
        ,json_extract(json_each_05.value, '$.widgetRuntimeType') AS type_05
        ,json_extract(json_each_06.value, '$.description') AS description_06
        ,json_extract(json_each_06.value, '$.widgetRuntimeType') AS type_06
        ,json_extract(json_each_07.value, '$.description') AS description_07
        ,json_extract(json_each_07.value, '$.widgetRuntimeType') AS type_07
        ,json_extract(json_each_08.value, '$.description') AS description_08
        ,json_extract(json_each_08.value, '$.widgetRuntimeType') AS type_08
        ,NULL AS description_09
        ,NULL AS type_09
        ,NULL AS description_10
        ,NULL AS type_10
        ,NULL AS description_11
        ,NULL AS type_11
        ,NULL AS description_12
        ,NULL AS type_12
        ,NULL AS description_13
        ,NULL AS type_13
        ,NULL AS description_14
        ,NULL AS type_14
    FROM 
        widget
        ,json_each(widget.json_data, '$.children') AS json_each_00
    LEFT JOIN
        json_each(json_each_00.value, '$.children') AS json_each_01
    LEFT JOIN
        json_each(json_each_01.value, '$.children') AS json_each_02
    LEFT JOIN
        json_each(json_each_02.value, '$.children') AS json_each_03
    LEFT JOIN
        json_each(json_each_03.value, '$.children') AS json_each_04
    LEFT JOIN
        json_each(json_each_04.value, '$.children') AS json_each_05
    LEFT JOIN
        json_each(json_each_05.value, '$.children') AS json_each_06
    LEFT JOIN
        json_each(json_each_06.value, '$.children') AS json_each_07
    LEFT JOIN
        json_each(json_each_07.value, '$.children') AS json_each_08
    UNION
    SELECT 
        project_name
        ,version
        ,file_path
        ,json_extract(json_each_00.value, '$.description') AS description_00
        ,json_extract(json_each_00.value, '$.widgetRuntimeType') AS type_00
        ,json_extract(json_each_01.value, '$.description') AS description_01
        ,json_extract(json_each_01.value, '$.widgetRuntimeType') AS type_01
        ,json_extract(json_each_02.value, '$.description') AS description_02
        ,json_extract(json_each_02.value, '$.widgetRuntimeType') AS type_02
        ,json_extract(json_each_03.value, '$.description') AS description_03
        ,json_extract(json_each_03.value, '$.widgetRuntimeType') AS type_03
        ,json_extract(json_each_04.value, '$.description') AS description_04
        ,json_extract(json_each_04.value, '$.widgetRuntimeType') AS type_04
        ,json_extract(json_each_05.value, '$.description') AS description_05
        ,json_extract(json_each_05.value, '$.widgetRuntimeType') AS type_05
        ,json_extract(json_each_06.value, '$.description') AS description_06
        ,json_extract(json_each_06.value, '$.widgetRuntimeType') AS type_06
        ,json_extract(json_each_07.value, '$.description') AS description_07
        ,json_extract(json_each_07.value, '$.widgetRuntimeType') AS type_07
        ,json_extract(json_each_08.value, '$.description') AS description_08
        ,json_extract(json_each_08.value, '$.widgetRuntimeType') AS type_08
        ,json_extract(json_each_09.value, '$.description') AS description_09
        ,json_extract(json_each_09.value, '$.widgetRuntimeType') AS type_09
        ,NULL AS description_10
        ,NULL AS type_10
        ,NULL AS description_11
        ,NULL AS type_11
        ,NULL AS description_12
        ,NULL AS type_12
        ,NULL AS description_13
        ,NULL AS type_13
        ,NULL AS description_14
        ,NULL AS type_14
    FROM 
        widget
        ,json_each(widget.json_data, '$.children') AS json_each_00
    LEFT JOIN
        json_each(json_each_00.value, '$.children') AS json_each_01
    LEFT JOIN
        json_each(json_each_01.value, '$.children') AS json_each_02
    LEFT JOIN
        json_each(json_each_02.value, '$.children') AS json_each_03
    LEFT JOIN
        json_each(json_each_03.value, '$.children') AS json_each_04
    LEFT JOIN
        json_each(json_each_04.value, '$.children') AS json_each_05
    LEFT JOIN
        json_each(json_each_05.value, '$.children') AS json_each_06
    LEFT JOIN
        json_each(json_each_06.value, '$.children') AS json_each_07
    LEFT JOIN
        json_each(json_each_07.value, '$.children') AS json_each_08
    LEFT JOIN
        json_each(json_each_08.value, '$.children') AS json_each_09
    UNION
    SELECT 
        project_name
        ,version
        ,file_path
        ,json_extract(json_each_00.value, '$.description') AS description_00
        ,json_extract(json_each_00.value, '$.widgetRuntimeType') AS type_00
        ,json_extract(json_each_01.value, '$.description') AS description_01
        ,json_extract(json_each_01.value, '$.widgetRuntimeType') AS type_01
        ,json_extract(json_each_02.value, '$.description') AS description_02
        ,json_extract(json_each_02.value, '$.widgetRuntimeType') AS type_02
        ,json_extract(json_each_03.value, '$.description') AS description_03
        ,json_extract(json_each_03.value, '$.widgetRuntimeType') AS type_03
        ,json_extract(json_each_04.value, '$.description') AS description_04
        ,json_extract(json_each_04.value, '$.widgetRuntimeType') AS type_04
        ,json_extract(json_each_05.value, '$.description') AS description_05
        ,json_extract(json_each_05.value, '$.widgetRuntimeType') AS type_05
        ,json_extract(json_each_06.value, '$.description') AS description_06
        ,json_extract(json_each_06.value, '$.widgetRuntimeType') AS type_06
        ,json_extract(json_each_07.value, '$.description') AS description_07
        ,json_extract(json_each_07.value, '$.widgetRuntimeType') AS type_07
        ,json_extract(json_each_08.value, '$.description') AS description_08
        ,json_extract(json_each_08.value, '$.widgetRuntimeType') AS type_08
        ,json_extract(json_each_09.value, '$.description') AS description_09
        ,json_extract(json_each_09.value, '$.widgetRuntimeType') AS type_09
        ,json_extract(json_each_10.value, '$.description') AS description_10
        ,json_extract(json_each_10.value, '$.widgetRuntimeType') AS type_10
        ,NULL AS description_11
        ,NULL AS type_11
        ,NULL AS description_12
        ,NULL AS type_12
        ,NULL AS description_13
        ,NULL AS type_13
        ,NULL AS description_14
        ,NULL AS type_14
    FROM 
        widget
        ,json_each(widget.json_data, '$.children') AS json_each_00
    LEFT JOIN
        json_each(json_each_00.value, '$.children') AS json_each_01
    LEFT JOIN
        json_each(json_each_01.value, '$.children') AS json_each_02
    LEFT JOIN
        json_each(json_each_02.value, '$.children') AS json_each_03
    LEFT JOIN
        json_each(json_each_03.value, '$.children') AS json_each_04
    LEFT JOIN
        json_each(json_each_04.value, '$.children') AS json_each_05
    LEFT JOIN
        json_each(json_each_05.value, '$.children') AS json_each_06
    LEFT JOIN
        json_each(json_each_06.value, '$.children') AS json_each_07
    LEFT JOIN
        json_each(json_each_07.value, '$.children') AS json_each_08
    LEFT JOIN
        json_each(json_each_08.value, '$.children') AS json_each_09
    LEFT JOIN
        json_each(json_each_09.value, '$.children') AS json_each_10
    UNION
    SELECT 
        project_name
        ,version
        ,file_path
        ,json_extract(json_each_00.value, '$.description') AS description_00
        ,json_extract(json_each_00.value, '$.widgetRuntimeType') AS type_00
        ,json_extract(json_each_01.value, '$.description') AS description_01
        ,json_extract(json_each_01.value, '$.widgetRuntimeType') AS type_01
        ,json_extract(json_each_02.value, '$.description') AS description_02
        ,json_extract(json_each_02.value, '$.widgetRuntimeType') AS type_02
        ,json_extract(json_each_03.value, '$.description') AS description_03
        ,json_extract(json_each_03.value, '$.widgetRuntimeType') AS type_03
        ,json_extract(json_each_04.value, '$.description') AS description_04
        ,json_extract(json_each_04.value, '$.widgetRuntimeType') AS type_04
        ,json_extract(json_each_05.value, '$.description') AS description_05
        ,json_extract(json_each_05.value, '$.widgetRuntimeType') AS type_05
        ,json_extract(json_each_06.value, '$.description') AS description_06
        ,json_extract(json_each_06.value, '$.widgetRuntimeType') AS type_06
        ,json_extract(json_each_07.value, '$.description') AS description_07
        ,json_extract(json_each_07.value, '$.widgetRuntimeType') AS type_07
        ,json_extract(json_each_08.value, '$.description') AS description_08
        ,json_extract(json_each_08.value, '$.widgetRuntimeType') AS type_08
        ,json_extract(json_each_09.value, '$.description') AS description_09
        ,json_extract(json_each_09.value, '$.widgetRuntimeType') AS type_09
        ,json_extract(json_each_10.value, '$.description') AS description_10
        ,json_extract(json_each_10.value, '$.widgetRuntimeType') AS type_10
        ,json_extract(json_each_11.value, '$.description') AS description_11
        ,json_extract(json_each_11.value, '$.widgetRuntimeType') AS type_11
        ,NULL AS description_12
        ,NULL AS type_12
        ,NULL AS description_13
        ,NULL AS type_13
        ,NULL AS description_14
        ,NULL AS type_14
    FROM 
        widget
        ,json_each(widget.json_data, '$.children') AS json_each_00
    LEFT JOIN
        json_each(json_each_00.value, '$.children') AS json_each_01
    LEFT JOIN
        json_each(json_each_01.value, '$.children') AS json_each_02
    LEFT JOIN
        json_each(json_each_02.value, '$.children') AS json_each_03
    LEFT JOIN
        json_each(json_each_03.value, '$.children') AS json_each_04
    LEFT JOIN
        json_each(json_each_04.value, '$.children') AS json_each_05
    LEFT JOIN
        json_each(json_each_05.value, '$.children') AS json_each_06
    LEFT JOIN
        json_each(json_each_06.value, '$.children') AS json_each_07
    LEFT JOIN
        json_each(json_each_07.value, '$.children') AS json_each_08
    LEFT JOIN
        json_each(json_each_08.value, '$.children') AS json_each_09
    LEFT JOIN
        json_each(json_each_09.value, '$.children') AS json_each_10
    LEFT JOIN
        json_each(json_each_10.value, '$.children') AS json_each_11
    UNION
    SELECT 
        project_name
        ,version
        ,file_path
        ,json_extract(json_each_00.value, '$.description') AS description_00
        ,json_extract(json_each_00.value, '$.widgetRuntimeType') AS type_00
        ,json_extract(json_each_01.value, '$.description') AS description_01
        ,json_extract(json_each_01.value, '$.widgetRuntimeType') AS type_01
        ,json_extract(json_each_02.value, '$.description') AS description_02
        ,json_extract(json_each_02.value, '$.widgetRuntimeType') AS type_02
        ,json_extract(json_each_03.value, '$.description') AS description_03
        ,json_extract(json_each_03.value, '$.widgetRuntimeType') AS type_03
        ,json_extract(json_each_04.value, '$.description') AS description_04
        ,json_extract(json_each_04.value, '$.widgetRuntimeType') AS type_04
        ,json_extract(json_each_05.value, '$.description') AS description_05
        ,json_extract(json_each_05.value, '$.widgetRuntimeType') AS type_05
        ,json_extract(json_each_06.value, '$.description') AS description_06
        ,json_extract(json_each_06.value, '$.widgetRuntimeType') AS type_06
        ,json_extract(json_each_07.value, '$.description') AS description_07
        ,json_extract(json_each_07.value, '$.widgetRuntimeType') AS type_07
        ,json_extract(json_each_08.value, '$.description') AS description_08
        ,json_extract(json_each_08.value, '$.widgetRuntimeType') AS type_08
        ,json_extract(json_each_09.value, '$.description') AS description_09
        ,json_extract(json_each_09.value, '$.widgetRuntimeType') AS type_09
        ,json_extract(json_each_10.value, '$.description') AS description_10
        ,json_extract(json_each_10.value, '$.widgetRuntimeType') AS type_10
        ,json_extract(json_each_11.value, '$.description') AS description_11
        ,json_extract(json_each_11.value, '$.widgetRuntimeType') AS type_11
        ,json_extract(json_each_12.value, '$.description') AS description_12
        ,json_extract(json_each_12.value, '$.widgetRuntimeType') AS type_12
        ,NULL AS description_13
        ,NULL AS type_13
        ,NULL AS description_14
        ,NULL AS type_14
    FROM 
        widget
        ,json_each(widget.json_data, '$.children') AS json_each_00
    LEFT JOIN
        json_each(json_each_00.value, '$.children') AS json_each_01
    LEFT JOIN
        json_each(json_each_01.value, '$.children') AS json_each_02
    LEFT JOIN
        json_each(json_each_02.value, '$.children') AS json_each_03
    LEFT JOIN
        json_each(json_each_03.value, '$.children') AS json_each_04
    LEFT JOIN
        json_each(json_each_04.value, '$.children') AS json_each_05
    LEFT JOIN
        json_each(json_each_05.value, '$.children') AS json_each_06
    LEFT JOIN
        json_each(json_each_06.value, '$.children') AS json_each_07
    LEFT JOIN
        json_each(json_each_07.value, '$.children') AS json_each_08
    LEFT JOIN
        json_each(json_each_08.value, '$.children') AS json_each_09
    LEFT JOIN
        json_each(json_each_09.value, '$.children') AS json_each_10
    LEFT JOIN
        json_each(json_each_10.value, '$.children') AS json_each_11
    LEFT JOIN
        json_each(json_each_11.value, '$.children') AS json_each_12
    UNION
    SELECT 
        project_name
        ,version
        ,file_path
        ,json_extract(json_each_00.value, '$.description') AS description_00
        ,json_extract(json_each_00.value, '$.widgetRuntimeType') AS type_00
        ,json_extract(json_each_01.value, '$.description') AS description_01
        ,json_extract(json_each_01.value, '$.widgetRuntimeType') AS type_01
        ,json_extract(json_each_02.value, '$.description') AS description_02
        ,json_extract(json_each_02.value, '$.widgetRuntimeType') AS type_02
        ,json_extract(json_each_03.value, '$.description') AS description_03
        ,json_extract(json_each_03.value, '$.widgetRuntimeType') AS type_03
        ,json_extract(json_each_04.value, '$.description') AS description_04
        ,json_extract(json_each_04.value, '$.widgetRuntimeType') AS type_04
        ,json_extract(json_each_05.value, '$.description') AS description_05
        ,json_extract(json_each_05.value, '$.widgetRuntimeType') AS type_05
        ,json_extract(json_each_06.value, '$.description') AS description_06
        ,json_extract(json_each_06.value, '$.widgetRuntimeType') AS type_06
        ,json_extract(json_each_07.value, '$.description') AS description_07
        ,json_extract(json_each_07.value, '$.widgetRuntimeType') AS type_07
        ,json_extract(json_each_08.value, '$.description') AS description_08
        ,json_extract(json_each_08.value, '$.widgetRuntimeType') AS type_08
        ,json_extract(json_each_09.value, '$.description') AS description_09
        ,json_extract(json_each_09.value, '$.widgetRuntimeType') AS type_09
        ,json_extract(json_each_10.value, '$.description') AS description_10
        ,json_extract(json_each_10.value, '$.widgetRuntimeType') AS type_10
        ,json_extract(json_each_11.value, '$.description') AS description_11
        ,json_extract(json_each_11.value, '$.widgetRuntimeType') AS type_11
        ,json_extract(json_each_12.value, '$.description') AS description_12
        ,json_extract(json_each_12.value, '$.widgetRuntimeType') AS type_12
        ,json_extract(json_each_13.value, '$.description') AS description_13
        ,json_extract(json_each_13.value, '$.widgetRuntimeType') AS type_13
        ,NULL AS description_14
        ,NULL AS type_14
    FROM 
        widget
        ,json_each(widget.json_data, '$.children') AS json_each_00
    LEFT JOIN
        json_each(json_each_00.value, '$.children') AS json_each_01
    LEFT JOIN
        json_each(json_each_01.value, '$.children') AS json_each_02
    LEFT JOIN
        json_each(json_each_02.value, '$.children') AS json_each_03
    LEFT JOIN
        json_each(json_each_03.value, '$.children') AS json_each_04
    LEFT JOIN
        json_each(json_each_04.value, '$.children') AS json_each_05
    LEFT JOIN
        json_each(json_each_05.value, '$.children') AS json_each_06
    LEFT JOIN
        json_each(json_each_06.value, '$.children') AS json_each_07
    LEFT JOIN
        json_each(json_each_07.value, '$.children') AS json_each_08
    LEFT JOIN
        json_each(json_each_08.value, '$.children') AS json_each_09
    LEFT JOIN
        json_each(json_each_09.value, '$.children') AS json_each_10
    LEFT JOIN
        json_each(json_each_10.value, '$.children') AS json_each_11
    LEFT JOIN
        json_each(json_each_11.value, '$.children') AS json_each_12
    LEFT JOIN
        json_each(json_each_12.value, '$.children') AS json_each_13
    UNION
    SELECT 
        project_name
        ,version
        ,file_path
        ,json_extract(json_each_00.value, '$.description') AS description_00
        ,json_extract(json_each_00.value, '$.widgetRuntimeType') AS type_00
        ,json_extract(json_each_01.value, '$.description') AS description_01
        ,json_extract(json_each_01.value, '$.widgetRuntimeType') AS type_01
        ,json_extract(json_each_02.value, '$.description') AS description_02
        ,json_extract(json_each_02.value, '$.widgetRuntimeType') AS type_02
        ,json_extract(json_each_03.value, '$.description') AS description_03
        ,json_extract(json_each_03.value, '$.widgetRuntimeType') AS type_03
        ,json_extract(json_each_04.value, '$.description') AS description_04
        ,json_extract(json_each_04.value, '$.widgetRuntimeType') AS type_04
        ,json_extract(json_each_05.value, '$.description') AS description_05
        ,json_extract(json_each_05.value, '$.widgetRuntimeType') AS type_05
        ,json_extract(json_each_06.value, '$.description') AS description_06
        ,json_extract(json_each_06.value, '$.widgetRuntimeType') AS type_06
        ,json_extract(json_each_07.value, '$.description') AS description_07
        ,json_extract(json_each_07.value, '$.widgetRuntimeType') AS type_07
        ,json_extract(json_each_08.value, '$.description') AS description_08
        ,json_extract(json_each_08.value, '$.widgetRuntimeType') AS type_08
        ,json_extract(json_each_09.value, '$.description') AS description_09
        ,json_extract(json_each_09.value, '$.widgetRuntimeType') AS type_09
        ,json_extract(json_each_10.value, '$.description') AS description_10
        ,json_extract(json_each_10.value, '$.widgetRuntimeType') AS type_10
        ,json_extract(json_each_11.value, '$.description') AS description_11
        ,json_extract(json_each_11.value, '$.widgetRuntimeType') AS type_11
        ,json_extract(json_each_12.value, '$.description') AS description_12
        ,json_extract(json_each_12.value, '$.widgetRuntimeType') AS type_12
        ,json_extract(json_each_13.value, '$.description') AS description_13
        ,json_extract(json_each_13.value, '$.widgetRuntimeType') AS type_13
        ,json_extract(json_each_14.value, '$.description') AS description_14
        ,json_extract(json_each_14.value, '$.widgetRuntimeType') AS type_14
    FROM 
        widget
        ,json_each(widget.json_data, '$.children') AS json_each_00
    LEFT JOIN
        json_each(json_each_00.value, '$.children') AS json_each_01
    LEFT JOIN
        json_each(json_each_01.value, '$.children') AS json_each_02
    LEFT JOIN
        json_each(json_each_02.value, '$.children') AS json_each_03
    LEFT JOIN
        json_each(json_each_03.value, '$.children') AS json_each_04
    LEFT JOIN
        json_each(json_each_04.value, '$.children') AS json_each_05
    LEFT JOIN
        json_each(json_each_05.value, '$.children') AS json_each_06
    LEFT JOIN
        json_each(json_each_06.value, '$.children') AS json_each_07
    LEFT JOIN
        json_each(json_each_07.value, '$.children') AS json_each_08
    LEFT JOIN
        json_each(json_each_08.value, '$.children') AS json_each_09
    LEFT JOIN
        json_each(json_each_09.value, '$.children') AS json_each_10
    LEFT JOIN
        json_each(json_each_10.value, '$.children') AS json_each_11
    LEFT JOIN
        json_each(json_each_11.value, '$.children') AS json_each_12
    LEFT JOIN
        json_each(json_each_12.value, '$.children') AS json_each_13
    LEFT JOIN
        json_each(json_each_13.value, '$.children') AS json_each_14
) AS r
-- SELECT 
--     	count(*)
-- FROM r
WHERE 
    r.version = 'summary'
    AND r.file_path = 'lib\screens\second_screen.dart'
	--   AND r.file_path = 'lib\screens\second_screen.dart'
    -- AND r.description_00 = 258
    -- 	AND type_02 = NULL
;
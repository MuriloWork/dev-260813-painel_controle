DROP TABLE IF EXISTS tb_vw_script_regex;
CREATE TABLE tb_vw_script_regex AS

SELECT
  rf.project_name
  ,rf.folder_path
  ,rf.file_path
  ,rf.length
  ,rf.line
  ,rf.column
  ,rf.string
  ,rf.comment
  ,rf.tag
  ,af.type_list AS ast_type
  ,(SELECT GROUP_CONCAT(rx2.tipo, ', ') FROM tb_dim_regex rx2 WHERE rx2.file_extension = 'dart' AND (rf.string REGEXP rx2.regex OR rf.comment REGEXP rx2.regex)) AS regex_tipo
  ,(SELECT GROUP_CONCAT(rx3.tag, ', ') FROM tb_dim_regex rx3 WHERE rx3.file_extension = 'dart' AND rf.string REGEXP rx3.regex) AS regex_tag
FROM
  vw_raw_flat_mu AS rf
  LEFT JOIN vw_ast_group af ON 
    rf.file_path = af.file_path 
    AND rf.line = af.line
GROUP BY
  rf.file_path
  ,rf.line
;
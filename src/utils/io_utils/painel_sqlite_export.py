import sqlite3
import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List

sys.path.insert(0, str(Path(__file__).parent.parent / 'init_utils'))
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'models'))
import painel_settings as ps
from export_model import FuncMap1DOutput, FuncMap2DOutput, FileOutput, FuncOutput, FuncVariable


def parse_func_1d(conn) -> Dict:
    """
    Converte os dados da view vw_ast_func_map_1d para o formato JSON correspondente.

    Args:
        conn: Conexão SQLite já estabelecida

    Returns:
        Dicionário contendo a estrutura JSON com dados e metadados
    """
    cursor = conn.cursor()
    cursor.execute("""
        SELECT file_path, ClassDeclarationImpl, MethodDeclarationImpl, VariableDeclarationImpl
        FROM tb_ast_func_map_1d
    """)

    rows = cursor.fetchall()

    files_dict: Dict[str, FileOutput] = {}

    for row in rows:
        file_path = row[0]
        method_name = row[2]
        variable_name = row[3]

        if file_path not in files_dict:
            files_dict[file_path] = FileOutput(file_name=file_path)

        file_out = files_dict[file_path]
        existing = [f for f in file_out.functions if f.function_name == method_name]

        if existing:
            existing[0].variables.append(FuncVariable(variable_name=variable_name))
        elif method_name:
            file_out.functions.append(FuncOutput(
                function_name=method_name,
                variables=[FuncVariable(variable_name=variable_name)] if variable_name else []
            ))

    result = FuncMap1DOutput(files=list(files_dict.values()))

    return result.model_dump(exclude_none=True)


def parse_func_2d(conn) -> Dict:
    """
    Converte os dados da view vw_ast_func_map_2d para o formato JSON correspondente.

    Args:
        conn: Conexão SQLite já estabelecida

    Returns:
        Dicionário contendo a estrutura JSON com dados e metadados
    """
    cursor = conn.cursor()
    cursor.execute("""
        SELECT file_path, ClassDeclarationImpl, MethodDeclarationImpl,
               VariableDeclarationImpl, max_count
        FROM tb_ast_func_map_2d
    """)

    rows = cursor.fetchall()

    files_dict: Dict[str, FileOutput] = {}

    for row in rows:
        file_path = row[0]
        method_name = row[2]
        variable_name = row[3]
        max_count = row[4]

        if file_path not in files_dict:
            files_dict[file_path] = FileOutput(file_name=file_path)

        file_out = files_dict[file_path]
        existing = [f for f in file_out.functions if f.function_name == method_name]

        if existing:
            existing[0].variables.append(FuncVariable(variable_name=variable_name, variable_count=max_count))
        elif method_name:
            file_out.functions.append(FuncOutput(
                function_name=method_name,
                variables=[FuncVariable(variable_name=variable_name, variable_count=max_count)] if variable_name else []
            ))

    result = FuncMap2DOutput(files=list(files_dict.values()))

    return result.model_dump()


def save_json(data: Dict, file_path: str) -> None:
    """
    Salva os dados JSON em arquivo específico.
    
    Args:
        data: Dados a serem salvos
        file_path: Caminho do arquivo de destino
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def main(selected_json: List[str]):
    """
    Função principal que coordena todo o processo de conversão.
    
    Args:
        selected_json: Lista indicando quais dados processar ([1d] ou [2d])
    """
    # Carregar variáveis de ambiente
    ps.load_environment_main()
    
    # Gerar timestamp para os nomes dos arquivos
    from datetime import datetime
    session_version = datetime.now().isoformat()
    timestamp_str = session_version.replace(':', '').replace('-', '')

    # Estabelecer conexão com o banco de dados SQLite
    sqlite_db_path = ps.DB_PARSE_DART
    conn = sqlite3.connect(sqlite_db_path)
    
    try:
        if "parse_func_1d" in selected_json:
            # Chamar parse_func_1d passando a conexão SQLite
            data_1d = parse_func_1d(conn)
            # Salvar em PJ_DIR_PARSE_JSON_FUNC com timestamp
            json_filename_1d = f"{timestamp_str}_srd_func_1d.json"
            output_path_1d = Path(ps.TARGET_DART_FUNC) / json_filename_1d
            save_json(data_1d, str(output_path_1d))
            print(f"Dados 1d salvos em: {output_path_1d}")
            
        if "parse_func_2d" in selected_json:
            # Chamar parse_func_2d passando a conexão SQLite
            data_2d = parse_func_2d(conn)
            # Salvar em PJ_DIR_PARSE_JSON_FUNC com timestamp
            json_filename_2d = f"{timestamp_str}_srd_func_2d.json"
            output_path_2d = Path(ps.TARGET_DART_FUNC) / json_filename_2d
            save_json(data_2d, str(output_path_2d))
            print(f"Dados 2d salvos em: {output_path_2d}")
            
    finally:
        # Fechar a conexão com o banco de dados SQLite
        conn.close()


if __name__ == "__main__":
    # Exemplo de uso
    main(["1d", "2d"])  # Processa ambos os tipos de dados


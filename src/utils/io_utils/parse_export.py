import os
import json
import sqlite3
import csv
from typing import Any, Type, Union, List as TypingList
from pydantic import BaseModel


def write_to_csv(data, csv_filepath):
    if not data:
        raise ValueError("No data to write to CSV.")

    fieldnames = [
        'project_name', 'version', 'folder_path', 'file_path', 'line', 'column',
        'script_string', 'comment', 'tag', 'length'
    ]

    try:
        with open(csv_filepath, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        raise RuntimeError(f"Erro ao escrever CSV '{csv_filepath}': {e}") from e

    return csv_filepath


def write_to_sqlite(data, sqlite_db_path, table_name):
    if not data:
        raise ValueError("No data to write to SQLite.")

    try:
        conn = sqlite3.connect(sqlite_db_path)
        cursor = conn.cursor()

        cursor.execute(f"DELETE FROM {table_name}")

        for item in data:
            cursor.execute(f"""
                INSERT INTO {table_name} (project_name, version, folder_path, file_path, json_data)
                VALUES (?, ?, ?, ?, ?)
            """, (item['project_name'], item['version'],
                  item['folder_path'], item['file_path'], item['json_data']))

        conn.commit()
        conn.close()
    except (sqlite3.Error, KeyError) as e:
        raise RuntimeError(f"Erro SQLite '{sqlite_db_path}': {e}") from e

    return sqlite_db_path


def write_to_json(data, json_filepath):
    if not data:
        raise ValueError("No data to write to JSON.")

    if not os.path.exists(os.path.dirname(json_filepath)):
        raise FileNotFoundError(
            f"Diretorio nao encontrado: {os.path.dirname(json_filepath)}")

    try:
        with open(json_filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        raise RuntimeError(f"Erro ao escrever JSON '{json_filepath}': {e}") from e

    return json_filepath


def validate_to_model(data: Any, model_class: Type[BaseModel]) -> Union[BaseModel, TypingList[BaseModel]]:
    if isinstance(data, list):
        return [model_class(**item) for item in data]
    return model_class(**data)

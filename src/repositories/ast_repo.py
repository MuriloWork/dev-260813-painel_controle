import json
import sqlite3
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional


def save_json_ast(data: List[Dict], output_dir: str, filename: str) -> str:
    output_path = Path(output_dir) / filename
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return str(output_path)


def load_json_ast(file_path: str) -> Optional[List[Dict]]:
    path = Path(file_path)
    if not path.exists():
        return None
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def upsert_sqlite(db_path: str, table_name: str, entries: List[Dict]) -> int:
    db = Path(db_path)
    db.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db))
    cursor = conn.cursor()

    count = 0
    for entry in entries:
        json_str = json.dumps(entry.get('json_data', entry), ensure_ascii=False)
        file_path = entry.get('file_path', '')
        cursor.execute(f"SELECT file_path FROM {table_name} WHERE file_path = ?", (file_path,))
        if cursor.fetchone():
            cursor.execute(f"""
                UPDATE {table_name} SET json_data = ?, version = ?,
                    project_name = ?, folder_path = ?, updated_at = CURRENT_TIMESTAMP
                WHERE file_path = ?
            """, (json_str, entry.get('version', ''), entry.get('project_name', ''),
                  entry.get('folder_path', ''), file_path))
        else:
            cursor.execute(f"""
                INSERT INTO {table_name} (project_name, version, folder_path, file_path, json_data)
                VALUES (?, ?, ?, ?, ?)
            """, (entry.get('project_name', ''), entry.get('version', ''),
                  entry.get('folder_path', ''), file_path, json_str))
        count += 1

    conn.commit()
    conn.close()
    return count

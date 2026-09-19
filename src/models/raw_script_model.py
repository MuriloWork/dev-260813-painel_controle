from pydantic import BaseModel
from typing import List, Optional


class RawScriptRow(BaseModel):
    line: int = 0
    column: int = 0
    script_string: str = ''
    comment: str = ''
    tag: str = ''
    length: int = 0

    model_config = {'populate_by_name': True}


class RawScriptEntry(BaseModel):
    project_name: str = ''
    version: str = ''
    folder_path: str = ''
    file_path: str = ''
    json_data: List[RawScriptRow] = []

    model_config = {'populate_by_name': True}

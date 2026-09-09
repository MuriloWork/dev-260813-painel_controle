from pydantic import BaseModel, RootModel
from typing import Dict, Optional, List


class MdAstField(BaseModel):
    type: str
    fields: Optional[Dict[str, str]] = None
    children: Optional[List['MdAstField']] = None


class MdAstModel(BaseModel):
    type: str = 'root'
    children: List[MdAstField] = []


class MdTypeMap(RootModel[Dict[str, Optional[str]]]):
    pass


class MdBlockRow(BaseModel):
    file_path: str = ''
    start_line: int = 0
    type: str = ''
    depth: int = 0
    h1: str = ''
    h2: str = ''
    h3: str = ''
    h4: str = ''
    h5: str = ''
    h6: str = ''
    value: str = ''

    model_config = {'populate_by_name': True}


class MdCodeRow(BaseModel):
    file_path: str = ''
    start_line: int = 0
    type: str = ''
    depth: int = 0
    h1: str = ''
    h2: str = ''
    h3: str = ''
    h4: str = ''
    h5: str = ''
    h6: str = ''
    lang: str = ''
    value: str = ''

    model_config = {'populate_by_name': True}


class MdTableRow(BaseModel):
    file_path: str = ''
    start_line: int = 0
    type: str = ''
    depth: int = 0
    row_index: int = 0
    cell_index: int = 0
    cell_type: str = ''
    h1: str = ''
    h2: str = ''
    h3: str = ''
    h4: str = ''
    h5: str = ''
    h6: str = ''
    value: str = ''

    model_config = {'populate_by_name': True}

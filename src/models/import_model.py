from pydantic import BaseModel, Field
from typing import Dict, List, Optional


class TagMapEntry(BaseModel):
    tag_name: str
    file_path: str
    class_name: Optional[str] = Field(None, alias='class')
    method_name: Optional[str] = Field(None, alias='method')
    log_name: Optional[str] = None
    placeholders_var_remove: Optional[List[str]] = Field(None, alias='placeholders_var_remove')

    model_config = {'populate_by_name': True}


class LogsStringEntry(BaseModel):
    log_name: str
    placeholders_var: Dict[str, str] = {}

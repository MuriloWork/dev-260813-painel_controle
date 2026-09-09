from pydantic import BaseModel
from typing import List, Optional


class FuncVariable(BaseModel):
    variable_name: Optional[str] = None
    variable_description: str = ''
    variable_count: Optional[int] = None


class FuncOutput(BaseModel):
    function_name: str
    function_description: str = ''
    variables: List[FuncVariable] = []


class FileOutput(BaseModel):
    file_name: str
    file_description: str = ''
    functions: List[FuncOutput] = []


class FuncMap1DOutput(BaseModel):
    files: List[FileOutput]


class FuncMap2DOutput(BaseModel):
    files: List[FileOutput]

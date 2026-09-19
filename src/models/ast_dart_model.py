from pydantic import BaseModel, Field
from typing import Optional, List, Any


class AstNode(BaseModel):
    type: str
    offset: int
    length: int
    line: int
    column: int
    source_text: str
    children: Optional[List['AstNode']] = None
    static_type: Optional[str] = Field(None, alias='staticType')
    name: Optional[str] = None
    method_name: Optional[str] = Field(None, alias='methodName')
    property_name: Optional[str] = Field(None, alias='propertyName')
    constructor_name: Optional[str] = Field(None, alias='constructorName')
    operator: Optional[str] = None
    return_type: Optional[str] = Field(None, alias='returnType')
    value: Optional[Any] = None

    model_config = {'populate_by_name': True}


class FlutterAppAst(BaseModel):
    id: Optional[int] = None
    project_name: str = ''
    version: str = ''
    folder_path: str = ''
    file_path: str = ''
    json_data: str = ''
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    model_config = {'populate_by_name': True}


class AstFuncMap1D(BaseModel):
    file_path: str
    class_declaration: Optional[str] = Field(None, alias='ClassDeclarationImpl')
    method_declaration: Optional[str] = Field(None, alias='MethodDeclarationImpl')
    variable_declaration: Optional[str] = Field(None, alias='VariableDeclarationImpl')


class AstFuncMap2D(BaseModel):
    file_path: str
    class_declaration: Optional[str] = Field(None, alias='ClassDeclarationImpl')
    method_declaration: Optional[str] = Field(None, alias='MethodDeclarationImpl')
    variable_declaration: Optional[str] = Field(None, alias='VariableDeclarationImpl')
    max_count: int = 0

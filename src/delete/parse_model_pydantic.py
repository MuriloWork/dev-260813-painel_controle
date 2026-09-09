import json
import os
import sys
import importlib.util
from typing import Dict, List, Optional, Union, Any, Type
from pathlib import Path
from pydantic import BaseModel, Field, ConfigDict, ValidationError, RootModel # Import ValidationError and RootModel

import utils
from utils import find_ast_json_files

# --- Schema Inference and Generation ---

def infer_json_schema(json_data: Union[Dict, List], current_inferred_schema: Optional[Dict[str, Dict[str, Any]]] = None, children_key: str = 'children', node_type_field: str = 'type') -> Dict[str, Dict[str, Any]]:
    """
    Recursively traverses the JSON data to infer a schema in an intermediate format.
    """
    inferred_schema = current_inferred_schema if current_inferred_schema is not None else {}

    def _recursive_infer(node_data: Union[Dict, List, Any]):
        if isinstance(node_data, list):
            for item in node_data:
                _recursive_infer(item)
            return

        if not isinstance(node_data, dict):
            return

        node_type = node_data.get(node_type_field)
        if not isinstance(node_type, str) or not node_type:
            node_type = 'GenericNode'

        if not node_type.isidentifier():
            node_type = f"Node_{node_type.replace('.', '_').replace('-', '_')}"

        if node_type not in inferred_schema:
            inferred_schema[node_type] = {}

        current_node_fields = inferred_schema[node_type]

        for key, value in node_data.items():
            if key not in current_node_fields:
                current_node_fields[key] = {'types': set(), 'is_list': False, 'optional': False}

            if value is None:
                current_node_fields[key]['optional'] = True
                continue

            field_info = current_node_fields[key]
            
            if isinstance(value, bool):
                field_info['types'].add('bool')
            elif isinstance(value, int):
                field_info['types'].add('int')
            elif isinstance(value, float):
                field_info['types'].add('float')
            elif isinstance(value, str):
                field_info['types'].add('str')
            elif isinstance(value, list):
                field_info['is_list'] = True
                # NOVO: Inferir tipos dos elementos da lista, especialmente se forem nós AST
                for item in value:
                    if isinstance(item, dict) and item.get(node_type_field):
                        # Se o item da lista tem um campo 'type', adicionamos esse tipo ao 'types' da lista pai
                        field_info['types'].add(item.get(node_type_field))
                    elif not isinstance(item, (dict, list)): # Tratar tipos primitivos dentro da lista
                         # Handle primitive types within lists
                        if isinstance(item, bool): field_info['types'].add('bool')
                        elif isinstance(item, int): field_info['types'].add('int')
                        elif isinstance(item, float): field_info['types'].add('float')
                        elif isinstance(item, str): field_info['types'].add('str')
                _recursive_infer(value) # Continuar recursão para itens da lista
            elif isinstance(value, dict):
                # It could be a node with a 'type' or just a generic dict
                if value.get(node_type_field):
                    field_info['types'].add(value.get(node_type_field))
                else:
                    field_info['types'].add('Dict[str, Any]')
                _recursive_infer(value)

    _recursive_infer(json_data)
    return inferred_schema

def finalize_schema(inferred_schema: Dict[str, Dict[str, Any]], children_key: str) -> Dict[str, Dict[str, Any]]:
    """
    Converts the intermediate schema into the final, simplified format with Pydantic type strings.
    """
    final_schema = {}
    all_node_types = set(inferred_schema.keys())

    for node_name, fields in inferred_schema.items():
        final_schema[node_name] = {}
        for field_name, field_info in fields.items():
            py_types = sorted([t for t in field_info['types'] if t is not None])
            
            # Sanitize types that are node references
            py_types = [f"Node_{t.replace('.', '_').replace('-', '_')}" if not t.isidentifier() else t for t in py_types]
            py_types = [t for t in py_types if t in all_node_types or t in ['str', 'int', 'float', 'bool', 'Dict[str, Any]', 'List[Any]']]


            if field_name == children_key and any(t in all_node_types for t in py_types):
                type_str = 'BaseASTNode'
            elif py_types:
                if len(py_types) > 1:
                    type_str = f"Union[{', '.join(sorted(list(set(py_types))))}]"
                else:
                    type_str = py_types[0]

            if field_info['is_list']:
                type_str = f'List[{type_str}]'

            if field_info['optional']:
                type_str = f'Optional[{type_str}]'

            final_schema[node_name][field_name] = type_str

    return final_schema

def generate_pydantic_code(schema: Dict[str, Dict[str, Any]]) -> str:
    """
    Generates the Pydantic models as a Python code string from the final schema.
    """
    model_names = sorted(schema.keys())
    
    code_lines_header = [
        "from __future__ import annotations",
        "import json",
        "import os",
        "from typing import Dict, List, Optional, Union, Any, Type, Callable",
        "from pydantic import BaseModel, Field, ConfigDict",
        ""
    ]

    # 1. Define BaseASTNode
    code_lines_base_node = [
        "",
        "# ================================================================",
        "# REGISTRY / DECORATOR",
        "# ================================================================",
        "AST_REGISTRY: Dict[str, Type['BaseASTNode']] = {}",
        "",
        "def register(cls: Type['BaseASTNode']) -> Type['BaseASTNode']:",
        "    \"\"\"Registra a classe no AST_REGISTRY usando o nome da classe como 'type'.\"\"\"",
        "    AST_REGISTRY[cls.__name__] = cls",
        "",
        "# ================================================================",
        "# BASE CLASS",
        "# ================================================================",
        "class BaseASTNode(BaseModel):",
        "    model_config = ConfigDict(extra='allow')",
        "    type: str",
        "",
        "    @classmethod",
        "    def model_validate(cls, data: Any) -> 'BaseASTNode':",
        "        \"\"\"",
        "        Router: cria a instância da subclasse correta baseada no campo `type`.",
        "        Também processa recursivamente 'children' se presente.",
        "        \"\"\"",
        "        if isinstance(data, BaseASTNode):",
        "            return data",
        "        if not isinstance(data, dict):",
        "            raise TypeError(f'Expected dict or BaseASTNode, got {type(data)!r}')",
        "        node_type = data.get('type')",
        "        if node_type is None:",
        "            raise ValueError(\"Missing 'type' in AST node data\")",
        "        impl = AST_REGISTRY.get(node_type)",
        "        if impl is None:",
        "            impl = cls",
        "        children = data.get('children')",
        "        if isinstance(children, list):",
        "            processed_children = []",
        "            for ch in children:",
        "                if isinstance(ch, dict):",
        "                    processed_children.append(BaseASTNode.model_validate(ch))",
        "                else:",
        "                    processed_children.append(ch)",
        "            data = dict(data)",
        "            data['children'] = processed_children",
        "        return impl(**data)",
        "",
        "    def to_dict(self) -> Dict[str, Any]:",
        "        \"\"\"Serializa recursivamente em dicionário (útil para debug).\"\"\"",
        "        out = self.model_dump(exclude_none=True)",
        "        if 'children' in out and isinstance(out['children'], list):",
        "            out['children'] = [",
        "                ch.to_dict() if isinstance(ch, BaseASTNode) else ch for ch in out['children']",
        "            ]",
        "        return out",
        "",
        "def load_ast_from_file(path: str) -> BaseASTNode:",
        "    with open(path, 'r', encoding='utf-8') as f:",
        "        data = json.load(f)",
        "    return BaseASTNode.model_validate(data)",
        ""
        ""
    ]

    # Store individual model definitions
    individual_model_definitions = []
    for node_name in model_names:
        fields = schema.get(node_name, {})
        
        individual_model_definitions.append(f"@register")
        individual_model_definitions.append(f"class {node_name}(BaseASTNode):")
        # individual_model_definitions.append(f"    model_config = ConfigDict(extra='allow')")
        
        if not fields:
            individual_model_definitions.append("    pass")
            individual_model_definitions.append("")
            continue

        for field_name, field_type_str in sorted(fields.items()):
            if field_name == 'type':
                continue
            
            default_value = "..."
            # Adjust type string for children to use AllASTNodes
            if field_name == 'children':
                field_type_str = f"List['BaseASTNode']"
                default_value = "Field(default_factory=list)"
            elif field_type_str == "Optional[List[AllASTNodes]]": # If it was previously inferred as such
                field_type_str = f"Optional[List['BaseASTNode']]"
                default_value = "Field(default_factory=list)"
            elif field_type_str.startswith("Optional["):
                default_value = "None"
            elif field_type_str.startswith("List["):
                default_value = "Field(default_factory=list)"
            else:
                default_value = "..." # For required fields

            field_name_sanitized = field_name
            alias = None
            if not field_name.isidentifier() or field_name in ['from']:
                alias = field_name
                field_name_sanitized = f"aliased_{field_name.replace('.', '_').replace('-', '_')}"
                if default_value == "...": # Required field with alias
                    default_value = f"Field(alias='{alias}')"
                else: # Optional or list field with alias
                    default_value = f"Field({default_value}, alias='{alias}')"
            elif alias is None and field_name != field_name_sanitized and default_value != "...":
                 default_value = f"Field({default_value}, alias='{field_name}')"
            elif alias is None and field_name != field_name_sanitized and default_value == "...":
                 default_value = f"Field(alias='{field_name}')"
            
            individual_model_definitions.append(f"    {field_name_sanitized}: {field_type_str} = {default_value}")
        
        individual_model_definitions.append("")

    # 3. Generate AllASTNodes = Union[...] after all concrete classes are defined -- NOT USED
    # all_ast_nodes_union_str = f"Union[{', '.join(f"'{name}'" for name in model_names)}]"
    # code_lines_all_ast_nodes_union = [
    #     f"AllASTNodes = {all_ast_nodes_union_str}",
    #     ""
    # ]

    # 4. Call model_rebuild() for all models -- NOT USED
    # code_lines_rebuild = []
    # for node_name in model_names:
    #     code_lines_rebuild.append(f"{node_name}.model_rebuild()")
        
    return "\n".join(code_lines_header + code_lines_base_node + individual_model_definitions)

def validate_json_with_pydantic(json_path: Optional[Path] = None, parsed_data: Optional[Union[Dict, List]] = None, pydantic_model_module: object = None) -> Union[BaseModel, List[BaseModel], None]:
    """
    Validates JSON data against a Pydantic model from a dynamically loaded module and returns the validated data.
    Can receive data either from a file path or as an already parsed Python object (dict or list).
    Leverages Pydantic's discriminator for efficient validation of polymorphic types.
    """
    if pydantic_model_module is None:
        print("AVISO: Módulo `pydantic_model` não foi carregado. Pulando validação.")
        return None
        
    # Get all Pydantic model classes from the dynamically loaded module
    all_pydantic_models = []
    for name in dir(pydantic_model_module):
        obj = getattr(pydantic_model_module, name)
        # Ensure it's a class, a subclass of BaseModel, not BaseModel itself, and not RootModel
        if isinstance(obj, type) and issubclass(obj, BaseModel) and obj not in [BaseModel, RootModel]:
            all_pydantic_models.append(obj)

    if not all_pydantic_models:
        print("ERRO DE VALIDAÇÃO: Nenhuma classe Pydantic encontrada no módulo gerado.")
        return None

    # Create a Union type for all possible AST nodes - NOT USED WITH NEW MODEL
    # AllASTNodes = getattr(pydantic_model_module, 'AllASTNodes', None)
    # if AllASTNodes is None:
        # print("ERRO DE VALIDAÇÃO: A classe 'AllASTNodes' não foi encontrada no módulo Pydantic gerado.")
        # return None

    BaseASTNode = getattr(pydantic_model_module, 'BaseASTNode', None)
    if BaseASTNode is None:
        print("ERRO DE VALIDAÇÃO: A classe 'BaseASTNode' não foi encontrada no módulo Pydantic gerado.")
        return None

    try:
        json_data = None
        data_source_description = "Dados JSON"

        if parsed_data is not None:
            json_data = parsed_data
            data_source_description = "Dados JSON parseados"
        elif json_path is not None:
            data_source_description = f"arquivo JSON {json_path.name}"
            with open(json_path, 'r', encoding='utf-8') as f:
                json_data = json.load(f)
        else:
            raise ValueError("Nenhum dado JSON ou caminho de arquivo fornecido para validação.")
        
        # The new BaseASTNode.model_validate handles both single objects and lists internally
        # It also handles the dynamic dispatch based on the 'type' field
        if isinstance(json_data, list):
            if not json_data:
                raise ValueError("JSON data is an empty list.")
            validated_data = [BaseASTNode.model_validate(item) for item in json_data]
            print(f"SUCESSO: {data_source_description} (lista) foram validados com sucesso usando o modelo BaseASTNode.")
            return validated_data
        else: # single object
            validated_data = BaseASTNode.model_validate(json_data)
            print(f"SUCESSO: {data_source_description} (objeto único) foram validados com sucesso usando o modelo BaseASTNode.")
            return validated_data
            
    except ValidationError as e:
        print(f"ERRO DE VALIDAÇÃO Pydantic: {data_source_description} falharam na validação: {e.errors()}")
        return None
    except Exception as e:
        import traceback
        print(f"ERRO DE VALIDAÇÃO: {data_source_description} falharam na validação: {e}")
        print(f"Tipo de Exceção: {type(e)}")
        print(f"Detalhes do Traceback:\n{traceback.format_exc()}")
        return None


def main():
    """
    Main function to run the schema inference, code generation, and validation.
    """
    pydantic_output_path = utils.PYDANTIC_OUTPUT_PATH
    children_key = 'children'
    node_type_field = 'type'
    ast_json_input_dir = utils.JSON_INPUT_DIR
    all_ast_json_files = utils.find_ast_json_files(ast_json_input_dir)

    if not all_ast_json_files:
        print(f"ERRO: Nenhum arquivo JSON de AST encontrado em {ast_json_input_dir}.")
        return

    # 1. Accumulate schema from all files
    print(f"DEBUG: Inferindo schema de {len(all_ast_json_files)} arquivos JSON de AST...")
    intermediate_schema = {}
    for json_file_path in all_ast_json_files:
        print(f"DEBUG: Processando arquivo: {json_file_path.name}")
        try:
            with open(json_file_path, 'r', encoding='utf-8') as f:
                json_data = json.load(f)
            intermediate_schema = infer_json_schema(json_data, intermediate_schema, children_key=children_key, node_type_field=node_type_field)
        except Exception as e:
            print(f"ERRO ao processar {json_file_path.name}: {e}")
            continue
    
    # 2. Finalize the accumulated schema
    final_schema = finalize_schema(intermediate_schema, children_key=children_key)

    # 3. Generate Pydantic code
    pydantic_code = generate_pydantic_code(final_schema)
    
    # 4. Write the generated code to file
    # os.makedirs(os.path.dirname(pydantic_output_path), exist_ok=True)
    with open(pydantic_output_path, 'w', encoding='utf-8') as f:
        f.write(pydantic_code)
    # print(f"Modelos Pydantic gerados e salvos em: {pydantic_output_path}")

    # 5. Dynamically load the generated module for validation
    loaded_pydantic_model_module = None # Renomeado para evitar conflito de escopo
    try:
        spec = importlib.util.spec_from_file_location("pydantic_model", pydantic_output_path)
        loaded_pydantic_model_module = importlib.util.module_from_spec(spec)
        sys.modules["pydantic_model"] = loaded_pydantic_model_module
        spec.loader.exec_module(loaded_pydantic_model_module)
    except Exception as e:
        print(f"ERRO: Não foi possível carregar dinamicamente o módulo gerado '{pydantic_output_path}': {e}")
        # Se o carregamento falhar, não podemos prosseguir com a validação
        return 

    # 6. Validate the main_dart.json file as a sample
    print("\n--- Iniciando Validação do JSON ---")
    json_to_validate_path = utils.JSON_INPUT_PATH
    if json_to_validate_path.exists():
        validate_json_with_pydantic(json_path=json_to_validate_path, pydantic_model_module=loaded_pydantic_model_module)
    else:
        print(f"AVISO: Arquivo de validação '{json_to_validate_path}' não encontrado.")

if __name__ == "__main__":
    main()


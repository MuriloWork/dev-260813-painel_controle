# dev/src/painel/services/utils_io/parse_utils.py
import os
import fnmatch


def _strip_globstar(pattern):
    """Remove leading **\\ or **/ do padrao."""
    p = pattern
    while p.startswith('**') and len(p) > 2 and p[2] in ('\\', '/'):
        p = p[3:]
    return p

def _match_component(rel, patterns):
    """True se qualquer componente do rel path casar com algum padrao (fnmatch)."""
    components = rel.split(os.sep)
    for pat in patterns:
        pp = _strip_globstar(pat)
        if any(fnmatch.fnmatch(c, pp) for c in components):
            return True
    return False

def _match_basename(rel, patterns):
    """True se o basename do arquivo casar com algum padrao (fnmatch)."""
    basename = os.path.basename(rel)
    for pat in patterns:
        pp = _strip_globstar(pat)
        if fnmatch.fnmatch(basename, pp):
            return True
    return False

def get_files_from_paths(
    paths,
    extensions=('.py', '.dart'),
    include_child_paths=None,
    include_child_globs=None,
    exclude_child_paths=None,
    exclude_child_globs=None,
):
    """
    Dado uma lista de paths de arquivos/diretorios, retorna lista de dicts
    com filepath absoluto, original_input_path e is_directory_input.

    Filtros aplicados em cada child file (nessa ordem):
    1. extensions — extensao deve estar na lista
    2. include_child_paths — se nao vazio, path relativo deve ter componente casando
    3. include_child_globs — se nao vazio, basename deve casar
    4. exclude_child_paths — se componente casar, exclui
    5. exclude_child_globs — se basename casar, exclui

    Padroes com prefixo **\\ ou **/ sao limpos antes da comparacao.
    """
    inc_paths = include_child_paths or []
    inc_globs = include_child_globs or []
    exc_paths = exclude_child_paths or []
    exc_globs = exclude_child_globs or []

    def _match_rel(abs_file, abs_parent):
        rel = os.path.relpath(abs_file, abs_parent)
        if inc_paths and not _match_component(rel, inc_paths):
            return False
        if inc_globs and not _match_basename(rel, inc_globs):
            return False
        if exc_paths and _match_component(rel, exc_paths):
            return False
        if exc_globs and _match_basename(rel, exc_globs):
            return False
        return True

    file_info_list = []
    for original_path_input in paths:
        abs_original_path = os.path.abspath(original_path_input)
        if os.path.isfile(abs_original_path):
            if abs_original_path.lower().endswith(extensions):
                if _match_rel(abs_original_path, abs_original_path):
                    file_info_list.append({
                        'filepath': abs_original_path,
                        'original_input_path': abs_original_path,
                        'is_directory_input': False
                    })
        elif os.path.isdir(abs_original_path):
            for root, _, files in os.walk(abs_original_path):
                for file in files:
                    full_file_path = os.path.join(root, file)
                    if full_file_path.lower().endswith(extensions):
                        if _match_rel(full_file_path, abs_original_path):
                            file_info_list.append({
                                'filepath': os.path.abspath(full_file_path),
                                'original_input_path': abs_original_path,
                                'is_directory_input': True
                            })
        else:
            print(f"Warning: Path '{original_path_input}' is neither a file nor a directory. Skipping.")

    parent_count = len(set(i['original_input_path'] for i in file_info_list))
    print(f"[SOURCES] {len(file_info_list)} file(s) em {parent_count} parent(s)")
    print(f"[EXTENSIONS] {extensions}")
    if inc_paths:   print(f"[INCLUDE_PATHS] {inc_paths}")
    if inc_globs:   print(f"[INCLUDE_GLOBS] {inc_globs}")
    if exc_paths:   print(f"[EXCLUDE_PATHS] {exc_paths}")
    if exc_globs:   print(f"[EXCLUDE_GLOBS] {exc_globs}")
    return file_info_list

def get_output_paths(filepath, original_input_path, is_directory_input):
    """
    Determines folder_path and file_path for output based on how the file was originally requested.
    """
    if is_directory_input:
        # If original input was a directory, folder_path is the absolute path of the requested directory
        folder_path = original_input_path
        # file_path is the relative path from the original input directory to the current file
        file_path = os.path.relpath(filepath, original_input_path)
    else:
        # If original input was a file, folder_path is the file's directory
        folder_path = os.path.dirname(filepath)
        # file_path is just the filename
        file_path = os.path.basename(filepath)
    return folder_path, file_path





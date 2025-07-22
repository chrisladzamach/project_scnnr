import os
import ast
from collections import defaultdict
from typing import Dict, List

def scan_files(base_path: str, extensions: List[str] = None) -> Dict[str, List[str]]:
  """
  Recorre el directorio y retorna archivos agrupados por extensión.
  Si se pasan extensiones, solo se consideran esas.
  """
  result = defaultdict(list)
  for root, _, files in os.walk(base_path):
    for file in files:
      ext = os.path.splitext(file)[1].lower()
      if extensions is None or ext in extensions:
        result[ext].append(os.path.join(root, file))
  return result


def count_files(file_dict: Dict[str, List[str]]) -> Dict[str, int]:
  """
  Cuenta cuántos archivos hay por extensión.
  """
  return {ext: len(paths) for ext, paths in file_dict.items()}

def get_total_file_count(file_dict: Dict[str, List[str]]) -> int:
  """
  Devuelve el total de archivos encontrados.
  """
  return sum(len(paths) for paths in file_dict.values())

def get_all_files_flat_list(file_dict: Dict[str, List[str]]) -> List[str]:
  """
  Devuelve todos los archivos en una sola lista.
  """
  all_files = []
  for file_list in file_dict.values():
    all_files.extend(file_list)
  return all_files

def get_files_by_keyword(files: List[str], keyword: str) -> List[str]:
  """
  Retorna archivos que contienen una palabra clave.
  """
  matched_files = []
  for path in files:
    try:
      with open(path, 'r', encoding='utf-8') as f:
        if keyword in f.read():
          matched_files.append(path)
    except Exception:
      continue
  return matched_files


def get_python_functions_by_name(files: List[str], name_fragment: str) -> Dict[str, List[str]]:
  """
  Busca definiciones de funciones que contengan cierto fragmento en el nombre.
  Retorna un diccionario con la ruta del archivo y las funciones encontradas.
  """
  result = {}

  for path in files:
    if not path.endswith('.py'):
      continue

    try:
      with open(path, 'r', encoding='utf-8') as f:
        tree = ast.parse(f.read(), filename=path)
        matches = [
          node.name for node in ast.walk(tree)
          if isinstance(node, ast.FunctionDef) and name_fragment in node.name
        ]
        if matches:
          result[path] = matches
    except Exception:
      continue

  return result

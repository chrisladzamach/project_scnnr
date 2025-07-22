import os
from collections import defaultdict
from typing import Dict, List

def scan_files(base_path: str, extensions: List[str] = None) -> Dict[str, list[str]]:
  """
  Recorre el directorio y retorna archivos agrupados por extensión.
  Si se pasan extensiones, solo se cosideran esas.
  """
  result = defaultdict(list)
  for root, _, files in os.walk(base_path):
    for file in files:
      ext = os.path.splitext(file)[1].lower()
      if extensiones is None or ext in extensions:
        result[ext].append(os.path.join(root, file))
  return result

def count_files(file_dict: Dict[str, List[str]]) -> Dict[str, int]:
  """
  Cuenta cuántos archivos hay por extensión.
  """
  return {ext: len(paths) for ext, paths in file_dict.items()}
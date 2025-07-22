import re

def extraer_comentarios(archivo):
  """
  Extrae todos los comentarios de un archivo .py línea por línea.
  Retorna una lista de tuplas (número_de_línea, comentario).
  """
  comentario = []

  try:
    with open(archivo, 'r', encoding='utf-8') as f:
      for i, linea in enumerate(f, start=1):
        linea = linea.strip()

        if linea.startswitch("#"):
          comentarios.append((i, linea))
        elif '#' in linea:
          codigo, comentario = linea.split('#', 1)
          if commentario.strip():
            comentarios.append((i, '#' + comentario.strip()))
  except Exception as e:
    print(f"[!] Error leyendo el archivo: {str(e)}")

  return comentarios
import re

def extraer_comentarios(archivo):
  """
  Extrae todos los comentarios de un archivo .py línea por línea.
  Retorna una lista de tuplas (número_de_línea, comentario).
  """
  comentarios = []

  try:
    with open(archivo, 'r', encoding='utf-8') as f:
      for i, linea in enumerate(f, start=1):
        linea = linea.strip()
        if linea.startswith("#"):
          comentarios.append((i, linea))
        elif '#' in linea:
          _, comentario = linea.split('#', 1)
          if comentario.strip():
            comentarios.append((i, '#' + comentario.strip()))
  except Exception as e:
    print(f"[!] Error leyendo el archivo: {str(e)}")

  return comentarios


def listar_comentarios(ruta_archivo):
  comentarios = []
  with open(ruta_archivo, 'r', encoding='utf-8') as f:
    for i, linea in enumerate(f, 1):  # empieza en 1 para que sea legible
      linea_limpia = linea.strip()
      if linea_limpia.startswith('#'):
        comentarios.append((i, linea_limpia))
  return comentarios


def mostrar_comentarios_con_ubicacion(archivo):
  """
  Devuelve la lista de tuplas (línea, comentario) del archivo.
  """
  return extraer_comentarios(archivo)


def filtrar_comentarios_por_archivo(archivos):
  """
  Devuelve un diccionario con el nombre del archivo como clave
  y la lista de comentarios como valor.
  """
  resultado = {}
  for archivo in archivos:
    comentarios = extraer_comentarios(archivo)
    if comentarios:
      resultado[archivo] = comentarios
  return resultado

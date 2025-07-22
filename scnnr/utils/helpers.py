import os

def es_archivo_valido(ruta, extensiones_permitidas):
  return os.path.isfile(ruta) and any(ruta.endswitch(ext) for ext in extensiones_permitidas)

def obtener_lineas(ruta_archivo):
  with open(ruta_archivo, "r", encoding="utf-8") as archivo:
    return archivo.readlines()

def guardar_lineas(ruta_archivo, linea):
  with open(ruta_archivo, "w", encoding="utf-8") as archivo:
    archivo.writelines(lineas)
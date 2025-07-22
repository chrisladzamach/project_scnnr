import os
from scnnr.auth import solicitar_contraseña
from ui.display import success, warning, error

def modificar_comentario(archivo, linea, nuevo_comentario):
  if not solicitar_contraseña():
    error("Contraseña incorrecta. No se realizaron cambios.")
    return

  try:
    with open(archivo, 'r', encoding='utf-8') as f:
      lineas = f.readlines()

    if linea < 1 or linea > len(lineas):
      error("Número de línea fuera de rango.")
      return

    anterior = lineas[linea - 1]
    lineas[linea - 1] = nuevo_comentario + '\n'

    with open(archivo, 'w', encoding='utf-8') as f:
      f.writelines(lineas)

    success(f"Comentario en la línea {linea} modificado con éxito.")
    print(f"Antes: {anterior.strip()}\nDespués: {nuevo_comentario}")
  except Exception as e:
    error(f"Error modificando el archivo: {str(e)}")

def eliminar_comentario(archivo, linea):
  if not solicitar_contraseña():
    error("Contraseña incorrecta. No se realizaron cambios.")
    return

  try:
    with open(archivo, 'r', encoding='utf-8') as f:
      lineas = f.readlines()

    if linea < 1 or linea > len(lineas):
      error("Número de línea fuera de rango.")
      return

    contenido = lineas[linea - 1].strip()
    lineas[linea - 1] = '\n'

    with open(archivo, 'w', encoding='utf-8') as f:
      f.writelines(lineas)

    success(f"Comentario en la línea {linea} eliminado.")
    print(f"Contenido eliminado: {contenido}")
  except Exception as e:
    error(f"Error eliminando comentario: {str(e)}")

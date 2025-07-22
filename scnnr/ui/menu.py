from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import radiolist_dialog
from ui.display import success, warning, error

def main_menu():
  while True:
    result = radiolist_dialog(
      title="SCNNR - Menú principa.",
      text="Seleccione una opción: ",
      values=[
        ("list_all", "Listar todos los comentarios del proyecto."),
        ("list_path", "Mostrar ruta y línea de comentarios."),
        ("edit_comment", "Modificar un comentario."),
        ("delete_comment", "Eliminar un comentario."),
        ("filter", "Filtrar por archivo o carpeta."),
        ("count_ext", "Contar archivos por extensión."),
        ("exit", "Salir del sistema.")
      ],
      style=None
    ).run()

    if result == "list_all":
      success("Función aún no implementada: Listar todos los archivos.")
    elif result == "list_path":
      warning("Función aún no implementada: Mostrar ruta y línea de comentario.")
    elif result == "edit_comment":
      warning("Función aún no implementada: Modificar un comentario.")
    elif result == "delete_comment":
      error("Función aún no implementada: Eliminar un comentario.")
    elif result == "filter":
      warning("Función aún no implementada: Filtar por archivo o carpeta.")
    elif result == "count_ext":
      warning("Función aún no implementada: Contar archivos por extensión.")
    elif result == "exit":
      print("\nSaliendo del sistema...")
      break
    else:
      error("Opción no reconocida o inexistente.")

from prompt_toolkit.shortcuts import radiolist_dialog
from ui.display import success, warning, error

def main_menu():
    while True:
        result = radiolist_dialog(
            title="SCNNR - Menú principal",
            text="Selecciona una opción:",
            values=[
                ("list_all", "Listar todos los comentarios del proyecto"),
                ("list_path", "Mostrar ruta y línea de los comentarios"),
                ("edit_comment", "Modificar un comentario"),
                ("delete_comment", "Eliminar un comentario"),
                ("filter", "Filtrar por archivo o carpeta"),
                ("count_ext", "Contar archivos por extensión"),
                ("exit", "Salir del programa"),
            ],
        ).run()

        if result is None:
            print("\nNo se seleccionó ninguna opción. Saliendo...\n")
            break

        if result == "list_all":
            success("Función aún no implementada: listar todos los comentarios.")
        elif result == "list_path":
            warning("Función aún no implementada: mostrar ruta y línea.")
        elif result == "edit_comment":
            warning("Función aún no implementada: editar comentarios.")
        elif result == "delete_comment":
            error("Función aún no implementada: eliminar comentarios.")
        elif result == "filter":
            warning("Función aún no implementada: filtrado.")
        elif result == "count_ext":
            warning("Función aún no implementada: conteo de extensiones.")
        elif result == "exit":
            print("\nSaliendo del sistema...\n")
            break
        else:
            error("Opción no reconocida o inexistente.")

import questionary
from ui.display import success, warning, error

def main_menu():
    while True:
        result = questionary.select(
            "Selecciona una opción:",
            choices=[
                "Listar todos los comentarios",
                "Mostrar ruta y línea",
                "Modificar un comentario",
                "Eliminar un comentario",
                "Filtrar por archivo o carpeta",
                "Contar archivos por extensión",
                "Salir"
            ]
        ).ask()

        if result == "Listar todos los comentarios":
            success("Función aún no implementada: listar todos los comentarios.")
        elif result == "Mostrar ruta y línea":
            warning("Función aún no implementada: mostrar ruta y línea.")
        elif result == "Modificar un comentario":
            warning("Función aún no implementada: editar comentarios.")
        elif result == "Eliminar un comentario":
            error("Función aún no implementada: eliminar comentarios.")
        elif result == "Filtrar por archivo o carpeta":
            warning("Función aún no implementada: filtrado.")
        elif result == "Contar archivos por extensión":
            warning("Función aún no implementada: conteo de extensiones.")
        elif result == "Salir":
            print("\nSaliendo del sistema...\n")
            break
        else:
            error("Opción no reconocida.")

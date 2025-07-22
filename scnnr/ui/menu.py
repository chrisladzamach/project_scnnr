from scnnr.auth import solicitar_contraseña
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
            success("Función aún no implementada: Listar todos los comentarios.")
        elif result == "Mostrar ruta y línea":
            warning("Función aún no implementada: Mostrar ruta y línea.")
        elif result == "Modificar un comentario":
            if solicitar_contraseña():
                warning("Función aún no implementada: Editar comentarios.")
            else:
                error("Acceso denegado.")
        elif result == "Eliminar un comentario":
            if solicitar_contraseña():
                warning("Función aún no implementada: Eliminar comentarios.")
            else:
                error("Acceso denegado.")
        elif result == "Filtrar por archivo o carpeta":
            success("Función aún no implementada: Filtrado.")
        elif result == "Contar archivos por extensión":
            success("Función aún no implementada: Conteo de extensiones.")
        elif result == "Salir":
            print("\nSaliendo del sistema...\n")
            break
        else:
            error("Opción no reconocida.")

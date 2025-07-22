from scnnr.auth import solicitar_contraseña
from scnnr.file_scanner import contar_archivos_por_extension
from scnnr.comment_parser import listar_comentarios, mostrar_comentarios_con_ubicacion, filtrar_comentarios_por_archivo
from scnnr.file_editor import modificar_comentario, eliminar_comentario
from ui.display import success, warning, error
import questionary

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
			comentarios = listar_comentarios()
			if comentarios:
				for comentario in comentarios:
					print(comentario)
				success(f"{len(comentario)} comentarios encontrados.")
			else: 
				error("No se encontraron comentarios.")
					
		elif result == "Mostrar ruta y línea":
			comentarios = mostrar_comentarios_con_ubicacion()
			if comentarios:
				for com in comentarios:
					print(f"{com['archivo']}:{com['linea']} -> {com['contenido']}")
				success(f"{len(comentarios)} comentarios con ubicación listados.")
			else:
				error("No se encontraron comentarios con ubicación.")

		elif result == "Modificar un comentario":
			if solicitar_contraseña():
				archivo = questionary.text("Ruta del archivo: ").ask()
				linea = int(questionary.text("Número de línea: ").ask())
				nuevo = questionary.text("Nuevo comentario: ").ask()
				if modificar_comentario(archivo, linea, nuevo):
					success("Comentario modificado con éxito.")
				else:
					error("No se pudo modificar el comentario.")
			else:
				error("Acceso denegado.")

		elif result == "Eliminar un comentario":
			if solicitar_contraseña():
				archivo = questionary.text("Ruta del archivo: ").ask()
				linea = int(questionary.text("Número de línea: ").ask())
				if eliminar_comentario(archivo, linea):
					success("Comentario eliminado con éxito.")
				else:
					error("No se pudo eliminar el comentario.")
			else:
				error("Acceso denegado.")

		elif result == "Filtrar por archivo o carpeta":
			ruta = questionary.text("Ruta del archivo o carpeta: ").ask()
			comentarios = filtrar_comentarios_por_archivo(ruta)
			if comentarios:
				for c in comentarios:
					print(f"{c['archivo']}:{c['linea']} -> {c['contenido']}")
				success(f"{len(comentarios)} comentarios filtrados.")
			else:
				error("No se encontraron comentarios en la ruta especificada.")

		elif result == "Contar archivos por extensión":
			ruta = questionary.text("Ruta base (por defecto .): ").ask() or "."
			conteo = contar_archivos_por_extension(ruta)
			if conteo:
				for ext, cantidad in conteo.items():
					print(f"{ext}: {cantidad}")
				success("Conteo completo.")
			else:
				error("No se encontraron archivos.")

		elif result == "Salir":
			print("\nSaliendo del sistema...\n")
			break
		else:
			error("Opción no reconocida.")

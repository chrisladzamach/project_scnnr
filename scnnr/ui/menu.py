from scnnr.auth import solicitar_contraseña
from scnnr.file_scanner import scan_files, count_files
from scnnr.comment_parser import listar_comentarios, mostrar_comentarios_con_ubicacion, filtrar_comentarios_por_archivo
from scnnr.file_editor import modificar_comentario, eliminar_comentario
from ui.display import success, warning, error
import questionary

#comentario de prueba

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
			archivo = questionary.text("Ruta del archivo .py: ").ask()
			comentarios = listar_comentarios(archivo)
			if comentarios:
				for linea, comentario in comentarios:
					print(f"[Línea {linea}] {comentario}")
				success(f"{len(comentarios)} comentarios encontrados.")
			else: 
				error("No se encontraron comentarios.")

		elif result == "Mostrar ruta y línea":
			ruta = questionary.text("Ruta base para buscar comentarios: ").ask() or "."
			comentarios = mostrar_comentarios_con_ubicacion(ruta)
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
				modificar_comentario(archivo, linea, nuevo)
			else:
				error("Acceso denegado.")

		elif result == "Eliminar un comentario":
			if solicitar_contraseña():
				archivo = questionary.text("Ruta del archivo: ").ask()
				linea = int(questionary.text("Número de línea: ").ask())
				eliminar_comentario(archivo, linea)
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
			file_dict = scan_files(ruta)
			conteo = count_files(file_dict)
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

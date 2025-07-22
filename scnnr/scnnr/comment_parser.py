import re
import os

def extraer_comentarios(ruta_archivo):
    comentarios = []
    extension = os.path.splitext(ruta_archivo)[1]

    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            lineas = f.readlines()
    except FileNotFoundError:
        print(f"Archivo no encontrado: {ruta_archivo}")
        return comentarios

    multilinea = False
    bloque_comentario = ''
    linea_inicio = 0

    for i, linea in enumerate(lineas, start=1):
        stripped = linea.strip()

        # Comentarios de Python
        if extension == '.py':
            if stripped.startswith('#'):
                comentarios.append({
                    'archivo': ruta_archivo,
                    'linea': i,
                    'contenido': stripped
                })
            continue  # No procesar reglas JS/TS para archivos .py

        # Comentario de una línea JS/TS
        if stripped.startswith('//'):
            comentarios.append({
                'archivo': ruta_archivo,
                'linea': i,
                'contenido': stripped
            })

        # Comentario en JSX: {/* comentario */}
        elif re.match(r'^\{\s*/\*.*\*/\s*\}$', stripped):
            comentarios.append({
                'archivo': ruta_archivo,
                'linea': i,
                'contenido': stripped
            })

        # Comentario de bloque en una línea
        elif '/*' in stripped and '*/' in stripped:
            comentarios.append({
                'archivo': ruta_archivo,
                'linea': i,
                'contenido': stripped
            })

        # Inicio de comentario multilínea
        elif '/*' in stripped:
            multilinea = True
            bloque_comentario = stripped
            linea_inicio = i

        elif '*/' in stripped and multilinea:
            bloque_comentario += '\n' + stripped
            comentarios.append({
                'archivo': ruta_archivo,
                'linea': linea_inicio,
                'contenido': bloque_comentario
            })
            multilinea = False
            bloque_comentario = ''

        elif multilinea:
            bloque_comentario += '\n' + stripped

    return comentarios


def listar_comentarios(ruta_archivo):
    """
    Devuelve comentarios (línea y contenido) para archivos .py solamente.
    """
    comentarios = []
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            for i, linea in enumerate(f, 1):
                linea_limpia = linea.strip()
                if linea_limpia.startswith('#'):
                    comentarios.append({
                        "linea": i,
                        "contenido": linea_limpia
                    })
    except Exception as e:
        print(f"[ERROR] {ruta_archivo}: {e}")
    return comentarios


def mostrar_comentarios_con_ubicacion(archivo):
    """
    Devuelve comentarios con línea, contenido y archivo.
    """
    return extraer_comentarios(archivo)


def filtrar_comentarios_por_archivo(archivos):
    """
    Devuelve todos los comentarios encontrados en los archivos especificados.
    """
    resultado = []
    for archivo in archivos:
        comentarios = extraer_comentarios(archivo)
        resultado.extend(comentarios)
    return resultado

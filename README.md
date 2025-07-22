# scnnr

`scnnr` es una herramienta de línea de comandos para escanear proyectos en busca de archivos, comentarios, y editar o eliminar contenido innecesario.

## Características

- Conteo de archivos por extensión
- Detección de comentarios en archivos fuente
- Eliminación de comentarios
- Autenticación por contraseña
- Interfaz por consola amigable

## Instalación

```bash
git clone https://github.com/tu_usuario/scnnr.git
cd scnnr
pip install -r requirements.txt


```bash
scnnr/
├── main.py
├── scnnr/
│   ├── auth.py
│   ├── comment_parser.py
│   ├── file_editor.py
│   └── ...
├── ui/
│   └── ...
├── utils/
│   └── ...
└── tests/

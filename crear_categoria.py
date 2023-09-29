from pathlib import Path

def crear_categoria(*args):
    nueva_categoria = args[0]
    ruta = args[1]
    nueva_categoria = nueva_categoria.strip()
    nueva_ruta = Path(ruta, nueva_categoria)
    try:
        nueva_ruta.mkdir()
    except FileExistsError:
        print("Carpeta con ese nombre ya existe")
    print("La categoria fue creada exitosamente")
    return "Creada"

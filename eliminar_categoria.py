from pathlib import Path
def eliminar_categoria(*args):
    categoria = args[0]
    ruta = args[1]
    nueva_ruta = Path(ruta, categoria)
    if not nueva_ruta.glob("**/*.txt"):
       nueva_ruta.rmdir()
       return "directorio vacio se elimina directorio"

    for recetas in nueva_ruta.iterdir():
        ruta_receta = Path(nueva_ruta, recetas.name)
        ruta_receta.unlink()
    nueva_ruta.rmdir()
    return "se ha eliminado correctamente"

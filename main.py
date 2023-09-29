from pathlib import Path
from os import system
from categorias import *
from crear_categoria import *

ruta = Path(Path.home(), "Recetas")
catidad_recetas = 0
for txt in ruta.glob("**/*.txt"):
    catidad_recetas = catidad_recetas + 1


print("Bienvenidos al recetario")
print(f"La ruta de acceso a la carpeta de recetas es: {ruta}")
print(f"La cantidad de recetas actuales son: {catidad_recetas}")
print("Tus opciones son")
print(""""
    [1] - Leer receta
    [2] - Crear receta
    [3] - Crear categoria
    [4] - Eliminar receta
    [5] - Eliminar Categoria
    [6] - Finalizar programa 
""")
opc = input("elige la opcion: ")
system("clear")

match opc:
    case "1":
        system("clear")
        categorias(ruta, "leer")
    case "2":
        # Uusrio creara reseta en la categoria deseada
        categorias(ruta, "crear")
    case "3":
        opc = input('Escribe el nombre de la categoria: ')
        crear_categoria(opc, ruta)
    case "4":
        #eliminar receta
        categorias(ruta, "eliminar")
    case "5":
        print('Eliminar categoria')
        categorias(ruta, "delcategoria")
    case "6":
        print('Hasta la proxima')
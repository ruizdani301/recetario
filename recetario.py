from pathlib import Path
from os import system

ruta = Path(Path.home(), "Recetas")
"""
recibe: ruta
muestra las categorias
"""
def categorias(*args):
    ruta = args[0]
    print("Las categorias son: ")
    c = 0
    dic = {}
    for txt in ruta.iterdir():
        c = c + 1
        print(f"{c}-> {txt.name}")
        dic[c] = txt.name

    opc = input("escoge el numero de la categoria: ")
    dic_opc = dic[int(opc)]
    if args[1] == "leer":
        receta(dic_opc, ruta)
    elif args[1] == "crear":
        nueva_receta = crear_receta(dic_opc, ruta)
        system("clear")
        print(nueva_receta)
    elif args[1] == "eliminar":
        system("clear")
        respuesta = eliminar_receta(dic_opc, ruta)
        print(respuesta)
    elif args[1] == "delcategoria":
        system("clear")
        respuesta = eliminar_categoria(dic_opc, ruta)
        print(respuesta)



"""
recibe: ruta
recibe: opcion de categoria
"""

def receta(*args):
    opc = args[0]
    ruta = args[1]
    nueva_ruta = Path(ruta, opc)
    print("las recetas de esta categoria son: ")
    c = 0
    dic_receta = {}
    for recetas in nueva_ruta.iterdir():
        c = c + 1
        print(f"{c}-> {recetas.name}")
        dic_receta[c] = recetas.name
    opc_receta = input("Elije la receta: ")
    ruta_receta = Path(nueva_ruta, dic_receta[int(opc_receta)])
    leer = open(ruta_receta)
    print(leer.read())
    leer.close()


"""
recibe : categoria
recibe : ruta
crea : archivo txt
"""
def crear_receta(*args):
    categoria = args[0]
    ruta = args[1]
    nueva_receta = input("Escribe e nombre de la nueva receta: ")
    nueva_receta = nueva_receta + ".txt"
    ruta_receta = Path(ruta, categoria, nueva_receta)
    crear_archivo = open(ruta_receta, 'a+')
    print(f"""se ha creado el archivo {nueva_receta} en la categoria {categoria},""")
    print("Presiona enter 2 veces seguidas para finalizar")
    texto = ""
    while True:
        linea = input("ahora escibe tu receta: ")
        if linea == "": # al presionar enter 2 veces aparece este caracter
            break
        texto += linea + "\n"
    print(texto)
    crear_archivo.writelines(texto)
    return f"""Se ha creado el archivo con exito en la ruta {ruta_receta}"""


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

def  eliminar_receta(*args):
    opc = args[0]
    ruta = args[1]
    nueva_ruta = Path(ruta, opc)
    print("las recetas de esta categoria son: ")
    c = 0
    dic_receta = {}
    for recetas in nueva_ruta.iterdir():
        c = c + 1
        print(f"{c}-> {recetas.name}")
        dic_receta[c] = recetas.name
    opc_receta = input("Elije la receta a eliminar: ")
    ruta_receta = Path(nueva_ruta, dic_receta[int(opc_receta)])
    try:
        ruta_receta.unlink()
    except OSError:
        print("Debe indicar in archivo")
    return "Receta eliminada"

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



"""·······························································"""

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



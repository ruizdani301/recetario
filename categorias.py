from os import system
from crear_receta import *
from listar_recetas import *
from eliminar_receta import *
from eliminar_categoria import *

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
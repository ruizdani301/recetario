from pathlib import Path

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
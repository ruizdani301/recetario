from pathlib import Path

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

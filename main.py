from libreria_pokemon import *
import acciones_pokemon as accion

"""
    AGREGAR:
    ✔ loadPkm
    - menu para hacer cosas con el pkm
    - iniciar programa (?)
    - crear pokemon segun entrada de usuario
    ✔ verificar si la especia de un pokemon existe <- tendran que de alguna forma escribir las 1000+ especies (o buscar la lista lista en algun lado)
"""

#inicar el programa
# 1. revisar si hay archivos de pkm en la carpeta
    # 1.1. si hay, cargar los datos
    # 1.2. si NO hay, hacer que el usuario cree un pkm y guardarlo


lista_pokemon = initPrograma()

for pokemon in lista_pokemon:
    imprimirPkm(pokemon)
    print('-'*10)
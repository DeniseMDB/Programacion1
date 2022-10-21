import json
import re


import funciones_lib as lib


def imprimir_menu():
    menu =\
        '''
        Seleccione una opcion:
        1 -Listar los últimos N pokemones.
        2 - Ordenar y Listar pokemones por poder. (asc o desc?)
        3 - Ordenar y Listar pokemones por ID. (asc o desc?)
        4 - Calcular la cantidad promedio de las key tipo lista (evoluciones, fortaleza, debilidad, tipo) (mayor o menor?)
        5 - Buscar pokemones por tipo
        6 - Exportar a CSV la lista de pokemones ordenada según opción elegida anteriormente [1-4]
        7 - Fin del programa

        '''
    print(menu)

def ejercicio_pokemon():
    file = "Practica Pokemon\pokedex.json"
    output = "Practica Pokemon\pokemon.csv"
    lista_pokemon = lib.cargar_json(file)
    lista_copia = []
    lista_archivo = []
    while True:
        imprimir_menu()
        respuesta = input("Seleccione opcion >> ")
        respuesta = lib.validar_numero(respuesta, "[1-9]{1}$")
        match respuesta:
            case 1:
                opcion = input("Cuantos pokemones desea mostar? >>>")
                opcion = lib.validar_numero(opcion, "[1-9]{1,2}$")
                cantidad = lib.validar_lista(lista_pokemon, opcion)
                lista_copia = lista_pokemon[:cantidad].copy()
                lista_archivo = lib.mostrar_lista(lista_copia, "poder")
            case 2:
                modo = input("Lo desea en orden asc o desc? >>> ")
                modo = lib.validar_respuesta(modo, "asc\desc")
                lista_copia = lib.sort_asc_desc(lista_pokemon, "poder", modo).copy()
                lista_archivo = lib.mostrar_lista(lista_copia,"poder")
            case 3:
                modo = input("Lo desea en orden asc o desc? >>> ")
                modo = lib.validar_respuesta(modo, "asc\desc")
                lista_copia = lib.sort_asc_desc(lista_pokemon, "id", modo).copy()
                lista_archivo = lib.mostrar_lista(lista_copia,"id")
            case 4:
                print("De que desea hayar el promedio?")
                key = input("evoluciones, fortaleza, debilidad, tipo >>> ")
                modo = input("Quiere mostrar los mayores o menores al promedio? >>> (mayor o menor)")
                key = lib.validar_respuesta(key,"evoluciones|fortaleza|debilidad|tipo")
                modo = lib.validar_respuesta(modo, "mayor|menor")
                print("El promedio de {0} es: {1}".format(key, lib.calcular_promedio(lista_pokemon, key)))
                lista_archivo = lib.comparacion_mayor_menor(lista_pokemon, key, modo)
                lib.mostrar_lista(lista_archivo, key)
            case 5:
                lista_copia = lib.devolver_valor_key(lista_pokemon,"tipo" )
                lib.sanitizar_dato(lista_copia)
                tipo = input("Ingrese el tipo de pokemon que desea mostrar: >>>")
                tipo = lib.validar_respuesta(tipo, "[a-z]")
                lista_archivo = lib.buscar(lista_pokemon, tipo)
            case 6:
                lib.crear_csv(lista_archivo, output)
                print("Archivo generado")
            case 7:
                break
                

ejercicio_pokemon()
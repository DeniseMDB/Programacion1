# -*- coding: utf-8 *-*
import funciones_ejer as lib

'''
1- Listar los primeros N héroes. El valor de N será ingresado por el usuario
(Validar que no supere max. de lista)

2- Ordenar y Listar héroes por altura.
Preguntar al usuario si lo quiere ordenar
de manera ascendente (‘asc’) o descendente (‘desc’)

3- Ordenar y Listar héroes por fuerza. Preguntar al usuario si lo quiere
ordenar de manera ascendente (‘asc’) o descendente (‘desc’)

4- Calcular promedio de cualquier key numérica,
filtrar los que cumplan con la condición de superar o no el promedio
(preguntar al usuario la condición: ‘menor’ o ‘mayor’)
se deberá listar en consola aquellos que cumplan con ser mayores o menores según corresponda.

5-Buscar héroes por inteligencia [good, average, high] y
listar en consola los que cumplan dicha búsqueda.

6- Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4]
'''


def imprimir_menu() -> None:
    menu =\
    """
    1- Listar los primeros N héroes. Ingresando cantidad N.
    2- Ordenar y Listar héroes por altura. (ascendente o descendente?)
    3- Ordenar y Listar héroes por fuerza. (ascendente o descendente?)
    4- Calcular promedio de cualquier key numérica. (menor o mayor?)
    5- Buscar héroes por inteligencia [good, average, high]
    6- Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4]
    7- Fin del Programa
    """
    print(menu)

def ejer_parcial ():
    archivo_json = "Practica parcial\data_stark.json"
    archivo_csv = "Practica parcial\stark.csv"
    lista_heroes = lib.cargar_json(archivo_json)
    lista_archivo = []
    lista_aux = []
    #key = ""
    while True:
        imprimir_menu()
        respuesta = input("Elija una opcion: >>")
        respuesta = lib.validar_numero(respuesta, "^[1-7]{1}$")
        match respuesta:
            case 1:
                key= "altura"
                respuesta = input("Cuantos hereoes quiere mostrar?: >>")
                cantidad = int(lib.validar_numero(respuesta, "^[1-9]{1,2}$"))
                cantidad = lib.validar_len_lista(lista_heroes, cantidad)
                lista_archivo = lista_heroes[:cantidad].copy()
                lib.mostrar_lista(lista_archivo, "altura")
            case 2:
                key = "altura"
                modo = input("asc o desc?: >>  ")
                modo = lib.validar_respuesta(modo, "asc|desc")
                lista_archivo = lib.sort_pedido(lista_heroes, key, modo)
                lib.mostrar_lista(lista_archivo, "altura")
            case 3:
                key = "fuerza"
                modo = input("asc o desc?: >>  ")
                modo = lib.validar_respuesta(modo, "asc|desc")
                lista_archivo = lib.sort_pedido(lista_heroes, key, modo)
                lib.mostrar_lista(lista_archivo, "fuerza")
            case 4:
                key = input("Que desea comparar? altura, fuerza, peso: >> ")
                key = lib.validar_respuesta(key, "altura|fuerza|peso")
                modo = input("mayor o menor?: >>  ")
                modo = lib.validar_respuesta(modo, "mayor|menor")
                lista_aux = lib.convertir_flotante(lista_heroes, key)
                print("\n\n")
                print(f"El promedio de {key} es: {lib.calcular_promedio(lista_aux, key)}.")
                lista_archivo= lib.comparar_mayor_menor(lista_aux, key, modo)
                lib.mostrar_comparacion(lista_archivo, key, modo)
                
            case 5:
                key= "inteligencia"
                modo = input("Seleccione inteligencia: good, average, high  >>> \n")
                modo = lib.validar_respuesta(modo, "good|average|high")
                lista_archivo=lib.buscar(lista_heroes, "inteligencia", modo)
            case 6:
                lib.exportar_csv(lista_archivo,key,archivo_csv)
            case 7:
                print("Fin del programa")
                break

ejer_parcial()





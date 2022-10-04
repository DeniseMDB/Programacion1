'''
    1 - Listar los personajes ordenados por altura
    2 - Mostrar el personaje mas alto de cada genero
    3 - Ordenar los personajes por peso
    4 - Armar un buscador de personajes 
    5 - Exportar lista personajes a CSV
    6 - Salir
'''


import funciones

def starwars_app():
    lista_personajes = funciones.cargar_json("PP_STARWARS/PP_STARWARS/data.json")
    output = "PP_STARWARS/PP_STARWARS/data.csv"
    while(True):
        print("1 - Listar los personajes ordenados por altura\n2 - Mostrar el personaje mas alto de cada genero\n3 - Ordenar los personajes por peso\n4 - Armar un buscador de personajes\n5 - Exportar lista personajes a CSV\n6 - Salir\n")
        respuesta = input("Ingrese la opcion que desea: >> ")
        if(respuesta=="1"):
            print("1 - Listar los personajes ordenados por altura\n")
            modo = input("Desea ordenar por orden asc o desc?: >>> ")
            lista_archivo = funciones.sort_asc_desc(lista_personajes, "height", modo).copy()
            funciones.mostrar_lista(lista_archivo)
        elif(respuesta=="2"):
            print("2 - Mostrar el personaje mas alto de cada genero\n")
            genero = input("Ingrese genero: male, female, n/a >>>  ")
            lista_aux = funciones.buscar_genero(lista_personajes, genero)
            i_max = funciones.buscar_max_min(lista_aux, "height", "asc")
            lista_archivo = (lista_aux[i_max])
            print("Nombre = {0} | Altura = {1} | Peso = {2} | Genero = {3}".format(lista_archivo["name"],lista_archivo["height"],lista_archivo["mass"],lista_archivo["gender"]))
        elif(respuesta=="3"):
            print("3 - Ordenar los personajes por peso\n")
            modo = input("Desea ordenar por orden asc o desc?: >>> ")
            lista_archivo = funciones.sort_asc_desc(lista_personajes, "mass", modo).copy()
            funciones.mostrar_lista(lista_archivo)
        elif(respuesta=="4"):
            print("4 - Armar un buscador de personajes\n")
            key = input("Desea buscar por name, height, mass o gender?: >> ")
            busqueda = input("A quien desea buscar?: >>> ")
            lista_archivo = funciones.buscar(lista_personajes, key, busqueda)
            lista = list(lista_archivo)
            print(lista_archivo)
        elif(respuesta=="5"):
            print("5 - Exportar lista personajes a CSV\n")
            funciones.crear_csv(output, lista_archivo)
        elif(respuesta=="6"):
            print("Fin del programa")
            break


starwars_app()


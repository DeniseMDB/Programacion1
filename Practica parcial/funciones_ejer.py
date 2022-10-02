import json
import re

def cargar_json(path: str)-> list[dict]:
    buffer_dict = []
    with open(path, 'r') as archivo:
        buffer_dict = json.load(archivo)
    return buffer_dict["heroes"]



def validar_numero(respuesta: str, patron_regex: str)-> int:  #valida opcion numerica de menu
    if respuesta: #evalua si es vacio o no, false vacio
        if re.match(patron_regex, respuesta):
            return int(respuesta)
        return -1

def convertir_flotante(lista: list[dict],key: str)-> list: 
    if lista:
        for element in lista:
            if (key in element.keys()):
                element[key] = int(element[key])
        return lista
    return -1


def validar_respuesta(respuesta: str, patron_regex: str)-> str: #valida opcion asc|desc, good|average etc
    if respuesta: #evalua si es vacio o no, false vacio
        if re.match(patron_regex, respuesta):
            return respuesta
        return -1


def validar_len_lista(lista: list[dict], tam: int)-> int:
    if lista: #valida lista vacia 
        if int(tam) < len (lista):
            print(f"Tamano correcto: {tam}")
            return tam
    print(f"tamaño maximo superado, hay {len(lista)} heroes")
    return len(lista)

def mostrar_lista(lista: list[dict], key: str)-> None:
    if lista:
        print("\n")
        for element in lista:
            if key in element.keys():
                mensaje = f'Nombre: {element["nombre"]} | Identidad: {element["identidad"]} | {key.capitalize()}: {element[key]}'
                print(mensaje)

def buscar_min_max(lista: list, key: str, modo: str)-> int: 
    retorno = -1
    if lista:    #es igual que len(lista)>0
        i_min_max = 0
        for i in range(len(lista)):
            if ((modo == 'asc' and lista[i][key] < lista[i_min_max][key]) or
                (modo == 'desc' and lista[i][key] > lista[i_min_max][key])):
                i_min_max = i
        retorno = i_min_max
    return retorno

def sort_pedido(lista: list, key: str = "altura", modo: str = "asc") -> list[dict]:          #
    lista_copia = lista.copy()
    for i in range(len(lista_copia)):
        lista_aux = lista_copia[i:]
        indice_min_max = buscar_min_max(lista_aux, key, modo) + i #me busca sumando al indice
        lista_copia[i], lista_copia[indice_min_max] = lista_copia[indice_min_max], lista_copia[i]
    return lista_copia

def buscar(lista: list, key: str, modo: str)-> list[dict]:
    lista_copia = lista.copy()
    print("\n")
    for elemento in lista_copia:
        if(re.search(modo,elemento["inteligencia"],re.IGNORECASE)):
            mensaje = f'Nombre: {elemento["nombre"]} | Identidad: {elemento["identidad"]} | {key.capitalize()}: {elemento[key]}'
            print(mensaje)

def calcular_promedio(lista: list, key: str)-> int:
    acumulador = 0
    total_suma = 0
    for personaje in lista:
        acumulador += 1
        total_suma += personaje[key]
        promedio = total_suma / acumulador
    promedio = int(promedio)
    return promedio


def comparar_mayor_menor(lista: list, key: str, modo: str)->list:
    '''
    recibe lista de heroes con la key a comparar
    hace el promedio
    devuelve lista de mayores a promedio y menores
    ''' 
    lista_copia = lista.copy()
    promedio = calcular_promedio(lista_copia, key)
    mensaje = -1
    lista_final = []
    for elemento in lista_copia:
        if((modo == "mayor") and (elemento[key] > promedio)):
            lista_final.append(elemento.copy())
        elif(modo == "menor" and elemento[key] < promedio):
            lista_final.append(elemento.copy())
    return lista_final


def mostrar_comparacion(lista: list, key: str, modo: str)-> list:       
    if lista:
        print("\n")
        print("Personajes con {0} {1} al promedio: ".format(key, modo))
        for element in lista:
            mensaje = f'Nombre: {element["nombre"]} | Identidad: {element["identidad"]} | {key.capitalize()}: {element[key]}'
            print(mensaje)
            # if(modo == "mayor"):
            #     print("Los personajes mayores al promedio son: ")
            #     print(mensaje)
            # elif(modo == "menor"):
            #     print("Los personajes menores al promedio son: {0}".format(mensaje))

def exportar_csv(lista: list,key: str, path: str):
    with open(path, 'w') as archivo:
        for elemento in lista:
            mensaje = f'Nombre: {elemento["nombre"]} | Identidad: {elemento["identidad"]} | {key.capitalize()}: {elemento[key]}\n'
            archivo.write(mensaje)
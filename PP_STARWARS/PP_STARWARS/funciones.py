
import json
import re

def cargar_json(path: str):
    buffer_dict = []
    with open(path, 'r') as archivo:
        buffer_dict = json.load(archivo)
    return buffer_dict["results"]

def mostrar_lista(lista: list[dict])->list:
    if lista:
        print("\n")
        for element in lista:
            mensaje = "Nombre = {0} | Altura = {1} | Peso = {2} | Genero = {3}".format(element["name"],element["height"],element["mass"],element["gender"] )
            print(mensaje)

def validar_numero(pattern: str, respuesta: str):
    if re.match(pattern, respuesta):
        return respuesta
    return -1

def buscar_max_min(lista: list, key: str, modo: str)-> int:
    if lista:
        i_max_min = 0
        for i in range(len(lista)):
            if(modo =="asc" and int(lista[i][key]) > int(lista[i_max_min][key])):
                i_max_min = i
            elif(modo == "desc" and int(lista[i][key]) < int(lista[i_max_min][key])):
                i_max_min = i
    return i_max_min


def buscar_genero(lista: list, genero: str)-> list:
    lista_genero = []
    for personaje in lista:
        if personaje["gender"] == genero:
            lista_genero.append(personaje)
    return lista_genero

def sort_asc_desc(lista: list, key: str, modo: str)->list:
    lista_copia = lista.copy()
    for i in range(len(lista)):
        lista_aux = lista_copia[i:]
        indice_min_max = buscar_max_min(lista_aux, key, modo) + i
        lista_copia[i], lista_copia[indice_min_max] = lista_copia[indice_min_max], lista_copia[i]
    return lista_copia

def crear_csv(path: str, lista: list):
    with open(path, 'w') as archivo:
        for elemento in lista:
            mensaje = "Nombre = {0} | Altura = {1} | Peso = {2} | Genero = {3}".format(elemento["name"],elemento["height"],elemento["mass"],elemento["gender"] )
            archivo.write(mensaje)

def buscar(lista: list[dict], key: str, respuesta: str):
    if lista:
        for elemento in lista:
            if re.match(respuesta, elemento[key]):
                mensaje = "Nombre = {0} | Altura = {1} | Peso = {2} | Genero = {3}".format(elemento["name"],elemento["height"],elemento["mass"],elemento["gender"] )
        return mensaje










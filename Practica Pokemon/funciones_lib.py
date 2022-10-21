from dataclasses import replace
import json
import re

'''
Ejercicio tipo parcial

1 -Listar los últimos N pokemones. El valor de N será ingresado por el usuario
(Validar que no supere max. de lista)
2- Ordenar y Listar pokemones por poder.
Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)
3- Ordenar y Listar pokemones por ID.
Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)
4- Calcular la cantidad promedio de las key tipo lista (evoluciones, fortaleza, debilidad, tipo),
filtrar los que cumplan con la condición de superar o no el promedio (preguntar al usuario la condición: ‘menor’ o ‘mayor’)
se deberá listar en consola aquellos que cumplan con tener mayores o menores cantidades en la lista de dicha key según corresponda.
5- Buscar pokemones por tipo (dar e elegir los diversos tipos que un pokémon puede poseer,
muchos de ellos poseen más de un tipo, con lo cual habrá que darle a elegir al usuario
entre todos los tipos que existen en el json) una vez seleccionado listar en consola
los que posean dicho tipo. (Usando RegEx para la búsqueda).
Ejemplo: Si el usuario elige: volador y hay un pokemon con muchos tipos, pero uno de ellos es volador, deberá listarlo. (charizard, zapdos, moltres, articuno poseen más de un tipo, pero uno de ellos es volador).
6- Exportar a CSV la lista de pokemones ordenada según opción elegida anteriormente [1-4]

Aclaraciones:
Los puntos deben ser accedidos mediante un menú. Para todas las opciones,
validar lo ingresado por consola con RegEx
El set de datos proviene de un json
Realizar las validaciones que crea pertinentes
En todos los casos se deberá trabajar con una copia de la lista original

'''
def cargar_json(path: str)->list[dict]:
    buffer_dict = []
    with open(path,'r') as archivo:
        buffer_dict = json.load(archivo)
    return buffer_dict["pokemones"]

def validar_numero(respuesta: str, patron_regex: str)-> int:
    if respuesta:
        if re.match(patron_regex, respuesta):
            return int(respuesta)
        return -1
    
def validar_lista(lista: list[dict], respuesta: int)-> list:
    if lista:
        if respuesta <= len(lista):
            print("Valor correcto")
            n = respuesta
            return n
        print(f"Valor incorrecto, hay {len(lista)} pokemones")
        return len(lista)

def mostrar_lista(lista: list, key: str)-> list:
    if lista:
        print("\n")
        for element in lista:
            if key in element.keys():
                mensaje = f'ID: {element["id"]} | Nombre: {element["nombre"]} | Evoluciones: {element["evoluciones"]} | Poder: {element["poder"]} | Fortaleza: {element["fortaleza"]} | Debilidad: {element["debilidad"]}'
                print(mensaje)

def definir_min_max(lista: list, key: str, modo: str)->int:
    retorno = -1
    if lista:
        i_min_max = 0
        for i in range(len(lista)):
            if((modo == "asc" and lista[i][key] > lista[i_min_max][key]) or
                (modo == "desc" and lista[i][key] < lista[i_min_max][key])):
                i_min_max = i
        retorno = i_min_max
    return i_min_max

def sort_asc_desc(lista: list, key: str, modo: str)-> list:
    lista_copia = lista.copy()
    retorno = -1
    for i in range(len(lista)):
        lista_aux = lista_copia[i:]
        indice_min_max = definir_min_max(lista_aux, key, modo) + i #me busca sumando al indice
        lista_copia[i], lista_copia[indice_min_max] = lista_copia[indice_min_max], lista_copia[i]
    return lista_copia

def calcular_promedio(lista: list[dict], key: str)-> int:
    acumulador = 0
    suma_key = 0
    if lista:
        for elemento in lista:
            acumulador +=1
            suma_key += len(elemento[key])
        promedio = suma_key / acumulador
    return int(promedio)

def comparacion_mayor_menor(lista: list[dict], key: str, modo: str)->list:
    if lista:
        promedio = calcular_promedio(lista, key)
        lista_final = []
        for elemento in lista:
            if(modo == 'mayor' and len(elemento[key]) > promedio):
                lista_final.append(elemento.copy())
            elif(modo == 'menor' and len(elemento[key]) < promedio):
                lista_final.append(elemento.copy())
        return lista_final

def validar_respuesta(respuesta: str, patron_regex: str)-> int:
    if respuesta:
        if re.match(patron_regex, respuesta):
            return respuesta
        return -1

def devolver_valor_key(lista: list[dict], key: str ="tipo")-> list:  #Devuelve lista de tipos de pokemones
    lista_copia = lista.copy()
    lista_value = []
    for elemento in lista_copia:
        lista_value.append((elemento[key]).copy())
    return lista_value

def sanitizar_dato(lista: list)-> str:
    lista_value = str(lista)
    lista_value = set(re.findall('[a-z]+', lista_value))
    lista_value = list(lista_value)
    print("Los tipos a elegir son: ")
    for elemento in lista_value:
        print(f"- {elemento}")
    return lista_value



def buscar(lista: list, modo: str)-> list[dict]:
    lista_copia = lista.copy()
    lista_aux = []
    print("\n")
    for elemento in lista_copia:
        elemento["tipo"]= str(elemento["tipo"])
        if(re.findall(modo, elemento["tipo"])):
            mensaje = f'ID: {elemento["id"]} | Nombre: {elemento["nombre"]} | Tipo: {elemento["tipo"]} | Evoluciones: {elemento["evoluciones"]} | Poder: {elemento["poder"]} | Fortaleza: {elemento["fortaleza"]} | Debilidad: {elemento["debilidad"]}'
            mensaje = mensaje.replace("[", " ")
            mensaje = mensaje.replace("]", " ")
            mensaje = mensaje.replace(",", "y")
            mensaje = mensaje.replace("'", " ")             
            print(mensaje)
            lista_aux.append(mensaje)
            print(type(mensaje))
    print(type(lista_aux))
    print(len(lista_aux))
    return lista_aux

def crear_csv(lista: list, path: str):
    with open(path, 'w') as archivo:
        for elemento in lista:
            mensaje = f'ID: {elemento["id"]} | Nombre: {elemento["nombre"]} | Tipo: {elemento["tipo"]} | Evoluciones: {elemento["evoluciones"]} | Poder: {elemento["poder"]} | Fortaleza: {elemento["fortaleza"]} | Debilidad: {elemento["debilidad"]}'
            archivo.write(mensaje)



                




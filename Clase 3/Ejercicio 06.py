'''
Desafío #00:

Analizar detenidamente el set de datos
Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
Calcular e informar cual es el superhéroe más y menos pesado.
Ordenar el código implementando una función para cada uno de los valores informados.
Construir un menú que permita elegir qué dato obtener

'''
'''
{
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": "79.349999999999994",
    "peso": "18.449999999999999",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": "average"
},
'''
from data_stark import lista_personajes

def nombre_personaje():
    #------NOMBRES PERSONAJES--------
    for personaje in lista_personajes:
        print(personaje["nombre"])

def nombre_altura():
    #------NOMBRES Y ALTURAS--------
    for personaje in lista_personajes:
        print(personaje["nombre"], personaje["altura"])

def personaje_mas_alto():
#------PERSONAJE MAS ALTO--------
    personaje_alto = lista_personajes[0]
    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])
        if(personaje["altura"] > personaje_alto["altura"]):
            personaje_alto = personaje
    print("El personaje mas alto es: ",personaje_alto["nombre"])

def personaje_mas_bajo():
    #------PERSONAJE MAS BAJO--------
    personaje_bajo = lista_personajes[0]
    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])
        if(personaje["altura"] < personaje_bajo["altura"]):
            personaje_bajo = personaje
    print("El personaje mas bajo es: ", personaje_bajo["nombre"])

def promedio_alturas():
    #------PROMEDIO ALTURAS--------
    acumulador_alturas = 0
    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])
        acumulador_alturas += personaje["altura"]
    print("Promedio: {0} - Cantidad: {2} - Acumulador: {1}".format((acumulador_alturas/len(lista_personajes)),acumulador_alturas,len(lista_personajes)))

def personaje_mas_pesado():
    #------PERSONAJE MAS PESADO--------
    personaje_pesado = lista_personajes[0]
    for personaje in lista_personajes:
        personaje["peso"] = float(personaje["peso"])
        if(personaje["peso"] > personaje_pesado["peso"]):
            personaje_pesado = personaje
    print("Personaje mas pesado: {0} - Peso: {1}".format(personaje_pesado["nombre"],personaje_pesado["peso"]))

def personaje_menos_pesado():
    #------PERSONAJE MENOS PESADO--------
    personaje_liviano = lista_personajes[0]
    for personaje in lista_personajes:
        personaje["peso"] = float(personaje["peso"])
        if(personaje["peso"] < personaje_liviano["peso"]):
            personaje_liviano = personaje
    print("Personaje mas liviano: {0} - Peso: {1}".format(personaje_liviano["nombre"],personaje_liviano["peso"]))

while True:
    respuesta = input("\n1 - Nombre personajes\n2 - Nombre y altura \n3 - Personaje mas alto\n4 - Personaje mas bajo\n5 - Promedio alturas\n6 - Personaje mas pesado\n7 - Personaje menos pesado\n\n")
    if(respuesta == "1"):
        nombre_personaje()
    elif(respuesta == "2"):
        nombre_altura()
    elif(respuesta == "3"):
        personaje_mas_alto()
    elif(respuesta == "4"):
        personaje_mas_bajo()
    elif(respuesta == "5"):
        promedio_alturas()
    elif(respuesta == "6"):
        personaje_mas_pesado()
    elif(respuesta == "7"):
        personaje_menos_pesado()



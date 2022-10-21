'''
Desafío #01:
Agregar al código elaborado para cumplir el desafío #00 los siguientes puntos, utilizando un menú que permita acceder a cada uno de los puntos por separado.
A-Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
B-Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
C-Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
D-Recorrer la lista y determinar cuál es el superhéroe más alto de género F 
E-Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 
F-Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F 
G-Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
H-Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
I-Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a G)
J-Determinar cuántos superhéroes tienen cada tipo de color de ojos.
K-Determinar cuántos superhéroes tienen cada tipo de color de pelo.
L-Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). 
M-Listar todos los superhéroes agrupados por color de ojos.
N-Listar todos los superhéroes agrupados por color de pelo.
O-Listar todos los superhéroes agrupados por tipo de inteligencia

'''


from data_stark import lista_personajes
'''
for personaje in lista_personajes:
    lista_femenino = []
    if personaje["genero"] == "F":
        lista_femenino.append(personaje)
        print(lista_femenino)
    else:
        pass
'''
#------PERSONAJES MASCULINOS--------
for personaje in lista_personajes:
    if (personaje["genero"] == "M"):
        print("Personaje masculino ", personaje["nombre"])

#------PERSONAJES FEMENINOS--------
for personaje in lista_personajes:
    if (personaje["genero"] == "F"):
        print("Personaje femenino ",personaje["nombre"])

#------MASCULINO MAS ALTO--------
for personaje in lista_personajes:
    if (personaje["genero"] == "M"):
        masculino_alto = lista_personajes[0]
        masculino_alto["altura"] = float(masculino_alto["altura"])
        personaje["altura"] = float(personaje["altura"])
        if(masculino_alto["altura"] < personaje["altura"]):
            masculino_alto["altura"] = personaje["altura"]
            masculino_alto["nombre"] = personaje["nombre"]
print("El personaje masculino mas alto es: ",masculino_alto["nombre"])

#------FEMENINO MAS ALTO--------
for personaje in lista_personajes:
    if (personaje["genero"] == "F"):
        femenino_alto = personaje
        femenino_alto["altura"] = float(femenino_alto["altura"])
        personaje["altura"] = float(personaje["altura"])
        if(femenino_alto["altura"] < personaje["altura"]):
            femenino_alto["altura"] = personaje["altura"]
            femenino_alto["nombre"] = personaje["nombre"]
print("El personaje femenino mas alto es: ",femenino_alto["nombre"])

#------MASCULINO MAS BAJO--------
for personaje in lista_personajes:
    if (personaje["genero"] == "M"):
        masculino_bajo = lista_personajes[0]
        masculino_bajo["altura"] = float(masculino_bajo["altura"])
        personaje["altura"] = float(personaje["altura"])
        if(masculino_bajo["altura"] > personaje["altura"]):
            masculino_bajo["altura"] = personaje["altura"]
            masculino_bajo["nombre"] = personaje["nombre"]
print("El personaje masculino mas bajo es: ",masculino_bajo["nombre"])

#------FEMENINO MAS BAJO--------
def femenino_mas_bajo():
    femenino_bajo = {}
    flag = True
    for personaje in lista_personajes:
        if personaje["genero"] == "F" and flag == True:
            femenino_bajo = personaje
            flag = False
        elif personaje["genero"] == "F":
            if (float(femenino_bajo["altura"]) > float(personaje["altura"])):
                femenino_bajo = personaje
    print("El personaje femenino mas bajo es: ",femenino_bajo["nombre"])


#------ALTURA PROMEDIO MASCULINO--------
def promedio_masculino():
    for personaje in lista_personajes:
        acumulador = 0
        total_alturas = 0
        if personaje["genero"] == "M":
            acumulador += 1
            total_alturas += personaje["altura"]
            promedio = total_alturas / acumulador
    print("El promedio de alturas de personajes masculinos es: ", promedio)

#------ALTURA PROMEDIO FEMENINO--------
def promedio_femenino():
    acumulador = 0
    total_alturas = 0
    for personaje in lista_personajes:
        if personaje["genero"] == "F":
            acumulador += 1
            total_alturas += personaje["altura"]
            promedio = total_alturas / acumulador
    print("El promedio de alturas de personajes femeninos es: ", promedio)


#------COLOR DE OJOS--------
def lista_color_ojos():
    lista_ojos = []
    for personaje in lista_personajes:
        lista_ojos.append(personaje["color_ojos"])
    lista_ojos = set(lista_ojos)
    lista_ojos = list(lista_ojos)

    for color in lista_ojos:
        cantidad_personajes = 0
        for personaje in lista_personajes:
            if personaje["color_ojos"] == color:
                cantidad_personajes += 1
        mensaje = "Hay {0} personaje/s con el color {1} de ojos".format(cantidad_personajes, color)
    return mensaje

#------COLOR DE PELO--------
def lista_pelo():
    lista_pelo = []
    for personaje in lista_personajes:
        lista_pelo.append(personaje["color_pelo"])
    lista_pelo = set(lista_pelo)
    lista_pelo = list(lista_pelo)

    for color in lista_pelo:
        cantidad_personajes = 0
        for personaje in lista_personajes:
            if personaje["color_pelo"] == color:
                cantidad_personajes += 1
        mensaje = "Hay {0} personaje/s con el color {1} de pelo".format(cantidad_personajes, color)
    return mensaje


#------TIPO DE INTELIGENCIA--------
def tipo_inteligencia():
    lista_inteligencia = []
    for personaje in lista_personajes:
        lista_inteligencia.append(personaje["inteligencia"])
    lista_inteligencia = set(lista_inteligencia)
    lista_inteligencia = list(lista_inteligencia)

    for tipo in lista_inteligencia:
        cantidad_personajes = 0
        for personaje in lista_personajes:
            if personaje["inteligencia"] == tipo:
                cantidad_personajes += 1
        mensaje = "Hay {0} personaje/s con el tipo {1} de inteligencia".format(cantidad_personajes, tipo)

#------LISTA SUPERHEROES OJOS--------
def dic_ojos():
    dic_ojos_personajes = {}
    lista_ojos = []
    for personaje in lista_personajes:
        lista_ojos.append(personaje["color_ojos"])
    lista_ojos = set(lista_ojos)
    lista_ojos = list(lista_ojos)
    for color in lista_ojos:
        for personaje in lista_personajes:
            if color == personaje["color_ojos"]:
                dic_ojos_personajes[color] = personaje
            else:
                -1
    return dic_ojos_personajes

#------LISTA SUPERHEROES PELO--------
def dic_pelo():
    dic_pelo_personajes = {}
    lista_pelo = []
    for personaje in lista_personajes:
        lista_pelo.append(personaje["color_pelo"])
    lista_pelo = set(lista_pelo)
    lista_pelo = list(lista_pelo)
    for color in lista_pelo:
        for personaje in lista_personajes:
            if color == personaje["color_pelo"]:
                dic_pelo_personajes[color] = personaje
            else:
                -1
    return dic_pelo_personajes

#------LISTA SUPERHEROES INTELIGENCIA--------
def dic_inteligencia():
    dic_inteligencia_personajes = {}
    lista_inteligencia = []
    for personaje in lista_personajes:
        lista_inteligencia.append(personaje["inteligencia"])
    lista_inteligencia = set(lista_inteligencia)
    lista_inteligencia = list(lista_inteligencia)
    for inteligencia in lista_inteligencia:
        for personaje in lista_personajes:
            if inteligencia == personaje["inteligencia"]:
                dic_inteligencia_personajes[inteligencia] = personaje
            else:
                -1
    return dic_inteligencia_personajes

    
    

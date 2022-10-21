from data_stark import lista_heroes
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
}
'''
#ejercicio 1.1
def extraer_nombre (heroe:dict)-> str:
    nombre_heroe = heroe["nombre"].upper()
    if(len(nombre_heroe) > 0):
        if (nombre_heroe.count("THE") > 0):
            nombre_heroe = nombre_heroe.replace("THE", "")
        if (nombre_heroe.count("-") > 0):
            nombre_heroe = nombre_heroe.replace("-", " ")
        iniciales = ""
        lista_nombres = nombre_heroe.split()
        for nombre in range(len(lista_nombres)):
            iniciales += "{0}.".format(lista_nombres[nombre][0])
        return iniciales
    else:
        return "N/A"
#ejercicio 1.2
'''
La función deberá agregar una nueva clave al diccionario
recibido como parámetro.
La clave se deberá llamar ‘iniciales’ y su valor será
el obtenido de llamar a la función ‘extraer_iniciales’
'''
def definir_iniciales_nombre (heroe:dict):
    for heroe in lista_heroes:
        respuesta = False
        # Que el dato recibido sea del tipo diccionario
        # Que el  diccionario contengan la clave ‘nombre’  
        if(type(heroe) == type({}) and "nombre" in heroe.keys()):
            key, value = 'iniciales', extraer_nombre(heroe)
            heroe.update({"key": value})
            heroe["iniciales"] = extraer_nombre(heroe)
            respuesta = True
    return respuesta
#ejercicio 1.3
'''
La función deberá iterar la lista_heroes pasándole
cada héroe a la función definir_iniciales_nombre.
'''
def agregar_iniciales_nombre (lista_heroes: list):
    if(type(lista_heroes) == type([]) and (len(lista_heroes) > 0 )):
        for heroe in lista_heroes:
            definir_iniciales_nombre(lista_heroes)
            if(definir_iniciales_nombre(lista_heroes) == False):
                print("El origen de datos no contiene el formato correcto")
        return True

#ejercicio 1.4
'''
La función deberá utilizar la función agregar_iniciales_nombre’
para añadirle las iniciales a los diccionarios contenidos en la lista_heroes
Luego deberá imprimir la lista completa de los nombres
de los personajes seguido de las iniciales encerradas entre paréntesis () 
'''
def stark_imprimir_nombres_con_iniciales(lista_heroes: list):  
    if(type(lista_heroes) == type([]) and (len(lista_heroes) > 0 )):
        for heroe in lista_heroes:
            agregar_iniciales_nombre(lista_heroes)
            nuevo_nombre = "* {0} ({1})".format(heroe["nombre"], heroe["iniciales"])
            print(nuevo_nombre)
        
#Ejercicio 2.1            
def generar_codigo_heroe(id_heroe: int, genero_heroe: str) -> str:
    codigo_heroe = ""
    if(len(genero_heroe) > 0 and type(id_heroe) == type(int()) 
        and (genero_heroe == "M" or genero_heroe == "F" or
        genero_heroe == "NB")):
        id_heroe = str(id_heroe)
        suma_variables = len(genero_heroe) + 1
        numero_completar = 10 - suma_variables
        codigo_heroe = "{0}-{1}".format(genero_heroe, id_heroe.zfill(numero_completar)) 
        return codigo_heroe
    else:
        return "N/A"

#Ejercicio 2.2 
'''
La función deberá agregar una nueva clave llamada 
‘codigo_heroe’ al diccionario ‘heroe’ recibido como parámetro y 
asignarle como valor un código utilizando 
la función ‘generar_codigo_heroe’
'''
def agregar_codigo_heroe(heroe: dict, id_heroe: int):
    heroe["codigo_heroe"] = generar_codigo_heroe(id_heroe, heroe["genero"])
    if(len(lista_heroes) > 0 and len(heroe["codigo_heroe"]) == 10 ):
        respuesta = True
    else:
        respuesta = False
    return respuesta

#Ejercicio 2.3
'''
La función deberá iterar 
la lista de personajes y agregarle el código 
a cada uno de los personajes.
'''
def stark_generar_codigos_heroes(lista_heroes: list):
    id_heroe = 0
    for heroe in lista_heroes:
        if(len(lista_heroes) > 0 and type(heroe) == type({}) and "genero" in heroe.keys()):
            id_heroe += 1
            agregar_codigo_heroe (heroe, id_heroe)
        else:
            print("El origen de datos no contiene el formato correcto")
    ultimo_heroe = len(lista_heroes)-1
    print("Se asignaron {0} codigos".format(id_heroe))
    print("El codigo del primer heroe es: {0}".format(lista_heroes[0]["codigo_heroe"]))
    print("El codigo del ultimo heroe es: {0}".format(lista_heroes[ultimo_heroe]["codigo_heroe"]))

#Ejercicio 3.1

def sanitizar_entero (numero_str: int)->str:
    if((numero_str.isnumeric() == True) and numero_str > 0):
        numero_str = numero_str.strip()
        numero_str = int(numero_str)
        return numero_str
    elif (type(numero_str) != type (int())):
        return "-1"      #Si contiene carácteres no numéricos
    elif(type(numero_str) == type (int()) and numero_str < 0):
        return "-2"      #Si el número es negativo 
    else:
        return "-3"      #Si ocurren otros errores que no permiten convertirlo a entero

#Ejercicio 3.2
def sanitizar_flotante(numero_str: float)->str:
    if(type(numero_str) == type (float()) and numero_str > 0):
        numero_str = numero_str.strip()
        numero_str = float(numero_str)
    elif (type(numero_str) != type (int())):
        return "-1"         #Si contiene carácteres no numéricos
    elif(type(numero_str) == type (int()) and numero_str < 0):
        return "-2"         #Si el número es negativo 
    else:
        return "-3"         #Si ocurren otros errores que no permiten convertirlo a entero

#Ejercicio 3.3
def sanitizar_string(valor_str: str,valor_por_defecto: str = "-" ):
    import re
    #valor_por_defecto = "-"
    busqueda = re.findall("[0-9]+", valor_str)#falta verificar numeros en valor_str
    print(busqueda)
    if((busqueda[0:]).isnumeric == True):
        return "N/A"
    elif(len(valor_str) == 0):
        valor_por_defecto = valor_por_defecto.lower()
        return valor_por_defecto
    else:
        valor_str = valor_str.replace("/", " ")
        valor_str = valor_str.lower()
        return valor_str
    valor_str = valor_str.strip()
    valor_por_defecto = valor_por_defecto.strip()    


#print(agregar_codigo_heroe(lista_heroes[0], 1))
#print(lista_heroes[0]["codigo_heroe"])

# print(stark_generar_codigos_heroes(lista_heroes))
# print(lista_heroes[0])
# print(lista_heroes[5])
# print(lista_heroes[10])
print(sanitizar_string("holis2/", ""))

















# while True:
#     respuesta = input("\n1 - EJERCICIO 1.1\n2 - EJERCICIO 1.2 \n3 - EJERCICIO 1.3\n4 - EJERCICIO 1.4\n5 - EJERCICIO 1.5\n6 - Personaje mas pesado\n7 - Personaje menos pesado\n\n")
#     if(respuesta == "1"):
#         extraer_nombre(lista_heroes)
#     elif(respuesta == "2"):
#         definir_iniciales_nombre(lista_heroes)
#     elif(respuesta == "3"):
#         agregar_iniciales_nombre(lista_heroes)
#     elif(respuesta == "4"):
#         stark_imprimir_nombres_con_iniciales(lista_heroes)
#     elif(respuesta == "5"):
#         stark_generar_codigos_heroes(lista_heroes)
#     elif(respuesta == "6"):
#         pass
#     elif(respuesta == "7"):
#         pass
#Ejercicio Integrador 03
#Denise Du Bois

#La división de alimentos de industrias Wayne está trabajando en
#un pequeño software para cargar datos de heroínas y héroes,
#para para tener un control de las condiciones de heroes existentes, nos solicitan:
#Nombre de Heroína/Héroe
#EDAD (mayores a 18 años)
#Sexo ("m", "f" o "nb")
#Habilidad ("fuerza", "magia", "inteligencia").
#A su vez, el programa deberá mostrar por consola lo siguiente:
#Dar el nombre de Héroe | Heroína de 'fuerza' más joven.
#El sexo y nombre de Heroe | Heroína de mayor edad.
#La cantidad de Heroinas que tienen habilidades de 'fuerza' o 'magia'.
#El promedio de edad entre Heroinas.
#El promedio de edad entre Heroes de fuerza.


acumulador_heroinas = 0
suma_edad_heroina = 0
acumulador_heroes_fuerza = 0
suma_edad_heroes = 0
acumulador_heroina_fuerza_magia = 0
edad_fuerza_joven = 0
flag_fuerza_joven = True
flag_mayor = True
edad_mayor = 0
respuesta = True


while (respuesta):
    nombre = input("Ingrese el nombre de Heroína/Héroe: ")

    while (True):
        edad = int(input("Ingrese la edad: "))
        if edad >= 18:
            break

    sexo = input("Ingrese el sexo (m, f o nb): ")
    while sexo != "m" and sexo != "f" and sexo != "nb":
        sexo = input("Ingrese el sexo (m, f o nb): ")

    habilidad = input("Ingrese la habilidad (fuerza, magia, inteligencia): ")
    while habilidad != "fuerza" and habilidad != "magia" and habilidad != "inteligencia":
        habilidad = input("Ingrese la habilidad (fuerza, magia, inteligencia): ")

    #Dar el nombre de Héroe | Heroína de 'fuerza' más joven.
    if (flag_fuerza_joven):
        if habilidad == "fuerza":
            nombre_fuerza = nombre
            edad_fuerza_joven = edad
            flag_fuerza_joven = False
        elif habilidad == "fuerza" and edad_fuerza_joven > edad:
            nombre_fuerza = nombre
            edad_fuerza_joven = edad

    #El sexo y nombre de Heroe | Heroína de mayor edad.
    if (flag_mayor):
        nombre_mayor = nombre
        sexo_mayor = sexo
        edad_mayor = edad
        flag_mayor = False
    elif edad_mayor < edad:
        edad_mayor = edad
        sexo_mayor = sexo
        nombre_mayor = nombre

    #La cantidad de Heroinas que tienen habilidades de 'fuerza' o 'magia'.
    if sexo == "f" and (habilidad == "fuerza" or habilidad == "magia"):
        acumulador_heroina_fuerza_magia += 1

    #El promedio de edad entre Heroinas
    if sexo == "f":
        acumulador_heroinas += 1
        suma_edad_heroina += edad

    #El promedio de edad entre Heroes de fuerza.
    if sexo == "m":
        acumulador_heroes_fuerza += 1
        suma_edad_heroes += edad
    
    confirmar = str.lower(input("Desea continuar? si o no"))
    if (confirmar == "no"):
        respuesta = False



promedio_heroinas = suma_edad_heroina / acumulador_heroinas
promedio_heroes = suma_edad_heroes / acumulador_heroes_fuerza

#Dar el nombre de Héroe | Heroína de 'fuerza' más joven.
#El sexo y nombre de Heroe | Heroína de mayor edad.
#La cantidad de Heroinas que tienen habilidades de 'fuerza' o 'magia'.
#El promedio de edad entre Heroinas.
#El promedio de edad entre Heroes de fuerza.

print("El nombre de Héroe | Heroína de 'fuerza' más joven es: ", nombre_fuerza)
print("El sexo y nombre de Heroe | Heroína de mayor edad es: ", sexo_mayor," ", nombre_mayor)
print("La cantidad de Heroinas que tienen habilidades de 'fuerza' o 'magia' es: ", acumulador_heroina_fuerza_magia)
print("El promedio de edad entre Heroinas es: ", promedio_heroinas)
print("El promedio de edad entre Heroes de fuerza: ", promedio_heroes)
print("Fin del programa")





    



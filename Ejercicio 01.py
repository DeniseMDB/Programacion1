#
## La división de higiene está trabajando en un control de stock para productos sanitarios.
#Debemos realizar la carga de 5 (cinco) productos de prevención de contagio,
# de cada una debe obtener los siguientes datos:
# El tipo (validar "barbijo", "jabón" o "alcohol")
#El precio: (validar entre 100 y 300)
#La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades)
#La marca y el Fabricante.
#  
## Se debe informar lo siguiente:
##Del más caro de los barbijos, la cantidad de unidades y el fabricante.
##Del ítem con más unidades, el fabricante.
# Cuántas unidades de jabones hay en total.

# Hacemos 
tipo_producto = ''
precio = 0
cantidad = 0
marca = ''
fabricante = ''

marca_barbijo_caro = ''
cantidad_barbijo_caro = ''
fabricante_barbijo_caro = ''
precio_barbijo_caro = ''

item_mas_unidades = ''
fabricante_mas_unidades = ''

cantidad_jabones = 0

for iteracion in range (5):

    tipo_producto = input("Ingrese tipo de producto (jabon, barbijo o alcohol): ")
    while tipo_producto != 'barbijo' and tipo_producto!= 'jabon' and tipo_producto != 'alcohol':
        tipo_producto = input("Ingrese tipo de producto (jabon, barbijo o alcohol): ")

    precio = int(input("Ingrese el precio: $"))
    
    while (True):

        if precio > 99 and precio < 301:
            break
    #Version do-while UTN
    while (True):
        cantidad = int(input("Ingrese cantidad: "))
        if cantidad > 0 and cantidad < 1000:
            break

    marca = input("Ingrese marca: ")
    fabricante = input("Ingrese fabricante: ")

## Se debe informar lo siguiente:
##Del más caro de los barbijos, la cantidad de unidades y el fabricante.
##Del ítem con más unidades, el fabricante.
# Cuántas unidades de jabones hay en total.

    if tipo_producto == 'barbijo':
        # Es mas caro que el anterior
        if precio > precio_barbijo_caro:
            precio_barbijo_caro = precio
            cantidad_barbijo_caro =  cantidad
            fabricante_barbijo_caro = fabricante
            marca_barbijo_caro =  marca
    elif tipo_producto == 'jabon':
        cantidad_jabones += cantidad



    if cantidad > item_mas_unidades:
            item_mas_unidades = cantidad
            fabricante_mas_unidades = fabricante


print("Babrijo mas caro hay: ", cantidad_barbijo_caro, " y lo fabrica: ", fabricante_barbijo_caro)
print("El item con mas unidades lo fabrica: ", fabricante_mas_unidades)
print("Jabones hay: ", cantidad_jabones)
print("Fin del programa")






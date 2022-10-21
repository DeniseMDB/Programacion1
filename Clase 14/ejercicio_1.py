import re
lista_precios = {
    
    "banana" : {
        "precio" : 120.10,
        "unidad_medida": "kg",
        "stock": 50
    },
    
    "pera": {
        "precio": 240.50,
        "unidad_medida": "kg",
        "stock": 40        
    },
    
    "frutilla": {
        "precio": 300,
        "unidad_medida": "kg",
        "stock": 100        
    }, 
    
    "mango" : {
        "precio": 300,
        "unidad_medida": "unidad",
        "stock": 100  
    }

}

# Punto 1: solicitar al usuario un producto y verificiar si existe en 'lista_precios' en caso de existir mostrar precio y el stock. En caso de no existir el 
# producto mostrar el mensaje 'el articulo no se encuentra en la lista'


# Punto 2: agregar al punto anterior que el usuario ingrese la cantidad y retornar el precio total (precio * cantidad)


# Punto 3: solicitar al usuario que ingrese una nueva fruta junto con su precio, unidad de medida y stock. Agregar la nueva fruta a la lista de precios


# Punto 4: imprimir el listado de frutas (solo su nombre)


# Punto 5: solicitarle al usuario el nombre de fruta y en caso de exisitir eliminarla. En caso de que el producto no exista mostrar 
# el mensaje 'el articulo no se encuentra en la lista'

#Punto 1:
def imprimir_precio_fruta():
    fruta = input("Ingrese la fruta a buscar: >>>")
    msg_error = 'Key inexistente'
    prod_dict = lista_precios.get(fruta, 'el articulo no se encuentra en la lista')
    if not type(prod_dict) == str:
        precio = prod_dict.get("precio", msg_error)
        stock = prod_dict.get("stock", msg_error)
        if precio == msg_error:
            print(prod_dict)
        else:
            print(f'El precio de {fruta} es: ${precio} y el stock es de: {stock}')
    else:
        print(prod_dict)

# Punto 2:
def calcular_precio_final():        
    msg_error = 'Key inexistente'
    fruta = input("Ingrese la fruta a buscar: >>>")
    prod_dict = lista_precios.get(fruta, 'el articulo no se encuentra en la lista')
    if not type(prod_dict) == str:
        precio = prod_dict.get("precio", msg_error)
        if not type(precio) == str:
            cantidad = int(input("Ingrese la cantidad: >>>"))
            precio_total = cantidad * precio
            print("El precio final es: ${0}".format(precio_total))
        else:
            print(msg_error)
    else:
        print(prod_dict)

# Punto 3:
def anadir_frutas(frutas: dict)-> dict:
    frutas_copy = frutas.copy()
    nueva_fruta = input("Ingrese el nombre de la fruta a agregar: >>>")
    nuevo_precio = input("Ingrese el precio: >>> $")
    nueva_medida = int(input("Ingrese la nueva unidad de medida a agregar: kg, unidad >>>"))
    nuevo_stock = int(input("Ingrese el stock de la fruta: >>>"))

    fruta_dict = dict()
    fruta_dict[nueva_fruta] = {}
    fruta_dict[nueva_fruta]['stock'] = nuevo_stock
    fruta_dict[nueva_fruta]['precio'] = nuevo_precio
    fruta_dict[nueva_fruta]['medida'] = nueva_medida

    frutas_copy.update(fruta_dict)

    return frutas_copy

# Punto 4:
print(list(lista_precios.keys()))

# Punto 5:
def buscar_eliminar(lista: list[dict]):
    frutas_copy = lista.copy()
    fruta_busqueda = (input("Que fruta desea eliminar?: >>>")).lower()
    if fruta_busqueda in lista.keys():
        frutas_copy.pop(fruta_busqueda)
    else:
        print('el articulo no se encuentra en la lista')
    return frutas_copy
print(buscar_eliminar(lista_precios))

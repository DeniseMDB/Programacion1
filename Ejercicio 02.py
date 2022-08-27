#Denise Du Bois 
#La división de alimentos está trabajando en un pequeño software para cargar
#las compras de ingredientes para la cocina de Industrias Wayne. 
#Realizar el algoritmo permita ingresar los datos de una compra de ingredientes para
#preparar comida al por mayor, HASTA QUE EL CLIENTE QUIERA.
#PESO: (entre 10 y 100 kilos)
#PRECIO POR KILO: (mayor a 0 [cero]).
#TIPO VALIDAD: ("v", "a", "m");(vegetal, animal, mezcla).
#Además tener en cuenta que si compro más de 100 kilos en total tenes 15% de descuento sobre el precio bruto.
# o si compro más de 300 kilos en total, tenes 25% de descuento sobre el precio bruto.
#El importe total a pagar, BRUTO sin descuento.
#El importe total a pagar con descuento (Solo si corresponde).
#Informar el tipo de alimento más caro.
#El promedio de precio por kilo en total.


respuesta = True
flag_maximo = True
acumulador_peso = 0
acumulador_precio = 0

while (respuesta):
    peso = int(input("Ingrese el peso: "))
    while peso < 10 and peso > 100:
        peso = int(input("Ingrese el peso: "))    

    precio = int(input("Ingrese el precio: "))
    while precio <0 :
        precio = int(input("Ingrese el precio: "))

    tipo_alimento = str.lower(input("Ingrese el tipo de alimento (vegetal, animal o mezcla) v, a o m : "))
    while tipo_alimento != "v" and tipo_alimento != "a" and tipo_alimento != "m":
        tipo_alimento = str.lower(input("Ingrese el tipo de alimento (v, a o m) : "))

    if (peso > 100):
        descuento = 0.85
    elif (peso > 300):
        descuento = 0.75
    else:
        descuento = 1

    if (flag_maximo):
        alimento_caro = tipo_alimento
        precio_caro = precio
        flag_maximo = False
    elif (precio_caro < precio):
        precio_caro = precio
        alimento_caro = tipo_alimento

    acumulador_peso += peso
    acumulador_precio += precio

    confirmar = str.lower(input("Desea continuar? Si o No"))
    if (confirmar == "no"):
        respuesta = False
    

promedio = acumulador_peso/acumulador_precio
importe_bruto = peso * precio   
importe_final = importe_bruto * descuento
if (alimento_caro == "a"):
    alimento_caro = "Animal"
elif (alimento_caro == "v"):
    alimento_caro = "Vegetal"
else:
    alimento_caro = "Mezcla"

#El importe total a pagar, BRUTO sin descuento.
#El importe total a pagar con descuento (Solo si corresponde).
#Informar el tipo de alimento más caro.
#El promedio de precio por kilo en total.

print("EL importe bruto a pagar es: $", importe_bruto)
print("EL importe final a pagar es: $", importe_final)
print("EL tipo de alimento mas caro es: ", alimento_caro)
print("EL promedio es: ", promedio)





    


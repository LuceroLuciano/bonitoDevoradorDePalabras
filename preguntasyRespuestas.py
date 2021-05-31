"""
Objetivos

    Familiarizarse con la función input().
    Familiarizarse con los operadores de comparación en Python.

    #PRUEBA DE LABORATORIO MODULO - 3
"""
#n = int(input("Introduce un entero: "))
#print(n >= 100)

#numero mayor de tres numeros

#lee tres números

"""
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))
numero3 = int (input("Ingresa el tercer número:"))


nmasGrande = numero1

if numero2 > nmasGrande:
    nmasGrande = numero2

if numero3 > nmasGrande:
    nmasGrande = numero3

print("El número más grande es:", nmasGrande)
"""

#Prueba de laboratorio

"""
nombrePlanta = input("Ingresa nombre de planta: ")

if nombrePlanta == "Espatifilo":
    print("¡Si, " + nombrePlanta + " es la mejor planta de todas!!")

elif nombrePlanta == "espatifilo":
    print("No, ¡quiero un gran " + "Espatifilo!")

else:
    print("¡Espatifilo! ¡NO " + nombrePlanta + "!")
"""

#Prueba de laboratorio

"""
ingreso=float(input("Ingrese el ingreso anual:"))

extencion_fiscal = 556.2

if ingreso < 85528:
    #calculo del impuesto
    impuesto = (((ingreso * 18) / 100) - extencion_fiscal)

else:
    #calculo del impuesto
    excedente = ingreso - 85528
    impuesto = (((excedente * 32) / 100) + 14839.2)

#si el calculo del impuesto es menor a 0
#el impuesto sera de 0.0
if impuesto < 0:
    impuesto = 0.0;

impuesto=round(impuesto, 0)
print("El impuesto es: ", impuesto, "pesos")

"""

#Prueba de laboratorio
año = int(input("Introduzca un año:"))

if año > 1582:
    if año % 4:
        print("Año comun")
    elif año % 100:
        print("Año bisiesto")
    elif año % 400:
        print("Año comun")
    else:
        print("Año bisiesto")
else:
    print("No dentro del perido del calendario Greogoriano")
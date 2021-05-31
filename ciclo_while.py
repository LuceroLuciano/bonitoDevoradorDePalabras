"""
#Almacenamos el numero mas grande actual aqui
maximumNumber = -999999999

#ingresa el primer valor
number = int(input("Input a number or writting -1 to stop: "))

#si el numero no es igual a -1, continuaremos
while number != -1:
    #¿Es el numero mas grande que el numero mas grande?
    if number > maximumNumber:
        #Si si, actualiza el mayor numero Numero
        maximumNumber = number
    #Ingresa el siguieente numero
    number = int(input("Input a number or writting -1 to stop: "))

#print the maximum Number
print("The maximum number is: ", maximumNumber)

"""
#--------------------------------------------------------------------------------------------
"""
# Almacenaremos el número más grande actual aquí
numeroMayor = -999999999

# Ingresa el primer valor
numero = int(input ("Introduzca un número o escriba -1 para detener:"))

# Si el número no es igual a -1, continuaremos
while numero != -1:
    # ¿Es el número más grande que el número más grande?
    if numero > numeroMayor:
        # Sí si, actualiza el mayor númeroNúmero
        numeroMayor = numero
    # Ingresa el siguiente número
    numero = int(input("Introduce un número o escribe -1 para detener:"))

# Imprimir el número más grande
print("El número más grande es:", numeroMayor)
"""

#------------------------------------------------------------------------------
numeroSecreto = 777

print(
    """
    +==================================+
    | Bienvenido a mi juego, muggle!   |
    | Introduce un número entero       |
    | y adivina qué número he          |
    | elegido para ti.                 |
    | Entonces,                        |
    | ¿Cuál es el número secreto?      |
    +==================================+
    """)
# pedir un numero al usuario
numero = int(input("Ingresa un numero entero: "))

while numero != numeroSecreto:
    if numero != numeroSecreto:
        print("¡Ja, Ja! ¡Estas atrapado en mi ciclo!")
        numero = int(input("Ingresa un numero entero: "))

print("¡Bien  hecho, muggle! Eres Libre ahora")
#ciclo while y la rama else
"""
i = 6

while i < 5:
    print(i)
    i += 1
else:
    print("else: ", i)
"""

"""
# 3.1.2.14 LABORATORIO: Lo fundamental del ciclo while
bloques = int(input("Ingrese el número de bloques:"))

altura = 0
baseBlock = 1

while baseBlock < bloques:
    altura += 1
    bloques -= baseBlock
    baseBlock += 1

print("La altura de la pirámide:", altura)
"""

"""
#3.1.2.15 LABORATORIO: Hipótesis de Collatz

# lee un numero entero positivo
numero = int(input("Ingresa un numero etero positivo: "))

# asigna el valor del numero a c0
c0 = numero
pasos = 0

while c0 != 1:
    # si c0 es par
    # entonces evalua un nuemo c0 como c0/2
    if c0 % 2 == 0:
        c0 = c0 // 2
        print(c0)
    # de lo contrario, si es impar
    else:
        # evalue c0 como 3 * c0 +1
        c0 = 3 * c0 + 1
        print(c0)

    pasos += 1
print("pasos", pasos)
"""

"""
#ejercicio 1- puntos clave sobre los ciclos
#Crea un bucle for que cuente de 0 a 10,
#e imprima números impares en la pantalla.
# Usa el esqueleto de abajo:

for i in range(0, 11):
    #if el modulo de i es igual a 1 etinces es numero PAR
    if i % 2 == 1:
        print(i)
"""

"""
#ejercicio 2
#Crea un bucle while que cuente de 0 a 10, e imprima
#números impares en la pantalla. Usa el esqueleto de abajo:

x = 1
while x < 11:
    if x % 2 != 0:
        print(x)
    x += 1
"""

"""
#ejercicio 3
#Crea un programa con un bucle for y una declaración break.
#El programa debe iterar sobre los caracteres en una dirección
#de correo electrónico, salir del bucle cuando llegue al símbolo @
# e imprimir la parte antes de @ en una línea. Usa el esqueleto
# de abajo:

for caracter in "innovaccion.virtual@microsoft.org":
    if caracter == "@":
        break
    print(caracter, end="")
"""

"""
#ejercicio 4
#Crea un programa con un bucle for y una declaracióncontinue.
# El programa debe iterar sobre una cadena de dígitos,
# reemplazar cada 0 con x, e imprimir la cadena modificada
# en la pantalla. Usa el esqueleto de abajo:

for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")
"""

"""
#ejercicio 5

n = 3

while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)
"""

"""
#ejercicio 6
# ¿Cuál es la salida del siguiente codigo?
n = range(4)

for num in n:
    print(num - 1)
else:
    print(num)
"""

"""
#ejercicio 7
#¿cual es la salida del siguiente código?

for i in range(0, 6, 3):
    print(i)
"""

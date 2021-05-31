"""
LABORATORY - The basic of list

Objetives:
 - use the instruccions basic related with list.
 - create and modifc list

Scenario:
there one day a hat. The hat no have rabbit, if no have it
a ist of five numbers: 1, 2, 3, 4, 5

Your task is:
- Writte a line of code that give to the user that
  remplace the number central in the list with a int numner
  ingresado for the user (step 1)

- Writting a line of code taht deleted the end numeber
  of the list (step 2)

- Writting a line of code that print the lend of the list
 existent (step 3)
"""
listaSombrero = [1, 2, 3, 4, 5] # Esta es una lista existente de números ocultos en el sombrero.
print("La lista actual es:", listaSombrero)
# Paso 1: escribe una línea de código que solicite al usuario
# para reemplazar el número de en medio con un número entero ingresado por el usuario.

numero = int(input("Ingrese un numero entero: "))
listaSombrero [2] = numero
print("La listaSombrero con el numero que ingreso el usuario es:", listaSombrero)

# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del listaSombrero[4]
print("La lista previa con el ultimo elemnto eliminado es:", listaSombrero)
# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print("La longitud de la lista es:", len(listaSombrero))

"""
Objetivos:
    Familiarizarse con la función input().
    Familiarizarse con los operadores de comparación en Python.
    Encontrar el numero mas grande de tres numeros.
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
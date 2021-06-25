"""
Objetivo:

    -Crea un programa con un bucle for y una declaración break.
    -El programa debe iterar sobre los caracteres en una dirección
     de correo electrónico, salir del bucle cuando llegue al símbolo @
    -imprimir la parte antes de @ en una línea. 
"""

for caracter in "innovaccion.virtual@microsoft.org":
    if caracter == "@":
        break
    print(caracter, end="")

"""
Objetivo:
    -Utilizar la función continue de los ciclos
    -Ciclo for
    -condicional (if-elif-else)

    Tu programa debe:

    -Pedir al usuario que ingrese una palabra.
    -Utilizar userWord = userWord.upper() para convertir la palabra ingresada por el usuario a mayúsculas;
    -Usa la ejecución condicional y la instrucción continue para "comer" las siguientes vocales A , E , I , O , U de la palabra ingresada.
    -Asigne las letras no consumidas a la variable palabrasinVocal e imprime la variable en la pantalla.

"""
print ("""
        +----------------------------------+
        |  El bonito devorador de palabras |
        +----------------------------------+
        """)

# palabraSinVocal = ""

userWord = input("Ingrese una palabra: ")
userWord = userWord.upper()

for letra in userWord:
    if letra == "A":
        continue
    elif letra == "E":
        continue
    elif letra == "I":
        continue
    elif letra == "O":
        continue
    elif letra == "U":
        continue
    else:
        palabraSinVocal = letra
        print(palabraSinVocal, end="")

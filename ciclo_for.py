"""
#Cilo for con un argumento
 for i in range(10):
   print("El valor de i es actualmente", i)
"""

"""
#cilo for con dos argumentos
for i in range(2, 8):
    print("El valor de i es actualmente", i)
"""

"""
#ciclo for con tres arguemntos

for i in range(2, 8, 3):
    print("El valor de i actualmente es", i)

"""

#Laboratorio

"""
import time

for i in range(1, 6): # Escribe un ciclo for que cuente hasta cinco.
    print(i, "Mississippi") # Cuerpo del ciclo: imprime el número de iteración del ciclo y la palabra "Mississippi".
    time.sleep(3)  #esperar tres segundos para imprimir cada mensaje

# Escribe una función de impresión con el mensaje final.
print("¡Listo o no!, ahi voy!")
"""


"""
#LABORATORIO - DECLARACION BREAK - ATASCADA EN UN CILO

palabraSecreta = "chupacabra"

while True:
    palabraIntroducida = input("Ingresa una palabra: ")
    if palabraIntroducida == palabraSecreta:
        print("¡Has dejado el ciclo con exito!")
        break

"""

# La sentencia continue - El Feo Devorador de Vocales
print("""
    +----------------------+
    | El Feo devorador de  |
    |   palabras [^~^]     |
    +----------------------+
    """)

userWord = input("Ingresa una palabra: ")
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
        print(letra)

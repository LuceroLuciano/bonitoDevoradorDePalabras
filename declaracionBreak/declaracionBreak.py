#LABORATORIO - DECLARACION BREAK - ATASCADA EN UN CILO

palabraSecreta = "chupacabra"

while True:
    palabraIntroducida = input("Ingresa una palabra: ")
    if palabraIntroducida == palabraSecreta:
        print("¡Has dejado el ciclo con exito!")
        break
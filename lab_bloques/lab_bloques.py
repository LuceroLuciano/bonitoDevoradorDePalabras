#LABORATORIO: Lo fundamental del ciclo while

bloques = int(input("Ingrese el número de bloques:"))

altura = 0
baseBlock = 1

while baseBlock < bloques:
    altura += 1
    bloques -= baseBlock
    baseBlock += 1

print("La altura de la pirámide:", altura)







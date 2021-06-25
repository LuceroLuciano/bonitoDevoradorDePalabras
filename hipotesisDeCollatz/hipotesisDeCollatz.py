#LABORATORIO: Hipótesis de Collatz

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

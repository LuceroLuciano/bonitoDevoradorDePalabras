#Operaciones basicas

print(8 * " " + "+" + 26 * "-" + "+")
print(8 * " " + "|" + 3 * " " + "OPERACIONES BASICAS" + 4 * " " + "|\n", end="")
print(8 * " " + "+" + 26 * "-" + "+" + "\n")

numero_a = float(input("Ingresa un valor numerico para la variable a: "))
numero_b = float(input("Ingresa un valor numerico para la variable b: "))

resta = numero_a - numero_b
multiplicacion = numero_a * numero_b
division =  numero_a / numero_b

print("\nLa suma de ", numero_a, "+", numero_b, "es: " + str(numero_a + numero_b))
print("La resta de " + str(numero_a) + " - " + str(numero_b) + " es ", resta)
print("El producto de " + str(numero_a) + " * " + str(numero_b) + " es " + str(multiplicacion))
print("La division de: ", numero_a, "/", numero_b, "es: ", division)



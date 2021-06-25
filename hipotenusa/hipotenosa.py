#Calculado la hipotenusa con vlores ingrsados

#La riaz cuadrada de X es = X ^ 0.5
#Ejemplo:
#La raiz cuadrada de 9 = 3
#Es lo mismo si elevamos 9 ^ 0.5 = 3

cateto_a = float(input("Inserta la longitud del primer cateto: "))
cateto_b = float(input("Inserta la longitud del segundo cateto: "))
hipotenusa = ((cateto_a ** 2 + cateto_b ** 2) ** .5)
print("La longitud de la hipotenusa es: ", hipotenusa)


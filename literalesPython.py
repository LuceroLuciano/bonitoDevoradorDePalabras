print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

#Teorema de pitágoras

a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c=", c)

#desafio de LABORATORIO
"""
Érase una vez en la Tierra de las Manzanas, Juan tenía tres manzanas, María tenía cinco manzanas, y Adán tenía seis manzanas. Todos eran muy felices y vivieron por muchísimo tiempo. Fin de la Historia.

Tu tarea es:

    Crear las variables: juan, maria, y adan.
    Asignar valores a las variables. El valor debe de ser igual al numero de manzanas que cada quien tenía.
    Una vez almacenados los números en las variables, imprimir las variables en una línea, y separar cada una de ellas con una coma.
    Después se debe crear una nueva variable llamada totalManzanas y se debe igualar a la suma de las tres variables anteriores.
    Imprime el valor almacenado en totalManzanas en la consola.
    Experimenta con tu código: crea nuevas variables, asigna diferentes valores a ellas, y realiza varias operaciones aritméticas con ellas (por ejemplo, +, -, *, /, //, etc.). Intenta poner una cadena con un entero juntos en la misma línea, por ejemplo, "Numero Total de Manzanas:" y totalManzanas.

"""
juan = 3
maria = 5
adan = 6

print(juan, maria, adan, sep=", ")

totalManzanas = juan + maria + adan
print("El numero total de manzanas es: ", totalManzanas, "\n")

#DESAFIO2 DE LABORATORIO
#conversion de millas a kilometros

"""

"""

# 1 m = 1.61 Km

kilometros = 12.25
millas = 7.38

millas_a_kilometros = millas * 1.61
kilometros_a_millas = kilometros / 1.61

print(millas, "millas son", round(millas_a_kilometros, 2), "Kilometros ")
print(kilometros, "kilometros son", round(kilometros_a_millas, 2), "Millas \n")


#conversiones de temperatura
"""
    De Celsius a Kelvin: KELVIN = CELSIUS + 273.15.
    De Celsius a Farenheit: FARENHEIT = (CELSIUS) *9/5 + 32.
    De Farenheit a Celsius: CELSIUS = (FARENHEIT – 32) * (5/9)
    De Farenheit a Kelvin: KELVIN = (FARENHEIT – 32) * (5/9) + 273.15.
    De Kelvin a Celsius: CELSIUS = KELVIN – 273.15.
"""
#conversiones de temperatura
celsius = 27
farenheit = 80
kelvin = 24

celsius_a_kelvin = celsius + 237.15
celsius_a_farenheit = ((celsius * (9 / 5)) + 32)
farenheit_a_celsius = ((farenheit - 32) * (5 / 9))
farenheit_a_kelvin = (((farenheit - 32) * (5 / 9)) + 237.15)
kelvin_a_celsius = kelvin - 237

print(celsius, "°Celsius equivalen a", round(celsius_a_kelvin, 2), "°Kelvin")
print(celsius, "°Celsius equivalen a", round(celsius_a_farenheit, 2), "°Farenheit")
print(farenheit, "°Farenheit equivalen a", round(farenheit_a_celsius, 2), "°Celsius")
print(farenheit, "°Farenheit equivalen a", round(farenheit_a_kelvin, 2), "°Kelvin")
print(kelvin, "°kelvin equivalen a", round(kelvin_a_celsius, 2), "°Celsius \n")


#Desafio3 LABORATORIO
"""
Escenario

Observa el código en el editor: lee un valor flotante, 
lo coloca en una variable llamada x, 
e imprime el valor de la variable llamada y. 

Tu tarea es completar el código para evaluar la siguiente expresión:

3x3 - 2x2 + 3x - 1

El resultado debe ser asignado a y.

Recuerda que la notación algebraica clásica muy seguido 
omite el operador de multiplicación, aquí se debe de incluir de manera explicita. 
Nota como se cambia el tipo de dato para asegurarnos de que x es del tipo flotante.

Mantén tu código limpio y legible, y pruébalo utilizando los datos que han sido proporcionados. 
No te desanimes por no lograrlo en el primer intento. Se persistente y curioso. 

"""
#expresion
# 3x3 - 2x2 + 3x - 1

#datos de prueba
# X = 0, x =  1, X = -1
# y = -1.0, y = 3.0, y = -9.0

x = 0
x = float(x)
y = ((3 * (x ** 3)) - (2 * (x ** 2)) + (3 * x) -1)
print("y =", y)

#pruebas con comentarios

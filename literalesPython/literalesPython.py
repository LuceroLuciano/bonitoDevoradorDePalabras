#Desafio3 LABORATORIO
"""
Escenario:

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

Expresion:
    3x3 - 2x2 + 3x - 1

Datos de prueba:
    X = 0, x =  1, X = -1
    y = -1.0, y = 3.0, y = -9.0

"""

x = 0
x = float(x)
y = ((3 * (x ** 3)) - (2 * (x ** 2)) + (3 * x) -1)
print("y =", y)
print("\n-----------------------------------------------------------")

#Jerarquia de operaciones
print("\nPequeño ejemplo de jerarquia de operaciones")
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
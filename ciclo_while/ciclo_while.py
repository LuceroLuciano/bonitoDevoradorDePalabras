"""
objetivos:
    usar el cilo while
    adivinar un nuemro secreto
"""

numeroSecreto = 777

print(
    """
    +==================================+
    | Bienvenido a mi juego, muggle!   |
    | Introduce un número entero       |
    | y adivina qué número he          |
    | elegido para ti.                 |
    | Entonces,                        |
    | ¿Cuál es el número secreto?      |
    +==================================+
    """)
# pedir un numero al usuario
numero = int(input("Ingresa un numero entero: "))

while numero != numeroSecreto:
    if numero != numeroSecreto:
        print("¡Ja, Ja! ¡Estas atrapado en mi ciclo!")
        numero = int(input("Ingresa un numero entero: "))

print("¡Bien  hecho, muggle! Eres Libre ahora")
"""
Compara una palabra con el nombre de la planta:
Espatifilo, si el nombre es el mismo muestra
un mensaje
"""

nombrePlanta = input("Ingresa nombre de planta: ")

if nombrePlanta == "Espatifilo":
    print("¡Si, " + nombrePlanta + " es la mejor planta de todas!!")

elif nombrePlanta == "espatifilo":
    print("No, ¡quiero un gran " + "Espatifilo!")

else:
    print("¡Espatifilo! ¡NO " + nombrePlanta + "!")
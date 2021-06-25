#Prueba de laboratorio
año = int(input("Introduzca un año:"))

if año > 1582:
    if año % 4:
        print("Año comun")
    elif año % 100:
        print("Año bisiesto")
    elif año % 400:
        print("Año comun")
    else:
        print("Año bisiesto")
else:
    print("No dentro del perido del calendario Greogoriano")
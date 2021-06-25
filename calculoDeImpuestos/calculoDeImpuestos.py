"""
Calculo de impuestos
"""
ingreso=float(input("Ingrese el ingreso anual:"))

extencion_fiscal = 556.2

if ingreso < 85528:
    #calculo del impuesto
    impuesto = (((ingreso * 18) / 100) - extencion_fiscal)

else:
    #calculo del impuesto
    excedente = ingreso - 85528
    impuesto = (((excedente * 32) / 100) + 14839.2)

#si el calculo del impuesto es menor a 0
#el impuesto sera de 0.0
if impuesto < 0:
    impuesto = 0.0;

impuesto=round(impuesto, 0)
print("El impuesto es: ", impuesto, "pesos")
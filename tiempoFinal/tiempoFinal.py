#Encontrar el tiempo final de un periodo de
#tiempo dado, expresandolo en horas y minutos.
#Las horas van de 0 a 23 y los minutos de 0 a 59


hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

#convesion de horas a minutos
#1 hr = 60 min

tiempo_final_minutos = (min + dura)
conversion_minutos_a_horas = (tiempo_final_minutos % 60)
horas = ((tiempo_final_minutos // 60) + hora)
conversion_horas_a_minutos = (horas % 24)

tiempo_final = (conversion_horas_a_minutos, ":", conversion_minutos_a_horas)
print(tiempo_final)

print(str(conversion_horas_a_minutos) + ":" + str(conversion_minutos_a_horas))

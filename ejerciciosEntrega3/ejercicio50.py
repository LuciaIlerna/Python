# 50. Una persona se encuentra en el kilómetro 70 de una carretera, otra se encuentra en el km
# 150, los coches tienen sentido opuesto y tienen la misma velocidad. Realizar un programa para
# determinar en qué kilómetro de esa carretera se encontrarán.

km_persona1 = 70
km_persona2 = 150

velocidad = float(input("Introduce la velocidad de los coches (km/h): "))

distancia = km_persona2 - km_persona1
tiempo_encuentro = distancia / (2 * velocidad)
km_encuentro = km_persona1 + velocidad * tiempo_encuentro

print("Los coches se encontrarán en el kilómetro:", km_encuentro)

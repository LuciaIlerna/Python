# 7. Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas
#horas y minutos corresponde.

minutos = int(input("Introduce una cantidad de minutos: "))

horas = minutos // 60
minutos_restantes = minutos % 60

print(horas, "horas", "y", minutos_restantes, "minutos")
# 17. Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de
#viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora
#de llegada a la ciudad B.

HH = int(input("Hora de salida (0-23): "))
MM = int(input("Minutos de salida (0-59): "))
SS = int(input("Segundos de salida (0-59): "))

T = int(input("Tiempo de viaje en segundos: "))

# Convertir a segundos
salida_total = HH * 3600 + MM * 60 + SS

# Sumar tiempo de viaje
llegada_total = salida_total + T

# Ajustar si pasa de 24 horas
llegada_total %= 86400

# Volver a HH:MM:SS
HH_l = llegada_total // 3600
MM_l = (llegada_total % 3600) // 60
SS_l = llegada_total % 60

print("Hora de llegada:", HH_l, "horas,", MM_l, "minutos y", SS_l, "segundos")

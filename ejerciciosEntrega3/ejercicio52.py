# 52. Una empresa les paga a sus empleados con base en las horas trabajadas en la semana.
# Realice un algoritmo para determinar el sueldo semanal de N trabajadores y, además, calcule
# cuánto pagó la empresa por los N empleados.

N = int(input("Ingrese el número de trabajadores: "))
sueldo_total = 0

for i in range(1, N + 1):
    horas_trabajadas = float(input(f"Ingrese las horas trabajadas por el trabajador {i}: "))
    tarifa_hora = float(input(f"Ingrese la tarifa por hora del trabajador {i}: "))
    sueldo_semanal = horas_trabajadas * tarifa_hora
    sueldo_total += sueldo_semanal
    print(f"Sueldo semanal del trabajador {i}: {sueldo_semanal} euros")
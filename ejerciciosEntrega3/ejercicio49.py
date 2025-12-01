# # 49. Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la
# semana (seis días) y requiere determinar el total de éstas, así como el sueldo que recibirá por
# las horas trabajadas.

precio = float(input("Cuanto ganas por hora? "))

horas_totales = 0

print("Introduce horas trabajadas cada dia:")

for i in range(6):
    horas = float(input("Dia " + str(i+1) + ": "))
    horas_totales = horas_totales + horas

sueldo = horas_totales * precio

print("Horas totales:", horas_totales)
print("Sueldo:", sueldo)
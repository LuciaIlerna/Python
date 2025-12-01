# 34. Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta

dia = str(input("Introduce el día: "))
mes = str(input("Introduce el mes: "))
año = str(input("Introduce el año: "))

if dia == "lunes":
    print("El dia es correcto.")
else:
    print("El dia es incorrecto.")

if mes == "diciembre":
    print("El mes es correcto.")
else:
    print("El mes es incorrecto.")
    
if año == "2025":
    print("El año es correcto.")
else:
    print("El año es incorrecto.")
#31. El director de una escuela está organizando un viaje de estudios, y requiere determinar
#cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio.
#La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada alumno es de 65
#euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos de
#30, el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos.
#Realice un algoritmo que permita determinar el pago a la compañía de autobuses y lo que
#debe pagar cada alumno por el viaje.

print("Introduce el número de alumnos para el viaje de estudios:")

alumnos = int(input("Introduce el número de alumnos: "))

if alumnos >= 100:
    costo_por_alumno = 65
    pago_compañia = alumnos * costo_por_alumno
    
elif 50 <= alumnos <= 99:
    costo_por_alumno = 70
    pago_compañia = alumnos * costo_por_alumno
    
elif 30 <= alumnos <= 49:
    costo_por_alumno = 95
    pago_compañia = alumnos * costo_por_alumno
    
elif alumnos < 30:
    costo_por_alumno = 4000
    pago_compañia = 4000
    
print("El pago a la compañía de autobuses es de:", pago_compañia, "euros.")
print("El costo por alumno es de:", costo_por_alumno, "euros.")

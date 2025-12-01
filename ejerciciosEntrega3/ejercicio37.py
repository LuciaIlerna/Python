# 37. Una compañía de transporte internacional tiene servicio en algunos países de América del
# Norte, América Central, América del Sur, Europa y Asia. El costo por el servicio de transporte se
# basa en el peso del paquete y la zona a la que va dirigido...

peso = float(input("Introduce el peso del paquete en kg: "))
zona = int(input("Introduce la zona de destino (1: América del Norte, 2: América Central, 3: América del Sur, 4: Europa, 5: Asia): "))

if zona == 1:
    costo = peso * 11.00
elif zona == 2:
    costo = peso * 10.00
elif zona == 3:
    costo = peso * 12.00
elif zona == 4:
    costo = peso * 24.00
elif zona == 5:
    costo = peso * 27.00
else:
    print("Zona no válida")
    costo = 0

# Mostrar el resultado
if costo > 0:
    print("Costo total: ", costo, "euros")
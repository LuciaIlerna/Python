# 25. La universidad ha categorizado las matrículas de acuerdo a la facultad que va a estudiar el
#postulante. Ingrese por teclado el nombre del postulante y la facultad que va a estudiar, muestre
#el importe, la mensualidad, el IGV 18% (importe + mensualidad) y el monto final a pagar. (Use el
#control switch).

nombre = str(input("Introduce el nombre del postulante: "))
facultad = str(input("Introduce la facultad: ")).lower()

importe = 0
mensualidad = 0
boolean = False

if facultad == "ing. de sistemas":
    importe = 350
    mensualidad = 650
    
elif facultad == "derecho":
    importe = 300
    mensualidad = 550
    
elif facultad == "ing. saviera":
    importe = 300
    mensualidad = 500
    
elif facultad == "ing. pesquera":
    importe = 310
    mensualidad = 460
    
elif facultad == "contabilidad":
    importe = 280
    mensualidad = 490
    
elif facultad == "administración":
    importe = 280
    mensualidad = 520

else:
    boolean = True

igv = (importe + mensualidad) * 0.18
montoFinal = importe + mensualidad + igv

if boolean == False:
    
    print("Postulante: ", nombre)
    print("Facultad: ", facultad)
    print("Importe: ", importe)
    print("Mensualidad: ", mensualidad)
    print("IGV: ", igv)
    print("Monto final: ", montoFinal)
else:
    print("No has introducido ninguna de las facultades disponibles.")
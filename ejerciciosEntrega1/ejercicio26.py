# 26. En un casino de juegos se desea mostrar los mensajes respectivos por el puntaje obtenido
#en el lanzamiento de tres dados de un cliente, de acuerdo a los siguientes resultados:
#Si los tres dados son seis, mostrar el mensaje “Excelente”
#Si dos dados se obtienen seis, mostrar el mensaje “Muy bien”
#Si un dado se obtiene seis, mostrar el mensaje “Regular”
#Si ningún dado se obtiene seis, mostrar el mensaje “Pésimo”
#(Use el control switch).
import random

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
dado3 = random.randint(1, 6)

print("Dado 1:", dado1, "Dado 2:", dado2, "Dado 3:", dado3)

if dado1 == 6 and dado2 == 6 and dado3 == 6:
    print("Excelente")
    
elif dado1 == 6 and dado2 == 6 or dado1 == 6 and dado3 == 6 or dado2 == 6 and dado3 == 6:
    print("Muy bien")
    
elif dado1 == 6 or dado2 == 6 or dado3 == 6:
    print("Regular")
    
else:
    print("Pésimo")

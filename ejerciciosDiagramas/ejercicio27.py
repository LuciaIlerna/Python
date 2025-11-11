bandera = False
num = 11

while num != -1:
    num = int(input("Introduce un número que vaya del 0 al 10 ó -1 para terminar la secuencia: "))
    if num >= 0 and num <= 10:
        if num == 10:
            bandera = True
    else:
        print("Error. Introduce un número válido")
if bandera:
    print("Ha habido un 10")
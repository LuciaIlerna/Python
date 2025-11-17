# 16. Programa que lee una secuencia de notas (con valores que van de 0 a 10) que termina con
#el valor -1 y nos dice si hubo o no alguna nota con valor 10.

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
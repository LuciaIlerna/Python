# 40. Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la
# media de todos los números introducidos.

suma = 0
contador = 0
num = 1

while num != 0:
    num = int(input("Numero: "))
    if num != 0:
        suma = suma + num
        contador = contador + 1

if contador > 0:
    print("Suma:", suma)
    print("Media:", suma / contador)
else:
    print("No hay numeros")
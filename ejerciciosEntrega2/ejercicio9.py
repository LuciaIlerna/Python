# 9. Programa que lea una secuencia de números no nulos hasta que se introduzca un 0, y luego
#muestre si ha leído algún número negativo, cuantos positivos y cuantos negativos.

pos = 0
neg = 0
num = 1  
while num != 0:
    num = int(input("Introduce un número: "))
    if num > 0:
        pos += 1
    else:
        neg += 1
print("El número introducido es cero.")
print("Se han introducido", pos, "números positivos")
print("Se han introducido", neg, "números negativos")
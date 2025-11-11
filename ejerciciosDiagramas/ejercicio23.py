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
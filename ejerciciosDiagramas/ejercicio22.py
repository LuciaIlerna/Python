pos = 0
neg = 0
cont = 0
while cont < 100:
    num = int(input("Introduce un número: "))
    
    if num != 0:
        cont += 1
        if num > 0:
            pos += 1
        else:
            neg += 1

    if num == 0:
        print("Error. No se puede introducir el número cero.")   
    
print("Se han introducido", pos, "números positivos")
print("Se han introducido", neg, "números negativos")
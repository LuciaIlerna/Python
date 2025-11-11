pares = 0
impares = 0

for i in range(100, 201):
    if i % 2 == 0:
        pares += i
    else:
        impares += i   
print("La suma de los números pares es: ", pares)
print("La suma de los números impares es: ", impares)
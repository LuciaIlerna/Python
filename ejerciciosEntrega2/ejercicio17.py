# 17. Programa que suma independientemente los pares y los impares de los números
#comprendidos entre 100 y 200, y luego muestra por pantalla ambas sumas.

pares = 0
impares = 0

for i in range(100, 201):
    if i % 2 == 0:
        pares += i
    else:
        impares += i   
print("La suma de los números pares es: ", pares)
print("La suma de los números impares es: ", impares)
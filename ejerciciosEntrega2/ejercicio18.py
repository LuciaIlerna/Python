# 18. Programa que calcule el valor A elevado a B (A^B) sin hacer uso del operador de potencia
#(^), siendo A y B valores introducidos por teclado, y luego muestre el resultado por pantalla.

pares = 0
impares = 0

for i in range(100, 201):
    if i % 2 == 0:
        pares += i
    else:
        impares += i   
print("La suma de los números pares es: ", pares)
print("La suma de los números impares es: ", impares)
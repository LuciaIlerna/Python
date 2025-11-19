# 18. Programa que calcule el valor A elevado a B (A^B) sin hacer uso del operador de potencia
#(^), siendo A y B valores introducidos por teclado, y luego muestre el resultado por pantalla.

res = 1
num = int(input("Introduce el valor de A: "))
exponente = int(input("Introduce el valor de B: "))
for i in range (1, exponente + 1):
    res = num * res
print("El resultado de A elevado a B es: ", res)
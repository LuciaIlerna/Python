# 13. Escriba un programa que lea dos números y lo visualiza en orden ascendente.

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
if num1<num2:
    print(num1, "<", num2)
else:
    print(num2, "<", num1)
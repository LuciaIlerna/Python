# 14. Escriba un programa que lea dos números y nos diga cual es mayor o si son iguales.

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
if num1 == num2:
    print("Los números son iguales.")
elif num1 > num2:
    print("El número mayor es: ", num1)
else:
    print("El número mayor es: ", num2)

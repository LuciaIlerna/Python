# 15. Escriba un programa que lea tres números y nos diga cual es mayor, cual menor y cuales son iguales.

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))  
num3 = int(input("Introduce el tercer número: "))
if num1 == num2 == num3:
    print("Los números son iguales.")  
elif num1 == num2:
    print("El número 1 y el número 2 son iguales. El númer mayor es:", max(num1, num3), "y el menor es: ", min (num1, num3))
elif num1 == num3:
    print("El número 1 y el número 3 son iguales. El númer mayor es:", max(num1, num2), "y el menor es: ", min (num1, num2))
elif num2 == num3:
    print("El número 2 y el número 3 son iguales. El númer mayor es:", max(num2, num1), "y el menor es: ", min (num2, num1))
else:
    print("El número mayor es:", max(num1, num2, num3))
    print("El número menor es:", min(num1, num2, num3))
# 23. Crea un programa que pida al usuario dos números y muestre su división si el segundo no
#es cero, o un mensaje de aviso en caso contrario.

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if num2 != 0:
    print("La división es:", num1 / num2)
else:
    print("Error: no se puede dividir entre cero.")

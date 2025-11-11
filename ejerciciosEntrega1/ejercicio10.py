# 10. Escriba un programa que lea dos números, calcule y muestre el valor de sus suma, resta, producto y división (Ten en cuenta la división por cero)

num1 = int(print("Introduce el primer número: "))
num2 = int(print("Introduce el segundo número: "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
if num2 == 0:
    print("No se puede dividir entre cero")
    print("La suma es:", suma, "\n"
          "La resta es:", resta, "\n"
          "La multiplicación es:", multiplicacion,  "\n")
else:
    division= num1 / num2
    print("La suma es:", suma, "\n"
          "La resta es:", resta, "\n"
          "La multiplicación es:", multiplicacion,  "\n"
          "La división es:", division)
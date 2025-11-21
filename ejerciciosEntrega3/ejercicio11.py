# 11. Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su
#diferencia, de modo que el resultado sea siempre positivo).

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

'''
if num1 > num2:
    distancia = num1 - num2
else:
    distancia = num2 - num1
'''

distancia = abs(num1 - num2)


print("La distancia entre", num1, "y", num2, "es:", distancia)
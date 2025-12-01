# 29. Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los
#lados de un triángulo. El programa debe determinar qué tipo de triángulo es, teniendo en
#cuenta:
#• Si se cumple Pitágoras entonces es triángulo rectángulo
#• Si sólo dos lados del triángulo son iguales entonces es isósceles.
#• Si los 3 lados son iguales entonces es equilátero.
#• Si no se cumple ninguna de las condiciones anteriores, es escaleno.

A = float(input("Introduce el lado A: "))
B = float(input("Introduce el lado B: "))
C = float(input("Introduce el lado C: "))

# Si es rectángulo
if A**2 + B**2 == C**2 or A**2 + C**2 == B**2 or B**2 + C**2 == A**2:
    print("Triángulo rectángulo")
# Si les equilatero
elif A == B == C:
    print("Triángulo equilátero")
# Si es isosceles
elif A == B or A == C or B == C:
    print("Triángulo isósceles")
# Si es escaleno
else:
    print("Triángulo escaleno")

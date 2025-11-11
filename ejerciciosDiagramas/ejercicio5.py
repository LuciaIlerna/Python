import math
radio = int(input("Introduce la longitud del radio: "))
longitud = 2 * math.pi * radio
area = math.pi * radio * radio
volumen = (4/3) * math.pi * radio**3
print("La longitud de la circunferencia es:", longitud, "\n"
      "El área del círculo es:", area, "\n"
      "El volumen de la esfera es:", volumen)
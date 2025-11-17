# 21. Escriba un programa que calcula el salario neto semanal de un trabajador en función del
#número de horas trabajadas y la tasa de impuestos de acuerdo a las siguientes hipótesis:
#• Las primeras 35 horas se pagan a tarifa normal.
#• Las horas que pasen de las 35 horas se pagan a 1,5 veces la tarifa normal.
#• Las tasas de impuesto son:
#o Los primeros 500€ son libres de impuestos.
#o Los siguientes 400€ tiene un 25% de impuesto.
#o Los restantes un 45% de impuesto.
#Escribe el nombre del trabajador, salario bruto, tasas y salario neto

horas = int(input("Introduce la cantidad de horas trabajadas: "))
tarifa = int(input("Introduce la tarifa: "))

dinero = 0
impuesto = 0

if horas <= 35:
    dinero = horas * tarifa
else:
    dinero += 35
    horas -= 35
    dinero += horas * tarifa * 1.5
    
if dinero > 500:
    sobra = dinero - 500
    
    if sobra > 400:
        impuesto1 = 400 * 0.25
        sobra -= 400
        
    impuesto2 = sobra * 0.45
    impuesto += impuesto1 + impuesto2
    
print("El dinero neto es: ", dinero - impuesto)
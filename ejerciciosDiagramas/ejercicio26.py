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
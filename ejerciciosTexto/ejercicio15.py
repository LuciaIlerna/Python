cadena = "Hola, me llamo Lucia"
cadenaNueva = ""
vocales = "aeiouAEIOU"

for letra in cadena:
    if letra in vocales:
        cadenaNueva += "*"
    else:
        cadenaNueva += letra
print(cadenaNueva)
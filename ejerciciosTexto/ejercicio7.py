cadena = "hola mi nombre es lucia"
caracter = "u"
caracterNuevo = "i"
cadena2 = ""

for letra in cadena:
    if letra == caracter:
        cadena2 += caracterNuevo
    else:
        cadena2 += letra
print(cadena2)
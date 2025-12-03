texto = "Hola Mundo"
resultado = ""

for letra in texto:
    if "a" <= letra <= "z":              
        may = chr(ord(letra) - 32)       
        resultado += may
    else:
        resultado += letra               

print(resultado)

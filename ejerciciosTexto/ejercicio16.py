cadena1 = str(input("Escribe la primera cadena: "))
cadena2 = str(input("Escribe la segunda cadena: "))
cadenaCompleta = ""

for letra in cadena1:
    cadenaCompleta += letra
    
for letra in cadena2:
    cadenaCompleta += letra
    
print("La cadena completa es:", cadenaCompleta)
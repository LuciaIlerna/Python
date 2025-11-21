cadena = "Hola mi nombre es Juanita Juana"
contador = 0

for i in range(len(cadena)):
    if cadena[i] == "a":
        contador += 1
        
print("El número de veces que aparece la letra 'a' en la cadena es:", contador)
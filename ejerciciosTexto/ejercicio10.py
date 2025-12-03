cadena = "Hola me llamo Lucia"
mayus = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
contador = 0

for letra in cadena:
    if letra in mayus:
        contador+=1
print("Hay", contador, "mayúsculas")
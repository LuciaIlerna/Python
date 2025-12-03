cadena = "Hola buenas tardes, como estamos"
buscada = "i"
encontrada = False

for letra in cadena:
    if letra == buscada:
        encontrada = True
        break
if encontrada:
    print("La letra sí está en la cadena")
else:
    print("La letra no está en la cadena")
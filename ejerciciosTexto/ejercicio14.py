cadena = str(input("Escribe una cadena de texto: "))
numeros = "0123456789"
contador = 0

for letra in cadena:
    if letra in numeros:
        contador += 1
print("Hay", contador, "números")
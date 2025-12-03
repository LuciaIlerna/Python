cadena = input("Escribe una cadena: ")

resultado = ""

for letra in cadena:
    contador = 0
    for otra in cadena:
        if letra == otra:
            contador += 1
    
    if contador > 1 and letra not in resultado:
        resultado += letra

print("Caracteres repetidos:", resultado)

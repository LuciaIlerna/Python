cadena = input("Escribe una cadena: ")

resultado = ""

for letra in cadena:
    l = letra.lower()

    if not (l == "a" or l == "e" or l == "i" or l == "o" or l == "u"):
        resultado += letra

print("Consonantes solamente:", resultado)
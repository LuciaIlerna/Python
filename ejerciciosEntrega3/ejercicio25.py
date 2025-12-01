# 25. Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

cadena = input("Introduce un carácter: ")

if len(cadena) == 1 and cadena >= 'A' and cadena <= 'Z':
    print("Es una letra mayúscula.")
else:
    print("No es una letra mayúscula.")


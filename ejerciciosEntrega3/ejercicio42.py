# 42. Algoritmo que pida caracteres e imprima 'VOCAL' si son vocales y 'NO VOCAL' en caso
# contrario, el programa termina cuando se introduce un espacio.

while True:
    letra = input("Letra: ")
    
    if letra == " ":
        break
    
    letra = letra.lower()
    
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print("VOCAL")
    else:
        print("NO VOCAL")
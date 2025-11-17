# 5. Programa que muestre en líneas separadas lo siguiente:
#ZYWXVUTSRQPONMLKJIHGFEDCBA, YWXVUTSRQPONMLKJIHGFEDCBA,
#WXVUTSRQPONMLKJIHGFEDCBA, ...., DCBA, CBA, BA, A.

letras = "ZYXWVUTSRQPONMLKJIHGFEDCBA"

i = 0
while i < 26:
    print(letras[i:])
    i += 1

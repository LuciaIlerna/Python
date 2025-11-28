# 14. Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido.

n = int(input("Número de dos cifras: "))

decena = n // 10
unidad = n % 10

invertido = unidad * 10 + decena

print(invertido)

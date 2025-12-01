# 47. Escribe un programa que diga si un número introducido por teclado es o no primo. Un
# número primo es aquel que sólo es divisible entre él mismo y la unidad. Nota: Es suficiente
# probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número.

num = int(input("Introduce un número: "))
es_primo = True
if num <= 1:
    es_primo = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
if es_primo:
    print("El número es primo.")
else:
    print("El número no es primo.")
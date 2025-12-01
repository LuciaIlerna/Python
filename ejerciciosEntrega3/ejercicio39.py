# 39. Crea una aplicación que permita adivinar un número. La aplicación genera un número
# aleatorio del 1 al 100. A continuación, va pidiendo números y va respondiendo si el número a
# adivinar es mayor o menor que el introducido, además de los intentos que te quedan (tienes 10
# intentos para acertarlo). El programa termina cuando se acierta el número (además te dice en
# cuantos intentos lo has acertado), si se llega al límite de intentos te muestra el número que
# había generado.

import random

numero_secreto = random.randint(1, 100)
intentos = 10

print("Adivina el numero entre 1 y 100")
print("Tienes 10 intentos")

for i in range(intentos):
    print("Intento", i + 1, "de", intentos)
    numero = int(input("Introduce un numero: "))
    
    if numero == numero_secreto:
        print("Correcto! Has acertado en", i + 1, "intentos")
        break
    elif numero < numero_secreto:
        print("El numero secreto es MAYOR")
    else:
        print("El numero secreto es MENOR")
    
    print("Te quedan", intentos - (i + 1), "intentos")
else:
    print("Perdiste. El numero era:", numero_secreto)
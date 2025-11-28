# 13. Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
#Python3 no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿Cómo se
#puede calcular?

num = int(input("Introduce un número"))

raizCuadrada = num ** 0.5
raizCubica = num ** (1/3)

print ("La raiz cuadrada de ", num, "es: ", raizCuadrada, "y la raiz cúbica  de ", num, "es :", raizCubica)
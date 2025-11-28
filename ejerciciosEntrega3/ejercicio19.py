# 19. Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: por
#cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime
#el resultado obtenido por el estudiante.

correctas = int(input("Cantidad de respuestas correctas: "))
incorrectas = int(input("Cantidad de respuestas incorrectas: "))
blanco = int(input("Cantidad de respuestas en blanco: "))

nota_final = correctas * 5 + incorrectas * -1 + blanco * 0

print("La nota final del estudiante es:", nota_final)

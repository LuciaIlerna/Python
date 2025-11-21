# Ejercicio 1: Diamante hueco
#Enunciado:
#Imprime un diamante hueco de altura total 2n - 1, centrado con asteriscos, donde solo se imprimen los bordes y el centro.
#Figura para n=5:

#Parte izquierda
n = 5
altura = (2 + 5) - 1
#Superior
for i in range(1, altura + 1):
    if i == 1:  
        print(" " * (altura - i) + "*")
    else:  
        print(" " * (altura - i) + "*" + " " * (i - 2) + "*")

#Inferior
for i in range(altura -1, 0, - 1):
    if i == 1:  
        print(" " * (altura - i) + "*")
    else:  
        print(" " * (altura - i) + "*" + " " * (i - 2) + "*")
        
#Parte derecha
#Superior
#Superior (girado a la derecha)
for i in range(1, altura + 1):
    if i == 1:
        print("*" + " " * (altura - 1) + "*")
    else:
        print("*" + " " * (i - 2) + "*" + " " * (altura - i) + "*")

#Inferior
for i in range(altura -1, 0, 1):
    if i == 1:
        print(" " * (altura - i) + "*" + " " * (altura - 1) + "*")
        



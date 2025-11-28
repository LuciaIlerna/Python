# 12. Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano.
#Calcula y muestra la distancia entre ellos.

print ("Introduce dos pares de números que representen dos puntos en el plano")

x1 = float(input("Ingresa x1: "))
y1 = float(input("Ingresa y1: "))
x2 = float(input("Ingresa x2: "))
y2 = float(input("Ingresa y2: "))

distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print("La distancia entre los puntos es: ", distancia)
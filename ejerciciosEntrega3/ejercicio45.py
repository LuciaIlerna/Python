# 45. Escribe un programa que pida el límite inferior y superior de un intervalo. Si el límite inferior
# es mayor que el superior lo tiene que volver a pedir. A continuación, se van introduciendo
# números hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes
# informaciones:
# • La suma de los números que están dentro del intervalo (intervalo abierto).
# • Cuantos números están fuera del intervalo.
# • He informa si hemos introducido algún número igual a los límites del intervalo.

print("Introduce los limites del intervalo")

while True:
    inferior = int(input("Limite inferior: "))
    superior = int(input("Limite superior: "))
    
    if inferior < superior:
        break
    else:
        print("Error: El limite inferior debe ser menor que el superior")

print("Introduce numeros (0 para terminar):")

suma_dentro = 0
fuera = 0
igual_limite = False

while True:
    num = int(input("Numero: "))
    
    if num == 0:
        break
    
    if num == inferior or num == superior:
        igual_limite = True
    
    if inferior < num < superior:
        suma_dentro = suma_dentro + num
    else:
        fuera = fuera + 1

print("Resultados:")
print("Suma de numeros dentro del intervalo:", suma_dentro)
print("Numeros fuera del intervalo:", fuera)

if igual_limite:
    print("Se introdujo algun numero igual a los limites")
else:
    print("No se introdujo ningun numero igual a los limites")
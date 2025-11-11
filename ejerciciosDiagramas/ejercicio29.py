opcion = 50
limitSup = 100
limitInf = 0
print("Piensa un número del 1 al 100 y lo intentaré adivinar. Introduce 0 si he acertado, 1 si tu número es menor, o 2 si es mayor")

def adivinar (limitSup, limitInf, opcion):
    intentos = 0
    while True:
        print("[0] Acierto : [1] Menor : [2] Mayor")
        num = int(input(f"¿Tu número es {opcion}?"))
        intentos += 1
        if num == 0:
            break
        elif num == 1:
            limitSup = opcion
            opcion -= (limitSup - limitInf) 
            
        elif num == 2:
            limitSup = opcion
            opcion += (limitSup - limitInf)
            
    return intentos

intentos = adivinar (limitSup, limitInf, opcion)
print("He adivinado el número en", intentos, "intentos.")
            
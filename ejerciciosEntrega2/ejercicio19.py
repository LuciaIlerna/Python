# 19. Programa donde el usuario "piensa" un número del 1 al 100 y el ordenador intenta
#adivinarlo. Es decir, el ordenador irá proponiendo números una y otra vez hasta adivinarlo (el
#usuario deberá indicarle al ordenador si es mayor, menor o igual al número que ha pensado).

limiteInf = 1
limiteSup = 100
intentos = 0

print(f"\nPiensa un número entre {limiteInf} y {limiteSup}.")
print("Introduce '0' si acierto, '1' si tu número es menor o '2' si es mayor.")


while True:
    guess = (limiteInf + limiteSup) // 2
    
    print ("\n[0] Acierto : [1] Menor : [2] Mayor")
    opc = int(input(f"¿Tu número es {guess}? "))
    intentos += 1


    if opc == 0: 
        break
    
    elif opc == 1: 
        limiteSup = guess - 1
        
    elif opc == 2: 
        limiteInf = guess + 1
        
    else: 
        print("Error.")


print(f"He usado {intentos} intentos.")
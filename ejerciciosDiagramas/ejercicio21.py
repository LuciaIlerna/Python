cont = 0
while cont < 100:
    num = int(input("Introduce un número: "))
    
    if num != 0:
        cont += 1

    if num == 0:
        print("Error. No se puede introducir el número cero.")   
        
    if num < 0:
        print("Se ha introducido un número negativo.")
     
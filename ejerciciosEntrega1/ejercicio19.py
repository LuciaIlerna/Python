# 19. Escriba un programa que simule un cajero automático con un saldo inicial de 1000 dólares, con el siguiente menú de opciones:
#Bienvenido a su Cajero Virtual
#1. Ingresar dinero en cuenta
#2. Retirar dinero de la cuenta
#3. Salir

saldo_inicial = 1000
ingresar = 1
retirar = 2
salir = 3

while True:
    print("Bienvenido a su Cajero Virtual")
    print("Tu saldo inicial es de:", saldo_inicial, "euros.")

    print ("1. Ingresar dinero en cuenta: ")
    print ("2. Retirar dinero de la cuenta: ")
    print ("3. Salir")
    opcion = int(input("Elige una opción (1-3): "))

    if opcion == 1:
        cantidad = float(input("Introduce la cantidad a ingresar: "))
        saldo_inicial += cantidad
        print("Has ingresado", cantidad, "euros. Tu saldo actual es de:", saldo_inicial, "euros.")
    elif opcion == 2:
        cantidad = float(input("Introduce la cantidad a retirar: "))
        if cantidad > saldo_inicial:
            print("No tienes suficiente saldo para retirar esa cantidad.")
        else:
            saldo_inicial -= cantidad
            print("Has retirado", cantidad, "euros. Tu saldo actual es de:", saldo_inicial, "euros.")
    elif opcion == 3:
        print("Gracias por usar el Cajero Virtual. Tu saldo final es de:", saldo_inicial, "euros.")
        break



num = int(input("Introduce un número: "))
while num < 0 or num > 10:
    print("Error. El número introducido no puede ser negativo ni superior a diez.")
    num = int(input("Introduce un número: "))

if num < 3:
    print("Muy deficiente")
elif num < 5:
    print("Insuficiente")
elif num < 6:
    print("Suficiente")
elif num < 7:
    print("Bien")
elif num < 9:
    print("Notable")
elif num <= 10:
    print("Sobresaliente")    
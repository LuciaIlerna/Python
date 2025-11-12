# 16. Escriba un programa que pida un número entre 0 y 99999, y que diga cuantas cifras tiene.

num = int(input("Introduce un número entre 0 y 99999: "))
if num <0 or num >99999:
    print("El número no está en el rango solicitado.")
else:
    print("El número tiene", len(str(num)), "cifras.")
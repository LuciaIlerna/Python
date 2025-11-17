# 24. Tiendas Don Pepe desea un programa para ingresar por teclado el monto de compra y el día
#de la semana; si el día es martes o jueves, se realizará un descuento del 15% por la compra.
#Visualizar el descuento y el total a pagar por la compra.

monto_de_compra = int(input("Introduce el monto de compra: "))
dia = str(input("Introduce el día de la semana: ")).lower()

if dia == "martes" or dia == "jueves":
    descuento = monto_de_compra * 0.15
    total = monto_de_compra - descuento
    print("Descuento aplicado: ", descuento)
    print("Total a pagar: ", total)
else:
    print("No es martes ni jueves, por lo que no habrán descuentos")
    print("Total a pagar: ", monto_de_compra)
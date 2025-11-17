# 23. Una farmacia desea un programa para ingresar el valor de compra y calcular lo siguiente: si
#el pago se efectúa al “contado”, calcular un descuento del 5%; pero si el pago es con “tarjeta”
#se incrementa un recargo del 3% al valor de compra. Calcular y visualizar el descuento o recargo
#según sea el caso y el total a pagar de la compra.

compra = float(input("Ingrese el valor de la compra: "))

pago = str(input('Forma de pago ("contado" o "tarjeta"): ')).lower()

if pago == "contado":
    descuento = compra * 0.05
    total = compra - descuento
    print("Descuento aplicado: ", descuento)
    print("Total a pagar: ", total)

elif pago == "tarjeta":
    recargo = compra * 0.03
    total = compra + recargo
    print("Recargo aplicado: ", recargo)
    print("Total a pagar: ", total)

else:
    print("Forma de pago no válida. Debe ser 'contado' o 'tarjeta'.")


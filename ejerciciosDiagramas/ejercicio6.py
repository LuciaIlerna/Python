precioA = int(input("Introduce el precio del artículo real: "))
precioV = int(input("Introduce el precio de venta: "))
desc = 100 - ((precioV * 100) / precioA)
print("El descuento aplicado es de:", desc, "%")
# 6. Escriba un programa que dado el precio de un artículo y el precio de venta real nos muestre el porcentaje de descuento realizado.

precioA = int(print("Introduce el precio del artículo real: "))
precioV = int(print("Introduce el precio de venta: "))
desc = 100 - ((precioV * 100) / precioA)
print("El descuento aplicado es de:", desc, "%")
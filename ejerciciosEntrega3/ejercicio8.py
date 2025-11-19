# 8. Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el
#vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas
#que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y
#comisiones.

sueldo_base = 1200
venta1 = 150
venta2 = 200
venta3 = 300

comisiones = (venta1 + venta2 + venta3) * 0.10

total = sueldo_base + comisiones  

print("El total de comisiones es: ", comisiones)
print("El total a recibir en el mes es: ", total) 


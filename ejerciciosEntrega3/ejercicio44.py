# 44. Realizar un algoritmo que muestre la tabla de multiplicar de un número introducido por
# teclado.

num = int(input("Que tabla de multiplicar quieres ver? "))

print("Tabla del", num)

for i in range(1, 11):
    resultado = num * i
    print(num, "x", i, "=", resultado)
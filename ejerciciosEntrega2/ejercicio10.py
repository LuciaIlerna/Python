# 10. Programa que calcula y escribe la suma y el producto de los 10 primeros números naturales.

sum = 0
multi = 1
for i in range(1, 11):
    sum = sum + i
    multi = multi * i
print("La suma de los números de la secuencia es:", sum)
print("El producto de los números de la secuencia es:", multi)
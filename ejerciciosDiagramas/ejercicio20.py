factorial = 1
n = int(input("Introduce un número positivo que no sea cero: "))
for i in range (1, n + 1):
    factorial = factorial * n
    n = n - 1
print("El factorial es: ", factorial)
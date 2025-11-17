# 6. Programa que lea un número positivo N y calcule y visualice su factorial N! Siendo el
#factorial:
#0! = 1
#1! = 1
#2! = 2 * 1
#3! = 3 * 2* 1
#N! = N * (N-1) * (N-2) * … * .

factorial = 1
n = int(print("Introduce un número positivo que no sea cero: "))
for i in range (1, n + 1):
    factorial = factorial * n
    n = n - 1
print("El factorial es: ", factorial)
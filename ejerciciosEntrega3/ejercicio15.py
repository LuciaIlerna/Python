# 15. Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un
#algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.

A = float(input("Ingrese A: "))
B = float(input("Ingrese B: "))

Aux = A
A = B
B = Aux

print("A ahora vale:", A)
print("B ahora vale:", B)

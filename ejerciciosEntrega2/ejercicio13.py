# 13. Crea una aplicación que dibuje una escalera de números, siendo cada línea números
#empezando en uno y acabando en el numero de la línea. Este es un ejemplo, si introducimos un
#5 como altura:

altura = int(input("Introduce la altura: "))

for i in range(1, altura + 1):
    linea = ""
    for n in range(1, i + 1):
        linea += str(n)
    print(linea)

# 48. Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si al final de
# cada mes deposita cantidades variables de dinero; además, se quiere saber cuánto lleva
# ahorrado cada mes.

total = 0

for mes in range(1, 13):
    print("Mes", mes)
    ahorro = float(input("Dinero ahorrado este mes: "))
    
    total = total + ahorro
    
    print("Total acumulado:", total)
    print()

print("Ahorro total en el año:", total)
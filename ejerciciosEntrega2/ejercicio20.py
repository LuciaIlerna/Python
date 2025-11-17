# 20. Programa que dada una cantidad de euros que el usuario introduce por teclado (múltiplo de
#5 €) mostrará los billetes de cada tipo que serán necesarios para alcanzar dicha cantidad
#(utilizando billetes de 500, 200, 100, 50, 20, 10 y 5). Hay que indicar el mínimo de billetes posible.
#Por ejemplo, si el usuario introduce 145 el programa indicará que será necesario 1 billete de 100
#€, 2 billetes de 20 € y 1 billete de 5 € (no será válido por ejemplo 29 billetes de 5, que aunque
#sume 145 € no es el mínimo número de billetes posible)

b500 = 0
b200 = 0
b100 = 0
b50 = 0
b20 = 0
b10 = 0
b5 = 0
n = int(input("Introduce una cantidad de dinero múltiplo de 5: "))

while True:
    
    if n % 5 != 0:
        n = int(input("El número no es múltiplo de 5. Inténtalo otra vez: "))
    
    elif n >= 500:
        b500 += 1
        n -= 500
        
    elif n >= 200:
        b200 += 1
        n -= 200
        
    elif n >= 100:
        b100 += 1
        n -= 100
        
    elif n >= 50:
        b50 += 1
        n -= 50
        
    elif n >= 20:
        b20 += 1
        n -= 20
        
    elif n >= 10:
        b10 += 1
        n -= 10
        
    elif n >= 5:
        b5 += 1
        n -= 5
        
    elif n == 0:
        break
    
print("Cantidad de billetes : ")
print("Billetes de 500: ", b500)
print("Billetes de 200: ", b200)
print("Billetes de 100: ", b100)
print("Billetes de 50:  ", b50)
print("Billetes de 20:  ", b20)
print("Billetes de 10:  ", b10)
print("Billetes de 5:   ", b5)
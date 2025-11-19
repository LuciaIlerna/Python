#Normal
#altura = int(input("Introduce la altura teniendo en cuenta que el número que introduzcas será la de cada mitad: "))

#for i in range(1, altura + 1):
#    print("*" * i)
    
#Invertida

#for i in range(altura, 0, -1):
#    print("*" * i)
    
#altura = int(input("Introduce la altura teniendo en cuenta que el número que introduzcas será la de cada mitad: "))
altura = 5

#Superior
for i in range(1, altura + 1):
    if i == 1:  
        print(" " * (altura - i) + "*")
    else:  
        print(" " * (altura - i) + "*", ((2*(i-2))+1) * " ", "*", sep ="")

#Inferior
for i in range(altura - 1, 0, -1):  
    if i == 1:  
        print(" " * (altura - i) + "*")
    else:  
        print(" " * (altura - i) + "*", ((2*(i-2))+1) * " ", "*", sep ="")
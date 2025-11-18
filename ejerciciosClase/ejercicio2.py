#altura = int(input("Introduce la altura teniendo en cuenta que el número que introduzcas será la de cada mitad: "))

#for i in range(1, altura + 1):
#    print(str(i) * i)

altura = int(input("Introduce la altura teniendo en cuenta que el número que introduzcas será la de cada mitad:  "))

for i in range(1, altura + 1):
    if i == 1: 
        print("4")
    elif i == altura:  
        print("4" * i)
    else: 
        print("4" + " " * (i - 2) + "4")
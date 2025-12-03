altura = 4

#Superior
for i in range (1, altura + 1):
    print((altura - i) * " ", (i * 2 - 1)* "*")
    
#Inferior
for i in range(altura - 1, 0, -1):
    print((altura - i) * " ", (i * 2 - 1) * "*")
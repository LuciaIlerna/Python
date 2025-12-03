texto = "Hola a todos"
nuevo = ""

for i in texto:
    if i not in "aeiouAEIOU":
        nuevo += i
print(nuevo)
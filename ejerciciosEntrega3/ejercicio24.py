# 24. Escribe un programa que pida un nombre de usuario y una contraseña y si se ha
#introducido "pepe" y "asdasd" se indica "Has entrado al sistema", sino se da un error.

nombre = str(input("Introduce tu nombre de usuario: "))
contraseña = str(input("Introduce la contraseña: "))

if nombre == "pepe" and contraseña == "asdasd":
    print("Has entrado al sistema.")
else:
    print("Error: Usuario o contraseña equivocadas.")
# 17. Escriba un programa que simule un inicio de sesión solicitando el nombre de usuario y
#contraseña, y mostrar un mensaje en pantalla, inicio de sesión correcto/ nombre de usuario
#incorrecto

nombreCorrecto = "Lucia"
contraseñaCorrecta = "12345"

nombre = input("Introduce el nombre de usuario: ")
contraseña = input("Introduce la contraseña: ")

if nombre == nombreCorrecto:
    print("Nombre de usuario correcto.")
else:
    print("Nombre de usuario incorrecto.")
if contraseña == contraseñaCorrecta:
    print("Contraseña correcta.")
else:
    print("Contraseña incorrecta.")
    
if nombre == nombreCorrecto and contraseña == contraseñaCorrecta:
    print("Inicio de sesión correcto.")
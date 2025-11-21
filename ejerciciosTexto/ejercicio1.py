# Leer una cadena desde teclado y mostrarla carácter por carácter usando un ciclo for y el índice.

cadena = str(input("Introduce una cadena de texto: "))
for i in range(len(cadena)):
    print(cadena[i])
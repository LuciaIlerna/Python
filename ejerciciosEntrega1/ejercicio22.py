# 22. Escriba un programa que recibe como datos de entrada una hora expresada en horas,
#minutos y segundos que nos calcula y escribe la hora, minutos y segundos que serán,
#transcurrido un segundo

horas = int(input("Horas:"))
minutos = int(input("Minutos:"))
segundos = int(input("Segundos:"))

segundos += 1

if segundos == 60:
    segundos = 0
    minutos += 1
    
if minutos == 60:
    minutos = 0
    horas += 1
    
if horas == 24:
    horas = 0
    
print ("La hora dentro de un segundo será: " , horas , ":",  minutos ,":", segundos )
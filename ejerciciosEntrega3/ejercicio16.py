# 16. Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una
#distancia d. El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para
#ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto
#determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro.

d = float(input("Distancia entre los vehículos (km): "))
v1 = float(input("Velocidad del vehículo más rápido (km/h): "))
v2 = float(input("Velocidad del vehículo más lento (km/h): "))

velocidad_relativa = v1 - v2

if velocidad_relativa <= 0:
    print("El vehículo rápido no alcanzará al otro.")
else:
    tiempo_horas = d / velocidad_relativa
    tiempo_minutos = tiempo_horas * 60
    print("Lo alcanzará en: ", tiempo_minutos, "minutos.")

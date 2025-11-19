# 10. Un alumno desea saber cuál será su calificación final en la materia de Algoritmos Dicha
#calificación se compone de los siguientes porcentajes:
#• 55% del promedio de sus tres calificaciones parciales.
#• 30% de la calificación del examen final.
#• 15% de la calificación de un trabajo final.

parcial1 = 8
parcial2 = 7
parcial3 = 9
examen = 8
trabajo = 10

promedio_parciales = (parcial1 + parcial2 + parcial3) / 3
calificacion_final = (promedio_parciales * 0.55) + (examen * 0.30) + (trabajo * 0.15)

print(calificacion_final)
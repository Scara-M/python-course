"""
Definir una lista por asignación que almacene en la primer componente el nombre de un alumno y en las dos siguientes sus notas. Imprimir luego el nombre y el promedio de las dos notas.
"""
alumno = ['Mariano', 7, 8]

# calcular promedio
promedio = (alumno[1] + alumno[2]) // 2

print('El alumno es ', alumno[0], '- El promedio es ', promedio)
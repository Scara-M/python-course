"""
Almacenar en una lista los sueldos (valores float) de 5 operarios. 
Imprimir la lista y el promedio de sueldos.
"""
# Lista vacia
sueldos = []
acum = 0

for x in range(5):
    sueldo = float(input('Ingresar el sueldo del operario: '))
    sueldos.append(sueldo)
    acum += sueldo

# Calcular promedio
prom = acum / 5

# Salida
print('La lista es ', sueldos)
print('El promedio de los sueldos es ', prom)

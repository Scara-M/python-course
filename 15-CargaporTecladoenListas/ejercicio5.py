"""
Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados (4 por la mañana y 4 por la tarde) 
Confeccionar un programa que permita almacenar los sueldos de los empleados agrupados en dos listas.
Imprimir las dos listas de sueldos.
"""

sueldos_manana = []
sueldos_tarde = []

# Turno mañana
print('-'*7)
print('TURNO MAÑANA')
for x in range(4):
    sueldo = float(input('Ingresar sueldo del operario: '))
    sueldos_manana.append(sueldo)

# Turno tarde
print('-'*7)
print('TURNO TARDE')
for x in range(4):
    sueldo = float(input('Ingresar sueldo del operario: '))
    sueldos_tarde.append(sueldo)

# Salida
print('-'*7)
print('Sueldos turno mañana: ', sueldos_manana)
print('Sueldos turno tarde: ', sueldos_tarde)
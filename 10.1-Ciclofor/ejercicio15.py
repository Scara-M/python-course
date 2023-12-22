"""
Se cuenta con la siguiente información:
Las edades de 5 estudiantes del turno mañana.
Las edades de 6 estudiantes del turno tarde.
Las edades de 11 estudiantes del turno noche.
Las edades de cada estudiante deben ingresarse por teclado.
a) Obtener el promedio de las edades de cada turno (tres promedios)
b) Imprimir dichos promedios (promedio de cada turno)
c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor.
"""


print('TURNO MAÑANA')
acum_man = 0
for x in range(5):
    edad = int(input('Ingresar la edad del estudiante: '))
    acum_man += edad


print('TURNO TARDE')
acum_tar = 0
for x in range(6):
    edad = int(input('Ingresar la edad del estudiante: '))
    acum_tar += edad


print('TURNO NOCHE')
acum_noche = 0
for x in range(11):
    edad = int(input('Ingresar la edad del estudiante: '))
    acum_noche += edad


# Promedio de cada turno
prom_man = acum_man / 5
prom_tar = acum_tar / 6
prom_noche = acum_noche / 11

# Determinar el promedio mayor
if prom_man > prom_tar and prom_man > prom_noche:
    mayor = 'mañana'
elif prom_tar > prom_noche:
    mayor = 'tarde'
else:
    mayor = 'noche'

# Salida
print('El promedio del turno mañana es ', prom_man)
print('El promedio del turno tarde es ', prom_tar)
print('El promedio del turno noche es ', prom_noche)
print('El promedio mayor es el del turno ', mayor)
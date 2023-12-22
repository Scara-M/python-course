"""
Escribir un programa que solicite por teclado 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.
"""
aprobados = 0
desaprobados = 0

# Proceso
for x in range(10):
    nota = int(input('Ingresar nota del alumno: '))
    if nota >= 7:
        aprobados += 1
    else:
        desaprobados += 1

# Salida por pantalla
print('La cantidad de alumnos aprobados es ', aprobados)
print('La cantidad de alumnos desaprobados son ', desaprobados)
"""
Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.
"""
x = 1
aprobados = 0
desaprobados = 0

# Procesar nota
while x <= 10:
    nota = int(input('Ingresar nota: '))
    if nota >= 7:
        aprobados += 1
    else:
        desaprobados += 1
    x = x + 1

# Salida por pantalla
print('La cantidad de aprobados es ', aprobados)
print('La cantidad de desaprobados son: ', desaprobados)        
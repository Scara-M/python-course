"""
Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre posteriormente la suma de los valores ingresados y su promedio.
"""
x = 1
suma = 0
while x <= 10:
    num = int(input('Ingresar número: '))
    suma = suma + num
    x = x + 1

# calculo promedio
promedio = suma / 10

# Salida
print('La suma de los valores ingresados es ', suma)
print('El promedio de los valores ingresados es ', promedio)
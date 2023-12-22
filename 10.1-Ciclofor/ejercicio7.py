"""
Codificar un programa que lea n números enteros y calcule la cantidad de valores mayores o iguales a 1000 (n se carga por teclado). 
"""
may_igual1000 = 0
n = int(input('Ingresar la cantidad de enteros a procesar: '))

for x in range(n):
    num = int(input('Ingresar número: '))
    if num >= 1000:
        may_igual1000 += 1

# Salida
print('La cantidad de valores mayores o iguales a 1000 ', may_igual1000)
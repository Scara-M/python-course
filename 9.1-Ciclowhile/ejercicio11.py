"""
Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores fueron pares y cuántos impares.
"""

n = int(input('Ingresar la cantidad de enteros a procesar: '))
x = 1
pares = impares = 0

# Proceso
while x <= n:
    num = int(input('Ingresar un número entero: '))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    x += 1
    
# Salida 
print('La cantidad de pares es ', pares)
print('La cantidad de impares es ', impares)
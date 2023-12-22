"""
Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los últimos 5 valores ingresados
"""
suma = 0

for x in range(10):
    num = int(input('Ingresar número: '))
    if x > 4:
        suma += num

# Salida por pantalla
print('La suma de los últimos cinco valores es ', suma)
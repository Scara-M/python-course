"""
Escribir un programa que lea 10 números enteros y luego muestre cuántos valores ingresados fueron múltiplos de 3 y cuántos de 5. Debemos tener en cuenta que hay números que son múltiplos de 3 y de 5 a la vez.
"""
multiplos3 = 0
multiplos5 = 0

for x in range(10):
    num = int(input('Ingresar un número: '))
    if num % 3 == 0:
        multiplos3 += 1
    if num % 5 == 0:
        multiplos5 += 1

# Salida
print('La cantidad de valores múltiplos de 3 son ', multiplos3)
print('La cantidad de valores múltiplos de 5 son ', multiplos3)
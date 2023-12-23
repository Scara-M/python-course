"""
Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar dicha suma.
"""
# Creamos la lista por asignación
lista = [7, 8, 9, 5, 3]
x = 0
suma = 0

# Recorremos la lista
while x < len(lista):
    suma += lista[x]
    x += 1

# Salida
print('La suma de los elementos de la lista es ', suma)
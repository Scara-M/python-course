"""
Definir una lista por asignación con 5 enteros. Mostrar por pantalla solo los elementos con valor iguales o superiores a 7.
"""
lista = [10, 2, 7, 1, 8]

for x in range(len(lista)):
    if lista[x] >= 7:
        print(lista[x])
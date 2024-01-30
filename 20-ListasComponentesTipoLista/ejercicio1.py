"""
Crear una lista por asignación. La lista tiene que tener cuatro elementos. Cada elemento debe ser una lista de 3 enteros.
Imprimir sus elementos accediendo de diferentes modos.
"""
lista = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

# Lista completa
print('Lista completa')
print(lista)
print(" ")

# primer componente
print('Primer componente')
print(lista[0])
print(" ")

# primer componente de la lista contenida en la primer componente de la #lista principal
print('Primer componente de la primera componente de la lista principal')
print(lista[0][0])
print(" ")

# lista contenida en la primer componente de la lista principal
for x in range(len(lista[0])):
    print(lista[0][x])
print(" ")

# Imprimir cada elemento de cada lista 
for k in range(len(lista)):
    for x in range(len(lista[k])):
        print(lista[k][x])
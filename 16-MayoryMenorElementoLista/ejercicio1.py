"""
Crear y cargar una lista con 5 enteros. Implementar un algoritmo que identifique el mayor valor de la lista.
"""
lista = []

# Carga de enteros
for x in range(5):
    num = int(input('Ingrese valor: '))
    lista.append(num)


# Buscar  el mayor de la lista
mayor = lista[0]
for x in range(1, 5):
    if lista[x] > mayor:
        mayor = lista[x]


print('La lista completa: ', lista)
print('El mayor de la lista es ', mayor)
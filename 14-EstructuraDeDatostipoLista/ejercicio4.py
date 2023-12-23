"""
Definir por asignación una lista con 8 elementos enteros. Contar cuantos de dichos valores almacenan un valor superior a 100.
"""
lista = [5, 101, 8, 9, 500, 600, 5000, 800000,]
cant100 = 0

for x in range(len(lista)):
    if lista[x] > 100:
        cant100 += 1

print('La cantidad de elementos mayores 100 son ', cant100)
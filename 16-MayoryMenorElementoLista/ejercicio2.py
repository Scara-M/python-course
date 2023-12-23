"""
Crear y cargar una lista con 5 enteros por teclado. Implementar un algoritmo que identifique el menor valor de la lista y la posición donde se encuentra.
"""
lista = []

# cargar valores
for x in range(5):
    num = int(input('Ingresar número: '))
    lista.append(num)

# Bucar menor y posicion
menor = lista[0]
posicion = 0
for x in range(1,5):
    if lista[x] < menor:
        menor = lista[x]
        posicion = [x]

# Salida 
print('La lista completa es ', lista)
print('El menor de la lista es ', menor, ' y su posicion es ', posicion)
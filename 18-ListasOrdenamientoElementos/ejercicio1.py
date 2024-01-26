"""
Se debe crear y cargar una lista donde almacenar 5 sueldos. Desplazar el valor mayor de la lista a la última posición.
"""
# Lista vacia
lista = []

# cargar lista
for x in range(5):
    sueldo = int(input('Ingresar sueldo: '))
    lista.append(sueldo)

print('Los elementos de la lista son: ')
print(lista)

# Ordenar la lista
for x in range(4):
    if lista[x] > lista[x + 1]:
        aux = lista[x]
        lista[x] = lista[x + 1]
        lista[x + 1] = aux

# Lista ordenada
print('Lista con el mayor a la última posicion')
print(lista)
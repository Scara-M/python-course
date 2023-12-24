"""
Realizar un programa que pida la carga de dos listas numéricas enteras de 4 elementos cada una. Generar una tercer lista que surja de la suma de los elementos de la misma posición de cada lista. Mostrar esta tercer lista.
"""
lista1 = []
lista2 = []
lista3 = []

# carga de lista
for x in range(4):
    num1 = int(input('Ingresar número de la primer lista: '))
    lista1.append(num1)
    num2 = int(input('Ingresar número de la segunda lista: '))
    lista2.append(num2)

for x in range(4):
    suma = lista1[x] + lista2[x]
    lista3.append(suma)

# Salida por pantalla
print('Lista 1', lista1)
print('Lista 2', lista2)
print('Lista de la suma de las dos listas', lista3)
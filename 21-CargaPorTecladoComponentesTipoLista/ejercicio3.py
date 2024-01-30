"""
Solicitar por teclado dos enteros. El primer valor indica la cantidad de elementos que crearemos en la lista. El segundo valor indica la cantidad de elementos que tendrá cada una de las listas internas a la lista principal.
Mostrar la lista y la suma de todos sus elementos.
"""
lista = []

# carga de datos
elementos = int(input('Ingresar la cantidad de elementos de la lista: '))

sub = int(input('Ingresar la cantidad de elementos de las listas internas: '))

for k in range(elementos):
    lista.append([])
    for x in range(sub):
        valor = int(input('Ingrese valor: '))
        lista[k].append(valor)
print(lista)


suma = 0
for k in range(len(lista)):
    for k in range(len(lista[k])):
        suma = suma + lista[k][x]


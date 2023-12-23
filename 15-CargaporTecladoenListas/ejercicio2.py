"""
Realizar la carga de valores enteros por teclado, almacenarlos en una lista. Finalizar la carga de enteros al ingresar el cero. Mostrar finalmente el tamaño de la lista.
"""
lista = []
num = int(input('Ingresar valor (0 para finalizar): '))

while num != 0:
    lista.append(num)
    num = int(input('Ingresar valor (0 para finalizar): '))

print('Tamaño de la lista')
print(len(lista))
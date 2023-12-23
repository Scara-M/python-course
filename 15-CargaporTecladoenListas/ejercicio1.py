"""
Definir una lista vacía y luego solicitar la carga de 5 enteros por teclado y añadirlos a la lista. Imprimir la lista generada.
"""
# Definir lista vacia
lista = []

for x in range(5):
    num = int(input('Agregar elemento de la lista: '))
    lista.append(num)

print(lista)
"""
Definir una lista de enteros por asignación en el bloque principal. 
Llamar a una función que reciba la lista y nos retorne el producto de todos sus elementos. 
Mostrar dicho producto en el bloque principal de nuestro programa.
"""
def calcular_producto(lista):
    producto = 1
    for x in range(len(lista)):
        producto = producto * lista[x]
    return producto

# bloque principal
lista = [1, 2, 3, 4, 5]
print('El producto de los elementos de la lista es ', calcular_producto(lista))
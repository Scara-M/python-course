"""
Desarrollar una funcion que reciba un string como parametro y nos muestre la cantidad de vocales. 
Llamarla desde el bloque principal del programa 3 veces con string distintos.
"""
def contar_vocales(cadena):
    cant = 0
    vocales = ['a', 'A', 'e', 'E', 'i' , 'I', 'o', 'O', 'u', 'U']
    for x in range(len(cadena)):
        if cadena[x] in vocales:
            cant += 1
    print('La cantidad de vocales son ', cant)

palabra = input('Ingrese una palabra: ')
contar_vocales(palabra)
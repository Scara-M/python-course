"""
Elaborar una función que nos retorne el perímetro de un cuadrado pasando como parámetros el valor de un lado.
"""
def calcular_perimetro(lado):
    perimetro = lado * 4
    return perimetro

# bloque principal
lado = int(input('Ingresar un lado del cuadrado: '))
print('El perímetro es ', calcular_perimetro(lado))
"""
Confeccionar una función que calcule la superficie de un rectángulo y la retorne, la función recibe como parámetros los valores de dos de sus lados:
def retornar_superficie(lado1,lado2):
En el bloque principal del programa cargar los lados de dos rectángulos y luego mostrar cual de los dos tiene una superficie mayor.
"""
def retornar_superficie(lado1, lado2):
    superficie = lado1 * lado2
    return superficie


# bloque principal
print('Rectángulo 1')
lado1 = int(input('Ingresar un lado: '))
lado2 = int(input('Ingresar otro lado: '))
superficie1 = retornar_superficie(lado1, lado2)
print('Rectángulo 2')
lado1 = int(input('Ingresar un lado: '))
lado2 = int(input('Ingresar otro lado: '))
superficie2 = retornar_superficie(lado1, lado2)

if superficie1 > superficie2:
    print('El de mayor superficie es del primer rectángulo')
else:
    print('El de mayor superficie es del segundo rectángulo')
"""
Confeccionar una función que le enviemos como parámetros dos enteros y nos retorne el mayor.
"""
def retornar_mayor(x1, x2):
    if x1 > x2:
        mayor = x1
    else:
        mayor = x2
    return mayor

# bloque principal
valor1 = int(input('Ingresar primer número: '))
valor2 = int(input('Ingresar segundo número: '))
mayor = retornar_mayor(valor1, valor2)
print('El mayor de los dos números es ', mayor)
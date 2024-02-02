"""
Elaborar una función que reciba tres enteros y nos retorne el valor promedio de los mismos.
"""
def calcular_promedio(num1, num2, num3):
    return (num1 + num2 + num3) // 3

# bloque principal
valor1 = int(input('Ingresar número: '))
valor2 = int(input('Ingresar número: '))
valor3 = int(input('Ingresar número: '))
promedio = calcular_promedio(valor1, valor2, valor3)
print('El promedio de los 3 valores ingresados es: ', promedio)
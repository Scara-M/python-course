"""
Desarrollar un programa con dos funciones. 
La primer solicite el ingreso de un entero y muestre el cuadrado de dicho valor. 
La segunda que solicite la carga de dos valores y muestre el producto de los mismos. 
LLamar desde el bloque del programa principal a ambas funciones.
"""
def calcular_cuadrado():
    print('Calcular cuadrado')
    valor = int(input('Ingrese un número: '))
    cuadrado = valor * valor
    print('El cuadrado del número ingresado es ', cuadrado)


def calcular_producto():
    print('Calcular producto')
    valor1 = int(input('Ingrese el primer valor: '))
    valor2 = int(input('Ingrese el segundo valor: '))
    producto = valor1 * valor2
    print('El producto de los números es ', producto)


# bloque principal
calcular_cuadrado()
calcular_producto()

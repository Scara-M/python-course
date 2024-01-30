"""
Confeccionar una función que reciba tres enteros y nos muestre el mayor de ellos. La carga de los valores hacerlo por teclado.
"""

def mostrar_mayor(x1, x2, x3):
    print('El mayor valor de los 3 es ')
    if x1 > x2 and x1 > x3:
        print(x1)
    else:
        if x2 > x3:
            print(x2)
        else:
            print(x3)


def cargar():
    valor1 = int(input('Ingrese el primer valor: '))
    valor2 = int(input('Ingrese el segundo valor: '))
    valor3 = int(input('Ingrese el tercer valor: '))
    mostrar_mayor(valor1, valor2, valor3)


# programa principal
cargar()
"""
Confeccionar una función que reciba tres enteros y los muestre ordenados de menor a mayor. 
En otra función solicitar la carga de 3 enteros por teclado y proceder a llamar a la primer función definida.
"""
def ordenar_ascendente(x1, x2, x3):
    if x1 < x2 and x1 < x3:
        menor = x1
        if x2 < x3:
            medio = x2
            mayor = x3
        else:
            medio = x3
            mayor = x2
    else:
        if x2 < x3:
            menor = x2
            if x1 < x3:
                medio = x1
                mayor = x3
            else:
                medio = x3
                mayor = x1
        else:
            menor = x3
            if x1 < x2:
                medio = x1
                mayor = x2
            else:
                medio = x2
                mayor = x1
    print('Orden ascendente: ', menor, medio, mayor)


def carga_numeros():
    v1 = int(input('Ingresar primer número: '))
    v2 = int(input('Ingresar segundo número: '))
    v3 = int(input('Ingresar tercer número: '))
    ordenar_ascendente(v1, v2, v3)


# bloque principal
carga_numeros()
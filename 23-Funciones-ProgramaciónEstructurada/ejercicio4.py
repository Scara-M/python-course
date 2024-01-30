"""
Desarrollar un programa que solicite la carga de tres valores y muestre el menor. 
Desde el bloque principal del programa llamar 2 veces a dicha función (sin utilizar una estructura repetitiva)
"""
def determinar_menor():
    num1 = int(input('Ingresar primer número: '))
    num2 = int(input('Ingresar segundo número: '))
    num3 = int(input('Ingresar tercer número: '))
    if num1 < num2 and num1 < num3:
        menor = num1
    else:
        if num2 < num3:
            menor = num2
        else:
            menor = num3
    print('El menor de los tres ingresados es ', menor)


# blqoue principal
determinar_menor()
determinar_menor()
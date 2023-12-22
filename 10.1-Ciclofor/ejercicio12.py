"""
Realizar un programa que lea los lados de n triángulos, e informar:
a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
b) Cantidad de triángulos de cada tipo.
"""

n = int(input('Ingresar la cantidad de triángulos a procesar: '))
cant_equi = cant_isos = cant_esc = 0

# Procesar triángulos
for x in range(n):
    print('-'*7)
    lado1 = int(input('Ingresar lado del triángulo: '))
    lado2 = int(input('Ingresar lado del triángulo: '))
    lado3 = int(input('Ingresar lado del triángulo: '))

    # Determinar el tipo de triángulo
    if lado1 == lado2 and lado1 == lado3:
        print('El triángulo es equilátero')
        cant_equi += 1
    elif lado1 != lado2 and lado1 != lado3:
        print('El triángulo es escaleno')
        cant_esc += 1
    else: 
        print('El triángulo es isosceles')
        cant_isos += 1
    print('-'*7)
    
# Salida
print('Hay ', cant_equi, ' triángulos equilateros')
print('Hay ', cant_isos, ' triángulos isosceles')
print('Hay ', cant_esc, ' triángulos escalenos')
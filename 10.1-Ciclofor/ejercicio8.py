"""
Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida de la base y la altura de un triángulo. El programa deberá informar:
a) De cada triángulo la medida de su base, su altura y su superficie.
b) La cantidad de triángulos cuya superficie es mayor a 12.
"""

n = int(input('Ingresa la cantidad de triángulos a analizar: '))
x = 1
cant = 0

# Proceso
for x in range(n):
    print('-'*7)
    print('Triángulo ', x)
    # carga por teclado
    base = float(input('Ingresar la medida de la base del triángulo: '))
    altura = float(input('Ingresar la altura del triángulo: '))
    sup = (base * altura)/2
    
    if sup > 12:
        cant += 1

    print('-'*7)
    print('La base del triángulo ', x, ' es ', base)
    print('La altura del triángulo ', x, ' es ', altura)
    print('La superficie del triángulo ', x, ' es', sup)

# Salida por pantalla
print('La cantidad de triángulos con superficie mayor a 12 es ', cant)
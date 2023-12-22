"""
Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano.
Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante. Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.
"""
n = int(input('Ingresar la cantidad de puntos a analizar: '))
cant1 = cant2 = cant3 = cant4 = cant_origen = 0

for x in range(n):
    print('-'* 7)
    x = int(input('Ingresar la coordenada x: '))
    y = int(input('Ingresar la coordenada y: '))

    # Contar cuadrante
    if x > 0 and y > 0:
        cant1 += 1
    elif x < 0 and y > 0:
        cant2 += 1
    elif x < 0 and y < 0:
        cant3 += 1
    elif x > 0 and y < 0:
        cant4 += 1
    else: 
        cant_origen += 1

# Salida
print('-'* 7)
print('En el primer cuadrante se ingresaron ', cant1, ' puntos')
print('En el segundo cuadrante se ingresaron ', cant2, ' puntos')
print('En el tercer cuadrante se ingresaron ', cant3, ' puntos')
print('En el cuarto cuadrante se ingresaron ', cant4, ' puntos')
print('En el origen se ingresaron ', cant_origen, ' puntos')
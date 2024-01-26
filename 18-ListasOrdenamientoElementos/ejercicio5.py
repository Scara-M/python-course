"""
Cargar una lista con 5 elementos enteros. 
Ordenarla de menor a mayor y mostrarla por pantalla, luego ordenar de mayor a menor e imprimir nuevamente.
"""
numeros = []

# carga de enteros
for x in range(5):
    num = int(input('Ingresar número entero: '))
    numeros.append(num)

print('Lista sin ordenar ', numeros)
print(" ")


# ordenar de menor a mayor
for j in range(4):
    for x in range(4-j):
        if numeros[x] > numeros[x+1]:
            aux = numeros[x]
            numeros[x] = numeros[x+1]
            numeros[x+1]=aux

print('Lista ordenada de menor a mayor ', numeros)
print(" ")

# ordenar de mayor a menor
for j in range(4):
    for x in range(4-j):
        if numeros[x] < numeros[x+1]:
            aux = numeros[x]
            numeros[x] = numeros[x+1]
            numeros[x+1]=aux

print('Lista ordenada de mayor a menor ', numeros)
print(" ")
"""
Cargar una lista con 5 elementos enteros. 
Imprimir el mayor y un mensaje si se repite dentro de la lista (es decir si dicho valor se encuentra en 2 o más posiciones en la lista)
"""
lista = []

# carga de enteros
for x in range(5):
    num = int(input('Ingresar número entero: '))
    lista.append(num)


# buscar el mayor
mayor = lista[0]
posicion = 0
for x in range(1, 5):
    if lista[x] > mayor:
        mayor = lista[x]
        posicion = [x]

# buscar si se repite el mayor
cant = 0
for x in range(5):
    if lista[x] == mayor:
        cant += 1

# Salida
print('La lista es ', lista)
print('El mayor es ', mayor)
if cant > 1:
    print('El elemento se encuentra en más de una posicion')
else:
    print('El elemento se encuentra una vez')
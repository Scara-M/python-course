"""
Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra. 
Definir dos listas paralelas. Mostrar cuantos productos tienen un precio mayor al primer producto ingresado.
"""
productos = []
precios = []

# carga de datos
for x in range(5):
    prod = input('Ingresar el nombre del producto: ')
    productos.append(prod)
    pre = float(input('Ingresar el precio del producto: '))
    precios.append(pre)

# Determinar precio mayor al primer producto
cant = 0   
precio1 = precios[0]
for x in range(1, 5):
    if precios[x] > precio1:
        cant += 1

# Salida
print('La cantidad de productos con precio mayor al primer producto son: ', cant)
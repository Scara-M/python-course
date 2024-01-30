"""
Crear una lista por asignación. La lista tiene que tener 2 elementos. Cada elemento debe ser una lista de 5 enteros.
Calcular y mostrar la suma de cada lista contenida en la lista principal.
"""

lista=[[1,1,1,1,1], [2,2,2,2,2]]

# primera forma
print('Primera forma')
suma1 = lista[0][0] + lista[0][1] + lista[0][2] + lista[0][3] + lista[0][4]
print(suma1)
suma2 = lista[1][0] + lista[1][1] + lista[1][2] + lista[1][3] + lista[1][4]
print(suma2)
print(" ")


# Segunda forma
print('Segunda forma')
suma1 = 0
for x in range(len(lista[0])):
    suma1 += lista[0][x]
print(suma1)

suma2 = 0
for x in range(len(lista[1])):
    suma2 += lista[1][x]
print(suma2)
print(" ")


# Tercera forma
print('Tercera forma')
for k in range(len(lista)):
    suma = 0
    for x in range(len(lista[k])):
        suma += lista[k][x]
    print(suma)
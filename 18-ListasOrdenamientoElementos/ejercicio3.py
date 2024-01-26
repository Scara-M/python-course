"""
Crear una lista y almacenar los nombres de 5 países. Ordenar alfabéticamente la lista e imprimirla.
"""
paises = []

# carga de paises
for x in range(5):
    pais = input('Ingresar el nombre del país: ')
    paises.append(pais)

print('Lista sin ordenar')
print(paises)
print(" ")
# Ordenar alfabeticamente la lista
for j in range(4):
    for x in range(4-j):
        if paises[x] > paises[x + 1]:
            aux = paises[x]
            paises[x] = paises[x + 1]
            paises[x + 1] = aux

# Lista ordenada
print(paises)
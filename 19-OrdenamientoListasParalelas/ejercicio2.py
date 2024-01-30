"""
Crear y cargar en un lista los nombres de 5 países y en otra lista paralela la cantidad de habitantes del mismo. 
Ordenar alfabéticamente e imprimir los resultados. 
Por último ordenar con respecto a la cantidad de habitantes (de mayor a menor) e imprimir nuevamente.
"""
paises = []
habitantes = []

# carga de elementos de la lista
for x in range(5):
    pa = input('Ingresar el nombre del país: ')
    paises.append(pa)
    hab = int(input('Ingresar la cantidad de habitantes: '))
    habitantes.append(hab)

print(" ")
# Orden alfabetico
for k in range(4):
    for x in range(4 - k):
        if  paises[x] > paises[x+1]:
            aux1 = paises[x]
            paises[x] = paises[x+1]
            paises[x+1] = aux1
            aux2 = habitantes[x]
            habitantes[x] = habitantes[x+1]
            habitantes[x+1] = aux2


print('Orden alfabetico')
for x in range(5):
    print(paises[x], habitantes[x])
print(" ")

# Orden por cantidad de habitantes de mayor a menor
for k in range(4):
    for x in range(4 - k):
        if  habitantes[x] < habitantes[x+1]:
            aux1 = paises[x]
            paises[x] = paises[x+1]
            paises[x+1] = aux1
            aux2 = habitantes[x]
            habitantes[x] = habitantes[x+1]
            habitantes[x+1] = aux2


print('Orden de mayor a menor por cantidad de habitantes')
for x in range(5):
    print(paises[x], habitantes[x])
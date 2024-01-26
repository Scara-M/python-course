"""
Se debe crear y cargar una lista donde almacenar 5 sueldos. Ordenar de menor a mayor la lista.
"""
sueldos = []

for x in range(5):
    sueldo = int(input('Ingresar sueldo: '))
    sueldos.append(sueldo)

print(sueldos)

# Ordenar de menor a mayor
for x in range(4):
    for x in range(4):
        if sueldos[x] > sueldos[x + 1]:
            aux = sueldos[x]
            sueldos[x] = sueldos[x + 1]
            sueldos[x + 1] = aux

print('Los elementos de la lista ordenado son ', sueldos)
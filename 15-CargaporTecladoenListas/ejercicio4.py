"""
Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float)
Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio y cuántas más bajas.
"""
alturas = []
acum = 0
cant_altas = 0
cant_bajas = 0

# Cargar alturas
for x in range(5):
    alt = float(input('Ingresar altura de la persona: '))
    alturas.append(alt)
    acum += alt


prom = acum / 5

for x in range(5):
    if alturas[x] > prom:
        cant_altas += 1
    else:
        cant_bajas += 1


# Salida por pantalla
print('La alturas de las personas son ', alturas)
print('El promedio de las personas es ', prom)
print('La cantidad de personas más altas que el promedio son: ', cant_altas)
print('La cantidad de personas más bajas que el promedio son: ', cant_bajas)
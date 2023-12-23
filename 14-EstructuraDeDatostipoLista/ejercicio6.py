"""
Definir una lista que almacene por asignación los nombres de 5 personas. Contar cuantos de esos nombres tienen 5 o más caracteres.
"""
lista = ['Mariano', 'Maria', 'Ana', 'Ernesto', 'Juan']
cant = 0
x = 0

while x < len(lista):
    if len(lista[x]) >= 5:
        cant += 1
    x += 1

# Salida
print('La cantidad de nombres que tienen 5 o más caracteres son ', cant)
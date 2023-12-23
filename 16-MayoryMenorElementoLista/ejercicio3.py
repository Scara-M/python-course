"""
Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. 
Mostrar el nombre de persona menor en orden alfabético
"""
nombres = []

# Carga de nombres
for x in range(5):
    nom = input('Ingresar nombre: ')
    nombres.append(nom)

# Menor orden alfabetico
menor = nombres[0]
for x in range(1, 5):
    if nombres[x] < menor:
        menor = nombres[x]

# Salida
print('La lista es ', nombres)
print('EL menor en orden alfabetico es ', menor)
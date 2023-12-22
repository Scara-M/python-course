"""
Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.
"""

# ------------ Lista 1
print('-'*5)
print('Lista 1')
x = 1
acum1 = 0
while x <= 15:
    num = int(input('Ingresar valor: '))
    acum1 += num
    x += 1


# ----------- Lista 2
print('-'*5)
print('Lista 2')
x = 1
acum2 = 0
while x <= 15:
    num = int(input('Ingresar valor: '))
    acum2 += num
    x += 1


# ---------- Comparar listas
print('-'*5)
if acum1 > acum2:
    print('La lista 1 es mayor a la 2')
elif acum2 > acum1:
    print('La lista 2 es mayor a la lista 1')
else:
    print('Las listas son iguales')
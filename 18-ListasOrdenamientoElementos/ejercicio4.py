"""
Solicitar por teclado la cantidad de empleados que tiene la empresa. 
Crear y cargar una lista con todos los sueldos de dichos empleados. Imprimir la lista de sueldos ordenamos de menor a mayor.
"""
n = int(input('Ingresar la cantidad de empleados de la empresa: '))

sueldos = []

# Carga de sueldos
for x in range(n):
    su = int(input('Ingresar el sueldo del empleado: '))
    sueldos.append(su)

print('Sueldos sin ordenar', sueldos)


# Ordenar sueldos de menor a mayor
for j in range(n-1):
    for x in range(n - 1 - j):
        if sueldos[x] > sueldos[x+1]:
            aux = sueldos[x]
            sueldos[x] = sueldos[x+1]
            sueldos[x+1] = aux

#Sueldos ordenados
print('Sueldos ordenados ', sueldos)
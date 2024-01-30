"""
Confeccionar un programa que permita cargar los nombres de 5 alumnos y sus notas respectivas. Luego ordenar las notas de mayor a menor. Imprimir las notas y los nombres de los alumnos.
"""
alumnos = []
notas = []

# carga de datos
for x in range(5):
    nom = input('Ingresar nombre del alumno: ')
    no = int(input('Ingresar nota del alumno: '))
    alumnos.append(nom)
    notas.append(no)


# ordenar de mayor a menor las notas
for k in range(4):
    for x in range(4-k):
        if notas[x] < notas[x+1]:
            aux1 = notas[x]
            notas[x] = notas[x+1]
            notas[x+1] = aux1
            aux2 = alumnos[x]
            alumnos[x] = alumnos[x+1]
            alumnos[x+1] = aux2

# Lista de alumnos y sus notas
for x in range(5):
    print(alumnos[x], notas[x])
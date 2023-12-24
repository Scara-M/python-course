"""
En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben procesar de acuerdo a lo siguiente:
a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
b) Realizar un listado que muestre los nombres, notas y condición del alumno. En la condición, colocar "Muy Bueno" si la nota es mayor o igual a 8, "Bueno" si la nota está entre 4 y 7, y colocar "Insuficiente" si la nota es inferior a 4.
c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”.
"""
alumnos = []
notas = []

# carga de datos alumnos
for x in range(4):
    nom = input('Ingresar el nombre del estudiante: ')
    alumnos.append(nom)
    no = int(input('Ingresar la nota del alumno: '))
    notas.append(no)

# definir condicion
cant = 0
for x in range(4):
    print(alumnos[x])
    print(notas[x])

    if notas[x] >= 8:
        print('Muy bueno')
        cant += 1
    elif notas[x] >= 4 and notas[x] < 8:
        print('Bueno')
    else:
        print('Insuficiente')

print('La cantidad de estudiantes con condición muy bueno son: ', cant)
"""
Se tiene que cargar la siguiente información:
· Nombres de 3 empleados
· Ingresos en concepto de sueldo, cobrado por cada empleado, en los últimos 3 meses.
Confeccionar el programa para:

a) Realizar la carga de los nombres de empleados y los tres sueldos por cada empleado.
b) Generar una lista que contenga el ingreso acumulado en sueldos en los últimos 3 meses para cada empleado.
c) Mostrar por pantalla el total pagado en sueldos a cada empleado en los últimos 3 meses
d) Obtener el nombre del empleado que tuvo el mayor ingreso acumulado
"""
nombres = []
sueldos = []
totalsueldos = []

# carga de datos
for x in range(3):
    nom = input('Ingresar el nombre del empleado: ')
    nombres.append(nom)
    su1 = int(input('Ingresar sueldo del primer mes: '))
    su2 = int(input('Ingresar sueldo del segundo mes: '))
    su3 = int(input('Ingresar sueldo del tercer mes: '))
    sueldos.append([su1, su2, su3])


# lista de ingreso acumulado por empleado
for x in range(3):
    total = sueldos[x][0] + sueldos[x][1] +  sueldos[x][2]
    totalsueldos.append(total)


# muestra de sueldos acumulados
for x in range(3):
    print(nombres[x], totalsueldos[x])


# empleado con mayor ingreso acumulado
posmayor = 0
mayor = totalsueldos[0]
for x in range(1, 3):
    if totalsueldos[x] > mayor:
        mayor = totalsueldos[x]
        posmayor = x
print('Empleado con mayores ingresos en los últimos 3 meses')
print(nombres[posmayor])
print('con un ingreso de ', mayor)
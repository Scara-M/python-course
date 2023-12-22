"""
En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.
"""
x = 1
n = int(input('Ingresar la cantidad de empleados: '))
menos300 = mayor300 = 0

# Procesar empleados
while x <= n:
    sueldo = int(input('Ingresar el sueldo del empleado: '))
    if sueldo <= 300:
        menos300 += 1
    else:
        mayor300 += 1
    x += 1


# Salida por pantalla
print('La cantidad de empleados que cobra por debajo de los 300 son: ', menos300)
print('La cantidad de empleados que cobra por arriba de los 300 son: ', mayor300)
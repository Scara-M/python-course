"""
Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas.
"""
# Inicializar y cargar variables
n = int(input('Ingresar la cantidad de alturas a procesar: '))
x = 1
acumulada = 0

# Procesar alturas
while x <= n:
    altura = float(input('Ingresar la altura de la persona: '))
    acumulada += altura
    x += 1

# Promedio
promedio = acumulada / n

# Salida por pantalla
print('-'*5)
print('La altura promedio de las personas es ', promedio)
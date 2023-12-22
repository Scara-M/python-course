"""
Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
a) La cantidad de valores ingresados negativos.
b) La cantidad de valores ingresados positivos.
c) La cantidad de múltiplos de 15.
d) El valor acumulado de los números ingresados que son pares.
"""
negativos = 0
positivos = 0
multiplos15 = 0
acum_pares = 0

for x in range(10):
    num = int(input('Ingresar entero: '))

    if num < 0:
        negativos += 1
    
    if num >= 0:
        positivos += 1
    
    if num % 15 == 0:
        multiplos15 += 1
    
    if num % 2 == 0:
        acum_pares += num
    
# Salida
print('La cantidad de números negativos es ', negativos)
print('La cantidad de números positivos es ', positivos)
print('La cantidad de múltiplos de 15 es ', multiplos15)
print('El valor acumulado de los pares ingresados es ', acum_pares)
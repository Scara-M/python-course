"""
Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas. 
Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años)
"""

nombres = []
edades = []

# cargar datos 
for x in range(5):
    nom = input('Ingresar el nombre de la persona: ')
    nombres.append(nom)
    edad = int(input('Ingresar la edad de la persona: '))
    edades.append(edad)


# Mostrar los nombres de las personas mayores a 18 años
for x in range(5):
    if edades[x] > 18:
        print(nombres[x])
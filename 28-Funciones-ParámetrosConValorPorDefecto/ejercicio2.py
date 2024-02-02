"""
Confeccionar una función que reciba entre 2 y 5 enteros. 
La misma nos debe retornar la suma de dichos valores. 
Debe tener tres parámetros por defecto.
"""
def suma (num1, num2 , num3 = 0, num4 = 0, num5 = 0):
    suma = num1 + num2 + num3 + num4 + num5
    print('La suma de los números es ', suma)

# bloque principal
suma(1,2,3)

'''
Frente a los rumores de una cuarta ola de la pandemia, la Dirección Regional 
de Salud del Cusco desea implementar acciones de prevención. Para lo cual, 
se tiene la información del número de contagiados COVID de cada distrito de 
cada una de las provincias del departamento del Cusco, correspondientes a los 
meses de mayo y junio. Se implementa una acción de prevención en aquellos distritos 
que tengan más de 100 contagiados en los dos meses o que el número de contagiados en el 
mes de junio sea 2 veces más que los del mes de mayo. Escribir un programa modular 
que determine en cúantos distritos de una determinada provincia se debe implementar acciones de prevención.
'''

# Modulo para determinar si un distrito cumple condiciones para acciones de prevención
def Prevencion(nroMes1, nroMes2):
    # Si el nro de contagiados en el mes de mayo es mayor a 100 o el nro de 
    # contagiados en el mes de junio es 2 veces mayor que los del mes de mayo
    return (nroMes1 > 100) or (nroMes2 > nroMes1 * 2)

deef 
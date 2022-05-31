'''
Desarrolle una funcion en donde reciba como parámetro de entrada una oración y 
retorne en una lista la longitud de cada palabra.
Ejemplo: longitud (‘Python es muy fácil’)
Resultado: [6, 2, 3, 5]
'''
oracion = 'Python es muy fácil'

def longitud_de_palabra(oracion):
    lista = oracion.split()
    longitud = []
    for i in lista:
        longitud.append(len(i))
    return longitud

print(longitud_de_palabra(oracion))


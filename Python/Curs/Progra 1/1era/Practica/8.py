'''
EScribir una funcion recursiva que nos permita obtener
el determinante de una matriz cuadrada de dimension n
'''

# primera forma
def determinante(matriz):
    if len(matriz) == 1:
        return matriz[0][0]
    else:
        return sum([(-1)**i * matriz[0][i] * determinante([fila[:i] + fila[i+1:] for fila in matriz[1:]]) for i in range(len(matriz))])

# segunda forma
def determinante2(matriz):
    if len(matriz) == 1:
        return matriz[0][0]
    else:
        return sum([(-1)**i * matriz[0][i] * determinante2([fila[:i] + fila[i+1:] for fila in matriz[1:]]) for i in range(len(matriz))])

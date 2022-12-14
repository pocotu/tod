# modulo que crean una matriz de 9 x 9 con valores aleatorios entre 1 y 9 con algunas casillas vacías
def sudoku(Mat):
    respuesta = []
    for i in range(len(Mat)):
        respuesta.append(False)
    for i in range(len(Mat)):
        for j in range(len(Mat)):
            if Mat[i][j] == 1:
                respuesta[i] = True
    return respuesta

# Escriba una función que reciba una matriz 9 x 9 como parámetro,

# que represente una propuesta de solución para un Sudoku, y pruebe si la matriz es una 
# solución válida para el juego, devolviendo True en caso verdadero y False, caso contrario.

# ingresar la matriz para el sudoku de 9 x 9 por columnas


# imprimir la matriz de 9 x 9 de forma de sudoku


# verificar si la matriz es una solución válida para el juego

# programa principal


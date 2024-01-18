def solucion(mat):
    # Verificar si cada cuadrado cumple con la regla (a)
    for i in range(3):
        # Recorrer cada cuadrado
        for j in range(3):
            # crear un diccionario para guardar los valores del cuadrado
            cuad = {}
            # recorrer cada elemento del cuadrado y verificar si ya existe en el diccionario
            for k in range(3):
                for l in range(3):
                    # si el elemento [3*i+k][3*j+l] ya existe en el diccionario, entonces no es una solucion valida
                    if mat[3*i+k][3*j+l] in cuad:
                        # si no es una solucion valida, retornar False
                        return False
                    # si el elemento [3*i+k][3*j+l] no existe en el diccionario, agregarlo
                    cuad[mat[3*i+k][3*j+l]] = True
    
    # Verificar si cada fila cumple con la regla (b)
    for i in range(9):
        # crear un diccionario para guardar los valores de la fila
        fila = {}
        # recorrer cada elemento de la fila y verificar si ya existe en el diccionario
        for j in range(9):
            # si el elemento [i][j] ya existe en el diccionario, entonces no es una solucion valida
            if mat[i][j] in fila:
                return False
            # si el elemento [i][j] no existe en el diccionario, agregarlo
            fila[mat[i][j]] = True
    
    # Verificar si cada columna cumple con la regla (c)
    for j in range(9):
        # crear un diccionario para guardar los valores de la columna
        col = {}
        # recorrer cada elemento de la columna y verificar si ya existe en el diccionario
        for i in range(9):
            # si el elemento [i][j] ya existe en el diccionario, entonces no es una solucion valida
            if mat[i][j] in col:
                return False
            # si el elemento [i][j] no existe en el diccionario, agregarlo
            col[mat[i][j]] = True
    
    return True

def main():
    # Ejemplo de matriz con una solución válida para el juego Sudoku
    mat = [
        [8, 5, 9, 6, 1, 2, 4, 3, 7],
        [7, 2, 3, 8, 5, 4, 1, 6, 9],
        [1, 6, 4, 3, 7, 9, 8, 5, 2],
        [9, 8, 6, 1, 4, 7, 3, 2, 5],
        [3, 7, 5, 2, 6, 8, 9, 4, 1],
        [2, 4, 1, 9, 3, 5, 7, 8, 6],
        [5, 9, 7, 4, 8, 1, 2, 6, 3],
        [6, 3, 2, 5, 9, 7, 8, 1, 4],
        [4, 1, 8, 7, 2, 3, 5, 9, 6]]
    
    # Verificar si la matriz es una solución válida para el juego Sudoku
    if solucion(mat):
        print("La matriz es una solución válida para el juego Sudoku.")
    else:
        print("La matriz NO es una solución válida para el juego Sudoku.")

main()

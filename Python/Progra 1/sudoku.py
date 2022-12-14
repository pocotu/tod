# Escriba una función que reciba una matriz 9 x 9 como parámetro,
def sudoku(Mat):
    respuesta = []
    for i in range(len(Mat)):
        respuesta.append(False)
    for i in range(len(Mat)):
        for j in range(len(Mat)):
            if Mat[i][j] == 1:
                respuesta[i] = True
    return respuesta

# que represente una propuesta de solución para un Sudoku, y pruebe si la matriz es una 
# solución válida para el juego, devolviendo True en caso verdadero y False, caso contrario.

# ingresar la matriz para el sudoku de 9 x 9 por columnas
def ingresar_matriz():
    Mat = []
    # si no se ingresa un valor numérico, se produce un error de tipo ValueError que se captura en el except y se vuelve a pedir el valor
    for i in range(9):
        Mat.append([])
        for j in range(9):
            try:
                Mat[i].append(int(input("Ingrese el valor de la posición Mat[{}][{}]: ".format(i, j))))
            except ValueError:
                print("El valor ingresado no es un número entero")
                j -= 1
    return Mat

# imprimir la matriz de 9 x 9 de forma de sudoku
def imprimir_matriz(Mat):
    for i in range(len(Mat)):
        for j in range(len(Mat)):
            print(Mat[i][j], end = " ")
            if j == 2 or j == 5:
                print("|", end = " ")
        print()
        if i == 2 or i == 5:
            print("---------------------")


# verificar si la matriz es una solución válida para el juego
def verificar(Mat):
    for i in range(len(Mat)):
        for j in range(len(Mat)):
            if Mat[i][j] == 0:
                return False
    return True

# programa principal
def main():
    Mat = ingresar_matriz()
    print("La matriz ingresada es:")
    imprimir_matriz(Mat)
    if verificar(Mat):
        print("La matriz ingresada es una solución válida para el juego")
    else:
        print("La matriz ingresada no es una solución válida para el juego")

main()






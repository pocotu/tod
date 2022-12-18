# supongq que una mattriz binaria Mat represente enlaces entre ciudades,
# donde, si Mat[i][j] = 1, entonces hay un enlace entre la ciudad i y la ciudad j.
# ejemplo: Mat = [[0, 1, 1], [0, 0, 0], [1, 0, 0]]

# escriba una funcion verificar(Mat) que reciba como parametro una matriz
# cuadrada Mat, indicando las rutas entre ciudades, y devuelva una lista respuesta

def verificar(Mat):
    respuesta = []
    for i in range(len(Mat)):
        for j in range(len(Mat)):
            if Mat[i][j] == 1 and Mat[j][i] == 1:
                respuesta.append(i)
                respuesta.append(j)
    return respuesta

# escribir una funcion para determinar las ciudades a laa que llegan las rutas,
# mas sin rutas que salen de la ciudad, indicandolo esto en la lista respuesta,
# tal que respuesta[i] recibe True si la ciudad i satisface esta propiedad y
# False, caso cotrario.
def ciudades_con_entrada_y_sin_salida(Mat):
    respuesta = []
    for i in range(len(Mat)):
        if sum(Mat[i]) == 0 and sum([Mat[j][i] for j in range(len(Mat))]) > 0:
            respuesta.append(True)
        else:
            respuesta.append(False)
    return respuesta

# matriz de nxn
def matriz(n):
    Mat = []
    for i in range(n):
        Mat.append([])
        for j in range(n):
            Mat[i].append(0)
    return Mat


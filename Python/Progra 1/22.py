# Suponga que una matriz binaria Mat represente enlaces entre ciudades, donde, si una posición 
# Mat[i][j] tiene el valor 1, entonces hay una ruta de la ciudad i a la ciudad j. 
# Sea el siguiente ejemplo de matriz:

# Mat = [[0, 1, 1], [0, 0, 0], [1, 0, 0]]

# En este caso, hay rutas de la ciudad 0 a las ciudades 1 y 2, y de la ciudad 2 a la ciudad 0. 
# Para cada ítem de abajo

# escriba una función verificar(Mat) que reciba como parámetro una matriz 
# cuadrada Mat, indicando las rutas entre ciudades, y devuelva una lista respuesta.
def verificar(Mat):
    respuesta = []
    for i in range(len(Mat)):
        respuesta.append(False)
    for i in range(len(Mat)):
        for j in range(len(Mat)):
            if Mat[i][j] == 1:
                respuesta[i] = True
    return respuesta

# Escribir una función para determinar las ciudades a las que llegan las rutas, más sin rutas que salen 
# de la ciudad, indicándolo esto en la lista respuesta, tal que respuesta[i] recibe True si la ciudad i 
# satisface esta propiedad y False, caso contrario.


# Escribir una función para determinar las ciudades con salida de rutas, más sin rutas 
# llegando a la ciudad, indicando esto en la lista respuesta, tal que respuesta[i] 
# recibe True caso la ciudad i satisfaga esta propiedad y False caso contrario.

# Escribe una función para determinar ciudades aisladas (sin rutas que lleguen o salgan de la 
# ciudad), indicándolo esto en la lista respuesta, tal que respuesta[i] reciba True caso 
# la ciudad i satisfaga esta propiedad y False, caso contrario.
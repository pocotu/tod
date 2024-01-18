def cuenta_habitaciones(matriz):
    # Creamos una matriz de booleanos para marcar los espacios vacíos que ya hemos visitado
    visitados = [[False for j in range(len(matriz[0]))] for i in range(len(matriz))]

    # Inicializamos el contador de habitaciones
    habitaciones = 0

    # Recorremos cada uno de los espacios de la matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            # Si encontramos un espacio vacío y no lo hemos visitado todavía, entonces es una habitación nueva
            if matriz[i][j] == "." and not visitados[i][j]:
                habitaciones += 1
                # Llamamos a la función recursiva para explorar todos los espacios vacíos adyacentes
                explorar_habitacion(matriz, visitados, i, j)

    return habitaciones

def explorar_habitacion(matriz, visitados, fila, columna):
    # Definimos una lista con los movimientos posibles
    movimientos = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    # Marcamos el espacio actual como visitado
    visitados[fila][columna] = True

    # Recorremos cada uno de los movimientos posibles
    for movimiento in movimientos:
        # Calculamos la nueva posición
        nueva_fila = fila + movimiento[0]
        nueva_columna = columna + movimiento[1]
        # Si la nueva posición es válida y es un espacio vacío, entonces la exploramos
        if es_posicion_valida(matriz, nueva_fila, nueva_columna) and matriz[nueva_fila][nueva_columna] == "." and not visitados[nueva_fila][nueva_columna]:
            explorar_habitacion(matriz, visitados, nueva_fila, nueva_columna)

def es_posicion_valida(matriz, fila, columna):
    # Verificamos que la fila y la columna estén dentro de los límites de la matriz
    return 0 <= fila < len(matriz) and 0 <= columna < len(matriz[0])

matriz = [  ["#", "#", "#", "#", "#", "#", "#"],
            ["#", ".", ".", "#", ".", ".", "#"],
            ["#", ".", "#", "#", "#", ".", "#"],
            ["#", ".", ".", ".", ".", ".", "#"],
            ["#", "#", "#", "#", "#", "#", "#"]]

print(cuenta_habitaciones(matriz))  # debería imprimir 5

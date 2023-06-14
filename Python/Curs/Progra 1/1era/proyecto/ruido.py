
def distancia_hamming(secuencia1, secuencia2):
    # Inicializar la distancia de Hamming en 0
    distancia = 0
    # Recorrer las posiciones de las secuencias
    for i in range(len(secuencia1)):
        # Si los caracteres en la misma posición son diferentes
        if secuencia1[i] != secuencia2[i]:
            # Incrementar la distancia de Hamming en 1
            distancia += 1
    # Devolver la distancia de Hamming
    return distancia











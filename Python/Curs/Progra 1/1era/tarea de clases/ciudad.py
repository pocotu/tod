def verificar(Mat):
    def verificar_1(Mat):
        # lista vacia para guardar los resultados
        respuesta = []
        # recorrer la matriz
        for i in range(1, len(Mat)):
            # agregar a la lista los resultados de la condicion de la funcion any (si hay un 1 en la fila)
            respuesta.append(any(Mat[0][j] for j in range(len(Mat[i])) if i != j))
        return respuesta

    def verificar_2(Mat):
        respuesta = []
        for i in range(len(Mat)):
            respuesta.append(any(Mat[i][j] for j in range(len(Mat[i])) if i != j))
        return respuesta

    def verificar_3(Mat):
        respuesta = []
        for i in range(len(Mat)):
            respuesta.append(all(Mat[i][j] for j in range(len(Mat[i])) if i != j))
        return respuesta

    resultado_1 = verificar_1(Mat)
    resultado_2 = verificar_2(Mat)
    resultado_3 = verificar_3(Mat)

    return [resultado_1, resultado_2, resultado_3]

# programa principal para una matriz de 3x3
def main():
    Mat = [[0, 1, 0],
           [0, 0, 1],
           [1, 0, 0]]
    print("La lista de ciudades que muestra son las que tienen al menos una carretera que las conecta con otra ciudad.")
    # imprimir los resultados de la funcion verificar de la matriz Mat
    print(verificar(Mat)[0])
    print(verificar(Mat)[1])
    print(verificar(Mat)[2])

main()


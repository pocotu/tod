'''
triangulo de pascal con numeros enteros usando recursividad
'''

def TrianguloPascal(n):
    if n==0:
        return 1
    else:
        return TrianguloPascal(n-1) + TrianguloPascal(n-2)

def crearTriangulo(n_filas):
    for fila in range(n_filas):
        for j in range(n_filas-fila+1):
            print(" ", end="")
        if fila == 0:
            print("1 1")
        else:
            for j in range(fila+2):
                print(TrianguloPascal(fila+1, j), end=" ")
            print()
        
crearTriangulo(int(input("Indica el número de filas que desee: ")))
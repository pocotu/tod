'''
Cuadrado mágico. Un cuadrado mágico es aquel dividido en líneas 
y columnas, con un número en cada posición y en el cual la suma de 
las líneas, columnas y diagonales es la misma. Por ejemplo, vea 
un cuadrado mágico de lado 3, con números de 1 a 9:
8 3 4
1 5 9
6 7 2
Implemente una función que identifica y muestra en pantalla 
todos los cuadrados mágicos con las características mencionadas. 
Sugerencia: produzca todas las combinaciones posibles y verifique 
la suma cuando complete cada cuadrado. Usar un vector de 1 a 9 
parece ser más simple que usar una matriz 3x3.
'''

# Genera todas las combinaciones posibles de 1 a 9
def generar_cuadrado_magico_aleatorio():
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                for l in range(1, 10):
                    for m in range(1, 10):
                        for n in range(1, 10):
                            for o in range(1, 10):
                                for p in range(1, 10):
                                    for q in range(1, 10):
                                        # si la suma de cada fila, columna y diagonal es igual
                                        if i + j + k == l + m + n == o + p + q == i + l + o == j + m + p == k + n + q == i + m + q == k + m + o:
                                            # si i es distinto de j, k, l, m, n, o, p, q
                                            if (i != j) and (i != k) and (i != l) and (i != m) and (i != n) and (i != o) and (i != p) and (i != q):
                                                # si j es distinto de k, l, m, n, o, p, q
                                                if (j != k) and (j != l) and (j != m) and (j != n) and (j != o) and (j != p) and (j != q):
                                                    # si k es distinto de l, m, n, o, p, q
                                                    if (k != l) and (k != m) and (k != n) and (k != o) and (k != p) and (k != q):
                                                        # si l es distinto de m, n, o, p, q
                                                        if (l != m) and (l != n) and (l != o) and (l != p) and (l != q):
                                                            # si m es distinto de n, o, p, q
                                                            if (m != n) and (m != o) and (m != p) and (m != q):
                                                                # si n es distinto de o, p, q
                                                                if (n != o) and (n != p) and (n != q):
                                                                    # si o es distinto de p, q
                                                                    if (o != p) and (o != q):
                                                                        # si p es distinto de q
                                                                        if (p != q):
                                                                            print(i, j, k)
                                                                            print(l, m, n)
                                                                            print(o, p, q)
                                                                            print()
                                  
generar_cuadrado_magico_aleatorio()

# if i != j and i != k and i != l and i != m and i != n and i != o and i != p and i != q and j != k and j != l and j != m and j != n and j != o and j != p and j != q and k != l and k != m and k != n and k != o and k != p and k != q and l != m and l != n and l != o and l != p and l != q and m != n and m != o and m != p and m != q and n != o and n != p and n != q and o != p and o != q and p != q:

    


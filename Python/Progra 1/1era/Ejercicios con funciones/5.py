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

# Validar cuadro magico
def validar_cuadro_magico(cuadro_magico):
    # Verificar que sea una matriz de 3x3
    if len(cuadro_magico) == 3:
        for fila in cuadro_magico:
            if len(fila) != 3:
                return False
    else:
        return False
    # Verificar que los valores sean del 1 al 9
    for fila in cuadro_magico:
        for valor in fila:
            if valor < 1 or valor > 9:
                return False
    # Verificar que no haya valores repetidos
    valores = []
    for fila in cuadro_magico:
        for valor in fila:
            if valor in valores:
                return False
            else:
                valores.append(valor)
    # Verificar que la suma de las filas, columnas y diagonales sea igual
    suma = sum(cuadro_magico[0])
    # Verificar filas
    for fila in cuadro_magico:
        if sum(fila) != suma:
            return False
    # Verificar columnas
    for i in range(3):
        if cuadro_magico[0][i] + cuadro_magico[1][i] + cuadro_magico[2][i] != suma:
            return False
    # Verificar diagonales
    if cuadro_magico[0][0] + cuadro_magico[1][1] + cuadro_magico[2][2] != suma:
        return False
    if cuadro_magico[0][2] + cuadro_magico[1][1] + cuadro_magico[2][0] != suma:
        return False
    return True

# Generador de cuadrados magicos 3x3
def generador_cuadrado_magico():
    suma_columnas = []
    suma_filas = []
    suma_diagonal = []
    suma_diagonal_inversa = []
    # matriz de 3x3
    matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    # lista de 1 a 9
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # recorre la lista de 1 a 9
    for i in range(len(lista)):
        # recorre la lista de 1 a 9
        for j in range(len(lista)):
            # recorre la lista de 1 a 9
            for k in range(len(lista)):
                # recorre la lista de 1 a 9
                for l in range(len(lista)):
                    # recorre la lista de 1 a 9
                    for m in range(len(lista)):
                        # recorre la lista de 1 a 9
                        for n in range(len(lista)):
                            # recorre la lista de 1 a 9
                            for o in range(len(lista)):
                                # recorre la lista de 1 a 9
                                for p in range(len(lista)):
                                    # recorre la lista de 1 a 9
                                    for q in range(len(lista)):
                                        # asigna los valores de la lista a la matriz
                                        matriz[0][0] = lista[i]
                                        print(lista[i])
                                        matriz[0][1] = lista[j]
                                        print(lista[j])
                                        matriz[0][2] = lista[k]
                                        print(lista[k])
                                        matriz[1][0] = lista[l]
                                        print(lista[l])
                                        matriz[1][1] = lista[m]
                                        print(lista[m])
                                        matriz[1][2] = lista[n]
                                        print(lista[n])
                                        matriz[2][0] = lista[o]
                                        print(lista[o])
                                        matriz[2][1] = lista[p]
                                        print(lista[p])
                                        matriz[2][2] = lista[q]
                                        print(lista[q])
                                        
                                        # suma las columnas
                                        suma_columnas.append(matriz[0][0] + matriz[1][0] + matriz[2][0])
                                        suma_columnas.append(matriz[0][1] + matriz[1][1] + matriz[2][1])
                                        suma_columnas.append(matriz[0][2] + matriz[1][2] + matriz[2][2])
                                        # suma las filas
                                        suma_filas.append(matriz[0][0] + matriz[0][1] + matriz[0][2])
                                        suma_filas.append(matriz[1][0] + matriz[1][1] + matriz[1][2])
                                        suma_filas.append(matriz[2][0] + matriz[2][1] + matriz[2][2])
                                        # suma la diagonal
                                        suma_diagonal.append(matriz[0][0] + matriz[1][1] + matriz[2][2])
                                        # suma la diagonal inversa
                                        suma_diagonal_inversa.append(matriz[0][2] + matriz[1][1] + matriz[2][0])
                                        # verifica si las sumas de las columnas, filas, diagonales y diagonales inversas son iguales
                                        if suma_columnas[0] == suma_columnas[1] == suma_columnas[2] == suma_filas[0] == suma_filas[1] == suma_filas[2] == suma_diagonal[0] == suma_diagonal_inversa[0]:
                                            # muestra el cuadrado mágico
                                            print(matriz[0][0], matriz[0][1], matriz[0][2])
                                            print(matriz[1][0], matriz[1][1], matriz[1][2])
                                            print(matriz[2][0], matriz[2][1], matriz[2][2])
                                            print()
                                        # vacia las listas
                                        suma_columnas.clear()
                                        suma_filas.clear()
                                        suma_diagonal.clear()
                                        suma_diagonal_inversa.clear()


def menu():
    print('''
    1. Verificar si un cuadrado mágico es válido
    2. Generar cuadrados mágicos
    3. Salir
    ''')
    opcion = int(input('Ingrese una opción: '))
    if opcion == 1:
        cuadro_magico = []
        for i in range(3):
            fila = input('Ingrese la fila {}: '.format(i + 1))
            fila = fila.split()
            fila = [int(valor) for valor in fila]
            cuadro_magico.append(fila)
        print(cuadro_magico)
        if es_cuadro_magico(cuadro_magico):
            print('Es un cuadrado mágico')
        else:
            print('No es un cuadrado mágico')
    elif opcion == 2:
        generador_cuadrado_magico()
    elif opcion == 3:
        print('Hasta luego!')
    else:
        print('Opción inválida')

menu()

###### Muy inefficiente #####
#def cuadro_magico():
#    # lista con los numeros del 1 al 9
#    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#    # lista con las combinaciones de los numeros
#    combinaciones = []
#    # lista con los cuadrados magicos
#    cuadrados_magicos = []
#    
#    # crea una lista con todas las combinaciones posibles de los numeros
#    for i in range(len(numeros)):
#        for j in range(len(numeros)):
#            for k in range(len(numeros)):
#                for l in range(len(numeros)):
#                    for m in range(len(numeros)):
#                        for n in range(len(numeros)):
#                            for o in range(len(numeros)):
#                                for p in range(len(numeros)):
#                                    for q in range(len(numeros)):
#                                        combinaciones.append([numeros[i], numeros[j], numeros[k], numeros[l], numeros[m], numeros[n], numeros[o], numeros[p], numeros[q]])
#    
#    # elimina las combinaciones que tengan numeros repetidos
#    for combinacion in combinaciones:
#        if len(combinacion) == len(set(combinacion)):
#            cuadrados_magicos.append(combinacion)
#    
#    # imprime los cuadrados magicos
#    for cuadrado in cuadrados_magicos:
#        # imprime el cuadrado
#        print(f"{cuadrado[0]} {cuadrado[1]} {cuadrado[2]}")
#        print(f"{cuadrado[3]} {cuadrado[4]} {cuadrado[5]}")
#        print(f"{cuadrado[6]} {cuadrado[7]} {cuadrado[8]}")
#        # imprime un salto de linea para separar los cuadrados
#        print()
#        
#        # suma de las filas
#        fila1 = cuadrado[0] + cuadrado[1] + cuadrado[2]
#        fila2 = cuadrado[3] + cuadrado[4] + cuadrado[5]
#        fila3 = cuadrado[6] + cuadrado[7] + cuadrado[8]
#        # suma de las columnas
#        columna1 = cuadrado[0] + cuadrado[3] + cuadrado[6]
#        columna2 = cuadrado[1] + cuadrado[4] + cuadrado[7]
#        columna3 = cuadrado[2] + cuadrado[5] + cuadrado[8]
#        # suma de las diagonales
#        diagonal1 = cuadrado[0] + cuadrado[4] + cuadrado[8]
#        diagonal2 = cuadrado[2] + cuadrado[4] + cuadrado[6]
#
#        # verifica si las sumas de las filas, columnas y diagonales son iguales
#        if fila1 == fila2 == fila3 == columna1 == columna2 == columna3 == diagonal1 == diagonal2:
#            print("Es un cuadrado magico")
#        else:
#            print("No es un cuadrado magico")
#        # imprime un salto de linea para separar los cuadrados
#        print()
#
#cuadro_magico()
'''
Se le da un número entero n y una matriz a1, a2, ..., an.
Debes reordenar los elementos del arreglo a de tal manera que la 
suma de MEX en los prefijos (i-esimo prefijo es a1, a2, ..., ai) 
se maximiza.

Formalmente, debe encontrar una matriz b1, b2, ..., bn tal que,
los conjuntos de elementos de los arreglos a y b son iguales
(es equivalente a la matriz b que se puede encontrar como una 
matriz a con algunos reordenamientos de sus elementos) y sumatoria 
de MEX desde 1 hasta n en los prefijos de b es máxima.

MEX de un conjunto de enteros no negativos es el mínimo entero 
no negativo tal que no está en el conjunto.

por ejemplo, MEX({1, 2, 3}) = 0, MEX({0, 1, 2, 4, 5}) = 3 
'''

# funcion que calcula el MEX
def mex(arr):
    # se ordena el arreglo
    arr.sort()
    print("Arreglo ordenado:", arr)
    # si el primer elemento del arreglo es diferente de 0 entonces el MEX es 0
    if arr[0] != 0:
        print("El MEX es 0")
        return 0
    # si el primer elemento del arreglo es 0 entonces se recorre el arreglo
    else:
        # se recorre el arreglo desde el segundo elemento hasta el ultimo
        for i in range(len(arr) - 1):
            # imprime el elemento actual y el siguiente elemento del arreglo para ver si son iguales
            print("Comparando", arr[i], "con", arr[i + 1])
            # si el elemento actual es diferente del siguiente elemento entonces el MEX es el siguiente elemento
            # se suma 1 al elemento actual para ver si es igual al siguiente elemento del arreglo y asi sucesivamente
            # hasta que el elemento actual sea igual al siguiente elemento del arreglo y asi se obtiene el MEX del arreglo
            if arr[i + 1] - arr[i] > 1:
                # se imprime el MEX del arreglo
                print("El MEX es", arr[i] + 1)
                return arr[i] + 1
        # si el MEX no se encuentra en el arreglo entonces el MEX es el ultimo elemento del arreglo + 1
        print("El MEX es", arr[-1] + 1)
        # se retorna el MEX del arreglo + 1 porque el MEX es el siguiente elemento del ultimo elemento del arreglo
        return arr[-1] + 1
    
def main():
    # arr convierte la cadena de caracteres en una lista de enteros separados por espacios
    # split separa la cadena de caracteres en una lista de cadenas de caracteres
    arr = list(map(int, input("Ingrese los elementos del arreglo: ").split()))
    print("MEX:", mex(arr))

main()
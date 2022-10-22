# **********************   MODULOS   ***************************
# -----------  Leer Datos  -------------
def LeerLista():
    # -- Leer el numero de elementos de la Lista
    N = int(input("Numero de elementos de la Lista: "))
    # -- Inicializar lista vacia
    L = []
    # -- Leer los elementos
    for K in range(0, N):
        # -- Leer el K-esimo elemento de la Lista
        print("Ingresar el elemento ",K,":",end="")
        Elemento = float(input())
        L = L + [Elemento]

    # -- Retornar el arreglo
    return N, L

# -----------  Escribir Datos
def EscribirLista(N, L):
    # -- Escribir los elementos de la Lista
    for K in range(0, N):
        # -- Escribir el K-esimo elemento de la Lista
        print(L[K])

    
# *****************   PROGRAMA PRINCIPAL   *******************
# -- Leer Lista
N, L = LeerLista()
# -- Mostrar Datos
print()
print("Los elementos de la Lista son")
EscribirLista(N, L)

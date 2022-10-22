# **********************   MÓDULOS   ***************************

# -----------  Agregar elemento a la lista  -------------
def Agregar(Lista, Elemento):
    return Lista + [Elemento]

# -----------  Insertar elemento a la lista  -------------
def Insertar(Lista, K, Elemento):
    if (K <= len(Lista)):
        Lista = Lista[0:K] + [Elemento] + Lista[K:]
    return Lista

# -----------  Insertar elemento a la lista  -------------
def Eliminar(Lista, K):
    if (0 < K <= len(Lista)):
        return Lista[0:K]+ Lista[K+1:len(Lista)]
    else:
        return Lista

# -----------  Leer Lista  -------------
def LeerLista():
    # -- Leer el número de elementos de la Lista
    N = int(input("Número de elementos de la Lista: "))
    # -- Inicializar una lista vacía
    Lista = []
    # -- Leer los elementos de la lista
    for K in range(0, N):
        # -- Leer el K-ésimo elemento de la lista
        print("Ingresar el elemento ",K+1,":",end="")
        Elemento = input()
        Lista = Agregar(Lista, Elemento)

    # -- Retornar la lista
    return Lista

# -----------  Escribir Lista  -------------
def EscribirLista(Lista):
    print()
    # -- Escribir los elementos de la lista
    for Elemento in Lista:
        # -- Escribir el K-ésimo elemento de la lista
        print(Elemento)

    
# *****************   PROGRAMA PRINCIPAL   *******************
# -- Leer la lista
Lista = LeerLista()
# -- Mostrar la lista
print("Los elementos de la lista son:")
EscribirLista(Lista)
# -- Insertar un elemento
Lista = Insertar(Lista, 2, "Javier")
EscribirLista(Lista)
# -- Eliminar un elemento
Lista = Eliminar(Lista, 4)
EscribirLista(Lista)
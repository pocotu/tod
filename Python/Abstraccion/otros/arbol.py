def Mostrar(espacios, asteriscos):
    # Mostrar espacios y asteriscos
    print(' '*espacios+'*'*asteriscos)

def CopaArbol(espacios, asteriscos):
    if asteriscos > 0:
        # Suma 1 al espacio y resta 1 al asterisco en cada llamada
        CopaArbol(espacios+1, asteriscos-1)
        # 
        #Mostrar(espacios, 2*asteriscos-1)

def Tronco(espacios, n):
    if n > 0:
        Tronco(espacios, n-1)
        Mostrar(espacios, 3)

def Base(n):
    if n > 0:
        Mostrar(0, n)

CopaArbol(0, 5)
Tronco(3, 3)
Base(10)

# crear una libreria para una calculadora

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    return a/b

def potencia(a,b):
    return a**b

#raiz 
def raiz(a,b):
    return a**(1/b)
#raiz tipo con recursividad
def raiz2(a,b):
    
    if b == 1:
        return a
    else:
        return a * raiz2(a,b-1)


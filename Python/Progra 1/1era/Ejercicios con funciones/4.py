'''
Un entero positivo n es pitagórico si existen 
enteros positivos a y b tales que a2+b2 = n. Por 
ejemplo, 13 es pitagórico, pues 22+32 = 13
Implementar una función que reciba como 
parámetro tres enteros a,b y n, y devuelva True
caso a2+b2 = n y False, caso contrario.
La siguiente función debe ser implementada:
def prueba(a,b,n):
'''

def prueba(a, b, n):
    # si a^2 + b^2 es igual a n, entonces es pitagórico
    if a**2 + b**2 == n:
        return True
    else:
        return False

def main():
    # pide al usuario que ingrese los valores de a, b y n
    a = int(input("Ingrese el valor de a: "))
    b = int(input("Ingrese el valor de b: "))
    n = int(input("Ingrese el valor de n: "))
    
    # imprime el resultado de la función
    print(prueba(a, b, n))

main()
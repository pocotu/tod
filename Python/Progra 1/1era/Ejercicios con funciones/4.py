'''
Un entero positivo n es pitagórico si existen enteros positivos 
a y b tales que a2+b2 = n. Por ejemplo, 13 es pitagórico, 
pues 22+32 = 13. Implementar una función que reciba como parámetro 
tres enteros a,b y n, y devuelva True caso a2+b2 = n y False, caso contrario.
La siguiente función debe ser implementada:
def prueba(a,b,n):
'''

def pitagorico(a,b,n):
    if a**2 + b**2 == n:
        return True
    else:
        return False

def main():
    a = int(input("Ingrese el valor de a: "))
    while a <= 0:
        print("El valor de a debe ser positivo")
        a = int(input("Ingrese el valor de a: "))
    b = int(input("Ingrese el valor de b: "))
    while b <= 0:
        print("El valor de b debe ser positivo")
        b = int(input("Ingrese el valor de b: "))
    n = int(input("Ingrese el valor de n: "))
    while n <= 0:
        print("El valor de n debe ser positivo")
        n = int(input("Ingrese el valor de n: "))
    
    if pitagorico(a,b,n):
        print("Es pitagorico")
    else:
        print("No es pitagorico")
    print(pitagorico(a, b, n))

main()
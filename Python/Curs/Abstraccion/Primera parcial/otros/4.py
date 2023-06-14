'''
Implemente un algoritmo, usando una función recursiva, que resuelva la siguiente
sumatoria:
K(n, p) = p + 2 ∗ p + 3 ∗ p + 4 ∗ p + … + n ∗ p
● El programa debe pedir al usuario que ingrese un número n, y un número d,
● Luego debe calcular el valor de K(n, p) usando una función recursiva,
● Debe imprimir el resultado de K(n, p)

Algunos ejemplos de diálogo de este programa serían:
input n: 5
input p: 2
ouput: 30
'''
n = int(input("Ingrese n: "))
p = int(input("Ingrese p: "))
def recursivo(n,p):
    if n == 0:
        return 0
    else:
        return p + 2 * p + 3 * p + 4 * p + recursivo(n-1,p)
print(recursivo(n,p))
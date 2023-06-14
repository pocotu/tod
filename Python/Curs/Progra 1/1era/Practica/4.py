'''
Escribir una funcion recursiva que calcule el maximo comun divisor (MCD)
de dos enteros positivos. si M >= N una funcion recursiva para MCD es.
MCD = M si N = 0
MCD = MCD (N, M mod N) si N <> 0
'''

# primera forma
def mcd(m, n):
    if n == 0:
        return m
    else:
        return mcd(n, m % n)
    
# segunda forma
def mcd2(m, n):
    if n == 0:
        return m
    else:
        return mcd2(n, m - n)
    
def main():
    print(mcd(124, 12))
    print(mcd2(124, 12))

main()
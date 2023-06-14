'''
maximo comun divisor de dos numeros con recursividad
'''
def mcd2(a,b):
    if b==0:
        return a
    else:
        return mcd2(b,a%b)
def mcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
print(mcd(12,18))
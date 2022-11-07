'''
escribir una funcion que permita  calcular la potencia de un
numero de forma recursiva, tanto para exponentes negativos como positivos
'''

def potencia(base, exp):
    if exp == 0:
        return 1
    elif exp > 0:
        return base * potencia(base, exp - 1)
    else:
        return 1 / potencia(base, -exp)
    
def potencia2(base, exp):
    res = 1
    for i in range(abs(exp)):
        res *= base
    if exp < 0:
        res = 1 / res
    return res

def main():
    base = int(input("ingrese la base: "))
    exp = int(input("ingrese el exponente: "))
    print("el resultado es: ", potencia(base, exp))
    print("el resultado es: ", potencia2(base, exp))

main()
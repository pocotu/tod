'''
Escriba una funcion recursiva que calcule la suma de los
elementos de un arreglo de numeros enteros
'''

# primera forma
def suma(arreglo):
    if len(arreglo) == 0:
        return 0
    else:
        return arreglo[0] + suma(arreglo[1:])
    
# segunda forma
def suma2(arreglo):
    if len(arreglo) == 0:
        return 0
    else:
        return arreglo[-1] + suma2(arreglo[:-1])

def main():
    arreglo = [1,2,3,4,5,6,7,8,9]
    print(suma(arreglo))
    print(suma2(arreglo))
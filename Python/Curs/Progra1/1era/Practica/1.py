'''
Escribir una funcion recursiva que invierta el orden de
de los numeros de un arreglo de enteros
'''

# primera forma
def invertir(arreglo):
    if len(arreglo) == 0:
        return []
    else:
        return invertir(arreglo[1:]) + [arreglo[0]]
    
# segunda forma
def invertir2(arreglo):
    if len(arreglo) == 0:
        return []
    else:
        return [arreglo[-1]] + invertir2(arreglo[:-1])
    
def main():
    arreglo = [1,2,3,4,5,6,7,8,9]
    print(invertir(arreglo))
    print(invertir2(arreglo))

main()
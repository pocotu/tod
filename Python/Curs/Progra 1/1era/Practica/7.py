'''
Escriba una funcion que ordene de menor a mayor un arreglo de enteros
basandose en la siguiente idea: coloque el elemento mas peque;o en la primera
ubicacion y luego ordene el resto del arreglo con una llamada recursiva
'''

# primera forma
def ordenar(arreglo):
    if len(arreglo) == 0:
        return []
    else:
        return [min(arreglo)] + ordenar(arreglo[1:])
    
# segunda forma
    
def main():
    arreglo = [3, 5, 2, 7 ,4]
    print(ordenar(arreglo))
    
main()
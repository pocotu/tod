'''
Hacer las torres de Hanoi
'''



def torres_de_hanoi(n, origen, auxiliar, destino):
    if n == 1:
        print('Mover disco 1 de la torre', origen, 'a la torre', destino)
    else:
        torres_de_hanoi(n-1, origen, destino, auxiliar)
        print('Mover disco', n, 'de la torre', origen, 'a la torre', destino)
        torres_de_hanoi(n-1, auxiliar, origen, destino)

print('Torres de Hanoi')
n = int(input("Ingrese el numero de discos: "))

torres_de_hanoi(n, 'A', 'B', 'C')
'''
Implementar un programa para imprimir:
1
1 2
1 2 3
……
1 2 3…. N
Para un n informado por el usuario. Use una 
función que reciba un valor n entero imprima 
hasta la n- ésima línea.
'''

def imprimir(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            # imprime todos los numeros de 1 a i en la misma linea
            print(j, end=" ")
        # imprime un salto de linea despues de terminar de imprimir todos los numeros de 1 a i
        print()

def main():
    n = int(input("Ingresa un numero: "))
    imprimir(n)

main()
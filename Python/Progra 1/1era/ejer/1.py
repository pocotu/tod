'''
Implementar un programa para imprimir:
1
1 2
1 2 3
......
1 2 3.... N
Para un n informado por el usuario. Use una
función que reciba un valor n entero imprima
hasta la n- ésima línea.
'''

def main():
    n = int(input("Ingrese un numero: "))
    while n < 0:
        print("El numero debe ser mayor a 0")
        n = int(input("Ingrese un numero: "))
    print("")
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print("")

main()

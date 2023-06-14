'''
crear una funcion recursiva que sume los numeros de 1 a n
'''

def suma(n):
    if n == 1:
        return 1
    else:
        return n + suma(n-1)

def main():
    n = int(input("ingrese un numero: "))
    print("la suma de los numeros de 1 a", n, "es:", suma(n))

main()
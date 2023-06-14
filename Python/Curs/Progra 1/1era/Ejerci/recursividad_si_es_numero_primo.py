'''
 Escribir una función recursiva que determine si un número entero n es primo.
'''

def verificar_primo(n, i):
    if i == 1:
        return True
    else:
        if n % i == 0:
            return False
        else:
            return verificar_primo(n, i-1)

def main():
    n = int(input("n: "))
    while n < 1:
        n = int(input("n: "))
    print(verificar_primo(n, n-1))

main()


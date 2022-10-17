"""
Mostrar los numeros pitagoricos menores que N.
Se dice que un numero es pitagorico si resulta de la suma de dos 
cuadrados de otros 2 numeros.
EJEMPLO: 5^2 + 12^2 = 13^2
"""

def pitagoricos(n):
    # recorre todos los numeros desde 1 hasta n
    for a in range(1, n + 1):
        # recorre todos los numeros desde 1 hasta n
        for b in range(1, n + 1):
            # recorre todos los numeros desde 1 hasta n
            for c in range(1, n + 1):
                # si a^2 + b^2 es igual a c^2
                if a**2 + b**2 == c**2:
                    print(a, b, c)

def main():
    n = int(input("Introduce un numero: "))
    pitagoricos(n)

main()
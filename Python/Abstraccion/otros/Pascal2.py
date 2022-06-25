# Haciendo el triangulo de Pascal con recursividad

def ValidarNumero(n):
    if 0 < n < 20:
        return crearTriangulo(n)
    else:
        return ValidarTexto(input("Ingrese un número entre 1 y 200: "))

def ValidarTexto(n):
    if n.isdigit():
        return ValidarNumero(int(n))
    else:
        return ValidarTexto(input("Ingrese un númerooo: "))

def factorial(num):
    if num > 0:
        # Haciendo el factorial de un numero con recursividad
        return int(num*factorial(num-1))
    else:
        return 1

def combinatoria(num1, num2):
    return int(factorial(num1) / (factorial(num2)*factorial(num1-num2)))

#def crearTriangulo(n):
#    # Creando el triangulo de Pascal con recursividad
#    if n == 1:
#        return 1
#    else:
#        return combinatoria(n, 1) + crearTriangulo(n-1)

def crearTriangulo(n_filas):
    for fila in range(n_filas):
        for j in range(n_filas-fila+1):
            print(" ", end="")
        if fila == 0:

            print("1 1")
        else:
            for j in range(fila+2):
                print(combinatoria(fila+1, j), end=" ")
            print()

n = input("Indica el número de filas que desee: ")
ValidarTexto(n)
#ValidarTexto(input("Ingrese un texto: "))




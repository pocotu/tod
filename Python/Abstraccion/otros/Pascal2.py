# Haciendo el triangulo de Pascal con recursividad

def ValidarNumero(num):
    if 0 < num < 20:
        return crearTriangulo(num)
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

num = input("Indica el número de filas que desee: ")
ValidarTexto(n)
#ValidarTexto(input("Ingrese un texto: "))




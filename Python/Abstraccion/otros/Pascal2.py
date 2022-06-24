# Haciendo el triangulo de Pascal con recursividad

def ValidarNumero(n):
    if 0 < n < 20:
        return crearTriangulo(n)
    else:
        return ValidarNumero(int(input("Ingrese un número entre 1 y 20: ")))

def ValidarTexto(texto):
    if n.isdigit() != True:
        n = input("Ingrese un número entero: ")
        return ValidarTexto(n)

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

n = int(input("Indica el número de filas que desee: "))
ValidarTexto(n)




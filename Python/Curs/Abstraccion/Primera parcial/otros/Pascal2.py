def ValidarTexto(num):
    # si el numero es un numero entero
    if num.isdigit():
        # retorna funcion de ValidarNumero con el numero ingresado 
        return ValidarNumero(int(num))
    else:
        # si no es un numero entero, retorna la funcion de ValidarTexto
        return ValidarTexto(input("Ingrese un número entre 1 y 200: "))

def ValidarNumero(num):
    if 0 < num < 20:
        return crearTriangulo(num)
    else:
        return ValidarTexto(input("Ingrese un número entre 1 y 2000: "))

def factorial(num):
    if num > 0:
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
            #print("1")
            print("1 1")

        else:
            for j in range(fila+2):
                print(combinatoria(fila+1, j), end=" ")
            print()

#def triangle(n):
#  if n==1:
#    return [1]
#  else:
#    x_linea=triangle(n-1)
#    pascal=[ x_linea[a]+x_linea[a+1] for a in range(len(x_linea)-1)] 
#    pascal.insert(0,1)
#       pascal.append(1)
#     return pascal 

ValidarTexto(input("Indica el número de filas que desee entre 1 y 20: "))



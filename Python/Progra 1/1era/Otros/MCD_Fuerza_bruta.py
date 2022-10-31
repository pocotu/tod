"""
Funcion que devuelve el maximo comun divisor de dos numeros,
Metodo: Hallar los divisores comunes y quedarse con el mayor
"""

def MCD_Fuerza_bruta(a, b):
    ###### 1era forma ######
    if a > b:
        menor = b
    else:
        menor = a
    # mientras no se cumpla la condicion, entonces menor no es divisor de a y b
    while not (a % menor == 0 and b % menor == 0):
        # si no es comun, se disminuye el divisor
        menor = menor - 1
    # se devuelve el divisor comun
    else:
        return menor
    
    ###### 2da forma ######
    # recorremos todos los numeros desde 1 hasta el menor
    #if a > b:
    #    menor = b
    #else:
    #    menor = a
    #for i in range(1, menor+1):
    #    # si a y b son divisibles por i, entonces i es el divisor comun
    #    if a % i == 0 and b % i == 0:
    #        mcd = i
    #return mcd

def main():
    a = int(input("Ingresa un numero: "))
    b = int(input("Ingresa otro numero: "))
    print("El maximo comun divisor es: ", MCD_Fuerza_bruta(a, b))

main()
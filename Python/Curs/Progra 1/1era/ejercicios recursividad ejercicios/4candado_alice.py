def abre_candado(n, combinacion):
    # Caso básico: si el candado tiene sólo un número, entonces Alice sólo necesita girarlo una vez
    if n == 1:
        return 1
    # Si el número inferior es igual a cero, entonces no necesitamos girar el número superior
    elif combinacion[-1] == 0:
        return abre_candado(n - 1, combinacion[:-1])
    # Si el número inferior no es cero, entonces necesitamos girar tanto el número inferior como el superior
    else:
        return abre_candado(n - 1, combinacion[:-1]) + 1

def main():
    # Leemos los datos
    n = int(input('Introduce el número de números del candado: '))
    print('Introduce la combinación del candado: ')
    print('Ejemplo: 1 2 3 4 5')
    combinacion = [int(x) for x in input('=>').split()]
    # Calculamos el número de veces que Alice debe girar el candado
    print(abre_candado(n, combinacion))

main()
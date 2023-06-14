'''
crear una funcion que verifique si una palabra es palindromo con recursividad
'''

def palindromo(cadena):
    # CASO BASE
    # si la cadena es de longitud 1 o 0 es palindromo
    if len(cadena) <= 1:
        return True
    # CASO RECURSIVO
    else:
        # compara el primer caracter con el ultimo
        if cadena[0] == cadena[-1]:
            # retorna el valor de la funcion palindromo con la cadena sin el primer y ultimo caracter
            return palindromo(cadena[1:-1])
        # si no es palindromo retorna False
        else:
            return False

# funcion recursiva palindromo con bucle while
def palindromo2(cadena):
    while len(cadena) > 1:
        if cadena[0] == cadena[-1]:
            return palindromo2(cadena[1:-1])
        else:
            return False
    return True


def main():
    cadena = input("Ingrese una cadena: ")
    if palindromo(cadena):
        print('primera funcion')
        print("Es palindromo")
    else:
        print('primera funcion')
        print("No es palindromo")

    if palindromo2(cadena):
        print('segunda funcion')
        print("Es palindromo")
    else:
        print('segunda funcion')
        print("No es palindromo")

main()

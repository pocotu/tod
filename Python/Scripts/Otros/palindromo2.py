# usando indexacion / usando for loop
def palindromo2(cadena):
    # asigna el valor de la longitud de la cadena
    longitud = len(cadena)
    # recorre la cadena
    for i in range(longitud):
        # compara el valor de la posicion i con la longitud menos 1 menos i
        if cadena[i] != cadena[longitud - 1 - i]:
            # si no son iguales, no es palindromo
            return print("No es palindromo")
    # si se llega a este punto, es palindromo
    return print("Es palindromo")

# ejecuta la funcion
cadena = input("Ingrese una cadena: ")
palindromo2(cadena)


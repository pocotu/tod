# mediante uso del bucle WHILE
def palindromo4(cadena):
    longitud = len(cadena)
    primero = 0
    ultimo = longitud - 1
    while primero < ultimo:
        # compara el valor de la posicion i con la longitud menos 1 menos i
        if cadena[primero] == cadena[ultimo]:
            # si son iguales, se suma 1 a los indices
            primero += 1
            print(primero)
            # se resta 1 a los indices
            ultimo -= 1
            print(ultimo)
        else:
            return print("No es palindromo")
    return print("Es palindromo")
# ejecuta la funcion
cadena = input("Ingrese una cadena: ")
palindromo4(cadena)
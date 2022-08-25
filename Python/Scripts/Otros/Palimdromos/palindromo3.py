# mediante uso de funciones incorporadas - reversa y union
def palindromo3(cadena):
    # invierte la cadena con la funcion REVERSED y los une con la funcion union JOIN
    temporal = ''.join(reversed(cadena))
    # compara la cadena con la invertida
    if cadena == temporal:
        print("Es palindromo")
    else:
        print("No es palindromo")

cadena = input("Ingrese una cadena: ")
palindromo3(cadena)

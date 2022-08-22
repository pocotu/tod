def palindromo(cadena):
    # invierte la cadena
    temporal = cadena[:-1]
    print(temporal)
    if cadena == temporal:
        print("Es palindromo")
    else:
        print("No es palindromo")

cadena = input("Ingrese una cadena: ")
palindromo(cadena)
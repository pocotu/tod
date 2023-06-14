"""
implementar tanto de forma recursiva como iterativa una funcion que
invierta una cadena de caracteres
"""

def invertir(cadena):
    if len(cadena) == 1:
        return cadena
    else:
        return cadena[-1] + invertir(cadena[:-1])
    
def invertir2(cadena):
    res = ""
    for i in range(len(cadena)):
        res = cadena[i] + res
    return res

def main():
    cadena = input("ingrese una cadena de caracteres: ")
    print("la cadena invertida es: ", invertir(cadena))
    print("la cadena invertida es: ", invertir2(cadena))

main()


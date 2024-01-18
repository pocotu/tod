"""
implementar tanto de forma recursiva como iterativa una funcion que
nos diga si es cadena de caracteres es simetrica (un palindromo).
"""

def es_simetrica(cadena):
    if len(cadena) == 1:
        return True
    elif len(cadena) == 2:
        return cadena[0] == cadena[1]
    else:
        return cadena[0] == cadena[-1] and es_simetrica(cadena[1:-1])
    
def es_simetrica2(cadena):
    res = True
    for i in range(len(cadena) // 2):
        res = res and cadena[i] == cadena[-i - 1]
    return res

def main():
    cadena = input("ingrese una cadena de caracteres: ")
    print("la cadena es simetrica: ", es_simetrica(cadena))
    print("la cadena es simetrica: ", es_simetrica2(cadena))

main()
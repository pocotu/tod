# Implementar una función recursiva que, dada una string s y un 
# carácter c, cuente el número de ocurrencias del carácter c en 
# el string s. Implementar una función principal que haga uso 
# de la función implementada.

#def contar_ocurrencias(s, c):
#    if len(s) == 0:
#        return 0
#    else:
#        if s[0] == c:
#            return 1 + contar_ocurrencias(s[1:], c)
#        else:
#            return contar_ocurrencias(s[1:], c)
#        
#def main():
#    s = input("Ingresa una cadena de caracteres: ")
#    c = input("Ingresa un caracter: ")
#    print("El caracter", c, "aparece", contar_ocurrencias(s, c), "veces en la cadena", s)
#
#main()

def count_char_occurrences(s: str, c: str) -> int:
    if not s:  # Si la cadena es vacia 
        return 0 
    if s[0] == c:  # Si el primer carácter de la cadena es igual al carácter que se busca
        return 1 + count_char_occurrences(s[1:], c)  # sumar 1 al resultado y llamar recursivamente a la función con la subcadena que va desde el segundo hasta el último carácter
    else:
        return count_char_occurrences(s[1:], c)  # llamar recursivamente a la función con la subcadena que va desde el segundo hasta el último carácter

def main():
    s = input("Ingrese una cadena: ")
    c = input("Ingrese un carácter: ")
    count = count_char_occurrences(s, c)
    print(f"La cadena '{s}' tiene {count} ocurrencias del carácter '{c}'.")

main()
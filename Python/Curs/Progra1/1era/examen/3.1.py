def contar_ocurrencias(s, c):
    # Si la cadena es vacia, regresa 0
    if len(s) == 0:
        return 0
    else:
        # Si el primer carácter de la cadena es igual al carácter que se busca
        if s[0] == c:
            # sumar 1 al resultado y llamar recursivamente a la función con 
            # la subcadena que va desde el segundo hasta el último carácter
            return 1 + contar_ocurrencias(s[1:], c)
        else:
            # llamar recursivamente a la función con la subcadena que va desde
            # el segundo hasta el último carácter
            return contar_ocurrencias(s[1:], c)
        
def main():
    s = input("Ingresa una cadena de caracteres: ")
    c = input("Ingresa un caracter: ")
    print("El caracter", c, "aparece", contar_ocurrencias(s, c), "veces en la cadena", s)

main()


# Implementar una función recursiva que, dada una string s y un 
# carácter c, cuente el número de ocurrencias del carácter c en 
# el string s. Implementar una función principal que haga uso 
# de la función implementada.

def contar_ocurrencias(s, c):
    if len(s) == 0:
        return 0
    else:
        if s[0] == c:
            return 1 + contar_ocurrencias(s[1:], c)
        else:
            return contar_ocurrencias(s[1:], c)
        
def main():
    s = input("Ingresa una cadena de caracteres: ")
    c = input("Ingresa un caracter: ")
    print("El caracter", c, "aparece", contar_ocurrencias(s, c), "veces en la cadena", s)

main()
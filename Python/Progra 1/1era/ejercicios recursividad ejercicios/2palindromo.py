def es_palindromo(s):
    # Si la cadena está vacía o tiene un solo carácter, entonces es un palíndromo
    if len(s) <= 1:
        return True

    # Si el primer y último carácter son iguales, entonces comparamos el resto de la cadena
    if s[0] == s[-1]:
        return es_palindromo(s[1:-1])
    else:
        # Si el primer y último carácter no son iguales, entonces la cadena no es un palíndromo
        return False

def main():
    # Leemos la cadena
    s = input('Introduce una cadena: ')
    # Comprobamos si es un palíndromo
    if es_palindromo(s):
        print('La cadena es un palíndromo')
    else:
        print('La cadena no es un palíndromo')

main()
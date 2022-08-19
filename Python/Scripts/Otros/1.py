s = input("Ingrese una cadena: ")

# funcion palindrome
def es_palindromo(s):
    # agrega el texto 
    return s == s[::-1]

#print(es_palindromo(s))

if s == es_palindromo(s):
    print("Es palindromo")
else:
    print("No es palindromo")
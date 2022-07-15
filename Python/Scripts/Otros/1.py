s = input("Ingrese una cadena: ")

def es_palindromo(s):
    return s == s[::-1]

print(es_palindromo(s))

if s == es_palindromo(s):
    print("Es palindromo")
else:
    print("No es palindromo")
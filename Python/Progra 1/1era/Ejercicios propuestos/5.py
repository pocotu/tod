'''
Implementar una función que determine si un número N es o no especial. Un 
número N es especial si cada dígito que está en N aparece tantas veces como su 
propia magnitud. Por ejemplo, si el dígito 3 aparece en un número entonces deberá 
aparecer en exactamente 3 posiciones distintas para que dicho número sea especial; 
si el 1 aparece, deberá aparecer sólo una vez; si el 2 aparece está dos veces, etc. Por 
ejemplo, los números 333, 3313, 4234132434 son números especiales.
'''

def numero_especial(n):
    print("primero", type(n))
    # Convertimos el numero a string para poder iterar sobre sus digitos
    n = str(n)
    print("segundo", type(n))
    # Iteramos sobre los digitos del numero
    for i in range(len(n)):
        print("for", type(n[i]))
        # Contamos la cantidad de veces que aparece el digito en el numero
        if n.count(n[i]) != int(n[i]):

            return "El numero no es especial"
    return "El numero es especial"


def main():
    n = int(input("Ingrese un numero: "))
    while n < 1:
        n = int(input("Ingrese un numero: "))
    print(numero_especial(n))

main()

# Calcular el MCD de N números

# Leer el número de números
N = int(input('Ingresa el número de números: '))
# Leer el primer número
A = int(input('Ingresa el número 1: '))
# Efectuar el proceso repetitivo para calcular el MCD
for K in range(2,N+1):
    # Leer el siguiente número
    B = int(input('Ingresa el número '+str(K)+': '))
    # Calcular el MCD 
    Resto = A % B
    while not (Resto == 0):
        A = B
        B = Resto
        Resto = A % B

    # El MCD almacenarlo nuevamente en A
    A = B    
# Mostrar el resultado final
print('El MCD es: ', A)


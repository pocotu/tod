# Calcular el MCD de 2 números

# Leer el primer número
A = int(input('Ingresa el número 1: '))
# Leer el siguiente número
B = int(input('Ingresa el número 2: '))
# Calcular el MCD 
Resto = A % B
while (Resto > 0):
    A = B
    B = Resto
    Resto = A % B

# Mostrar el resultado final
print('El MCD es: ', B)


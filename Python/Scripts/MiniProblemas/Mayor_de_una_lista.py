lista = []
n = int(input("Ingresa el tamaño de la lista: "))
print()
i=1

while(n>0):
    numero = float(input("Numero " + str(i) + ": "))
    lista.append(numero)
    i = i + 1
    n = n - 1

print('El mayor es:',numero)


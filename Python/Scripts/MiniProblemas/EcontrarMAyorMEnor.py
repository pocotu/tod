lista = []
n = int(input("Ingresa el tamaño de la lista: "))
print()
mayor = 0
menor = 0
i=1

while(n>0):
    numero = float(input("Numero " + str(i) + ": "))
    lista.append(numero)
    i = i + 1
    n = n - 1

print()
mayor = max(lista)
menor = min(lista)

print("Lista: ",lista)

print("El mayor es: ",mayor)
print("El menor es: ",menor)


lista = []
n = int(input("Ingresa el tamaño de la lista: "))
print()
i=0

while(n>0):
    numero = float(input("Elemento " + str(i) + ": "))
    lista.append(numero)
    i = i + 1
    n = n - 1

print()
print(lista)
eliminar = int(input("Que elemento desea eliminar? "))
print()
lista.pop(eliminar)
print("Eliminando el elemento",eliminar)
print("La nueva lista es: ",lista)
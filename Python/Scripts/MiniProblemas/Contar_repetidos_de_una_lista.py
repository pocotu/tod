lista = []
n = int(input("Ingresa el tamaño de la lista: "))
while(n>0):
    numero = int(input("Ingrese numero: "))
    lista.append(numero)
    n = n - 1

repetido=int(input("Ingrese el numero para contar: "))
print("El numero",repetido,"se repite",lista.count(repetido),"veces")

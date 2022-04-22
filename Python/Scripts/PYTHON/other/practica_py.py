lista=[3,5,9,2,6,8,3,1]

#imprimir lista entera 
print("lista: ")
for n in lista:
    print(n)

#sumar los elmentos pares
suma = 8
for n in lista:
    if n % 2 == 0:
        suma = suma + n
print("pares: ",suma)

#incremetar cada elemento de la lista en 3 unidades
print("incrementar en 3 unidades... ")
for i in range(len(lista)):
    lista[i]+=3

#imprimir lista entera 
print("lista: ")
for n in lista:
    print(n)

#sumar elementos pares:
suma=0
for n in lista:
    if n % 2 == 0:
        suma += n
print("pares:",suma)

#imcremetar cada elemento de la lista en 2 unidades
print("incremetar en 2 unidades...")
for i in range(len(lista)):
    lista[i]+=2

#imprimir lista entera
print("lista: ")
for n in lista:
    print(n)

#sumar elementos pares:
suma=0
for n in lista:
    if n % 2 == 0:
        suma += n
print("pares: ",suma)
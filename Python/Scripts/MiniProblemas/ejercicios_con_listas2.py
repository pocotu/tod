#imprimir lista entera
def imprimirLista(l):
    print("lista: ")
    for n in l:
        print(n)

#sumar elementos pares:
def sumarPares(l):
    suma = 0
    for n in l:
        if n % 2 == 0:
            suma += n
    return suma

#incrementar cada elemento de la lista en n unidades
def incrementarN(l,n):
    print("sumando",n,"a caca elemento de la lista...")
    for i in range(len(l)):
        l[i]+=n

lista=[3,5,9,2,6,8,3,1]
imprimirLista(lista)
print("pares: ",sumarPares(lista))

incrementarN(lista,3)
imprimirLista(lista)
print("pares: ",sumarPares(lista))

incrementarN(lista,2)
imprimirLista(lista)
print("pares ",sumarPares(lista))
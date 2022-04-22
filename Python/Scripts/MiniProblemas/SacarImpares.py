#### Varios formas de imprimir numeros impares #####

#### Tipo 1 ####
#mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#filtrado = []
#
#for num in mi_lista:
#    if num % 2 != 0:
#        filtrado.append(num)
#
#print(filtrado)      # Python 2: impresión de filtrado
## [1, 3, 5, 7, 9]

#### Tipo 2 ####
#filtrado = [x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if x % 2 != 0]
#print(filtrado)      # impresión de filtrado

#### Tipo 3 ####
#def NumerosImpares():
#    Impares = []
#    Lista = int(input("Ingrese un numero: "))
#    for i in range(0, Lista):
#        print("Ingrese el numero", i+1, ":", end="")
#        NuevaLista = int(input())
#        if NuevaLista % 2 != 0:
#            Impares.append(NuevaLista)
#    print(Impares)
#    #return Impares
#NumerosImpares()

#def NumerosImpares():
#    Impares = []
#    Lista = int(input("Ingrese la cantida de elementos: "))
#    for i in range(0, Lista):
#        print("Ingrese el numero", i, ": ", end = "")
#        NuevaLista = int(input())
#        if NuevaLista % 2 != 0:
#            Impares = Impares + [NuevaLista]
#    print("Impares:", Impares)
#    #return Impares
#NumerosImpares()

### Tipo 4 ####
def NumerosImpares():
    Lista = int(input("Ingrese la cantidad de números que desea generar: "))
    Lista = [x for x in range(1, Lista + 1)]
    Lista = [x for x in Lista if x % 2 != 0]
    return Lista

print("Impares son:", NumerosImpares())


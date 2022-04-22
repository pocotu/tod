def busquedaBinaria(vector,clave):
    izq=0
    der=len(vector)-1

    while der>=izq:
        centro=(izq+der)//2
        if clave <vector[centro]:
            der =centro-1
        elif clave == vector[centro]:
            return centro
        else:
            izq=centro+1
    return -izq-1

list=[2,4,7,10,11,45,50,59,60,66,69,70,79]

i=busquedaBinaria(list,2)
print(i)

j=busquedaBinaria(list,11)
print(j)

k=busquedaBinaria(list,12)
print(k)

l=busquedaBinaria(list,1)
print(l)

m=busquedaBinaria(list,3)
print(m)

n=busquedaBinaria(list,0)
print(n)
n=int(input("Ingrese el tamaño del primer vector: "))
v1=[]
m=int(input("Ingrese el tamaño del segundo vector: "))
v2=[]
print("Primer vector")
for i in range(n):
    i=int(input("Ingrese numero: "))
    v1.append(i)
print("Segundo vector")
for i in range(n):
    i=int(input("Ingrese numero: "))
    v2.append(i)
def pro_escalar(v1,v2):
    if len(v1)!=len(v2):
        return ("Operacion invalida")
    else:
        pe=0
        for i in range(len(v1)):
            pe+=v1[i]*v2[i]
    return pe
P=pro_escalar(v1,v2)
print("El producto escalar es: ",P)
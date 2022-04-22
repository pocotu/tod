v=[]
n=int(input("Ingrese el tamaño del vector: "))
for i in range(n):
    i=int(input("Ingrese numero: "))
    v.append(i)
m=int(input("Ingrese el escalar: "))

for i in range(len(v)):
    v[i]=v[i]*m

print("El producto de un escalar por el vector es:")
print(v)
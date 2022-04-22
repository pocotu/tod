vector=[]
n=int(input("Ingrese el tamaño del vector: "))

for i in range(n):
    i=int(input("Ingrese numero: "))
    vector.append(i)
x=0
for i in range(len(vector)):
    x=x+vector[i]
promedio=x/n
print("El promedio del vector es: ",promedio)
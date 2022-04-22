'''
Dados dos vectores de 8 posiciones: [a0, a1, ……a7] y 
[b0, b1, ……b7], ¿cuál de los siguientes 
pseudocódigos calcula Y = a0 + b0 + a1 + b1 +……a7 + b7 ?
'''
a = [1,2,3,4,5,6,7,8]
b = [1,2,3,4,5,6,7,8]

acc1 = 0
for i in range(0, 8):
    acc1 = acc1 + a[0] + b[i]
y = acc1
print("Suma 1: ",acc1)

# Bien
acc2 = 0
for i in range(0, 8):
    acc2 = acc2 + a[i] + b[i]
y = acc2
print("Suma 2: ",acc2)

acc3 = 0
for i in range(0, 8):
    acc3 = acc3 + a[i] * b[i]
y = acc3
print("Suma 3: ",acc3)


#for i in range(0, 8):
#    acc4 = acc4 + a[i] + b[i]
#y = acc4
#print("Suma 4: ",acc4)



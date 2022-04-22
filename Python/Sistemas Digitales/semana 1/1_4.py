"""
¿Cuál de los siguientes pseudocódigos calcula la suma de los cuadrados de los 
100 primeros números naturales (desde el 1 hasta el 100 ambos incluidos)?
"""

#for num in range(1,101):
#    total = total + num**2
#print(total)

# Bien
total1 = 0
for num in range(1,101):
    total1 = total1 + num**2
print("total 1: ",total1)

total2 = 1
for num in range(1,100):
    total2 = total2 + num**2
print("Total 2: ",total2)

total3 = 0
for num in range(1,101):
    total3 = num + num**2
print("Total 3: ",total3)




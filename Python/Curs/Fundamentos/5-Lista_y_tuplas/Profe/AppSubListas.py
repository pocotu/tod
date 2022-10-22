L = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

# -- Sub lista con tres parámetros (Inicio, final, incremento)
print()
print('Sub listas con tres paráetros')
L1 = L[3:7:1]
print(L1)
L2 = L[4:9:2]
print(L2)
# -- Sub lista sin el tercer parámetro (Asume 1)
print()
print('Sub listas sin tercer parámetro')
L3 = L[2:5]
print(L3)
# -- Sub lista sin el primer y tercer parámetro (Asume 0 para el primer y 1 para el tercero)
print()
print('Sub listas sin primer y tercer parámetro')
L4 = L[:6]
print(L4)
# -- Sub lista sin el segundo y tercer parámetro (Asume el último para el segundo 0 y 1 para el último)
print()
print('Sub listas sin segundo y tercer parámetro')
L5 = L[7:]
print(L5)

'''
En la competencia "Dos vueltas a Valle Sagrado de los Incas", 
se tiene registrado los tiempos de c/vueltas en HH:MM:SS, del ganador
de la competencia. Escribir un algoritmo que determine el tiempo menor
por vuelta realizado por el ganador de la competencia.
'''

# Hallar el menor tiempo en una competencia automovilistica

# Leer los tiempos de cada vuelta
# Leer el tiempo de la primera vuelta
print("Ingrese el tiempo de la primera vuelta")
HH1 = int(input('Ingresa la hora: '))
MM1 = int(input('Ingresa los minutos: '))
SS1 = int(input('Ingresa los segundos: '))

# Leer el tiempo de la segunda vuelta
print("Ingrese el tiempo de la segunda vuelta")
HH2 = int(input('Ingresa la hora: '))
MM2 = int(input('Ingresa los minutos: '))
SS2 = int(input('Ingresa los segundos: '))

# Calcular el tiempo en segundos de cada vuelta
T1 = HH1 * 3600 + MM1 * 60 + SS1
T2 = HH2 * 3600 + MM2 * 60 + SS2

# Determinar el tiempo menor e imprimir el resultado
if (T1 <= T2):
    print('El tiempo menor es: ',HH1,MM1,SS1)
else:
    print('El tiempo menor es:',HH2,MM2,SS2)
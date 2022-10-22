# Programa para intercambiar dos numeros en ascendente

# Leer numeros
Nro1 = float(input('Ingrese el primer numero: '))
Nro2 = float(input('Ingrese el segundo numero: '))

# Intermcabiar numeros
if Nro1 >= Nro2:
    # Intermcabiando numeros
    Temp = Nro1
    Nro1 = Nro2
    Nro2 = Temp

# Mostar los numeros ordenados
print('Nros ordenados son: ',Nro1,Nro2)
'''
Escribir un algoritmo que determine si un numero de
3 digitos es igual a la suma de los cubos de sus digitos
'''

Nro = int(input('Ingresa un numero de 3 digitos: '))

# Descomponer numero
C = Nro //100
D = (Nro%100)//10
U = Nro%10

# Calcular la suma
SumaDigitos = (c**3) + (D**3) + (D**3)

# Determinar si los cubos sin iguales o no
if Nro == SumaDigitos:
    Mensaje = 'Es igual a'
else:
    Mensaje = 'No es igual a'

# Escribir el mensaje de los digitos
print(Nro,Mensaje,SumaDigitos)
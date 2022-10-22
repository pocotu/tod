'''
Se tiene un numero formado por ceros y unos. Escribir un modulo recursivo
que determine si en dicho numero hay ceros o unos
Ejemplo:
Numero          Mensaje
1100110101      Hay mas unos
100001101000    Hay mas ceros
10101010        Iguales
'''

## nueval linea

# Leer datos
Numero = int(input('Ingrese numero: '))

# Modulo para contar unos
def Uno(Numero):
    if Numero == 0:
        return 0
    else:
        return Numero % 10 + Uno(Numero // 10)

# Cantidad de unos
Cant_unos = Uno(Numero)

# Cantidad de Ceros
Cant_ceros = len(str(Numero)) - Cant_unos

# Mostrar datos
if(Cant_unos > Cant_ceros):
    print("Hay mas unos")

elif(Cant_unos < Cant_ceros):
    print("Hay mas ceros")

elif(Cant_unos == Cant_ceros):
    print("Iguales")

'''
def Uno(Numero):
    if Numero == 0:
        return 0
    else:
        if Numero % 10 == 1:
            return 1 + Uno(Numero // 10)
        else:
            return Uno(Numero // 10)
'''
'''
def Unos(n):    
  if (n == 1):
    return 1    
  else:
    if (n%10 == 1):
      return 1 + Unos(n//10)
    else:
      return Unos(n//10)
    
#n = int(input('n:')) 
n = 111001101011101
unos = Unos(n)
ceros = len(str(n)) - unos
print(unos,ceros)


if(unos < ceros):
  print("unos < ceros")
if(unos > ceros):
  print("unos > ceros")
if(unos == ceros):
  print("unos = ceros")

'''
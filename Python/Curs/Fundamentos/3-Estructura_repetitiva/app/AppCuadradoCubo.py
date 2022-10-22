'''Escribir un algoritmo que muestre el Numero,cuadrado y cubo
de los N primeros numeros enteros positivos.'''
# -- Leer Nro. de Elementos
N = int(input('Ingresa N: '))
while (N< 0):
    N = int(input('ERROR.. Ingresa N > 0: '))
# -- Mostrar el Numero, Cuadrado y Cubo
print('Numero  Cuadrado  Cubo')
print('======================')
for Numero in range(1,N+1):
    # -- Calcular el Cuadrado y Cubo
    Cuadrado = Numero **2
    Cubo = Numero**3
    # -- Mostrar Resultado
    print(Numero,'     ',Cuadrado,'       ',Cubo)
    

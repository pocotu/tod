# Programa para calcular el perímetro  y área de un triángulo

# *********************  MÓDULOS   **************************

# Modulo para verificar si los lados corresponden o no a un triángulo
def EsTriangulo(Lado1, Lado2, Lado3):
    return ((Lado1 + Lado2) > Lado3) and ((Lado2 + Lado3) > Lado1) and ((Lado1 + Lado3) > Lado2)

# Módulo para calcular el perímetro de un triángulo
def Perimetro(Lado1, Lado2, Lado3):
    return Lado1 + Lado2 + Lado3

# Módulo para calcular el área de un triángulo
def Area(Lado1, Lado2, Lado3):
    S = (Lado1 + Lado2 + Lado3) / 2
    return (S * (S - Lado1) * (S - Lado2) * (S - Lado3))**0.5
# Módulo para leer un punto
def LeerPunto():
    #print(Texto)
    X = float(input('Ingrese el valor de la coordenada X: '))
    Y = float(input('Ingrese el valor de la coordenada Y: '))
    return X, Y

# Módulo para calcular la distancia entre dos puntos
def Distancia(X1, Y1, X2, Y2):
    return ((X2 - X1)**2 + (Y2 - Y1)**2)**0.5

# ***************  PROGRAMA PRINCIPAL   *********************

# Leer los vértices del triángulo
print('Ingresar las coordenadas del primer vertice')
X1, Y1 = LeerPunto()
print('Ingresar las coordenadas del segundo vertice')
X2, Y2 = LeerPunto()
print('Ingresar las coordenadas del tercer vertice')
X3, Y3 = LeerPunto()

# Calcular los lados del triángulo
Lado1 = Distancia(X1, Y1, X2, Y2)
Lado2 = Distancia(X2, Y2, X3, Y3)
Lado3 = Distancia(X3, Y3, X1, Y1)

# Verificar si los lados corresponden a un triángulo
if (EsTriangulo(Lado1, Lado2, Lado3)):
    # Calcular Perimetro
    Perimetro = Perimetro(Lado1, Lado2, Lado3)
    # Calcular Area
    Area = Area(Lado1, Lado2, Lado3)
    # Mostrar resultados
    print('Perimetro= ', Perimetro)
    print('Area= ', Area)
else:
    print('Los datos no corresponden a los vertices de un triangulo')

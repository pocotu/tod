# Programa para determinar si una figura es un cuadrado o un rectángulo

from Libreria import *

#*******************  MODULO PRINCIPAL   ********************
# Leer los puntos
X1,Y1 = LeerPunto('Ingresar primer punto')
X2,Y2 = LeerPunto('Ingresar segundo punto')
X3,Y3 = LeerPunto('Ingresar tercer punto')
X4,Y4 = LeerPunto('Ingresar cuarto punto')
# Calcular los lados
L12 = Distancia(X1, Y1, X2, Y2)
L13 = Distancia(X1, Y1, X3, Y3)
L14 = Distancia(X1, Y1, X4, Y4)
L34 = Distancia(X3, Y3, X4, Y4)
L24 = Distancia(X2, Y2, X4, Y4)
L23 = Distancia(X2, Y2, X3, Y3)

# Determinar si es cuadrado o rectángulo
if (L12 == L34) and (L13 == L24) and (L14 == L23):
    # -- Los puntos corresponden a los vértices de un cuadrado o rectángulo
    if (L12 == L13) or (L12 == L14) or (L13 == L14):
        Texto = 'Es cuadrado'
    else:
        Texto = 'Es rectángulo'
else:
    # -- Los puntos NO corresponden a los vértices de un cuadrado o rectángulo
    Texto = 'No es cuadrado ni rectángulo'
            
# Mostrar resultado
print(Texto)
    

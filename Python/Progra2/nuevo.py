# Definir dos funciones para calcular la suma del 1 a n numero
# una de ellas sumando una a una cada numero y la otra
# aplicando la formula de al suma aritmetica de gauss

def suma1(n):
    resultado = 0
    for i in range(1, n+1):
        resultado += i
    return resultado

def suma2(n):
    return (n*(n+1))/2

print(suma1(10))
print(suma2(10))


'''
Escribir un programa modular para calcular el n-ésimo término de la serie de Fibonacci.
'''
# Modulo para serie Fibonacci
def Fibonacci(numero):
    """ 
    devuelve el fibonacci más grande
    número menor que x y el más bajo
    número de fibonacci mayor que x
    """
    if numero < 0:
        return -1
    (anterior,nuevo, lub) = (0,1,0)
    while True:
        if nuevo < numero:
            lub = nuevo 
            (old,nuevo) = (new,ante+nuevo)
        else:
            return (lub, nuevo)
            
while True:
    numero = int(input("Your number: "))
    if numero <= 0:
        break
    (lub, sup) = Fibonacci(numero)
    print("Largest Fibonacci Number smaller than x: " + str(lub))
    print("Smallest Fibonacci Number larger than x: " + str(sup))
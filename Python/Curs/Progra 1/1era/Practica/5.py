'''
Escribir una funcion recursiva transforme un numero entero positivo
a notacion binaria
'''

# primera forma
def binario(n):
    if n == 0:
        return ''
    else:
        return binario(n // 2) + str(n % 2)
    
# segunda forma
def binario2(n):
    if n == 0:
        return ''
    else:
        return str(n % 2) + binario2(n // 2)
    
def main():
    print(binario(10))
    print(binario2(10))
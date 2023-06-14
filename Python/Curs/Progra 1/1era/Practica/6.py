'''
Escribir una funcion recursiva que transforme un numero binario a su notacion
en decimal
'''

# primera forma
def decimal(n):
    if n == 0:
        return 0
    else:
        return decimal(n // 10) + (n % 10) * 2
    
# segunda forma
def decimal2(n):
    if n == 0:
        return 0
    else:
        return (n % 10) * 2 + decimal2(n // 10)
    
def main():
    print(decimal(1010))
    print(decimal2(1010))
'''
Escriba una funcion recursiva qu tine un parametro  n de tipo entero
y que devuelva el n-simo numero de Fibonacci. los numeros de 
Fibonacci se definen de la siguiente manera:
F0 = 1
F1 = 1
F(i+2) = Fi + F(i+1)
'''

# primera forma
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
# segunda forma
def fibonacci2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci2(n-2) + fibonacci2(n-1)
    
def main():
    print(fibonacci(10))
    print(fibonacci2(10))
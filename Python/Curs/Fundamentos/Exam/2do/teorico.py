'''
def Modulo1(x):
    return x*x

def Modulo2(x):
    return Modulo1(x*x)

print(Modulo2(5))

def mayor(x,y):
    return x if x>y else y

print(mayor(mayor(20,15),mayor(27,18)))

def distacia1(x1,y1,x2,y2):
    d = ((x1-x2)**2+(y1-y2)**2)**0.5

import math
def distacia2(x1,y1,x2,y2):
    return math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

def distacia3(x1,y1,x2,y2):
    a = (x2-x1)
    b = (y2-y1)
    return (a*a+b*b)**(1/2)



print(distacia1(1, 7, 4, 3))
print(distacia2(1, 7, 4, 3))
print(distacia3(1, 7, 4, 3))
'''
def intercambiar(x,y):
    x = x + y
    y = x - y
    x = x - y
    return x, y

a = 25
b = 20
a,b = intercambiar(a, b)
print(a,b)


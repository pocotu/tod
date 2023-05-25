from turtle import *

speed(10)
color('yellow')
bgcolor('black')
i = 200 # numero de vueltas
while i>0:
    # left(i) hace que la tortuga gire a la izquierda
    left(i)
    # forward(i*3) hace que la tortuga avance
    forward(i*1)

    # imprimir en que numero de vuelta esta de cada vuelta
    print(i)
    i = i-1



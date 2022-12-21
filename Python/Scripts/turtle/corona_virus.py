from turtle import *

speed(10)
color('yellow')
bgcolor('black')
i = 100 # numero de vueltas
while i>0:
    left(i)
    forward(i*3)
    i = i-1

# mantiene la ventana abierta

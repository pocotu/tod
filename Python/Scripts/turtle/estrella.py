from turtle import *

# Crea una instancia de la clase Turtle y una ventana para dibujar
t = Turtle()
s = Screen()

# Establece la velocidad de la tortuga y el tamaño del lápiz
t.speed(10)
t.pensize(5)

# Mueve la tortuga a la posición de inicio
t.penup()
t.goto(-50, 0)
t.pendown()

# rellena la estrella de color negro
t.fillcolor('black')
t.begin_fill()

# Dibuja la estrella
for i in range(5):
    t.right(144)
    t.forward(100)
    t.left(72)
    t.forward(100)

t.end_fill()

# Mantiene la ventana abierta hasta que se cierre manualmente
done()


import turtle

t = turtle
t.speed(20)
t.bgcolor("black")
t.penup()
t.goto(-50, 60)
t.pendown()
t.color("green")
turtle.begin_fill()
turtle.goto(100, 100)
turtle.goto(100, -100)
#dibujar logo windows
turtle.goto(-50, -60)
turtle.goto(-50, 60)
turtle.end_fill()
turtle.color('black')
turtle.goto(15, 100)
# cortar en dos partes iguales
turtle.color('black')
turtle.width(10)
turtle.goto(15, -100)
turtle.penup()
turtle.goto(100, 0)
turtle.penup()
turtle.pendown()
turtle.goto(-100, 0)
t.done()
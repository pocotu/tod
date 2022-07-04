import turtle as t

# crear una ventana de turtle
t.bgcolor("black")
# velocida de la tortuga (fastest '0', slowest '1', normal '6')
t.speed("fastest")
# grosor de la linea
t.pensize(5)

# funcion para dibujar la curva
def curve():
    # dibujar la curva en 200 iteraciones (200*1 = 200)
    for i in range(200):
        # girar a la derecha 1 grado
        t.right(1)
        # avanzar 1 pixel
        t.fd(1)

def texts(text,x,y):
    t.up()
    t.goto(x,y)
    t.down()
    t.pencolor("white")
    t.write(text, font=('Roboto',150,'bold'))
    t.up()
    t.goto(-50,-50)
    t.down()

# dibujar la curva
def head():
    # color de la linea y puntero de la tortuga
    t.color('red','white')
    # rellenar el poligono (True/False)
    t.begin_fill()
    # angulo de giro de la curva (0-360)
    t.left(140)
    t.fd(120)
    curve()
    t.left(125)
    curve()
    t.fd(120)
    t.end_fill()
    t.hideturtle()

# texto en la ventana de turtle "Eres..." en la posicion (-420, 180)
texts("Eres...", -320, 150)
# incia la curva
head()
# texto en la ventana de turtle "un" en la posicion (-420,0)
texts("un", -420,0)
# texto en la ventana de turtle "Pdj0" en la posicion (-400,-250)
texts("Pdj0",-400,-250)
# texto en la ventana de turtle "❤" en la posicion (130,-430)
texts("❤",130,-430)
# esperar a que se presione una tecla
t.exitonclick()
# Nombre de la canción: Past lives
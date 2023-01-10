#import turtle
#import time
#
#def dibujar_marco(longitud, anchura):
#    # Mover el cursor sin dibujar
#    turtle.penup()
#    turtle.forward(longitud / 2)
#    turtle.right(90)
#    turtle.forward(anchura / 2)
#    turtle.left(90)
#
#    # Dibujar el marco
#    turtle.pendown()
#    turtle.forward(longitud)
#    turtle.right(90)
#    turtle.forward(anchura)
#    turtle.right(90)
#    turtle.forward(longitud)
#    turtle.right(90)
#    turtle.forward(anchura)
#
#def dibujar_marcas(longitud, anchura):
#    # Mover el cursor sin dibujar
#    turtle.penup()
#    turtle.backward(longitud / 2)
#    turtle.left(90)
#    turtle.backward(anchura / 2)
#    turtle.right(90)
#    turtle.pendown()
#
#    # Dibujar las marcas
#    for i in range(12):
#        turtle.penup()
#        turtle.forward(longitud / 2)
#        turtle.pendown()
#        turtle.forward(anchura / 20)
#        turtle.penup()
#        turtle.backward(longitud / 2)
#        turtle.right(30)
#
#def dibujar_manecillas(longitud, anchura):
#    # Mover el cursor sin dibujar
#    turtle.penup()
#    turtle.backward(longitud / 2)
#    turtle.left(90)
#    turtle.backward(anchura / 2)
#    turtle.right(90)
#
#    # Dibujar la manecilla de segundos
#    turtle.pendown()
#    turtle.pensize(longitud / 50)
#    turtle.pencolor("red")
#    turtle.backward(longitud * 0.4)
#    turtle.penup()
#
#    # Mover el cursor sin dibujar
#    turtle.left(90)
#    turtle.forward(longitud / 2)
#    turtle.left(90)
#
#    # Dibujar la manecilla de minutos
#    turtle.pendown()
#    turtle.pensize(longitud / 30)
#    turtle.pencolor("blue")
#    turtle.backward(longitud * 0.3)
#    turtle.penup()
#
#    # Mover el cursor sin dibujar
#    turtle.left(90)
#    turtle.forward(longitud / 2)
#    turtle.left(90)
#
#    # Dibujar la manecilla de horas
#    turtle.pendown()
#    turtle.pensize(longitud / 20)
#    turtle.pencolor("green")
#    turtle.backward(longitud * 0.2)
#    turtle.penup()
#
#def actualizar_reloj():
#    # Obtener la hora actual
#    hora_actual = time.strftime("%I:%M:%S")
#    hora, minuto, segundo = hora_actual.split(":")
#    hora = int(hora)
#    minuto = int(minuto)
#    segundo = int(segundo)
#
#    # Calcular el ángulo de la manecilla de segundos
#    segundos_en_grados = segundo * 6
#    segundos_en_radianes = segundos_en_grados * 3.14 / 180
#
#    # Calcular el ángulo de la manecilla de minutos
#    minutos_en_grados = minuto * 6
#    minutos_en_radianes = minutos_en_grados * 3.14 / 180
#
#    # Calcular el ángulo de la manecilla de horas
#    horas_en_grados = hora * 30
#    horas_en_radianes = horas_en_grados * 3.14 / 180
#
#    # Borrar el reloj anterior
#    turtle.clear()
#
#    # Dibujar el nuevo reloj
#    dibujar_marco(200, 300)
#    dibujar_marcas(200, 300)
#    dibujar_manecillas(200, 300)
#
#    # Mover la manecilla de segundos
#    turtle.penup()
#    turtle.goto(0, 0)
#    turtle.right(segundos_en_grados)
#    turtle.pendown()
#    turtle.forward(100)
#
#    # Mover la manecilla de minutos
#    turtle.penup()
#    turtle.goto(0, 0)
#    turtle.right(minutos_en_grados)
#    turtle.pendown()
#    turtle.forward(75)
#
#    # Mover la manecilla de horas
#    turtle.penup()
#    turtle.goto(0, 0)
#    turtle.right(horas_en_grados)
#    turtle.pendown()
#    turtle.forward(50)
#
#    # Actualizar el reloj cada segundo
#    turtle.ontimer(actualizar_reloj, 1000)
#
## Configurar la ventana y el cursor
#turtle.setup(800, 800)
#turtle.bgcolor("lightgray")
#turtle.shape("turtle")
#turtle.speed(0)
#
## Dibujar el reloj por primera vez
#actualizar_reloj()
#
## Mantener la ventana abierta
#turtle.mainloop()

import turtle
import time

def dibujar_marco(longitud, anchura):
    # Mover el cursor sin dibujar
    turtle.penup()
    turtle.forward(longitud / 2)
    turtle.right(90)
    turtle.forward(anchura / 2)
    turtle.left(90)

    # Dibujar el marco
    turtle.pendown()
    turtle.forward(longitud)
    turtle.right(90)
    turtle.forward(anchura)
    turtle.right(90)
    turtle.forward(longitud)
    turtle.right(90)
    turtle.forward(anchura)

def dibujar_marcas(longitud, anchura):
    # Mover el cursor sin dibujar
    turtle.penup()
    turtle.backward(longitud / 2)
    turtle.left(90)
    turtle.backward(anchura / 2)
    turtle.right(90)
    turtle.pendown()

    # Dibujar las marcas
    for i in range(12):
        turtle.penup()
        turtle.forward(longitud / 2)
        turtle.pendown()
        turtle.forward(anchura / 20)
        turtle.penup()
        turtle.backward(longitud / 2)
        turtle.right(30)

def dibujar_manecillas(longitud, anchura):
    # Mover el cursor sin dibujar
    turtle.penup()
    turtle.backward(longitud / 2)
    turtle.left(90)
    turtle.backward(anchura / 2)
    turtle.right(90)

    # Dibujar la manecilla de segundos
    turtle.pendown()
    turtle.pensize(longitud / 50)
    turtle.pencolor("red")
    turtle.backward(longitud * 0)
    # Mover el cursor sin dibujar
    turtle.penup()
    turtle.backward(longitud / 2)
    turtle.left(90)
    turtle.backward(anchura / 2)
    turtle.right(90)

    # Dibujar la manecilla de segundos
    turtle.pendown()
    turtle.pensize(longitud / 50)
    turtle.pencolor("red")
    turtle.backward(longitud * 0.4)
    turtle.penup()

    # Mover el cursor sin dibujar
    turtle.left(90)
    turtle.forward(longitud / 2)
    turtle.left(90)

    # Dibujar la manecilla de minutos
    turtle.pendown()
    turtle.pensize(longitud / 30)
    turtle.pencolor("blue")
    turtle.backward(longitud * 0.3)
    turtle.penup()

    # Mover el cursor sin dibujar
    turtle.left(90)
    turtle.forward(longitud / 2)
    turtle.left(90)

    # Dibujar la manecilla de horas
    turtle.pendown()
    turtle.pensize(longitud / 20)
    turtle.pencolor("green")
    turtle.backward(longitud * 0.2)
    turtle.penup()

def dibujar_reloj():
    # Dibujar el marco, las marcas y las manecillas del reloj
    dibujar_marco(200, 300)
    dibujar_marcas(200, 300)
    dibujar_manecillas(200, 300)

# Configurar la ventana y el cursor
turtle.setup(800, 800)
turtle.bgcolor("lightgray")
turtle.shape("turtle")
turtle.speed(0)

# Dibujar el reloj por primera vez
dibujar_reloj()

# Mantener la ventana abierta
turtle.mainloop()

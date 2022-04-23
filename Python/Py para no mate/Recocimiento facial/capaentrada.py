import cv2 as cv 
import os
# (activar la libreria siguiente si la camara graba en alta resolucion)
#import imutils

# crear una carpeta para guardar las imagenes
modelo = 'FotosRoss'
# ruta de la carpeta donde se encuentran las imagenes
ruta1 = (r'D:/Algo/Win/tod/Python/Py para no mate/Recocimiento facial/Data')
# concatenar la carpeta con el nombre del modelo para crear la carpeta
ruta_completa = ruta1 + '/' + modelo

# si no existe la carpeta, la crea dentro de la carpeta actual
if not os.path.exists(ruta_completa):
    os.mkdir(ruta_completa)

# abriendo la camara de video
camara = cv.VideoCapture(0)
# importando todos los ruidos
ruido = cv.CascadeClassifier(r'D:\Algo\Win\tod\Python\Py para no mate\Recocimiento facial\haarcascade_frontalface_default.xml')

# creando un contador para el nombre de las imagenes
id = 0
# si la camara esta abierta
while True:
    # leemos un frame
    respueta, captura = camara.read()
    # si arroja un valor False, termina el ciclo
    if respueta == False:break
    # bajar la resolucion de la imagen (activar la siguiente linea si la camara graba en alta resolucion)
    #captura = imutils.resize(captura, width=640)
    # convertimos la imagen a escala de grises
    grises = cv.cvtColor(captura, cv.COLOR_BGR2GRAY)
    # captura de puntos de la cara. Ahorra procesamiento
    id_captura = captura.copy()
    # detectamos los rostros, cantidad de rostros y cantidad de contornos
    caras = ruido.detectMultiScale(grises, 1.3, 5)
    # recorremos todos los rostros
    for (x, y, ancho, altura) in caras:
        # dibujamos un rectangulo en las coordenadas de la cara
        cv.rectangle(captura, (x,y), (x+ancho, y+altura), (0, 255, 0), 2)
        # sacar fracmetos de la cara
        rostro_capturado = id_captura[y:y+altura, x:x+ancho]
        # unificar tamano de la imagen y cambiar tamano del cuadro.
        rostro_capturado = cv.resize(rostro_capturado, (160, 160), interpolation=cv.INTER_CUBIC)
        # asignar un nombre a la imagen de "rostro_capturado"
        cv.imwrite(ruta_completa + '/imagen_{}.jpg'.format(id), rostro_capturado)
        # incrementar el contador de ID
        id += 1
    # mostrar la imagen
    cv.imshow('Resultado de rostro', captura)
    # detener la ejecucion del programa cuando toma 350 imagenes
    if id == 501:
        break
# cerrar la camara
camara.release()
# destruir todas las ventanas
cv.destroyAllWindows()

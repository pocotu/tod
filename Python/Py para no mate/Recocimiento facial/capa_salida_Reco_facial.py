import cv2 as cv
import os

# ruta de la carpeta donde se encuentran las imagenes
data_ruta = ('D:/Algo/Win/tod/Python/Py para no mate/Recocimiento facial/Data')
# listar todos los archivos de la carpeta
lista_data = os.listdir(data_ruta)
# 
entrenamientoEigenFAceRecognizer = cv.face.EigenFaceRecognizer_create()
# importando el entrenamiento de la base de datos
entrenamientoEigenFAceRecognizer.read(r'D:\Algo\Entrenamientos\entrenamientoEigenFAceRecognizer.xml')
# importando ruidos
ruidos = cv.CascadeClassifier(r'D:\Algo\Win\tod\Python\Py para no mate\Recocimiento facial\haarcascade_frontalface_default.xml')
# iniciando la camara
camara = cv.VideoCapture(0)

while True:
    # capturando el video frame por frame
    _, captura = camara.read()
    # convertir la imagen a grises
    grises = cv.cvtColor(captura, cv.COLOR_BGR2GRAY)
    # 
    id_captura = grises.copy()
    # detectar los rostros
    cara = ruidos.detectMultiScale(grises, 1.3, 5)

    for (x, y, ancho, altura) in cara:

        # sacar fracmetos de la cara
        rostro_capturado = id_captura[y:y+altura, x:x+ancho]
        # unificar tamano de la imagen y cambiar tamano del cuadro.
        rostro_capturado = cv.resize(rostro_capturado, (160, 160), interpolation=cv.INTER_CUBIC)
        # comparando la cara capturada con la base de datos
        resultado = entrenamientoEigenFAceRecognizer.predict(rostro_capturado)
        # colocando numeros en la imagen
        cv.putText(captura, '{}'.format(resultado), (x, y-5), 1, 1.3, (0, 255, 0), 1, cv.LINE_AA)
        # 
        if resultado[1] < 10000:
            # colocando el nombre de la persona
            cv.putText(captura, 'No encontrado', (x, y-20), 2, 1.1, (0, 255, 0), 1, cv.LINE_AA)
            # dibujando el cuadro
            cv.rectangle(captura, (x, y), (x+ancho, y+altura), (0, 255, 0), 2)
        else:
            # dibujando el cuadro
            cv.putText(captura, '{}'.format(resultado[0]), (x, y-20), 2, 0.7, (0, 255, 0), 1, cv.LINE_AA)
            cv.rectangle(captura, (x, y), (x+ancho, y+altura), (255, 0, 0), 2)
    # mostrando la imagen capturada
    cv.imshow('Reconocimiento Facial', captura)
    # pulsar la tecla 's' para salir
    if cv.waitKey(1) == ord('s'):
        break
# finalizamos la camara y cerramos la ventana
camara.release()
cv.destroyAllWindows()
        
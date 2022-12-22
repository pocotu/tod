import cv2
# capturar mano
from cvzone.HandTrackingModule import HandDetector


# Inicializar la primera camara dsiponible
captura = cv2.VideoCapture(0)
# Definir el ancho y alto de la camara
camara_ancho, camara_alto = 640, 480
# Definir el ancho y alto de la ventana
captura.set(3, camara_ancho)
captura.set(4, camara_alto)

# Inicializar el detector de manos con un umbral de confianza de 0.65
# y un maximo de 1 mano
detectar = HandDetector(detectionCon=0.65, maxHands=1)

while True:
    # Leer la imagen de la camara y guardarla en la variable frame
    # La variable ret es un booleano que indica si se ha leido la imagen correctamente
    ret, frame = captura.read()
    # Invertir la imagen horizontalmente para que sea como un espejo
    frame = cv2.flip(frame, 1)
    # Detectar la 
    mano, frame = detectar.findHands(frame)
    if mano:
        # Obtener la lista de puntos de la mano detectada y el indice del dedo pulgar
        Puntos_dedos = mano[0]['lmList']
        # Obtener la posicion del dedo pulgar y dibujar un circulo en esa posicion en el frame
        ind_x, ind_y = Puntos_dedos[8][0], Puntos_dedos[8][1]
        # El color del circulo es amarillo y el grosor es 2 de tamaño 5 pixeles
        cv2.circle(frame, (ind_x, ind_y), 5, (0, 255, 255), 2)


    # Mostrar la imagen en una ventana
    cv2.imshow("Camara", frame)
    cv2.waitKey(1)

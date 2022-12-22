import cv2
# capturar mano
from cvzone.HandTrackingModule import HandDetector
import mouse
import numpy as np
import pyautogui 


# Inicializar la primera camara dsiponible
captura = cv2.VideoCapture(0)
# Definir el ancho y alto de la camara
camara_ancho, camara_alto = 640, 480
# Definir el ancho y alto de la ventana
captura.set(3, camara_ancho)
captura.set(4, camara_alto)


framer = 100

# Inicializar el detector de manos con un umbral de confianza de 0.65
# y un maximo de 1 mano
detectar = HandDetector(detectionCon=0.65, maxHands=1)

while True:
    # Leer la imagen de la camara y guardarla en la variable frame
    # La variable ret es un booleano que indica si se ha leido la imagen correctamente
    ret, frame = captura.read()
    # Invertir la imagen horizontalmente para que sea como un espejo
    frame = cv2.flip(frame, 1)
    # Detectar la mano en el frame
    mano, frame = detectar.findHands(frame)
    cv2.rectangle(frame, (framer, framer), (camara_ancho - framer, camara_alto - framer), (255, 0, 255), 2)

    if mano:
        # Obtener la lista de puntos de la mano detectada y el indice del dedo pulgar
        Puntos_dedos = mano[0]['lmList']

        # Obtener la posicion del dedo pulgar y dibujar un circulo en esa posicion en el frame
        ind_x, ind_y = Puntos_dedos[8][0], Puntos_dedos[8][1]
        # El color del circulo es amarillo y el grosor es 2 de tamaño 5 pixeles
        cv2.circle(frame, (ind_x, ind_y), 5, (0, 255, 255), 2)
        #La función np.interp() es una función de interpolación lineal que se utiliza para calcular un valor 
        #intermedio entre dos puntos en una línea. En este caso, se está utilizando np.interp() para mapear un 
        #valor en el rango (framer, camara_ancho-framer) al rango (0, 1920) y otro valor en el rango 
        #(framer, camara_alto-framer) al rango (0, 1080).

        #Los valores ind_x e ind_y son los valores de entrada que se utilizarán para calcular los valores interpolados. 
        #Los valores framer, camara_ancho y camara_alto son los límites del rango de entrada y salida.

        #Los resultados de la interpolación se convierten a enteros mediante la función int() 
        #antes de ser asignados a las variables conv_x y conv_y.
        conv_x = int(np.interp(ind_x, (framer, camara_ancho-framer), (0, 1920)))
        conv_y = int(np.interp(ind_y, (framer, camara_alto-framer), (0, 1080)))
        # Mover el cursor del raton a la posicion convertida
        mouse.move(conv_x, conv_y)

        dedos = detectar.fingersUp(mano[0])
        # Si el dedo indice y el pulgar estan levantados hacer click izquierdo
        if dedos[0] and 1:
            # Hacer click izquierdo si el dedo pulgar y el indice estan levantados
            pyautogui.mouseDown(button='left')

        else:
            # Soltar el click izquierdo si el dedo pulgar y el indice estan bajados
            pyautogui.mouseUp(button='left')

    # Mostrar la imagen en una ventana
    cv2.imshow("Camara", frame)
    cv2.waitKey(1)


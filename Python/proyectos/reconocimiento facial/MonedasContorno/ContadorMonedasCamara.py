from cv2 import cv2
import numpy as np

# uvicar puntos de las monedas
def OrdenarPuntos(puntos):
    # Concatenando puntos y convertiendo a lista
    n_puntos = np.concatenate([puntos[0], puntos[1], puntos[2], puntos[3]]).tolist()
    # Ordenando puntos
    y_orden = sorted(n_puntos, key = lambda n_puntos:n_puntos[1])
    x1_orden = y_orden[:2]
    x1_orden = sorted(x1_orden, key = lambda x1_order:x1_order[0])
    x2_orden = y_orden[2:4]
    x2_orden = sorted(x2_orden, key = lambda x2_order:x2_order[0])
    return [x1_orden[0], x1_orden[1], x2_orden[0], x2_orden[1]]

# Alinear el contorno de la moneda con el contorno de la camara
def Alineamiento(imagen, ancho, alto):
    # imagen_alineada = np.zeros((alto, ancho, 3), np.uint8)
    imagen_alineada = None
    grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    _ , umbral = cv2.threshold(grises, 150, 255, cv2.THRESH_BINARY)
    cv2.imshow("Umbral", umbral)
    contorno = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    contorno = sorted(contorno, key = cv2.contourArea, reverse = True)[:1]

    for c in contorno:
        # para que las curvas no tengan mucho ruido
        epsilon = 0.01 * cv2.arcLength(c, True)
        aproximacion = cv2.approxPolyDP(c, epsilon, True)
        if len(aproximacion) == 4:
            puntos = OrdenarPuntos(aproximacion)
            puntos1 = np.float32(puntos)
            puntos2 = np.float32([[0,0], [ancho,0], [0,alto], [ancho,alto]])
            # No cambiar de lugares los puntos
            M = cv2.getPerspectiveTransform(puntos1, puntos2)
            imagen_alineada = cv2.warpPerspective(imagen, M, (ancho, alto))
    return imagen_alineada
capturavideo = cv2.VideoCapture(0)

while True:
    tipocamara, camara = capturavideo.read()
    if tipocamara == False:
        break
    imagen_A6 = Alineamiento(camara, ancho = 480, alto = 640)
    if imagen_A6 is not None:
        puntos = []
        imagen_gris = cv2.cvtColor(imagen_A6, cv2.COLOR_BGR2GRAY)
        # Desenfoque en la imagen
        blur = cv2.GaussianBlur(imagen_gris, (5, 5), 1)
        # Umbralizar la imagen
        _, umbral2 = cv2.threshold(blur, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)
        # Encontrar los contornos
        cv2.imshow('Umbral', umbral2)
        contorno2 = cv2.findContours(umbral2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        cv2.drawContours(imagen_A6, contorno2, -1, (255, 0, 0), 2)
        # Encontrar los contornos mas grandes
        suma1 = 0.0
        suma2 = 0.0
        
        # momentos de los contornos
        for c_2 in contorno2:
            area = cv2.contourArea(c_2)
            momentos = cv2.moments(c_2)
            # Encontrar el centroide
            if (momentos["m00"] == 0):
                # Si el momento es 0, no se puede dividir
                momentos["m00"] = 1.0
            x = int(momentos["m10"]/momentos["m00"])
            y = int(momentos["m01"]/momentos["m00"])
            # Encontrar monedas de  0.20 centimos
            if area < 9300 and area > 8000:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(imagen_A6, 'S/ 0.20', (x, y), font, 0.75, (0, 255, 0), 2)
                suma1 = suma1 + 0.2
            # Encontrar monedas de  0.10 centimos
            if area < 7800 and area > 6500:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(imagen_A6, 'S/ 0.10', (x, y), font, 0.75, (0, 255, 0), 2)
                suma2 = suma2 + 0.1
        # Suma de las monedas
        total = suma1 + suma2
        print("sumatoria total en centimos:", round(total, 2))
        # Mostrar la suma de las monedas
        cv2.imshow("Imagen A6", imagen_A6)
        cv2.imshow("Camara", camara)
    if cv2.waitKey(1) == ord('s'):
        break
# Detener la captura de video
capturavideo.release()
cv2.destroyAllWindows()


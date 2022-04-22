from cv2 import cv2
import numpy as np

### Convetir imagen a escala de grises
valorGauss = 3
valorKernel = 3

original = cv2.imread(r"./MonedasContorno/monedas.jpg")
gris = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

#eliminar ruido de imagen
#gauss = cv2.GaussianBlur(gris, (valorGauss,valorKernel), 0)
gauss = cv2.GaussianBlur(gris, (valorGauss,valorGauss), 0)

#Encuentra los bordes
canny = cv2.Canny(gauss, 60, 100)

#Escogiendo contorno de afuera
kernel = np.ones((valorKernel,valorKernel), np.uint8)

cierre = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)

contornos, jerarquia = cv2.findContours(cierre.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print('Monedas encontradas: {}'.format(len(contornos)))
cv2.drawContours(original, contornos, -1, (0,0,255), 2)

#Mostrar resultados
cv2.imshow('Grises', gris)
cv2.imshow('Gauss', gauss)
cv2.imshow('Canny', canny)
cv2.imshow('Cierre', cierre)
cv2.imshow('Resultado', original)
cv2.waitKey(0)

#Imprimir resultados como archivos
#cv2.imwrite('D:\Algo\Win\AllProy\Python\Py para no mate\MonedasContorno\monedas_grises.jpg', gris)
#cv2.imwrite('D:\Algo\Win\AllProy\Python\Py para no mate\MonedasContorno\monedas_gauss.jpg', gauss)
#cv2.imwrite('D:\Algo\Win\AllProy\Python\Py para no mate\MonedasContorno\monedas_canny.jpg', canny)
#cv2.imwrite('D:\Algo\Win\AllProy\Python\Py para no mate\MonedasContorno\monedas_cierre.jpg', cierre)
#cv2.imwrite('D:\Algo\Win\AllProy\Python\Py para no mate\MonedasContorno\monedas_resultado.jpg', original)

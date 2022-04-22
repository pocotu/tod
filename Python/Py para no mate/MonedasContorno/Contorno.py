from cv2 import cv2, findContours

#Leer imagen con su ruta

# Direccion de imagen para windows
#imagen = cv2.imread('D:\Algo\Win\AllProy\Python\Py para no mate\MonedasContorno\contorno.jpg') 

# Direccion de imagen para Ubuntu
imagen = cv2.imread('/media/kli/tod/Algo/Ubun/AllProy/Python/Py para no mate/MonedasContorno/contorno.jpg')
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY) #cambiando colores a escala de grises
_,umbral = cv2.threshold(grises,100,255,cv2.THRESH_BINARY) #Subguion ignora la primera salida de la funcion
contorno, jerarquia = cv2.findContours(umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) #Fuscando contorno en modo simple

#Dibujando contornos
# '-1 : todos los contornos', '1 : primer contorno', '2 : segundo contorno', etc
cv2.drawContours(imagen, contorno, -1, (251, 63, 52), 3) 

# Mostrar
cv2.imshow('Imagen original', imagen) #Mostrar imagen original
#cv2.imshow('Imagen en grises', grises) #Mostrar imagen en grises
#cv2.imshow('Imagen umbral', umbral)
cv2.waitKey(0) #Tiempo de espera de ventana, '1' videos, '0' imagenes
cv2.destroyAllWindows() #Cerrar ventanas abiertas

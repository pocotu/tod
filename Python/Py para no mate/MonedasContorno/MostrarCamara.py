import cv2 as cv 
CapturaVideo = cv.VideoCapture(0)

while True:
    TipoCamara, Camara = CapturaVideo.read()
    if not TipoCamara:
        print('No se pudo leer frame')
        break
    Filtro = cv.cvtColor(Camara, cv.COLOR_BGR2GRAY)
    cv.imshow('Camara', Filtro)
    if cv.waitKey(1) == ord('q'):
        break


#if not CapturaVideo.isOpened():
#    print('No se encontro camara')
#    exit()
#
#while True:
#    TipoCamara, Camara = CapturaVideo.read()
#    #filtro de camara
#    #Filtro = cv.cvtColor(Camara, cv.COLOR_BGR2GRAY)
#    Filtro = cv.cvtColor(Camara, cv.COLOR_BGR2HSV)
#    cv.imshow('En vivo', Filtro)
#    if cv.waitKey(1)== ord('q'):
#        break
#
#CapturaVideo.release()
#cv.destroyAllWindows()


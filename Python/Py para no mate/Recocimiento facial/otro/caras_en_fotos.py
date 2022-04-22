import face_recognition
import cv2 as cv2

# importando imagen para reconocer las caras
path = 'D:\Algo\Win\AllProy\Python\Py para no mate\Recocimiento facial\otro\caras.jpg'
# leer la imagen
img = cv2.imread(path)
# 
face_loc = face_recognition.face_locations(img)
print(face_loc)

for i in face_loc:
    cv2.rectangle(img, (i[3], i[0]), (i[1], i[2]), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
import cv2 as cv2
import face_recognition
import numpy
# Get image from a folder
path = "D:\Algo\Win\AllProy\Python\Py para no mate\Recocimiento facial\caras.jpg"
image = cv2.imread(path)
wight = int(image.shape[1] * 0.35)
height = int(image.shape[0] * 0.35)
image = cv2.resize(image, (wight, height))
# Create a temporary blank image.
blank = numpy.zeros((100, 100, 3))
# Draw rectangle on faces on image
face_location = face_recognition.face_locations(image)
for i in face_location:
    draw_rectangle = cv2.rectangle(image, (i[3], i[0]), (i[1], i[2]), (0, 255, 0), 2)
cv2.imshow("blank", draw_rectangle)
# Cut the faces from image
for i in face_location:
    blank = image[i[0]:i[2], i[3]:i[1]]
    cv2.imshow(f"face{i}", blank)
    cv2.imwrite(f"face{i}.jpg", blank)
cv2.waitKey(0)

#cv2.destroyAllWindows()
# Get the face encodings for the known faces
#known_face_encodings = face_recognition.face_encodings(blank)

import os
import cv2
import face_recognition
# Get the photos and folder
faces_img_folder = "faces image"
test_img = cv2.imread("test img/Together2.jpeg")
# get face images from face_image folder
face_images = []
face_name = []

mylist = os.listdir(faces_img_folder)
for name in mylist:
    curImg = cv2.imread(f"faces image/{name}")
    face_images.append(curImg)
    face_name.append(os.path.splitext(name)[0])
# get the incode of faces images
face_encode = []
for img in face_images:
    encode = face_recognition.face_encodings(img)[0]
    face_encode.append(encode)
print("We have found ",len(face_encode), " face in your "+ faces_img_folder + " folder")
# get encode and face location of test img
test_face_loc = face_recognition.face_locations(test_img)
test_face_encode = face_recognition.face_encodings(test_img)
# draw rectangle on face of test_image
for loc in test_face_loc:
    cv2.rectangle(test_img, (loc[3], loc[0]), (loc[1], loc[2]), (0, 255, 0), 2)
# lets compare face and get the result
for encode , loc in zip(test_face_encode, test_face_loc):
    matches = face_recognition.compare_faces(face_encode, encode, 0.5)
    print(matches)
    if True in matches:
        index = matches.index(True)
        cv2.putText(test_img, f"{face_name[index]}", (loc[3], loc[0]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.imshow("After proccess", test_img)
cv2.waitKey(0)


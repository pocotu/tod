import cv2 as cv 
# para rutas de carpetas
import os
import numpy as np 
from time import time 


# ruta de la carpeta donde se encuentran las imagenes
data_ruta = (r'D:\Algo\Win\tod\Python\Py para no mate\Recocimiento facial\Data')
# listar todos los archivos de la carpeta
lista_data = os.listdir(data_ruta)
# imprimir la lista de carpetas
print('Datos', lista_data)
# agregar etiquetas a las imagenes
ids = []
# recorrer la lista de imagenes
rostros_data = []
id = 0
tiempo_inicial = time()

for fila in lista_data:
    ruta_completa = data_ruta + '/' + fila
    print('inciando proceso de lectura de imagenes')
    for archivo in os.listdir(ruta_completa):
 
        print('leyendo imagen', fila + '/' + archivo)
        # agregar etiquetas a 'ids'
        ids.append(id)
        # concatenar la ruta completa con el nombre del archivo
        rostros_data.append(cv.imread(ruta_completa + '/' + archivo, 0))
        # leer la imagen y convertirla a escala de grises
        #imagenes = cv.imread(ruta_completa + '/' + archivo, 0)
        # tiempo de lectura de imagenes

    # aumentar el id
    id = id + 1
    tiempo_final_lectura = time()
    tiempo_total_lectura = tiempo_final_lectura - tiempo_inicial
    print('tiempo total de lectura de imagenes', tiempo_total_lectura)
# primer entrenamiento con el metodo eigenfaces
entrenamientoEigenFaceRecognizer = cv.face.EigenFaceRecognizer_create()
print('iniciando el entrenamiento...espere')
# entrenar el modelo
entrenamientoEigenFaceRecognizer.train(rostros_data, np.array(ids))
tiempo_final_entrenamiento = time()
tiempo_total_entrenamiento = tiempo_final_entrenamiento - tiempo_final_lectura
print('tiempo entrenamiento total:', tiempo_total_entrenamiento)
# guardar el modelo entrenado
entrenamientoEigenFaceRecognizer.write('D:\Algo\Entrenamientos\entrenamientoEigenFaceRecognizer.xml')
print('entrenamiento finalizado')


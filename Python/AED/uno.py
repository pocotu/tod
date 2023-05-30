import numpy as np

class ImageMatrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def apply_filter(self, filter_matrix):

        try:
            filtered_matrix = np.multiply(self.matrix, filter_matrix)
            return filtered_matrix
        except Exception as e:
            print("Error al aplicar el filtro:", str(e))

    def get_dimensions(self):
        try:
            rows, cols = self.matrix.shape
            return rows, cols
        except Exception as e:
            print("Error al obtener las dimensiones:", str(e))

class ImageEnhancer:
    def __init__(self, image_matrix):
        self.image_matrix = image_matrix

    def enhance_quality(self):
        try:
            filter_matrix = np.array([[0.5, 0.5, 0.5], [0.5, 1, 0.5], [0.5, 0.5, 0.5]])
            enhanced_matrix = self.image_matrix.apply_filter(filter_matrix)
            return enhanced_matrix
        except Exception as e:
            print("Error al mejorar la calidad de la imagen:", str(e))

# Ejemplo de uso
try:
    # Crear una matriz de imagen de ejemplo
    image_data = np.array([[100, 120, 150], [200, 180, 210], [50, 80, 100]])
    image_matrix = ImageMatrix(image_data)

    # Mejorar la calidad de la imagen
    enhancer = ImageEnhancer(image_matrix)
    enhanced_image = enhancer.enhance_quality()

    # Obtener las dimensiones de la imagen mejorada
    rows, cols = image_matrix.get_dimensions()

    # Imprimir la imagen original y sus dimensiones
    rows, cols = image_matrix.get_dimensions()
    print("Imagen original:")
    print(image_data)
    print("Dimensiones:", rows, "x", cols)

    # Imprimir la imagen mejorada y sus dimensiones
    print("Imagen mejorada:")
    print(enhanced_image)
    print("Dimensiones:", rows, "x", cols)
except Exception as e:
    print("Error:",str(e))

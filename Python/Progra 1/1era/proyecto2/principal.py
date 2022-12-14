'''
El proyecto consiste en implementar un conjunto de funciones en el archivo secuencias.py que 
permitan resolver problemas relacionados con el secuenciamiento genético. El secuenciamiento 
genético se refiere a la identificación del orden en que aparecen los nucleótidos en una molécula 
de ADN. Esta información es importante ya que secuencias más largas de nucleótidos codifican 
proteínas en el cuerpo. Las funciones implementadas en secuencias
se utilizarán para resolver problemas específicos en los programas ruido y diferencias.

Entrada 
 
La primera línea contiene el tamaño de una ventana, la segunda línea la secuencia del genoma 
de referencia y la tercera, el genoma de la variante. 
 
4 
AAAATTTTGGGGCCCC 
AGGATTATGGGGAAAC 
 
Salida 
Para cada gen de la variante cuya distancia de Hamming al gen correspondiente de referencia 
sea al menos un tercio del tamaño de la ventana, se deberá enumerar la diferencia. Si hay 
varios genes diferentes, entonces los genes deben ser listados en orden de posición en que aparecen. Diferencia 1: 
   Posición: 0 
Referencia: AAAA 
  Variante: AGGA 
 Distancia: 2 
 
Diferencia 2: 
   Posición: 12 
Referencia: CCCC 
  Variante: AAAC 
 Distancia: 3 
'''

# Importamos la función distancia_hamming del archivo secuencias.py
from secuencias import distancia_hamming

# Función para identificar los genes con la mayor diferencia entre la secuencia de una nueva variante de una bacteria y la secuencia del genoma de referencia
def identificar_diferencias(secuencia_variante, secuencia_referencia, ventana):
    """
    Función para identificar los genes con la mayor diferencia entre la secuencia de
    una nueva variante de una bacteria y la secuencia del genoma de referencia.

    Parámetros:
    - secuencia_variante (str): la secuencia de la nueva variante
    - secuencia_referencia (str): la secuencia del genoma de referencia
    - ventana (int): el tamaño de la ventana para dividir las secuencias en genes

    Devuelve:
    - una lista con los genes que tienen la mayor diferencia entre las dos secuencias
    """

    # Inicializamos una lista para almacenar los genes con la mayor diferencia
    genes_mayor_diferencia = []

    # Inicializamos una variable para almacenar la mayor diferencia hasta el momento
    mayor_diferencia = 0

    # Recorremos las secuencias por genes
    for i in range(0, len(secuencia_variante), ventana):

        # Obtenemos el gen de la secuencia de la variante
        gen_variante = secuencia_variante[i:i + ventana]

        # Obtenemos el gen de la secuencia de referencia
        gen_referencia = secuencia_referencia[i:i + ventana]

        # Calculamos la distancia de Hamming entre los dos genes
        distancia_hamming = distancia_hamming(gen_variante, gen_referencia)

        # Si la distancia de Hamming es mayor que la mayor diferencia hasta el momento
        if distancia_hamming > mayor_diferencia:

            # Actualizamos la mayor diferencia hasta el momento
            mayor_diferencia = distancia_hamming

            # Vaciamos la lista de genes con la mayor diferencia
            genes_mayor_diferencia = []

            # Añadimos el gen con la mayor diferencia a la lista
            genes_mayor_diferencia.append(gen_variante)

        # Si la distancia de Hamming es igual que la mayor diferencia hasta el momento
        elif distancia_hamming == mayor_diferencia:

            # Añadimos el gen con la mayor diferencia a la lista
            genes_mayor_diferencia.append(gen_variante)

    # Devolvemos la lista de genes con la mayor diferencia
    return genes_mayor_diferencia
'''
RUIDO
El ruido es un concepto fundamental estudiado en el procesamiento de señales, en el análisis de datos 
y en varias otras áreas de la computación y afines. En estas disciplinas, la información se transmite en 
forma de una señal y el ruido se refiere a modificaciones o adiciones no deseadas en los datos de la señal con 
la que deseamos trabajar. Por ejemplo, en la comunicación por radio, la interferencia electromagnética puede 
superponerse a la señal real. En datos de sensores, como el de temperatura, los problemas físicos pueden 
provocar lecturas incorrectas en medio de una secuencia de lecturas correctas. 
En procesos que dependen de seres humanos, como análisis de laboratorio, puede haber entrada de datos inválidos.

La distancia de Hamming 
Una técnica básica para lidiar con ciertos tipos de ruido es calcular la distancia de Hamming. Dadas 
dos secuencias del mismo tamaño x e y, la distancia de Hamming entre x e y , 
 denotada por d(x,y), es el número de posiciones donde las secuencias son diferentes. Por ejemplo, para
secuencias de bits x=0100 y=1101, la distancia de Hamming es d(x,y) =2 , porque estas secuencias tienen 
diferentes bits en las posiciones 0 y 3. Una manera de utilizar esta medida para hacer frente al ruido se describe 
a continuación. Consideramos válidas para nuestra aplicación solo algunas secuencias acordadas previamente. En caso de que recibamos 
una secuencia desconocida durante el proceso de transmisión de datos, sustituya esa secuencia por la secuencia 
pre-acordada más parecida. Para decidir qué secuencia es más parecida, elegimos aquella con la menor distancia de Hamming. 
Por ejemplo, dos amigos músicos deciden conversar por secuencias melódicas. Así, una nota corta representa 
un bit 0 y una nota larga representa un bit 1. Como no es posible identificar la duración de notas individualmente, 
combinan que una secuencia significa 111 significa sim y una secuencia 000 significa no. Si uno de ellos escucha una 
secuencia de notas correspondiente a 010, concluirá que en realidad la secuencia debería ser 000 
e interpretará la respuesta como no. La razón es que d(010, 000)=1, sin embargo d(010,111)=2 
'''

def distancia_hamming(secuencia1, secuencia2):
    """
    Función para calcular la distancia de Hamming entre dos secuencias de ADN.

    Parámetros:
    - secuencia1 (str): la primera secuencia de ADN
    - secuencia2 (str): la segunda secuencia de ADN

    Devuelve:
    - la distancia de Hamming entre las dos secuencias
    """
    # Inicializar la distancia de Hamming en 0
    distancia = 0
    # Recorrer las posiciones de las secuencias
    for i in range(len(secuencia1)):
        # Si los caracteres en la misma posición son diferentes
        if secuencia1[i] != secuencia2[i]:
            # Incrementar la distancia de Hamming en 1
            distancia += 1
    # Devolver la distancia de Hamming
    return distancia



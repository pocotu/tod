from ruido import *
from diferencias import *

def sustituir(secuencia, secuencia_referencia, ventana):
    # Inicializamos una lista para almacenar los genes con la mayor diferencia
    genes_mayor_diferencia = []
    # Inicializamos una variable para almacenar la mayor diferencia hasta el momento
    mayor_diferencia = 0

    # Recorremos las secuencias por genes
    for i in range(0, len(secuencia), ventana):
        # Obtenemos el gen de la secuencia de la variante
        gen_variante = secuencia[i:i + ventana]
        # Obtenemos el gen de la secuencia de referencia
        gen_referencia = secuencia_referencia[i:i + ventana]
        # Calculamos la distancia de Hamming entre los dos genes
        distancia_hamming = distancia_hamming(gen_variante, gen_referencia)
        # Si la distancia de Hamming es mayor o igual a la mitad del tamaño de la ventana
        if distancia_hamming >= ventana // 3:
            # Si la distancia de Hamming es mayor que la mayor diferencia hasta el momento
            if distancia_hamming > mayor_diferencia:
                # Actualizamos la mayor diferencia
                mayor_diferencia = distancia_hamming
                # Vaciamos la lista de genes con la mayor diferencia
                genes_mayor_diferencia = []
            # Si la distancia de Hamming es igual a la mayor diferencia hasta el momento
            if distancia_hamming == mayor_diferencia:
                # Añadimos el gen a la lista de genes con la mayor diferencia
                genes_mayor_diferencia.append((i, gen_referencia, gen_variante, distancia_hamming))

    # Devolvemos la lista de genes con la mayor diferencia
    return genes_mayor_diferencia

def main():
    # Leemos el tamaño de la ventana
    ventana = int(input('Tamaño de la ventana: '))
    # Leemos la secuencia de referencia
    secuencia_referencia = input('Secuencia de referencia: ')
    # Leemos la secuencia de la variante
    secuencia_variante = input('Secuencia de la variante: ')
    # Obtenemos las diferencias entre las secuencias
    diferencias = identificar_diferencias(secuencia_variante, secuencia_referencia, ventana)
    # Mostramos las diferencias
    for i, diferencia in enumerate(diferencias):
        # Convertimos el índice en entero para poder sumarle 1 y obtener la posición
        diferencia['posicion'] = int(diferencia['posicion']) + 1
        # Mostramos la diferencia actual en pantalla con un formato legible para el usuario final (1-based)
        print(f"Diferencia {i + 1}:")
        print(f"Posición: {diferencia['posicion']}")
        print(f"Referencia: {diferencia['referencia']}")
        print(f"Variante: {diferencia['variante']}")
        print(f"Distancia: {diferencia['distancia']}")
        print()
        
main()


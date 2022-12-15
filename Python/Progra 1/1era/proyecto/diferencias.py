from ruido import *

def identificar_diferencias(secuencia_variante, secuencia_referencia, ventana):
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
        hamming = distancia_hamming(gen_variante, gen_referencia)
    
        # Si la distancia de Hamming es mayor que la mayor diferencia hasta el momento
        if hamming > mayor_diferencia:
            # Actualizamos la mayor diferencia hasta el momento
            mayor_diferencia = hamming
            # Vaciamos la lista de genes con la mayor diferencia
            genes_mayor_diferencia = []
            # Añadimos el gen con la mayor diferencia a la lista
            genes_mayor_diferencia.append({
                'posicion': i,
                'referencia': gen_referencia,
                'variante': gen_variante,
                'distancia': hamming
            })
        # Si la distancia de Hamming es igual que la mayor diferencia hasta el momento
        elif hamming == mayor_diferencia:
            # Añadimos el gen con la mayor diferencia a la lista
            genes_mayor_diferencia.append({
                'posicion': i,
                'referencia': gen_referencia,
                'variante': gen_variante,
                'distancia': hamming
            })
    
    # Devolvemos la lista de genes con la mayor diferencia
    return genes_mayor_diferencia




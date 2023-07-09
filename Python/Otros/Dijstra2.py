def Dijkstra(grafo, start):
    # Inicializar las distancias a todos los nodos como 
    # infinito, excepto el nodo de inicio
    distancia = {nodo: float('inf') for nodo in grafo}
    distancia[start] = 0
    
    # Lista de nodos no visitados
    no_visitado = set(grafo.keys())
    
    # Almacenar el camino más corto para cada nodo
    camino = {nodo: [] for nodo in grafo}
    
    while no_visitado:
        # Obtener el nodo no visitado con la distancia mínima
        nodo_actual = min(no_visitado, key=lambda nodo: distancia[nodo])
        no_visitado.remove(nodo_actual)
        
        # Ignorar nodos con distancia infinita (inaccesibles)
        if distancia[nodo_actual] == float('inf'):
            break
        
        # Explorar los vecinos del nodo actual
        for vecino, peso in grafo[nodo_actual].items():
            distance = distancia[nodo_actual] + peso
            
            # Actualizar la distancia si encontramos un camino más corto
            if distance < distancia[vecino]:
                distancia[vecino] = distance
                # Actualizar el camino más corto para el nodo vecino
                camino[vecino] = camino[nodo_actual] + [vecino]
    
    return distancia, camino

# Diccionario de grafos
grafo = {
    'a': {'b': 4, 'c': 2},
    'b': {'a': 4, 'c': 1, 'd': 5},
    'c': {'a': 2, 'b': 1, 'd': 8},
    'd': {'b': 5, 'c': 8, 'e': 2},
    'e': {'c': 10, 'd': 2, 'f': 2},
    'f': {'e': 2, 'd': 6},
}

iniciar_nodo = 'a'
distancia, camino = Dijkstra(grafo, iniciar_nodo)

print(f"Distancias minimas desde el nodo '{iniciar_nodo}':")
for nodo, distance in distancia.items():
    print(f"Nodo: {nodo}, Distancia: {distance}")

print(f"\nMejor camino encontrado desde el nodo '{iniciar_nodo}':")
for nodo, path in camino.items():
    print(f"Nodo: {nodo}, Camino: {['->'.join(path)] if path else ['N/A']}")


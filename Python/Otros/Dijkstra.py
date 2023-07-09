import networkx as nx
import matplotlib.pyplot as plt

def Dijkstra(grafo, inicio):
    # Inicializar las distancias a todos los nodos como 
    # infinito, excepto el nodo de inicio

    # Diccionario de distancias
    distancia = {nodo: float('inf') for nodo in grafo}
    # El nodo de inicio tiene una distancia de 0
    distancia[inicio] = 0
    
    # Lista de nodos no visitados
    no_visitado = set(grafo.keys())
    
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
    return distancia

grafo = {
    'a': {'b': 4, 'c': 2},
    'b': {'a': 4, 'c': 1, 'd': 5},
    'c': {'a': 2, 'b': 1, 'd': 8},
    'd': {'b': 5, 'c': 8, 'e': 2},
    'e': {'c': 10, 'd': 2, 'f': 2},
    'f': {'e': 2, 'd': 6},
}

# Iniciar el algoritmo de Dijkstra
iniciar_nodo = 'a'
# Obtener las distancias minimas desde el nodo de inicio
distancia = Dijkstra(grafo, iniciar_nodo)

print(f"Distancias minimas desde el nodo '{iniciar_nodo}':")
for nodo, distance in distancia.items():
    print(f"Nodo: {nodo}, Distancia: {distance}")

####################################################################
# Crear un objeto de grafo de networkx
G = nx.Graph()

# Agregar los nodos y las aristas al grafo
for nodo, vecino in grafo.items():
    G.add_node(nodo)
    for vecino, weight in vecino.items():
        G.add_edge(nodo, vecino, peso=weight)

# Posiciones de los nodos en el gráfico
pos = nx.spring_layout(G)

# Dibujar los nodos y las aristas del grafo
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)

# Etiquetar las aristas con los pesos
edge_labels = nx.get_edge_attributes(G, 'peso')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Mostrar el gráfico
plt.axis('off')
plt.show()

####################################################################
# Diccionario de grafos
#grafo = {
#    'A': {'B': 5, 'C': 2},
#    'B': {'A': 5, 'C': 1, 'D': 3},
#    'C': {'A': 2, 'B': 1, 'D': 2},
#    'D': {'B': 3, 'C': 2, 'E': 4},
#    'E': {'D': 4}
#}
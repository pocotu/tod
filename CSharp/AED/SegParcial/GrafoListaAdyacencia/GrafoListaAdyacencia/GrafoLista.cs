using System;
using System.Collections.Generic;

namespace Grafos
{
    // Clase que representa un grafo utilizando listas de adyacencia
    public class GrafoLista
    {
        // Atributos
        private int numVertices;
        private Dictionary<int, List<int>> listaAdyacencia;

        // Constructor
        public GrafoLista(int vertices)
        {
            numVertices = vertices;
            // Inicializar la lista de adyacencia
            listaAdyacencia = new Dictionary<int, List<int>>();
            for (int i = 0; i < numVertices; i++)
            {
                // Agregar una lista vacia para cada vertice
                listaAdyacencia.Add(i, new List<int>());
            }
        }

        // Agregar una arista al grafo
        public void AgregarArista(int origen, int destino)
        {
            listaAdyacencia[origen].Add(destino); // Si el grafo es no dirigido
            listaAdyacencia[destino].Add(origen); // Si el grafo es no dirigido
        }

        // Mostrar el grafo
        public void MostrarGrafo()
        {
            foreach (var vertice in listaAdyacencia)
            {
                // Mostrar los vecinos del vertice
                Console.Write($"Vertice {vertice.Key}: ");
                // Recorrer la lista de vecinos
                foreach (var vecino in vertice.Value)
                {   
                    // Mostrar el vecino
                    Console.Write($"{vecino} ");
                }
                Console.WriteLine();
            }
        }
    }

}


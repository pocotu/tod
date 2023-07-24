using System;

namespace Grafos
{
    // Clase que representa un grafo utilizando matriz de adyacencia
    public class GrafoMatriz
    {
        private int numVertices;
        private int[,] matrizAdyacencia; // donde [,] = [fila, columna]

        // Constructor
        public GrafoMatriz(int vertices)
        {
            numVertices = vertices;
            matrizAdyacencia = new int[numVertices, numVertices];
        }

        // Agregar una arista al grafo
        public void AgregarArista(int origen, int destino)
        {
            matrizAdyacencia[origen, destino] = 1; // Si el grafo es no dirigido
            matrizAdyacencia[destino, origen] = 1; // Si el grafo es no dirigido
        }

        // Mostrar el grafo
        public void MostrarGrafo()
        {
            // Recorrer la matriz de adyacencia
            for (int i = 0; i < numVertices; i++)
            {
                // Mostrar los vecinos del vertice i
                Console.Write($"Vertice {i}: ");
                // Recorrer la fila i
                for (int j = 0; j < numVertices; j++)
                {
                    // Si hay una arista entre i y j
                    Console.Write($"{matrizAdyacencia[i, j]} ");
                }
                Console.WriteLine();
            }
        }
    }

}

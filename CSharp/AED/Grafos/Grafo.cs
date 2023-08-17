using System;
using System.Collections.Generic;

namespace AppGrafo
{
    public class Grafo
    {
        private int[,] matrizAdyacencia;
        private int numVertices;

        public Grafo(int numVertices)
        {
            this.numVertices = numVertices;
            matrizAdyacencia = new int[numVertices, numVertices];
        }

        public void CargarGrafo(int[,] grafo)
        {
            if (grafo.GetLength(0) == numVertices && grafo.GetLength(1) == numVertices)
            {
                matrizAdyacencia = grafo;
                MostrarGrafo();
            }
            else
            {
                Console.WriteLine("Dimensiones del grafo incorrectas.");
            }
        }

        public void AgregarArco(int verticeInicio, int verticeFin)
        {
            if (verticeInicio >= 1 && verticeInicio <= numVertices &&
                verticeFin >= 1 && verticeFin <= numVertices)
            {
                matrizAdyacencia[verticeInicio - 1, verticeFin - 1] = 1;
                MostrarGrafo();
            }
            else
            {
                Console.WriteLine("Vertices inválidos.");
            }
        }

        public void EliminarArco(int verticeInicio, int verticeFin)
        {
            if (verticeInicio >= 1 && verticeInicio <= numVertices &&
                verticeFin >= 1 && verticeFin <= numVertices)
            {
                matrizAdyacencia[verticeInicio - 1, verticeFin - 1] = 0;
                MostrarGrafo();
            }
            else
            {
                Console.WriteLine("Vertices invalidos.");
            }
        }

        public void MostrarGrafo()
        {
            Console.Clear();
            Console.WriteLine("Representacion Grafica del Grafo:");
            for (int i = 0; i < numVertices; i++)
            {
                Console.Write((i + 1) + " -> ");
                for (int j = 0; j < numVertices; j++)
                {
                    if (matrizAdyacencia[i, j] == 1)
                    {
                        Console.Write((j + 1) + " ");
                    }
                }
                Console.WriteLine();
            }
        }

        public void MostrarMatrizAdyacencia()
        {
            Console.WriteLine("Matriz de Adyacencia:");
            for (int i = 0; i < numVertices; i++)
            {
                for (int j = 0; j < numVertices; j++)
                {
                    Console.Write(matrizAdyacencia[i, j] + " ");
                }
                Console.WriteLine();
            }
        }

        public bool EsSimetrico()
        {
            for (int i = 0; i < numVertices; i++)
            {
                for (int j = 0; j < numVertices; j++)
                {
                    if (matrizAdyacencia[i, j] != matrizAdyacencia[j, i])
                    {
                        return false;
                    }
                }
            }
            return true;
        }

        public List<List<int>> EncontrarCaminos(int verticeInicio, int verticeFin)
        {
            List<List<int>> caminos = new List<List<int>>();
            EncontrarCaminosRecursivo(verticeInicio - 1, verticeFin - 1, new List<int>(), caminos);
            return caminos;
        }

        private void EncontrarCaminosRecursivo(int verticeActual, int verticeFin, List<int> caminoActual, List<List<int>> caminos)
        {
            caminoActual.Add(verticeActual + 1);

            if (verticeActual == verticeFin)
            {
                caminos.Add(new List<int>(caminoActual));
            }
            else
            {
                for (int i = 0; i < numVertices; i++)
                {
                    if (matrizAdyacencia[verticeActual, i] == 1 && !caminoActual.Contains(i + 1))
                    {
                        EncontrarCaminosRecursivo(i, verticeFin, caminoActual, caminos);
                    }
                }
            }

            caminoActual.RemoveAt(caminoActual.Count - 1);
        }

        public int CalcularLongitudCamino(List<int> camino)
        {
            return camino.Count;
        }

        public bool EsReflexivo()
        {
            for (int i = 0; i < numVertices; i++)
            {
                if (matrizAdyacencia[i, i] != 1)
                {
                    return false;
                }
            }
            return true;
        }

        public List<List<int>> EncontrarCiclos(int vertice)
        {
            List<List<int>> ciclos = new List<List<int>>();
            EncontrarCiclosRecursivo(vertice - 1, vertice - 1, new List<int>(), ciclos);
            return ciclos;
        }

        private void EncontrarCiclosRecursivo(int verticeActual, int verticeInicio, List<int> cicloActual, List<List<int>> ciclos)
        {
            cicloActual.Add(verticeActual + 1);

            if (cicloActual.Count > 1 && verticeActual == verticeInicio)
            {
                ciclos.Add(new List<int>(cicloActual));
            }
            else
            {
                for (int i = 0; i < numVertices; i++)
                {
                    if (matrizAdyacencia[verticeActual, i] == 1 && (cicloActual.Count == 1 || i != verticeInicio))
                    {
                        EncontrarCiclosRecursivo(i, verticeInicio, cicloActual, ciclos);
                    }
                }
            }

            cicloActual.RemoveAt(cicloActual.Count - 1);
        }
    }
}

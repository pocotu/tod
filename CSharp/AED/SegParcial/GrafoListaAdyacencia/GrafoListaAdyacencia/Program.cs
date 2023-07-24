using System;

namespace Grafos
{
    class Program
    {
        static void Main()
        {
            // Crear un grafo utilizando listas de adyacencia
            GrafoLista grafoLista = new GrafoLista(5);
            grafoLista.AgregarArista(0, 1);
            grafoLista.AgregarArista(0, 4);
            grafoLista.AgregarArista(1, 2);
            grafoLista.AgregarArista(1, 3);
            grafoLista.AgregarArista(1, 4);
            grafoLista.AgregarArista(2, 3);
            grafoLista.AgregarArista(3, 4);

            Console.WriteLine("Grafo utilizando listas de adyacencia:");
            grafoLista.MostrarGrafo();

            Console.WriteLine();

            // Crear un grafo utilizando matriz de adyacencia
            GrafoMatriz grafoMatriz = new GrafoMatriz(5);
            grafoMatriz.AgregarArista(0, 1);
            grafoMatriz.AgregarArista(0, 4);
            grafoMatriz.AgregarArista(1, 2);
            grafoMatriz.AgregarArista(1, 3);
            grafoMatriz.AgregarArista(1, 4);
            grafoMatriz.AgregarArista(2, 3);
            grafoMatriz.AgregarArista(3, 4);

            Console.WriteLine("Grafo utilizando matriz de adyacencia:");
            grafoMatriz.MostrarGrafo();
        }
    }
}

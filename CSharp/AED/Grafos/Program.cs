using System;

namespace AppGrafo
{
    class Programa
    {
        static void Main(string[] args)
        {
            int[,] grafoInicial = {
                {0, 1, 0, 0},
                {0, 0, 1, 0},
                {1, 0, 0, 1},
                {0, 1, 0, 0}
            };

            Grafo grafo = new Grafo(grafoInicial.GetLength(0));
            grafo.CargarGrafo(grafoInicial);

            int opcion;
            do
            {
                Console.WriteLine("\nMenu:");
                Console.WriteLine("1. Agregar Arco");
                Console.WriteLine("2. Eliminar Arco");
                Console.WriteLine("3. Mostrar Grafo");
                Console.WriteLine("4. Mostrar Matriz de Adyacencia");
                Console.WriteLine("5. Verificar Simetría");
                Console.WriteLine("6. Encontrar Caminos");
                Console.WriteLine("7. Calcular Longitud de Camino");
                Console.WriteLine("8. Verificar Reflexividad");
                Console.WriteLine("9. Encontrar Ciclos");
                Console.Write("Ingrese su opcion: ");
                opcion = int.Parse(Console.ReadLine());

                switch (opcion)
                {
                    case 1:
                        Console.Write("Ingrese vertice de inicio: ");
                        int verticeInicio = int.Parse(Console.ReadLine());
                        Console.Write("Ingrese vertice de fin: ");
                        int verticeFin = int.Parse(Console.ReadLine());
                        grafo.AgregarArco(verticeInicio, verticeFin);
                        break;

                    case 2:
                        Console.Write("Ingrese vertice de inicio: ");
                        verticeInicio = int.Parse(Console.ReadLine());
                        Console.Write("Ingrese vértice de fin: ");
                        verticeFin = int.Parse(Console.ReadLine());
                        grafo.EliminarArco(verticeInicio, verticeFin);
                        break;

                    case 3:
                        grafo.MostrarGrafo();
                        break;

                    case 4:
                        grafo.MostrarMatrizAdyacencia();
                        break;

                    case 5:
                        Console.WriteLine("El grafo es simetrico: " + grafo.EsSimetrico());
                        break;

                    case 6:
                        Console.Write("Ingrese vertice de inicio: ");
                        verticeInicio = int.Parse(Console.ReadLine());
                        Console.Write("Ingrese vertice de fin: ");
                        verticeFin = int.Parse(Console.ReadLine());
                        var caminos = grafo.EncontrarCaminos(verticeInicio, verticeFin);
                        Console.WriteLine("Caminos posibles:");
                        foreach (var camino in caminos)
                        {
                            Console.WriteLine(string.Join(" -> ", camino));
                        }
                        break;

                    case 7:
                        Console.Write("Ingrese vertice de inicio: ");
                        int verticeInicioLongitud = int.Parse(Console.ReadLine());
                        Console.Write("Ingrese vertice de fin: ");
                        int verticeFinLongitud = int.Parse(Console.ReadLine());
                        var caminosLongitud = grafo.EncontrarCaminos(verticeInicioLongitud, verticeFinLongitud);
                        Console.WriteLine("Caminos posibles:");
                        foreach (var camino in caminosLongitud)
                        {
                            Console.WriteLine("Camino: " + string.Join(" -> ", camino));
                            int longitud = grafo.CalcularLongitudCamino(camino);
                            Console.WriteLine("Longitud: " + longitud);
                        }
                        break;

                    case 8:
                        Console.WriteLine("El grafo es reflexivo: " + grafo.EsReflexivo());
                        break;

                    case 9:
                        Console.Write("Ingrese vertice para encontrar ciclos: ");
                        int verticeCiclo = int.Parse(Console.ReadLine());
                        var ciclos = grafo.EncontrarCiclos(verticeCiclo);
                        Console.WriteLine("Ciclos posibles:");
                        foreach (var ciclo in ciclos)
                        {
                            Console.WriteLine(string.Join(" -> ", ciclo));
                        }
                        break;

                    default:
                        Console.WriteLine("Opción invalida.");
                        break;
                }

            } while (opcion != 0);
        }
    }
}
